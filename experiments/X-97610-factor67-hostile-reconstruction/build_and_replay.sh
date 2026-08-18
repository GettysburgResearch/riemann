#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_scalar_algebra.py
python3 verify_x184.py
python3 verify_interfaces.py
CXX=${CXX:-g++}
"$CXX" -O3 -std=c++17 -fno-fast-math -ffp-contract=off -Isrc \
  src/certify_p61_bias.cpp -Wl,-l:libmpfr.so.6 -lgmp -o certify_p61_bias
./certify_p61_bias results/p61_bias_verification.json
rm -f certify_p61_bias
printf '%s\n' PASS_X_97610_FACTOR67_HOSTILE_RECONSTRUCTION
