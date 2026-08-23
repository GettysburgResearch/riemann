#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT/formal"

TARGETS=(RiemannFormal comparator/Solution comparator/ChallengeDeps)

if grep -RInP --include='*.lean' '\b(sorry|admit)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target contains sorry/admit' >&2
  exit 1
fi

if grep -RInP --include='*.lean' '^\s*(axiom|opaque)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target declares a custom axiom/opaque constant' >&2
  exit 1
fi

if grep -RInP --include='*.lean' '\b(by\?|exact\?|apply\?|simp\?|aesop\?)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target contains an unresolved tactic suggestion' >&2
  exit 1
fi

# Reviewer C owns these comparator prefixes.  Each trusted challenge must carry
# exactly one placeholder, while the corresponding solution must carry none.
shopt -s nullglob
for challenge in comparator/Challenge/{XiPick,Operator,Refutation}*.lean; do
  count="$(grep -Ec '\b(sorry|admit)\b' "$challenge" || true)"
  if [[ "$count" -ne 1 ]]; then
    echo "trusted challenge must contain exactly one placeholder: $challenge ($count)" >&2
    exit 1
  fi
  topic="$(basename "$challenge")"
  solution="comparator/Solution/$topic"
  if [[ ! -f "$solution" ]]; then
    echo "missing comparator solution for $challenge" >&2
    exit 1
  fi
  stem="${topic%.lean}"
  lake build "Challenge.${stem}" "Solution.${stem}"
done

python3 scripts/verify_declaration_map.py
python3 scripts/check_statement_sources.py

echo PASS_FORMAL_NO_SORRY_OR_CUSTOM_AXIOM
