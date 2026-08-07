# X-20703 — Structured Cauchy frame and graph-Schur invariance

This exact standard-library experiment verifies the finite algebra used by
`L-20701`--`L-20703`.

It checks:

1. the fixed transform from D-0001 even rows to Cauchy–Vandermonde rows;
2. the exact determinant product;
3. the Lagrange/residue structured inverse;
4. the rational Newton lower-triangular pivots;
5. invariance of the complete positive-sector Schur complement under an
   arbitrary graph shear.

Run:

```text
python verify.py certificate.json --output /tmp/result.json
cmp /tmp/result.json results/verification.json
```

Retained exact values:

```text
Cauchy determinant  24137569 / 16614935900640000
base Schur pivot    23347 / 2400000
graph Schur pivot   23347 / 2400000
proof digest        d3ae709be011153dd9ad22949751a8383309f3dbc93f90b2a2a1f78ce327704b
```

The experiment is finite algebra only. It proves that frame conditioning and
graph cross terms can be handled exactly; it does not prove the cofinal sign of
the zeta prime-side Schur pivot.
