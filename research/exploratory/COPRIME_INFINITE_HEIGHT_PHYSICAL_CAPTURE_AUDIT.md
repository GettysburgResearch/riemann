# Independent audit: coprime infinite-height physical capture

Accepted: 2026-08-31, at the exact scientific source below.
This is a nonnative analytic countercontrol, not an actual-Xi theorem.

## Frozen identity and decision

Scientific source: 7aed2ec0b99b9d7f2fb94a774922a83d5b84a870.
Authoring parent: 36eddbbf065959f535ca4a7b08455d489ed4bd18.
Programme import: fbf5c0c1d7a6eb77b8532caf0fe9fd174cbe92a5.

Exactly five source additions were reviewed. Their scientific bytes were
not edited for acceptance. The source's PROPOSED status is historical;
this separate audit records the acceptance and its scope.

Root read the complete proof, producer, manifest and tests, parsed the
entire fixture, and independently reconstructed its finite mathematics.
A separate non-author reviewer read all five files and both complete
frozen HC/LP parent notes. The root had already read and reviewed these
same parent notes in this continuing pass. Neither reviewer inferred an
infinite-dimensional theorem from bounded fixtures.

The [proof](COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md) establishes:

    b_n=16*2^n+i, u_n=16*2^n+i*(1+2^-n), n>=1.
    B,U are pure meromorphic Blaschke products, with no common inner divisor.
    Both sum Im(b_n) and sum Im(u_n) are infinite.
    ||P_(U H2) P_(K_B)||_HS^2 < 1/9.

Every measurable output projection is a contraction, so the corrected
physical trace is finite on every output set, including the whole
positive Fourier half-line. In contrast the bare trace is infinite on
every positive-measure subset of that half-line.

## Analytic chain reviewed independently

1. The geometric real parts make the reciprocal-modulus sums finite.
   The specified factors equal one at zero and are unimodularly normalized
   Blaschke factors. Their genus-zero numerator/denominator products
   converge locally normally. This gives pure products, meromorphic
   across every finite real point, without a hidden exponential factor.
   Their zero divisors are disjoint, so common-inner reduction changes
   neither zero set. Origin-centered disks retain initial prefixes.

2. In the unitary boundary-dx Fourier convention, normalized kernel
   inverse transforms are e_n(t)=sqrt(2) exp(-(1+i a_n)t). Their Gram is
   G_mn=2/(2+i(a_n-a_m)), conjugate-linear in the first argument.
   The absolute off-diagonal row sums are at most 1/4. Hence

       (3/4) Id <= G <= (5/4) Id.

   These bounds first hold for finite vectors and extend by density.
   Synthesis has closed range. A vector in K_B orthogonal to every
   kernel vanishes at every b_n and is divisible by the pure factor B;
   it must be zero. Thus the family is a complete Riesz basis, not
   merely a finite Gram family or an upper frame.

3. Writing synthesis as T, the actual projection is T G^-1 T*.
   The bounded inverse has norm at most 4/3. The relevant numerator
   operator is P_U=M_U M_U*, projecting onto U H2. Its kernel action is

       P_U e_b = conjugate(U(b)) U e_b,
       ||P_U e_b||^2 = |U(b)|^2.

   This is neither the complementary K_U projection nor multiplication
   M_U alone. Its finite physical Gram has the orientation
   U(b_m) conjugate(U(b_n)) G_mn.

4. The matching numerator factor bounds

       |U(b_n)|^2 <= (2^-n/(2+2^-n))^2 < 4^-n/4,
       sum |U(b_n)|^2 < 1/12.

   Therefore P_U T is Hilbert--Schmidt. Multiplying by the bounded
   inverse square root, or legitimate trace-class cyclicity, gives the
   strict 1/9 bound. No formal trace of an unbounded inverse is used.

5. Conversely P_(K_B)>=(4/5) T T*. Every e_n has the same positive mass
   integral_I 2 exp(-2t)dt on any positive-measure output set I.
   Positive finite-prefix trace lower bounds tend to infinity.
   No subtraction of two infinite traces occurs.

6. For P_N=P_(K_(B_N)), the residual synthesis
   S_N=(1-P_N)T_+ has lower Riesz bound 3/4 and range
   K_B orthogonal-minus K_(B_N). This follows by minimizing over the
   finite prefix coordinates, then using density and closed range.
   It is the actual orthogonal complement, not the raw tail kernels.

