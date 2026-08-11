# Integration handoff — Brownian Bohr instability

## Source

Stack on PR #343 at

```text
fed85f2969a5ab9f09890cd89bd6b57ff2115320
```

The base itself contains the parent PR #296 Brownian Nörlund/Green-Robin programme.

## Canonical disposition

- `L-90601`: raw Brownian high-frequency zero theorem.
- `L-90602`: fixed-compact truncation expansion and zero-displacement theorem.
- `R-90601`: raw cofinal/all-large half-plane stability is `FALSE`.
- `L-90603`: positive cutoff-mixture Bohr-instability theorem.
- `L-90604`: functional-equation symmetrization preserves the off-line zeros.
- `R-90602`: BLNRZ and BGRRZ are `FALSE` for logarithmic Nörlund and central-binomial Green weights.
- `X-90601/X-90602`: finite exact/floating regressions only.

## Supersession

The following boundary lines must be superseded:

```text
PR #343:
cofinal half-plane zero-free theorem OPEN / RH-BEARING

PR #296:
BLNRZ/BGRRZ real-zero theorem OPEN / RH-BEARING
```

Replace them with:

```text
cofinal raw half-plane stability               FALSE (R-90601);
logarithmic Norlund finite real-zero stability  FALSE (R-90602);
central-binomial Green finite real-zero         FALSE (R-90602);
height-dependent finite stability               OPEN;
producer redesign avoiding torus zeros          OPEN;
infinite limiting canonical system              OPEN;
RH                                               UNPROVED.
```

## Retained mathematics

Do not discard:

- finite gamma/Dirichlet/Hermite identities;
- exact small-`N` stability;
- serial-exponential recurrence;
- minimum/order-statistic representation;
- positive cutoff and occupation formulas;
- individual Robin-fiber self-adjointness;
- functional equation and reflection symmetry;
- local-uniform convergence to xi;
- the new fixed-zero `1/N` displacement theorem.

## Exact scope

The refutation concerns globally half-plane-stable finite Dirichlet-polynomial producers on an unbounded sequence of indices. It does not rule out:

- choosing `N=N(T)` and proving a theorem only below height `T`;
- a genuinely different producer whose every Bohr vertical limit is zero-free;
- constructing the infinite limiting canonical system directly without finite global real-zero approximants.
