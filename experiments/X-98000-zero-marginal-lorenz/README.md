# X-98000 — Ordered scalar-target ratio and zero-marginal Lorenz collapse

Run:

```bash
python3 verify.py
```

Expected:

```text
PASS_T98000_ZERO_MARGINAL_LORENZ_COLLAPSE
58d3191b80bd7f4763733423b5f94671f2626a19b2a81ce4547170e27e6ee7bc
```

The standard-library replay checks:

- the six finite cell derivative margins for the scalar-to-target ratio;
- the analytic-tail constant at `Y=8`;
- the positive squarefree-shell constant;
- exact one-switch fractional-knapsack algebra;
- the native target Mellin kernel identity.

The squarefree-shell asymptotic itself uses the classical prime number theorem
and squarefree-density theorem. The replay does not prove `GTC67`, `GPC67`,
`CPSL67`, or RH.