#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "[+] Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

echo "[+] Installing dependencies..."
"$VENV_DIR/bin/pip" install -r "$PROJECT_DIR/requirements.txt"

echo "[+] Starting Red-Grid..."
"$VENV_DIR/bin/python" "$PROJECT_DIR/malware_simulation_lab.py"
