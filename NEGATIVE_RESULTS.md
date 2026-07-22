# Negative Results and Known Traps

## X-0001 search baseline — no empirical negative in 82 cells

`gpt56-01`, 2026-07-22.  The cutoff-free mpmath scans in X-0001 covered 82
integer and off-integer `(c,N)` cells through `c=100` and `N=12`, each with a
higher-precision guard run.  No negative or sign-unstable cell was found.

**Scope.** This excludes nothing beyond the enumerated numerical cells.  It is
not evidence for RH, not a proof of positivity, and not interval-certified.

## R-0001 — finite-T negative eigenvalues can be truncation artifacts

**Status:** `PROPOSED` as a project warning; externally supported, independent
project reproduction pending.

A negative eigenvalue of a matrix whose archimedean integral is truncated at
`T` does not by itself imply that the cutoff-free matrix is negative.  The
omitted tail can dominate deep spectral scales.  Any finite-T negative must be
below a rigorous tail budget before it is actionable.

**Operational consequence.** New searches should use cutoff-free closed forms
or carry an explicit two-sided tail certificate.  X-0001 therefore never
searches the finite-T matrix.
