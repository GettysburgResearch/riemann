# Independent review: weight-36 subspace divisors

Verdict: **PASS for the stated fixed-weight theorem and exact finite
identities.** Prediction/blinding provenance is restricted below.

Exact scientific commit:
`0c07ba0e9c6464d3b623f7d997e471544f4e807e`.
The reviewer is not the author of this packet. No scientific file was
changed. Review was conducted in a separate worktree at the frozen commit.

## Scope and complete reading

The entire theorem note, 5-file packet, producer, 32-test module and source
manifest were inspected. The FI predecessor and its independent audit,
the coefficient-flag period normalization, and the HC source were already
read in the same research pass; their exact SD bindings were authenticated
again. All seven immediate Git source blobs, four current artifacts and
the fixture payload seal agree.

The theorem is about the literal completed period of S_36 and every fixed
proper nonzero complex coefficient subspace. It is not a numerical search
for actual divisor locations. The finite 27-subspace panel is not an
exhaustive Grassmannian enumeration.

## Analytic proof audit

1. The eigenbasis is real and normalized by its first Fourier coefficient.
   Its Euclidean coordinate metric is explicitly distinguished from the
   Petersson metric. For complex s the period matrix is symmetric, not
   Hermitian. Restriction correctly uses V* M V, including conjugation.
   Changing quotient coordinates contributes only a nonzero constant.

2. The prime-two characteristic polynomial has three distinct real,
   nonzero, nonopposite roots. Their squares and their three distinct pair
   products separate the three GL3 and three GL4 inputs, respectively.
   The rank groups are distinct by degree. Trivial central character and
   finite-place unramifiedness exclude every nontrivial quadratic twist
   relating or fixing the GL2 forms; there is no globally nontrivial
   quadratic character unramified at all finite primes over Q.

3. The precise lift hypotheses are paid: no quadratic self-twist gives
   cuspidal adjoint GL3 lifts; non-dihedral, pairwise non-twist-equivalent
   pairs give cuspidal GL4 tensor lifts. Their finite Satake bounds follow
   from the actual holomorphic GL2 parameters, not a general unproved GL4
   Ramanujan hypothesis. The seven-input application is thus unconditional.

4. The symmetric determinant is irreducible. In the proof's expression
   (xy-a^2)z-(xc^2+yb^2-2abc), the leading coefficient is irreducible and
   does not divide the constant coefficient; the explicit specialization
   given in the note proves the latter assertion. Gauss's lemma applies.

5. The diagonal Cauchy--Binet restriction has positive squared Pluecker
   coefficients. A single surviving Pluecker coordinate forces a coordinate
   subspace. A coordinate plane still has its off-diagonal square term.
   Hence only coordinate lines have monomial denominators. Any other
   denominator has a noncoordinate irreducible factor of degree at most
   two, which is coprime to the irreducible cubic determinant. Applying
   the Nullstellensatz to the determinant times all six entry variables
   gives the required torus target with the complementary factor nonzero.
   Reversing the two roles gives a protected zero target for EVERY W.

6. These are actual Euler-input targets, not merely six free matrix
   entries: set the zeta coordinate to 1 and use the six remaining nonzero
   entries as the symmetric-square/tensor coordinates. Booker--Thorne's
   common-prime-phase proposition then applies with cutoff 3/2. Its 2018
   correction replaces a rate inside the proof but preserves this conclusion.

7. The first three q functionals are independent. Cauchy--Binet gives
   nonnegative Dirichlet coefficients and at least one nonzero restricted
   coefficient at index at most six. The full determinant has the positive
   coefficient at six displayed in SD14. Consequently a common completely
   multiplicative prime twist cannot annihilate either series identically.
   This step prevents an invalid inference from a formal target alone.

8. The coefficient majorants 3d4, 6d8 and 6d12 pay COMPLETE tails for lines,
   planes and the full determinant, uniformly in prime phases. They follow
   from entrywise degree-four bounds and squared sums of Pluecker moduli.
   The paired contour argument protects the complementary factor on the
   whole disk, not only its boundary. It therefore produces genuine
   noncancelled zeros and poles. Positive-density positive shifts and the
   2rho overlap bound count distinct points, without assuming simplicity.

9. For an eigenline the denominator Z S_i is an absolutely convergent
   nonzero Euler product on Re s>1; no poles occur there. All planes,
   including Hecke planes, and all mixed lines have protected pole targets.
   Every line and plane has protected zero targets. The classification and
   its fixed-W, near-one strip quantifiers follow.

Primary passages personally checked in this review are
[Gelbart--Jacquet, Theorem 9.3, p534](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf),
[Ramakrishnan, Proposition 2.3.1 and Theorem M, pp53--54](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf),
[Booker--Thorne, Theorem 1.2 and Proposition 3.1](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf),
its [complete two-page correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf),
and [the Nullstellensatz](https://stacks.math.columbia.edu/tag/00FV).
These are credited imported theorems, not new general results of this packet.

## Independent primitive reconstruction

The resident reviewer script executes NO author arithmetic code. It constructs
E4 and E6 from their divisor sums, obtains Delta=(E4^3-E6^2)/1728, and uses
an inverse pivot matrix for the actual Miller basis. SymPy exact polynomial
arithmetic and stdlib rational convolution supply independent routes for:

- all 57 basis entries through q18, both Hecke matrices and all 45 Hecke
  action cells beyond and including the pivots;
- characteristic polynomial, discriminant, opposite-root resultant, three
  real root intervals, commutation, and the q3 polynomial in T2;
- all 36 full determinant Dirichlet coefficients, using signed determinant
  convolution rather than the author's distinct-index minor summation,
  including three complete zeta(2s) square-support convolutions;
- all 27 complex restriction polynomials, Pluecker diagonals and Gram
  normalizations, and all 51 protected zero/pole torus targets;
- 50 additional exact Gaussian-rational line/plane controls, checking
  nonmonomiality, coprimality and positive coefficient rank. These are a
  declared extra algebra panel, not an infinite coverage theorem.

The independent report is byte-identical in normal and optimized Python.
Its scientific fixture LF SHA256 is
`2c388024ebf80c28abb8eeb049601516568c68219c9f738e53a1a2a8d1a02073`.
The 36-coefficient stream digest is
`17c477638c36d07bbcbe2cd468bd789cd58d6e879f94de23415bca3ef25020c4`.

All 32 source tests pass in normal Python (30.041s) and optimized Python
(28.516s). Both producer checks and all four exact LF fixture/manifest
emits pass. The tests include fresh unmocked resealed coverage, coefficient,
scope and protected-target attacks, strict types/caps, and source/artifact
tampering. Ruff and the complete FI-base whitespace check pass. The review
does not claim a second independent analytic-number-theory library.

One reviewer implementation correction was needed before acceptance:
symbolic Gram equality must be expanded before comparison. An initially
unsimplified SymPy equality rejected a correct complex expression; the
scientific fixture and producer required no change.

## Prediction provenance and remaining boundaries

The author confirmed that the SD predictions called "preregistered" in
the frozen note were recorded in the retained task discussion before the
computation, NOT in a separately frozen pre-computation Git artifact. This
review authenticates their exact identities and complete replay, but does
NOT certify independently source-frozen preregistration or blinded held-out
status. Future summaries should call them task-discussion predictions.
This limitation does not alter the all-subspace analytic theorem.

No claim is made about all weights, effective BT widths or height onsets,
actual numerical zero/pole locations, simplicity, unsigned asymptotics,
critical-line placement, a new automorphic family, or RH. The theorem also
does not conflict with a different large-weight, low-rank endpoint regime.
