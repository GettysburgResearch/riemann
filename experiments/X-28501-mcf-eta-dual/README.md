# X-28501 — Exact MCF dyadic-dual algebra

Run:

```bash
python experiments/X-28501-mcf-eta-dual/verify.py
```

The checker uses only Python integers and `fractions.Fraction`. It verifies:

1. the dyadic potential `Phi(n)=L(n)-1`, with `Phi(1)=0`, is superadditive on every declared MCF edge through `n=512`;
2. its first difference is supported exactly on powers of two;
3. the divisor coefficient is both `mu * Delta Phi` and the factor-two shift of the finite Dirichlet inverse of eta;
4. `1*a=Delta Phi` and the floor reconstruction of `Phi`;
5. the exact finite pairing identity for an independent rational target;
6. an exterior-edge mutation with negative dual defect.

Retained result:

```text
classification
EXACT_MCF_DYADIC_DUAL_ALGEBRA_VERIFIED

proof-object SHA-256
78ee2628bb03aa026e01196b415f0e1e3cda64eb358feee6da2be01c31591fbe
```

The checker authenticates finite algebra only. The cofinal contradiction uses the complete analytic proof in `R-28501`: the exact Mellin transform, the eta-factor poles, the interpolation estimate, and Landau's one-sign theorem.
