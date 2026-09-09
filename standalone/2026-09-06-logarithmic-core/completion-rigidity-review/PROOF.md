# Direct native-sign attempt: exact variational rigidity and a shorter frequency range

Date: 2026-09-07. Status: PROPOSED COMPONENT PROOFS; independent review required.
**This is not a complete proposed proof of RH. The arithmetic sign/count estimate in Section 7 is unproved.**
Parent: PR #803 at ed074bcabfd2c1ca3336e457b8fdd09a25bcd2a7.
Local labels CR1--CR4 are not canonical claim IDs. No external novelty is claimed.

## 1. The exact problem and what this pass attempts

For all real m >= 2, retain the literal prime-power source

    w(u) = u/3 - 1/(192u^2),        1/4 < u <= 1,
           1/(3u^2) - u/192,        1 < u < 4,
           0,                      otherwise,
    a0 = 45/128,
    P(m^2) = (1/m) sum_n Lambda(n) w(n/m^2),
    D(m) = P(m^2) - a0 m + 1/4.                         (1)

All prime powers have Lambda(p^j) = log p. Both outside endpoint values are zero.
The weight is continuous at 1. No prime-only, sampled-spectrum, or random-source substitution is made.

The parent supplies finite polynomials with the genuine Mobius prefix and two exact normalizations. The attempted finish is to exploit the freedom in their remaining coefficients to make the critical-line integral nonnegative, or sufficiently rarely negative. This pass solves that *variational* question exactly: the complete signed functional is constant after both normalizations are fixed. Before the second normalization is imposed, its Hessian has rank one. This does not determine the unknown minimum.

Separately, a uniform tail estimate reduces the remaining frequency interval. Neither result supplies its sign. The final conditional implication is spelled out so that the unproved premise is not delegated to a reviewer to discover.

## 2. Admissible polynomials, finite source identity, and contour

Let Y >= ceil(2m) be an integer. Let p(s) = sum p_n n^(-s) be ANY finite real Dirichlet polynomial such that

    p_n = mu(n) for n < Y,       p(1) = 0.               (2)

Write d = p'(1). Coefficients above Y are unrestricted for CR1; no uniform bound or fixed support multiple is assumed until Section 4.

The admissible class is nonempty with any prescribed real d. Explicitly, set

    M = sum_(n<Y) mu(n)/n,
    L = sum_(n<Y) mu(n) log n/n,
    ell = (1/Y) sum_(Y<=n<2Y) log n,
    q(s) = (1/Y) sum_(Y<=n<2Y) n^(1-s),
    b = (M ell - L - d)/log 2,        a = -M-b,
    p(s) = sum_(n<Y) mu(n)n^(-s) + q(s)(a+b 2^(1-s)).   (3)

Its support is below 4Y. Since q(1)=1 and q'(1)=-ell, direct differentiation gives p(1)=0 and p'(1)=d.
For d=1 this is precisely the parent's p_Y. The parent proves, by the exact harmonic divisor identity, |p_n|<20 and

    S(p) := sum |p_n|^2/n < 130 + log Y.                 (4)

Those bounds are an explicitly pinned dependency, freshly replayed at their finite test scope. They are not used to infer an unproved continuum norm. The new uniform estimates below in fact assume only the stated support and S(p) bounds, not the particular formula (3).

Let u(n)=1, e(n)=1_(n=1), l(n)=log n, and use Dirichlet convolution. With r=e-u*p,

    Lambda_p = 2p*l - p*p*u*l,
    Lambda - Lambda_p = Lambda*r*r.                     (5)

Indeed mu*u=e and mu*l=Lambda. Expanding Lambda*(e-2u*p+u*u*p*p) proves (5). Since r vanishes for n<Y and Lambda vanishes for n<2,

    Lambda_p(n)=Lambda(n) for n<2Y^2.                   (6)

The first possible difference is at 2Y^2 and equals log 2 times r(Y)^2. All n in the nonzero support of (1) are below 4m^2 <= Y^2, so their coefficients agree exactly. This is the classical quadratic convolution principle, not a new inversion theorem [E1].

On Re s>1 the proxy has Dirichlet series

    L_p(s) = -2 zeta'(s)p(s) + zeta(s)zeta'(s)p(s)^2.    (7)

It is meromorphic with no possible pole except at 1. In particular it has no reciprocal-zeta poles. It is NOT the native logarithmic derivative globally.

The entire Mellin transform of the weight is

    J(s) = integral_(1/4)^4 w(u)u^(s-1)du
         = [65/64 - (4^(s-1/2)+4^(-s+1/2))/8]
           / [9/4-(s-1/2)^2].                           (8)

