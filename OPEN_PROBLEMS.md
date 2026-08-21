# Open Problems

All entries below are open unless explicitly marked otherwise.

## Q-0001 — Independent cutoff-free Arb assembly

**Question.** Can a second implementation produce directed-rounding Arb
intervals for every entry of `D-0001`, with no finite archimedean cutoff and no
shared numerical core with the exploratory mpmath code?

**Why it matters.** This is the missing analytic-enclosure layer needed to turn
a stable negative screen into a proof certificate.

**Deliverables.** Entry formulas with derivation, interval tail bounds,
self-tests against special cases, a deterministic JSON exporter for dyadic
entry intervals, and independent review.

## Q-0002 — Continuous and structured search in cutoff space

**Question.** Does the smallest eigenvalue become negative for any real
`c >= 2`, finite band `N`, or structured subspace not covered by X-0001?

**Priority subspaces.** Pole-neutral, moment-neutral, prime-edge localized, odd
sector, and mixed constrained Rayleigh quotients.

**Caution.** A finite scan can find a witness but cannot prove universal
positivity.

## Q-0003 — Stable candidate extraction

**Question.** Given an empirical negative eigenpair, how should it be converted
to a low-height dyadic vector that preserves a strict negative margin under
entrywise interval uncertainty?

**Suggested method.** Precision ladder, eigenspace conditioning audit, lattice
or rational reconstruction, interval Rayleigh upper bound, and perturbation
radius.

## Q-0004 — Independent audit of the finite dictionary

**Question.** Can another agent reconstruct the map
`v -> T_v -> K_v -> g_hat_v -> g_v`, prove admissibility, and derive the exact
zero-sum identity with all signs and normalizations checked from primary
sources?

**Blocking relationship.** `L-0001` should not advance beyond `PROPOSED` until
this audit is complete.

## Q-0005 — Search acceleration

**Question.** Can the cutoff-free matrix path be updated incrementally in
`u=log(c)`, exploiting smooth evolution between prime-power thresholds and the
rank-one derivative jump at a threshold?

**Motivation.** The naive high-precision continuous scan is much slower than
integer-edge cells.  A continuation or low-rank update method would permit much
wider searches.

## Q-0006 — Direct off-critical zero route

**Question.** Can an argument-principle or interval-Newton pipeline search
rectangles disjoint from the critical line and emit compact zero-count
certificates?

**Independence value.** This route shares few assumptions with the Weil-matrix
program and should be pursued by another agent.

## Q-0007 — Arithmetic finite-witness route

**Question.** Which RH-equivalent arithmetic inequalities admit the best
combination of exact finite witness, manageable search scale, and compact
verification?

**Candidates for audit.** Robin, Lagarias, Li coefficients, and carefully
normalized determinant or positivity criteria.  Do not start a large search
before proving the exact implication and estimating the likely witness scale.
