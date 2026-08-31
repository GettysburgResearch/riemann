# Independent exact-SHA review: fixed26 polynomial Xi transport

Verdict: **PASS** on scientific source
2a27043c73cded47c2804ba50b9b1001145a0a82.

Immediate prototype parent:
9cb2989fedf3d5624b8c1f492d4c5b52ecae14bb.
Preregistration:
0cc801421768e3e42ebf0f1c7960081707e52968.
Five-file authoring base, accepted JP:
96543552b5bc5976d96c35123bfb82e609a27972.

No actionable mathematical or release-contract defect was found. No frozen
scientific file was changed, and there was no author coordination for proof
acceptance. The separate independent calculation was completed and frozen at
36637f833352d937ce4bdca53e0964b4e1c5bfe0 BEFORE this review read the finished
extension. The eight-success report had already been disclosed, so this is
not a blinded prediction.

## 1. Complete proof and fixed-source scope

I read the complete169-line proof,442-line producer,147-line tests and
140-line manifest, and loaded and checked the entire compact fixture.
The accepted JP proof/review and the load-bearing QT critical-point and
full-cover arguments were read. The extension changes the selected index
to the complete fixed26-point loop; it does not change the local theorem.

For each inherited REAL critical point t, the exact identity f6(t)=0
cancels the constant and linear critical terms BEFORE numerical evaluation.
With g=f5, a=g(t), c=g''(t), the quadratic factors as

    P(w)=(c/2)(w-i*y)(w-i*(lambda+d)).

The assumptions ac<0, 0<2q<lambda and 0<r<min(y,2d) give a unique model
root in the upper-half-plane disc and the lower margin |c|r(d-r/2).
The remainder coefficient of w^2 is -i*lambda*f8(t)/2; at n>=3 it is
[f^(n+5)(t)-i*lambda*f^(n+6)(t)]/n!. The factorial shifts are correct.

The Cauchy tail begins at n32 in BOTH differentiated series. The factors
5!*binom(37,5)/(R^5(1-x)^6) and
lambda*6!*binom(38,6)/(R^6(1-x)^7), multiplied by M*x^32, follow from
the all-j binomial product inequality, not finite enumeration.
Every true circle point has |w|<=h<R=7/8. The proof correctly does NOT
assume that every corner of an outward rectangular arc enclosure lies
inside that Cauchy disc.

All64 closed angular intervals cover the whole circle, including shared
endpoints. Complete strict comparison gives one zero counted with
multiplicity, hence a SIMPLE companion zero. The separate whole-parent
rectangle comparison identifies it with the existing HA root for every
admissible unknown t,y,r. Containment alone is not a certificate.
The separate C5/R0/C0 nonvanishing guards remain inherited from HA;
they are not inferred from the polynomial remainder lemma.

There is no innerness or RH premise in this finite local argument.
A nonreal zero of f5-i*lambda*f6 is not an off-line zero of classical Xi.

## 2. Independent primitive reconstruction, with disclosed lineage

The independent helper is adapted from the root's accepted JP review
f77477c061e0e9e5ce340ee810254ddd50fad32f, not from the JX producer.
It imports NO JP/QT/HA/OA author module. Its independent inputs remain the
accepted JP/QT sources and the frozen extension design, not extension
values or numerical helpers.

It uses the reflected formula xi_R(1/2-i*z), which equals the literal
source by the completed functional equation, including at complex z.
The series derivative uses the corresponding -i chain factor. It uses
the SAME pinned python-flint0.9.0/FLINT3.6.0 implementation; this is not a
second gamma/zeta library or a formal verification of that library.

At fixed1024bits, with no fallback or pointwise tuning, it freshly computes:

- All26 critical-point Rouche recertifications on the original tiny discs.
- All26 complete40-term signed jets over the full real critical intervals.
- All26 NEW full16x16 outer covers:6656 reflected scalar evaluations,
  with the original center uncertainty and literal source-domain guards.
- All1664 arc bounds by ascending powers and direct summation, rather
  than Horner, using N32, ratio1/2, R7/8 and the same64 closed arcs.
- All26 full-parent rectangle comparisons.

Every prerequisite and containment check passes. Exactly the same eight
complete circles certify:17,18,19,20,21,23,24,25. This is the known control19
plus SEVEN of the other25 fixed source points. All18 other points remain
unresolved. The independent partial-arc counts are39,42,51 at12,13,22,
and zero at other unresolved points:644/1664 in total.

