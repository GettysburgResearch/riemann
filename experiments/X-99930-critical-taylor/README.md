# X-99930 — Critical Taylor renormalization replay

This standard-library replay checks the finite algebra supporting T-99930.
It does not prove the final critical envelope and does not establish RH.

Run:

```bash
./replay.sh
```

Checks include:

- duplicate-67 labelled Euler coefficients;
- the exact integral formula and scaling inequality for every sampled Taylor remainder;
- a directed rational upper bound below one for the complete exponent-3/2 prime-label mass;
- positivity and the quadratic complement identity for the critical kernel;
- the exact closed Mellin transform at rational test points;
- the positive-real pole ledger and a last-step sign mutation.

Expected verdict:

```text
PASS_T99930_CRITICAL_TAYLOR_RENORMALIZATION
```

The generated JSON must retain:

```text
critical_envelope_sign      open
critical_negative_mass      open
riemann_hypothesis          open
rh_established              false
```
