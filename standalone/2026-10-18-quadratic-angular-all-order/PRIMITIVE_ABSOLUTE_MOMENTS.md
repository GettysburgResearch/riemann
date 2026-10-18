# Every fixed absolute moment of the exact split-prime source

**Status:** unconditional fixed-field asymptotic, conditional only on the *classical* generalized Ikehara–Delange Tauberian theorem (or the equivalent fixed-order ideal divisor asymptotic), not on RH, quasi-RH, a metaplectic theta estimate, or conjectural prime correlations. **This is an absolute coefficient moment, NOT a reciprocal L-value moment, not a signed principal moment, and not an RH proof.** The Euler factor and Tauberian method are classical; no priority claim is made.

Use the EXACT rational sequence b_K(n) from PRIMITIVE_CORE_EQUIVALENCE.md. Fix an imaginary quadratic K with discriminant d_K and a finite rationally saturated exclusion Q divisible by 6*rad(|d_K|). Thus b_K(n)=mu(n)2^omega(n) when n is squarefree and all its prime factors are unexcluded split primes, otherwise 0.

## Theorem: all fixed integer absolute powers

For EVERY fixed integer r>=1 put

    m_r=2^(r-1).

Then as X tends to infinity,

    sum_(n<=X) |b_K(n)|^r
       ~ C_(K,Q,r) X (log X)^(m_r-1),                    (1)

where C_(K,Q,r)>0 is the explicit absolutely convergent Euler product constant

    C_(K,Q,r)=kappa_(K,S)^(m_r) U_r(1)/Gamma(m_r),
    kappa_(K,S)=Res_(s=1) zeta_K^S(s),

    U_r(s) =
      prod_(p split,p∤Q)
           (1+2^r p^(-s))(1-p^(-s))^(2m_r)
      prod_(p inert,p∤Q)
           (1-p^(-2s))^(m_r).                            (2)

All ramified p are excluded. The coefficient Dirichlet series factors EXACTLY:

    sum_n |b_K(n)|^r / n^s
       =prod_(p split,p∤Q)(1+2^r p^(-s))
       =zeta_K^S(s)^(m_r) U_r(s), Re s>1.               (3)

At a split p write x=p^(-s); its correction is
(1+2^r x)(1-x)^(2m_r)=(1+2m_r x)(1-x)^(2m_r), whose LINEAR coefficient is ZERO. At inert p, (1-x^2)^(m_r) also starts at quadratic order. Therefore U_r(s) has an absolutely convergent Dirichlet series (indeed an absolutely convergent Euler product) in every Re s>1/2, with U_r(1)>0, independently of the value of fixed r.

The fixed Dedekind zeta zeta_K^S has one simple pole at s=1 with positive residue kappa_(K,S); zeta_K has no other singularities on Re s=1. All coefficients on the left of (3) are nonnegative. The classical generalized Ikehara–Delange theorem applied to (3) gives (1), including precisely the Gamma(m_r) factor. Alternatively, apply the fixed-order ideal divisor main term to the coefficients of zeta_K^S(s)^(m_r) and convolve with the correction coefficients, which are absolutely summable with weight n^(-sigma) for sigma>1/2. No zeros on the critical strip and no unproved moment estimates are used.

In particular:

    r=1:  sum |b(n)|    ~ C_1 X,
    r=2:  sum |b(n)|^2  ~ C_2 X log X,
    r=3:  sum |b(n)|^3  ~ C_3 X (log X)^3,
    r=4:  sum |b(n)|^4  ~ C_4 X (log X)^7,
    r=5:  sum |b(n)|^5  ~ C_5 X (log X)^15.

These reflect genuinely heavy, arithmetic (not subgaussian) absolute coefficient tails: the log exponent is 2^(r-1)-1. This growth is NOT an obstruction to RH, since the RH-equivalent criterion asks for signed cancellation in the cumulative sum b(n), rather than any of these positive moments. Fixed-r constants can grow arbitrarily with r; no growing-r uniform conclusion is claimed.

## Complete local coefficient identities

Let d_m^K(n) denote the rational norm coefficient of zeta_K^S(s)^m. Let u_r(n) denote the correction coefficient of U_r(s). Equation (3) says

    |b_K|^r = d_(m_r)^K * u_r.                            (4)

These are exact coefficient formulas, including all shared primes. For unexcluded split p and e>=1,

    d_m^K(p^e)=binom(2m+e-1,e),
    u_r(p^e)=(-1)^e binom(2m,e)
                   +2m(-1)^(e-1)binom(2m,e-1).           (5)

Binomial coefficients beyond their range are zero. For an inert p,

    d_m^K(p^(2j))=binom(m+j-1,j), d_m^K(p^(2j+1))=0,
    u_r(p^(2j))=(-1)^j binom(m,j), u_r(p^(2j+1))=0.       (6)

At excluded primes these series are 1. The local Dirichlet convolution (4) can be verified at any finite degree without enumerating ideals.

## Checks and relevance to the harder target

The included check_primitive_moments.py verifies the complete identity (4) for every n<=1200 and EACH r=1,2,3,4,5, i.e. 6,000 exact integer convolution identities. Normal and optimized Python produce identical archived RESULTS_PRIMITIVE_MOMENTS.json. The checker tests (4), NOT the asymptotic proof or generalized Delange.

This is a source-faithful calibration for experiments on the fixed rational primitive-core target. It may suggest which high-moment inequalities are fundamentally lossy: taking absolute moments here preserves magnitude but completely deletes the very split-prime parity sign whose square-root cancellation is equivalent to Dedekind RH. In particular, substituting this theorem for a signed native 2k-th critical moment would be a category error. The signed open target in PRIMITIVE_CORE_EQUIVALENCE.md remains unchanged.
