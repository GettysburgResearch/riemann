#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo "usage: $0 /path/to/riemann" >&2
  exit 2
fi
repo="$(cd "$1" && pwd)"
packet="$(cd "$(dirname "$0")" && pwd)"
base="d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33"
branch="research/gpt56-pro/107000-beta-nyquist-compression"
cd "$repo"
test "$(git rev-parse HEAD)" = "$base" || {
  echo "expected exact PR #759 head $base" >&2
  exit 1
}
test -z "$(git status --porcelain)" || {
  echo "working tree is not clean" >&2
  exit 1
}
python3 "$packet/validate_packet.py"
git switch "$branch"
git apply --index "/mnt/data/t107020-hyperbolic-native-beta-add-only.patch"
python3 experiments/X-107020-hyperbolic-native-beta/verify.py \
  --output /tmp/t107020-verification.json
cmp /tmp/t107020-verification.json \
  experiments/X-107020-hyperbolic-native-beta/results/verification.json
sha256sum -c SHA256SUMS_T107020
git commit -m "research: compress native beta criterion to log X loglog X features"
git push origin "$branch"
if command -v gh >/dev/null 2>&1; then
  gh pr edit 759 \
    --title "research: hyperbolic log-log compression of the native beta RH criterion (T107000-T107020)" \
    --body-file "$packet/PR_BODY_107020.md"
fi
