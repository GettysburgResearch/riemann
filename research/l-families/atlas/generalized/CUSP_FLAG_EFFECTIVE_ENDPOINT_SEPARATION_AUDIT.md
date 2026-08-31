# Independent audit: effective cusp-quotient endpoint separation

Accepted: 2026-08-31 at the exact scientific identity below.
The effective existence theorem and the non-effective fine asymptotic
are separate conclusions.

## Identity and decision

Scientific source: 27496745df9dd49fcde17699d333a54cf8620772.
Authoring parent: bcd3ad5ff0c42e7b205663b68a010e2dbde6d941.
Programme import: bb47d0ea1fef50cb7f80cf535a5918cee8f11b15.

Exactly five additions were reviewed and imported without changing their
scientific bytes. The source's proposed status is historical; this
separate audit records acceptance.

Root read the complete proof, producer, tests and manifest, parsed the
entire fixture, and reconstructed its finite mathematics independently.
The complete UQ and CZ parent proofs had already been read in this
continuing pass. A separate non-author reviewer independently read all
five additions and those parent notes. Neither reviewer inferred an
analytic limit or period sign from a finite numerical panel.

The [proof](CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md) establishes, for
every native weight k=12d>=65536 (first admissible weight 65544), an
uncancelled odd-order real zero of Q in (1-18/k,1), and its reflected
partner in (0,18/k). It also identifies the finer endpoint scale for
zeros whose c=k(1-s) stays in a compact subset of (0,24).

## Analytic chain checked independently

1. Splitting the Euler Gamma integrals at one gives
   Gamma(x)<=1/x+1/e and |Gamma'(x)|<=1/x^2+2/e for 0<x<=1.
   These imply the displayed envelopes for
   F(u)=pi^(-u/2) Gamma(u/2) on [1/2,1] and [3/2,2].
   Euler summation writes zeta(u)=1/(u-1)+H(u), with 0<=H<=1
   in the required first interval. The resulting constants are

       |Lambda(1-2 epsilon)+1/(2 epsilon)|<=19,
       |Lambda(2-2 epsilon)-pi/6|<=48 epsilon.

   The poles are removed before estimating the first expression.
   No special function is evaluated numerically.

2. The UQ all-W Parseval inequality, the sign of the polar term and
   the bounded nonconstant Eisenstein remainder give, uniformly over
   the entire subspace W and 0<epsilon<=18/k,

       I_s(f,f)/G(f,f) <= -k/144+60 < 0.

   This is an operator coercivity estimate, not a test on basis vectors.
   Its constants remain uniform as epsilon tends to zero from above.

3. For h=Delta E4^(k/4-3), the high-cusp squared product envelope is
   u<=289 k^-5 at y>=log k. On the low region, the ratio to the full
   Gamma moment is at most

       B(k)=3^16 k^2 (96 log(k)/k)^k.

   The proof bounds this for EVERY integer k>=65536:
   log(k)/k decreases, 96*16/65536=3/128<1/32,
   k^2<=2^k follows by induction, and 3^16<2^26.
   Consequently B(k)<2^(26-4k)<1/1000. Checking five fixture
   weights is not the all-integer proof.

4. The mass ratio lies between 998/1000 and 1003/1000, uniformly
   for moment exponent beta in [0,1]. Convexity of Y^(-epsilon)
   for the full Gamma law and concavity of y^epsilon for the actual
   mass give the two required Jensen inequalities. In particular

       M_(1-epsilon)/G_h >= (49/50) k/(4 pi),
       M_epsilon/G_h <=101/100

   at epsilon=18/k. Combining these with the Lambda bounds proves

       I_(1-18/k)(h,h)/G_h >= 773 k/72000-2019/100 >0.

   The denominator is negative definite at this same point.
   At k=65544 the respective proved bounds are -2371/6 and
   2050493/3000. These are analytic inequalities, not sampled periods.

5. Since the W block is invertible throughout the interval,
   Q=I(h,h)-b^t D^-1 b is real analytic there and at the left endpoint
   is at least I(h,h)>0. Its positive residue at s=1 makes Q negative
   just to the left of one. The intermediate value theorem therefore
   supplies a sign-changing odd-order zero with nonzero denominator.
   The previously proved functional equation supplies the reflected
   zero of the same order. The original Miller inverse entry 1/Q
   has a genuine pole there.

6. For compact J inside (0,24), all-W coercivity extends uniformly
   to c=k epsilon in J. Choose a fixed cutoff A log(k), with A
   depending on the requested algebraic order but not on k.
   The proof estimates the COMPLEX ratio h/q-1 by telescoping the
   actual modular products. A bound on its modulus alone would not
   give the necessary cancellation.

