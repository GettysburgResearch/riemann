# X-20202 — Exact `r`-adic renormalization regression

This experiment checks only the finite algebra supporting `T-20203/L-20202`.
It evaluates no zeta function, prime stream, zero table, Laplace transform, or
Landau argument.

The retained synthetic packet uses `r=5` and verifies:

- the negative-prime threshold exponent `2/(r+1)=1/3`;
- exact negative, zero, and positive normalized prime-weight rows;
- the termwise positive Lerch numerator
  `r^2(1-y)-(1-y^r)` and its elementary lower bound;
- the positive-mixture residue balance and the forced descendant-multiplicity
  conclusion;
- the dilation cocycle
  `D_(rs)(t)=r^2 D_s(t)+D_r(st)` with an independently bound expected value.

Run:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

The immutable expected verdict is

```text
EXACT_R_ADIC_RENORMALIZATION_ALGEBRA_VERIFIED
```

with proof-object SHA-256

```text
8a2d2a52203a38293cd3e2eeb904045a9b34e6404b9d3735ef3a6851295eee3f
```

The proof boundary is strict: this regression does not certify the imported
screw normalization, the pole-descent theorem, a production prime value, an
eventual sign, or RH.
