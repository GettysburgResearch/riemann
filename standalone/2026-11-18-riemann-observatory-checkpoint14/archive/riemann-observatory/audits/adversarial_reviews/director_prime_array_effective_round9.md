# Director adjudication: effective bounds, finite certificates and a failed cutoff

17 November 2026. I read the complete proofs in prime_array63_effective_bound.md and prime_array63_effective_bound_skeptic.md, the original finite-ball program and its independent QA, and generator63_hard_mangoldt_skeptic.md. I checked the constant arithmetic, pole cancellation, contour identity, tail integral and binomial lower bound. Definitions are those of [the prescribed tapered array](director_tapered_prime_array_round9.md). The bounds are deliberately coarse; they are not estimates of the actual limiting constant.

## An explicit RH-conditional global upper bound

For L=log N, every integer N>=3 satisfies, under RH,

    E_N(2) <= 10^27/L,
    E_N(k) <= 10^44 k^6/L       (every integer k>=2).

Here E_N(k) is the full squared boundary error of the prescribed anchored logarithmic prime array, not an infimum over unspecified coefficients. The independent k=2 proof establishes |zeta|+|zeta'|<=10^5(2+|t|)^(7/16) from Euler summation, the functional equation and Gaussian three-lines. Jensen gives at most 100 log(2+|t|) zeros in a unit window on RH. Paired Hadamard differences and a fixed radius-1/4 disc give a regularized derivative at most 10^5 log(2+|t|). The left contour and actual anchor are bounded separately. In the full boundary norm the scaled squared near part is less than 10^23, and the four remaining parts together contribute less than 2·10^26 before the final factor 2. Thus 10^27 is valid. No derivative of a moving zero cutoff is taken. Horizontal contours avoid zeros before the limit.

The separate general-k proof uses (k^(1-s)-1)/k^3, whose first two derivatives and strip values have uniform elementary bounds. Its assembled squared bound is below 10^44. This proof supplies the stated simultaneous k,N inequality; the sharper k=2 argument alone would not do so. Neither proof assumes simple zeros or inverse-derivative moments.

Consequently for any prescribed integer sequence k_N>=2 with k_N^6/log N tending to zero, RH is equivalent to E_N(k_N) tending to zero. The forward implication uses the uniform bound. For the converse fix one right off-line zero; its first nonvanishing derivative jet annihilates every competing polynomial, while |k_N^(1-rho)-1|>=2^(1-beta)-1. The fixed evaluation norm gives a uniform positive error lower bound. This does not give a joint leading-constant asymptotic or a useful practical threshold for large k.

## Unconditional finite full-error enclosures

The 160-bit run and independent 224-bit replay bound the entire norm, including the infinite tail. For k=2 the squared enclosures are

| N | Full squared-error interval |
|---|---|
| 10 | [0.342801539918328691, 0.343111054662620134] |
| 30 | [0.247656566621497315, 0.247904631616511935] |
| 100 | [0.179598089981701525, 0.179908683595524940] |

The finite sum is exact unit-cell integration with ball coefficients. If X is the last cell, Y=X+1 and S is the sum of absolute floor coefficients, the tail is at most

    [(2 log Y+S)^2+4(2 log Y+S)+8]/Y.

This follows from |R_2(x)|<=2 log x and the anchor-cancelled bounded floor combination. Endpoints are rounded outward from exact dyadics. These certificates are unconditional finite computations. Their L-scaled values are not monotone and do not certify the infinite limit or RH.

Original v1 code and result hashes remain preserved. The subsequent v2 replaces generic ball exponentiation by explicit multiplication and rejects nonfinite balls at unsupported precision; the actual original 160/224-bit computations were already finite and valid. Independent QA replayed the full N=10 case for both versions and checked coefficient, direct-cell, whole-small-sum, rounding and low-precision controls. See jump_factorial_prime_array63_finite_qa.md and the version-specific reproducibility document.

## A natural hard cutoff diverges despite exact initial-cell matching

Let f_j(x)=j floor(x/j)-floor x and define the anchored finite candidate

    A_(k,M)=log k (f_k-f_M)+sum_(d<=M) Lambda(d) f_k(x/d).

Its length is at most kM. It agrees exactly with R_k on all cells x<M. Nevertheless

    ||R_k-A_(k,M)||^2 >= M(log k)^2/68,
    ||R_k-A_(k,M)||^2 = Theta_k(M).

On [M,2M) the error is psi(x)-psi(M)-M log k. For h<=M/16, Legendre's formula gives psi(M+h)-psi(M)<=log binomial(M+h,h)<(M/2)log 2. Integration on [M,17M/16] gives the lower bound because the dx/x^2 mass is 1/(17M). The elementary dyadic-binomial estimate psi(M)=O(M), bounded floor functions and logarithmic target give the upper bound. No PNT or prime-gap hypothesis is needed. The exact comparison is this displayed renormalized hard cutoff; it is not an assertion about every unsmoothed truncation of the tapered coefficients. The negative result identifies why agreement on arbitrarily many initial cells alone cannot control this norm.
