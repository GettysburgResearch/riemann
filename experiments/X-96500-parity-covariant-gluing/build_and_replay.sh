#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p results build
c++ -O2 -std=c++20 -I src src/fixed_depth_star_mpfr.cpp \
  -o build/fixed_depth_star_mpfr -Wl,-l:libmpfr.so.6 -lgmp
./build/fixed_depth_star_mpfr > results/fixed-depth-star.json
python3 verify.py
