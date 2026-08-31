# Independent audit: actual Xi off-axis ball certificates

Verdict: PASS at the exact scientific source
134a55016b4f3ea970dc8e5f03505d4e97afff07,
parent ac7fa9af27c3fbcb3314f3ed58c8eed35b318052.
Review date: 2026-08-31.
The reviewer is not the packet author. There was no author coordination.
This audit adds only this document on a separate exact-source branch.
No scientific source, fixture, manifest, test, programme front or PR was edited.

PASS has the source's explicit implementation qualification: the finite
certificates rely on the pinned FLINT rigorous-enclosure contract. The
local zero and meromorphic-pole conclusions do not assume RH. Only the
reduced-inner and global projection interpretation assumes both companions
are inner. No band capture, trace divergence, global coprimality or RH
conclusion is accepted.

## 1. Frozen coverage and identities

All five scientific files were read. The entire fixture was parsed and
freshly reconstructed, including all nine rows, every derivative/enclosure
field and all1944 canonical rational endpoint/input pairs. This was not a
comparison of summary hashes alone.

The five frozen identities are:

| Path | Git blob | SHA256 after CRLF-to-LF normalization |
|---|---|---|
| research/exploratory/XI_COMPANION_OFF_AXIS_BALL_CERTIFICATES.md | 625cc29f67510bd58ed667f6f5fec242b84e4a11 | 020597b67044d996e12e2f76655550557cc33cd52cf717553e2fc6be9d48e396 |
| research/exploratory/xi_companion_off_axis_ball_certificates.json | e7cdd61fcc046d142ccc95b5796d3106a79139c4 | 268e67f84bdae5d41a4acb95df96fff18e00c3d0ae3430a9be8c89f633ff7c5b |
| research/exploratory/xi_companion_off_axis_ball_certificates.py | b0cecac35dcdb3a583ae891609d7d89b378b537b | 319e9abf775199e1747b0642dd99f24e52d9700bf71c04385d02cf5be9aac15f |
| research/exploratory/xi_companion_off_axis_ball_certificates.sources.json | 06434dc776028d155b8107f8cb5ea8687a3ce9dc | eec3231292d8d5b030c68ffaed9520dd5697657dcd17f15c91e4f34ee8f9be4c |
| tests/test_xi_companion_off_axis_ball_certificates.py | f1f323d579968949cf07c662dd245172380759ba | 3cfd3a3c2177ccbb242aeb5a9fa7e83b27859f9485a532489304019499b8dcd7 |

The fixture's canonical unsigned-payload SHA256 is
44af17faa1f8c3269b6e241bcf8e2dbf99a9169d7bcff706bace39cd5ab91dc7.
Its LF file SHA256 is
268e67f84bdae5d41a4acb95df96fff18e00c3d0ae3430a9be8c89f633ff7c5b.
The four artifact seals were independently checked against the actual files.

All six complete frozen source notes were personally read and independently
authenticated by Git blob and LF SHA256, not by execution of ancestor code:

| Source | Exact commit | Load-bearing import |
|---|---|---|
| NA | d38961c15fc76d671cef4fddfc92d3c866af4fd5 | Actual unrescaled Xi, fixed companions, W identity, corrected projection |
| GH | 9da33e7ea2b15a4badb3cb436e38e54762ad5e1d | Native Theta0/Theta5 allocation and the separate inner premise |
| CP | 7aed2ec0b99b9d7f2fb94a774922a83d5b84a870 | Correct projection versus multiplication; no height-to-capture shortcut |
| GC | d76a1a8eb8ec40b19a351af95439b9a6514bee87 | Genuine versus canceled companion zeros; local versus global common divisor |
| L-106610 | 81d52e569cc8bb566e54043fd692fd6157406aab | Exact Riemann--Siegel phase, not its leading asymptotic |
| L-106620 | 81d52e569cc8bb566e54043fd692fd6157406aab | Frozen positive constant scale and literal native quotient |

