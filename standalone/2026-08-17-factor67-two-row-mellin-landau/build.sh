#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=0
latexmk -C >/dev/null 2>&1 || true
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf factor67-two-row-mellin-landau-proposal.pdf
