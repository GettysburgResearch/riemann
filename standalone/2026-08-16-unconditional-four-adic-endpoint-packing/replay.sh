#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
