#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

python3 -B verify.py --output results/verification.json
python3 -B -m unittest discover -s tests -v
python3 -B - <<'PY'
from pathlib import Path
for rel in ["verify.py", "tests/test_verify.py"]:
    src = Path(rel).read_text(encoding="utf-8")
    compile(src, rel, "exec")
print("PASS_T99000_PYTHON_SYNTAX_CHECK")
PY
sha256sum -c SHA256SUMS

if [[ "${FULL:-0}" == "1" ]]; then
  BIN="$(mktemp)"
  OUT="$(mktemp)"
  trap 'rm -f "$BIN" "$OUT"' EXIT
  g++ -O3 -std=c++17 src/scan_cprefix_exact.cpp -o "$BIN"
  "$BIN" 1000000000 40 > "$OUT"
  cmp "$OUT" results/cprefix_exact_1e9.txt
  echo PASS_T99000_FULL_BILLION_REGENERATION
fi

echo PASS_T99000_FULL_REPLAY
