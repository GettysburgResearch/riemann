# X-91107 — Balanced-ray monotone parity lift

This standard-library replay certifies two finite/exact parts of `L-91320`:

1. the balanced channel `H_*=L+kappa_*R` has a strict Hall transport with
   support `e<=o` throughout the full factor-54 reset window;
2. every monotone transport edge has an exact nonnegative interval seed whose
   adjacent difference, ordinary carry and radix-four detail are the intended
   odd-minus-even divisor stencils.

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_BALANCED_RAY_MONOTONE_PARITY_LIFT
```

The replay does **not** prove that the interval seed has nonnegative parabolic
endpoint-row coefficients. That endpoint-row cone inclusion remains open.
