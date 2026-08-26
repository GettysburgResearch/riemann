#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FORMAL="$ROOT/formal"
OUT="$(mktemp)"
DECLARED="$(mktemp)"
DISCOVERED="$(mktemp)"
REGISTRY_AUDIT="$(mktemp --suffix=.lean -p "$FORMAL")"
trap 'rm -f "$OUT" "$DECLARED" "$DISCOVERED" "$REGISTRY_AUDIT"' EXIT

cd "$FORMAL"

MANIFEST="scripts/axiom_print_modules.txt"
PYTHON="${PYTHON:-python3}"
JOBS="${LAKE_JOBS:-1}"
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

"$PYTHON" - "$REGISTRY_AUDIT" <<'PY'
import csv
import sys
from pathlib import Path

out = Path(sys.argv[1])
root = Path.cwd()
paths = [
    root / "registry" / "deltas" / "C.tsv",
    root / "registry" / "deltas" / "C_API.tsv",
]
declarations = []
for path in paths:
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            declarations.append(row["lean_declaration"].strip())
declarations = list(dict.fromkeys(declarations))
out.write_text(
    "import RiemannFormal\n\n"
    + "\n".join(f"#print axioms {name}" for name in declarations)
    + "\n",
    encoding="utf-8",
)
print(f"GENERATED_C_AXIOM_AUDIT declarations={len(declarations)}")
PY

sources=("${files[@]}" "$REGISTRY_AUDIT")

lake -Kjobs="$JOBS" build RiemannFormal RiemannComparatorSolution
{
  for path in "${files[@]}"; do
    test -f "$path" || { echo "missing axiom-print module: $path" >&2; exit 1; }
    lake env lean "$path"
  done
  lake env lean "$(basename "$REGISTRY_AUDIT")"
} 2>&1 | tee "$OUT"

"$PYTHON" scripts/audit_axiom_output.py "$OUT" "${sources[@]}"
mkdir -p reports/generated
cp "$OUT" reports/generated/C_AXIOM_OUTPUT.txt
echo "PASS_FORMAL_AXIOM_AUDIT modules=${#files[@]} registry_complete=true"
