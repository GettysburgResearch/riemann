#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$(mktemp)"
trap 'rm -f "$OUT"' EXIT

cd "$ROOT/formal"
{
  lake env lean RiemannFormal/AxiomAudit.lean
  lake env lean comparator/PrintAxioms/RH.lean
} 2>&1 | tee "$OUT"

python3 "$ROOT/formal/scripts/audit_axiom_output.py" "$OUT"
echo PASS_FORMAL_AXIOM_AUDIT
