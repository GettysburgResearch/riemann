# X-106451 — Endpoint Hermite–Bézout replay

Run:

```bash
python3 experiments/X-106451-hermite-bezout/verify.py \
  --output experiments/X-106451-hermite-bezout/results/verification.json
```

The replay checks finite exact algebra only:

- the endpoint Bézout decomposition on rational grids;
- the literal `+1/-1` CRT root labels;
- a finite inertia/signature fixture;
- the exact `99.48% -> 90%` signature threshold.

It does not evaluate Xi, construct the source congruence, prove
`HBSIG106451/HBRT106451`, prove ninety percent, prove density one, or prove RH.