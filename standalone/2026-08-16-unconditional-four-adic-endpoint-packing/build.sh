#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1786867200
export FORCE_SOURCE_DATE=1
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
mv -f main.pdf four-adic-endpoint-packing-rh-proposal-v1.pdf
