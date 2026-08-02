#!/usr/bin/env python3
"""Invalidate generated data when the user's source package changes."""

import argparse
import hashlib
import json
import os
from pathlib import Path

EXTENSIONS = {".apk", ".xapk", ".apkm", ".apks", ".zip"}


def sampled_hash(path: Path, size: int) -> str:
    """Hash enough data to notice replacements without rereading multi-GB bundles."""
    digest = hashlib.sha256()
    window = 1024 * 1024
    with path.open("rb") as stream:
        digest.update(stream.read(window))
        if size > window:
            stream.seek(max(0, size - window))
            digest.update(stream.read(window))
    return digest.hexdigest()


def identity(game_dir: Path, recipe: Path) -> dict:
    files = []
    for path in sorted((game_dir / "gamedata").iterdir(), key=lambda p: p.name.casefold()):
        if path.name == "runtime.apk" or not path.is_file() or path.is_symlink() or path.suffix.lower() not in EXTENSIONS:
            continue
        stat = path.stat()
        files.append({
            "name": path.name,
            "size": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "sample_sha256": sampled_hash(path, stat.st_size),
        })
    return {"schema": 1, "recipe_sha256": hashlib.sha256(recipe.read_bytes()).hexdigest(), "inputs": files}


def atomic_json(path: Path, data: dict) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.part")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("before", "record"))
    parser.add_argument("--game-dir", required=True, type=Path)
    parser.add_argument("--recipe", required=True, type=Path)
    args = parser.parse_args()
    game_dir = args.game_dir.resolve(strict=True)
    current = identity(game_dir, args.recipe.resolve(strict=True))
    marker = game_dir / ".gmloader-source.json"
    if args.mode == "record":
        atomic_json(marker, current)
        return 0
    try:
        previous = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        previous = None
    if previous != current:
        for path in (game_dir / "gamedata/runtime.apk", game_dir / ".nxextract-gmloader-runtime.json"):
            if path.is_file() and not path.is_symlink():
                path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