7. The cross Gram obeys

       ||T_N* T_+||_HS^2 <= N 4^-N/48,
       ||P_N T_+||^2 <= N 4^-N/36.

   The second norm can be the operator norm. The Hilbert--Schmidt ideal
   inequality and squared triangle inequality retain the overlap term,
   and yield

       ||P_U(P-P_N)||_HS^2 <= 4^-N(2/9+2N/243).

   Orthogonal INPUT splitting gives the exact capture difference.
   The infinite U remains fixed, and the error bound is uniform over
   output sets only. The omitted height remains infinite for every N.

8. Multiplication M_U is an isometry, so its transmitted GLOBAL trace
   is infinite. Bounded-band transmitted traces are not decided by this
   packet. The corrected and transmitted quantities cannot be exchanged.

## Exact replay and genuinely independent finite checks

Root named-suite replay passed all 32 tests normally (1.404 seconds)
and under -O (1.399 seconds). Both producer checks, Ruff check and format,
and the complete authoring-base-to-source whitespace check passed.

The non-author reviewer separately passed all 32 tests in both modes,
all four LF-normalized report/manifest emissions, and the same release
checks. Its independent residue/integral calculation reconstructed all
sixteen finite prefix pairs, all seven recorded models and 47 physical
Gram entries, and all five orthogonal-prefix tails. It also rejected
125 additional hostile checks per mode, including 73 independently
resealed full-validator changes.

Root used a different finite construction: explicit Takenaka--Malmquist
rational functions, with their pole coefficients computed directly.
Their exact Gram orthogonality reconstructs the projection onto the
finite U complement without the producer's elimination/inverse.
The B basis then computes capture and omitted-source tails by sums over
orthogonal coordinates, not by assuming a raw kernel-tail identity.

This independently checked, normally and under -O:

- all 16 pairs of finite B/U prefix lengths 1,...,4;
- all seven fixture models and their 47 physical Gram entries;
- every recorded Gram, inverse, product value and determinant;
- all five orthogonal-input tail sums;
- eleven geometric controls, including held-out indices 17, 64 and 257;
- 29 independently resealed attacks against actual full reconstruction;
- two literal source bindings, four artifact seals and all five frozen blobs;
- all four LF-byte report/manifest emissions.

The independent scaffold initially converted an empty-product identity
to a floating value. That scaffold error was corrected to an explicit
exact integer before either accepted full replay. No source packet
change was needed; all accepted algebra is rational.

Unmatched finite U prefixes are deliberately not covered by the small
capture bound. The controls include capture 1/25 for lengths (1,1), but
107122/103025>1 for (2,1). Finite U controls do not evaluate the infinite U.

## Byte identities and source context

Fixture LF SHA-256:

    77c74e194ea75685ae6cf7b1e37f8d0ac82c748f28ded552e5fdc1fa4d7a506c

Payload SHA-256:

    d3a95aaa21c9448394c3276ec8ffd8a6c00a334c401594c020b1ed8fecc933a3

Frozen Git blobs:

    proof     cd74bd06267eb4d60bc977353d11f6a0fb72ba6a
    producer  6385af02839d9b2f8cdd93717fd322bf0667ef92
    fixture   4c093355877c4e69a05e6d417e414c406f8bc9da
    manifest  134669bea673b36d367c2d4c4f6eb42b6347fc11
    tests     c96c11f9d6a6fe3974371dc17a1821a113c5c5d2

The source manifests authenticate the complete frozen HC and LP notes
by commit, Git blob and LF digest. Root also directly read the relevant
introduction, Section 2.2/Theorem A and Section 2.4 of
[Boricheva's primary paper](https://arxiv.org/html/2203.15372v1).
Its model-space projection is the complement of the packet's P_U.
Classical Riesz/kernel context is credited; its compactness statement
is not imported as a Hilbert--Schmidt theorem. Remote bytes are not
part of the offline hash contract.

## Exact boundary of acceptance

This refutes a generic claim that coprimeness plus infinite reduced
denominator height forces divergent corrected physical capture.
Both products are pure and infinite-height, and the denominator is
already reduced. The literal compatible synthetic data are O=1,
N_src=U, D_src=B, R_src=U-B.

This is not the actual Xi source. It establishes no native Riesz property,
numerator sampling estimate, reduced-divisor identification, physical-T
uniformity, cofinal failure, total Pick charge, descent estimate, RH or GRH.
It is not a new abstract Hardy theory or an exhaustive novelty claim.
