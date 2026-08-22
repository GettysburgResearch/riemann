#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -B verify.py --output results/verification.json
python -B -m unittest discover -s tests -p 'test_*.py' -v
