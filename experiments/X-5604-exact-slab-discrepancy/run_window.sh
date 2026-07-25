#!/bin/sh
exec python3 -u slab_discrepancy.py \
  --a 75347258181331/16 --b 37673629090985/8 \
  --target 20225875608341108140435/4294967296 \
  --prec 192 --list-zeros --max-list 400 \
  --out results/window-pr71.json
