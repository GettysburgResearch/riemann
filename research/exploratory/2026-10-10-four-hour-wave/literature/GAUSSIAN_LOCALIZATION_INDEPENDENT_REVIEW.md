# Independent adaptive Gaussian and census-localization audit

Read-only hostile review by `kappa_proof_audit`, 2026-10-10, completed about
13:43 UTC. Base: `/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave`.
No Git or checkout mutation. The full native runtime was not duplicated;
all audit scripts and outputs are in `/tmp`.

## Conclusion and scope

Scoped PASS for the adaptive coverage/parameter aggregation, the retained
Gaussian receipt's exact tree and rational acceptance guards, and
CENSUS_LOCALIZATION L1–L13. No mathematical gap found. Small domain,
reflection and direct-source-hash wording points were corrected by the
owner during review; the acceptance checker remained frozen.

The Gaussian certificate is order zero, lambda=10, |T|<=13 and
0<=y<=1/2. Its native primitive replay, complete-count FLINT contract,
classical strip, complete product and coarse count remain the explicitly
named source dependencies. This audit does not replay the historical
Gram/Rosser verification or provide an independent arithmetic backend.

The localization theorem holds for every fixed derivative order with
positive displayed width, and for every lambda>0. It proves wide
derivative/companion nonvanishing and a real-axis sector. It does not
prove the companion sector throughout the corresponding lower strip.
The finite Gaussian result and global outer result have their own
different lambda, order and domain scopes. No cofinal or RH claim follows.

## Adaptive checker and exact family aggregation

`check_gaussian_slab.py` 35–52 freezes the native height, dyadic input
denominator, complete count 8049 and candidate binding. Lines 65–84
require the census endpoint to be nonzero and every primitive bracket to
be exact, strictly disjoint, below R, and a strict native sign crossing.
Together with the named complete multiplicity-count contract these
justify all finite product roots being real and simple; candidates alone
do not provide completeness.

Lines 90–103 protect the entire compact rectangle by B=105/8<R, bound
the complete tail, and enclose all 32 bins of the actual unknown
coefficient a1 in [0,S]. Each bin is a directed product enclosure of an
exact rational interval with the ball enclosing S; their union contains
the entire exact parameter interval. No fitted parameter is substituted.

Lines 113–162 enclose the complete finite sums over all 8049 roots and
every domain/parameter box. An invalid factor, derivative denominator,
nonfinite quotient, unproved sector or failed final guard returns None
for the entire domain box. Each accepted leaf completes the full
32-bin loop before computing min(Re W) and max(|W|). With a being the
family real lower bound and M the family modulus upper bound, a/M is a
valid uniform angular lower bound. Partial work on a failed bin can
increase attempted-work statistics but cannot supply an accepted leaf.

