# A native signed Jensen balance with a real-zero initial condition

Date: 2026-09-12. **PROPOSED component proofs, not an RH proof.** The exact cofinal signed-production estimate in Section 8 remains open. No source or predecessor status is changed.

This is an attempt to supply the missing zero-sensitive step of #862/#865, rather than another absolute approximation bound. Its outcome is an exact balance, a source-specific native tangent, and a quantitative refutation of one possible sign shortcut. All quantities below are defined without unknown zero locations. Classical analytic facts and the separate numerical imports are listed in SOURCES.json.

## 1. Source, defect, and the baseline problem

Let independent G_n have gamma shape two and rate one, and put

    X_N=sum_(n<=N) G_n/n^2,       X=sum_(n>=1) G_n/n^2.

Use exactly the #865 Radau rule on

    sigma_N=sum_(n>N)(2/n^2) delta_(1/n^2).

For N>=2 and r>=0 it supplies a positive drift d, scales x_j in (0,b), shapes alpha_j>0, where b=(N+1)^(-2), with

    Y_(N,r)=X_N+d+sum_(j<=r) Gamma(alpha_j,scale x_j),
    d+sum alpha_j x_j=tau_N=2 sum_(n>N)n^-2.             (1)

For r=0, d=tau_N. For the closing diagonal take r=floor(N/4). The construction, exact cumulant matching, and exponential approximation are imported as proposed component results at the frozen #865 source. They are not newly certified here.

For any density u in this packet define

    h_u(t)=sqrt(u(pi e^(2t))u(pi e^(-2t))),
    Z_u=int_R h_u(t)dt,
    F_u(z)=Z_u^-1 int_R h_u(t)e^(izt)dt,
    mu_2(u)=Z_u^-1 int_R t^2 h_u(t)dt.                  (2)

All square roots are the positive real roots. The normalized infinite target is Phi(z)=Xi(z)/Xi(0), with Xi(z)=xi(1/2+iz) and the entire xi completion. The classical BPY/Jacobi identification, in this scaling, is

    E (X/pi)^(s/2)=2xi(s),
    f(pi^2/x)=(x/pi)^(5/2)f(x),                         (3)

where f is the density of X. These identities use no zero-location assumption.

For a real even normalized entire function in this class, define

    Delta(F)=(1/4) sum_(F(rho)=0) mult(rho)(Im rho)^2/|rho|^4.
                                                               (4)

All zeros and multiplicities are included. Imaginary-axis zeros are absent because F(iy) is a strictly positive cosh integral. Equivalently (4) sums b^2/(a^2+b^2)^2 once per first-quadrant nonreal quartet, with its multiplicity. Real zeros contribute zero. The common growth bounds below make the sum convergent, including intermediate path parameters.

#862/#865 prove that Delta(F_(N,floor(N/4))) tends to Delta(Phi), and that its vanishing is equivalent to RH. A path starting at Phi can only give

    Delta(F_(N,r))-Delta(Phi)=integrated variation.

Showing this difference tends to zero is already known and does not determine the unknown initial constant. We therefore construct a path starting at a source whose defect is zero independently of RH.

## 2. An explicit positive convolution path from a Bessel anchor

Let A have Gamma(4,rate 4) law, density

    g(x)=(256/6)x^3 e^(-4x) 1_(x>0).

Introduce the positive finite measure

    nu_B(dv)=2(e^(-v)-e^(-4v))dv/v,  v>0,
    Lambda=nu_B((0,infinity))=2log4.                    (5)

Its first moment is 3/2. Let C_theta be a compound-Poisson variable with Levy measure theta*nu_B. Independently let V_theta contain drift theta*d, gamma components with shapes 2theta at scales n^-2 for 3<=n<=N, and gamma components with shapes theta*alpha_j at scales x_j. Zero shapes mean deterministic zero. Set

    Y_theta=A+C_theta+V_theta,       0<=theta<=1.        (6)

