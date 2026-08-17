#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

CXX=${CXX:-g++}
"$CXX" -O3 -std=c++17 -fno-fast-math -ffp-contract=off -Isrc \
  src/certify.cpp -Wl,-l:libmpfr.so.6 -lgmp -o certify

./certify results/verification.json
python3 verify_interfaces.py --output results/interface-verification.json
python3 make_proof_object.py
python3 -m py_compile verify_interfaces.py make_proof_object.py
sha256sum -c SHA256SUMS

echo PASS_T97400_FULL_REPLAY
