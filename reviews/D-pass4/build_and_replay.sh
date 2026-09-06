#!/usr/bin/env bash
# No privileged workflow, network access, or repository secrets are needed.
set -euo pipefail
cd "$(dirname "$0")"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
# Vendor mpfr.h is preferred; the local fallback is for the tested 64-bit MPFR4 ABI.
${CXX:-g++} -std=c++17 -O2 p61_replay.cpp -Wl,-l:libmpfr.so.6 -lgmp -o "$TMP/p61"
"$TMP/p61" "$TMP/p61.json"
cmp "$TMP/p61.json" p61.full.json
${CXX:-g++} -std=c++17 -O2 constant_audit.cpp -Wl,-l:libmpfr.so.6 -lgmp -o "$TMP/c0"
"$TMP/c0" > "$TMP/constant.json"
cmp "$TMP/constant.json" constant.audit.json
python3 checks.py --compare checks.normal.json --output "$TMP/normal.json"
python3 -O checks.py --compare checks.optimized.json --output "$TMP/optimized.json"
cmp "$TMP/normal.json" "$TMP/optimized.json"
python3 rejections.py
python3 validate.py
printf '%s\n' PASS_D4_FULL_REPLAY
