#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FORMAL="$ROOT/formal"
cd "$FORMAL"

OUT="$(mktemp)"
REGISTRY_AUDIT="$(mktemp --suffix=.lean -p "$FORMAL")"
trap 'rm -f "$OUT" "$REGISTRY_AUDIT"' EXIT

python3 - "$REGISTRY_AUDIT" <<'PY'
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
    "import RiemannFormal\n\n" +
    "\n".join(f"#print axioms {name}" for name in declarations) + "\n",
    encoding="utf-8",
)
print(f"GENERATED_C_AXIOM_AUDIT declarations={len(declarations)}")
PY

SOURCES=(RiemannFormal/AxiomAudit.lean "$REGISTRY_AUDIT")
{
  lake env lean RiemannFormal/AxiomAudit.lean
  lake env lean "$(basename "$REGISTRY_AUDIT")"
  while IFS= read -r file; do
    SOURCES+=("$file")
    lake env lean "$file"
  done < <(find comparator/PrintAxioms -maxdepth 1 -type f -name '*.lean' | sort)
} 2>&1 | tee "$OUT"

python3 scripts/audit_axiom_output.py "$OUT" "${SOURCES[@]}"
mkdir -p reports/generated
cp "$OUT" reports/generated/C_AXIOM_OUTPUT.txt

echo PASS_FORMAL_AXIOM_AUDIT_REGISTRY_COMPLETE
