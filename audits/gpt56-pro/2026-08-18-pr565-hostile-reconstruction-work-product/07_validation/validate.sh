#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
sha256sum -c SHA256SUMS
python3 03_evidence/code/reproduce_x184.py > /tmp/x184.json
python3 03_evidence/code/mutation_tests.py > /tmp/mutations.json
g++ -O3 -std=c++17 -Wall -Wextra -pedantic 03_evidence/code/scan_p61_bias_corrected.cpp -o /tmp/scan_p61_bias_corrected
/tmp/scan_p61_bias_corrected 1000000 > /tmp/scan_1m.txt
grep -q '^argmin_42F_minus_M=184$' /tmp/scan_1m.txt
grep -q '^argmin_M_minus_20F=67$' /tmp/scan_1m.txt
python3 02_original_recovery_packet/extracted/riemann-parity-contractive-annular-97100-recovery/experiments/X-97100-parity-contraction/verify.py >/tmp/original_checker.txt
python3 - <<'PY'
import json
p='02_original_recovery_packet/extracted/riemann-parity-contractive-annular-97100-recovery/experiments/X-97100-parity-contraction/results/verification.json'
r=json.load(open(p))
assert r['bias_contract']['directed_certificate_replayed_here'] is False
assert r['rh_established'] is False
print('scope_guard=PASS')
PY
echo WORK_PRODUCT_VALIDATION_PASS
