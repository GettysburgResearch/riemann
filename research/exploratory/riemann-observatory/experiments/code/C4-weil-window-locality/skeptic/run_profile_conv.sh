#!/bin/bash
# SKEPTIC C4: N-convergence of the even-sector profile (independent implementation sk_profile.py)
OUT=/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic/sk_profile_conv.jsonl
cd "$(dirname "$0")"
for args in "0.5 25 60 100" "0.5 30 60 110" "0.5 40 60 130" "0.6 24 60 100" "0.6 32 60 120" "0.6 40 60 130" "0.8 36 60 120" "0.8 46 70 140" "0.8 56 70 160"; do
  python3 sk_profile.py $args >> $OUT
done