This is a positive convolution path with a fixed gamma factor, not an interpolation of desired zero data. Frullani's integral, obtained by integrating the difference of two exponentials, gives

    E e^(-s C_theta)=[(1+s/4)/(1+s)]^(2theta),  Re s>-1.

Consequently Y_1 has exactly the law (1): the two initial head factors satisfy

    (1+s/4)^(-4)[(1+s/4)/(1+s)]^2
              =(1+s)^(-2)(1+s/4)^(-2).               (7)

Equivalently, at an intermediate theta the slow head is Gamma(2theta,rate1) plus Gamma(4-2theta,rate4). The compound-Poisson version (6) is the useful one for parameter estimates.

Let u_theta,h_theta,Z_theta,F_theta,mu_(2,theta) denote (2). At theta=0 the reciprocal kernel of the pure gamma density is a positive constant times exp[-4pi cosh(2t)]. Thus

    F_0(z)=K_(iz/2)(4pi)/K_0(4pi).                    (8)

This anchor has only real zeros. Here is the standard Sturm argument at the required normalization. If K_(iz/2)(4pi)=0, the nontrivial decaying function w(t)=K_(iz/2)(4pi e^t) on t>=0 satisfies

    -w''+(4pi)^2 e^(2t)w=(z^2/4)w,   w(0)=0.

The integral representation for K and its derivatives gives the required decay at infinity. Integration against conjugate(w) gives a strictly positive real left-hand energy, so z^2/4 is positive real. Therefore z is real. The zero function is excluded by K's large-positive-argument asymptotic, or directly its defining integral. These are the classical modified-Bessel equation and Sturm energy argument, not a statement about xi. In particular

    Delta(F_0)=0.                                      (9)

## 3. Whole-path envelopes and a signed source derivative

The endpoint law has the #865 bound u_1(x)<=64x e^(-x). Since Y_theta is the anchor plus an increasing subordinator, for 0<=theta<=1,

    E exp(3Y_theta/4)<=E exp(3Y_1/4)<=1024.             (10)

Removing the anchor cannot increase this exponential moment. Convolution and
sup_(x>0) e^(x/2)g(x)<32 therefore give

    u_theta(x)<=2^15 e^(-x/2), x>=0.                  (11)

The supremum follows by maximizing x^3e^(-7x/2) at 6/7; even dropping its exponential at that point leaves (256/6)(6/7)^3<32.

The non-anchor mean is at most pi^2/3-1<23/10. Hence Markov gives probability greater than 1/10 that it is at most 13/5. On 3<=x<=4, the remaining anchor argument then lies in [2/5,4]. Direct endpoint checks and unimodality give g>2^-14 on that interval; at 4 use 3^17<2^27. Thus

    u_theta(x)>1/(10*2^14), 3<=x<=4,
    Z_theta>2^-23,
    h_theta(t)/Z_theta<=2^38 exp[-(3/2)cosh(2t)].       (12)

For the normalizer use |t|<=1/100, where both pi e^(+-2t) lie in [3,4]. All these bounds hold uniformly in N,r,theta.

The fast Levy measure is

    nu_f(dv)=[2 sum_(n=3)^N e^(-n^2v)
                  +sum_j alpha_j e^(-v/x_j)]dv/v.    (13)

Its scales are at most 1/9. Its first moment together with the drift is

    d+int v nu_f(dv)=pi^2/3-5/2<4/5.                 (14)

Extending densities by zero, the exact parameter derivative is

    q_theta(x)=partial_theta u_theta(x)
       =-d u_theta'(x)
         +int_0^infinity [u_theta(x-v)-u_theta(x)]
                                      (nu_B+nu_f)(dv).  (15)

The small-jump subtraction in (15) is essential. The first moment of each Levy measure is finite, and the head g is smooth, so the integral converges in the usual weighted L1 generator sense. One direct proof first truncates the jumps below epsilon, differentiates the finite compound-Poisson expansion, and lets epsilon decrease to zero. The difference of translates is bounded by v times the weighted norm of the first derivative. Exponential moments control the large jumps. This proves (15), rather than assigning a sign to a high-order differential operator.

