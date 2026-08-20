# X-100610 — Two-ended implication-matrix replay

This standard-library replay checks the finite algebra supporting
`L-100610--L-100611` and `T-100610`.

```bash
python3 experiments/X-100610-two-ended-matrix/verify.py \
  --output /tmp/x100610.json
cmp /tmp/x100610.json \
  experiments/X-100610-two-ended-matrix/results/verification.json
```

Expected:

```text
PASS_T100610_TWO_ENDED_IMPLICATION_MATRIX
dd11e217b29501bd0917a21c5bb41b32e9cf585f9bc651ce8cfa64e640ca540b
```

The replay verifies:

- the exact positive-coefficient two-ended hazard identity;
- the direct min/max tensor and both of its marginals;
- the two-ended Littlewood--Paley identity on exact rational fixtures;
- the norm-one survival-vector bounds;
- the two-sided Schur bilinear estimate;
- exact row-only and column-only multiplicity separators.

It deliberately records

```text
focr100610_proved = false
locr100610_proved = false
rh_established    = false
```

because the replay authenticates the implication-matrix algebra, not the open
arithmetic Schur estimates.