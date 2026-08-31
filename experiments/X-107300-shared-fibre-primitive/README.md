# X-107300 exact replay

Run:

```bash
python3 experiments/X-107300-shared-fibre-primitive/verify.py \
  --output experiments/X-107300-shared-fibre-primitive/results/verification.json
```

The replay checks exact rational instances of:

- rectangular residue aggregation;
- tensor-product Wick factorization;
- mean/primitive norm decomposition;
- the one-hundred-history \(3,3,-1,\ldots,-1\) panel;
- the equal-history opposite-sign calibration;
- the rank-one aggregate-only counterexample;
- fail-closed conclusion flags.

It does not enumerate the complete live source, construct a sheaf, prove a
uniform trace estimate, bind the principal member, or prove RH/GRH.
