# X-98000 — Ordered scalar-target ratio and zero-marginal Lorenz collapse

Run:

```bash
python3 verify.py
```

Expected:

```text
PASS_T98000_ZERO_MARGINAL_LORENZ_COLLAPSE
7b6042d0e6d1632ae35cce1018dd97316c51acb954f64981ae42f3af5deb4dd5
```

The standard-library replay uses exact `Fraction` interval arithmetic. Square
roots are enclosed by integer-square-root decimal rationals; logarithms are
enclosed by a finite atanh series with an exact remainder bound.

It checks:

- the six finite cell derivative margins for the scalar-to-target ratio;
- the analytic-tail constant at `Y=8`;
- the positive squarefree-shell constant;
- exact one-switch fractional-knapsack algebra;
- the native target Mellin kernel identity.

The squarefree-shell asymptotic itself uses the classical prime number theorem
and squarefree-density theorem. The replay does not prove `GTC67`, `GPC67`,
`CPSL67`, or RH.