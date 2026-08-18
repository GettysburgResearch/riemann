#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
rm -f main.aux main.out main.toc main.log main.pdf
for _ in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
 done
cp main.pdf factor67-parity-lorenz-hostile-reconstruction-v3.pdf
