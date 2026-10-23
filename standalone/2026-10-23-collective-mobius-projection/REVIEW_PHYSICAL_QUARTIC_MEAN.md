# Independent review of the physical quartic cubic-row mean

23 October 2026. Reviewed object:
`../two-hour-type-20261023/PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md`, SHA256
`eea3bd9425f35ab198795ab50febd650ff098f26c2fe5ca716d204346a52f1b8`.
The reviewer did not write the mean proof. The local identity and consumer
had been discussed independently before this review. No reviewed bytes
were changed.

Verdict: no mathematical defect found in the stated squarefree-row,
fixed nonzero angular-mode estimate or its explicitly unsuccessful
inverse consumer. This is a source-dependent analytic review, not a
formal certification of DDHL or the imported large sieve.

## Source interfaces

I checked the live primary sources DDHL
<https://arxiv.org/html/2306.11875v4>, equations (3.7), (4.12)--(4.28),
Proposition 4.3 and its convexity proof, and de Faveri
<https://arxiv.org/html/2610.04045v1>, Theorem 1.1.

The numerator valuation three admits precisely the good-prime modulus
exponents zero and four; the latter coefficient is minus the cube of
the prime norm. After the half-unit shift of the Dirichlet variable,
the local factor in Q2 and the deleted Euler factor in Q3 agree.
Fourth-power CRT phases are trivial. The completion variable need not
be coprime to the squarefree column, and the proof correctly preserves
that fact.

DDHL's complete cusp vector, together with both angular signs, is
closed. Its bad-prime expansion is finite because the numerator has
fixed valuation at the bad prime. The remaining dependence on the
good row is periodic and can be partitioned into finitely many sectors.
This is sufficient for the sieve application; no claim of arbitrary
growing conductor twists is needed.

## Absorption and height

The original fourth-power completion is summable in amplitude on the
line in question: its mass is bounded by the ideal sum with exponent
1+4 delta. Freezing a completion ideal restricts the positive row norm,
so the natural common-prime mask causes no loss. Applying the imported
quartic sieve to each squarefree column dyad gives Q7.

The functional equation keeps the numerator k cubed. Its squared
conductor factor is K raised to 6 delta. The three complex gamma
quotients produce height raised to 12 delta in the squared residual;
the rational bad-prime matrices are bounded on the chosen vertical
line. The signs and the contour displacement in Q8--Q9 are consistent.
Nonzero angular type removes the possible poles of the completed
family; division by gamma factors introduces no poles.

With cutoff Y=C0 K^(3/2) L^3, the residual coefficient is a constant
times C0^(-4 delta). The three displayed height monomials are stable
under Gaussian convolution. The fourth original sieve term produces
K^(13/8-3 delta)L^(9/4-6 delta); the other mixed term is bounded by
K^(3/2-3 delta)L^(3-6 delta). This verifies Q5 algebraically.

The supremum used for absorption is finite before absorption: at each
fixed row dyad, source convexity bounds the squared height growth by
L^(3-6 delta+epsilon), while Q5 includes that height exponent with a
strict small epsilon buffer. Filling the bounded excluded discs uses
entireness and the maximum principle. There is no unjustified supremum
over all row lengths in this argument.

## Consumer and limitation

Mellin inversion of the normalized annular sum costs D^(2 delta) in
the squared norm. The reciprocal completion factor lies on real part
1+4 delta, so its absolute Euler-product bound is uniform in the
deleted good primes. The integrated height factors are absorbed by
the fixed smooth Mellin transform. Thus Q11 follows without any new
zero-free-region assumption.

At K=D^2/H and H=D^a, 0<=a<=1, the two pieces meet at delta=5/24.
Below that value the exponent in Q12 has slope 3a-4<0; above it the
slope is 2. The optimum is exactly D^(17/12+epsilon), independently
of a. It does not approach the desired row scale H in this range.

An additional way to see the same obstruction is the length comparison

    D / sqrt(K^3) = H^(3/2)/D^2 <= D^(-1/2).

The physical annulus is always on the short side of this functional
equation for H<=D. A single reflection has length K^3/D, which is
larger than D. Cancelling the local completion factors does not change
this conductor. This observation rules out the proposed direct
long-sum interpretation, not a more refined centered cancellation
argument.

No all-row, moving-angular, complementary-projector, new fixed
zero-free-boundary, or RH assertion follows from this review.
