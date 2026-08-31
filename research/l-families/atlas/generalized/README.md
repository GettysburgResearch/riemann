# Generalized L-object Gate-0 packets

Status: **reviewed local/global boundaries, a classical signed parent, and
an actual global period quotient; no new automorphic L-function or external
novelty claim**.

For the latest six-hour pass and its thirty-seven scientific replay modules,
start with [SIXHOUR_PASS3_RESULTS.md](SIXHOUR_PASS3_RESULTS.md). It includes the
exact Segre bridge, higher-rank purity chambers, all-fixed-depth flag ladder,
fixed-weight complex-subspace divisors, source-first theta completion and its
positive-source zero firewall. Four separately reviewed analytic notes
also expose off-central zeros of a native restriction and prove a real
off-central pair in each proper coefficient-source quotient for EVERY
j>=1 and even k>=96j. They do not add computational modules, establish
simplicity, settle weight24 or transfer the period-side12j/k location law.
The thirty-seven-module panel passes 962 tests
and all producer checks in both normal and optimized Python.

The earlier twenty-seven-packet result and historical open gates are preserved
in [CONTINUATION_RESULTS.md](CONTINUATION_RESULTS.md). The following introduction
describes that earlier stage; its queue is superseded by the latest map.
The [all-weight cusp-flag family](CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md)
extends the [weight-24 quotient](RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md).
Its [positive-spectrum boundary](CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md)
separates real positivity and monotonicity from a positive Laplace spectrum.
The [effective derivative certificate](CUSP_FLAG_EFFECTIVE_NEGATIVE_DERIVATIVE.md)
now gives an exact wrong-sign derivative for the actual weight-24 quotient.
The [signed divisor explicit formula](CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md)
retains the fractional-frequency atom and both gamma ladders.
The [signed counting law](CUSP_FLAG_SIGNED_RIEMANN_VON_MANGOLDT.md)
counts zeros minus poles. The [full-period real-zero theorem](CUSP_PERIOD_OFF_CENTRAL_REAL_ZEROS.md)
forces off-central real zeros at k=12d>=6144 without claiming they survive
in the quotient.
The [uncancelled quotient-zero theorem](CUSP_FLAG_UNCANCELLED_OFF_CENTRAL_REAL_ZEROS.md)
pays that separate noncancellation obligation. Its
[effective endpoint theorem](CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md) and
[all-weight extension](CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md) prove an
actual reflected quotient-zero pair for every even k>=65536.
The [local simplicity theorem](CUSP_FLAG_LOCAL_SIMPLE_ENDPOINT_ZERO.md)
separately proves eventual uniqueness, simplicity and reality in each fixed
shrinking disc around 12/k and 1-12/k. Its sufficient threshold is not
computed; 65536 is an existence bound, not a simplicity bound.
The [native denominator-pole theorem](CUSP_FLAG_NATIVE_DENOMINATOR_POLES.md)
now proves an eventual simple real reflected pole pair near 24/k and
1-24/k. It pays the entire higher-flag correction and a positive surviving
cross-period; no effective pole onset or global pole census is claimed.
Each has an independent exact-source audit in the continuation map.
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
