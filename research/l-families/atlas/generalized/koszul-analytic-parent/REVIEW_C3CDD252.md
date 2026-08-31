# Independent exact-SHA review: constructible pole-clearing source

Reviewed scientific freeze: `c3cdd2528595cbf22c31d88a40c8a611b6385752`.

Inspected the complete `CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md`, including the final finite-even-grade ladder, the full `constructible_pole_clearing_replay.py`, all 23 tests in `tests/test_constructible_pole_clearing.py`, and the replay scope. Confirmed the committed five-file packet. Paths are under `research/l-families/atlas/generalized/koszul-analytic-parent/`.

## Independent proof findings

The construction defines each finite grade before taking Euler factors. Ordinary sheaf extension is followed by tensor and symmetric algebra on the standard sheaf placed in grading degree two. At each ramified stalk this gives `A^I tensor Sym(S^I)`, not invariants of the generic tensor algebra. The old C2 degree-three dimensions 23 and 26 correctly distinguish the two operations. The new-zero and infinity rules retain their full original invariant factors; the added standard stalk has dimension zero at infinity. No perverse or derived extension convention is silently substituted.

The full-place product of the added standard symmetric factor is the actual Artin/cohomological polynomial `P_E(z^2)`. Thus the previously specified polynomial modification has an independently defined constructible graded source. It is a new algebra and function, not an equality with the original coherent source.

The exact analytic dichotomy follows from the frozen divisor theorem. Clearing grade two leaves a genuine grade-four pole whenever either elliptic sector has a nonresonant eigenvalue, giving radius `Q^(-1/8)`. In the fully resonant case the effective prior theorem gives radius one and the unit-circle meromorphic natural boundary. The different coefficient root-growth statements refer to the new function; the original quarter-power growth is unchanged.

For each fixed even N, adjoining the actual nontrivial isotypic modules in grades at most N gives the stated finite polynomial multiplier and the guaranteed disk `|z| < Q^(-1/(2(N+2)))`. This is not asserted to be the exact radius in every case. The proof correctly refuses to infer an infinite-cutoff analytic limit or a larger domain for the old Lie operator.

## Independent code review and repaired finding

The producer authenticates the prior source before import. The complete local checks include both quadratic signs, old C2, the new quadratic branch and both infinity Frobenius cosets. The split/nonsplit infinity comparisons distinguish dimensions from traces. The first two global coefficients are independently assembled from all retained rational stalks and the unchanged degree-two closed-place first-grade contribution, then compared with the standard cohomological factor. Existing fields only are used.

During review I found that the first candidate assigned elliptic multiplicities `m_D=m_E=1` to every native source without checking whether its two elliptic polynomials share roots. This could overstate a reported grade-four pole order, although it did not affect the proof of a surviving pole. The final code uses `m_E=1` and `m_D=int(P_D==P_E)`, valid for the simple irreducible elliptic quadratics over the declared nonsquare fields. The corresponding test now expects one plus the actual coincidence indicator. I read this repair in both producer and test. No remaining code or coverage blocker was found.

## Execution and limits

I performed independent proof/code reading and no computation. The parent reports Ruff, 23 ordinary tests in 0.911 seconds, 23 optimized tests in 0.884 seconds, and all three producer modes passing, followed by successful final source-binding checks. These execution results are parent-reported.

This packet realizes a particular operation in a specified category of degreewise constructible sheaf algebras. It is not a universal tensor-commutation statement, a new Koszul presentation, a single finite-rank infinite graded sheaf, an archimedean completion, a native retained-gamma decoder, or an RH consequence. The finite-ladder corollary is proved symbolically; no empirical all-grade extrapolation or infinite analytic completion is claimed.

No remaining proof or code blocker found.
