#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
export SOURCE_DATE_EPOCH=1787002090
export FORCE_SOURCE_DATE=1
rm -f main.aux main.out main.toc main.pdf main.log main.fls main.fdb_latexmk \
      parity-annular-hostile-reconstruction.tmp.pdf
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >"/tmp/t97350-latex-$i.log"
done
gs -q -dSAFER -dBATCH -dNOPAUSE \
  -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
  -dDetectDuplicateImages=true -dCompressFonts=true \
  -sOutputFile=parity-annular-hostile-reconstruction.tmp.pdf main.pdf
mv parity-annular-hostile-reconstruction.tmp.pdf parity-annular-hostile-reconstruction.pdf
rm -f main.aux main.out main.toc main.pdf main.log main.fls main.fdb_latexmk
printf 'built %s\n' "$ROOT/parity-annular-hostile-reconstruction.pdf"
