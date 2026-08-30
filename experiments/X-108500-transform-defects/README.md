# X-108500 — stdlib-exact replay of the transform defect law (T-108500)

Run from the repository root:

```
python3 experiments/X-108500-transform-defects/verify.py
```

Expected banner: `PASS_108500_TRANSFORM_DEFECTS checks=7`.

Checks D1-D7 (all `EXACT_RATIONAL`, standard library only, no floats):
defect law m=2,3,4 at 24 integer instantiations against the claimed closed
forms; the trace-zero degeneration; the self-duality coefficient identity;
the `c_1 = a^m - h_m` law for m=2..6; the Cauchy/Hadamard identity at 12
pairs; the Jacobi-Trudi Hankel-minor identity; the Adams relabelling
identity. Writes `results/verification.json` with
`"rh_established": false` (this experiment asserts nothing about RH).

Independence: this replay shares no code with the sympy discovery layer
(`research/exploratory/2026-08-30-two-programme-pass/matrix/`); agreement
of the two routes is part of the claim's verification story.

Tests: `python3 -m unittest discover -s experiments/X-108500-transform-defects/tests`
