# T-105114 - Simultaneous anchored collar transfer frontier

Claim ID: T-105114

Status: **PROPOSED EXACT FINITE TRANSFER; XI ABSORPTION OPEN**

Created: 2026-08-23

Depends on: L-105114; L-105112; L-105113

RH status: **unproved**

## Result

For a holomorphic function normalized at a nonzero anchor, L-105114 gives
an explicit lower modulus outside one radius-\(\varepsilon r_2\) disk per
zero. Jensen controls the nominal total radius. For finitely many
functions, the radius loads add, and the sharp projection criterion

\[
2S<\min(\Delta_T,\Delta_\eta)
\tag{T-105114.1}
\]

selects one common symmetric rectangle avoiding the entire union, provided
the candidate boundary family is contained in the disk on which the
minimum-modulus conclusion holds.

For the residue carriers \(F/F'\) and \(F^2/(F'F'')\), the raw route needs
zero disks only for \(F'\) and \(F''\). It permits zeros of \(F\) on the
selected boundary and gives the explicit quotient bounds

\[
\left|\frac F{F'}\right|
\le\frac{|F(a)|}{|F'(a)|}e^{A_0+B_1},
\qquad
\left|\frac{F^2}{F'F''}\right|
\le\frac{|F(a)|^2}{|F'(a)F''(a)|}e^{2A_0+B_1+B_2}.
\tag{T-105114.2}
\]

These feed either the direct edge integrals or the restricted safe-set
Tonelli selection of L-105113. The L-105112 domain firewall remains in
force: an outer selector has only an upper norm bound on an intermediate
edge, not constant-modulus equality there.

## Programme split

    NORM105114
      Normalize by a certified nonzero anchor before applying a
      minimum-modulus theorem. Closed finitely by L-105114.

    RADIUS105114
      Exact Jensen zero count and nominal equal-disk total-radius budget.
      Closed finitely by L-105114.

    COMMON105114
      One common disk-safe symmetric rectangle for a finite family.
      Closed conditionally by L-105114 plus the projection lemma.

    RAW105114
      Direct quotient bounds charge disks only for F' and F''.
      Closed finitely by L-105114.

    PRINTED105114
      Use an unnormalized Cartan display literally.
      Refuted by R-105114.

    XIANCHOR105114
      Authenticate a common off-center anchor for three consecutive
      t-plane Xi derivatives. Open.

    XIGROWTH105114
      Prove cofinal growth loads with all domain constants and fixed-k
      quantifiers tracked. Open.

    XIABSORB105114
      Absorb reciprocal margins, edge length, safe-set loss, and actual
      selector cost at the residue-moment scale. Open.

## Boundary

    normalized finite minimum-modulus transfer       PROPOSED EXACT / REVIEW PENDING
    equal-zero-disk total-radius budget              PROPOSED EXACT / REVIEW PENDING
    finite simultaneous rectangle interface         PROPOSED EXACT / REVIEW PENDING
    raw route excludes F-zero disks                  PROPOSED EXACT / REVIEW PENDING
    unnormalized printed transfer                    REFUTED
    common Xi derivative anchor                      OPEN
    cofinal Xi growth and margin loads               OPEN
    complete Xi actual-pole manifests                OPEN
    selector/margin absorption                       OPEN
    strict Xi jet coherence                          OPEN
    RCMV104530                                       OPEN
    Riemann Hypothesis                               UNPROVED

The finite theorem is analytic, not numerical. No zero scan, Xi
evaluation, cofinal passage, RCMV104530, or RH conclusion follows.
