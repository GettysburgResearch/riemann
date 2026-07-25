#!/bin/sh
exec python3 -u certified_sign_changes.py \
  ../X-5602-riemann-siegel-detector/results/zeros-pr71-ordinate.txt \
  --a 75347258181331/16 --b 37673629090985/8 \
  --prec 192 --expected-N 172 \
  --out results/certified-signs-pr71.json
