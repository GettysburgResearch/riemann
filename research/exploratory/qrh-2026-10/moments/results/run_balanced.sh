#!/bin/sh
cd "$(dirname "$0")/.."
date
python3 -I balanced.py results/balanced.json --D 500 1000 2000 --thetas 0.05 0.1 0.25 --workers 2 > results/balanced_A.log 2>&1
date
python3 -I balanced.py results/balanced.json --D 4000 --thetas 0.05 0.1 --workers 2 > results/balanced_B.log 2>&1
date
python3 -I balanced.py results/balanced.json --D 8000 --thetas 0.05 0.1 --workers 2 > results/balanced_C.log 2>&1
