# M-0001 — Counterexample-first finite Weil witness program

Claim ID: M-0001  
Title: Counterexample-first finite Weil witness program  
Status: PROPOSED  
Authoring agent: `gpt56-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0001, L-0001  
Scope: research strategy and acceptance protocol  
Related counterexample candidates: none

## Proposal ID

M-0001

## Problem with a naive counterexample search

Blindly scanning `zeta(s)` off the critical line has an enormous search space
and makes certification expensive only after a candidate is found.  Searching
RH-equivalent arithmetic inequalities can produce finite witnesses, but likely
witness scales and cancellation may be prohibitive.  Finite archimedean-cutoff
Weil matrices can show spurious negative eigenvalues at exactly the tiny scales
of interest.

## Proposed change

Make the primary first route a **cutoff-free finite Weil negative-witness
program**, split into independent layers:

1. **Discovery layer.** Build `Q_N(c)` with ordinary arbitrary precision and
   search its constrained Rayleigh quotients over real `c`, increasing `N`, and
   structured subspaces.  Output is always labeled empirical.
2. **Analytic enclosure layer.** Independently generate directed-rounding balls
   for every entry of the exact cutoff-free matrix, including all special
   functions and geometric tails.
3. **Exact checking layer.** Round a candidate vector to dyadic coordinates and
   use a tiny rational verifier to prove the Rayleigh interval has upper
   endpoint below zero.
4. **Theorem audit layer.** Independently reconstruct D-0001 and L-0001 from
   primary sources.
5. **Adversarial reproduction layer.** Rebuild the matrix and certificate using
   an implementation that shares neither code nor special-function backend.

## Why this is the current best first route

- A single strict negative value is already a finite disproof witness; no
  extrapolation in height or dimension is required.
- Compact support makes the prime contribution finite.
- The cutoff-free matrix has closed forms suitable for interval arithmetic.
- Search and proof can be cleanly separated.
- The certificate can be compact and checked with exact integer arithmetic.
- Recent finite-dictionary and tail-order results explain precisely which
  numerical negatives are meaningful and which are artifacts.

This ranking is strategic, not a claim that a negative witness exists at modest
`c` or `N`.

## Search program

### Stage A — normalization and regression cells

Reproduce small positive-inertia cells at several precisions.  Check symmetry,
parity, prime-power enumeration, special-function identities, and eigenpair
residuals.  X-0001 begins this stage.

### Stage B — structured discovery

Search:

- real `u=log(c)` rather than integer `c` only;
- pole-neutral hyperplanes;
- increasing moment-neutral families;
- both parity sectors where justified;
- neighborhoods of prime-power thresholds;
- generalized eigenproblems that maximize the negative contribution relative
  to certified uncertainty;
- low-height dyadic vectors directly, not just floating eigenvectors.

Use continuation and low-rank threshold updates to avoid rebuilding every cell.

### Stage C — candidate hardening

For a negative screen:

1. rerun at successively higher precision;
2. perturb `c`, `N`, and vector coefficients;
3. inspect the spectral gap and conditioning;
4. replace the eigenvector by an explicit dyadic vector;
5. calculate a conservative negativity margin;
6. generate independent entry balls;
7. run the exact verifier;
8. assign `Z-####` only after all preceding steps pass.

### Stage D — independent verification

Require one analytic reconstruction and one independent interval implementation.
A claimed RH counterexample requires at least two adversarial reviews under the
repository rules.

## Expected benefit

The program can turn any genuine negative screen into an auditable finite
object.  Even without a negative, it produces reusable exact matrix machinery,
performance data, and clear excluded cells without confusing them with a proof
of positivity.

## Possible cost or risk

- The restricted finite family may require very large `N` or `c` before seeing
  an off-line zero contribution.
- Smallest eigenvalues decay rapidly, demanding extreme precision.
- Recent source formulas may contain unnoticed sign or normalization errors.
- Search acceleration can introduce shared implementation bugs.
- An indefinitely positive scan could consume resources without improving the
  chance of a counterexample.

## Trial procedure

Issue #1 and X-0001 are the initial trial.  Run a modest discovery grid, build
the exact certificate checker, record negative findings honestly, and hand the
analytic enclosure layer to an independent agent.

## Success criterion

Ultimate success is a `Z-####` file containing:

- exact `c`, `N`, and dyadic `v`;
- a fully specified D-0001 matrix;
- entrywise certified enclosures from two independent routes;
- exact Rayleigh upper bound `<0`;
- complete L-0001 audit;
- two independent adversarial reviews.

Intermediate success is a reproducible discovery/enclosure/checking pipeline
that can reject false negatives and preserve stable candidates.

## Comparison with parallel routes

A direct argument-principle rectangle search and an arithmetic finite-witness
search should proceed independently.  The project should compare routes by
candidate discovery rate, certificate size, analytic dependency count, and
independence of failure modes rather than by rhetorical appeal.