The apparent poles are removable. On any fixed vertical strip it is O((1+|t|)^(-2)), and

    j(t):=J(1/2+it)
        = [65/64 - cos(t log 4)/4]/(9/4+t^2)>0.          (9)

Define the real quadratic functional

    I_m(p) = (1/pi) Re integral_0^infinity
                 j(t)L_p(1/2+it)m^(2it)dt.              (10)

For every fixed finite p the integral converges absolutely. The classical bounds

    |zeta(1/2+it)| + |zeta'(1/2+it)|
                      <<_eta (1+|t|)^(1/4+eta)          (11)

and their fixed-strip versions suffice, with 0<eta<1/4. For zeta this follows from the approximate functional equation and convexity; Cauchy's formula on circles of radius comparable to 1/log |t| supplies zeta', with the logarithm absorbed into eta [E2]. No numerical constant is certified here, and no zero-location assumption is used.

Mellin inversion initially on a fixed 1<c<2 is absolutely convergent. Shift to Re s=1/2. The horizontal segments tend to zero by (8),(11), and the sole crossed pole is at 1. All zero-valued weight endpoints avoid half-weight ambiguities. Pairing conjugate t gives (10). These justifications are for each finite p; uniformity over families is proved separately in Section 4.

## 3. CR1: the complete variational problem has exactly one direction

