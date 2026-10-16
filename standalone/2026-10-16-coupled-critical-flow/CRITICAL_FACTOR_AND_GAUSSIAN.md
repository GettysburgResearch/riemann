# A cover-order-uniform critical factor and the actual Gaussian detector

**Status:** proposed component mathematics, with proofs below. The native critical bound, the generalized physical moments and RH are not proved. These notes and the tests have one author; there has been no independent mathematical review or Lean build.

**Scope:** a fixed number field F, its nonzero integral ideals outside a fixed finite set S, and arbitrary primewise phases of modulus at most one. Here m is a prime-power correction degree, not a claim that an automorphic representation of every cover degree has been constructed. For the below-critical continuation statement, S contains every prime ideal of norm 2. The inspected Dedekind source already excludes the primes over 2 and 3.

**Predecessors:** #948, `05b6f2172c686356ccd9900d33ffc5f526c5e98b`, EULER_STRIPPING.md, proves the m=6 coupled source and a two-way critical comparison with root cost log(D)^(12[F:Q]); it explicitly leaves the Gaussian adapter separate. #949, `cdb0666fc48d5166f5edd81f394b13e2001a6b5d`, RENORMALIZED_CERTIFICATE.md, proves the nonvanishing numerator on Re(s)>1/2 and the signed sixth-power Mellin operation. Those results are credited, not rebranded as new. This note separates one more explicit factor, proves a constant-cost remainder, improves the critical coefficient budget to one logarithm, and treats the untruncated Gaussian directly.

## 1. Local definitions and exact separation

Write q=Np, r=1/q, and let |a_p|,|b_p|<=1. Put m>=2 and

    A = a_p q^(-s),       D = b_p q^(m/2-1-ms),
    F_p(s) = 1-(1-r)A-D,
    j_p(s) = F_p(s)/(1-A),
    u_p(s) = F_p(s)/[(1-A)(1-D)].                         (1)

Complex powers of q use its real logarithm. The letters D in (1) and the later physical scale D are unrelated; in formulae below the local term is written explicitly when ambiguity is possible.

The exact identity is

    u_p = 1 + A(r-D)/[(1-A)(1-D)],
    j_p = (1-D) u_p.                                     (2)

At m=6 this is the normalized coupled factor from #948/#949, after omitting the constant product C_S=product_(p notin S)(1-q^(-2)). In the principal application a_p=1, and b_p is the actual sixth theta phase. No finite-order Hecke interpretation of b_p is assumed here.

Let c_m(n), j_m(n), u_m(n) denote the formal multiplicative coefficients of product F_p, product j_p and product u_p. The coupled coefficients are

    c_m(p)=-(1-1/q)a_p,
    c_m(p^m)=-b_p q^(m/2-1),
    c_m(p^e)=0 for e notin {0,1,m},     c_m(1)=1.           (3)

Let mu_a(n)=mu_F(n)a(n), where a is extended completely multiplicatively. Then c_m=mu_a*j_m, with unrestricted Dirichlet convolution. Shared prime factors in that convolution must not be deleted. The unique occupied-prime representation of (3), in contrast, uses disjoint exponent-1 and exponent-m prime supports.

If a physical nonunit mask at p applies, set BOTH a_p and b_p to zero. All its local factors are then one. In the usual twisted family a_p=xi_u(p) and b_p=eta_p xi_u(p)^m; this implements exactly the same zero in both branches.

## 2. A normally convergent, nonzero remainder below the critical line

### Theorem 1

Set alpha_m=m/[2(m+1)]. If S contains every prime ideal of norm 2, then

    U_m(s)=product_(p notin S) u_p(s)                     (4)

is holomorphic and nowhere zero for Re(s)>alpha_m. On every closed sub-half-plane strictly inside that domain, U_m and its reciprocal are bounded, for fixed m and F, uniformly in the phases. In particular, for m=6 the domain is Re(s)>3/7.

**Proof.** Put sigma=Re(s). The denominators in (1) are nonzero on sigma>=alpha_m: |A|<=q^(-alpha_m)<1 and |D|<=q^(alpha_m-1)<1. To prove the numerator is nonzero, it is enough to show

    (1-1/q)q^(-alpha)+q^(alpha-1)<1
          for q>=3, 1/3<=alpha<=1/2.                    (5)

For fixed q the left side is convex as a function of alpha, so its maximum on this interval occurs at an endpoint. For fixed alpha in that interval it is strictly decreasing for q>=3. Indeed, its derivative has the sign of

    -alpha q+(alpha+1)+(alpha-1)q^(2alpha),

