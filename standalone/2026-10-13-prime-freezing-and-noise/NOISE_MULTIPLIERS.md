# Uniform invertible noise multipliers for the native family

Status: PROPOSED reviewable mathematics; complete proofs below, not independently reviewed. The analytic factorization is a native-field adaptation of established biased-random-multiplicative-function theory, not a newly discovered RH equivalence. No original undamped moment bound or zero-free exponent is improved here.

Scope: a fixed number field (in the application K = Q(sqrt(-3))), arbitrary deterministic local phases of modulus at most one, literal local zeros, arbitrary bias profiles, and every fixed moment order. The finite coefficient estimates are uniform in the bias profile and hence allow a profile depending on the column cutoff. The infinite analytic assertions concern one fixed profile at a time.

Dependencies: ideal counting A_K(X) <<_K X and its harmonic consequence; an elementary sign inequality proved below; ordinary Dirichlet-series convergence and independent mean-zero random-series convergence. The native source is PR #930, `ef64e9591fa5a5530c513606b0a17cbbdba9820a`, `standalone/2026-10-12-parity-and-cubic-fibers/PARITY_DAMPED_MOMENTS.md`, Sections 1, 5--7. Historical source: Aymone--Sidoravicius, arXiv:1412.1157v2, Lemma 2.1 and proof of Theorem 1.1, especially Claim 4.1 (printed p.14).

## 1. Local normalization and exact algebra

All sums and convolutions are over nonzero integral ideals. Bad primes and any moving exclusion are implemented by setting the corresponding local phase to zero. Write xi(p) for the remaining local phase, |xi(p)| <= 1, extended completely multiplicatively. In the native application xi_u(p) = nu(p) (u/p)_6. In particular a prime dividing the row has phase zero; it is not replaced by a unit phase.

Choose deterministic numbers 0 <= a_p <= 1, and independent signs e_p with

    P(e_p = +1) = (1-a_p)/2,    E e_p = -a_p.

Put z_p = e_p+a_p. Let f(p)=e_p xi(p), f(p^j)=0 for j>=2, and define m(p)=-a_p xi(p), m(p^j)=0 for j>=2. All multiplicative functions in this note equal one at the unit ideal.

For a formal variable x, with the phase kept outside x, define

    H_p(x) = (1+e_p xi(p)x)/(1-a_p xi(p)x),
    G_p(x) = H_p(x)^(-1).

Let h,g denote the multiplicative coefficient sequences of these Euler products. Their exact prime-power coefficients are

    h(p^j) = z_p a_p^(j-1) xi(p)^j,
    g(p^j) = -z_p (-e_p)^(j-1) xi(p)^j,              j>=1.       (1.1)

The convention a^0=1 includes a=0. In particular the squarefree function f is not h unless all relevant biases vanish. Formal multiplication proves coefficientwise

    f = m*h,       h*g = delta_1,       f*g = m.                 (1.2)

No analytic convergence is needed for these identities; a coefficient has only finitely many ideal divisors.

There is a useful second factorization of the inverse. Define

    h_minus(p^j) = -z_p (-a_p)^(j-1) xi(p)^j,
    d(p^(2j)) = (1-a_p^2) xi(p)^(2j),    d(p^(2j-1))=0.

Then

    g = d*h_minus.                                               (1.3)

Indeed, at x with the phase included as y=xi(p)x,

    (1-a_p y)/(1+e_p y)
      = (1-a_p^2 y^2)/(1-y^2) * (1-z_p y/(1+a_p y)).              (1.4)

This uses e_p^2=1. The first factor is supported on square ideals and has coefficients of modulus at most one. The second factor has one centered sign per distinct prime. Thus the inverse is not merely another centered squarefree series: its deterministic square contribution must be retained.

### A concrete coupled cancellation

At p^2 the coefficient of f*g is identically zero, as required for m. Its two nonzero summands have expectations

    E g(p^2) = (1-a_p^2) xi(p)^2,
    E [f(p)g(p)] = -(1-a_p^2) xi(p)^2.                           (1.5)

They cancel exactly. Replacing g by an independent copy would give E[f(p)] E[g(p)]=0 and would leave the first term. Therefore independence between the two factors in (1.2) is an invalid inference, even though each factor separately admits useful estimates.

## 2. Elementary coefficient lemmas

### Lemma 2.1: centered-sign inequality

If F(z)=sum_I B_I product_(p in I) z_p is multilinear, then for every fixed integer k>=1,

    ||F||_(2k)^2 <= sum_I [4(2k-1)]^|I| |B_I|^2.                 (2.1)

Proof. Take an independent copy z'. Multilinearity and E z'_p=0 give F(z)=E_(z') F(z-z'). Jensen reduces the estimate to z-z'. Each coordinate is the difference of two identically distributed signs, hence symmetric, independent across primes, and of absolute value at most two. Conditional on the absolute values it is a uniform sign times that absolute value; the zero case can be assigned an extra irrelevant uniform sign.

