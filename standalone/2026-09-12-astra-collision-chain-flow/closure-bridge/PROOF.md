# CJB26: a quantitative joint bridge and an eight-moment connected theta chain

Date: 2026-09-12. **PROPOSED component proofs and computer-assisted existence;
independent mathematical and implementation review required. RH is not proved.**

This is an additive child of CCF26 / PR875 at
`be149104721ae7b65b624c100118edfd7b76b69b`. It preserves all previous claims,
files and acceptance statuses. Classical Lee--Yang, finite random-cluster
expansion, entire products, Taylor estimates, and Brouwer's theorem are
credited ingredients, not discoveries claimed here. The source-specific
combination and constants below are proposed for review; no priority claim.

The positive construction in Sections 1--2 matches one more native even moment
than CCF26, at a *specified nonzero coupling interval*. Sections 3--5 join the
Ising and gamma routes quantitatively. They do not prove the cofinal feasibility
hypothesis of Section 4. Section 6 exposes the native arithmetic remainder
without claiming to bound it.

## 1. An actual connected infinite chain matching through degree eight

Use the unchanged even theta density, for t >= 0,

    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                            exp[-pi n^2 exp(2t)],
    w(t)=phi(|t|)/integral_R phi(|u|)du,
    mu_(2r)=integral_R t^(2r)w(t)dt, v=mu_2.

The classical Jacobi/Mellin identification is
Phi(z)=Xi(z)/Xi(0)=integral exp(izt)w(t)dt. In particular the scale in this
manuscript is the native t scale, not variance-one rescaled coordinates.
The inherited complete-source quadrature contract is re-evaluated, not replaced
by a saved table. Let kappa_(2r) denote these native cumulants.

Let (sigma_n) be the stationary fair-sign Markov chain with

    P(sigma_(n+1)=sigma_n)=(1+q)/2.

For q>0 every finite restriction is a connected, zero-field, nearest-neighbor
ferromagnet with J=atanh(q)>0 on each edge. Its covariance is q^|i-j|.
The observable weights are, IN THIS ORDER,

    a_1,...,a_31 = (25 copies of a, 4 copies of b, c, e),
    a_n = 1/(2n)+d(q) log(n)/n^2, n>=32,
    d(q)=7/[8 log((1+q)/2)].                                  (1)

Set r=(1-q)/(1+q),

    m_q(u)=sinh(u)/sqrt(sinh(u)^2+r^2),
    C(q)=-1+int_0^1 m_q(u)/u du +int_1^infinity [m_q(u)-1]/u du,
    S=sum_(n>=32) log(n)/n^2,
    A(q)=-(1+log(2pi))/2 +(log2-gamma)/2+H31/2-C(q)/2-d(q)S.     (3)

Here gamma is Euler's constant and H31=sum_(n<=31)1/n. The integrals
are ordinary convergent real integrals with the removable value at u=0.

**Theorem CJB1 (proposed).** There is at least one parameter vector in the
closed radius-10^-6 infinity-norm box about the EXACT rational center

    a = 0.0220541091324322
    b = 0.06132452139209203
    c = 0.10954428841029012
    e = 0.004620404935551159
    q = 0.018145167180821594                                  (4)

such that X=sum_(n>=1)a_n sigma_n satisfies

    25a+4b+c+e=A(q),
    E X^(2r)=mu_(2r), r=1,2,3,4.                             (5)

The sum is an L2 limit of the *connected* process, not a sum of independent
blocks. All weights are positive, 0<q<1/32, and X has an entire characteristic
function with only real zeros. Its complete real-field growth is

    log E exp(hX)=(h/2)log h-[(1+log(2pi))/2]h
                                  +(7/4)log h+O(1).          (6)

Every zero of the equation in this box has the strict separation

    .029 < [E X^10-mu_10]/v^5 < .032.                         (7)

Consequently these roots do NOT realize the full theta law. The theorem
asserts existence, NOT uniqueness and NOT a solution at every q in the box.
This improves the matched order of CCF26's growth-calibrated infinite chain,
not the repository's separate finite or harmonic-star degree-14 records.

### Infinite law and growth

