#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo "usage: $0 /path/to/riemann" >&2
  exit 2
fi
repo="$(cd "$1" && pwd)"
packet="$(cd "$(dirname "$0")" && pwd)"
base="99cc94c48bafd9b96141f7cef9f1e7aa83012747"
branch="research/gpt56-pro/102600-completion-defect-current"
cd "$repo"
test "$(git rev-parse HEAD)" = "$base" || {
  echo "expected exact PR #715 head $base" >&2
  exit 1
}
test -z "$(git status --porcelain)" || {
  echo "working tree is not clean" >&2
  exit 1
}
python3 "$packet/validate_packet.py"
git switch -c "$branch"
git apply --index "$packet/t102600-completion-defect-add-only.patch"
python3 experiments/X-102600-completion-defect/verify.py --output /tmp/t102600.json
cmp /tmp/t102600.json experiments/X-102600-completion-defect/results/verification.json
sha256sum -c T102600_CONTENT_SHA256SUMS
git commit -m "research: reduce scale and occupancy to one completion-defect current"
git push -u origin "$branch"
if command -v gh >/dev/null 2>&1; then
  gh pr create --draft     --base "research/gpt56-pro/102500-common-mother-stress-tensor"     --head "$branch"     --title "research: completion-defect current after owner/transfer cancellation (T102600)"     --body-file "$packet/PR_BODY_102600.md"
fi