Their exact paths, Git blobs and LF hashes are the six literal entries in
the reviewed source manifest. The audit confirmed each entry against Git.
The authoring delta has exactly the declared five files. The worktree was
clean at the source SHA, and the complete base-to-source whitespace check passed.

The runtime was also reconstructed independently using installed package
metadata and hashing every native file, not by accepting the producer's
runtime dictionary. It matched CPython3.12.10, python-flint0.9.0,
FLINT3.6.0, Windows AMD64, all44 native .pyd/.dll files, and the aggregate
36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc.
This is not a security attestation or a hash of the interpreter and OS.

## 2. Exact gauge, source allocation and half-plane orientation

Differentiating the literal phase in L-106610 gives

    theta'(a)
      = [psi(1/4+ia/2)+psi(1/4-ia/2)]/4 - log(pi)/2
      = Re psi(1/4+ia/2)/2 - log(pi)/2.

Thus OA2 and producer frozen_lambda use exactly the same constant
lambda_a=1/theta'(a). The three positive values were independently
enclosed using a SERIES derivative of the two log-Gamma terms, not the
producer's digamma expression. Positivity and agreement pass at32,64,128.
The asymptotic2/log(a/(2pi)) is not substituted.

The selected anchors are not proved to be prescribed physical partition
anchors. Nor is the historical sufficiently-high threshold identified
with32. The packet explicitly states both limitations. Its local
constant-scale companion algebra remains meaningful and exact.

With f=Xi and constant lambda,

    R5=f5-i lambda f6,   C5=f5+i lambda f6,
    R5'=f6-i lambda f7,  R5''=f7-i lambda f8.

The derivative is with respect to z and does not differentiate lambda.
The native quotient is R0*C5/(C0*R5), not its reciprocal. Cancellation of
the nonzero local Riemann--Siegel carrier in L-106620 preserves this ratio.

For real lambda and even real entire f,

    C5(bar z)=overline(R5(z)),
    R5(-bar z)=-overline(R5(z)).

Hence the declared upper-half-plane disks concern R5 zeros. Their
conjugates contain C5 zeros in the lower half-plane; the negative-real
upper reflected disks contain R5 zeros. No upper C5 zero is inferred.
The declared disks have strictly positive imaginary parts and exact
real coordinates within(a-6,a+6). Disjointness was checked using rational
coordinates, separately at each frozen parameter.

## 3. Taylor coefficients and the uniform Rouché proof

The source constructor, producer lines369--385, evaluates

    xi_R(1/2+i(z+X))
      = (s(s-1)/2) exp(-(s/2)log(pi)) Gamma(s/2) zeta(s).

