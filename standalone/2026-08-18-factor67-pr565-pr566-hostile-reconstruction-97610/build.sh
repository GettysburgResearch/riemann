#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1787011200
export FORCE_SOURCE_DATE=1
export TZ=UTC
export LC_ALL=C.UTF-8
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf factor67-pr565-pr566-hostile-reconstruction.pdf
