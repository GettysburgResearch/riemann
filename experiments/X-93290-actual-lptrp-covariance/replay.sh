#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
c++ -O3 -std=c++17 -Wall -Wextra "$HERE/certify_rows.cpp" -o "$TMP/certify_rows"
"$TMP/certify_rows" 100000000 "$TMP/row-certificate-100m.json"
cmp "$TMP/row-certificate-100m.json" "$HERE/results/row-certificate-100m.json"
python3 "$HERE/verify.py" --json "$TMP/verification.json"
cmp "$TMP/verification.json" "$HERE/results/verification.json"
(cd "$HERE" && sha256sum -c SHA256SUMS)
echo PASS_X_93290_FULL_REPLAY
