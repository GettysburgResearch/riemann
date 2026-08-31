# Independent frozen review: QR21936f22

Verdict: PASS, bounded to the literal separate-triangle criterion.

Scientific source: `21936f22246a12ab0b4e8bd706154b861b56b585`.
Immediate preregistration parent: `800b5e212f61a4df9a640788d294b0bbbf37862b`.
Five-file authoring base: `530732c5fd7f50364381f8af50e97ce809b674c5`.
Review worktree: `isolated/qr-audit-pass3`.
All five scientific files remain unchanged. No author coordination was
used to obtain acceptance, and no repair or push was performed.

## 1. Analytic result and independent proof

The source note's Section1 is sound. Set lambda=d+y with d,y>0 and
0<r<min(y,2d). Its literal sufficient-test threshold is

    H(r)=6F(r)/(3lambda+y+r),
    F(r)=r(d-r/2)/(y+r)^2.

The stated derivative is exactly

    F'(r)=(dy-lambda*r)/(y+r)^3.

The maximizer r*=dy/lambda is strictly smaller than both y and d,
hence lies strictly inside the allowed interval. Its value is
d^2/[2y(lambda+d)]. An independent completion of the square gives

    F(r*)-F(r)
      =(lambda*r-d*y)^2/[2y(lambda+d)(y+r)^2].

The second denominator in H(r) is STRICTLY larger than3lambda+y.
Consequently H(r)<B=3d^2/[y(lambda+d)(3lambda+y)] for every admissible
r, including at r*. Thus m=|g'''(t)|/|g''(t)|>=B rules out this strict
sufficient test at ALL admissible radii, even when equality m=B holds.
The necessary premise M3>=|g'''(t)| is legitimate because QT requires
the complete Taylor disc centered at t, not merely the final Rouche
circle centered at t+iy. See the source note lines24-40 and the frozen
QT parent Section1.

The coarse-improvement identity in the note is also exact:

    d/(2lambda*y)-B
      =d(5d+4y)/[2lambda(lambda+d)(3lambda+y)]>0.

B is NOT asserted to be the exact supremum of H. In particular failure
to exceed B does not prove that any radius succeeds. The eight unresolved
points cannot be promoted to successful transport or to an optimality
claim for this ceiling.

No additional analyticity theorem is needed for this algebraic
obstruction: the source explicitly inherits QT's literal analytic-disc
criterion, whose hypotheses were independently reviewed at
`a99a357b96abf535af79a20d5e1948aed6bd3da7`.

## 2. Actual source and complete finite comparison

