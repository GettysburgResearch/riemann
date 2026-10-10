#!/bin/sh
# main runs (sequential; each uses 2 threads)
cd "$(dirname "$0")/.."
date
python3 -I moments.py results/moments.json --D 500 707 1000 1414 2000 2828 4000 5657 --thetas 0.05 0.1 0.25 0.5 --d2-max 5657 --workers 2 > results/moments_A.log 2>&1
date
python3 -I moments.py results/moments.json --D 8000 11314 16000 22627 32000 45255 64000 --thetas 0.05 0.1 0.25 0.5 --theta-cap 32000:0.25 --workers 2 > results/moments_B.log 2>&1
date
python3 -I diag.py results/diag.json --D 500 707 1000 1414 2000 2828 4000 5657 8000 11314 16000 22627 32000 45255 64000 --exact2-max 22627 --exact3-max 2000 --samples 1000000 --workers 2 > results/diag.log 2>&1
date
