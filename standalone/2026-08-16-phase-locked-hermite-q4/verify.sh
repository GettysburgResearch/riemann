#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT/experiments/X-94050-phase-locked-hermite-q4"
python3 verify.py --json /tmp/x94050-verification.json
cmp /tmp/x94050-verification.json results/verification.json
sha256sum -c SHA256SUMS
cd "$ROOT"
sha256sum -c integration/gpt56-pro-94050-content-sha256.txt
printf '%s\n' PASS_STANDALONE_94050_PACKET
