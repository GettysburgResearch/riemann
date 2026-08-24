#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$(mktemp)"
trap 'rm -f "$OUT"' EXIT

cd "$ROOT/formal"
files=(
  "RiemannFormal/AxiomAudit.lean"
  "RiemannFormal/Analysis/AxiomAudit.lean"
)
while IFS= read -r path; do
  files+=("$path")
done < <(find comparator/PrintAxioms -maxdepth 1 -type f -name '*.lean' -print | sort)

{
  for path in "${files[@]}"; do
    test -f "$path" || { echo "missing axiom-print module: $path" >&2; exit 1; }
    lake env lean "$path"
  done
} 2>&1 | tee "$OUT"

python3 "$ROOT/formal/scripts/audit_axiom_output.py" "$OUT"
echo "PASS_FORMAL_AXIOM_AUDIT modules=${#files[@]}"
