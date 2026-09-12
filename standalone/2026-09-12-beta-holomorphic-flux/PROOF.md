# BHF26: a two-tail analytic homotopy and a complete collision balance

Date: 2026-09-12. Status: **PROPOSED component proofs; independent mathematical review required. NOT an RH proof.**

Scope: the exact beta/uniform fixed-point family of PR #876, not a convex mixture of endpoint transforms and not the discrete family of #870/#874. We establish a two-tail contraction, uniform complex-parameter continuation, all-order source responses, and finite-height absolute continuity through arbitrary multiplicities. An explicitly regularized source-only balance retains the whole height tail. Its required upper sign is NOT established.

The fixed-point source and its positive first response originate in #876. The regularized Jensen strategy also occurs for a different gamma path in #869. Banach contraction, beta integration, analytic implicit functions, Puiseux parametrization, and the Riesz/Jensen formula are classical; no priority claim is made for them. The proposed addition is the quantitative weighted-space construction and its application to this particular homotopy. Source freezes and reading boundaries are in SOURCES.md.

## 1. The unchanged source and the new norm

Let B have Beta(5/2,5/2) law, W=U^(-2) with U uniform on [1,2], and

    mu_theta = (1-theta) Law(B) + theta Law(W),  0<=theta<=1.
    A_theta f(t) = integral f(ct) mu_theta(dc),
    T_theta L = A_theta(L^2).

A single independent scale multiplies BOTH independent children. Define A_D=A_W-A_B. For complex zeta these formulas use the corresponding signed complex combination, not a probability measure.

Put b=2/5, x=bt, and

    L_G(t)=(1+x)^(-5/2),
    w(t)=x^3/(1+x)^5,
    ||h||_w=sup_(t>0) |h(t)|/w(t).                         (1)

The Banach space E consists of h=wq, q in C_b([0,infinity)); the quotient at zero is its continuous limit. This controls a cubic cancellation at zero AND O(t^-2) decay at infinity. It is different from the earlier cubic norm, which by itself permits growth at infinity.

Let C be the closed subset of L_G+E consisting of real functions 0<=L<=L_G. In particular every member has the same first two Taylor coefficients as L_G. The moment values of the scale are

    a_j(theta)=(1-theta)(5/2)_j/(5)_j
                 +theta(1-2^(1-2j))/(2j-1),  j>=1,
    a_1=1/2, a_2=7/24, a_3=(30+theta)/160.              (2)

Here (a)_j is rising factorial. The beta-gamma identity gives T_B L_G=L_G. The third-order comparison B <=_3 W gives T_W L_G<=L_G, so T_theta maps C into C.

For clarity, the comparison has an elementary proof, as in #876: the densities b(c)=128[c(1-c)]^(3/2)/(3pi) and w_C(c)=1/(2c^(3/2)) on [1/4,1] have matching moments of orders 0,1,2. Their difference has exactly three sign changes, in the order -, +, -, +. Quadratic interpolation at the changes proves E f(B)<=E f(W) for f''' >=0. Applying this to minus a Laplace transform proves the displayed inequality. Its Peano kernel kappa is nonnegative and has integral 1/960. These are source-law comparisons, not statements about complex zeros.

## 2. BHF1: a global two-tail contraction with explicit constants

For every L, Ltilde in C and theta in [0,1],

    ||T_theta L - T_theta Ltilde||_w
                          <= (3/5)||L-Ltilde||_w.      (3)

The same bound holds for K_theta h=2 A_theta(L_theta h), where L_theta is the fixed point. In particular ||(I-K_theta)^(-1)||<=5/2 on E.

### Beta part

Set v(t)=x^3/(1+x)^(11/2). Direct beta integration gives

    2 A_B(L_G v)=(3/8)v.

Since w/v=(1+x)^(1/2) is increasing and B<=1, positivity gives

    2 A_B(L_G w)<=(3/8)w.                             (4)

