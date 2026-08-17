#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1786924800
export FORCE_SOURCE_DATE=1
export TZ=UTC
rm -f main.aux main.log main.out main.toc main.pdf
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >/tmp/t96650-pdflatex-$i.log
  test -s main.pdf
done
cp main.pdf factor67-two-row-parity-resummed-v2.pdf
python /home/oai/skills/pdfs/scripts/pdf_preflight.py factor67-two-row-parity-resummed-v2.pdf > PDF_PREFLIGHT.txt
python /home/oai/skills/pdfs/scripts/pdf_inspect.py factor67-two-row-parity-resummed-v2.pdf > PDF_INSPECT.txt
