#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
python -B experiments/X-105320-wick-pick/verify.py --output "$TMP"
cmp "$TMP" experiments/X-105320-wick-pick/results/verification.json
python -B -m unittest discover -s experiments/X-105320-wick-pick/tests -p 'test_*.py' -v
sha256sum -c T105320_CONTENT_SHA256SUMS
