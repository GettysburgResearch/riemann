#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FORMAL="$ROOT/formal"
JOBS="${LAKE_JOBS:-1}"

cd "$ROOT"
python3 formal/scripts/generate_registry.py
python3 formal/scripts/validate_registry.py
python3 formal/scripts/verify_source_locks.py
python3 formal/scripts/validate_blueprint.py
python3 formal/scripts/verify_formal_v0_1_release.py

cd "$FORMAL"
lake -Kjobs="$JOBS" build
lake -Kjobs="$JOBS" build RiemannFormal.Release
bash scripts/build_local_comparators.sh
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh
python3 scripts/verify_all_comparator_types.py --repo "$ROOT"

cd "$ROOT"
python3 formal/scripts/generate_registry.py
python3 formal/scripts/validate_registry.py
python3 formal/scripts/verify_source_locks.py
python3 formal/scripts/validate_blueprint.py
python3 formal/scripts/verify_formal_v0_1_release.py

echo PASS_EXACT_FORMAL_V0_1_PACKAGE
