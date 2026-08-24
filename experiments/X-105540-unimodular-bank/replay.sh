#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 experiments/X-105540-unimodular-bank/verify.py \
  --output experiments/X-105540-unimodular-bank/results/verification.json
python3 -m unittest experiments/X-105540-unimodular-bank/tests/test_verify.py
