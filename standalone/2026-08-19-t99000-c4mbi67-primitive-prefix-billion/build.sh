#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE"
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf t99000-c4mbi67-primitive-prefix-billion-latex.pdf
if command -v pdfinfo >/dev/null 2>&1; then
  pdfinfo t99000-c4mbi67-primitive-prefix-billion-latex.pdf >/dev/null
fi
printf '%s\n' PASS_T99000_LATEX_BUILD
