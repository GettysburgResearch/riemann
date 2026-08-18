#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
python3 "$ROOT/experiments/X-97500-resolvent-transfer/verify.py" \
  --output "$ROOT/experiments/X-97500-resolvent-transfer/results/verification.json"
python3 -m pytest -q "$ROOT/experiments/X-97500-resolvent-transfer/tests"
"$(dirname "$0")/build.sh"
cd "$ROOT"
sha256sum -c T97500_GITHUB_TEXT_SHA256SUMS
