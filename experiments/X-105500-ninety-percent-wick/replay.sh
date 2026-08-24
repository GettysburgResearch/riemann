#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 experiments/X-105500-ninety-percent-wick/verify.py \
  --output experiments/X-105500-ninety-percent-wick/results/verification.json
python3 -m unittest discover \
  -s experiments/X-105500-ninety-percent-wick/tests \
  -p 'test_*.py'
