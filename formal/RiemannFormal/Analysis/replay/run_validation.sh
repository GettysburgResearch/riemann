#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(git rev-parse --show-toplevel)}"
cd "$ROOT/formal"

start="$(date +%s)"

lake exe cache get
lake build
lake build Challenge.MellinAPI Solution.MellinAPI

python3 scripts/generate_registry.py
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
python3 scripts/validate_blueprint.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh

end="$(date +%s)"
echo "PASS_ANALYSIS_REPAIR_VALIDATION duration_seconds=$((end-start))"
