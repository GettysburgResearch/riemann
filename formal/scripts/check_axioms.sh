#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FORMAL="$ROOT/formal"
cd "$FORMAL"

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

SOURCES=(RiemannFormal/AxiomAudit.lean)
lake env lean RiemannFormal/AxiomAudit.lean >"$TMP"

# Compile and audit every comparator print module.  This automatically includes
# future A/B topics without requiring a shared hard-coded declaration list.
while IFS= read -r file; do
  SOURCES+=("$file")
  lake env lean "$file" >>"$TMP"
done < <(find comparator/PrintAxioms -maxdepth 1 -type f -name '*.lean' | sort)

python3 scripts/audit_axiom_output.py "$TMP" "${SOURCES[@]}"
