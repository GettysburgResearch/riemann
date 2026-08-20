#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 experiments/X-101100-implication-matrix/verify.py \
  --output experiments/X-101100-implication-matrix/results/verification.json
python3 -m unittest discover -s experiments/X-101100-implication-matrix/tests -v
sha256sum -c T101100_CONTENT_SHA256SUMS
