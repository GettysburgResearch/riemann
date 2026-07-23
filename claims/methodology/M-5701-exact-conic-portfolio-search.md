# M-5701 — Exact conic portfolio search and replay

Proposal ID: M-5701  
Status: PROPOSED  
Authoring agent: `gpt56-06-c`  
Created: 2026-07-23

## Problem with the current process

The project has accumulated many finite RH-valid inequalities on shared data,
but search usually ranks them one at a time: one scalar sign, one eigenvector,
one determinant, or one branch bound. This can discard a real finite
inconsistency when common uncertainty cancels only after several rows are
combined.

Floating LP/SDP solutions also create a new danger: a solver may report a
negative optimum whose rounded multipliers are not nonnegative, not PSD, or no
longer separated after rigorous reevaluation.

## Proposed change

Use a three-layer pipeline.

### Layer 1 — canonical primitive feature table

Evaluate each exact primitive once. Assign stable IDs and preserve joint
uncertainty. Build route-specific rows and affine matrix pencils symbolically
over those IDs.

### Layer 2 — untrusted portfolio nomination

An LP, SDP, eigensolver, rational model, or custom optimizer may choose rows,
nonnegative scalar weights, and low-rank PSD Gram vectors. Optimize a normalized
robust objective using the actual uncertainty model, not midpoint negativity.

For interval boxes, one useful LP normalization is to bound the `L1` norm of the
combined primitive coefficient vector. This targets the L-5702 `L-infinity`
feature-repair moat rather than an arbitrarily scalable raw score.

### Layer 3 — exact replay

1. Freeze exact rational/dyadic weights and Gram vectors.
2. Reconstruct all combined coefficients from source rows.
3. Contract shared primitives before applying enclosures.
4. Verify nonnegative weights and exact PSD Gram representation.
5. Verify exact feature/gate manifest equality.
6. Compute the robust upper endpoint with exact rational support data.
7. Reject if the endpoint reaches zero.
8. Report the scale-invariant feature-repair moat.
9. Reproduce the decisive primitive enclosures independently.

## Expected benefit

- Several individually inconclusive inequalities can combine into a strict
  certificate.
- Common-mode uncertainty is not counted repeatedly.
- Matrix certificates can use higher-rank PSD multipliers instead of one fragile
  eigenvector.
- Solver complexity is moved outside the trusted base.
- The exact checker remains small and route independent.

## Possible cost or risk

A large row library may overfit numerical noise and produce ill-conditioned
weights. Rationalization can destroy a thin moat. Coefficient growth can amplify
special-function uncertainty. Every logical gate used by any positive-weight
row remains a dependency of the portfolio.

## Trial procedure

1. Start with synthetic shared-cancellation and PSD-Gram controls in X-5701.
2. Use the proof-grade Issue #39 feature table after Arb balls are available.
3. Add rows incrementally: scalar, two-channel, secant, barycentric, frozen Pick,
   Stieltjes localizer, selected Loewner minors.
4. Compare best individual robust endpoint with best normalized portfolio.
5. Rationalize at several bit depths and replay exactly.
6. Require a second implementation to reconstruct any strict real-data result.

## Success criterion

A real finalist is promoted only when:

- every used primitive and logical gate is manifest-bound;
- exact weights and Gram factors pass replay;
- the complete joint uncertainty set gives a strict negative upper endpoint;
- a positive feature-repair moat is reported;
- independent primitive evaluation reproduces the certificate.
