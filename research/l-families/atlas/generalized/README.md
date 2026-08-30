# Generalized L-object Gate-0 packets

Status: **proposed exact local mathematics; external novelty unreviewed**.

The independent continuation
[Multiplicative recurrence preservers and mixed-rank determinant parents](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md)
classifies all continuous multiplicative complex maps using one
nondegenerate shifted-circle recurrence test, gives sharp generic complex
orders and collision semantics, and proves the finite graded determinant
boundary for arbitrary mixed input ranks. Its exact controls and source
locks are in `multiplicative_recurrence_mixed_parents.json`; this is a local
representation/recurrence result, not a new global L-function. The frozen
eleven-packet base below is retained unchanged.

For the current eleven-packet result and the next global completion gates,
start with [CONTINUATION_RESULTS.md](CONTINUATION_RESULTS.md).
The packet introductions below and the wave-2 research map record the
earlier six-packet stage; their open-work lists are superseded by that
continuation checkpoint.

This directory contains bounded theorem and obstruction packets for issue
[#764](https://github.com/gfreund123/riemann/issues/764). It reuses the atlas
normalization and provenance conventions but does not extend the atlas into a
catalogue of generalized zeta functions.

The first packet is
[`NONINTEGRAL_LOCAL_POWER_RATIONALITY.md`](NONINTEGRAL_LOCAL_POWER_RATIONALITY.md).
It classifies rationality of one positive-chamber, determinant-one local
coefficient-power series. Here \(x>2\) is the hyperbolic, non-tempered
chamber, not the normalized tempered \(\mathrm{GL}_2\) trace chamber
\([-2,2]\). The result is local: it constructs no global Euler product,
completion, automorphic lift, or zero theorem, and it is not an automorphic
nonintegral-symmetric-power no-go theorem. Its inherited inputs are recorded
in the colocated
[sources manifest](nonintegral_local_power_rationality.sources.json).

The second packet is
[IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md](IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md).
For a determinant-one tempered recurrence with
\(\theta/\pi\notin\mathbb Q\), it proves that
\(\sum_r |u_r|^\lambda T^r\) is rational exactly for even nonnegative
integers \(\lambda=2m\), with minimal local order \(2m+1\). It treats
absolute powers rather than complex powers, excludes rational rotations,
and makes no global or novelty claim. Its inherited inputs and nearby
almost-periodic-series prior art are recorded in the colocated
[sources manifest](irrational_rotation_absolute_power_rationality.sources.json).

The third packet is
[RATIONAL_ROTATION_BRANCH_CENSUS.md](RATIONAL_ROTATION_BRANCH_CENSUS.md).
It closes the complementary rational tempered chamber: exact zero classes,
minimal periods for absolute and fixed-branch complex powers, every
\(\lambda=0\) zero-value convention, and the root-of-unity collision spectrum
for positive integer powers.  It also separates the scalar observable from
its finite-dimensional symmetric-power state-space parent.  Pointwise
periodicity alone is not a uniform local-degree theorem as the angle
denominator grows; the sixth packet below supplies the missing reduced-degree
argument.  The exact inherited files and nearby literature are recorded in
its colocated [sources manifest](rational_rotation_branch_census.sources.json).

The fourth packet is
[IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md](IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md).
For any fixed real-axis logarithm branch, \(\lambda=0\) or
\(\operatorname{Re}\lambda>0\), it proves that the signed complex-power
series on an irrational tempered orbit is rational exactly at nonnegative
integer exponents.  At \(k\), its minimal order is \(k+1\), and it is a
weighted resolvent trace of the genuine \(\operatorname{Sym}^k\) local
state-space parent.  The noninteger corollary excludes only constant
finite-dimensional linear realizations; it does not exclude infinite-rank or
categorical parents.  Exact dependencies and branch-cut prior art are in the
colocated [sources manifest](irrational_rotation_principal_complex_power_rationality.sources.json).

The fifth packet is
[TRANSFER_MATRIX_SYMMETRIC_PARENT.md](TRANSFER_MATRIX_SYMMETRIC_PARENT.md).
It replaces a fitted scalar recurrence by the honest local parent
\(\operatorname{Sym}^k(A)\), proves the exact matrix-coefficient identity,
and isolates a load-bearing determinant effect.  Across all degrees through
\(d\), a generic rank-\(n\) torus has \(\binom{n+d}{n}\) distinct weights,
whereas the determinant-one subtorus has
\(\binom{n+d}{n}-\binom{d}{n}\).  This is standard local tensor and
weight-lattice algebra, not a global symmetric-power \(L\)-function or a
novelty claim; degeneration and cancellation loci are retained explicitly.

The sixth packet is
[RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md](RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md).
It proves the sharp uniform-L3 classification over all reduced rational
angles.  For \(\operatorname{Re}\lambda>0\), absolute powers have uniformly
bounded reduced degree exactly at positive even integers, and a fixed
real-axis branch has uniformly bounded degree exactly at positive integers.
The sharp bounds are \(2m+1\) and \(k+1\); at the excluded absolute exponent
\(\lambda=1\), every denominator \(b\) has full recurrence order \(b\).
The obstruction is finite-dimensional and local, not a global
\(L\)-function or infinite-parent no-go theorem.

The [wave-2 research map](WAVE2_RESEARCH_MAP.md) consolidates all six
packets, the primary-literature boundary, held-out families, L0--L9 status,
four broader deformation axes, and a ranked continuation queue.  It is a
programme map, not another theorem packet.