which is at most -alpha for q>=3, using q^(2alpha)>=1 and alpha-1<0. At q=3, alpha=1/3, put t=3^(-1/3)<7/10; then the expression is (2/3)t+t^2<287/300<1. At alpha=1/2 it is 5/(3 sqrt(3))<1. This proves (5). Increasing sigma only decreases the absolute-value majorant. Thus each u_p is holomorphic and nonzero in the claimed domain.

For any fixed sigma0>alpha_m, (2) gives

    |u_p(s)-1| <= C_(sigma0,m)
          [q^(-1-sigma0)+q^(m/2-1-(m+1)sigma0)]           (6)

uniformly for sigma>=sigma0. Both exponents have prime-sum decay strictly greater than one. Comparison with sum_n (Nn)^(-t), t>1, proves normal and uniform convergence. For all sufficiently large q the local factors stay within 1/2 of one. The finitely many other factors stay bounded away from zero by (5). The same reasoning applies to the reciprocal product. QED.

The norm-2 exclusion in this continuation theorem is substantive. For m=6, a=b=1 and q=2, the numerator as a function of x=2^(-s) is 1-x/2-4x^6. At x=37/50 it is negative, while at x=0 it is positive; moreover (37/50)^7<1/8. A positive real root therefore corresponds to s>3/7. This does not affect the next critical-weight theorem, which permits norm 2.

The new 3/7 is the domain of a CORRECTION FACTOR, not a zero-free boundary for zeta. The primary reciprocal L-function is still present.

## 3. Constant coefficient cost at the critical weight, uniform in m

For a formal local series h(x)=sum h_e x^e define its absolute coefficient mass at t by sum |h_e|t^e. This is a coefficient norm, not the absolute value of h(t).

### Theorem 2

For all m>=2, all q>=2 and all permitted phases, u_p and u_p^(-1) have phase-independent nonnegative coefficient majorants whose masses at t=q^(-1/2) are at most

    1 + 2q^(-3/2)/[(1-q^(-1/2))(1-q^(-1))].              (7)

Consequently, there are multiplicative nonnegative majorants u_m^+,u_m^- for the two global coefficient kernels such that

    sum_n u_m^+(n)/sqrt(Nn) <= K_F,
    sum_n u_m^-(n)/sqrt(Nn) <= K_F,
    K_F := product_p [1+2q^(-3/2)/((1-q^(-1/2))(1-q^(-1)))]
          <= exp(32[F:Q]).                               (8)

These constants do not depend on m, S, moment order, row data or phases. The two majorants need not be the same coefficient sequence.

**Proof.** In the formal variable x, write A=a x and D=b q^(m/2-1)x^m. From (2), a nonnegative majorant for u_p-1 is

    x(q^(-1)+q^(m/2-1)x^m)/[(1-x)(1-q^(m/2-1)x^m)].       (9)

For the inverse use the distinct exact identity

    u_p^(-1)=1-A(r-D)/[1-(1-r)A-D].                       (10)

A majorant for its nonconstant part is

    x(q^(-1)+q^(m/2-1)x^m)/[1-(1-q^(-1))x-q^(m/2-1)x^m]. (11)

At t=q^(-1/2), q^(m/2-1)t^m=q^(-1)=r, independently of m. Both (9) and (11) therefore have mass 2rt/[(1-r)(1-t)], since 1-(1-r)t-r=(1-r)(1-t)>0. All geometric series used here genuinely converge at t. This proves (7).

Multiply the coefficientwise nonnegative majorants over prime ideals and use Tonelli. For q>=2, (1-q^(-1/2))(1-q^(-1))>=1/8, so log K_F<=16 sum_p q^(-3/2). There are at most [F:Q] primes over a rational prime and their norms are at least that prime. Finally sum_(n>=2)n^(-3/2)<=2. This proves (8). QED.

The infinite Dirichlet convolution by U_m and by its inverse therefore has a bounded critical root-norm cost, including for any nonnegative physical row measure. This is a genuine uniform kernel estimate. It is not an upper bound for the native source acted on by that kernel.

## 4. The remaining critical cost is exactly a single harmonic sum

Let A_F>=1 satisfy I_F(T):=#{nonzero integral ideals with norm<=T}<=A_F T for T>=1. This classical fixed-field ideal count is the only counting input here. Partial summation gives

    sum_(Nn<=R) 1/Nn <= A_F(1+log R), R>=1.               (12)

