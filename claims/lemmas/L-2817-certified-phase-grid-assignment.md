# L-2817 — Certified nearest-grid assignment from a phase interval

Claim ID: L-2817  
Title: Algebraic phase intervals admit a unique grid bin except at explicitly detected boundaries  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: L-2813; L-2815; elementary interval arithmetic  
Scope: phase-grid production for complete fixed-vector prime sums  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Fix `M>=2` and grid nodes

\[
 \theta_j=\frac{2\pi j}{M}\pmod{2\pi},
 \qquad 0\le j<M.
\]

Suppose an outward real interval `Phi=[phi_-,phi_+]` contains an exact phase `phi`. Let `G` be an outward interval for the scaled phase

\[
 g=\frac{M\phi}{2\pi}.
\]

For an integer `j`, if there exists an integer translate `nM` such that

\[
 \boxed{
 G\subset
 \left(j+nM-\frac12,
       j+nM+\frac12\right),
 }
\]

then `j mod M` is the unique nearest phase-grid node, and the exact residual

\[
 \delta=\phi-\theta_j-2\pi n
\]

lies in `[-pi/M,pi/M]`. An outward residual interval is obtained by subtracting outward intervals for the selected node and period.

If no strict containment can be proved, a proof-producing evaluator may do either of the following:

1. evaluate the term with the direct phase backend; or
2. assign the term to every intersected adjacent bin and take the interval hull of the resulting term enclosures.

Selecting a midpoint bin in the unresolved case is not valid.

## Proof

The open intervals

\[
 \left(k-\frac12,k+\frac12\right),
 \qquad k\in\mathbb Z,
\]

are the Voronoi cells of the integer grid. Strict containment of `G` in the cell centered at `j+nM` proves that every possible exact scaled phase in `G` has the same unique nearest integer. Scaling back by `2*pi/M` gives the residual bound and the chosen grid node modulo `M`.

If the interval touches or crosses a half-integer boundary, both neighboring nodes are compatible with the available enclosure. Direct evaluation contains the term by construction. Alternatively, the union of all compatible bin-specific enclosures contains the term, and its interval hull is therefore valid.

## Target consequence

For unfinished PR #65 segments, L-2815 gives a truncation contribution to the phase radius below `10^-23`. At `M=32768`, the grid spacing is approximately `1.9*10^-4`. Thus series truncation alone is more than nineteen orders of magnitude smaller than one grid cell.

This does not prove that no exact phase lies near a boundary. It proves instead that ambiguity is sparse and mechanically detectable. Every ambiguous term can be sent to the already reviewed direct MPFR evaluator without changing the test function or completeness claim.

## Deposition-knot analogue

The same rule applies to the support coordinate

\[
 r_q=\frac{K\log q}{\log c}.
\]

If its interval lies strictly inside `(d,d+1)`, the two active autocorrelation knots are uniquely `d,d+1`. If it intersects an integer, hull both neighboring interpolations or use the direct evaluator. No midpoint floor is allowed.

## Certificate metadata

Every accelerated shard should record:

- total prime count;
- unique phase-bin assignments;
- direct phase fallbacks;
- multi-bin hulls, if enabled;
- unique support cells;
- deposition-knot fallbacks or hulls;
- maximum phase interval width;
- maximum support-coordinate interval width;
- grid size, Taylor order, and series orders;
- all vector, parameter, normalization, and producer fingerprints.

A nonzero fallback count is not a failure. An unrecorded ambiguity is.

## Gap audit

- The lemma assumes the input phase interval is valid.
- Reduction modulo `M` must preserve the exact integer translate used in the residual.
- A point exactly on a Voronoi boundary may be assigned to either adjacent bin only if the corresponding residual and Taylor enclosure are evaluated consistently; hulling is simplest.
- The phase-grid Taylor remainder of L-2813 must still be added.
- A unique phase bin does not imply a unique deposition cell; both tests are required.

## Adversarial tests

1. Place an interval strictly inside one grid cell and recover its unique index.
2. Place intervals touching the left and right half-integer boundaries and require fallback.
3. Cross the `0 mod M` wrap and verify the integer translate is preserved.
4. Force a support-coordinate interval across an integer knot and require a two-cell hull.
5. Mutate the grid size after producing a shard and require fingerprint rejection.

## Suggested next attack

Implement the segment-centered evaluator as a third producer backend. On each ordinary prime, attempt algebraic log and reciprocal-square-root evaluation, unique support-cell assignment, and unique phase-bin assignment. Invoke the direct MPFR term evaluator only on a failed uniqueness test.