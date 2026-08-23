# X-104580 — Stationary horizontal-minimum exact algebra replay

This standard-library replay checks only the finite algebra used by the new
fixed-order frontier.

It verifies:

1. the real-axis variance determinant for one symmetric positive atom source;
2. an exact imaginary stationary-point counterexample showing that real-axis
   log-convexity does not continue automatically;
3. the fixed-order transfer constants for `q=3/4`, `q=9/10`, and `q=1` using
   Conrey's `alpha_3=0.9873` input;
4. the factor two between horizontal modulus curvature and the Laguerre
   profile.

Run:

```bash
python3 experiments/X-104580-stationary-horizontal-minimum/verify.py \
  experiments/X-104580-stationary-horizontal-minimum/results/verification.json
```

Expected:

```text
PASS_T104580_STATIONARY_HORIZONTAL_MINIMUM_ALGEBRA
e72e1c6f6fc25d271f922c746728676ec9c2fd50276a46d09752732450c220cc
```

The replay does **not** prove `SHMIN104580`, `CSAMP104580`,
`AMPREG104580`, the fixed-order descent, or RH.
