# X-100720 — Exact cubic hinge / rough-prefix algebra replay

This standard-library checker verifies only the finite algebraic interfaces of
`T-100720`.

Run:

```bash
python3 experiments/X-100720-cubic-hinge/verify.py \
  --output /tmp/t100720.json
cmp /tmp/t100720.json \
  experiments/X-100720-cubic-hinge/results/verification.json
```

Expected:

```text
PASS_T100720_CUBIC_HINGE_ROUGH_PREFIX_ALGEBRA

a05a9ed1c455a87115424ec8d4bfb0ec1fc8acc94ce0f36f012c4c35be88f0ba
```

The replay checks:

- the exact hinge and carrier/collar identities;
- the compensated rough-prefix derivative on a rational square-label fixture;
- the exact `L1` and first-moment factorization of the third derivative;
- four exact two-sided Taylor certificate inequalities;
- the scaling constant in the regularity countermodel.

It does **not** replay Tao's published semigroup theorem.  It does not prove
`LPCC100723`, `FPCC100723`, or RH.
