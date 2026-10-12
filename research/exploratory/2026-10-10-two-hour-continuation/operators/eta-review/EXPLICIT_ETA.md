# A concrete right extension from the completed scalar native gate

Status: proposed source-qualified analytic theorem, pending independent review.
Scope: every complex native L2 test on every 0<L<=1+10^-36. This is a
microscopic explicit extension, not a specified macroscopic window or RH.
Exact sources: the frozen four-hour-wave operator OPEN_WINDOW_PROPAGATION.md,
CODIMENSION_14_REFINEMENT.md, WINDOW_FAMILY_TO_LOG3.md, the complete native
kernel and coupling O1--O4, the completed codimension14 scalar continuum
receipt and its independent review, and the exact primitive synthesis
receipt. Their precise hashes are bound by check_eta.py and its receipt.
What was run: a source-bound coefficient/constants audit and a fresh exact
rational positive-definiteness check of the serialized complete scalar
matrix. No second continuum integration or endpoint replay is claimed.
Smallest remaining gate: independent analytic/source review and replay of
this new finite audit. Infinite continuity estimates are proved below;
the finite checker does not machine-prove them.

## E1. Exact theorem and retained hypotheses

Retain b=3/2,c=1/2 and the complete literal even kernel W, with native form

    q_L(h,h)=b integral_0^L integral_0^L bar(h(t))W(t-u)h(u)du dt,
    G_L h(t)=integral_0^t cosh(c(t-u))h(u)du.

Assume the reviewed inherited source/coupling/primitive facts O1--O4 on
lengths below log3. In particular, for E_L spanned by sin(j*pi*t/L),
j=1..11, exp(+-ct), cosh(bt), and V_L=E_L^perp, the supporting line gives

    q_L(v,v)>=b[13/10-710L^2/(12*pi)^2] ||G_Lv||^2.

The completed exact L1 tests z_i, i=1..14, and residual R0 satisfy

    S0=U0-(15/8)R0 >=10^-11 I.                          (E1)

Their actual complete coefficients c_ji are the uniquely defined exact
Galerkin coefficients enclosed in the frozen continuum receipt, not chosen
points in its balls. The directed coefficient audit gives

    max_i sum_j |c_ji| < C=10^7.                       (E2)

The same completed source also supplies

    trace((15/8)R0)<1/4,
    sum_i ||G_1z_i||^2<3/4.                            (E3)

The latter is the separately reviewed exact complete synthesis computation.
Then, with eta=10^-36, every complex native test satisfies

    q_L(h,h)>= ||G_Lh||^2/800000000000,
                          every0<L<=1+eta.             (E4)

The primitive is injective, so the form is strictly positive on nonzero
tests. This is a compact primitive norm bound, not an L2 spectral gap.
The source/Weil identification and complete analytic source facts are
inherited reviewed hypotheses, rather than authenticated by this finite
audit. No L>=1+eta claim beyond the closed endpoint follows.

## E2. Fixed coefficients remove moving Cholesky conditioning

Use the unitary rescaling h(Ls)=L^-1/2 H(s),0<s<1. Define

    Z_i(L,s)=sum_j c_ji f_j(L,s),

where the exact114 raw functions are sin(n*pi*s),n=1..11; exp(+-cLs),
cosh(bLs); and sin(n*pi*s),n=12..111, in that order. Let
z_i^L(Ls)=L^-1/2 Z_i(L,s). At one these are exactly the completed tests.
At other lengths they are actual native tests; no energy optimality or
moving orthonormalization is required. On1<=L<=10001/10000,

    ||Z_i(L)||_infty<=5C,
    ||d_LZ_i(L)||_infty<=5C.                            (E5)

Only the three soft functions have a length derivative. These bounds use
exp(3/5)<2,exp(8/5)<5,cosh(bL)<3 and sinh(bL)<3. Every sine remains in
the inventory. No coefficient projection, high frequency or source term
is omitted.

## E3. Complete native kernel bounds, including the moving prime cusp