For any finite real vector u, the covariance matrix gives
Var(sum u_i sigma_i)<=[(1+q)/(1-q)]sum u_i^2. This constructs the L2 limit.
The finite weighted Lee--Yang theorem, with its even product at zero, gives

    E X_N^(2k)/(2k)! <= (Var(X_N)/2)^k/k!,
    E exp(hX_N)<=exp(Var(X_N)h^2/2).                           (8)

Uniform exponential integrability and L2 convergence yield all moments and
locally uniform entire convergence. Hurwitz then retains only real zeros.
This is the classical finite-graph Lee--Yang input; the program does not
numerically certify that theorem.

The growth computation uses the connected transfer-matrix comparison proved
in #871 and CCF26, with its hypotheses retained here. If

    f_q(u)=log{[(1+q)cosh u+sqrt((1-q)^2+(1+q)^2 sinh^2u)]/2},

then log E exp(hX)=sum_n f_q(h a_n)+O(1). The error is uniformly bounded in
h because there are finitely many head transitions and the positive Perron
vector ratios telescope on the positive decreasing tail; boundary vectors
are retained. This is not multiplication of eigenvalues as an equality.
The harmonic Riemann sum is
sum f_q(x/n)=x log x+(gamma+C(q))x+O(1). The complete logarithmic weight
correction contributes h d S+2d log((1+q)/2)log h+O(1).
Replacing the first31 harmonic weights contributes h(A-H31/2)+O(1).
Substitution of (1),(3) gives (6). In the displayed box |d|<1.3 and
1/(4n)<a_n<1/(2n), 0<-a'(x)<=1/(2x^2) on x>=32, so the earlier tail and
transfer hypotheses really apply. No zero of Xi enters this calibration.

## 2. Full-source, full-tail Brouwer certificate

The certificate uses the 512-bit outward dyadic backend of CCF26, byte-locked
in `certify_chain.py`. `native_theta.py` recomputes moments through ten from
all n<=20 and the 1/128 spatial mesh through t=3, adding the inherited complete
alias, index and spatial-tail error (2r)! 2^-237. Normalization is bounded
away from zero. The analytic remainder proof in the parent NUMERICS/ISING
manuscripts is an explicitly inherited proposed component, not a newly
independent implementation.

### 2.1 Exact connected recursion

For a finite segment define F(u)=E exp(iuX),
S(u)=E[sigma_last exp(iuX)]/[iF(u)] as formal series at zero. Appending weight a
across an edge of correlation q gives exactly

    S_new=[tan(au)+qS]/[1-q tan(au)S],
    -log F_new=-log F-log cos(au)-log[1-q tan(au)S].              (9)

All coefficients of S and -log F are nonnegative. The checker retains S
through degree nine and -log F through degree ten. For two adjacent segments,
reverse the second so its recorded endpoint faces the first; reversibility
then gives

    F_join=F_left F_right(1-q S_left S_right).                 (10)

All cross terms are retained. The tail32..8192 is propagated backward with
one automatic-differentiation variable q; the31 head weights and their
joining edge use five variables. Small independent spin enumerations in the
tests check values and derivatives against (9),(10), not against a saved
large-chain answer.

### 2.2 Complete tails without differentiating them by assumption

Uniformly on the box, a_n<=1/(2n), q<=1/32, and the head mass is <1.
Thus S_31<=tan u coefficientwise. The checker uses a separate exact rational
recursion from n=32 through64 to prove

    S_64<=tan(2u/64) through degree7,
    S_64<=tan(3u/64) through degree9.                           (11)

For odd degrees j<=7, q<=(5/8)^j; for j<=9, q<=(3/4)^j. At n>=65,

    1/2+(5/8)*2*(65/64)<2,
    1/2+(3/4)*3*(65/64)<3.

The tangent addition identity therefore propagates (11) to every subsequent
n. The logarithmic increment in (9) is coefficientwise at most
-log cos(2u/n), or -log cos(3u/n) respectively. With N=8192 and sign cumulants
c2=1,c4=-2,c6=16,c8=-272,c10=7936, the ENTIRE omitted signed cumulants obey

    0<=(-1)^(r+1)[kappa_(2r,infinity)-kappa_(2r,N)]
          <=|c_(2r)|2^(2r)/[(2r-1)N^(2r-1)], r=2,3,4,
    0<=kappa_(10,infinity)-kappa_(10,N)<=7936*3^10/(9N^9).       (12)

