#!/bin/sh
X=/home/user/riemann/experiments/X-5604-exact-slab-discrepancy
# 1: census -> gap analysis
( while [ ! -s $X/results/platt-certify-1e13-50k.json ]; do sleep 20; done
  python3 -u $X/gap_census.py $X/results/balls-1e13-50k.txt \
      --top 15 --interior-z 5 --out $X/results/gap-census-50k.json \
      > $X/results/gap-census-50k.log 2>&1 ) &
# 2: 1e16 count -> platt engine (kill the slow gram phase first)
( while [ ! -s $X/results/height-1e16-slab.json ]; do sleep 30; done
  N=$(python3 -c "import json;print(json.load(open('$X/results/height-1e16-slab.json'))['N_total_in_slab'])")
  NA=$(python3 -c "import json;print(json.load(open('$X/results/height-1e16-slab.json'))['N_a']['integer'])")
  NB=$(python3 -c "import json;print(json.load(open('$X/results/height-1e16-slab.json'))['N_b']['integer'])")
  pkill -f "certify_gram.py --a 20000000000000001/2" 2>/dev/null
  pkill -f "certify_height.py --t0 10000000000000000" 2>/dev/null
  python3 -u $X/platt_certify.py --a 20000000000000001/2 --b 20000000000000009/2 \
      --prec 128 --block 64 --Na $NA --Nb $NB --label "t=1e16 platt" \
      --balls-out $X/results/balls-1e16.txt --out $X/results/platt-certify-1e16.json \
      > $X/results/platt-certify-1e16.log 2>&1 ) &
wait
