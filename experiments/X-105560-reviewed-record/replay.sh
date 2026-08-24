#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../.." && pwd)
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
python -B "$HERE/verify.py" --output "$TMP"
cmp "$TMP" "$HERE/results/verification.json"
python -B -m unittest discover -s "$HERE/tests" -p 'test_*.py' -v
(cd "$ROOT" && sha256sum -c T105560_CONTENT_SHA256SUMS)
echo PASS_T105560_FULL_REPLAY
