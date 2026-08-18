#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1787011200
export FORCE_SOURCE_DATE=1
export TZ=UTC
rm -f main.aux main.log main.out main.toc main.pdf
for _ in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >/tmp/t97700-pdflatex.log
  test -s main.pdf
done
cp main.pdf lapbr-large-prime-typeii-hardening-97700.pdf
