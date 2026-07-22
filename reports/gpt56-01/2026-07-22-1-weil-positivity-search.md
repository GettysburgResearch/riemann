# Agent report — initial finite Weil witness route

Agent: `gpt56-01`  
Issue: #1  
Branch: `agent/gpt56-01/1-weil-positivity-search`  
Date: 2026-07-22

## Starting hypothesis

A finite negative value of a compact-support, cutoff-free Weil quadratic form
is a stronger first counterexample target than an unstructured off-critical
zero scan: it can be represented by a finite vector and checked using interval
matrix entries plus exact rational arithmetic.

## Approaches attempted

1. Read the complete project README and confirmed that no state files, issues,
   reports, or pull requests existed.
2. Created and claimed Issue #1 as `gpt56-01`.
3. Surveyed current primary work on finite Weil matrices, the exact
   Guinand--Weil dictionary, archimedean tail order, and prime-threshold
   structure.
4. Reconstructed a cutoff-free finite matrix implementation from released
   closed forms using mpmath, avoiding finite-T quadrature.
5. Added invariant and adversarial tests.
6. Ran integer and off-integer precision-ladder scans.
7. Designed and implemented a separate exact dyadic Rayleigh-certificate
   verifier using only Python integers and fractions.
8. Bootstrapped the project-state and claim registries.

## New results

### Proposed logical criterion

`L-0001` records the one-way implication: under the exact finite dictionary and
autocorrelation identity, a strict certified negative finite matrix value
implies RH is false.  This is a complete-looking reduction but remains
`PROPOSED` pending independent audit of the substantial dependencies.

### Empirical computation

X-0001 scanned 82 `(c,N)` cells:

- 24 baseline cells through `c=13`, `N<=8`;
- 42 extended integer cells through `c=100`, `N<=12`;
- 16 off-integer logarithmic-grid cells through `c=100`, `N=8`.

Every cell was repeated at higher precision.  There were zero empirical
negative cells and zero sign-instability cells.

This result is finite, empirical, and negative.  It must not be interpreted as
support for RH.

### Exact certificate checker

The algebraic certificate layer is exact.  Given dyadic intervals for every
matrix entry and a dyadic vector, it computes the full Rayleigh interval with
`fractions.Fraction` and accepts only a strict negative upper endpoint.  The
committed negative certificate is synthetic and tests the checker only.

### Tests

Fourteen tests passed in the working environment.  They cover matrix invariants,
precision-sensitive residuals, exact interval arithmetic, malformed
certificates, and zero-boundary rejection.

## Candidate counterexamples

None.  No `Z-####` ID was assigned.

## Certified computations

No zeta/Weil matrix sign was certified.  Only the synthetic exact arithmetic of
the standalone certificate checker was certified by construction and tests.

## Failed approaches

A denser 31-point continuous grid at `N=8,12` with 90/130 decimal digits did not
finish within the execution budget.  The process was stopped without output.
The failure is computational scaling, not evidence about the matrix.

A local GitHub clone was unavailable in the execution environment, so the
branch and files are published through the GitHub connector rather than a
normal local push.

## Potential errors

- Recent source formulas may have a sign or normalization error not caught by
  invariants.
- The mpmath geometric-series truncation bounds are analytically conservative
  but numerically non-interval.
- Agreement with a released implementation is not independence when formulas
  share a source.
- High-precision eigensolvers can return persuasive values for a wrongly
  assembled matrix.
- The simple full-inertia computation is not optimized and will not scale to
  large bands.

## Files changed

- foundational state and registry files;
- D-0001, L-0001, and M-0001;
- X-0001 code, tests, result artifacts, and certificate checker;
- this report;
- pull-request template.

## Claims affected

- Added `D-0001` (`PROPOSED`).
- Added `L-0001` (`PROPOSED`).
- Added `M-0001` (`PROPOSED`).
- Added `X-0001` (`EMPIRICAL`).
- Added project warning `R-0001` in `NEGATIVE_RESULTS.md`.

## Recommended next actions

1. Assign Q-0004 to an analytic verifier who does not use the X-0001 derivation.
2. Assign Q-0001 to an Arb specialist and define a deterministic exporter for
   the dyadic certificate schema.
3. Implement fast continuation in `u=log(c)` and constrained pole-neutral
   searches.
4. Open independent issues for direct argument-principle zero search and an
   arithmetic finite-witness audit.
5. Review whether the finite family is complete enough to justify resource
   escalation; do not confuse search convenience with likelihood of success.

## Organizational improvement ideas

The discovery/enclosure/checking split should become standard for computational
proof claims.  A small checker should be reviewable without the search code,
and candidate promotion should require certificate provenance plus independent
reconstruction.
