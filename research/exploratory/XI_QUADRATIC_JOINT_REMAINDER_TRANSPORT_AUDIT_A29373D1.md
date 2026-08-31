# Independent exact-SHA review: JRa29373d1

Verdict: PASS in the stated theorem and inherited-data scope.

Scientific source: `a29373d16abcf646cc0f86bd7d3f215e98ed15b0`.
Immediate design parent: `99a7eb0310ca86392ef28b91b7c6d1fe81f35e61`.
Five-file authoring base: `530732c5fd7f50364381f8af50e97ce809b674c5`.
Review worktree: `isolated/jr-audit-pass3`.
The five scientific files are unchanged. This is a separate non-author
review; no acceptance discussion with the author or scientific edit occurred.

## 1. The joint remainder is valid

The note's Section1 has the correct orientation, coefficients and domain.
With g'(t)=0, w=z-t and R=g-i*lambda*g', Taylor's integral formula gives

    g(t+w)-a-cw^2/2
      =w^3/2 * integral_0^1 (1-u)^2 g'''(t+uw) du,
    g'(t+w)-cw
      =w^2 * integral_0^1 (1-u) g'''(t+uw) du.

Subtract i*lambda times the second identity and put tau=1-u. This yields
exactly the joint identity in the manuscript. It is not obtained by
subtracting independent upper bounds.

On |w-iy|<=r, with the source's 0<r<y<lambda,

    |tau*w/2-i*lambda|
      <= lambda-tau*y/2+tau*r/2.

The modulus at the center simplifies with the displayed sign because
lambda-tau*y/2>0. Integration against tau gives
lambda/2-(y-r)/6. This factor is positive, at least lambda/3.
Every segment point t+(1-tau)w lies in |z-t|<=y+r, so the SAME M3
disc bound suffices. No translation-invariance or smaller-region
assumption is being imported without proof.

QT's exact quadratic has roots iy and i(lambda+d), separated by2d.
The unchanged lower bound |c|r(d-r/2) therefore combines with the new
error bound to give one zero counting multiplicity, hence a simple
upper-half-plane zero, whenever the strict new inequality passes.
No nonvanishing conclusion for another numerator is automatic.

The old and new factors differ by exactly y/3>0. Thus this is a strict
improvement of the sufficient theorem, not merely a renamed criterion.
The nonnative cubic g(w)=3/8-w^2/2+w^3/18 has M3=1/3 and gives exactly

    joint error=11/128 < model margin=12/128 < old error=15/128.

Its allowable M3 thresholds4/15 and4/11 are correct. This example is
not an actual-Xi success, and the manuscript does not represent it as one.

## 2. Domain-preserving inheritance and complete comparisons

All native data come from frozen QT530732c5, whose independent review
is `a99a357b96abf535af79a20d5e1948aed6bd3da7`. Current JR imports neither
QT nor FLINT and does not freshly evaluate Xi, rerun Newton, reproduce
the outer-cover census, or reexecute the historical worker attempts.
The fixed calibration remains lambda_(64), not the scalar64.

The geometry reconstruction at producer lines376-396 is conservative.
Both discriminant formulas enclose the same exact value, so their
intersection is valid. The512-bit integer-square-root bounds are outward;
intersecting with the authenticated original d interval is valid. The
retained y interval intersects lambda-d and the original y interval.
The stable quotient identity is checked for a nonempty consistency
intersection, but its narrower interval is deliberately NOT retained.
Discarding that extra narrowing loses precision, not validity.

Intersecting r with its original enclosure and ratio*y retains the exact
source radius. Crucially, line477 requires upper(y+r) no larger than the
ORIGINAL inherited M3 radius. The full critical interval is retained,
and all390 such domain checks pass. Thus there is no illicit application
of a derivative supremum on an expanded domain.

The exact model bounds at lines399-410 have correct signs and endpoint
directions. M3 is nonnegative; all h, factor and margin components are
positive. The comparison uses upper(error)<lower(margin), not midpoints.
The entire parent rectangle calculation at lines413-420 bounds every
rectangle point against every admissible critical t, y and radius.
Its strict squared comparison is stronger than overlap.

