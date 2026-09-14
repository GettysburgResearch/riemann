# X-106440 — Even-endpoint exact replay

Run:

```bash
python3 experiments/X-106440-even-endpoint/verify.py \
  --output experiments/X-106440-even-endpoint/results/verification.json
```

The replay checks only:

- the endpoint Gaussian identity `N-D=2 i lambda(F F^(K+1)-F'F^K)`;
- the even-power exterior-square factorization through order twelve;
- exact rational same-sign and reflected source inequalities on a finite grid;
- the complete four-channel constant;
- the `99.48% -> 90%` signed-tail arithmetic.

It does **not** evaluate Xi, locate a companion zero, estimate the signed residue
Gram, prove `EVENST106440`, prove ninety percent, prove density one, or prove RH.