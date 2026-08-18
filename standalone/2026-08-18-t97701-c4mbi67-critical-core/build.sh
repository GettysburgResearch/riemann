#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1787020800
export FORCE_SOURCE_DATE=1
export TZ=UTC
rm -f main.aux main.log main.out main.toc main.pdf
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >/tmp/t97701-pdflatex-$i.log
  test -s main.pdf
done
cp main.pdf t97701-c4mbi67-critical-core.pdf
python /home/oai/skills/pdfs/scripts/pdf_preflight.py t97701-c4mbi67-critical-core.pdf > PDF_PREFLIGHT.txt
python /home/oai/skills/pdfs/scripts/pdf_inspect.py t97701-c4mbi67-critical-core.pdf > PDF_INSPECT.txt
