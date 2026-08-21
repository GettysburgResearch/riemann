#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 experiments/X-101500-compensated-matrix/verify.py
cmp experiments/X-101500-compensated-matrix/results/verification.json \
    experiments/X-101500-compensated-matrix/results/verification.json
sha256sum -c T101500_CONTENT_SHA256SUMS