Let j_m^+,j_m^- be positive coefficient majorants of j_m and j_m^(-1) obtained from (2), (8) and, respectively,

    product_p (1+q^(m/2-1)x_p^m),
    product_p (1-q^(m/2-1)x_p^m)^(-1).

### Theorem 3

For T>=1, uniformly in m>=2 and all phases,

    sum_(Nn<=T) j_m^+(n)/sqrt(Nn),
    sum_(Nn<=T) j_m^-(n)/sqrt(Nn)
       <= K_F A_F [1+(log T)/m].                         (13)

**Proof.** The first of the two displayed products is supported on n=d^m with d squarefree, and the second on n=d^m with d arbitrary. Their coefficients have absolute size (Nd)^(m/2-1); at critical weight the mass is exactly 1/Nd. Convolve with u_m^+ or u_m^-. For each remaining factor h, the inner sum has Nd<=(T/Nh)^(1/m), so (12) bounds it by A_F[1+log T/m]. Sum the outer critical mass using (8). No coprimality between h and d is imposed. QED.

At m=6 this replaces #948's log(T)^(12[F:Q]) upper budget by O_F(1+log T). The sharper dependence is 1+log(T)/6; a numerical constant-cost claim for j itself would still be false.

For completeness, the logarithmic order cannot in general be removed. For unit-modulus a,b and m>=3, the coefficients at p^m satisfy

    |j_m(p^m)| >= q^(m/2-1)(1-q^(-m/2)),
    |j_m^(-1)(p^m)| >= q^(m/2-1)(1-q^(-m/2)).             (14)

The exact coefficients are q^(-1)a^m-bq^(m/2-1) and bq^(m/2-1)-q^(-1)(1-q^(-1))^(m-1)a^m. Restrict to ideals d^m with d squarefree. The product of the extra lower factors is at least product_p(1-q^(-3/2))>0, uniformly in m>=3. In F=Q with a fixed finite exclusion, the elementary squarefree count gives sum_(d<=R,(d,S)=1)mu(d)^2/d >= c_S(1+log R). Hence the two truncated absolute coefficient masses are bounded below by c_S[1+log T/m] already in this case. This is sufficient to disprove a constant budget uniform in scale. No lower operator norm after grouping equal ideal norms in an arbitrary field is being inferred.

One proof of the quoted rational squarefree count is mu(n)^2=sum_(d^2|n)mu(d): imposing the finite exclusion gives density product_(p in S)(1-1/p) product_(p notin S)(1-1/p^2)>0, with O_S(sqrt(R)) error (or an O_S(sqrt(R)log R) bound suffices). Partial summation supplies the logarithmic lower bound.

## 5. A direct Gaussian adapter: no compact-support substitution

Use the ACTUAL fixed Gaussian norm test

    w_c(y)=(1/(2sqrt(pi))) y^(-c) exp(-(log y)^2/4),
    c=5/6,
    integral_0^infinity w_c(y)y^s dy/y = exp((s-c)^2).      (15)

It is not compactly supported. Fix any finite nonnegative row measure w(u), of mass Z_w, and any rowwise phase profiles and common nonunit masks. Let A_u(X) and B_(m,u)(X) be the full ideal sums with coefficients mu_a,u and c_m,u against w_c(Nn/X). Define, for 1<=p<infinity,

    E_A,p(D)=sup_(0<X<=D) X^(-1/2)||A(X)||_Lp(w),
    E_B,p(D)=sup_(0<X<=D) X^(-1/2)||B_m(X)||_Lp(w).         (16)

The SAME row measure is held fixed at every shorter scale. These are suprema of norms, not norms of maxima.

### Theorem 4

There is C_(F,c) such that for every D>=2, every integer m>=2, every p>=1, and every permitted row profile,

    E_B,p(D) <= C_(F,c)[1+log D/m] E_A,p(D),
    E_A,p(D) <= C_(F,c)[1+log D/m] E_B,p(D).               (17)

The constant is independent of m,p,S, row mass, phases and masks. The same compact-test comparison follows from (13), with a support-dependent constant. No estimate available only along H=X^h has been promoted to the fixed-height premise in (16).

**Proof.** The coupled coefficients satisfy |c_m,u(n)|<=(Nn)^(1/2), uniformly in m; the unit coefficient is exactly one. Gaussian decay makes both ideal sums absolutely convergent. For every M>3/2, uniformly for 0<X<=1,

    |A_u(X)|+|B_(m,u)(X)| <= C_(M,F,c) X^M.               (18)

