# X-92300 — Fractional-string renormalization replay

This experiment checks only finite algebra and high-precision diagnostics for
`L-92300/L-92301/R-92300`.

It verifies:

1. the exact central-binomial beta-Hankel determinant
   \[
   \det\left(\binom{2(i+j+1)}{i+j+1}4^{-(i+j+1)}\right)
   =2^{-n(2n-1)}
   \]
   through order eight;
2. an exact rational squared-pole control that is positive through Hankel order
   seven and strictly negative at order eight;
3. numerical convergence of the safely evaluated Xi admittance to the drifting
   fractional-power background.

The diagnostic does **not** prove:

- the sectorial uniform error bounds;
- the growing-order theorem;
- the near-cut fractional-string completion;
- complete Bernstein passivity;
- the Riemann Hypothesis.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_FRACTIONAL_STRING_RENORMALIZATION
```
