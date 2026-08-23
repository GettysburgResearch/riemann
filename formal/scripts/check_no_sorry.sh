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

echo PASS_FORMAL_NO_SORRY_OR_CUSTOM_AXIOM
