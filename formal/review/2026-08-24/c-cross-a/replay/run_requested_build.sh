#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-$(pwd)}"
TARGET="92f70a3b49b9295b5efb88491107670065b03317"
BOOTSTRAP="573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f"

cd "$ROOT"
test "$(git rev-parse "$TARGET^{commit}")" = "$TARGET"
test "$(git merge-base "$BOOTSTRAP" "$TARGET")" = "$BOOTSTRAP"

tmp="$(mktemp -d)"
trap 'git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"' EXIT
git worktree add --detach "$tmp" "$TARGET"
cd "$tmp/formal"

lake exe cache get
lake build
lake build Challenge.MellinAPI Solution.MellinAPI

python3 scripts/generate_registry.py
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
python3 scripts/validate_blueprint.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh
