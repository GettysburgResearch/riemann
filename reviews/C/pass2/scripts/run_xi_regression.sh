#!/usr/bin/env bash
# NOT RUN IN REVIEWER C'S PASS. Run only in a disposable, pinned repository checkout.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
SOURCE="formal/comparator/ChallengeDeps/RiemannComparatorChallengeDeps/XiPickOrderThreeConditional.lean"
EXPECTED="7d3dd6c98fd453d1810d80b0e1a39e2e4fbc7ab5"
ACTUAL="$(git hash-object "$ROOT/$SOURCE")"
if [[ "$ACTUAL" != "$EXPECTED" ]]; then
  printf 'Refusing different shared-source blob: %s\n' "$ACTUAL" >&2
  exit 1
fi
command -v lake >/dev/null || { echo 'lake is required; no automatic installer' >&2; exit 1; }
cd "$ROOT/formal"
lake build RiemannComparatorChallengeDeps.XiPickOrderThreeConditional
lake env lean ../reviews/C/pass2/lean/XiInputNonvacuity.lean
