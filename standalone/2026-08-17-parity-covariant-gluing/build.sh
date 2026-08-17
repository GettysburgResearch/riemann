#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export TZ=UTC
export SOURCE_DATE_EPOCH=1786924800
export FORCE_SOURCE_DATE=1
rm -f main.aux main.log main.out main.toc main.pdf
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/tmp/t96500-latex-1.log
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/tmp/t96500-latex-2.log
mv -f main.pdf parity-covariant-gluing-fixed-depth-96500.pdf
