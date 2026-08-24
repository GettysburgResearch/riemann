#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT/formal"

TARGETS=(RiemannFormal comparator/Solution comparator/ChallengeDeps)

if grep -RInP --include='*.lean' '\b(sorry|admit)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target contains sorry/admit' >&2
  exit 1
fi

if grep -RInP --include='*.lean' '^\s*(axiom|opaque|unsafe)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target declares a custom axiom/opaque/unsafe constant' >&2
  exit 1
fi

if grep -RInP --include='*.lean' '\b(by\?|exact\?|apply\?|simp\?|aesop\?)\b' "${TARGETS[@]}"; then
  echo 'trusted formal target contains an unresolved tactic suggestion' >&2
  exit 1
fi

# Reviewer C challenge files each contain exactly one statement-only placeholder;
# corresponding ChallengeDeps and Solution files contain none and compile.
shopt -s nullglob
for challenge in comparator/Challenge/{XiPick,Operator,Refutation}*.lean; do
  count="$(grep -Ec '\b(sorry|admit)\b' "$challenge" || true)"
  if [[ "$count" -ne 1 ]]; then
    echo "trusted challenge must contain exactly one placeholder: $challenge ($count)" >&2
    exit 1
  fi
  topic="$(basename "$challenge")"
  stem="${topic%.lean}"
  solution="comparator/Solution/$topic"
  deps="comparator/ChallengeDeps/$topic"
  if [[ ! -f "$solution" || ! -f "$deps" ]]; then
    echo "missing comparator dependency or solution for $challenge" >&2
    exit 1
  fi
  if grep -EIn '\b(sorry|admit)\b|^\s*(axiom|opaque|unsafe)\b' "$solution" "$deps"; then
    echo "trusted comparator dependency/solution is not clean: $topic" >&2
    exit 1
  fi
  lake build "Challenge.${stem}" "Solution.${stem}"
done

python3 scripts/verify_declaration_map.py
python3 scripts/check_statement_sources.py
python3 scripts/check_external_input_usage.py
python3 scripts/verify_comparator_fidelity.py

echo PASS_FORMAL_NO_SORRY_OR_CUSTOM_AXIOM
