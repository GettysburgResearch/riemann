# X-15125 — Centered Heath–Brown / scale-contraction exact regression

This standard-library experiment checks three finite algebraic interfaces used by
`L-15155`, `L-15156`, `T-15121`, and `M-15112`:

1. the exact truncated Heath–Brown identity for `K=3`, `V=4`, through
   `X=V^K=64`, using a symbolic completely-additive prime-log basis;
2. invariance of a positive Gram under independent subtraction of two declared
   null modes from every decomposition row, together with the finite-vector
   Cauchy bound;
3. a synthetic three-component strict-scale-contraction recurrence.

It deliberately does **not** claim or test the open centered packet estimate
`CP(K)` on Riemann data.

Run:

```bash
python verify.py results/exact-verification.json
python -m unittest discover -s tests -v
```

Retained proof digest:

```text
3dc50743f1b3b435e2d9b969c5a1191ef0a94e89a4f4ccd17a2b211e6d91dea0
```
