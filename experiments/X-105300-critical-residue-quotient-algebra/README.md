# X-105300 — Critical-residue quotient spectrum

Run:

```bash
python -B experiments/X-105300-critical-residue-quotient-algebra/verify.py \
  --output experiments/X-105300-critical-residue-quotient-algebra/results/verification.json
```

Expected:

```text
PASS_X_105300_CRITICAL_RESIDUE_QUOTIENT_ALGEBRA
3a61bc251360b0d165f30b405c3b6d2ec68bdccc1e133e69f9807ad188f7536c
RH_UNPROVEN
```

The standard-library replay checks exact quotient reduction, trace moments,
the normalized resultant characteristic polynomial at sixteen rational points,
PR #723's quartic root-ledger/cross-debt identity, a perfectly coherent cubic,
and the variance/coherence formula.

It does not replay the analytic Xi saddle, the moderate-deviation contour
argument, `CRDB105200`, or RH.