The independent standard-library-only review script imports no author
producer and reconstructs every one of the390 cells from the frozen
parent: all geometry endpoints, joint/old errors, model margins, source
attempt/tier hashes, unchanged old status, M3 domain and whole-rectangle
comparison. It also checks all26 inherited critical-point inequalities.
There are210 true rectangle-containment flags, but ZERO transport passes;
therefore there are ZERO matched-root conclusions. This independently
confirms the implementation does not promote containment to transport.

All390 new outcomes are noncertifications with inherited bounds. The
least sufficient-check ratio is exactly at node19, ratio1/2, tier256:

    1637350 <= 1000000*error_upper/margin_lower < 1637351.

This is an exact integer bracket for a quotient of two chosen bounds.
It is neither an actual remainder measurement nor a necessary lower
bound on every admissible error estimate. JR proves no impossibility
for all M3, all radii or higher signed Taylor models. The separate
old-criterion QT/QR obstructions remain valid but do not apply to JR1.

The independent script additionally verifies30 monomial coefficient
identities via exact beta integrals,300 rational disc-factor controls,
and the strict cubic example. The analytic proof above, not these
finite cases, establishes the joint-remainder theorem.

## 3. Source and release audit

The entire proof,658-line producer,354-line tests and manifest were read.
The7502832-byte fixture was parsed, its semantics independently rebuilt,
and its canonical payload and four artifacts authenticated. All38
recursive Git-blob/LF source records were independently acquired.
The producer separately pins the original QT payload, source list,
contract, runtime provenance and historical ledger. This is source
authentication, not fresh execution of that historic runtime.

Commit-object and canonical relative-path guards are present. Strict
integers, booleans in numeric fields, reduced rational pairs, interval
domains, duplicate JSON keys, nonfinite/float tokens, source hashes,
payload hashes and bounded tree/bit/byte coverage are enforced with
exceptions, not assertions. The declared MIXED arithmetic correctly
describes exact rationals and finite coverage; the512-bit outward
square-root rounding is explicitly retained. There is no claim of
new directed-ball or primitive special-function computation.

The28 source tests pass in57.973s normally and57.732s optimized. Both
producer checks and all four fixture/source emits pass, with exact
LF-normalized output equality. Source and review Ruff/format checks,
the full base-to-science whitespace check, and source immutability
checks pass.

The author's twelve resealed cases compare against a previously fresh
setUpClass reconstruction via an explicit build_report patch; this
review does NOT call those twelve separate fresh reconstructions.
The additional reviewer hostile harness instead invokes the unpatched
checker for two fully resealed attacks in EACH mode: a forged transport
pass at an already-contained rectangle, and changed M3/domain data.
It also checks thirteen additional strict invalid inputs. Both fully
resealed attacks are rejected normally in14.875s/13.922s and optimized
in14.593s/13.953s. The thirteen strict guards reject in each mode, and
both independent report checks pass. No source, result or build function
was mocked by this additional harness.

The design's106-line source is authenticated at the immediate parent
commit. No numerical outcome was written into that design. This checks
the frozen provenance record, not an unobserved wall-clock history.
All four review files are staged before the full science-to-review
whitespace check. No scientific file or historic identity is amended.

## 4. Exact hashes and remaining scope

Scientific fixture LF SHA256:

    b94616081a5f3ed187cd5aeb17fe36e03c09e97b6f1460c798531035678e8c3a

Scientific payload SHA256:

    4d9c3f411619c4e024a7bf3763c2e053a051c3231a37de10f3dad291b87678b7

Independent report payload SHA256:

    339f869db57b14d8b51576f08277f27b257ccd8a641cf251f57c0ab9ef94cd20

Independent38-source closure SHA256:

    5deb4c4d04f097c4d6aa69ef2d8db159fdc95291b13c6c8fe80647e2fb6e6f02

No actionable mathematical or release-contract repair was found.
The theorem improvement is real; this fixed inherited-data panel still
certifies no transport. There is no new companion zero, quotient pole,
innerness, RH, physical-band or cofinal result. A genuinely sharper
primitive bound or a different signed-remainder method remains outside
this packet, not refuted by its390 nonpasses.
