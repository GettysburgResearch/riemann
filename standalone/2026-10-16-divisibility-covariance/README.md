# Unconditional off-diagonal estimates for the coupled Gaussian source

Status: PROPOSED complete unconditional component proofs, with exact finite
checks. No critical-energy bound, new zero-free region, or RH proof. No
independent mathematical review or formal proof-assistant build.

Base: #952, `3b7d2948840446c752bbf284f6f90f6592395a29`.
Read [THEOREMS.md](THEOREMS.md); source and review limits are in
[SOURCES.md](SOURCES.md) and [VALIDATION.md](VALIDATION.md).

## Actual new estimates relative to the preceding packet

The source has local coefficients at exponents 0,1,m, with
`c(p)=-(1-1/q)a_p`, `c(p^m)=-q^(m/2-1)b_p`. At m=6 it is exactly the
coupled coefficient source used in #952, not a changed prime-sign model.
The original Gaussian and every nonunit zero remain.

**1. Entire divisibility sector.** For every m>=3, all D>=1, arbitrary
bounded phases and masks, the absolute Gaussian-energy sum over ALL unequal
ideal pairs with one ideal dividing the other is `O_K,c(1+log D)`.
The constant is independent of m and the masks. A nonnegative physical row
measure of total mass Z only multiplies this bound by Z. This also holds
for the original Mobius source. It is a proved bound for genuine off-diagonal
terms, extending #952's ideal-diagonal estimate.

**2. Signed infinite prime-quotient asymptotic.** For the principal source,
with arbitrary unit powerful phases, sum every ordered pair whose quotient
in either direction is any good PRIME IDEAL. At m=6 the exact subtotal is

    P_6(D)=-L log D+B-J D^(-1/6)+O_epsilon(D^(-1/4+epsilon)),
    L>0, J>0, 0<epsilon<1/12.

The constants are explicit convergent products and sums. This whole subtotal
is strictly negative for every D>0. No theta-phase character assumption,
critical moment hypothesis, quasi-RH result, or zero-free region is used.

**3. Nonzero secondary square-coefficient term.** For K=Q(omega), the actual
Gaussian with c=5/6, and fixed exclusions,

    sum_n |c_6(n)|^2 W_(5/6)(Nn/X)
           =A X-B X^(5/6)+O_epsilon(X^(3/4+epsilon)), A,B>0.

The proof establishes a two-pole continuation of the positive coefficient
Dirichlet series using elementary zeta/L partial summation. The leading
square-mass density is independent of m, and the general secondary exponent
is 1-1/m. This is not a zero-free claim or an asymptotic for a different theta
coefficient family.

**4. Forced positive covariance.** With only the primes over 2,3 excluded,
the two split ideals over 7 and the two over 13 give negative prime-quotient
covariance exceeding the leading ideal diagonal by more than 5%. Therefore
ALL other off-diagonal terms together are at least `c log D-C`, c>0.
A short rational certificate verifies the strict 5% margin. This is
unconditional, not an implication assuming RH, and it prevents a false
blanket-negativity conclusion for the complement.

## What is still unresolved

Incomparable ideals with large coprime reduced cores are not bounded here.
The Gaussian suppresses a large quotient in the divisibility theorem, but
it does not suppress two different large cores of comparable norm. The
critical total-energy estimate and generalized native moments remain open.
The full-source comparisons do not identify these selected subtotals across
different completions. Standard Euler/Mellin methods are credited; no global
priority claim is made.

## Replay

    python check.py > /tmp/divisibility-normal.json
    python -O check.py > /tmp/divisibility-optimized.json
    cmp RESULTS.json /tmp/divisibility-normal.json
    cmp RESULTS.json /tmp/divisibility-optimized.json
    python verify_manifest.py

The fixed tests include 51,030 exact coefficient-pair checks with literal
Eisenstein characters and all 54 rows of norm <=13 at the principal m=6
fixture. The pair fixture is ONLY a three-prime semigroup. Separately, two
complete constructions agree for every rational norm <=200,000 at
m=3,4,6,8: 800,000 exact norm-fiber coefficient equalities, retaining split
multiplicity and inert norms. These are finite checks, not the analytic proof.