This is a gamma-weighted eigenfunction calculation, not a spectral realization of xi zeros.

### Uniform-scale part, with an exact all-t bound

For fixed c and x>=0,

    L_G(ct) w(ct)/w(t)=c^3(1+x)^5/(1+cx)^(15/2).

If c>=2/3 its maximum in x is c^3. For c<2/3 the maximum is

    [32/(2187 sqrt(3))] c^-2 (1-c)^(-5/2).

Integrating this pointwise maximum against twice the W density gives

    2 A_W(L_G w)/w
      <= q_W := 41642/59049 - (4576/98415)sqrt(6)
       < 876314/1476225 < 3/5.                        (5)

The first upper bound is not claimed sharp. To check the integral without numerical quadrature, use y=sqrt((1-c)/c) and

    P(y)=-1/(3y^3)-4/y+6y+(4/3)y^3+y^5/5.

The part c in [1/4,2/3] is proportional to 2[P(sqrt(3))-P(1/sqrt(2))]; the remaining part is (2/5)[1-(2/3)^(5/2)]. The rational inequality in (5) uses sqrt(6)>12/5. The complete continuum bound, rather than sampled x values, is what supplies (3).

Indeed |L^2-Ltilde^2|<=(L+Ltilde)|L-Ltilde|<=2 L_G |L-Ltilde|. Equations (4),(5) prove (3).

Banach contraction on C gives a unique fixed point and convergence from L_G. The iterates are Laplace transforms of positive branching laws. Their limit is a Laplace transform, since convergence is pointwise and the limit is continuous and equal to one at zero. The first two moments are 1 and 7/5. This independently realizes the same fixed law X_theta as #876. Higher integer moments follow from the positive recurrence

    m_j = a_j/(1-2a_j) sum_(i=1)^(j-1) binom(j,i)m_i m_(j-i).

