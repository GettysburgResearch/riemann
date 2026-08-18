#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify.py"
python3 "$HERE/tests/test_mutations.py"
g++ -O3 -DNDEBUG -std=c++17 "$HERE/src/scan_p67_ratio.cpp" -o /tmp/t98070_scan_p67
/tmp/t98070_scan_p67 1000000 /tmp/t98070_p67_smoke.json >/tmp/t98070_p67_smoke.txt
cmp /tmp/t98070_p67_smoke.json "$HERE/results/p67_ratio_scan_smoke_1e6.json"
echo PASS_T98070_FULL_REPLAY
