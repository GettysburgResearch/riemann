# R-16205 — Absolute source H4 does not control the normalized arithmetic endpoint remainder

Claim ID: `R-16205`  
Status: **REFUTED AS A RELATIVE PROFILE-GRAM INFERENCE**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01

## Error

For a repaired source `f` with first-alias leakage energy

```text
delta=||r_f||_2^2,
```

the unit profile is `r_f/sqrt(delta)`. Repeated integration by parts therefore
charges

```text
(zeta(4)-1)||f^(4)||_1 / [(2pi v)^4 sqrt(delta)],
```

not the same expression without `sqrt(delta)`.

At gamma=4096 the two repaired columns have

```text
log10 delta_target      approximately -3538.8421,
log10 delta_complement  approximately -3524.1072.
```

Their absolute fourth-derivative bounds are only polynomial, but division by
`sqrt(delta)` changes their logarithmic size to approximately

```text
10^1773.5 and 10^1766.7.
```

Thus the earlier compact ceilings `45000`, `1e-5`, `2e-10`, and `1/40000`
were not valid relative profile estimates.

## What survives

The normalized radial coefficient-tail, frequency-derivative tail,
horizontal-strip tail, and exact first-alias Gram were already divided by the
leakage norm and remain valid.

## Correct production gate

The endpoint/alias remainder must be obtained from the normalized radial
solution itself: retain the normalized endpoint channels and enclose the
remaining exterior radial expansion or interval-ODE tail. An absolute Sobolev
norm of the compact source is insufficient at the superexponential prolate
scale.

No downstream deterministic-error or complete profile-Gram field may be emitted
until this relative radial endpoint ledger and the complete cross-alias operator
bound are both present.
