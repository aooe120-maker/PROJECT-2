#!/usr/bin/env bash
set -euo pipefail

ONEFILE=${ONEFILE:-0}

python3 -m pip install --upgrade pip wheel
python3 -m pip install pyinstaller pygame-ce

ARGS=(-y pyinstaller.spec)
if [[ "$ONEFILE" == "1" ]]; then
  ARGS=(--onefile "${ARGS[@]}")
fi

pyinstaller "${ARGS[@]}"

echo "\nBuild complete. Output: dist/DokiDoki"

