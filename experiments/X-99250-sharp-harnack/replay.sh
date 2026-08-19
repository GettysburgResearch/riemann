#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" == "--full" ]]; then
  python3 verify.py --full-scan
else
  python3 verify.py
fi
