# Connection to the newly arrived native collision PR #868

Date: 2026-09-12. **Proposed analytic extension. RH and the global signed-production estimate remain open.** This note was added after the main gamma packet was frozen. It reads #868 at commit `8ae3ea4855fd89882f4b5d782bbd72b721ebf47b`, specifically its complete `standalone/2026-09-12-native-gamma-collision/PROOF.md`. Its numerical collision certificate was not replayed here. The local collision is its result, not a new certificate from this packet.

The useful connection is precise: #868 supplies an actual mean-preserving native update and a local annihilation; the present packet supplies a global Jensen balance which does not require simple zeros or a uniform finite exceptional region. Below we extend that balance through the update's u=0 endpoint and show how complete step budgets telescope without accumulating a separate spectral-tail error at each step.

## 1. The exact native update

Use the uncompressed centered sequence only. Write

    a=(N+1)^2,  tau_N=2 sum_(j>N) j^-2,
    Y_(N,u)=X_N+tau_N-2u/a+(u/a)G,  0<=u<=1,

where G is Gamma(2,rate 1), independent of X_N. Thus Y_(N,0)=Y_N and Y_(N,1)=Y_(N+1). Let g_u be its density, and define h_u,F_u,mu_(2,u) by (2) of PROOF.md. The parameter is u here, not the anchor path's theta.

#868 proves a different coupling of these marginals with the martingale property. Its complete density equation for u>0 is

    q_u=partial_u g_u
       =(2/a)g_u'+(2/u)(k_u*g_u-g_u)
       =(2u/a^2)D_x^2(k_u*g_u),
    k_u(v)=(a/u)exp(-av/u)1_(v>0).                  (L1)

The moving lower endpoint is d_u=tau_N-2u/a. In particular

    D_N:=tau_(N+1)<=d_u,
    T_N=(1/2)log(pi/D_N),
    h_u(t)=0 for |t|>=T_N.                        (L2)

The notation D_N in this note is a positive support bound, not the weighted zero defect, which is always written Delta.

## 2. A whole-step chain rule, including u=0

Here is a direct endpoint repair which does not assume that #868's finite exceptional-zero radius stays bounded as u decreases to zero.

