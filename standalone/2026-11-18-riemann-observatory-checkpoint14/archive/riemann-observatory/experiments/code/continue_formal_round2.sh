#!/usr/bin/env bash
# Invoke after checking no earlier RankTrace lake build is still running.
set -euo pipefail
observatory_root=$(cd -- "$(dirname -- "$0")/../.." && pwd)
formal_base="$observatory_root/sources/formal_round2"
export ELAN_HOME="$formal_base/elan"
export PATH="$ELAN_HOME/bin:$PATH"
export LEAN_NUM_THREADS=4
cd "$formal_base/zeta-23-lean-v1.0"
lake --no-cache build Zeta23.LinAlg.RankTrace
lake env lean "$observatory_root/experiments/code/FormalRound2Axioms.lean"
# Full headline verification is a separate, potentially long task:
# lake --no-cache build Solution.Multiplicity
# lake env lean comparator/PrintAxioms/Multiplicity.lean