For the variance use the exact integral of a(x)^2,

    I(N)=1/(4N)+d(log N+1/2)/(2N^2)
                 +d^2[(log N)^2+(2/3)log N+2/9]/(3N^3).       (13)

The approximation is V_N+kap I(N), kap=(1+q)/(1-q). Let qc=1/32,
kapc=(1+qc)/(1-qc). Its complete absolute error is at most

    kapc/(4N^2)+qc/[4(1-qc)^2 N^2]
                                +2qc/[(1-qc)N(N+1)].         (14)

Indeed the sum of a_n^2 differs from its integral by at most1/(4N^2).
For the stationary omitted segment, the covariance correction to kap sum a_n^2
is nonpositive with magnitude at most q/[4(1-q)^2 N^2], using
0<=a_n-a_(n+k)<=k/(2n^2). The complete prefix-to-tail covariance is at most
2q/[(1-q)N(N+1)], by E[sigma_N X_N]<=2/N from (11).
No independence of prefix and tail is asserted.

### 2.3 Complete calibration error

The finite calibration uses Simpson512 on [0,1] and Simpson4096 on [1,8].
For real q in the box, r>=2/3. On a complex u disk of radius1/4,
Re(r^2+sinh^2u)>=55/144. The analytic square root is its positive continuation;
both removable integrands have modulus<4 on their respective disks. Cauchy
bounds their fourth derivatives by24576. Also 0<1-m_q(u)<3exp(-2u) for u>=8.
Therefore the complete error in C is at most

    24576/(180*512^4)+24576*7^5/(180*4096^4)+3exp(-16)/16.       (15)

Euler's constant is approximated by H8192-log8192-1/(2*8192), with absolute
error1/[6*8191^2]. For S, sum32..255 and use at256 the integral, half-endpoint,
B2 and B4 terms. The entire periodic-B4 remainder is bounded by
|f'''(256)|/720 for f(x)=log(x)/x^2; f''''>0 there and beyond. These errors,
including multiplication by |d|, enter the head-mass equation. In particular
the code does not differentiate the unknown Simpson or infinite-tail error.

### 2.4 Why existence really follows

Let G(x) be the five COMPLETE equations: head mass minus A, then differences
of kappa2,-kappa4,kappa6,-kappa8, divided by the four fixed positive rational
scales in parameters.json. Write G=H+r, where H is the finite-calibration,
finite-chain-plus-variance-integral expression. Its values and its whole-box
Jacobian are computed by outward automatic differentiation. All differences
between the actual equations and H form the continuous remainder r, bounded
by (12)--(15). Uniform series convergence proves the required continuity.

R is the rational preconditioner in parameters.json; it need not be an exact
inverse. Direct rational elimination proves it nonsingular. If c is (4) and
radius=10^-6, the returned bounds are

    ||R H(c)||_infinity <7.441e-9,
    sup_box ||I-R H'(x)||_infinity <.076254,
    sup_box ||R r(x)||_infinity <3.024e-7,
    ||RH(c)||+radius*sup||I-RH'||+sup||Rr|| <3.861e-7.          (16)

The exact, outward endpoints are in chain_result.json. For T(x)=x-RG(x), the
mean-value bound and (16) put the entire box strictly into itself. Brouwer's
fixed-point theorem supplies G(x)=0 because R is nonsingular. No differentiable
bound on r or uniqueness assertion is needed. Checking only ||RH(c)|| would
not prove this statement.

Finally (12) for degree10, complete native kappa10, and the whole parameter box
bound (kappa10(X)-kappa10(theta))/v^5 within (.029,.032). Since all lower even
cumulants match and all odd cumulants vanish, this equals the raw tenth-moment
difference, proving (7).

## 3. A graph-wide necessary interaction budget

This addresses the tempting but invalid idea of iterating small-coupling
finite-moment continuations while letting all the interaction disappear.
It is NOT an obstruction to arbitrary Ising realizations or to RH.

For any finite zero-field ferromagnet with nonnegative weights a_i, write

    X=sum a_i sigma_i, V=Var X, S=sum a_i^2, D=V-S>=0,
    chi(t)=E exp(itX), chi_0(t)=product cos(a_i t).