For uniform signs epsilon, the two-point inequality

    E |A+epsilon B|^(2k) <= (|A|^2+(2k-1)|B|^2)^k

holds for complex A,B. To check it, expand after replacing Re(A conjugate(B)) by |A||B| and use binom(2k,2j) <= binom(k,j)(2k-1)^j. Iterating this inequality, with the triangle inequality in L^k at each stage, gives sum_I (2k-1)^|I| |B_I|^2. The absolute values bounded by two supply the additional 4^|I|. This proves (2.1). QED.

### Lemma 2.2: bounded radical multiplicity

For every eta>0, uniformly over squarefree ideals r and X>=2,

    #{n: Nn<=X, rad(n)=r} <<_(K,eta) X^eta.                     (2.2)

Proof. Write n=r v, with all prime factors of v dividing r. Rankin's bound gives

    count <= (X/Nr)^eta product_(p|r) (1-(Np)^(-eta))^(-1).

For all sufficiently large prime norms the local factor is at most (Np)^eta. The finitely many smaller primes contribute a constant depending only on K,eta. Consequently the product is at most C_(K,eta)(Nr)^eta, proving (2.2). Empty ranges cause no exception. The same argument shows c^omega(r) <<_(K,c,eta) (Nr)^eta for every fixed c. QED.

## 3. Unconditional all-order bounds on BOTH noise directions

### Theorem 3.1

For every fixed k>=1 and epsilon>0, every X>=2, and every deterministic array b(n) supported on Nn<=X with |b(n)|<=1,

    E |sum_n b(n) h(n)|^(2k)       <<_(K,k,epsilon) X^(k+epsilon),
    E |sum_n b(n) h_minus(n)|^(2k) <<_(K,k,epsilon) X^(k+epsilon),
    E |sum_n b(n) g(n)|^(2k)       <<_(K,k,epsilon) X^(k+epsilon). (3.1)

Constants are independent of the biases a_p, phases xi(p), their zero set, X-dependent exclusions, and the array b. They are not asserted uniform in k growing with X. The array b must be deterministic with respect to the signs. It may depend on an arithmetic row. If nonnegative row weights have total mass at most H, summing gives H X^(k+epsilon) for each of the three families, even with a shared sign realization across rows.

Proof for h and h_minus. Group the sum by r=rad(n). It is a multilinear polynomial in z_p. Each grouped coefficient B_r is a sum of at most O(X^eta) terms by Lemma 2.2. Its deterministic prime-power factors a_p^(j-1), or their signed versions, have modulus at most one. Cauchy therefore gives

    sum_r |B_r|^2 << X^eta sum_(Nn<=X) |b(n)|^2 <<_K X^(1+eta).

Use (2.1) and c_k^omega(r) << X^eta. The squared L^(2k) norm is O(X^(1+2eta)). Raising to k and choosing eta sufficiently small proves the first two estimates. The constant unit coefficient is included in this argument.

Proof for g. By (1.3), write the polynomial as

    sum_(Nr<=sqrt(X)) d(r^2)
         sum_(Nm<=X/(Nr)^2) b(r^2 m) h_minus(m).

The factors are correlated across r, but Minkowski does not assume independence. Since |d(r^2)|<=1, the first part, also at scales between 1 and 2 by a fixed constant, bounds its L^(2k) norm by

    C X^(1/2+eta) sum_r (Nr)^(-1-2eta) <<_(K,eta) X^(1/2+eta).

The convergent ideal sum follows from A_K(X)<<X. Adjust eta to obtain the third estimate. QED.

This is a useful replacement for an unspecified 'harmless random Euler factor': it supplies finite, uniform, arbitrary-coefficient moment estimates for the multiplier and its actual inverse, including the square correction. It supplies no estimate for a dependent convolution of one of these factors with f.

### Corollary 3.2: a uniform bias-budget bound

For the squarefree random coefficients f and any deterministic bounded array b supported on Nn<=X,

    ||sum_n b(n)f(n)||_(2k)
      << X^(1/2+epsilon) sum_(d squarefree, Nd<=X) a(d)/(Nd)^(1/2)
      <= C X^(1/2+epsilon) exp(sum_(Np<=X) a_p/(Np)^(1/2)),     (3.2)

where a(d)=product_(p|d) a_p. Constants are uniform in the full bias profile. Indeed, f=m*h, so the left side is at most the sum over d of |m(d)| times the L^(2k) norm of sum_(Nm<=X/Nd) b(d m)h(m). Theorem 3.1 bounds that norm by C(X/Nd)^(1/2+epsilon). Minkowski is valid although the terms share signs; m is deterministic. The Euler-product majorant gives the second inequality. Reallocate epsilon as needed.