Its coefficient of X^j is f^(j)(z)/j!, and multiplication by j! is correct.
The reflected route uses1-s, including the negative linear coefficient,
so it still produces z derivatives with the correct phases.
The standard completion and reflection agree with
[DLMF25.4.3--4](https://dlmf.nist.gov/25.4).
There is no frequency rescaling or missing scalar factor.

Series cap9 supplies precisely the derivatives0 through8. It is not used
as a guessed tail estimate for f(z+X). Instead the constant coefficient
is the entire rectangle and the same interval-series operations enclose
the eighth derivative uniformly at every point of that rectangle.
For all declared boxes, abs(Im s)>20; s=0,1 and Gamma poles are absent.
The product is analytic on a neighborhood without depending on cancellation
of a singular factor in a ball computation.

For F=R5, the complex line-segment integral remainder is

    F(c+zeta)-F(c)-F'(c)zeta
       = zeta^2 integral_0^1 (1-t) F''(c+t zeta) dt.

The factor1/2 in OA4--OA5 is therefore correct. The rectangle contains
every segment in the closed disk. Its independently bounded F'' is the
whole remainder input, not finitely sampled derivative data.

The extracted lower/upper endpoints are outward exact dyadics. Using
Fraction arithmetic, the acceptance inequality is

    A + M r^2/2 < D r,   r=2^-120,

with A>=abs F(c), D<=abs F'(c), and M>=sup_disk abs F''.
Comparison with the linear holomorphic function F'(c)(z-c) gives exactly
one zero counted with multiplicity and no boundary zero. Count one
therefore proves simplicity. No Newton convergence or zero list is needed.

The [official general ball contract](https://python-flint.readthedocs.io/en/latest/general.html)
covers rigorous interval outputs and conservative comparisons.
The [acb endpoint contract](https://python-flint.readthedocs.io/en/latest/acb.html)
states the directed modulus endpoints; the
[arb constructor and endpoint contract](https://python-flint.readthedocs.io/en/latest/arb.html)
covers rectangular radii and outward bounds. These were directly inspected.
The finite-series semantics were checked against the
[python-flint series API](https://python-flint.readthedocs.io/en/latest/acb_series.html)
and the Gamma/Zeta sections of the actual
[FLINT3.6.0 acb_poly documentation](https://raw.githubusercontent.com/flintlib/flint/v3.6.0/doc/source/acb_poly.rst).
The latter describes Taylor generation/composition for Gamma and
Euler--Maclaurin bounds for zeta series. No unsupported extrapolation
from ordinary high precision is being accepted.

## 4. Independent primitive reconstruction, not the producer calling itself

The audit implemented a different Xi representation in a transient,
read-only script without importing the scientific producer:

    s0 = 1/2 - i*z
    t = s0 + X
    L = log(t)+log(t-1)-log(2)-(t/2)log(pi)
          + logGamma(t/2)+log(zeta(t))
    q0 = exp(L0)
    qn = (1/n) sum_(j=1)^n j*Lj*q_(n-j)
    f^(n)(z) = (-i)^n*n!*qn.

This uses the reflected completion, a UNIT s-increment and an explicit
differential Bell recurrence. It is distinct from the source's direct
product-series evaluation in the z variable. All computations remained
balls; no decimal derivative or finite difference was used.
The independent zeta constant balls also excluded zero and the negative-real
logarithm cut; reflected Gamma arguments had strictly positive real part.

At BOTH384 and512 bits the independent script rebuilt every center and
rectangle from the exact rational fixture inputs, all nine derivative
orders, the fixed phase scale, companions, direct quotient-rule
Theta0/Theta0'/Theta0'' expressions, and the native residues.

For EACH precision, in EACH normal/-O execution:

| Independent check | Coverage/result |
|---|---|
| Primitive derivative comparisons |324 overlaps against all direct/reflected point/rectangle fields |
| Companion comparisons |72 overlaps |
| Raw Theta0 derivative comparisons |27 overlaps |
| Native residue comparisons |9 overlaps; zero excluded |
| Fresh Rouché proofs |9 pass, conservative binary slack lower bound58 |
| Nonzero guards |C5,R0,C0,f6,W,R5prime on every rectangle |
| Strict raw corridors |All9 pass, each raw modulus>1/4 |
| Frozen phase scales |All3 positive and matching |

In particular the new inequalities satisfy left*2^58<right, stronger
than the source's declared2^50 slack. This is recomputation of the whole
rectangle bound, not merely agreement of root approximations.

Functional-equation overlaps are diagnostics, not a proof of the
functional equation; that identity is independently sourced above.
Similarly an interval expression containing zero does not prove an
identity. OA6 was checked by direct symbolic expansion:

    (f-i lambda f')(f5+i lambda f6)
      -(f+i lambda f')(f5-i lambda f6)
       = 2i lambda (f*f6-f'*f5).

The independent replay still shares FLINT's transcendental implementation.
It is not advertised as a second special-function backend or a formal
verification of FLINT. That remaining implementation trust is explicit.

## 5. Genuine poles and the exact conditional operator consequence

On each full rectangle, C5,R0,C0 and R5prime exclude zero. Consequently
the unique simple R5 zero b is a genuine Theta5 zero and a genuine simple
pole of the literal native quotient. There is no hidden raw cancellation.

The nonzero residue is exactly

    R0(b)*C5(b)/(C0(b)*R5'(b)).

The interval evaluation on the whole rectangle encloses its value at the
unknown zero. The independent quotient computation verifies all nine
nonzero residue enclosures. The guard f6 supplies the redundant check
C5(b)=2i lambda f6(b). The W guard is consistent with, but does not
classify, GC's global exceptional set.

Under the separately stated two-component inner premise, write
Theta0=G U and Theta5=G B. Since Theta0(b) is nonzero, G(b) is nonzero;
the simple denominator zero survives in B. The valid modulus direction is

    abs U(b)=abs Theta0(b)/abs G(b) >= abs Theta0(b).

For e_b(z)=sqrt(Im b/pi)/(z-bar b), the boundary-dx norm is one,
e_b lies in K_B, and M_U^*e_b=bar U(b)e_b. Hence

    ||P_(UH2) P_(KB)||op >= ||P_(UH2)e_b|| = abs U(b).

The strict global lower bounds722/1000,692/1000,493/1000 are therefore
correct, respectively at the three DIFFERENT frozen parameters.
They do not combine the nine disks into a single-parameter census.

The raw upper corridors do not upper-bound the reduced U. The raw
derivative boxes are not reduced numerator/adjoint physical jets without
additional control of G. No native Riesz family or finite-band bound is
paid by one normalized kernel. CP's obstruction is respected.
This audit accepts no global exception decision, complete off-axis
census, band capture, high-T uniformity, cofinal trace statement, or RH claim.

## 6. Replay, hostile controls and fail-closed scope

At the exact source checkout:

- 36 tests passed normally in9.176s and under-O in8.539s.
- Both producer checks passed.
- All four report/source emissions matched the frozen files after LF
 normalization, including optimized execution.
- Ruff check and format check passed.
- The full parent-to-source diff passed whitespace checks.
- All five files passed the C0 scan; the producer has no assert guards
 or float/complex literals in its AST.
- The six source identities, four artifact seals, runtime's44 native hashes,
 fixture LF identity and canonical payload seal passed independently.

Additional tests outside the source suite ran in BOTH normal and-O modes:

- 18 fresh, UNMOCKED resealed-report attacks were rejected. These changed
 orientation, lambda rule, the inner premise, parameter-exception scope,
 physical conclusions, a rectangle, the eighth derivative, Rouché bounds,
 R5prime, Theta0'', a residue, bool-valued fields, runtime identity and a
 frozen primitive identity. Rebuilding primitives was not mocked.
- 28 further domain, cap, strict-type, equality-boundary, malformed-JSON,
 source-manifest and arithmetic-context attacks were rejected.
- The false/equality Rouché predicates were rejected; no non-strict
 comparison or Python assert controls mathematical acceptance.

The caps are bounded acceptance contracts, not a security sandbox.
The source reads fixture/source bytes before some size checks; this audit
does not certify pre-acquisition memory or subprocess-time bounds.
Public acceptance still rejects oversized JSON and out-of-domain
arithmetic rather than accepting a truncated or weakened certificate.
No denial-of-service hardening claim is inherited.

The normal/O proof replays used the prescribed runtime at
isolated/native-xi-pass3-runtime/Scripts/python.exe.
The source suite's runtime self-test anecdote was not used as proof;
this audit relied on the stated enclosure contract and the explicit
independent reconstructions above.

## 7. Final disposition

No result-invalidating gap was found at134a55016b4f3ea970dc8e5f03505d4e97afff07.
Accept the nine finite source-normalized zero/pole certificates under the
pinned rigorous-ball implementation contract, and accept the stated
global one-vector projection bounds only under the existing inner premise.

Do not promote this PASS to another SHA or to the unpaid physical-band,
reduced-jet, census or cofinal gates. RH remains unsolved.
