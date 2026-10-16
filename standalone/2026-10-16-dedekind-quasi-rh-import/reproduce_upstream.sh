#!/usr/bin/env bash
# Fetch the complete pinned source into a NEW directory; optionally build.
# This is a reproduction recipe, not a claim those commands were run here.
set -euo pipefail
if [[ $# -lt 1 || $# -gt 2 || ( $# -eq 2 && "$2" != "--build" ) ]]; then
  echo "Usage: $0 NEW_DIRECTORY [--build]" >&2
  exit 2
fi
DEST="$1"
PIN="09afbb4ce6570c1615d58509dc197fc9f0956b7d"
if [[ -e "$DEST" ]]; then
  echo "Refusing to overwrite existing path: $DEST" >&2
  exit 2
fi
command -v git >/dev/null || { echo "git is required" >&2; exit 2; }
mkdir -p "$DEST"
git -C "$DEST" init
git -C "$DEST" remote add origin https://github.com/AxiomMath/DedekindZetaZeroFree.git
git -C "$DEST" fetch --depth 1 origin "$PIN"
git -C "$DEST" checkout --detach FETCH_HEAD
[[ "$(git -C "$DEST" rev-parse HEAD)" == "$PIN" ]]
printf 'Pinned checkout: %s\n' "$PIN"
if [[ $# -eq 2 ]]; then
  command -v lake >/dev/null || { echo "Install Lean/elan with lake first; the checkout pins its toolchain." >&2; exit 2; }
  cd "$DEST"
  lake exe cache get
  lake build 2>&1 | tee dedekind-build.log
  lake comparator --config comparator.json 2>&1 | tee dedekind-comparator.log
  cat > ImportAxiomAudit.lean <<'LEAN'
import DedekindZetaSolution
#print axioms DedekindZetaZeroFree.main
#print axioms DedekindZetaZeroFree.heckeCorollary
LEAN
  lake env lean ImportAxiomAudit.lean 2>&1 | tee dedekind-axioms.log
fi
