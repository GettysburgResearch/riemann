# X-91673 — Root score-Hall common-normalization replay

This experiment checks the finite and algebraic shell of `L-91673/L-91674/T-91657`.

Run:

```bash
cd experiments/X-91673-root-score-hall-common-normalization
python3 verify.py --json results/verification.json
```

Expected verdict:

```text
PASS_ROOT_SCORE_HALL_COMMON_NORMALIZATION_ALGEBRA
```

The replay checks:

```text
fixed-window score-Hall margins on every activation endpoint;
score-normalized component-row monotonicity on all 1,431 root cells;
the exact stopped-leaf p=67,y=13 firewall;
score equality, target slack, and row-bonus algebra;
ordinary and radix-four response commutation;
finite positive endpoint integration;
same-index scalar covariance;
one global linear quantizer identity.
```

It does not certify the imported continuum endpoint density, B-spline mismatch estimates, terminal omission theorem, external endpoint-to-RH chain, or RH.
