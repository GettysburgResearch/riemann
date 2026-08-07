# X-25301 — Parabolic cover dual refutation

This standard-library checker validates the finite exact arithmetic used by
`R-25301` and the same-scale cluster algebra in `L-25301`.

It uses Python integers and `fractions.Fraction` to verify:

1. strict negativity of the reciprocal-cell derivative bracket for
   `N=37,38,39`;
2. `E(1/37)>2/5`;
3. the formal identity
   `sum_(q=p^a|m) Lambda(q)=log m` through `m=128`;
4. exact constants converting the continuum band and the PNT into the
   stated `sqrt(X)/4000` cover-cost lower bound;
5. nonnegative inverses for the path clusters of lengths one through three
   and the exceptional `{2,3,4,5}` divisibility matrix;
6. six fail-closed tests.

Run:

```bash
python verify.py --self-test --output results/exact-verification.json
```

The PNT and the uniform finite-difference passage are proved in `R-25301`;
the checker authenticates the finite reciprocal-cell, dual, and cluster
algebra.

Arithmetic class:

```text
EXACT_RATIONAL_CONTINUUM_AND_DUAL_REFUTATION_CONTROL
```

It does not prove a signed repair, the prime-ramp bound, or RH.
