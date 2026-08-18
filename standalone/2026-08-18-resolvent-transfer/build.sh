#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH=1787000000
export FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error -jobname=raw-contracted-parity-resolvent-97500 main.tex >/tmp/t97500-pdflatex-1.log
pdflatex -interaction=nonstopmode -halt-on-error -jobname=raw-contracted-parity-resolvent-97500 main.tex >/tmp/t97500-pdflatex-2.log
rm -f raw-contracted-parity-resolvent-97500.aux raw-contracted-parity-resolvent-97500.log raw-contracted-parity-resolvent-97500.out raw-contracted-parity-resolvent-97500.toc
