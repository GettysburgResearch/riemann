# X-15125 — Centered Heath–Brown / scale-contraction exact regression

This standard-library experiment checks four finite algebraic interfaces used by
`L-15155`, `L-15156`, `T-15121`, and `M-15112`:

1. the exact truncated Heath–Brown identity for `K=3`, `V=4`, through
   `X=V^K=64`, using a symbolic completely-additive prime-log basis;
2. exact tuple expansion and deterministic first-crossing Type-I/Type-II
   partition for `K=2`, `V=3`;
3. invariance of a positive Gram under independent subtraction of two declared
   null modes from every decomposition row, together with the finite-vector
   Cauchy bound;
4. a synthetic three-component strict-scale-contraction recurrence.

It deliberately does **not** claim or test the open centered packet estimate
`CP(K)` on Riemann data.

Run:

```bash
python verify.py results/exact-verification.json
python partition_verify.py
python -m unittest discover -s tests -v
```

Retained proof digests:

```text
main algebra
3dc50743f1b3b435e2d9b969c5a1191ef0a94e89a4f4ccd17a2b211e6d91dea0

row partition
fb68b871d6c8cbf984ee018d5bf9d7ddef374811a5dce5b604af8215cadfe22f
```

Retained tuple counts:

```text
Type I   30
Type II  41
```
