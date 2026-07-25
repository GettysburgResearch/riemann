#!/bin/sh
exec python3 -u certify_parallel.py \
  ../X-5602-riemann-siegel-detector/results/zeros-1e13.txt \
  --a 20000000000001/2 --b 20000000001999/2 \
  --procs 3 --expected-N 4467 --label "t=1e13" \
  --out results/certified-1e13.json
