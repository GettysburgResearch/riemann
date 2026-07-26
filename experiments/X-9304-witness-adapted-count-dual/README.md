# X-9304 — Witness-adapted count duals

`X-9304` is the exact finite checker for L-9305.

It combines:

- direct completed-`xi` modulus-square intervals at two exact positive nodes;
- unconditional exact total-zero counts on overlapping signed ordinate windows;
- rational lower bounds for the per-zero logarithmic response in each atom cell;
- one nonnegative integer primal atom-count vector;
- one unrestricted rational dual vector.

The checker verifies

```text
A x = m,
x >= 0,
A^T lambda <= c,
c^T x = m^T lambda,
```

then forms the exact directed row

```text
log H_T(v) - log H_T(u) - m^T lambda.
```

A strict negative `RIEMANN_XI_DIRECTED` row is an RH-disproof nomination pending independent count/primitive reproduction and analytic review.

## Why this is new

The overlapping-count envelope of PR #104 constructs the strongest universal radial subtraction. `X-9304` instead optimizes one fixed scalar witness. Correlations between asymmetric windows can make the row-specific bound strictly stronger than integrating the universal pointwise count profile.

## Exact synthetic control

The retained model

```text
H(u) = (u-5)^2 (u+4) (u+1)^5
u = 1
v = 3
```

uses count equations

```text
x_m1 + x_p1 + x_p2 = 5
x_m2 + x_m1 + x_p1 = 6
```

and rational cell costs

```text
(1/3, 1/2, 1/2, 1/3).
```

The coarse safe dual subtracts `2`; the optimal primal-dual pair subtracts `17/6`.

```text
raw row                         +2.4159137783010487
coarse count-deflated row       +0.4159137783010489
witness-adapted dual row        -0.4174195550322845
```

The exact log interval width is below `1.5e-155`.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Seven adversarial tests pass.

## Production adapter

A production certificate should bind:

- the direct completed-`xi` primitive table SHA-256;
- the unconditional total-count table SHA-256;
- every window proof-gate digest;
- exact atom endpoints relative to the common ordinate;
- exact modulus-square intervals;
- exact primal and dual vectors.

The LP solver is not trusted. Only the exported finite primal-dual certificate is checked.

## Classification

- L-9305: `PROPOSED`.
- X-9304 arithmetic checker: exact finite standard-library arithmetic.
- Synthetic separation: exact, not a Riemann-`xi` result.
- Production Riemann-`xi` result: pending.
- Counterexample status: none.
