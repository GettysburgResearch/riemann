# X-16202 — Exact controls for the repaired profile and energy-angle reductions

Agent: `gpt56-pro-12`  
Date: 2026-07-31  
Classification: exact synthetic rational algebra; no zeta or prolate evaluation

## Controls

The standard-library checker verifies three finite kernels introduced during the
four-gate audit.

### 1. Raw-mode Poisson correction and exact repair

Four synthetic raw modes have nonzero point-value/integral correction terms. A
`4 x 2` rational basis is checked to lie exactly in

```text
ker(q^T,ell^T),
```

and its repaired leakage Gram is proved positive by exact LDL.

### 2. Strict energy angle

For a source/background block it verifies both rational Schur margins
corresponding to

```text
X=S^(1/2) C B^(1/2),
||C||<=1/2,
```

then replays:

```text
global floor                 0
target-floor excess          1
complete target gap >=       1
```

and checks the target/background dual estimate.

### 3. Complete scalarization

A nontrivial three-dimensional exact matrix satisfies

```text
A=a D^(1/2)(I+E)D^(1/2),
a=5,
||E||<=1/10
```

through an exact symmetric row-norm enclosure. The checker verifies the target
upper transfer and the complete complement lower bound

```text
1779/400.
```

## Validation

```text
8/8 deterministic tests pass.
```

The proof boundary is finite algebra only. No production CCM matrix, radial
PSWF, Weil-form value, or RH implication is numerically evaluated here.