7. Exact Fourier orthogonality makes q orthogonal to every f in W
   on the high cusp against the constant Eisenstein terms.
   Weighted Cauchy--Schwarz applied to h-q, the high nonconstant
   remainder and the superpolynomially small low mass then gives

       |I_s(h,f)| <= C_(J,M) k^-M sqrt(G_h G_f)

   for every fixed M and all f in W. The estimate is uniform over
   the subspace, with no dimension factor. Combining its dual norm
   with the coercive inverse of -D shows that the Schur correction
   is O_(J,M)(k^(-2M-1) G_h), rather than merely small entrywise.

8. Integrating the digamma expansion over intervals of length c/k
   yields the necessary O(k^-2) exponent error. The proof does not
   multiply a coarse O(k^-1) Gamma-ratio error by a factor of order k.
   With L=log(k/(4 pi)), B0=(gamma-log(4 pi))/2,

       Q_(1-c/k)/G_h
       = k(1/24-1/(2c)) -(c/24+1/2)L
         +B0-1/24-c Lambda'(2)/(2 pi)
         +O_J(log^2(k)/k).

   The rational constant -1/24 and Lambda derivative term are both
   retained. All six finite scale ledgers agree with independent
   formal multiplication of the moment and Laurent expansions.

9. Put C12=B0-1/24-6 Lambda'(2)/pi. Every zero sequence with c in
   a fixed compact subset of (0,24) satisfies

       epsilon =12/k+
         [288 log(k/(4 pi))-288 C12]/k^2
         +O_J(log^2(k)/k^3).

   Fixed signs on either side of c=12 supply such zeros.
   Compactness and the nonzero leading slope 1/288 justify inversion
   without differentiating the asymptotic error or asserting uniqueness.

## Exact replay and independent finite reconstruction

Root named replay passed 32 tests normally (4.143 seconds) and under
optimized Python (4.211 seconds). Both producer checks, Ruff check and
format, complete base-to-source whitespace checks and Unicode C0/C1
checks passed. All four report/manifest emissions match the frozen
fixtures byte-for-byte after LF normalization.

Root independently used formal logarithmic derivatives of the actual
Delta and E4 products followed by a coefficient exponential, rather than
the producer's finite binomial powers. In both normal and optimized modes
this reconstructed all 16 native prefixes, their 144 coefficients, and
24 held-out native prefixes.

Independent symbolic multiplication and inversion checked all six scale
ledgers and the full second-term expression

    288 L -288 B0 +12 +1728 Lambda'(2)/pi.

The five onset controls, integer induction polynomials, elementary Lambda
envelopes and all 33 fixed-order budgets also passed independent algebra.
Root rejected 28 independently resealed changes using the actual full
validator in each mode, including scope, scale, location and prefix attacks.
No patched reconstruction oracle was used for these root attacks.

The non-author reviewer separately passed all 32 EP and 32 UQ tests in
both modes, both producer checks and eight byte-exact emissions.
It reconstructed all 16 prefixes by the E4^3-E6^2 discriminant identity
and binary powers, plus 24 held-outs. It also rejected 41 resealed report
attacks (four with full reconstruction), nine manifest attacks, three
raw-source/size attacks and 39 type/domain/cap/parser checks in both modes.

## Authentication and scope

Root independently authenticated ten literal source bindings, four
artifact seals, all five frozen Git blobs and the payload seal.
The non-author review also checked all twenty EP/UQ source-binding uses,
covering fifteen distinct frozen files, and eight artifact seals.

Fixture LF SHA-256:

    45bff65cecca10a128efa142e29b6281ce81d3490e9ebceec3bcf961ecbc8b2b

Payload SHA-256:

    bc21f815e10b017ab2677a4ee5dd2ec9a76f97246d0fb9ffc5055c1dea3aa41f

Frozen Git blobs:

    proof     c95b70b98052c9b608ab15cd7adae39edab55363
    producer  7e7bed2c227e58a7c27e69a8ae3bf70e9805393d
    fixture   fd2ec70a97d1aff5b2a878dae30ef02cb4982e94
    manifest  0e6a9c3aabb80def9638192f6af7a40b39f027ff
    tests     5b411d018ad3b6f88757a01e1b7e12e5f7a1d173

The additional primary contracts were checked directly:
[Euler summation](https://dlmf.nist.gov/25.11.E5),
[Gamma derivative integral](https://dlmf.nist.gov/5.9.E19), and
[digamma expansion](https://dlmf.nist.gov/5.11.E2).
Remote bytes are contextual sources, not part of the offline hash seal.

Acceptance does not assert an optimal threshold, inheritance of the
earlier 6144 determinant-only onset, an effective constant or onset for
the fine asymptotic, uniqueness, simplicity, a global zero census,
exclusion of endpoint-escaping c sequences, a new automorphic family,
exhaustive novelty, RH or GRH. This packet itself concerns k=12d only.