The native function is f(z)=xi_R(1/2+iz), g=f5, hence the controlling
derivatives are g''=f7 and g'''=f8. The calibration is the ONE fixed
lambda_(64), not the number64. The26 real f6 critical points and their
whole radius2^-120 intervals are inherited from exact QT530732c5.

At producer lines548-626 each entire real interval, not its center,
is fed to the nine-coefficient1024-bit actual-Xi wrapper. The f6
enclosure contains zero; f5*f7 is strictly negative and the source
discriminant is positive. These checks do NOT independently establish
a critical zero; that existence, uniqueness and reality are explicitly
inherited from QT. The strict source pins and critical-object digests
prevent replacing the inherited interval or choosing a new point.

The directed comparison lower(|f8|/|f7|)>=upper(B) is sound despite
interval dependencies: widening only makes the sufficient obstruction
harder to certify. Producer lines466-498 supply a separately arranged
Fraction/integer-square-root comparison for every accepted row. Its
256-bit square-root brackets and512-bit final outward dyadic rounding
have the stated directions and cannot manufacture an acceptance.

All26 rows have finite jets and pass the domain/sign guards. Results:

| Box center | Nodes | All-radius obstruction | Coarse obstruction | Unresolved |
|---:|---:|---:|---:|---:|
| 256 | 8 | 8 | 8 | 0 |
| 512 | 9 | 9 | 7 | 0 |
| 1024 | 9 | 1 | 0 | 8 |
| Total | 26 | 18 | 15 | 8 |

The exact additional sharper indices are13,14,22. There is no failed
numerical-domain row hidden in the unresolved count.

The independent script accompanying THIS review imports no HA, QT or
QR producer code. It freshly evaluates the reflected formula

    xi_R(1-(1/2+iz))
      =w(w-1)/2 * exp(-w log(pi)/2) * Gamma(w/2) * zeta(w),
      w=1/2-iz,

through degree8 on every full critical interval at1024bits, retaining
the derivative factorials. All four relevant derivative intervals overlap
the published enclosures. Its independently arranged rational comparison
eliminates q and the rationalized y:

    d^2=lambda^2+2f5/f7,
    B=3d^2/[(lambda^2-d^2)(4lambda-d)].

Using384-bit integer-square-root brackets, both the source-jet and
reflected-jet routes reproduce all26 flags and the18/15 outcomes.
Eighty additional exact extreme-geometry/radius cases verify the square
identity, the alternative B formula and strict ceiling inequalities.
They are controls, not the proof of the all-radius quantifier.

The special-function backend is still the SAME pinned FLINT library.
This is independent formula/comparison code, not a second implementation
of zeta/gamma, a formal proof of their bounds or a fresh critical-root
census. Normal and optimized independent reports agree.

## 3. Source, timing-history and strict acceptance

All38 immutable Git-blob/LF source bindings were independently acquired
and checked recursively. Current science matches exact21936f22; all four
artifacts, own payload, inherited QT payload and critical-object hashes
agree. The preregistration commit contains the102-line design and no
outcomes. This authenticates the frozen pre-outcome design text; it does
not independently certify any unrecorded historical computation timing.
The earlier five-ratio results were explicitly already known. No blind
prediction of18/15/8 is claimed.

Authentication at producer line381 locks the actual executed HA/BC/OA
helpers and the runtime44-file aggregate. QT's producer is not imported.
Its Newton searches,373 successful broad-history replays,173 historical
nonbounds and19,968 outer-cover cells are NOT reexecuted by QR and are
not needed for this fresh pointwise obstruction calculation. Their
separate accepted QT review remains an inherited dependency.

The694-line producer and247-line tests were read fully, as were the
whole proof and manifest. The179443-byte fixture was parsed and checked
against fresh complete reconstruction. Strict JSON integer/bool handling,
reduced rational endpoints, positive division/square-root domains,
source text controls, caps, artifact hashes and full canonical equality
were inspected. Acceptance uses explicit exceptions, not assertions.
MIXED arithmetic is correctly declared: directed ball enclosures, exact
rational arithmetic and complete finite coverage, with explicit rounding.

The25 source tests pass normally in160.950s and optimized in161.416s.
Both producer checks and all four fixture/manifest emits pass; the emits
match exactly after LF normalization. Independent normal/optimized
replay also passes. Thirteen extra strict hostile inputs are rejected
in each mode. Two additional fully resealed attacks per mode target a
false impossibility claim at unresolved index19 and an illicit assertion
that the JOINT remainder criterion is excluded. Each is rejected after
complete fresh reconstruction, with no build/source/result mock.

The only review-helper edit during pre-freeze testing binds the immediate
attack lambda's loop argument for Ruff; this does not change acceptance
or mathematical computation. Final helper replay after that edit rejected
both resealed attacks in17.516s/16.781s normally and17.203s/17.219s in
optimized mode. The thirteen strict guards passed again in each mode.
Both independent fixture checks were also repeated successfully.

Source and review Python files pass Ruff and formatting. Full
authoring-base-to-science and science-to-review whitespace checks pass.
The scientific five-file diff remains empty throughout this review;
only the four separately identified review files are committed.

## 4. Exact identities and boundary

Scientific fixture LF SHA256:

    806c4c0554af651c0fdd6a97a92bbb2f4cff5c16b86d8a2eef56c0372bc517d2

Scientific payload SHA256:

    f41dd7dd7c1b9fa1b2bcc931a7b150cda174a22c8019b48197695aad046250bf

Independent report payload SHA256:

    f2f75f657324c93c1cead75bb98a85fb87f44fcc6c0a8439adfd55032ae8abeb

Independent38-source closure SHA256:

    4e372c7231020b2070c77f4370164b74689be5b6780a5e74a9d01071902ba38d

No actionable mathematical or release-contract repair was found. The
result concerns only QT's separate-triangle sufficient criterion at
these18 certified critical points. It neither rules out the joint
Taylor-integral criterion nor higher signed Taylor models, alternate
source-defined centers, existing companion roots, or other transport
arguments. It assumes no raw innerness and makes no RH, cofinal capture,
global density, or physical-band conclusion.