### 3.1 Parameter regularity through the reciprocal square root

The following estimates justify that the path is absolutely continuous in every weighted h norm needed below; they also address theta=0.

For R>=0 set

    W_R(x)=[2^(15/2)/(2x)]
        exp[(R/2)|log(x/pi)|-pi^2/(4x)],
    C_R=sup_(x>0) W_R(x)e^(-x/4)<infinity.             (16)

This is a finite explicitly specified elementary supremum. Its finiteness follows from the exponentials at x=0 and infinity, for every fixed R. It depends on R, not N,r,theta.

For any density u=g*nu, Cauchy--Schwarz applied inside the convolution gives

    (u')^2/u <= (g'^2/g)*nu.

Integrate with e^(3x/4), use (10), and compute the anchor integral exactly:

    int e^(3x/4)(u')^2/u dx
      <=1024 int e^(3x/4)g(x)(3/x-4)^2 dx
      =1024*(382976/28561)<2^14.                       (17)

It follows that int e^(x/4)|u'|/sqrt(u) dx<=256. Values with u=0 are interpreted as zero; the convolution has no boundary atom. Also the fixed anchor yields

    u(x-a)<=e^(4a)u(x), a>=0.                         (18)

The polynomial x^3 in g is increasing on the positive half-line after the common exponential is removed, which proves (18) before convolution.

For the fast part of (15), the fundamental theorem of calculus, (18), (16), and (17) give

    int W_R(x)|q_fast(x)|/sqrt(u(x)) dx
      <=256 C_R[d+(4/9)int(e^(9v/4)-1)nu_f(dv)]
      <=256 C_R[d+(4/3)int v nu_f(dv)]<274 C_R.        (19)

The middle inequality uses the gamma scales <=1/9: integrating their exponential moments gives
int(e^(cv)-1)nu_f(dv)<=c int v nu_f(dv)/(1-c/9) at c=9/4. Thus every fast jump, including the infinite small-jump activity, is included.

The slow compound-Poisson part cannot be bounded by (19), since its largest scale is one. Keep its Poisson score instead. If K is its Poisson count, conditioning on Y_theta gives

    q_B(x)=u_theta(x) E[K/theta-Lambda |Y_theta=x].

Under exponential weighting at lambda=3/4, the count tilts to Poisson(theta*Lambda_lambda), where

    Lambda_lambda=int e^(lambda v)nu_B(dv)=2log13<6,
    |Lambda_lambda-Lambda|=2log(13/4)<3.

Conditional Cauchy--Schwarz and (10) give, for theta>0,

    int e^(3x/4)q_B(x)^2/u_theta(x) dx
                         <=1024(6/theta+9).           (20)

Thus int W_R|q_B|/sqrt(u) dx<=192 C_R(theta^(-1/2)+1). The singularity is integrable; this estimate does not assert a uniform weighted score bound at theta=0.

At points where the densities are positive, put x=pi e^(2t), y=pi e^(-2t) and

    v_theta(t)=(h_theta(t)/2)
           [q_theta(x)/u_theta(x)+q_theta(y)/u_theta(y)]. (21)

At zero-density points use zero almost everywhere. The two terms have equal weighted integrals by t->-t. Combining (19),(20) therefore proves

    int e^(R|t|)|v_theta(t)|dt
              <=C_R[466+192 theta^(-1/2)],            (22)

and its theta integral is at most 850 C_R. This includes both reciprocal tails and the changing support endpoints.

Here the parameter derivative exists before the chain rule is applied. On the space C_0(R), let P_theta f(x)=E f(x-C_theta-V_theta). The zero-extended fixed gamma density g is C^2 with bounded first derivative. Its generator

    Lg=-d g'+int[g(x-v)-g(x)](nu_B+nu_f)(dv)

is in C_0(R), because the Levy measure has finite first moment. To see the generator-domain assertion directly, truncate jumps below eta. The corresponding L_eta g converges uniformly to Lg, with error at most ||g'||_infinity int_(0,eta) v(nu_B+nu_f)(dv). Coupling the omitted jumps shows P_(theta,eta)f -> P_theta f uniformly in x and theta in [0,1] for each f in C_0(R), by uniform continuity of f and the omitted-jump mean bound. Passing to the limit in P_(theta,eta)g-g=int_0^theta P_(a,eta)L_eta g da gives P_theta g-g=int_0^theta P_a Lg da. Thus q_theta=P_theta Lg is the continuous C_0-valued parameter derivative. Commutation of convolution, the physical derivative, and the compensated jump integral gives precisely (15).

For clarity, now prove the chain rule first on a COMPACT t interval, where W_R is bounded below by a positive constant and the reciprocal arguments stay in a compact subset of (0,infinity). Regularize the PRODUCT by sqrt(u_theta(x)u_theta(y)+eta^2)-eta. This is bounded by h_theta, and its derivative is bounded by the actual absolute majorant in (21), since its denominator is at least sqrt(u_theta(x)u_theta(y)). Adding eta to each density separately would not retain that majorant at the reciprocal tails. Equations (19),(20) give an integrable majorant in (theta,t), so dominated convergence, rather than uniform L1 bounds alone, passes the regularized fundamental theorem to the limit.

For fixed t, positivity holds on the single initial parameter interval theta*d<min(x,y); beyond it the product is zero. On the positive interval the ordinary scalar chain rule applies. Equations (19),(20) and Fubini show that its absolute derivative is integrable in theta for almost every t, including near theta=0. At the other endpoint the continuous product tends to zero. The scalar fundamental theorem therefore extends across that endpoint, with no additional boundary measure. This also explicitly covers the support boundary in the preceding compact-interval limit. Finally exhaust the real line. Equation (22), used at R+1 when the required weight is e^(R|t|), makes the omitted derivative tails uniformly integrable; (11),(12) do the same for the original sources. The resulting weighted L1 identity is h_b-h_a=int_a^b v_theta dtheta, so h_theta is absolutely continuous in each of these weighted spaces with the displayed derivative almost everywhere. The same argument with |t|^k<=k!e^|t| handles every fixed t moment.

Consequently F_theta is absolutely continuous in theta locally uniformly in z, with

    dot F_theta(z)=Z_theta^-1 int v_theta(t)
                                  [e^(izt)-F_theta(z)]dt,
    dot mu_(2,theta)=Z_theta^-1 int v_theta(t)
                                  [t^2-mu_(2,theta)]dt. (23)

These exact signed expressions pay normalization before any estimate. In particular dot F_theta(0)=0.

## 4. A complete global zero budget, independent of theta

Elementary maximization of the double exponential in (12) gives

    |F_theta(z)|<=2^40[2(|z|+2)]^(|z|/2).              (24)

For instance int exp[a|t|-(3/2)cosh(2t)]dt<=3[2(a+2)]^(a/2). Also
|F_theta(z)-1|<2^43|z| for |z|<=1, using |t|<=e^|t| and the same bound with a=2. Therefore all functions share a zero-free disk |z|<=2^-44.

Jensen at radii R,2R gives a uniform zero count O(1+R log(2+R)); partial summation gives a uniform inverse-square tail O((1+log R)/R). All constants here can be taken from (24). Thus even pairing in Hadamard factorization is valid, there is no omitted exponential factor, and all multiplicities in (4) are controlled.

Let

    J_theta(a)=(1/(2pi))int_0^(2pi)
                              log|F_theta(ae^(i phi))|d phi.

Jensen implies J_theta>=0. The paired product and F_theta''(0)=-mu_(2,theta) give the exact identity

    Delta(F_theta)=(1/2)int_0^infinity J_theta(a) da/a^3
                                      -mu_(2,theta)/8. (25)

One direct check of the constants is to integrate each Jensen zero contribution:
int_b^infinity log(a/b)da/a^3=1/(4b^2). Subtract the reciprocal squared-zero coefficient at the origin; a quartet contributes exactly b^2/|a+ib|^4 to (25).

For R>=1, (24) supplies the explicit, complete Jensen tail bound

    0<=int_R^infinity J_theta(a)da/a^3
      <=14/R^2+[log(2R+4)+1]/(2R)=:T(R).              (26)

Indeed log|F_theta|<=28+(a/2)log(2a+4), and integration by parts uses
int_R^infinity log(2a+4)da/a^2
=log(2R+4)/R+(1/2)log(1+2/R)
<=[log(2R+4)+1]/R. No fixed-stage exterior-zero radius is substituted for this bound.

## 5. Signed integrated Jensen variation, with crossings and collisions included

Fix epsilon>0 and put

    J_(theta,epsilon)(a)=(1/(4pi))int_0^(2pi)
        log[(|F_theta(ae^(i phi))|^2+epsilon^2)/(1+epsilon^2)]d phi.

The normalization at zero is essential. Define, for z in C,

    C_(theta,epsilon)(z)
      = Re[dot F_theta(z) conjugate(F_theta(z))]
                                   /(|F_theta(z)|^2+epsilon^2)
        +dot mu_(2,theta) Re(z^2)/[2(1+epsilon^2)],

    V_(epsilon,R)(theta)
      =(1/(4pi))int_0^R int_0^(2pi)
                    C_(theta,epsilon)(ae^(i phi)) d phi da/a^3
                    -dot mu_(2,theta)/8.              (27)

The added quadratic term has angular integral zero. It cancels the actual leading term pointwise at a=0: F_theta(z)=1-mu_(2,theta)z^2/2+O(z^4). Thus C=O(a^4) near zero, with the integrable theta bounds from (22),(23). Omitting this subtraction and claiming absolute radial/angular integrability at the origin would be incorrect.

**Theorem (anchored production balance).** For every fixed N>=2,r>=0,

    Delta(F_(N,r))
       =lim_(R->infinity) lim_(epsilon->0+)
                           int_0^1 V_(epsilon,R)(theta)d theta. (28)

At every R>=1 the absolute error after the inner limit is at most

    T(R)/2=7/R^2+[log(2R+4)+1]/(4R).                  (29)

**Proof.** For epsilon>0 and finite R, the chain rule, (22), and the quadratic subtraction justify the fundamental theorem of calculus and Fubini. Its exact result is

    int_0^1 V_(epsilon,R)dtheta
      =(1/2)int_0^R [J_(1,epsilon)-J_(0,epsilon)]da/a^3
                          -(mu_(2,1)-mu_(2,0))/8.     (30)

For each endpoint, on an annulus the finitely many zeros may be factored locally, and log|z-rho| is locally integrable. Dominated convergence (or monotone convergence after an integrable lower bound) therefore lets epsilon decrease to zero in the integrated logarithms. Near zero the common zero-free disk and the even Taylor expansion give the uniform O(a^4) angular estimate required for the a^-3 weight. This proves (30) with ordinary J after the inner limit.

Now use (25). Each omitted endpoint tail lies in [0,T(R)]. Their difference, multiplied by 1/2, has absolute value at most T(R)/2. Finally Delta(F_0)=0 by the Bessel anchor. This proves (28),(29). QED.

No unregularized logarithmic derivative was integrated through zeros, no zero was assumed simple, and no interchange of the epsilon and R limits is asserted. Zeros crossing a chosen circle, real-pair collisions, and splitting near multiple zeros are already included by the endpoint logarithmic identity. In particular no additional zero-velocity term should be appended to (28).

### 5.1 Why differentiable zero labels would have been unsafe

The exact polynomial control

    P_t(z)=(1-z^2)^2+t z^2,    -1/4<=t<=1/4,

has Delta(P_t)=max(t,0)/4. For t<0 all four roots are real; for t>0 the squared roots lie on the unit circle and a first-quadrant root has (Im rho)^2=t/4. Thus the defect has a corner at the collision. For a higher real multiplicity its leading growth can involve fractional powers of t. Formula (28) remains meaningful in these situations; assigning an everywhere smooth Delta'(t) would not. This polynomial is an exact analytic control, not a substitute for the native gamma law or a characteristic-function claim.

## 6. What modular reciprocity supplies at the native endpoint

There is a second useful interpolation, the original #865 one: keep X_N, and interpolate the tail exponent from its exact exponent psi to its Radau exponent psi_r. Write its parameter as lambda to distinguish it from the anchored path. Let q_0 be the physical density derivative at lambda=0, where the density is exactly f.

Its signed Levy generator is

    q_0(x)=-d f'(x)+int[f(x-v)-f(x)]ell(v)dv,
    ell(v)=[sum_j alpha_j e^(-v/x_j)
                         -2sum_(n>N)e^(-n^2v)]/v,
    int v|ell(v)|dv<=2tau_N-d.                         (31)

It is the derivative of the full source, not only of its finite head. Let

    Q(s)=int_0^infinity (x/pi)^(s/2)q_0(x)dx.

The #865 positive remainder has psi_r(s)-psi(s)=s^M K(s), M=2r+2, with K the Laplace transform of a positive measure k of mass a_r=E_r/M. The exact distributional identity q_0=-D^M(k*f), and integration by parts against complex powers, give

    Q(s)=-a_r pi^(-M)(s/2)_falling_M
                       E[((X+W)/pi)^((s-2M)/2)],       (32)

where W is independent of X and has law k/a_r. All positive and inverse moments needed here exist: X+W>=X and the complete f has double-exponential small-x behavior through (3). The boundary terms vanish. This is an entire Mellin identity.

At this endpoint Jacobi reciprocity removes the nonlinear density ratio in the first variation. With s=1/2+iz, (3) gives h(t)=e^(5t/2)f(pi e^(2t)), and exactly

    dot F_native(z)
      =[Q(s)+Q(1-s)]/[4xi(1/2)]
                        -Phi(z)Q(1/2)/[2xi(1/2)].     (33)

To verify the scale, the Fourier transform of e^(5t/2)q_0(pi e^(2t)) is Q(s)/(2pi), and the variation of the geometric mean is half the sum of this expression and its reflected counterpart. The original normalizer is xi(1/2)/pi. Thus every factor in (33), including the normalizer correction, is fixed.

Equation (32) also yields a useful exact leading comparison in safe Euler half-planes. The remainder formula in #865 gives

    E W=[M/(M+1)]
       [(int x^2 p_r(x)^2 d sigma_N)/E_r+2sum_j x_j]
                    <=[M(M-1)/(M+1)]b.               (34)

For 0<=sigma=Re s<=1, let p=s/2. Since Re(p-M)<0, the integral mean-value estimate for a power gives

    Q(s)=-2a_r pi^(-M)(p)_falling_M xi(s-2M)+Err(s),
    |Err(s)|<=2a_r pi^(-M-1)|(p)_falling_M||p-M|
                                E W * xi(sigma-2M-2). (35)

By the functional equation the displayed xi values are on Re s>=2M and its reflection; the real error ceiling is an ordinary positive moment. These are native signed tangent coordinates, not a sign theorem for Q/Phi. At M=2, the polynomial -4p(p-1)=z^2+3/4+iz recovers the variance-shift operator of #855, including its two reflected signs. At a simple zero, (33) gives its local velocity, but division by xi' is not valid at a multiple zero; (28) avoids that issue.

Critically, inserting (33) into a variation integral starting at the native endpoint still leaves Delta(Phi) as its initial value. No claim that the tangent calculation alone evaluates that constant is made.

## 7. A quantitative native refutation of nonpositive forward production

Import exactly the proposed complete defining-integral disk theorem GE4 in #858 at its frozen head. It asserts one simple centered-N=5 zero in the radius-10^-12 disk about

    31.0835163803300613860836804713778137956057544691
       +0.2347791171837078741080118319340221394471947526 i.

This is the actual r=0 endpoint of (1), not a changed-rate stress source. The exact decimals and radius imply Im rho>23/100 and |rho|<32. Therefore

    Delta(F_(5,0))>529/(10000*32^4)>1/20000000.          (36)

No other zeros need be discarded or assumed real: all remaining terms of the full defect are nonnegative. The new rational checker verifies these disk-to-defect inequalities; it does not regenerate the inherited integral certificate.

By (28), the TOTAL signed production on the explicit positive convolution path from the Bessel anchor to this native centered source is greater than 5*10^-8. Thus a claim that (27) has nonpositive total production at every native finite stage is false under the inherited certificate. No claim is made that the production has a pointwise derivative of one sign, or that every parameter value has an off-real zero.

This does not refute possible decay with N or growing Radau order. It establishes the precise requirement: a completion cannot rely on a blanket nonpositive finite-stage source-flow inequality. It must permit real defect creation and prove that the complete signed production tends to zero along the actual cofinal family.

An optional scale comparison is available from the published Platt--Trudgian theorem that all zeta zeros through height H=3*10^12 lie on the line. Combined with the complete Jensen count n_Phi(t)<=26+2t log(2t+2) from #862 and |Im rho|<1/2, it gives

    Delta(Phi)<=13/(8H^4)
              +[log(4H)+1/3]/(6H^3)<2*10^-37.         (37)

Indeed off-real zeros have |rho|>H, and partial summation bounds their all-zero fourth-power tail by 26/H^4+(8/3)[log(4H)+1/3]/H^3; (4) contributes the further factor 1/16. This is a consequence of an imported finite-height theorem, not a new zero census, a vanishing result, or numerical evidence that proves RH. The main balance and (36) do not depend on (37).

## 8. The smallest remaining estimate and what this attempt achieved

Write

    B_(N,r)(R)=lim_(epsilon->0+)int_0^1
                                      V_(epsilon,R)(theta)dtheta.

Choose, for example, r_N=floor(N/4) and R_N=N. The complete tail in (29) tends to zero independently of N. The exact remaining estimate can therefore be stated without a zero list or unknown baseline:

    B_(N,r_N)(N)=o(1).                                  OPEN-GJV

Together with (28),(29), this is equivalent to Delta(F_(N,r_N))->0; the source convergence in #865 then gives RH by #862's finite repair/Hurwitz argument, or directly by nonnegativity of the limiting zero sum.

OPEN-GJV is NOT proved. The bounds (19),(20),(22) establish existence and parameter regularity of the signed source integral, not its smallness after the logarithmic denominator. Near-zero amplification, the variance subtraction, and cancellation of contributions across parameters and radii cannot be replaced by separate absolute estimates. The native recurrence and Jacobi identity enter (31)--(35), but no sign or summable cancellation estimate for their contribution to (27) has been derived.

The new completed components are: an explicit zero-safe anchor with an exact native endpoint; a first-order Levy/Poisson representation that controls the reciprocal-source parameter derivative; a fully signed integrated Jensen formula with multiplicities and collision singularities handled; an explicit complete spectral-radius remainder; and a quantitative native counterexample to one possible finishing sign. This reaches a sharper, reviewable version of the missing estimate, not an RH completion.

## 9. Validation and source boundaries

check.py uses only exact integers and Fractions. It reconstructs the gamma-head identity, weighted Fisher constant and normalization inequalities, finite Radau moment/cumulant controls, the M=2 native tangent polynomial, collision controls, the imported disk-to-defect lower bound, and the optional finite-height-to-defect arithmetic ceiling. The results file records precisely those bounded controls. Neither normal versus optimized Python nor multiple algebra panels constitute independent proof review.

No native Fourier/Jensen integral, large-order Radau rule, new zero, parent certificate campaign, Lean build, or repository-wide check was run in this packet. The imported #858 disk retains its proposed/certificate-dependent status. The external Platt--Trudgian theorem is an explicitly named published input; its computation was not replayed. The analytic proofs, particularly the weighted parameter-chain rule and the order of the regularization limits, require independent mathematical review.
