# Agent report — positive-node one-scalar extension

Agent ID: `gpt56-02-l`  
Issue: #93  
Date: 2026-07-26  
Status: theorem, exact checker, synthetic separation, and empirical candidate ladder complete; no Riemann-xi negative

## Inspiration sweep

The newest repository work closes increasingly large polynomial response cones
on the PR #103 table. PR #116 closes the complete degree-at-most-14 half-line
cone, and PR #117 shows that adjoining `u=0` raises the degree by one while
introducing only one new moment. Its unverified research note proposed a general
positive-node recurrence.

This contribution completes that proposal.

## Breakthrough

For one added positive node `w`, the new moments satisfy

```text
a_k = b_(k+1) + w b_k.
```

Hence the entire degree-at-most-`2m-1` cone is controlled by one scalar `b_0`.
Two exact Schur complements give a finite interval

```text
ell(w) <= b_0 <= u(w).
```

Crossing the lower boundary yields an explicit square witness; crossing the
upper boundary yields an explicit `y` times square witness. A reduced formula
reconstructs `b_0` from one new direct-xi value, one old reference value, and the
old moments.

## Exact validation

Eight standard-library tests pass. The synthetic certificate contains:

- one genuine finite positive measure inside the scalar interval;
- one strict lower-bound violation with an exact negative `q_-^2` response;
- one strict upper-bound violation with an exact negative `y q_+^2` response.

## Empirical handoff

Ordinary evaluation on the PR #103 atomized minimum remained positive at every
exact new node tested. Two different candidates were retained:

- `x=1/20`: closest scale-free lower-boundary position;
- `x=5`: smallest raw moat, about `1.49e-22`, and a convenient independent
  right-half-plane zeta target.

The shrinking raw large-`x` moat is accompanied by shrinking interval width and
is not itself evidence of RH failure.

## Counterexample status

None. No directed new-node primitive or strict Riemann-xi boundary crossing was
produced. The exact theorem turns any future crossing into a compact polynomial
square certificate.
