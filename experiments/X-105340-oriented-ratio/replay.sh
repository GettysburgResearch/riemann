#!/usr/bin/env bash
set -euo pipefail
python -B experiments/X-105340-oriented-ratio/verify.py --output experiments/X-105340-oriented-ratio/results/verification.json
python -B -m unittest discover -s experiments/X-105340-oriented-ratio/tests -p 'test_*.py' -v