For N>=2 let g_0 denote the zero-extended density at u=0. It is C^2 with bounded first two derivatives. The same-G representation is legitimate for differentiating these marginals, even though that representation itself is not the martingale coupling. With V=(2-G)/a,

    g_u(x)=E g_0(x+uV),
    q_u(x)=E[V g_0'(x+uV)].                       (L3)

These are continuous pointwise parameter derivatives by boundedness of g_0' and E|V|<infinity. Since EV=0 and EV^2=2/a^2, q_0=0 and

    ||q_u||_infinity<=2u ||g_0''||_infinity/a^2.   (L4)

The fixed Gamma(4,rate 4) decomposition in Section 2 of PROOF.md also applies to g_0, followed by positive convolution and translation. Its physical Fisher integral is exactly

    int g(x)(3/x-4)^2 dx=8.

Conditional Cauchy--Schwarz for convolution therefore gives I(g_0):=int (g_0')^2/g_0<=8. Apply the same inequality to the mixture (L3), then integrate x over the whole line. Translation invariance gives, for every u in [0,1],

    int q_u(x)^2/g_u(x) dx
       <=EV^2 I(g_0)<=16/a^2.                    (L5)

Zero-density ratios are set to zero. Zero extension causes no boundary distribution, since the relevant density and its first derivatives vanish there. Every g_u is bounded above by one: retain the rate-one Gamma(2) factor, whose density has supremum 1/e, and convolve with the remaining probability law.

Define the actual reciprocal derivative on its positive support by

    v_u(t)=(h_u(t)/2)
       [q_u(pi e^(2t))/g_u(pi e^(2t))
        +q_u(pi e^(-2t))/g_u(pi e^(-2t))].        (L6)

The two absolute terms have equal integrals by reflection. Substitute x=pi e^(2t), use g_u<=1, and apply (L5) and Cauchy--Schwarz. For every R>=0,

    int e^(R|t|)|v_u(t)|dt
       <= e^(R T_N)/2 * (int q_u^2/g_u)^(1/2)
          *[int_(D_N)^(pi^2/D_N) dx/x^2]^(1/2)
       <=2 e^(R T_N)/(a sqrt(D_N)).              (L7)

This is uniform through u=0 for each fixed step. Its explicit N dependence is retained; it is not asserted to be a useful uniform spectral contraction bound.

The product regularization and compact-interval chain rule from Section 3.1 of PROOF.md now apply using the actual derivatives (L3) and the integrable majorant (L7). The support is already contained in the fixed interval [-T_N,T_N]. Although a fixed t can enter the support as u increases, the continuous product is zero at entry and the integrable bound gives the fundamental theorem across that entry. Thus h_u is absolutely continuous on the CLOSED parameter interval [0,1] in every displayed weighted L1 space, with derivative (L6). There is no endpoint atom at u=0, and no need to differentiate individual zeros there. Normalization gives

    dot F_u(z)=Z_u^-1 int v_u(t)[e^(izt)-F_u(z)]dt,
    dot mu_(2,u)=Z_u^-1 int v_u(t)[t^2-mu_(2,u)]dt. (L8)

Here Z_u has a positive minimum on the compact parameter interval, since g_u(pi)>0 throughout. Stronger common bounds appear in Section 3 below.

### A stronger O(u) derivative bound for N>=3

One can also pay the cancellation in the complete generator (L1). The first three native gamma factors admit a fixed Gamma(6,rate 9) anchor. The remaining head convolution is compound Poisson with positive Levy measure

    2[e^(-v)+e^(-4v)-2e^(-9v)]dv/v.

This follows directly by multiplying its Laplace transform by (1+s/9)^(-6). Let b be the Gamma(6,rate 9) density. Direct gamma integration gives

    b''/b=20/x^2-90/x+81,
    int (b'')^2/b dx=4374.                       (L9)

For clarity, after scaling x by 9 the last integral is
9^4[400/120-400/60+140/20-20/5+1]=(2/3)9^4.
Positive convolution, conditional Cauchy--Schwarz, and the increasing polynomial in b yield

    int (g_u'')^2/g_u<=4374,
    g_u(x-v)<=e^(9v)g_u(x), v>=0.

Apply Jensen to the exponential convolution in (L1), use the last ratio, and integrate x. Since a>=16 and 0<=u<=1,

    int q_u^2/g_u
       <=(4u^2/a^4)*4374*a/(a-9u).

Consequently the same calculation as (L7) gives the explicit improvement

    int e^(R|t|)|v_u(t)|dt
       <= e^(R T_N)u/(a^2 sqrt(D_N))
                         *sqrt(4374*a/(a-9u))
       <100 e^(R T_N)u/(a^2 sqrt(D_N)).          (L10)

Indeed 4374*16/7<10000. This proves an integrable, vanishing endpoint derivative in the reciprocal norm. It is a source-regularity statement; division by F in an unregularized zero-motion formula would destroy this argument. In particular it does not imply an O(N^-4) bound for the complete zero defect or its signed production.

## 3. A complete one-step Jensen identity

The common bounds of Sections 3 and 4 of PROOF.md hold along ALL these native interpolations. To verify their inputs, the martingale transition from u to 1 followed by the remaining native updates gives

    E exp(3Y_(N,u)/4)<=E exp(3X/4)<=1024.

The last inequality follows from the inherited density bound f(x)<=64x e^(-x), which requires no RH assumption. Equivalently the exponential-moment inequality follows directly by comparing the centered gamma logarithmic transforms. Every Y_(N,u) has the same fixed Gamma(4,rate 4) anchor, with nonnegative independent remainder of mean pi^2/3-1. Therefore the lower normalizer, double-exponential envelope, zero-free origin disk, entire growth bound, and complete radial tail all carry over with the identical constants.

For clarity write

    T(R)=14/R^2+[log(2R+4)+1]/(2R), R>=1,
    J_u(r)=(1/(2pi))int_0^(2pi)log|F_u(re^(i phi))|dphi.

Thus int_R^infinity J_u(r)dr/r^3 is between zero and T(R), uniformly in N,u. Define V_(N,epsilon,R)(u) by equation (27) of PROOF.md with theta replaced by u and with the actual derivatives (L8). This includes the angular-zero quadratic subtraction and the variance subtraction; neither should be omitted.

The proof of (30), now justified on the whole interval by (L7), gives

    B_N(R):=lim_(epsilon->0+)int_0^1 V_(N,epsilon,R)(u)du
      =(1/2)int_0^R[J_(N+1)(r)-J_N(r)]dr/r^3
        -(mu_(2,N+1)-mu_(2,N))/8.                (L11)

Let E_N(R)=int_R^infinity J_N(r)dr/r^3. Then EXACTLY

    Delta(F_(N+1))-Delta(F_N)
       =B_N(R)+(E_(N+1)(R)-E_N(R))/2,
    |Delta(F_(N+1))-Delta(F_N)-B_N(R)|<=T(R)/2.  (L12)

Sending R to infinity defines the complete signed step budget. This includes possible higher collisions, all finite observation-boundary crossings, and the u=0 change of endpoint power. It does not use #868's exceptional-region theorem at that endpoint. Sequential limits epsilon first, R second are retained.

## 4. Cumulative budgets: the spectral error telescopes too

Fix a starting stage M>=2. Let A_M(R) be the finite-radius signed budget of our Bessel-anchor path to the uncompressed F_M (take r=0 in PROOF.md). For integers K>M, put

    C_(M,K)(R)=A_M(R)+sum_(N=M)^(K-1) B_N(R).     (L13)

All terms use the SAME spectral radius R. The endpoint Jensen expressions and variance terms telescope. If E_anchor(R) denotes the anchor's radial Jensen tail, the exact remainder is

    Delta(F_K)-C_(M,K)(R)
       =[E_K(R)-E_anchor(R)]/2,
    |Delta(F_K)-C_(M,K)(R)|<=T(R)/2.              (L14)

There is no factor K-M in this error. Bounding every step separately would lose this cancellation and create a spurious accumulated spectral-tail cost. This is an analytic telescoping identity, not a claim that separate numerical quadrature errors cancel; any future computation must still pay its actual numerical errors.

Together with the inherited convergence Delta(F_K)->Delta(Phi), the precise cumulative closing target is

    C_(M,K_j)(R_j)->0
    for some K_j->infinity and R_j->infinity.      (OPEN-GJV-NATIVE)

It suffices to establish the target on a sparse cofinal sequence of stages. The target is still equivalent to the unresolved vanishing-defect problem, now expressed in complete source-defined signed budgets anchored at defect zero. It is not a consequence of (L7), (L10), or a locally favorable collision. A possible genuinely stronger estimate would be a block contraction

    Delta(F_(K_(j+1)))
       <=(1-eta_j)Delta(F_(K_j))+eta_j epsilon_j,
    0<eta_j<=1, sum eta_j=infinity, epsilon_j->0,

proved from the whole block's signed budget. The same elementary iteration as #868's single-step proposal would then close. No such block estimate has been proved here.

## 5. What the new collision supplies, and what it cannot pay

#868's inherited proposed certificate locates a nondegenerate real double zero near x=31.1001854446, u=0.3237882584 in the native N=5 to 6 step. It also certifies a tiny complete two-zero continuation tube around that event, with positive squared splitting coefficient

    0.33402067<kappa<0.33403612.

We did not replay that certificate. Its local factorization gives the quartet contribution

    Delta_fold(u)=(-D(u))_+/(c(u)^2-D(u))^2,
    D(u*)=0, D'(u*)=kappa, c(u*)=x*.

Immediately before this death its defect decreases with limiting slope -kappa/x*^4; immediately afterwards its contribution is zero. The global identity (L11) already includes this continuous, kinked contribution. No extra jump or multiplicity payment is added to the Jensen budget.

The tube is not a whole-step census and does not establish lineage from the separate N=5 disk imported in our main proof. Other quartets may be born or drift adversely, including at parameters outside the tube. The useful next result is therefore a complete ONE-step or sparse-block signed budget, with the common-radius remainder (L14), followed by a non-summable contraction or comparable global estimate. A positive martingale generator for convex physical tests alone does not supply the needed oscillatory Fourier sign.

No new numerical collision result, native Jensen evaluation, certificate replay, or RH proof is asserted in this appendix. Its new contributions are the whole-step endpoint regularity estimates (L5)--(L10), the collision-safe native step balance, and the cumulative spectral-tail cancellation (L14).
