#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FORMAL="$ROOT/formal"
OUT="$(mktemp)"
DECLARED="$(mktemp)"
DISCOVERED="$(mktemp)"
REGISTRY_AUDIT="$(mktemp "$FORMAL/.formal_v0_1_registry_axioms.XXXXXX.lean")"
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
test "${#files[@]}" -eq 9 || {
  echo "expected exactly nine committed axiom-print modules, found ${#files[@]}" >&2
  exit 1
}

"$PYTHON" - "$REGISTRY_AUDIT" <<'PY'
import csv
import sys
from pathlib import Path

out = Path(sys.argv[1])
root = Path.cwd()
paths = [
    root / "registry" / "deltas" / "A.tsv",
    root / "registry" / "deltas" / "B.tsv",
    root / "registry" / "deltas" / "C.tsv",
    root / "registry" / "deltas" / "C_API.tsv",
]
declarations: list[str] = []
for path in paths:
    if not path.is_file():
        raise SystemExit(f"missing formal delta: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            declaration = row.get("lean_declaration", "").strip()
            if declaration:
                declarations.append(declaration)
declarations = list(dict.fromkeys(declarations))
if not declarations:
    raise SystemExit("no registry declarations found")
out.write_text(
    "import RiemannFormal\n\n"
    + "\n".join(f"#print axioms {name}" for name in declarations)
    + "\n",
    encoding="utf-8",
)
print(f"GENERATED_FORMAL_V0_1_AXIOM_AUDIT declarations={len(declarations)}")
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
"$PYTHON" scripts/test_audit_axiom_output.py
mkdir -p reports/generated
cp "$OUT" reports/generated/FORMAL_V0_1_AXIOM_OUTPUT.txt
echo "PASS_FORMAL_V0_1_AXIOM_AUDIT modules=${#files[@]} registry_complete=true"