For0<=x<log3 the literal kernel is exactly

    W(x)=exp(x/2)/2+C_b exp(-bx)+Gamma(x)
         -(P2/b)cosh(bx)+(Q2/b)sinh(b(x-d))1_(x>=d),
    Gamma(x)=sum_(j>=1) exp(-lambda_j*x)/(lambda_j^2-b^2),
    lambda_j=2j+1/2,d=log2,
    C_b=(1-EulerGamma-log(2*pi))/3,
    P2=-zeta'(2)/zeta(2), Q2=log2/sqrt2.                 (E6)

The complete prime constant and gamma sum are retained. The authenticated
source constants satisfy |C_b|<1/2,0<P2<3/5,0<Q2<1/2 and d<7/10.
Partial fractions give Gamma(0)=1/6+log2/3<2/5. Forx>0,

    |Gamma'(x)|<=sum exp(-2jx)/j= -log(1-exp(-2x))
                 <=log(2/x),                           (E7)
    Gamma''(x)<=2sum exp(-2jx)<=1/x.                    (E8)

Indeed lambda_j/(lambda_j^2-b^2)<=1/j, and
lambda_j^2/(lambda_j^2-b^2)<=25/16<2. The logarithmic bound uses
1-exp(-2x)>=2x/(1+2x) and x<=101/100; its right side is positive here.
All remaining smooth first derivatives have total absolute value below5;
all remaining regular second derivatives have total below7. Consequently,
for |x|<=101/100,

    |W(x)|<5,   |x W'(x)|<7,
    |x W''_reg(x)|<9.                                 (E9)

The derivative at zero is logarithmically singular and is never replaced
by a finite point value. The even extension has prime-cusp jumps Q2 in
W' at both x=+-d. The gamma derivative estimate and its logarithmic
integral also give, uniformly in1<=L<=10001/10000 and s in[0,1],

    integral_0^1 |W'(L(s-r))|dr<10.                    (E10)

For example its gamma part is at most twice the integral from0 to1 of
log(2/r), which is below4; the smooth part is below5.

Put T_LZ(s)=integral_0^1 W(L(s-r))Z(r)dr and
D_LZ(s)=integral_0^1 W'(L(s-r))Z(r)dr. As operators on bounded finite
tests, ||T_L||<=5 and ||d_LT_L||<=7. For D_L the regular derivative
has norm at most9. Differentiating the two moving cusp locations adds
at most2Q2*d/L^2<1. Thus its full length variation satisfies

    ||D_L||<=10, ||D_L-D_M||<=10|L-M|.                 (E11)

This bound includes the moving jump, rather than applying dominated
convergence across it without a quantitative term. The singularity at
r=s stays fixed under length rescaling, and (E8) bounds its scaled
derivative. These estimates follow either by splitting at the moving
cusp or by its distributional derivative; the relevant finite-test
convolutions are Lipschitz in length. Pointwise a.e. derivative bounds
and the fundamental theorem of calculus give the displayed differences.

## E4. Source residual and its protected rank-one projection

For K_z(t)=integral_0^L W(t-u)z(u)du, retain the actual coupling source
F_z=-K_z'+c^2 integral_0^t K_z. Its unitary transform is exactly

    Fcal_i(L)=L[-D_LZ_i(L)+c^2 L I T_LZ_i(L)],
    (If)(s)=integral_0^s f(r)dr.                        (E12)

No physical factor of L is suppressed. Equations(E5),(E9)--(E11), with
L<101/100, give

    ||Fcal_i(L)||_infty<=100C,
    ||Fcal_i(L)-Fcal_i(M)||_infty<=200C|L-M|.            (E13)

Explicitly the derivative bound is at most
50C+(101/100)100C+(101/200)25C
 +(1/4)(101/100)^2(35C+25C)<200C.

Let Pcos project onto1,cos(n*pi*s),n=1..11. The complete protected
projection is P_L=Pcos+projector onto

    rho_L=(I-Pcos)sinh(bLs).

Its cos12 moment is

    a12(L)=bL[cosh(bL)-1]/[(bL)^2+(12*pi)^2]>1/1000.

For this explicit lower bound, numerator>=27/16 and denominator<1500,
using pi^2<10 and bL<8/5. Bessel's inequality therefore gives
||rho_L||^2>=2a12(L)^2>10^-6. Also ||rho'_L||<=5. The normalized
rank-one projector hence obeys

    ||P_L-P_M||<=10000|L-M|.                           (E14)

