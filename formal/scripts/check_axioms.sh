#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT/formal"

lake env lean RiemannFormal/AxiomAudit.lean
lake env lean comparator/PrintAxioms/RH.lean

echo PASS_FORMAL_AXIOM_AUDIT