Indeed w_c(y)<=C_(M,c)y^(-M) for y>=1, and the ideal series at M-1/2 converges. The exact convolution identities B=j*A and A=j^(-1)*B hold for the Gaussian sums: use w_c(y)<=C_M y^(-M) globally for some M>3/2 and the absolute coefficient series to justify Fubini. Shared prime factors remain.

Split either convolution into Nn<=D^2 and Nn>D^2. For the first part, Minkowski and (13) give root-envelope cost at most K_F A_F[1+2log D/m]. For the tail, the argument X/Nn is at most one. Both j-majorants have uniformly bounded mass at weight one: by (8), their remaining powerful series costs at most zeta_F(m/2+1)<=zeta_F(2). Thus, using (18),

    X^(-1/2)||tail(X)||_p
      <= C_M Z_w^(1/p) X^(M-1/2)
                    sum_(Nn>D^2) j_m^(+/-)(n)/(Nn)^M
      <= C_M K_F zeta_F(2) Z_w^(1/p) D^(3/2-M).           (19)

Take M=3. This error can be absorbed uniformly into either original envelope, not merely appended without explanation. There exists a fixed X_0 in (0,1), depending only on F,c, such that for both sums

    |A_u(X_0)|, |B_(m,u)(X_0)| >= (1/2)w_c(1/X_0).        (20)

To see this, divide all nonunit-ideal terms by w_c(1/X_0). The absolute total is at most

    sum_(n != 1) (Nn)^(1/2-c-(log(1/X_0))/2)
                    exp(-(log Nn)^2/4),

which tends to zero as X_0 decreases to zero, uniformly in m and phases. Absolute ideal-series domination justifies the limit. Choose the total at most 1/2. Hence each envelope in (16) is at least a positive constant times Z_w^(1/p), unless Z_w=0, in which case everything is zero. Absorb (19) into (17). This proves both directions with constants independent of p and m. QED.

The Gaussian tail was neither discarded nor identified with a compact detector. The proof closes that specific interface left open in #948.

## 6. Exact identification with #949's signed detector

In the actual principal case of #949, let g be its quantitative spectral function multiplied by Z^(61/100), and let g_tilde be its signed sixth-power transform. Its initial Mellin identity is

    Mellin(g_tilde)(s)=exp((s-5/6)^2) H_tilde(s)/zeta_F^S(s).

By (1)--(3), on Re(s)>1,

    H_tilde(s)/zeta_F^S(s)=C_S product_p F_p(s),
    C_S=product_p(1-q^(-2)).                              (21)

Absolute convergence on Re(s)=2 and Gaussian inversion give EXACTLY

    g_tilde(Z)=C_S B_(6,1)(Z;w_(5/6)).                    (22)

The exponent Z^(61/100) has already been absorbed into g_tilde here. It must not be multiplied in a second time. This equality uses the source's actual Mellin identity and inverse-transform definition as pinned in #949. The Gaussian coefficient expansion and all subsequent comparison lemmas are proved here. No fresh Lean replay or reconstruction of the upstream theta theory is claimed.

A bound B_(6,1)(Z)<<_epsilon Z^(1/2+epsilon) would make its Mellin transform holomorphic on Re(s)>1/2 (flatness at zero follows from (18)). The nonvanishing numerator supplied by #949, or equivalently (2), (4) and the absolutely convergent powerful factor there, then excludes zeros of the target in that half-plane. This root bound is OPEN.

Theorem 4 shows that the coupled Gaussian all-epsilon bound and the native Gaussian all-epsilon bound are equivalent at this scalar level. It is an exact bridge, not a new estimate for either source.

## 7. What the second extraction does not do

Where b is a Hecke character, the explicit new factor is 1/L_F^S(ms-m/2+1,b); otherwise it is only its convergent Euler series. For Re(s)>1/2 its argument has real part >1, so this factor and its inverse are already controlled by absolute convergence. No finite-order assertion about an angular character is needed.

The other factor remains 1/L_F^S(s,a). U_m is nonzero, so it cannot cancel an off-critical zero of that target. The m=6 continuation to 3/7 therefore does NOT give zeta a 3/7 zero-free region, and varying m alone does not bootstrap RH. The unresolved arithmetic appears in the genuine two-channel prime-flow formula in COUPLED_PRIME_FLOW.md.
