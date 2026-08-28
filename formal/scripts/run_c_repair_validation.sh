#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
JOBS="${LAKE_JOBS:-1}"
cd "$ROOT/formal"

lake -Kjobs="$JOBS" exe cache get
lake -Kjobs="$JOBS" build

lake -Kjobs="$JOBS" build \
  RiemannComparatorChallenge.XiPickThreeNode \
  RiemannComparatorSolution.XiPickThreeNode
lake -Kjobs="$JOBS" build \
  RiemannComparatorChallenge.OperatorPositiveSchurRescue \
  RiemannComparatorSolution.OperatorPositiveSchurRescue
lake -Kjobs="$JOBS" build \
  RiemannComparatorChallenge.XiPickOrderThreeConditional \
  RiemannComparatorSolution.XiPickOrderThreeConditional

python3 scripts/generate_registry.py
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
python3 scripts/validate_blueprint.py
python3 scripts/verify_declaration_map.py
python3 scripts/check_statement_sources.py
python3 scripts/verify_c_repair_static.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh

echo PASS_REVIEWER_C_REPAIR_EXACT_HEAD_SUITE