**Theorem CJB2.** For every real t,

    |chi(t)-chi_0(t)| <=(t^2/2)D,                            (17)
    |chi(3t)| <=exp(3St^2/4)|chi(t)|
                         +(t^2/2)[9+exp(3St^2/4)]D.         (18)

**Proof.** Expand each bond as
exp(J sigma_i sigma_j)=exp(-J)[1+(exp(2J)-1)1_(sigma_i=sigma_j)].
After expanding all edges, each partition into bond clusters C has positive
weight proportional to 2^(number of clusters) times its bond weights.
Conditioned on those clusters, their spins are independent fair signs with
observable A_C=sum_(i in C)a_i. Consequently
chi=E product_C cos(A_C t), V=E sum_C A_C^2. This is the finite classical
random-cluster expansion, with no infinite-volume hypothesis.

Merging positive weights A,B changes their cosine product by
-sin(At)sin(Bt). Its absolute value is <=t^2 AB, and all untouched real cosine
factors have modulus<=1. Summing merges inside a cluster costs exactly
(t^2/2)(A_C^2-sum_(i in C)a_i^2). Average to prove (17).

The scalar inequality |cos3x|<=exp(3x^2/4)|cos x| uses the factor identity,
not division by a possibly zero cosine. To verify its nontrivial branch put
y=x^2. For y>=3/2, exp(3y/4)>=exp(9/8)>3. For 0<=y<=3/2, the alternating
cosine series gives sin^2x<=y-y^2/3+2y^3/45. The positive exponential terms
through degree3 make exp(3y/4)-(4sin^2x-1) at least

    2-(13/4)y+(155/96)y^2-(619/5760)y^3
      >=2-(13/4)y+(5581/3840)y^2 >0.

The last quadratic has negative discriminant and positive leading coefficient.
The other absolute-value branch is at most1. Multiplication proves
|chi_0(3t)|<=exp(3St^2/4)|chi_0(t)|, and applying (17) at t and3t gives (18).

**Native consequence, conditional on the explicitly imported STAR26 source
certificate.** That certificate supplies v<1/20, M0<5, a real theta zero
gamma<15, and |Phi(3gamma)|>5.8e-13. It does not assume RH or simplicity.
For any all-order theta-realizing sequence of finite ferromagnets, (8) permits
passage of characteristic functions and V->v. Since S<=V, (18) at gamma gives

    liminf D >= 2*5.8e-13/[225*(9+5000)] > 10^-18,              (19)

where exp(135/16)<5000. For a subsequence on which D does not stay bounded,
the lower bound is automatic; otherwise pass to a further convergent subsequence.
The source integral certificates behind these constants are NOT rerun here.

For a chain whose adjacent correlations are bounded by r<1,
D<=2rS/(1-r)<=2rV/(1-r), by its product covariance formula. Thus no all-order
realizing chain sequence can have maximal adjacent correlation tend to zero.
This does not exclude a small FIXED positive q, or the model in Section1.
The essential quantity in (19) is observable correlation variance, not the
number of edges, maximum edge coupling, or total unweighted coupling.

## 4. A finite-moment Ising certificate controls the WHOLE gamma defect

Let G be a finite-ferromagnet characteristic function of variance at most V.
Let F be any symmetric probability characteristic function with all exponential
moments. Denote its native even moments by mu_(2r,F). Define

    E_m(R)=sum_(r=0)^m |mu_(2r,F)-mu_(2r,G)| R^(2r)/(2r)!,
    eta_m(R)=E_m(R)+[F(2iR)+exp(2VR^2)]/4^(m+1).               (20)

**Theorem CJB3 (zero exclusion with no model-zero census).** If 0<b<=R and

    eta_m(R)<exp[-(2/3)VR^2]*(b/R)^(2VR^2),                   (21)

then F has no zero with |z|<=R and |Im z|>=b.

**Proof.** Finite Lee--Yang and the even exponential-type canonical product give
G(z)=product_(j)(1-z^2/r_j^2), with real r_j>0 including multiplicities and
sum_j r_j^-2=Var(G)/2. There is no quadratic exponential factor for finite
exponential type, and evenness removes the linear one. For |z|<=R,

    |1-z^2/r^2|^2=[(|z|^2-r^2)^2+4r^2(Im z)^2]/r^4.

