#!/usr/bin/env bash
set -euo pipefail

GAME_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
PYTHON_BIN="${NXEXTRACT_PYTHON:-python3}"
RECIPE="${NXEXTRACT_RECIPE:-$GAME_DIR/extractor.json}"

"$PYTHON_BIN" "$GAME_DIR/tools/source_guard.py" before \
  --game-dir "$GAME_DIR" --recipe "$RECIPE"

"$PYTHON_BIN" "$GAME_DIR/nxextract.py" install \
  --recipe "$RECIPE" --game-dir "$GAME_DIR" "$@"

"$PYTHON_BIN" "$GAME_DIR/tools/source_guard.py" record \
  --game-dir "$GAME_DIR" --recipe "$RECIPE"

