# X-106450 — Actual-visible signed-tail replay

Run:

```bash
python3 experiments/X-106450-actual-visible-signed-tail/verify.py \
  --output experiments/X-106450-actual-visible-signed-tail/results/verification.json
```

Expected:

```text
PASS_T106450_ACTUAL_SPECTRAL_TAIL_REDUCTION
```

The replay checks exact hard-band weights, the denominator-cancelled
counterfamily, simple Blaschke calibration, and the `73/1250`,
`851/15000`, and `101/15000` ledgers. It does not evaluate Xi or prove the
visible quotient transfer, OUT/HOLE estimates, ninety percent, or RH.
