#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 experiments/X-105520-physical-wick/verify.py \
  --output experiments/X-105520-physical-wick/results/verification.json
python3 -m unittest experiments/X-105520-physical-wick/tests/test_verify.py
