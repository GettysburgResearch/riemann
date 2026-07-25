#!/bin/sh
exec python3 -u slab_discrepancy.py \
  --a 18836814545413/4 --b 4709203636354 \
  --prec 192 --out results/gap-interior.json
