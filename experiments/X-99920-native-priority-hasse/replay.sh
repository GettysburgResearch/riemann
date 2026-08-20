#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
cd ../..
sha256sum -c T99920_CONTENT_SHA256SUMS