For r<=2R this is at least (b/R)^2. There are at most2VR^2 such factors.
For r>2R, the factor is >=1-R^2/r^2>=exp[-(4/3)R^2/r^2]. The complete product
therefore obeys

    |G(z)|>=exp[-(2/3)VR^2]*(b/R)^(2VR^2).                    (22)

This deliberately weak bound retains the entire far-zero product. No simplicity
or supplied zero position is used. Degenerate G=1 is covered directly.

Both moment sequences have nonnegative even entries. Their Taylor tails at R
are at most4^(-m-1) times their MGFs at2R. Inequality (8) bounds the latter for
G by exp(2VR^2). Thus |F-G|<=eta_m(R) on the whole complex disk. At any zero
in the specified region this would contradict (21),(22). This is direct
nonvanishing, not an unproved pairing of zeros.

### Application to the unchanged centered gamma source

Use the centered F_N of #862:
X_N=sum_(n<=N)Gamma(2,1)/n^2, tau_N=2sum_(n>N)n^-2,
h_N(t)=sqrt(g_N(pi exp(2t))g_N(pi exp(-2t))), where g_N is the density of
X_N+tau_N, and normalize its Fourier integral. Keep this family unchanged.
The following proposed complete-source bounds are imported from #862:

    max_(|z|<=r)|F_N(z)|<=204800(r+2)^(r/2),
    n_N(r)<=26+2r log(2r+2), r>=1,
    Delta_N=(1/4)sum_rho mult(rho)(Im rho)^2/|rho|^4,
    Delta_N tail beyond R <=7/R^2+[log(4R)+1]/R.                (23)

They count all complex zeros and multiplicities. Also Delta_N->Delta_Phi
and Delta_Phi=0 iff RH, by full source convergence and the uniform tail.
None of those inherited results asserts the vanishing itself.

Assume F_N(2i)<=2. Then for |z|<=1, positivity of the Taylor moments gives
|F_N(z)-1|<=(|z|^2/4)[F_N(2i)-1]<=1/4. There are no zeros in that disk.
Integration of the complete count in (23) gives

    sum_rho mult(rho)/|rho|^4
       =4 int_1^infinity n_N(r)r^-5 dr
       <=26+(8/3)log4+8/9 <31.                               (24)

Hence any certificate (21) for this F_N yields the WHOLE defect bound

    Delta_N <= (31/4)b^2+7/R^2+[log(4R)+1]/R.                  (25)

The weight of zeros outside R was not dropped, nor were small real-zero
clusters presumed simple.

### A completely explicit joint diagonal sufficient for RH

For every integer j>=2 put

    R_j=2^j, b_j=1/R_j, m_j=(2j+4)4^j,
    epsilon_j=2^[-(4j+4)4^j].                                (26)

Suppose there exist N_j->infinity and finite zero-field ferromagnets G_j with
nonnegative weights/couplings and variance<=1 such that

    F_(N_j)(2i)<=2, E_(m_j)(R_j)<=epsilon_j.                   (27)

Then (21) holds. Indeed R>=4, log204800<13 and log(2R+2)<=R give
F_N(2iR)<=exp(2R^2). Both MGF tails together cost at most
2^[-(4j+5)R^2-1], since log2>2/3. The right side of (21) is at least
2^[-(4j+1)R^2]. The sum of the two errors is strictly smaller. Thus

    Delta_(N_j)<=15/R_j^2+[log(4R_j)+1]/R_j ->0.              (28)

By the complete inherited consumer this would prove RH.

**OPEN-JOINT is the existence of models satisfying (27) on this unbounded
schedule. No such sequence is proved or numerically supplied.** The model of
Section1 matches theta through eight, not these gamma moments through m_j,
and is NOT asserted to satisfy even one instance of (27). Formula (26) is a
conservative sufficient budget, not an optimized practical schedule or a
necessary condition for RH. The general inequality (21) permits much better
source-specific choices.

This is the proposed connection: use finite admissible moment realizations to
pay the gamma defect directly, rather than separately proving an all-order
infinite Ising inverse theorem and a universal sign for the gamma score.

## 5. Why a fixed defective gamma stage cannot be fitted indefinitely

