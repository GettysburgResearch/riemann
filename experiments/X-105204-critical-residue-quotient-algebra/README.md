# X-105204 — Critical-residue quotient algebra replay

This lightweight standard-library replay authenticates the finite algebra in
`L-105204`.

Run:

```bash
python -B experiments/X-105204-critical-residue-quotient-algebra/verify.py \
  --output experiments/X-105204-critical-residue-quotient-algebra/results/verification.json
```

Expected:

```text
PASS_X_105204_CRITICAL_RESIDUE_QUOTIENT_ALGEBRA
e7b25fc4e8e81bb150e6ae85a363a98576139c420f34db344a049920eb1a09f5
RH_UNPROVEN
```

The replay uses exact `Fraction` arithmetic to check:

- the quotient interpolant `p''u = p mod p'`;
- residue trace moments through order four;
- the normalized resultant characteristic polynomial at 16 rational points;
- PR #723's quartic root-ledger/cross-debt identity;
- a perfectly coherent real-rooted cubic fixture;
- the exact spectral-variance/coherence identity;
- one rational Kantorovich threshold fixture.

It does **not** authenticate the analytic Xi saddle estimates, canonical-product
passage, `CRDB105200`, or RH.