The author's counts are41,44,53 at those three points, and650/1664 total.
The difference is expected for DISTINCT valid512-bit/Horner/inherited-cover
and1024-bit/direct-power/fresh-cover enclosures. It is not concealed or
converted into a claim of exact endpoint reproduction. The independent
worst error/margin upper bound among the eight successes is below0.992543.
The independent display ratios are rounded OUTWARD to2^-64; all actual
acceptance comparisons precede that display rounding and use exact
rational endpoints of directed balls.

The independent report and its normal/-O replay are preserved from the
preparation commit. Its complete payload SHA256 is

    cfa0f3bc2196c0476e912b04ee8e4692a6929bb7370e327fa7dc92f006d0875b.

## 3. Source, compact-fixture and prototype audit

The frozen-source review helper imports no author producer. It verifies
all five scientific files against exact Git bytes, all6 direct bindings
and46 transitive commit/path versions, four current artifact seals and
the canonical payload. Actual Git commit objects and canonical relative
paths are checked. The pinned44-file native-runtime identity is tied to
the freshly replayed independent calculation and matches the manifest.

The helper independently checks ALL1664 stored strict inequalities and
statuses, all26 rational Cauchy-tail upper bounds, all26 exact
whole-rectangle displacement bounds, complete ordered point/arc coverage,
the known-control/25-point denominator and exact inherited QT/HA records.
Every declared full cover is the original512-bit256-cell source cover.
The preserved real coefficient intervals are canonical and complete.

The full signed-jet hash and full64-arc stream hash at index19 agree exactly
with the accepted JP fixture. The producer reconstructs those streams,
and every other point's full stream, before compacting. A stream hash is
not substituted for numerical reconstruction.

Source metadata disagreement raises RuntimeError, which is NOT caught
as an unresolved criterion. Ordinary arithmetic/geometry failures retain
their failure reason and all64 not-evaluated slots when contour evaluation
cannot begin. Completed unsuccessful arcs remain explicitly unresolved.
The actual fixed panel has no guard failure.

The prototype-to-science producer delta is precisely the replacement
of y/2 by the literal JP operation qarb(RATIO)*y. These are the same
mathematical radius but need not have identical directed-ball endpoints.
The known-control full-stream check correctly exposed the differing
radius/margin endpoints. The repaired source reruns all26 points and
preserves the prototype history; it does not retune the criterion.
The final five-file state, not the failed prototype artifact, is accepted.

Science fixture LF SHA256:

    9e60f5d7dca44eca9323ec32500bc9b5dd10c8a83aae2fdcec07f0669428e94a

Science payload SHA256:

    a6fc98cd4cfe8c9b526dd8b0e738ce84d6e2edd0cf45c8951f925743736a736a

The46-version source catalog's independently computed SHA256 is

    978b1b718aa5c58840ba5877d737ee8b79fb4f11d69bd27c05a3d6ed616be4d6.

## 4. Exact release replay and hostile checks

The frozen16-test suite passed normally in104.238s and under -O in104.909s.
Both producer checks and all four LF-normalized fixture/manifest emissions
match exactly; the six producer invocations took87.980s in this review.
The independent frozen-source/rational-audit helper also passes in both modes.

An additional review harness rejects20 strict malformed/type/cap/index
inputs in EACH mode. It also rejects two FULLY RESEALED candidates in
EACH mode through the unpatched full26 reconstruction: removing all
displayed Cauchy tails while consistently updating errors/decisions/
summaries, and substituting the known positive point's record for the
unresolved physical point22. No source function, build result or primitive
is mocked or cached to obtain those fresh rejections. These are additional
to the two full-reconstruction resealed attacks already in each test run.

Ruff, the complete JP-base-to-science whitespace check, review whitespace,
scientific byte immutability and control-character checks pass.
The review-only files do not change or republish the scientific packet.

## 5. Accepted limit

This is a complete fixed finite source panel with seven new CRITERION
successes plus one separately counted known positive control. The roots
were already in HA; no new independent zero census is claimed.
Eighteen unresolved sufficient tests are not impossibility theorems.
This result neither defeats eighteen old-criterion obstructions nor makes
that different criterion necessary for polynomial transport.

No growing-height/cofinal transport, homotopy, physical capture, innerness,
RH, zero-purity claim or external novelty certification follows.
The exact eight local identifications, their source guards and their
complete declared denominator are the accepted result.
