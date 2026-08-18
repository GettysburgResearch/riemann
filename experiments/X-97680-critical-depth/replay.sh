#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
echo PASS_T97680_FULL_REPLAY
