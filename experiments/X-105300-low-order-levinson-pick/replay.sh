#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python -B experiments/X-105300-low-order-levinson-pick/verify.py \
  --output experiments/X-105300-low-order-levinson-pick/results/verification.json
python -B -m unittest discover \
  -s experiments/X-105300-low-order-levinson-pick/tests \
  -p 'test_*.py' -v
sha256sum -c T105300_CONTENT_SHA256SUMS
