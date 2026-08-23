#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT/formal"

if grep -RInE --include='*.lean' '\b(sorry|admit)\b' \
  RiemannFormal comparator/Solution comparator/ChallengeDeps; then
  echo 'trusted formal target contains sorry/admit' >&2
  exit 1
fi

echo PASS_FORMAL_NO_SORRY
