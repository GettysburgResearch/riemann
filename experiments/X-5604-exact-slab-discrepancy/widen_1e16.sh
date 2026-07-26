#!/bin/sh
X=/home/user/riemann/experiments/X-5604-exact-slab-discrepancy
python3 -u -c "
from flint import arb, ctx
ctx.prec = 192
x = arb(20000000000000081)/arb(2)      # 1e16 + 40.5
n = x.zeta_nzeros().unique_fmpz()
print(int(n))
" > $X/results/nb-1e16-wide.txt 2>$X/results/nb-1e16-wide.err
NB=$(cat $X/results/nb-1e16-wide.txt)
if [ -n "$NB" ]; then
  python3 -u $X/platt_certify.py --a 20000000000000001/2 --b 20000000000000081/2 \
    --prec 128 --block 300 --Na 54118226280292480 --Nb $NB --label "t=1e16 x40" \
    --balls-out $X/results/balls-1e16-40.txt --out $X/results/platt-certify-1e16-40.json \
    > $X/results/platt-certify-1e16-40.log 2>&1
fi