This avoids an inverse of the ill-conditioned soft Gram matrix. Define
r_i(L)=(I-P_L)Fcal_i(L) and R_ij(L)=<r_j(L),r_i(L)>. Then

    ||r_i(L)||<=100C,
    ||r_i(L)-r_i(M)||<=1000200 C|L-M|,
    ||R(L)-R(M)||_op<=5*10^9 C^2 |L-M|.                (E15)

The last bound follows from each Gram entry's bound
2*100*1000200 C^2 |L-M|<3*10^8 C^2 |L-M| and14 entries per row.
Every complete protected source component is retained.

## E5. Explicit finite gate and a frame without a separate Gram solve

In unitary coordinates,

    U_ij(L)=bL integral_0^1 integral_0^1
                  bar(Z_i(L,s))W(L(s-r))Z_j(L,r)dr ds.

Using(E5),(E9), each entry varies at most1000 C^2 |L-M|: the complete
bound is b[125+(101/100)(250+175)]C^2<1000C^2. Therefore
||U(L)-U(M)||_op<20000C^2|L-M|. With B(L)=(15/8)R(L),

    ||[U(L)-B(L)]-S0||_op<2*10^10 C^2|L-1|
                                 <=2*10^24|L-1|.       (E16)

For1<=L<=1+10^-36 the cost is at most2*10^-12. Thus

    U(L)-B(L)>=8*10^-12 I>=epsilon I,
                       epsilon=5*10^-12.               (E17)

The uniform complement gap kappa=6/5 follows from the exact rational
inequality710(10001/10000)^2<72(333/106)^2<72*pi^2, as in the reviewed
open-window proof. The exact coupling gives, for every v in V_L and
z_x=sum_i x_i z_i^L,

    |q_L(v,z_x)|^2<=q_L(v,v) x*B(L)x.                 (E18)

The fourteen vectors Pi_E_L z_i^L automatically span E_L. Otherwise
some x!=0 gives z_x in V_L. It cannot be zero by(E17). Complement
injectivity gives q_L(z_x,z_x)>0; putting v=z_x in(E18) and dividing
forces x*U(L)x<=x*B(L)x, contradicting(E17). Thus every native h has
a decomposition h=z_x+v with v in V_L. Square completion then proves
strict positivity for x!=0, and the complement gap handles x=0.
This argument works for arbitrary complex coefficients and needs neither
an energy-Galerkin solve nor a normalized finite frame away from one.

## E6. Preserve a useful quantitative primitive constant

Equation(E15) and(E3) give trace B(L)<1 throughout the new interval:
its trace variation is at most(15/8)*14*3*10^8 C^2 eta<10^-12.

The unitary native primitive on these tests is

    Gcal_L Z(s)=L integral_0^s cosh(cL(s-r))Z(r)dr.

Its bounded-test operator norm is below2 and its length derivative norm
below3. Hence ||Gcal_L Z_i||<=10C and its length Lipschitz bound is
25C. The complete synthesis trace varies by at most7000C^2|L-1|,
which is below10^-18 on the new interval. The exact(E3) trace then gives

    sum_i ||G_L z_i^L||^2<1.                            (E19)

Thus M=K=1 are valid uniform scalar bounds. With epsilon=1/200000000000,
theta=epsilon/(2M+epsilon)=1/400000000001, weighted Young gives

    q_L(h,h)>=(epsilon/2)||x||^2+theta*kappa||G_Lv||^2.

Since ||G_Lh||^2<=2K||x||^2+2||G_Lv||^2, one may take

    delta=min(epsilon/(4K),theta*kappa/2)
         =1/800000000000.                              (E20)

The previously reviewed exact L1 synthesis bound1/600000000000 and native
zero extension handle all0<L<=1 with this smaller common delta. This proves
(E4). Every source assumption, complete tail, activation cusp and complex
native test remains in scope. The tiny radius reflects deliberately coarse
global coefficient bounds; it makes no claim about an optimal radius or
the possibility of reaching any fixed larger length.
