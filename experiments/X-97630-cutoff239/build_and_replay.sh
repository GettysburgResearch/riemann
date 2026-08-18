#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py

if [[ "${RUN_RECONSTRUCTED_CPP:-0}" == "1" ]]; then
  g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off -Isrc \
    src/certify.cpp -Wl,-l:libmpfr.so.6 -lgmp -o certify
  ./certify results/mpfr-contract.json
fi

sha256sum -c SHA256SUMS
echo PASS_T97630_CUTOFF239_LIGHTWEIGHT_REPLAY
