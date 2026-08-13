# X-91109 — Reserve-normalized component-row monotonicity

This directed standard-library replay certifies the finite analytic gate in
`L-91322`.

For every exact component row `Q_Y(n)`, define

```text
R_n(Y)=Q_Y(n)/(sqrt(Y)-1).
```

On each activation cell, the derivative numerator decreases because

```text
M_(n,N)'(Y)=-Q_Y(n)/(2sqrt(Y)) <= 0.
```

The replay checks the right endpoint of all 1,431 cells in the full factor-54
window and proves

```text
M_(n,N)(Y)>1/20.
```

Together with the no-upward reserve Hall transport from `X-91103`, this yields
the exact finite-row positivity theorem in `L-91322`.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_NORMALIZED_COMPONENT_ROW_MONOTONICITY
```
