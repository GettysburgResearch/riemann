#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py --output results/verification.json
cd ../..
sha256sum -c T99700_CONTENT_SHA256SUMS
