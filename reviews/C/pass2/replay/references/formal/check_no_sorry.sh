#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
JOBS="${LAKE_JOBS:-1}"
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

python3 scripts/verify_all_comparator_types.py --self-test
python3 scripts/verify_all_comparator_types.py --repo "$ROOT" --preflight

shopt -s nullglob
challenges=(comparator/Challenge/RiemannComparatorChallenge/*.lean)
if [[ "${#challenges[@]}" -ne 7 ]]; then
  echo "expected exactly seven Challenge topics, found ${#challenges[@]}" >&2
  exit 1
fi

for challenge in "${challenges[@]}"; do
  topic="$(basename "$challenge")"
  stem="${topic%.lean}"
  solution="comparator/Solution/RiemannComparatorSolution/$topic"
  deps="comparator/ChallengeDeps/RiemannComparatorChallengeDeps/$topic"
  if [[ ! -f "$solution" || ! -f "$deps" ]]; then
    echo "missing comparator dependency or solution for $challenge" >&2
    exit 1
  fi
  if grep -EIn '\b(sorry|admit)\b|^\s*(axiom|opaque|unsafe)\b' "$solution" "$deps"; then
    echo "trusted comparator dependency/solution is not clean: $topic" >&2
    exit 1
  fi
  lake -Kjobs="$JOBS" build \
    "RiemannComparatorChallengeDeps.${stem}" \
    "RiemannComparatorChallenge.${stem}" \
    "RiemannComparatorSolution.${stem}"
done

python3 scripts/verify_declaration_map.py
python3 scripts/check_statement_sources.py
python3 scripts/check_external_input_usage.py
python3 scripts/verify_comparator_fidelity.py

echo PASS_FORMAL_V0_1_NO_SORRY_OR_CUSTOM_AXIOM topics=7
