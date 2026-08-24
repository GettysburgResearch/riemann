#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -B verify.py --output /tmp/t105550-verification.json
cmp /tmp/t105550-verification.json results/verification.json
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
