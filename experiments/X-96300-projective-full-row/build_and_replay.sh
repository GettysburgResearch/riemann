#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE"
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
# Optional full tail rebuild (long):
# g++ -O3 -std=c++17 -frounding-math -fno-fast-math -Isrc src/directed_tail_mpfr_arith.cpp /lib/x86_64-linux-gnu/libmpfr.so.6 -lgmp -o /tmp/t96300-tail
# run disjoint row chunks 2..66, then aggregate with verify_aggregate.py.
