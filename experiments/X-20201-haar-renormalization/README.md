# X-20201 — Exact Haar-renormalization algebra regression

This experiment verifies only finite algebra used by the proposed global criteria:

- the fourth-power spectral defect;
- the `(1,-2,1)` screw quadratic identity;
- the dilation cocycle;
- the negative polar square;
- the positive Lerch factorization;
- positive synthetic Stieltjes Hankel matrices.

It uses Python integers and `fractions.Fraction` only. It evaluates no zeta, xi, prime, zero, logarithm, trigonometric function, or floating-point value.

```bash
python verify.py certificates/synthetic.json --output results/verification.json
python -m unittest discover -s tests -v
```

A successful result is a regression for the new formulas, not evidence for RH.
