#!/usr/bin/env bash
# Usage: fetch_url_text.sh URL KEY   -> downloads URL (PDF or HTML) into cache dir KEY, extracts text, prints text path.
set -euo pipefail
URL="$1"; KEY=$(echo "$2" | tr '/: ' '___')
CACHE="${OBS_CACHE:-/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/fulltext}"
D="$CACHE/url/$KEY"; mkdir -p "$D"
if [ ! -s "$D/text.txt" ]; then
  curl -sSL --max-time 240 -A "Mozilla/5.0 (riemann-observatory)" -o "$D/raw" "$URL"
  echo "$URL" > "$D/source_url.txt"; sha256sum "$D/raw" | cut -d' ' -f1 > "$D/sha256.txt"
  if head -c 5 "$D/raw" | grep -q '%PDF'; then pdftotext -layout "$D/raw" "$D/text.txt"; pdfinfo "$D/raw" > "$D/pdfinfo.txt" 2>/dev/null || true
  else python3 -I -c "import sys,html,re;t=open(sys.argv[1],errors='ignore').read();t=re.sub(r'(?is)<(script|style).*?</\1>','',t);t=re.sub(r'<[^>]+>',' ',t);print(html.unescape(re.sub(r'[ \t]+',' ',t)))" "$D/raw" > "$D/text.txt"; fi
fi
echo "$D/text.txt"