**Theorem CR1.** Under (2), for every m and Y as above,

    I_m(p) = D(m)-1/4 + a0 m (p'(1)-1)^2.               (12)

Consequently

    min_(p satisfying (2)) [1/4+I_m(p)] = D(m),          (13)

and the minimizers are exactly the polynomials with p'(1)=1. Every such minimizer gives the SAME complete signed integral. The minimum is attained by (3). No positivity of that minimum is inferred.

Proof. Write z=s-1. Since p(1)=0,

    p(1+z)=d z+O(z^2),
    zeta(1+z)=z^(-1)+gamma_E+O(z),
    zeta'(1+z)=-z^(-2)+O(1).

Equation (7) has residue 2d-d^2 = 1-(d-1)^2 and no higher pole. The contour identity therefore reads

    P(m^2)=a0 m(2d-d^2)+I_m(p).

Substitute (1). This proves (12), and the remaining assertions follow because a0 m>0 and every d is attainable. End of proof.

### 3.1 Polarized tail formula and the exact null space

Let v,w be finite real Dirichlet polynomials supported at indices n>=Y, with v(1)=w(1)=0. Polarization of (12), or a separate contour calculation, gives

    (1/pi) Re integral_0^infinity
       j(t)zeta(1/2+it)zeta'(1/2+it)
       v(1/2+it)w(1/2+it)m^(2it)dt
       = a0 m v'(1)w'(1).                              (14)

For the separate calculation, the Dirichlet coefficients of zeta*zeta'*v*w vanish below 2Y^2, while its residue at 1 is -v'(1)w'(1). Its weighted coefficient sum is zero, so shifting the contour proves (14), with the sign shown.

Thus the Hessian of I_m on the real affine space (2) is

    Hess I_m(v,w)=2a0 m v'(1)w'(1).                     (15)

It has rank exactly one; a tail v=n0^(-s)-2(2n0)^(-s), n0>=Y, has v(1)=0 and v'(1)=(log2)/n0 !=0. Its radical consists exactly of variations also satisfying v'(1)=0. This is a REAL symmetric form with v(s)w(s), not a Hermitian form with a modulus square. No positivity of the unrestricted zeta/Weil form is claimed.

For any p with p'(1)=1, the first variation in every v satisfying v(1)=0 is zero. Variations with both jets zero leave I_m EXACTLY unchanged, not just to second order. This solves the completion optimization, not the native sign problem.

### 3.2 Convexity does not pay the intercept

A claim that (15) makes 1/4+I_m nonnegative would confuse a positive Hessian with a nonnegative minimum. Its homogeneous two-variable matrix is

    [[D(m)+a0 m, -a0 m], [-a0 m, a0 m]],

whose determinant is a0 m D(m). Checking its positivity is exactly checking the missing arithmetic sign again. Choosing d far from 1 can make I_m positive only by adding the known term a0 m(d-1)^2; subtracting the incorrectly retained main term would invalidate the source identity.

### 3.3 General three-jet residue as a normalization check

When p(1)=a, p'(1)=b and p''(1)=c, put H(s)=J(s)m^(2s-1), H_i=H^(i)(1). The complete residue of H(s)L_p(s) is

    -a^2 H_2/2 + (2a-2ab-gamma_E a^2)H_1
       +(2b-b^2-ac-2gamma_E ab)H_0.                     (16)

To verify it, zeta*zeta' has principal terms -z^(-3)-gamma_E z^(-2) and NO z^(-1) term. Multiply by p^2 and combine -2zeta'*p. Formula (16) is not used to license an unbalanced shift with the old residue. It records the higher principal parts that would otherwise be lost.

## 4. CR2: a uniform tail bound, before fixing the frequency cutoff

Let p be any finite real polynomial supported at n<=N, S=sum |p_n|^2/n, and put A_N=4N(1+log N). For every U>0 and any real interval of length U,

    integral |p(1/2+it)|^2 dt <= (U+A_N)S.               (17)

Proof. Expand the finite square with b_n=p_n/sqrt(n). The diagonal is US. Each unordered pair contributes at most 4|b_n b_k|/|log(k/n)|. For k>n use log(k/n)>=(k-n)/N and 2|b_n b_k|<=|b_n|^2+|b_k|^2. Harmonic row sums prove (17); A_N is deliberately larger than necessary. End of proof.

Let Tail_m(p;T) be the integral of the ABSOLUTE VALUE of the integrand in (10), including 1/pi, on [T,infinity), with T>=1. For each 0<eta<1/4, (9),(11),(17) give

    Tail_m(p;T) <<_eta
      sqrt(S)[T^(-3/4+eta)+sqrt(A_N)T^(-5/4+eta)]
       + S[T^(-1/2+2eta)+A_N T^(-3/2+2eta)].             (18)

The constant is independent of m,N,p,T; eta and the classical zeta bounds determine it. The phase m^(2it) has modulus one. No moment or sign assumptions enter.

For details, on [U,2U] the linear term is at most a constant times U^(-7/4+eta) integral |p|. Cauchy--Schwarz and (17) give the first bracket at U. The quadratic term is at most U^(-3/2+2eta)(U+A_N)S. Sum these bounds over U=2^j T; all exponents are negative. This accounts for the entire tail without truncating a coefficient or sampling a frequency.

## 5. CR3: shorter remaining interval and uniform asymptotic rigidity

Fix A>=4, B>=130 and 2/3<nu<=1. Consider all polynomials in (2) that also satisfy

    p'(1)=1,       N<=A Y,       S<=B(1+log Y).           (19)

The distinguished (3) with d=1 belongs to this class for every Y>=2 by (4). For 0<epsilon<3nu/2-1, (18) gives, uniformly over (19),

    Tail_m(p;Y^nu)
       <<_(A,B,nu,epsilon) (1+log Y)^2
                                Y^(1-3nu/2+epsilon).    (20)

Choose eta sufficiently small, for example eta=epsilon/(2nu), decreasing it further if necessary. Substitute N<=AY and S<=B(1+log Y) into (18). For 2/3<nu<=1 the slowest-decaying exponent is 1-3nu/2+2nu eta, from the quadratic off-diagonal allowance. Both linear exponents and the other quadratic exponent are no larger. Enlarging the constant pays bounded Y. This proves (20).

In particular, taking nu=3/4 yields

    D(m)=1/4+I_(m,Y^(3/4))(p)
             +O_(A,B,epsilon)((1+log Y)^2 Y^(-1/8+epsilon)),
                  0<epsilon<1/8,                       (21)

where I_(m,T) denotes (10) restricted to [0,T]. This improves the parent's choice T=Y. The cutoff Y^(2/3) itself is NOT justified by this bound: its leading exponent would be zero before logarithms and convexity losses. Neither optimality nor impossibility below that cutoff is asserted; better mean or signed estimates may improve it.

Combining (12) and (20), any two p,q in (19) satisfy

    |I_(m,Y^nu)(p)-I_(m,Y^nu)(q)|
       <<_(A,B,nu,epsilon) (1+log Y)^2
                                Y^(1-3nu/2+epsilon).    (22)

This holds even if the choices depend on m,Y or on the outcome of an optimization. Hence optimizing the TRUNCATED SIGNED integral within this fixed bounded-norm class can change it only by a vanishing amount. Optimizing an absolute majorant is a different problem and is not ruled out. Leaving the support/norm class invalidates the uniform conclusion unless the enlarged tail cost is paid again.

These are norm-tail and rigidity statements, not a sign estimate for I_(m,Y^nu).

## 6. An actual-source check against a stronger false finish

A simpler proposed finish would use j(t)>0 to assert I_m(p)>=0 for a normalized p. That assertion is false for the ACTUAL source already at m=2, not merely for a synthetic model.

For every admissible normalized p with Y>=4, (12) gives

    I_2(p) = (35/128)log2 +(18343/124416)log3
       +(3971/38400)log5 +(1251/25088)log7
       +(2765/185856)log11 +(633/86528)log13 -45/64.      (23)

All prime powers through 16 are included; the endpoint at 16 has zero weight. Direct rational atanh-series bounds, reconstructed by verify.py, prove

    -17/500 < I_2(p) < -33/1000 < 0.                    (24)

Consequently D(2)=1/4+I_2(p)>0. This does NOT refute the weaker lower bound needed for RH. It only rules out treating the signed product in (10) as pointwise nonnegative because j is positive. No numerical contour quadrature or zero oracle is used in (23)--(24).

## 7. Full conditional endpoint, and the unproved assertion

For integer k>=2 use m=k^2, Y=2k^2, the distinguished p_Y, and define

    T_k=(2k^2)^(3/4),
    Z_k=(1/pi) Re integral_0^T_k
           j(t)L_(p_(2k^2))(1/2+it)k^(4it)dt.           (25)

Equation (21) implies D(k^2)=1/4+Z_k+o(1). In particular, eventually

    D(k^2)<-1  implies  Z_k<-1.                          (26)

Here is the UNPROVED proposed closing statement:

    OPEN: there are delta>0,C>0 such that for every K>=2,
          #{2<=k<=K : Z_k<-1} <= C K^(1-delta).          (27)

No power saving, eventual lower bound, or new native positive range is established in this manuscript. The shorter frequency range in (25) does not make (27) an evaluated finite problem; its quantifier is unbounded.

For clarity, the complete consumer of (27) is recalled next. It uses the following exact-source components established in the pinned sparse-sign and curvature manuscripts, NOT their open counting conclusions:

* If Theta is the supremum of real parts of all nontrivial zeros and alpha=2Theta-1, then |D(m)|<=C m^alpha. This follows from the absolutely summable, full paired-zero expansion, with all multiplicities and both reflected off-line members retained. No attained edge is assumed.
* The Mellin transform F(z)=integral_2^infinity D(m)m^(-z-1)dm has meromorphic continuation regular near every positive real z. At each zero rho with Re rho>1/2 it has a nonzero pole at 2rho-1, of residue -m_rho J(rho). The compact initial term is retained and the real main pole cancels.
* On [k^2,(k+1)^2], the exact prime-power curvature/Green bound is
  D(m)>=min(D(k^2),D((k+1)^2))-45log(4(k+1)^4), k>=3.

Assume (27), decreasing delta to min(delta,1) if needed. By (26) the count of D(k^2)<-1 obeys the same power saving after absorbing finitely many initial nodes. Put f(m)=D(m)+1+45log(64m^2) for m>=9. Its negative part is supported only in square-grid cells adjacent to such failed nodes. In [T,2T] their total length is O(T^(1-delta/2)), since each cell has length O(sqrt T) and only O(T^((1-delta)/2)) nodes fail. Also f_-<=D_-<=C T^alpha there. Thus the Mellin transform of f_- is holomorphic for Re z>alpha-delta/2.

The transform of f itself differs from F only by compact entire terms and elementary transforms with poles at zero. If the nonnegative f_+ had convergence abscissa larger than max(0,alpha-delta/2), its continuation would be regular at that positive real boundary, contrary to Landau's theorem. Here is its short proof: at a point just to the right of a hypothetical regular real boundary, evaluate the Taylor series to the left. All coefficients after removing alternating signs are nonnegative integrals. Tonelli identifies the series with the convergent integral beyond that boundary, a contradiction. Compact initial pieces do not affect the argument.

Both parts therefore converge to the right of max(0,alpha-delta/2), and F has no pole there. If alpha>0 this contradicts the supremum alpha of the real parts of the surviving poles at 2rho-1. It does not require a pole on that supremum line. Therefore alpha=0; reflection gives RH.

This proves OPEN => RH, but NOT OPEN. The analytic consumer is given for checking the inference, not as a substitute for the required arithmetic estimate. The exact variational identity (12) shows why merely selecting a different completion does not supply OPEN. A uniform estimate exploiting the actual Mobius prefix in the low-frequency SIGNED integral, or another genuinely stronger arithmetic input, is still needed.

## 8. Referee boundary

CR1--CR3 have complete proposed arguments above; (23)--(24) have a bounded independently implemented arithmetic check. Classical analytic inputs are identified in SOURCES.json. The inherited spectral/curvature components in Section 7 require their own review and are not certified by this author replay. CR1--CR3 do not use those components or the old length-one numerical certificate.

There is no theorem here asserting native all-scale positivity, any nontrivial failure-count upper bound, RH, numerical values of the contour integrals, a formal kernel proof, or a new external priority. The experiment counts in result.json are bounded fixtures, not counts of proved infinite assertions. The finite checker cannot establish OPEN, the convexity estimate, or Landau's analytic theorem.
