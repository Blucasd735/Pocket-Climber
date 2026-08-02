#!/usr/bin/env python3
"""NXExtract hook that constructs a single GMloader-compatible runtime APK."""

from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import zipfile

CHUNK = 1024 * 1024
INPUTS = {".apk", ".xapk", ".apkm", ".apks", ".zip"}
BUNDLES = {".xapk", ".apkm", ".apks", ".zip"}
MAX_MEMBER = 2 * 1024**3
MAX_TOTAL = 6 * 1024**3


class PrepError(RuntimeError):
    pass


def report(done: int, total: int, detail: str) -> None:
    print(f"NXEXTRACT_PROGRESS {done} {total} {detail}", flush=True)


def safe_name(name: str) -> str:
    value = name.replace("\\", "/")
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts:
        raise PrepError(f"unsafe archive member: {name}")
    return str(path)


def is_apk(path: Path) -> bool:
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
        return "AndroidManifest.xml" in names or "assets/game.droid" in names
    except (OSError, zipfile.BadZipFile):
        return False


def discover(game_dir: Path) -> list[Path]:
    folder = game_dir / "gamedata"
    found = []
    for path in sorted(folder.iterdir(), key=lambda p: p.name.casefold()):
        if path.name == "runtime.apk" or not path.is_file() or path.is_symlink():
            continue
        if path.suffix.lower() in INPUTS:
            found.append(path)
    if not found:
        raise PrepError("place one APK/XAPK/APKM/APKS/ZIP in gamedata")
    return found


def unpack_sources(inputs: list[Path], temporary: Path) -> list[Path]:
    apks: list[Path] = []
    expanded = 0
    for source in inputs:
        if is_apk(source):
            apks.append(source)
            continue
        if source.suffix.lower() not in BUNDLES:
            raise PrepError(f"invalid APK: {source.name}")
        try:
            archive = zipfile.ZipFile(source)
        except (OSError, zipfile.BadZipFile) as error:
            raise PrepError(f"invalid bundle {source.name}: {error}") from error
        with archive:
            members = [i for i in archive.infolist() if not i.is_dir() and i.filename.lower().endswith(".apk")]
            if not members:
                raise PrepError(f"bundle contains no APK: {source.name}")
            for info in members:
                safe_name(info.filename)
                if info.flag_bits & 1 or info.file_size <= 0 or info.file_size > MAX_MEMBER:
                    raise PrepError(f"unsafe split APK: {info.filename}")
                expanded += info.file_size
                if expanded > MAX_TOTAL:
                    raise PrepError("expanded bundle exceeds safety limit")
                target = temporary / f"{len(apks):03d}-{PurePosixPath(info.filename).name}"
                with archive.open(info) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst, CHUNK)
                apks.append(target)
    return apks


def entries(path: Path) -> set[str]:
    try:
        with zipfile.ZipFile(path) as archive:
            return {safe_name(i.filename) for i in archive.infolist() if not i.is_dir()}
    except (OSError, zipfile.BadZipFile) as error:
        raise PrepError(f"invalid APK {path.name}: {error}") from error


def choose(apks: list[Path], abi: str) -> tuple[Path, list[Path]]:
    catalog = {path: entries(path) for path in apks}
    ranked = []
    for path, names in catalog.items():
        score = 200 * ("assets/game.droid" in names) + 30 * ("AndroidManifest.xml" in names)
        score += 40 * (path.name.casefold() in {"base.apk", "universal.apk"})
        score -= 100 * ("config." in path.name.casefold() or "split" in path.name.casefold())
        ranked.append((score, path.stat().st_size, path.name, path))
    ranked.sort(reverse=True)
    if not ranked or ranked[0][0] < 200:
        raise PrepError("could not find a GameMaker base APK with assets/game.droid")
    base = ranked[0][3]
    prefix = f"lib/{abi}/"
    providers = [path for path, names in catalog.items() if any(n.startswith(prefix) for n in names)]
    if not any(f"lib/{abi}/libyoyo.so" in catalog[path] for path in providers):
        raise PrepError(f"package does not contain lib/{abi}/libyoyo.so")
    return base, providers


def copy_entry(source: zipfile.ZipFile, info: zipfile.ZipInfo, target: zipfile.ZipFile) -> None:
    name = safe_name(info.filename)
    if info.is_dir() or info.file_size > MAX_MEMBER or info.flag_bits & 1:
        return
    if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
        raise PrepError(f"unsupported compression for {name}")
    clone = zipfile.ZipInfo(name, info.date_time)
    clone.compress_type = info.compress_type
    clone.external_attr = info.external_attr
    clone.create_system = info.create_system
    with source.open(info) as src, target.open(clone, "w", force_zip64=True) as dst:
        shutil.copyfileobj(src, dst, CHUNK)


def build(base: Path, providers: list[Path], output: Path, abi: str) -> None:
    prefix = f"lib/{abi}/"
    written: set[str] = set()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", allowZip64=True) as target:
        with zipfile.ZipFile(base) as source:
            for info in source.infolist():
                name = safe_name(info.filename)
                if name.startswith("lib/") and not name.startswith(prefix):
                    continue
                if name in written or info.is_dir():
                    continue
                copy_entry(source, info, target)
                written.add(name)
        for provider in providers:
            if provider == base:
                continue
            with zipfile.ZipFile(provider) as source:
                for info in source.infolist():
                    name = safe_name(info.filename)
                    if not name.startswith(prefix) or name in written or info.is_dir():
                        continue
                    copy_entry(source, info, target)
                    written.add(name)


def validate(path: Path, abi: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        bad = archive.testzip()
    required = {"assets/game.droid", f"lib/{abi}/libyoyo.so"}
    missing = sorted(required - names)
    if bad or missing:
        raise PrepError("runtime validation failed: " + (bad or ", ".join(missing)))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--game-dir", required=True, type=Path)
    parser.add_argument("--stage", required=True, type=Path)
    parser.add_argument("--abi", required=True)
    args = parser.parse_args()
    try:
        game_dir = args.game_dir.resolve(strict=True)
        output = args.stage / "gamedata/runtime.apk"
        report(0, 100, "LOCALIZANDO APK/XAPK")
        inputs = discover(game_dir)
        workspace = Path(os.environ.get("NXEXTRACT_WORKSPACE", args.stage))
        with tempfile.TemporaryDirectory(prefix="gmloader-hook-", dir=workspace) as temp_name:
            apks = unpack_sources(inputs, Path(temp_name))
            report(20, 100, "SELECIONANDO APK BASE E SPLIT")
            base, providers = choose(apks, args.abi)
            report(40, 100, f"CRIANDO RUNTIME {args.abi}")
            build(base, providers, output, args.abi)
        report(90, 100, "VALIDANDO RUNTIME")
        validate(output, args.abi)
        report(100, 100, "APK PRONTO")
        return 0
    except (OSError, PrepError, zipfile.BadZipFile) as error:
        print(f"gmloader prepare: ERROR: {error}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