The exact full multiplier identities give alpha=lambda J1 and
beta=M[2J1+lambda(J1^2+J2)]. The order-zero Gaussian base has real roots
and its exact logarithmic derivative gives the disk bound |H/E|<=1 and
|(H-2i lambda H')/E|<=2 throughout the closed lower half-plane. The
residual q is nowhere zero on the protected disk and includes every
permitted tail block. Thus the acceptance guard and GS3 have the correct
source binding and direction, including unknown nonreal tail zeros.

Lines 164–177 replace every unresolved parent by all four exact dyadic
children. The recursive function returns only after every child returns;
depth exhaustion fails the whole checker. By induction each returned
subtree covers its entire parent. The original 104 by 8 grid at 179–189
is exactly [0,13] by [0,1/2]. In a full four-child forest, each split adds
three leaves, giving the guard leaves=832+3*splits at 190–192. This
count is an additional invariant; geometric completeness follows from
the exact child construction, not from the count alone.

The even-real identity E(-conj z)=conj E(z),
E'(-conj z)=-conj E'(z), implies W(-conj z)=conj W(z).
It reflects T while retaining the lower half-plane and the real sector.
Thus the entire negative-T half is covered as well.

## Independent actual-receipt check, without native runtime duplication

`/tmp/review_gaussian_receipt.py` reconstructs every leaf's exact dyadic
quadtree path from its rational endpoints and depth. It verifies that
every one of the 832 coarse roots is present; every internal node has
exactly all four children; no accepted ancestor, duplicate leaf or
missing child exists; every child width and position are exact; and the
reported depths/counts agree. The actual receipt has:

    roots: 832
    internal splits: 551
    accepted leaves: 2485 = 832 + 3*551
    maximum depth: 3
    accepted parameter boxes: 79520 = 2485*32
    attempted parameter boxes: 80115

Every leaf explicitly reports all 32 bins. The audit uses Fraction
arithmetic and the receipt's directed J1,J2 upper endpoints to recompute
beta<1, alpha+(1+tau)beta<tau and the positive actual-sector lower bound
for every leaf. Every guard passes. The exact minimum independent
sector exceeds 1/100000, verifying the updated manuscript's uniform
claim. Approximate displays only: minimum acceptance 7.9951321171e-6,
minimum actual sector 1.14916896419e-5. Acceptance itself is rational.

Output: `/tmp/review-gaussian-receipt.json`. The accepted receipt SHA256
is `2754316ebd9af82490678a22ecb976b8cc90cda4fea0a2503df707e3f7d59719`.

`/tmp/review_gaussian_structure.py` separately executes the actual
cover_box AST using a deterministic enclosure oracle. Its 832 roots
produce 19963 leaves and 6377 splits at maximum depth three. Exact
rational checks prove complete area 13/2, no interior overlap, the
full-tree invariant and failure on exhausted depth. This is a lightweight
control of all branching paths, not a numerical native certificate.
Output: `/tmp/review-gaussian-structure.json`.

## Localization proof, L1–L13

L1/L2: conjugate roots have equal multiplicity and give precisely
2y[(x-gamma)^2+y^2-eta^2] divided by the positive two-factor denominator.
For |x|<C-A, gamma outside [-C,C], and |eta|<=A, the separation is
strictly greater than |eta|. Every real-root and conjugate-pair summand
has strictly positive imaginary part. This proves derivative nonvanishing
in the two open half-regions, while Gauss–Lucas preserves the full strip.
The hypothesis C>A is available at every needed induction step because
C_r=R-rA>0 means C_(r-1)>A. The loss is A per differentiation, not A per
zero or multiplicity.

L4–L6: complete even-real product approximants have all nonreal roots
outside the initial census range. Their degrees tend to infinity by the
positive source's imaginary-axis growth. Fixed derivatives converge
locally uniformly and are nonzero limits by the positive imaginary-axis
moments. Repeated localization and Gauss–Lucas, then Hurwitz on the
connected half-strips, give the stated complete nonreal-zero exclusion
and strip for H_r. No census of derivative roots is assumed.

L7–L10: on |Re z|<C_(r+1), Im z<0, the polynomial logarithmic derivatives
have positive imaginary part. Their limit is holomorphic because H_r
has already been protected on a wider region. The limit is nonnegative,
and its source anchor is i A_(r+1)(y)/A_r(y), strictly positive in
imaginary part. The harmonic minimum principle makes the sign strict.
Hence Re(E_r/H_r)=1+lambda Im(H_(r+1)/H_r)>1 for EVERY lambda>0.
This proves E_r nonzero there; E_r'=E_(r+1) is protected after one
additional width loss. It does not establish Im(E_r'/E_r)>0 there.

L11: fixed derivatives retain order below two and their parity. Passing
to z^2 after dividing odd H_r by its simple zero at zero gives a complete
genus-zero paired product with no extra exponential. Source growth
excludes a constant/monomial or a finite-zero polynomial; thus the
displayed zero sum is nonempty. The differentiated logarithmic product
is locally absolutely convergent because sum |rho|^-2 converges.
The nonreal-pair contributions are strictly positive on
|x|<C_(r+1), by the same strict separation. This proves the strict
Laguerre numerator wherever H_r(x) is nonzero.

L11–L12 simplicity: the simple original census starts induction. At a
central real zero of H_r, H_(r-1) cannot vanish because its zero would be
simple. The strict negative derivative of its logarithmic derivative
there forces H_r' nonzero. Thus every real derivative zero in its
protected interval remains simple. This also protects both real
companions, and the exact real-sector quotient is the stated positive
Laguerre numerator divided by H_r'^2+lambda^2 H_r''^2. Both L2 and L12
identities passed symbolic algebra controls.

L13: inserting R=8192,A=1/2 gives exactly the four displayed widths.
On-axis nonvanishing extends the pair of companions to y>=0 on the
narrower C_(r+2) region. Only the real derivative nonvanishing assertion
reflects to the upper half-plane. Companion nonvanishing and its
real-boundary sector supply no interior sector automatically; side
boundary information for a further harmonic argument is still missing.

## Reviewed hashes

    check_gaussian_slab.py 04ee33a3de71c6cc63d79abc904b3a2c6a6f23ecfb7e0d8539b4f82790c6804e
    GAUSSIAN_SLAB_CERTIFICATE.md 456299ba19252ceb777547b43b9d23222c3d527958118d2b869a784549072c5d
    CENSUS_LOCALIZATION.md 39cf1735058b98ef0821600f545455bec3a4767267751e5d9aa0621630e7b9e1
    GAUSSIAN_TAIL_TRANSPORT.md 05324d8d073259a77e1a7cae2e98ede22ef16830a592cec6fd52137bb1a32772
    THEOREM.md 2b35a58b119a6f924658a702769c401126e708e592738551e992403004cdfe6d
    SOURCE_TRANSPORT.md 43f3df148708c60692b7d01494ffa367704b0103988fd90717c4929f8e58fd85

The runtime receipt binds the pre-execution-status Gaussian manuscript
hash `2a502ed10b05ce6be870a5c138bb1da00d29e8aae17d7ac0ed1b12df00264481`;
the updated reviewed manuscript records the accepted runtime and wording
clarifications. The checker remains identical. Its direct listed source
hashes do not claim to authenticate every transitive analytic theorem.

## Independent full directed replay completed

The reviewer independently ran the frozen adaptive checker with Python optimization enabled, replaying all 8,049 native sign-crossing brackets, every accepted complex leaf and every parameter bin. The run passed all 2,485 leaves, 551 complete four-child splits and 80,115 attempted parameter boxes. The entire redirected receipt is byte-identical to the final canonical owner receipt: SHA256 `95d23c2bfe5738230c7d546fb82b6c8a5e67145cb2b449984ed1607e60847fba`. All 79,520 accepted parameter boxes are retained. This is an independent runtime execution of the same arithmetic implementation; it does not reprove the imported historical complete count or provide a different backend.
