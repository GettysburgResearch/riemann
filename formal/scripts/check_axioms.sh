#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$(mktemp)"
DECLARED="$(mktemp)"
DISCOVERED="$(mktemp)"
trap 'rm -f "$OUT" "$DECLARED" "$DISCOVERED"' EXIT

cd "$ROOT/formal"

MANIFEST="scripts/axiom_print_modules.txt"
PYTHON="${PYTHON:-python3}"
test -f "$MANIFEST" || { echo "missing axiom-print manifest: $MANIFEST" >&2; exit 1; }

awk 'NF && $1 !~ /^#/' "$MANIFEST" | LC_ALL=C sort > "$DECLARED"
if test -n "$(uniq -d "$DECLARED")"; then
  echo "duplicate entries in $MANIFEST" >&2
  uniq -d "$DECLARED" >&2
  exit 1
fi

{
  find RiemannFormal -type f -name 'AxiomAudit.lean' -print
  find comparator/PrintAxioms -maxdepth 1 -type f -name '*.lean' -print
} | LC_ALL=C sort > "$DISCOVERED"

if ! cmp -s "$DECLARED" "$DISCOVERED"; then
  echo "axiom-print manifest does not exactly match committed print modules" >&2
  diff -u "$DECLARED" "$DISCOVERED" >&2 || true
  exit 1
fi

mapfile -t files < "$DECLARED"
test "${#files[@]}" -gt 0 || { echo "empty axiom-print manifest" >&2; exit 1; }

lake -Kjobs="${LAKE_JOBS:-1}" build RiemannFormal RiemannComparatorSolution
{
  for path in "${files[@]}"; do
    test -f "$path" || { echo "missing axiom-print module: $path" >&2; exit 1; }
    lake env lean "$path"
  done
} 2>&1 | tee "$OUT"

"$PYTHON" "$ROOT/formal/scripts/audit_axiom_output.py" "$OUT" "${files[@]}"
echo "PASS_FORMAL_AXIOM_AUDIT modules=${#files[@]}"
