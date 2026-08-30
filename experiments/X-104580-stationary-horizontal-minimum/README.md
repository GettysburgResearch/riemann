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
   profile;
5. the exact scope of the critical-value weighted and amplitude-regularity
   interfaces.

Run:

```bash
python3 experiments/X-104580-stationary-horizontal-minimum/verify.py \
  experiments/X-104580-stationary-horizontal-minimum/results/verification.json
```

Expected:

```text
PASS_T104580_STATIONARY_HORIZONTAL_MINIMUM_ALGEBRA
ae633641b5399aedad7ad97738cf411f10fe9ebf471f70dac1f321a8194f147c
```

The replay does **not** prove `SHMIN104580`, `CSAMP104580`,
`AMPREG104580`, the fixed-order descent, or RH.
