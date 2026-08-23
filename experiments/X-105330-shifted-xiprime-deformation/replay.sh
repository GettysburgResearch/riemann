#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
python -B experiments/X-105330-shifted-xiprime-deformation/verify.py --output "$TMP"
cmp "$TMP" experiments/X-105330-shifted-xiprime-deformation/results/verification.json
python -B -m unittest discover -s experiments/X-105330-shifted-xiprime-deformation/tests -p 'test_*.py' -v
sha256sum -c T105330_CONTENT_SHA256SUMS
