#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
JOBS="${LAKE_JOBS:-1}"

cd "$ROOT/formal"
lake -Kjobs="$JOBS" build \
  RiemannComparatorChallengeDeps \
  RiemannComparatorChallenge \
  RiemannComparatorSolution