The native centered N=5 certificate in #858 supplies a zero rho with
|rho|<32, Im rho>1/5. It is NOT a zero of Xi. Its complete-source certificate
is an imported proposed finite theorem, not rerun by this packet.
The support of the defining t density lies inside (-11/10,11/10): one can
use tau5>=13/36, pi<22/7 and exp(11/5)>792/91. Thus Var(F5)<121/100<5/4
and F5(64i)<=exp(352/5).

Take R=32, b=1/5, V=5/4, m=16384. The right side of (21) is greater than

    exp(-2560/3)*160^-2560 > 2^-21760.                        (29)

Both MGF tails in (20) are together <2^-28929. Therefore there is NO finite
ferromagnet G of variance<=5/4 for which

    E_16384(32)<=2^-21762                                    (30)

for the actual F5 source. In particular no exact match through degree32768
exists. This finite-order consequence tolerates the specified nonzero error;
it is not just a qualitative statement that infinite limits preserve zeros.
No optimal forbidden order is claimed. The variance cap is automatic for an
exact match, and follows from the small second-moment error for (30) as well.

This does not obstruct the moving N_j diagonal. It prevents confusing that
joint problem with fitting a *fixed* nonreal-zero approximant to all orders.

## 6. Arithmetic: expose the bounded collar term exactly

For a native crossing Y use the #848 completion
c_n=mu(n) for n<=Y, c_(2Y)=-2Y m(Y), where m(Y)=sum_(n<=Y)mu(n)/n and
|m(Y)|<=1/Y. Let B=(Y+1)^2-1, F_X=sum_(k<=X)m(k)^2, z=c*c, and retain the
full coalesced kernels

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    D=sum_d z(d)^2 sum_(k=Y+1)^B K_d(k)^2,
    C=sum_(d!=e) z(d)z(e)sum_(k=Y+1)^B K_d(k)K_e(k),           (31)

where the off-diagonal is ORDERED. These are the crossing source's quantities,
not the older clipped or cubic completion covariances.

**Theorem CJB4.** Exactly,

    F_B-F_Y=D_Y+C_Y+4m(Y)P_Y,
    P_Y=sum_(n=Y+1)^(2Y-1) (2Y-n)mu(n)/n,
    |4m(Y)P_Y|<=2(Y-1)/Y<2.                                 (32)

**Proof.** With Q(k)=sum z(d)K_d(k), the two reciprocal moment cancellations
remove log d and H_k, so Q is the rational reciprocal sum of 1*z. The exact
Newton identity gives m(k)=2t(k)-Q(k) through B, with t(k)=m(Y) for
Y<k<2Y and zero thereafter. Let T=(Y-1)m(Y)^2. Then

    D+C=sum Q^2=F_B-F_Y+4T-4 sum t(k)m(k).

But sum t(k)m(k)=T+m(Y)P_Y, by finite summation. This proves the identity.
Finally |P_Y|<=sum_(n=Y+1)^(2Y-1)(2Y-n)/Y=(Y-1)/2; apply the crossing bound.

CCF26 already supplies D_Y asymptotic order (log Y)^4, and #848 supplies its
proposed common growth exponent. Thus C_Y<=K D_Y at unbounded native crossings
would still close that route. Equation (32) does not prove this: it shows,
up to an absolute bounded correction, precisely which native annular energy
that covariance must control. A generic covariance norm bound has not gained
an arithmetic cancellation merely by changing coordinates.

## 7. What has and has not been completed

Proposed proved components: the complete infinite eight-moment chain; the
finite-graph correlation-variance inequality; the quantitative finite-jet to
whole-defect theorem and explicit cofinal consumer; a finite fixed-stage
obstruction; and the exact bounded arithmetic collar identity.

The unproved closure is still arithmetic information about the ACTUAL source:
either the native crossing covariance upper bound, or OPEN-JOINT (which
simultaneously supplies the analytic routes' missing zero control), or a
successful source-specific full signed-production estimate. None is delegated
to reviewers as a routine omitted lemma. The #876 positive fixed-point
response was read for comparison; its positivity is in Laplace coordinates
and does not establish (21) or (27).

Read VALIDATION.md for what finite commands ran. Finite replay is not a proof
of Lee--Yang, canonical products, the inherited source identities, or any
unbounded feasibility assertion. No independent review, formal proof build,
repository-wide scientific acceptance, or new zeta zero has been claimed.