Uniform bounds follow by induction, first for the iterates and then by uniform integrability using the next moment. In particular

    m_3(theta)=21(30+theta)/[5(50-theta)],
    E(X_theta+X_theta')^3 <= 96/7.                    (6)

No assumption about zeros enters these constructions.

### Forcing and bilinear bounds

The following bounds will also be needed:

    ||A_D(L_theta^2)||_w <= 8,
    ||2 A_D(L_theta h)||_w <= (39/40)||h||_w,
    ||A_B(h k)||_w <=15||h||_w||k||_w,
    ||A_W(h k)||_w <= 1||h||_w||k||_w.                (7)

For the first bound the Peano identity and (6) give
0<=-A_D(L_theta^2)<=t^3/70. For x<=1 its ratio to w is at most 50/7. For x>=1 use -A_D(L_theta^2)<=A_B(L_theta^2)<=L_G; its ratio to w is at most 4sqrt(2)<6. The second bound is (4),(5) and the triangle inequality.

For the beta quadratic bound, when x<=1, A_B(w^2)/w<=32 E B^6=143/64. When x>=1, dropping (1-c)^(3/2) in the beta density and extending a positive integral to infinity gives

    A_B(w^2) <= x^(-5/2) B(17/2,3/2)/B(5/2,5/2)
               = (715/1536)x^(-5/2).

After division by w, the maximum for x>=1 is 715/48<15. For W, w(ct)/w(t)<=c^-2<=16 and max w=108/3125. Thus A_W(w^2)/w<=1728/3125<1. Polarization is not needed: |hk|<=||h||||k||w^2 proves the bilinear statements directly.

Subtracting two real fixed-point equations and using (3),(7) proves the useful global estimate

    ||L_beta-L_alpha||_w <=20|beta-alpha|.             (8)

In particular iteration from L_G has complete error at most 20(3/5)^n in this norm, uniformly in theta. This is not asserted to be the optimal rate, or better at large spectral heights than earlier positive-law Mellin bounds.

## 3. BHF2: uniform holomorphic continuation in the source parameter

Set

    delta=1/4096,   r=1/128,
    Omega={zeta in C: dist(zeta,[0,1])<delta}.          (9)

The real path L_theta extends to an E-valued holomorphic path L_zeta on Omega. For every a in [0,1] and |zeta-a|<delta,

    ||L_zeta-L_a||_w <= r.                           (10)

Complex parameters have no positive-law interpretation.

**Proof.** On the closed ball ||h||<=r consider

    F_zeta(h)=T_zeta(L_a+h)-L_a.

With d=|zeta-a|, (7) bounds this by

    8d + (3/5+39d/40)r + (15+16d)r^2 < r.            (11)

The Lipschitz constant in h is at most

    3/5+39delta/40+2(15+16delta)r < 7/8.              (12)

These are strict rational inequalities checked by the supplied script. The map is a bounded polynomial in h and zeta. Its Picard iterations converge uniformly, and hence holomorphically in zeta, to the fixed point. For real beta in this disk, (8) gives ||L_beta-L_a||<=20delta<r, so the new fixed point agrees with the physical one. Intersecting disks with real centers contain a real interval; the identity theorem glues the extensions. This proves (9),(10).

Write L_(a+z)=L_a+sum_(k>=1) ell_k z^k. Then

    ||ell_k||_w <= r delta^-k.

For |z|<=u delta, 0<=u<1, the remainder after k=K is bounded by

    r u^(K+1)/(1-u).                                (13)

All coefficients are source-defined by an invertible equation, not a fitted jet:

    (I-K_a)ell_1=A_D(L_a^2),
    (I-K_a)ell_k=A_a sum_(i=1)^(k-1)ell_i ell_(k-i)
       +2 A_D(L_a ell_(k-1))
       +A_D sum_(i=1)^(k-2)ell_i ell_(k-1-i), k>=2.  (14)

Empty sums are zero. Positivity of K_a and negativity of the first forcing give ell_1<=0 on the positive Laplace axis. Equation (14) does NOT imply a corresponding complex-zero sign.

The first response also has a complete strong-norm truncation:

    ||ell_1-sum_(j=0)^J K_a^j A_D(L_a^2)||_w
                                    <=20(3/5)^(J+1). (15)

This controls both ends of a Mellin integral; it is not just a bound on the total mass of a positive response measure.

## 4. BHF3: joint Mellin analyticity and complete response errors

Let c=pi/6 and p=s/2. For real theta use the original source

    M_theta(s)=E[(c(X_theta+X_theta'))^p],
    N_theta(s)=M_theta(s)+M_theta(1-s),
    H_theta(s)=N_theta(s)/[2(1+M_theta(1))].            (16)

For complex zeta, define the Mellin continuation by

    M_zeta(s)=c^p/Gamma(-p) * {
      integral_0^1 t^(-p-1)[L_zeta(t)^2-1+2t-(12/5)t^2]dt
      + integral_1^infinity t^(-p-1)L_zeta(t)^2 dt
      -1/p+2/(p-1)-(12/5)/(p-2)}.                    (17)

The values at p=0,1,2 are removable. This is jointly holomorphic for zeta in Omega and -4<Re p<3. At zero the integrand in square brackets is O(t^3); at infinity L_zeta=O(t^-2), uniformly in parameter. The required domination also applies on compact complex subdomains. For real parameters (17) agrees with the actual moments first by Laplace inversion, then by analytic continuation.

If a is real and h=L_zeta-L_a, then, for A=Re p in (-4,3),

    |M_zeta(s)-M_a(s)| <= (pi/15)^A/|Gamma(-p)| *
       [2||h||_w B(3-A,9/2+A)+||h||_w^2 B(6-A,4+A)]. (18)

Both beta integrals cover the entire positive real axis. There is no sampled spectral boundary or truncated small-value contribution. At p=0,1,2 the right side and the difference are zero, with removable interpretation.

At s=1, the right side of (18) is less than r/2=1/256: use (pi/15)^(1/2)/|Gamma(-1/2)|=1/(2sqrt(15))<1/6 and B(5/2,5), B(11/2,9/2)<=1. Thus 1+M_zeta(1) never vanishes on Omega. The normalized H is jointly holomorphic on

    Omega x {s: -5<Re s<6},                          (19)

and satisfies H_zeta(0)=H_zeta(1)=1/2 and H_zeta(1-s)=H_zeta(s). Conjugation holds jointly in parameter and argument. We assert neither entire continuation in s for intermediate parameters nor zero confinement from joint analyticity.

From (15), truncating the first response after J has Mellin error at most

    40(3/5)^(J+1) (pi/15)^A
                B(3-A,9/2+A)/|Gamma(-p)|.           (20)

It follows by differentiating (17) and bounding the complete integral of 2L_a times the response remainder. The reciprocal gamma factor can grow at large |Im p|. This absolute bound is not a relative error bound near zeros and does not solve the high-height sign problem.

## 5. Endpoints and a uniform whole-strip zero tail

The endpoints have not been redesigned. The gamma endpoint gives

    M_0(s)=(pi/15)^(s/2) Gamma(5+s/2)/Gamma(5).

The Brownian endpoint is L_1(t)=sqrt(6t)/sinh(sqrt(6t)). Its fixed equation follows by integrating csch^2 after u substitution. It has the required first two moments and belongs to C. One way to verify L_1<=L_G is Jensen applied to the probability measure sum alpha_j delta_alpha_j, alpha_j=6/(pi^2 j^2): its mean is 2/5 and the logarithmic derivative of L_1 is its Stieltjes transform. Integration of 1/(1+2t/5) gives the claimed comparison. Uniqueness in C identifies the endpoint.

The classical BPY theta/Mellin identity, with this normalization, gives

    M_1(s)=2xi(s),      H_1(s)=xi(s).                 (21)

This is an imported classical source identity; it is not proved by the finite checker.

For completeness the gamma endpoint is zero-safe on the whole critical strip. The Binet bound

    |psi(z)-log z+1/(2z)|<=1/[12(Re z)^2], Re z>0,

shows that M_0 has positive real part for 0<=Re s<=1, |Im s|<=4: its phase lies between -31/150 and 18/35+1/150. Above height four,

    partial_sigma log|M_0(s)/M_0(1-s)|
      >=log(pi/3)+(1/2)log(1+4/25)-1/10-1/300
       >77/7500>0.

The ratio has modulus one on the central line, and strictly different modulus off it. The reflected sum therefore has no off-central zeros. On the line its phase increases strictly, so the high zeros are simple. These are the same elementary gamma estimates as #876, included to retain the starting zero condition without assuming RH.

For every real theta, L_theta<=L_G bounds inverse moments of the pair S=X_theta+X_theta' by those of Gamma(5, rate 5/2). In particular E S^-1<=5/8. Together with E S=2 and E S^2=24/5 this gives, as in #876,

    |H_theta(s)|<4 on -1/2<=Re s<=3/2,
    H_theta(1/2)>1/20.                               (22)

For the lower bound, P(S>=1)>=5/24, so E(cS)^(1/4)>1/6; also 1+E sqrt(cS)<3. For the upper bound use V^a<=1+V+V^-1 on -1/4<=a<=3/4, E V=pi/3<4/3 and E V^-1<5/4.

The conformal map v=tan(pi(s-1/2)/4) and Jensen's formula imply, with all analytic multiplicities included,

    sum_(H_theta(rho)=0, 0<=Re rho<=1)
                   mult(rho) exp(-pi|Im rho|/2)<20.  (23)

Indeed sum log(1/|v_rho|)<log(80)<5, and on the smaller strip -log|v_rho| >= (1/4)exp(-pi|Im rho|/2). No census or simplicity of intermediate zeros is needed.

## 6. BHF4: all finite-height collisions, including persistent multiplicities

Use a slightly smoother diagnostic than #876; this does not silently change its definition. Set d=sigma-1/2 and

    h(sigma)=d^2(1/4-d^2)^2 for 0<=sigma<=1, else 0,
    g(t)=sech(pi t),
    D(theta)=sum_(H_theta(rho)=0, 0<Re rho<1) mult(rho)h(Re rho)g(Im rho).
                                                               (24)

The function h is C^1 with bounded weak second derivative, including across both vertical edges. It is positive exactly off the central line in the open critical strip and max h=1/432. Equation (23) gives

    0<=D(theta)-D_T(theta)<= (5/54)exp(-pi T/2),       (25)

where D_T uses the additional cutoff eta_T(t): one for |t|<=T, zero for |t|>=T+1, and 1-3u^2+2u^3 when u=|t|-T is in [0,1]. Take T>=1. The bound is uniform over the whole real parameter interval.

For each fixed T, D_T is absolutely continuous on [0,1], even through higher collisions and persistent multiple roots.

**Proof of the collision assertion.** Joint holomorphy (19) lets a small zero cluster be represented by a monic polynomial with holomorphic parameter coefficients, using contour power sums and Newton identities. Remove repeated factors over the field of meromorphic germs. Its square-free discriminant is not identically zero, so on a sufficiently small punctured parameter disk the roots continue analytically with finite permutation monodromy. A substitution theta-theta_0=v^q, q<=m!, removes that permutation for a cluster of degree m. The roots are bounded, so the singularity at v=0 is removable. They therefore have convergent Puiseux expansions. Repeated factors retain their full analytic multiplicities.

Along either real side every root branch is absolutely continuous: each nonconstant leading term has exponent at least 1/q, and its derivative is locally integrable. A finite cover of the compact parameter/zero region and a C^1 compactly supported weight now proves the assertion. Zeros crossing the support boundary contribute continuously because the weight and its first derivatives vanish there. There is no assumption that all collisions are nondegenerate folds.

At regular parameters a root with locally constant multiplicity m has velocity

    v_rho= - [partial_theta partial_s^(m-1) H(theta,rho)]
                         /[partial_s^m H(theta,rho)]. (26)

For m=1 this is the usual -H_theta/H_s. For persistent m>1, (26), not division by H_s, is required. The a.e. derivative of D_T is the full multiplicity-weighted sum of grad[h g eta_T] dot (Re v_rho, Im v_rho). The integrable singularities at isolated collisions do not create an omitted jump term.

This does not assert absolute integrability of the UNTRUNCATED infinite velocity sum. The correct global passage uses (25), or the regularized identity below.

A synthetic control explains why bounded velocities cannot be assumed: for P_u(z)=(z^2-4)^3-u, put u=v^3 and z=2+vw. Then v^-3 P_(v^3)(2+vw) tends to 64w^3-1. Two roots have imaginary part asymptotic to +/-sqrt(3)u^(1/3)/8; their squared-displacement cost is of order u^(2/3). Its derivative is integrable but unbounded. This is a polynomial control, NOT an observed collision of the native source.

## 7. BHF5: a source-only balance that does not lose collisions or infinity

Let W_T(s)=h(Re s)g(Im s)eta_T(Im s). Let Lap denote the two-dimensional real Laplacian. All area integrals below are over S={s:-1/2<Re s<3/2}; their weights have compact support inside this holomorphy strip. The Riesz identity for a nonzero holomorphic function gives

    D_T(theta)=(1/(2pi)) integral_S log|H_theta(s)| Lap W_T(s) dA(s).
                                                               (27)

The identity applies by smooth approximation to our compactly supported C^1 weight with bounded weak second derivatives. There are no artificial vertical-edge terms. All logarithmic zero singularities are locally integrable. Since integral Lap W_T=0, the positive normalization of H can be removed: use N_theta from (16) instead.

For epsilon>0 define the completely specified real integral

    I_(T,epsilon)=(1/(2pi)) integral_0^1 integral_S
       Re[(partial_theta N_theta) conjugate(N_theta)]
       /(|N_theta|^2+epsilon^2) * Lap W_T dA dtheta.  (28)

For fixed epsilon the inner expression is the theta derivative of
(1/2)log(|N_theta|^2+epsilon^2). Hence ordinary Fubini and the fundamental theorem give the exact endpoint difference. Taking epsilon down to zero at the two endpoints, in local L1, proves

    lim_(epsilon down to 0) I_(T,epsilon)
                    =D_T(1)-D_T(0)=D_T(1)>=0.       (29)

The gamma endpoint makes D_T(0)=0 independently of RH. The full conclusion is

    D(1)=lim_(T to infinity) lim_(epsilon down to 0) I_(T,epsilon),
    0<=D(1)-lim_epsilon I_(T,epsilon)
                           <=(5/54)exp(-pi T/2).     (30)

All intermediate births, annihilations, higher collisions, vertical crossings and the complete infinite height tail are retained. We neither interchange the two limits nor assert convergence of a formally differentiated infinite root sum.

The numerator in (28) is defined directly from the branching source. The positive response of #876 gives, p=s/2 and q=(1-s)/2,

    partial_theta N_theta(s)=2 chi_theta [
      c^p p(p-1)(p-2) E R_theta^(p-3)
      +c^q q(q-1)(q-2) E R_theta^(q-3)],
    chi_theta=56/(50-theta)^2.                        (31)

Here R_theta is the positive response variable explicitly constructed in #876, not an adjustable measure. Alternatively (14),(15),(20) define and bound the response directly in the new weighted space, without assuming a tail bound from mass alone. No zeta zero is an input to (28).

## 8. The attempted finish and the exact remaining inequality

Classical zero location and (21),(24) imply

    RH  <=>  D(1)=0
        <=> lim_(T to infinity) lim_(epsilon down to 0) I_(T,epsilon)=0.
                                                               (32)

Thus a source-specific UPPER bound on the last expression by zero would complete this route. It is necessary and sufficient; it does not require every intermediate source to be zero-safe, monotone inward motion, or simple zeros of xi.

**That upper bound is not proved here.** The work above closes a regularity/collision-accounting gap in the proposed homotopy route, not its arithmetic/complex sign gap. A proof of (32)'s upper bound would still be a major additional mathematical result.

I tested the tempting way to extract this sign by positivity alone. It fails already at the level of the explicit Green kernel, before any numerical source experiment. In the interior of the height cutoff,

    Lap(hg)=g[h''+pi^2 h(1-2 sech^2(pi t))].           (33)

At d=0 this is g/8>0. At d^2=1/8 one has h''=-5/32 and h=1/512, so pi^2<10 gives Lap(hg)<-35g/256<0. The kernel genuinely changes sign. Moreover the positive-law response (31) is oscillatory for complex p and q. Absolute values or separate positive bounds discard precisely the cancellation needed in (28). No favorable sign for the complete native integral was obtained.

This kernel sign change is NOT a refutation of the balance approach and NOT evidence against RH. It identifies the unresolved operation: prove the integrated source-specific cancellation, rather than replace it by phase monotonicity or positivity of an unrelated interpolating class.

## 9. Computation and review boundary

The standard-library script verifies exact rational/radical algebra used in the continuum norm bound, both nonlinear constants, the strict complex-ball inequalities, the source moment recurrence at specified rational parameters through order 12, its independent gamma and Brownian endpoint series, the weight identities, and the synthetic multiple-root velocity control. It does not evaluate I_(T,epsilon), a native collision, any xi zero, or an unbounded spectral region. Successful finite algebra is not a machine proof of the analytic theorems.

Independent review should first check: the all-x norm bound (5); the bilinear estimate and ball invariance; the Mellin domain and subtraction signs; the local Puiseux argument with persistent multiplicity; and the order of limits in (30). The unresolved closing claim is ONLY the upper sign in (32). Nothing has been merged or promoted by this manuscript.