Thus a bias budget sum_(Np<=X) a_p/sqrt(Np)=o(log X) gives diagonal size at every fixed moment order. The lower cutoff may depend on the rate in this little-o statement. Taking a_p=1 on a frozen set and zero outside gives the companion note's growing-prime theorem. Taking a_p=(Np)^(-t), t>=1/2, recovers the elementary unconditional damping threshold. Neither example supplies a native undamped estimate.

## 4. Analytic factorization and pole transport: the classical connection

For one fixed profile a, define initially for Re(s)>1

    Z_a(s) = product_p (1+e_p xi(p)(Np)^(-s)),
    D_a(s) = product_p (1-a_p xi(p)(Np)^(-s)).

### Theorem 4.1

Almost surely there is a nonvanishing holomorphic H_a on Re(s)>1/2, with holomorphic inverse, such that

    Z_a(s) = D_a(s) H_a(s)                                      (4.1)

where initially both sides are given by their Euler products. For every delta>0 and q>0,

    E |H_a(s)|^q + E |H_a(s)|^(-q) <= C_(K,delta,q),
                         Re(s)>=1/2+delta.                      (4.2)

The moment constant is uniform in the fixed profile and in xi, including every native row and its exclusions. The almost-sure event is asserted for a fixed profile, not simultaneously over uncountably many moving profiles.

Proof of holomorphy. The logarithm of the local ratio is

    log H_p(s) = z_p xi(p)(Np)^(-s) + O_delta((Np)^(-2 Re(s))).

The remainder is locally uniformly absolutely summable. At each rational sigma>1/2 the independent centered linear series has summable variances, so it converges almost surely. Grouping prime ideals with the same norm gives an ordinary Dirichlet series. Convergence at each such real sigma implies locally uniform convergence to the right of sigma by the usual partial-summation theorem for Dirichlet series. A countable intersection proves holomorphic convergence throughout Re(s)>1/2. Exponentiating its sum defines H and its inverse and proves they are nonvanishing. Local power-series logarithms are legitimate because |xi(p)(Np)^(-s)|<1.

Proof of (4.2). Put x=xi(p)(Np)^(-s). Uniformly for 0<=a<=1 and |x|<=2^(-1/2),

    log |(1+e x)/(1-a x)| = (e+a) Re(x) + O(|x|^2).

Expanding the exponential to second order and using E(e+a)=0 proves, for either sign of the real exponent q,

    E |(1+e x)/(1-a x)|^(+/- q) <= 1+C_q |x|^2.

Multiply over any finite prime set, use independence and sum_p (Np)^(-1-2delta)<infinity, then apply Fatou to the almost-sure limit. This proves (4.2). Cauchy also gives a uniform positive lower bound for E|H|^q from the upper bound for its reciprocal moment. QED.

### Corollary 4.2: native shifted poles are not erased

For the power profile a_p=(Np)^(-t), t>=0, the deterministic factor is

    D_a(s) = 1/L_u^S(s+t),

with the native omitted Euler factors retained in L_u^S. Thus

    Z_(u,t)(s) = H_(u,t)(s)/L_u^S(s+t).                          (4.3)

Every zero rho of L_u^S with Re(rho)-t>1/2 becomes a pole of exactly the same order at rho-t, almost surely. The random factor cannot cancel it. Away from poles,

    C^(-1)|L_u^S(s+t)|^(-q)
      <= E|Z_(u,t)(s)|^q <= C|L_u^S(s+t)|^(-q)                  (4.4)

on Re(s)>=1/2+delta, with the same uniformity as (4.2).

For any fixed smooth compact test W whose Mellin transform is nonzero at rho-t, a bound for its random smoothed coefficient sum of the form O(D^beta), beta<Re(rho)-t, would make the Mellin transform analytic there and contradict this pole. Thus the pole has an observable coefficient consequence, not just a formal Euler-product interpretation. The quantifier concerns that fixed sample on the full-probability event and a fixed nonannihilating test. It asserts neither a lower bound at every scale nor an almost-sure square-root lower bound at the boundary.

The underlying untwisted statement is explicitly already in Aymone--Sidoravicius (2014/2015 preprint; 2017 publication). Their Claim 4.1 identifies F_alpha(s)=theta(s)/zeta(s+alpha), with theta and its inverse analytic on Re(s)>1/2. No novelty is claimed for this mechanism. The present proof makes the native phases, masks, uniform finite moments, and inverse square coefficients explicit.

## 5. Consequence for the research direction

PR #930 already proved a Jensen return cost D^(2kt). Equation (4.3) explains why that cost is structurally natural: power damping translates the inverse-L singularities; it does not disperse them among exceptional noise realizations. Establishing better properties of H alone therefore cannot remove the missing arithmetic estimate.

The alternative in `PRIME_FREEZING.md` uses a growing frozen-prime set rather than a fixed power profile. Its finite estimates are uniform in that changing set, and its exact return identity is a signed prime-by-prime telescoping formula. That identity has no Jensen power cost, but its final signed correlation estimate is still open.
