# Cauchy determinant and rank-extension checkpoint

This checkpoint continues PR #780 from the two-ended frontier of `T-105670`.

## All-rank determinant theorem

The determinant of the canonical-overlap matrix exceeds the determinant of
the current compression at every positive height. The ratio is one explicit
product of strictly positive diagonal and complex-pair Cauchy gains.

This proves constant-one CTI at geometric-mean strength and gives a trace CTI
region whenever the current AM/GM spectral dispersion is smaller than the
explicit determinant gain.

## Rank-extension localization

Adding one exponential changes the trace defect by

```text
old-deep projection of the new shallow residual
+ new-shallow projection of the new deep residual
- one-step current mass of the new shallow residual.
```

A scalar trial vector isolates the possible reverse-moment deficit. The only
additional resource needed is the return of the new deep residual into the old
shallow model space.

The resulting gate `REC105681` is a one-factor statement. If it holds at every
step in one packet ordering, full finite CTI follows by induction.

## Boundary

The determinant theorem and extension ledger are exact. Return compensation,
full arbitrary-rank trace CTI, the cofinal Xi passage, pointwise localization,
and RH remain open.
