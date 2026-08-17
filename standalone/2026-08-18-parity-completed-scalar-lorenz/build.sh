#!/usr/bin/env bash
set -euo pipefail
export SOURCE_DATE_EPOCH=1787030400
export FORCE_SOURCE_DATE=1
export TZ=UTC
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
mv -f main.pdf parity-completed-factor67-scalar-lorenz-97400.pdf
sha256sum parity-completed-factor67-scalar-lorenz-97400.pdf main.tex references.bib
