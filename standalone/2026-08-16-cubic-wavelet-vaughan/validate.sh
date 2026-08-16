#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT/experiments/X-93300-cubic-wavelet-vaughan"
python3 verify.py --output /tmp/x93300-verification.json
cmp /tmp/x93300-verification.json results/verification.json
python3 -m py_compile verify.py
cd "$ROOT"
sha256sum -c CUBIC_93300_SHA256SUMS
