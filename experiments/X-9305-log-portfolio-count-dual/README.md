# X-9305 — Exact logarithmic-portfolio and count-dual checker

X-9305 verifies L-9308 using only Python integers and `fractions.Fraction`.

It recomputes

```text
P_beta(y) = -sum_i beta_i product_{j != i} (y+u_j)
```

and accepts the implemented response cone only when every monomial coefficient is nonnegative. It then contracts exact directed intervals for

```text
R_beta(T) = sum_i beta_i log H_T(u_i),
```

verifies the exact L-9305 primal-dual count certificate, and decides the strict sign of

```text
R_beta(T) - m^T lambda.
```

## Synthetic breakthrough control

```text
H(u)=(u-4/3)^2 (u+1)^4
nodes=(1,2,3)
beta=(-1,2,-1)
P_beta(y)=2
```

The raw portfolio is positive and both adjacent count-deflated two-point rows are positive. The multi-point count-deflated portfolio is strictly negative:

```text
raw portfolio       +0.0248450399971143
count subtraction    0.4
adapted portfolio   -0.3751549600028857
```

This proves that the portfolio cone is strictly more discriminating than testing only adjacent monotonicity rows on the same finite data.

## Reproduction

```bash
python -m unittest discover -s tests -v
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
```

Seven adversarial tests pass.

## Production

A future Riemann-xi certificate should be produced by an adapter that:

1. converts directed completed-xi rectangles into exact `H` intervals;
2. imports unconditional exact overlapping total-zero counts;
3. freezes rational nodes, beta, cell costs, primal counts, and dual multipliers;
4. binds both source artifacts by SHA-256;
5. runs this checker without an optimizer in the trust boundary.

No actual Riemann-xi negative is included.
