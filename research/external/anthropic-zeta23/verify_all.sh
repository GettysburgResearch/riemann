#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
OUT="$HERE/verification-results"
mkdir -p "$OUT"

python3 "$REPO/experiments/X-zeta23-constants/reproduce_constants.py" \
  --json "$OUT/constants.json"

python3 "$REPO/experiments/X-zeta23-multiplicity-frontier/frontier.py" \
  --max-multiplicity 12 \
  --json "$OUT/multiplicity.json"

python3 "$REPO/experiments/X-zeta23-rank-trace/stress_rank_trace.py" \
  --trials 1000 --dimension 16 --seed 20260810 \
  --json "$OUT/rank-trace.json"

python3 "$REPO/experiments/X-zeta23-support-optimizer/optimize_support.py" \
  --nodes 128 --iterations 18 --targets 0.70 0.80 0.90 \
  --json "$OUT/support-optimizer.json"

for experiment in \
  X-zeta23-gabor-fusion \
  X-zeta23-finite-isolation \
  X-zeta23-xi-cardinal-capture \
  X-zeta23-terminal-arithmetic-floor \
  X-zeta23-terminal-heat-residue
do
  temp="$(mktemp)"
  (
    cd "$REPO/experiments/$experiment"
    python3 verify.py --json "$temp"
    cmp "$temp" results/verification.json
    sha256sum -c SHA256SUMS
  )
  rm -f "$temp"
done

python3 -m unittest discover -s "$HERE/tests" -p 'test_*.py' -v

(
  cd "$REPO"
  find research/external/anthropic-zeta23 experiments/X-zeta23-* \
    -type f \
    ! -path '*/verification-results/SHA256SUMS' \
    ! -path '*/__pycache__/*' \
    -print0 | sort -z | xargs -0 sha256sum > "$OUT/SHA256SUMS"
)

echo "PASS_ALL_ZETA23_IMPORT_CHECKS"
