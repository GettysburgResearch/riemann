# X-30501 — Boundary atomic-norm firewall

This standard-library checker authenticates the exact finite arithmetic used by
`R-30501`:

```text
rational square bounds for the eta top-cell moat;
first omitted shifted-even / odd indices on N/3<q<=N/2;
source singleton geometry above the half-output cutoff;
exact central-binomial entropy increments.
```

Retained verdict:

```text
EXACT_BOUNDARY_ATOMIC_NORM_FIREWALL
```

Retained digest:

```text
32c1317529f8559b845fe3016d50424e9d213c9d7f6de3ea8be0672253eb3016
```

The analytic proof in `R-30501` establishes

```text
sum_m sqrt(m)|sigma_N(m)| >= N/240
```

for every stopped critical power with `N>=120`.  The checker does not certify a
replacement cancellation theorem, Cycle Debt, the prime-ramp estimate, or RH.
