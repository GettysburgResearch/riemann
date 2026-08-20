#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 experiments/X-103100-fractional-hankel/verify.py \
  --output experiments/X-103100-fractional-hankel/results/verification.json
python3 -m unittest discover -s experiments/X-103100-fractional-hankel/tests -v
sha256sum -c T103100_CONTENT_SHA256SUMS
