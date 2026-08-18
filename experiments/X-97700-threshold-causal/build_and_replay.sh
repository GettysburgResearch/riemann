#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
g++ -std=c++17 -O2 -frounding-math -fno-fast-math \
  src/certify.cpp /lib/x86_64-linux-gnu/libmpfr.so.6 -lgmp -o /tmp/t97700-certify
/tmp/t97700-certify results/finite-certificates.json
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
if [[ -f SHA256SUMS ]]; then sha256sum -c SHA256SUMS; fi
