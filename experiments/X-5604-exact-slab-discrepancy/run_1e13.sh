#!/bin/sh
python3 -u slab_discrepancy.py --a 10000000000000.5 --b 10000000000999.5 \
   --prec 192 --out results/slab-1e13.json
python3 -u certified_sign_changes.py \
   ../X-5602-riemann-siegel-detector/results/zeros-1e13.txt \
   --a 20000000000001/2 --b 20000000001999/2 --prec 192 \
   --out results/certified-signs-1e13.json
