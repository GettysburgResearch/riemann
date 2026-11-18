#!/usr/bin/env bash
# Usage: fetch_arxiv_text.sh ARXIV_ID [VERSION]
# Downloads the arXiv PDF (latest or given version) into a shared cache and extracts text with pdftotext -layout.
# Prints the path of the extracted text file. Cache: $OBS_CACHE (default: session scratchpad fulltext/).
set -euo pipefail
ID="$1"; VER="${2:-}"
CACHE="${OBS_CACHE:-/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/fulltext}"
SAFE=$(echo "$ID$VER" | tr '/' '_')
D="$CACHE/arxiv/$SAFE"; mkdir -p "$D"
if [ ! -s "$D/text.txt" ]; then
  for t in 1 2 3 4; do
    if curl -sSL --max-time 180 -A "riemann-observatory/0.1" -o "$D/paper.pdf" "https://arxiv.org/pdf/$ID$VER"; then
      if head -c 5 "$D/paper.pdf" | grep -q '%PDF'; then break; fi
    fi
    sleep $((t*5))
  done
  head -c 5 "$D/paper.pdf" | grep -q '%PDF' || { echo "ERROR: not a PDF (maybe withdrawn / no PDF)" >&2; exit 2; }
  pdftotext -layout "$D/paper.pdf" "$D/text.txt"
  pdfinfo "$D/paper.pdf" > "$D/pdfinfo.txt" 2>/dev/null || true
  sha256sum "$D/paper.pdf" | cut -d' ' -f1 > "$D/sha256.txt"
fi
echo "$D/text.txt"
