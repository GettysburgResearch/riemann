# X-105610 — Moving-carrier reciprocal source and Turán phase bridge

This replay checks exact finite algebra only.

It verifies:

- complete additivity of a formal logarithmic frequency;
- coefficientwise positivity of the Dirichlet-convolution exponential;
- the exact derivative identity
  `-u A' exp(uA) = sum log(n)c_u(n)n^-s`;
- the exact Laplace formula for `q-hq'` with a moving scalar carrier and its
  derivative;
- the prime-two real-carrier reciprocal coefficient;
- the Turán/hyperbolic-derivative factorization on rational polynomial
  fixtures;
- positivity of the exterior-square Fourier density for a finite positive
  Fourier source.

Run:

```bash
python3 experiments/X-105610-moving-carrier-turan/verify.py \
  experiments/X-105610-moving-carrier-turan/results/verification.json
```

Expected:

```text
PASS_X_105610_MOVING_CARRIER_TURAN_BRIDGE
checks=348
17e2887882e7b8da65ca6ffc091286ba8c6615cac28a685cf29832538724dadf
RH_UNPROVEN
```

The replay does not evaluate Xi, prove the far-safe-line analytic asymptotic,
perform the one-sided physical transfer, establish the pointwise microscope
sign, or prove RH.
