# Continuum subtraction in the original heat-Hankel metric

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
The unrestricted arithmetic positivity assertion and RH are NOT proved.
Scope: L2(0,infinity), its original metric, every prime power, arbitrary
finite test dimension, and arbitrary simultaneous cutoff/capture schedules.
Base: PR #790 at c64a0ae131d60cce48bc0dcc73358f7a1a857a89.
Local labels ASTRA-OR-01 through 05 have no canonical-registry status.
No external novelty or priority claim. This is not a new PNT error estimate.

## 1. Normalization and the actual completion attempted

Let d=1/4, A_rho=rho(1-rho), with all upper-half-plane nontrivial zeros
and their multiplicities, S(v)=sum_rho exp(-A_rho v), and
Gamma(s,t)=S(s+t). Put

    Omega(x)=Re digamma(1/4+i x/2)-log pi,
    k_l(v)=sqrt(pi/v) exp(-v/4-l^2/(4v)),       v>0,l>=0,
    K_l(s,t)=k_l(s+t).

The Fourier convention is ghat(l)=int_R g(x)exp(-ilx)dx. For real test
functions f,g put R_f(z)=int_0^infinity exp(-zt)f(t)dt. On compactly
supported smooth tests in (0,infinity),

    <f,K_l g>=int_R R_f(x^2+d)R_g(x^2+d)cos(lx)dx.

Complexification uses the corresponding Hermitian polarization. The
operators K_l have real symmetric kernels; they are not asserted positive.

Let Psi(x)=sum_(n<=x) Lambda(n) be RIGHT-CONTINUOUS, with full mass at an
integer cutoff, and E(x)=Psi(x)-x+1. Thus E(1)=0. Set

    P_X=sum_(2<=n<=X) Lambda(n)n^(-1/2) K_(log n),
    C_X=int_1^X x^(-1/2) K_(log x)dx,
    Delta_X=P_X-C_X.                                      (1)

These are genuine bounded trace-class operators for every finite X>=1.
The continuous term is exact, not a probabilistic model for the primes.
The intended completion was to subtract the entire continuum contribution,
prove an all-rank error estimate in the ORIGINAL metric, then prove
positivity of the remaining balanced finite operators. The first two steps
are proved below; the final sign is not.

## 2. ASTRA-OR-01: trace-norm bounds for each Gaussian prime atom

For every l>=1,

    ||K_l||_1 <16 sqrt(l) exp(-l/2),
    ||dK_l/dl||_1 <90 sqrt(l) exp(-l/2).                    (2)

Consequently, with L_l=exp(-l/2)K_l,

    ||L_l||_1 <16 sqrt(l)exp(-l),
    ||L'_l||_1 <100 sqrt(l)exp(-l).                         (3)

All derivatives in (2)--(3) are in trace norm on l>0. In particular,
these are operator bounds, not estimates only on one trial function.

### Proof by a shifted Fourier contour

Fix 0<=y<1/2 and write z=x+iy, a=1/4-y^2, lambda=z^2+1/4, alpha=Re lambda
=x^2+a>0. The Gaussian contour identity is

    k_l(v)=exp(-yl) int_R exp(ilx)exp(-lambda v)dx.           (4)

The kernel exp(-lambda(s+t)) is rank one, with trace norm 1/(2alpha).
The integral is absolutely convergent in trace norm, so

    ||K_l||_1 <=pi exp(-yl)/(2sqrt(a)).                      (5)

The pointwise Gaussian contour can first be shifted at v>0, then the
absolutely convergent rank-one integral identifies the bounded operator.
No convergence at the single corner s+t=0 is assumed.

A naive differentiation of (4) introduces z and loses absolute nuclear
integrability. One integration by parts in x repairs that loss. Since

    d/dx [z exp(ilz-lambda v)]
        =[1+ilz-2z^2v]exp(ilz-lambda v),

we obtain, for l>0,

    k'_l(v)=exp(-yl)/l int_R exp(ilx)
                        [2z^2v-1]exp(-lambda v)dx.          (6)

The kernel v exp(-lambda v) is the sum of the two rank-one kernels with
one factor t exp(-lambda t). Its trace norm is at most
sqrt(2)/(2alpha^2)<1/alpha^2. Thus (6) gives

    ||K'_l||_1 <= pi exp(-yl)/l
                    [3/(2sqrt(a))+y^2/a^(3/2)].            (7)

Here int_R (x^2+y^2)/(x^2+a)^2 dx
=pi/(2sqrt(a))+pi y^2/(2a^(3/2)). Every term is integrable.
For trace-norm differentiability, truncate the x integral in (4), apply
(6), and pass to the limit uniformly on compact positive l intervals.
The integrated boundary term z exp(-lambda(s+t)) has trace norm O(1/|x|)
and tends to zero. This also justifies the operator integration by parts.
The value of y is fixed during this differentiation; it may be chosen as
a function of l only AFTER (5) and (7) have been established pointwise.

Choose y=1/2-1/(l+2). Then a=(l+1)/(l+2)^2 and, for l>=1,

    1/a<=6l,       exp(-yl)<3exp(-l/2).

Using pi<4 and sqrt(6)<5/2, (5) is strictly less than
15sqrt(l)exp(-l/2). Equation (7) is strictly less than
45(l^(-1/2)+l^(1/2))exp(-l/2), hence less than the second bound in (2).
Finally exp(-l/2)(K'_l-K_l/2) proves (3), since 90+16/2<100.

K_l is also trace-norm continuous at l=0: use the unshifted representation
and dominated convergence with majorant 1/[2(x^2+1/4)]. No trace-norm
right derivative at zero is used in the argument. This suffices for C_X
as a finite Bochner integral starting at x=1.

An exact normalization, useful independently of these inequalities, is

    Tr K_l=pi exp(-l/2),   l>=0.                            (8)

Indeed Tr K_l=(1/2)int_0^infinity k_l(v)dv. The Gaussian Laplace integral
gives (8). Equivalently integrate 1/[2(x^2+1/4)] against cos(lx).

## 3. ASTRA-OR-02: the complete balanced arithmetic tail, uniformly in rank

Put rho(x)=|E(x)|/x. For X>=3 define the actual-source bound

    B_X=16 sqrt(log X) rho(X)
          +100 int_(log X)^infinity sqrt(v)rho(exp v)dv.    (9)

Then Delta_X has a limit Delta in TRACE NORM, and

    ||Delta-Delta_X||_1 <= B_X,              B_X ->0.        (10)

### Proof with the lower-boundary term retained

For 3<=X<Y, Stieltjes integration by parts in the Banach space of
trace-class operators gives exactly

    Delta_Y-Delta_X
      =E(Y)L_(log Y)-E(X)L_(log X)
                     -int_X^Y E(x)L'_(log x)dx/x.           (11)

The atom at X is excluded on the left; E(X) is its right-continuous value.
This is why the boundary sign and full integer mass matter. One can first
verify (11) on finite sums plus the ordinary continuous integral, so no
operator-valued measure theorem beyond Bochner integration is needed.

The classical quantitative PNT supplies C,c>0 such that

    rho(exp v)<=C exp(-c sqrt(v)),                v>=1.    (12)

The +1 in E and the change from half-weight to right-continuous Psi are
absorbed by enlarging C and, if necessary, reducing c to at most one.
This imports the classical unconditional estimate, not RH or a new prime
power saving. No numerical values for C,c are certified in this packet.
Equations (3) and (12) make the operator integral in (11) absolutely
convergent in trace norm and make the upper-boundary term tend to zero.
Taking Y to infinity proves (10), with exactly (9).

For explicit dependence on any supplied valid PNT constants, let l=log X.
Then

    B_X <= C exp(-c sqrt(l))
      [16sqrt(l)+200(l/c+2sqrt(l)/c^2+2/c^3)].               (13)

This follows by substituting w=sqrt(v) in (9) and integrating w^2exp(-cw).
It is an effective expression conditional on valid explicit constants,
not a claim that such constants were computed here.

For ANY finite real packet f_1,...,f_N, with G_ij=<f_i,f_j>, define the
residual-tail matrix by D_ij=<f_i,(Delta-Delta_X)f_j>. Then

    -B_X G <= D <= B_X G.                                  (14)

The same bound works for every N and every choice of signed coefficients.
No factor depending on dimension, exponent order or Gram conditioning is
hidden in (14). Numerical errors in the entries are a separate matter.

## 4. ASTRA-OR-03: an arithmetic-only construction of the full operator

The continuum kernel is elementary. Writing v=s+t, l=log X,

    C_X(v)=pi[erf((l-v)/(2sqrt(v)))+erf(sqrt(v)/2)],
    C_infinity(v)=pi[1+erf(sqrt(v)/2)],
    C_>X(v)=pi erfc((log X-v)/(2sqrt(v))).                   (15)

Complete the square in the l integral in (1) to prove these identities.
C_infinity and C_>X are NOT bounded operators on all L2: their kernels
tend to 2pi as v tends to infinity. Their use below is initially as forms
on integrable, compactly supported tests. We never subtract two purported
bounded operators represented by these unbounded kernels.

Define the trace-class base operator

    B(s,t)=(1/(4pi))int_R [Omega(x)+1/(x^2+1/4)]
                                  exp(-(x^2+1/4)(s+t))dx. (16)

The absolute trace-norm integral is finite since Omega is bounded near
zero and Omega(x)=log(|x|/(2pi))+O(1/|x|) at infinity. This uses only the
classical digamma estimates. The identity

    int_R exp(-(x^2+1/4)v)/(x^2+1/4)dx
                         =2pi erfc(sqrt(v)/2)              (17)

also follows by differentiation in v and the limit at infinity. Thus B
is the archimedean Gaussian integral divided by 4pi plus half the erfc
Hankel kernel. B need not be positive.

Now define, entirely from arithmetic and the stated PNT input,

    Gamma_X^bal = B-Delta_X/(2pi),
    Gamma^arith = B-Delta/(2pi).                            (18)

Both are trace-class self-adjoint operators and

    ||Gamma_X^bal-Gamma^arith||_1 <= B_X/(2pi) ->0.           (19)

The UNCONDITIONAL explicit formula identifies Gamma^arith with the
original Gamma_0(s,t)=S(s+t). To check this identity without a formal
subtraction of divergent operators, take v>0. The prime Gaussian series
converges absolutely, the continuum integral in (15) converges, and the
heat explicit formula is

    S(v)=1+(1/(4pi))int_R exp(-(x^2+1/4)v)Omega(x)dx
                          -(1/(2pi))sum_n Lambda(n)n^-1/2 k_(log n)(v).

Substitute Delta(v)=P_infinity(v)-C_infinity(v) and (15)--(17).
This proves (18)'s kernel identity pointwise at v>0. Finite kernels converge
uniformly on compact v intervals away from zero; trace-norm convergence
also gives Hilbert-Schmidt convergence, identifying the kernels almost
everywhere. Existence and trace-norm convergence of (18) did not use a
hypothetical zero set, a zero census, or the parent positivity claims.

For real integrable compactly supported f,g, the corresponding complete
prime-tail approximation is

    P_>X(f,g) = C_>X(f,g) + <f,(Delta-Delta_X)g>,
    |P_>X(f,g)-C_>X(f,g)| <= B_X ||f||_2 ||g||_2.           (20)

Formula (20) keeps the entire continuum endpoint mode exactly. It is a
uniform signed MATRIX approximation, not a proof that either term is a
positive or negative form. After this correction the remainder extends
continuously to all L2, as (10) specifies.

Equivalently the renormalized full prime form has a bounded trace-class
extension on L2:

    P(f,g)-2pi(int f)(int g)
      =<f,[A_Gamma/2-2pi Gamma_0]g>,                        (21)

where A_Gamma has kernel int_R Omega(x)exp(-(x^2+1/4)(s+t))dx.
The two integrals on the left are initially defined on the stated core.
Equation (21) does NOT assert that int f is continuous on L2. The extension
is the bounded operator on the right, not either unbounded term separately.
This is the operator-level version of the endpoint correction in pass8.

## 5. Exact finite-source compiler and trace check

Let s=1/2+sqrt(u+1/4)>1 for u>0. The Laplace transform of the balanced
kernel is

    h_X^bal(u) = 1/(2s-1) * [1/s + (1-X^(1-s))/(s-1)
              -(log pi)/2 + digamma(s/2)/2
              -sum_(2<=n<=X) Lambda(n)n^-s].                (22)

At s=1 the quotient has the removable value log X. To derive (22),
start with the parent's Euler/gamma source truncated at X. The exact
continuum tail has Laplace transform

    int_0^infinity exp(-uv) C_>X(v)dv/(2pi)
                  =X^(1-s)/[(2s-1)(s-1)].                  (23)

This follows either by Tonelli for the positive Gaussian scalar kernel
or by int_0^infinity exp(-uv)k_l(v)dv
=pi exp(-sqrt(u+1/4)l)/sqrt(u+1/4). Subtraction gives (22), including the
removed s=1 pole. No infinite prime tail is discarded.

Every exponential-test matrix is compiled by

    Q_X(p,q)=[h_X^bal(p)-h_X^bal(q)]/(q-p),
    Q_X(p,p)=-(h_X^bal)'(p),                                (24)

and confluent derivatives give every exponential-polynomial entry.
The original factorial L2 Gram is unchanged. Equation (19), not a
coefficientwise guess, pays the infinite arithmetic tail at every rank.

There is an exact trace normalization:

    Tr Delta_X=pi[sum_(2<=n<=X) Lambda(n)/n-log X],
    Tr Gamma_X^bal=1/2-gamma_E/4-log(4pi)/4
                          -(1/2)[sum_(n<=X)Lambda(n)/n-log X]. (25)

The first follows from (8). The second follows by taking the removable
u=0 value of (22) and dividing by two; trace equals half the integral of
these trace-class Hankel kernels. The absolute rank-one integral justifies
this operation, and digamma(1/2)=-gamma_E-2log2 fixes the constant.

Quantitative PNT implies that the bracket in (25) tends to -gamma_E.
For completeness, it has a limit by integration by parts with Psi(x)-x
and (12). The Mellin identity

    -zeta'/zeta(1+z)=(1+z)int_1^infinity Psi(x)x^(-2-z)dx

and -zeta'/zeta(1+z)=1/z-gamma_E+O(z) identify that limit as -gamma_E.
Consequently Tr Gamma^arith=[1+gamma_E/2-log(4pi)/2]/2, exactly the
parent's H/2, with an independent arithmetic convergence argument.

## 6. ASTRA-OR-04: arbitrary simultaneous cutoff and quadratic capture

Let Pi_r be the original-metric projection onto
E_(r+2,d_r), with d_r/r^2->c in (0,infinity), and a=1/(2c).
The pass8 strong projection theorem is an EXPLICIT dependency here.
For EVERY sequence X_r>=3 tending to infinity,

    ||Pi_r Gamma_(X_r)^bal Pi_r-P_a Gamma_0 P_a||_1 ->0.   (26)

There is NO required relation between X_r and r. Proof: the difference
from Pi_r Gamma_0 Pi_r is at most B_(X_r)/(2pi) by (19); the latter
compression converges in trace norm by the parent theorem and trace-class
compactness. This restores arbitrary simultaneous schedules for the
CONTINUUM-CORRECTED form. It does not restore that assertion for an
uncorrected prime tail or permit dropping the endpoint.

At d_r=r^2, the nonzero part of the limit is unitarily equivalent to
Gamma_1. In particular negative traces converge. For finite Gram matrices
Q_(X,r),Q_r and the exact metric G_r,

    -(B_X/(2pi))G_r <= Q_(X,r)-Q_r <= (B_X/(2pi))G_r.       (27)

The constants do not depend on their size r^2+1. This pays the entire
arithmetic truncation error in the physically relevant nonescaping regime.
It does NOT prove Q_(X,r)>=-eta_r G_r with eta_r->0.

## 7. ASTRA-OR-05: the attempted final positivity step fails as stated

Subtracting the continuum does NOT make every finite arithmetic cutoff
positive. This fails on the actual source, not just on synthetic data.
At X=2, (25) gives

    Tr Gamma_2^bal = [2-gamma_E-log(2pi)]/4 <0.             (28)

Indeed gamma_E>1/2 and log(2pi)>3/2 suffice. More strongly the single
literal test f(t)=exp(-2t) has exactly

    <f,Gamma_2^bal f>
      =[17/4-gamma_E-log(4pi)-pi^2/8-(3/4)(log2)^2]/27
      < -13/3240 <0.                                      (29)

Differentiate (22) at u=2 (so s=2), using digamma(1)=-gamma_E and
trigamma(1)=pi^2/6, to obtain the equality. The inequality uses only

    gamma_E>1/2, log(4pi)>12/5, pi>3, log2>2/3.

For explicit elementary certificates, e<11/4 and (11/4)^12<12^5 imply
log12>12/5; pi>3 then gives log(4pi)>12/5. Also (11/4)^2<8 gives
log2>2/3. The bound gamma_E>1/2 follows from
H_6-log7<gamma_E and exp(39/20)>7, where the latter is witnessed by a
finite positive exponential series; H_6=49/20. These are checked in
verify.py as exact rational inequalities. No floating-point special
function value is needed for (28)--(29).

The negative trace is not merely one off-metric raw-matrix artifact.
The real spectral density of this balanced cutoff is

    w_X(x)=Omega(x)+1/(x^2+1/4)
      -2sum_(n<=X) Lambda(n)n^-1/2 cos(xlog n)
      +2int_1^X u^-1/2 cos(xlog u)du.                      (30)

At X=2,

    w_2(0) < -1-14/15+12/7 = -23/105 <0,                 (31)

using Omega(0)<-5, sqrt2<10/7 and log2>2/3. Omega(0)<-5 follows from
its exact quarter-argument value and the same elementary bounds.
By continuity there is a negative interval. At infinity w_2(x) is
positive eventually, since Omega grows logarithmically and the other
terms are bounded. Its signed Laplace measure is absolutely integrable
with weight 1/lambda. The elementary density of rational Laplace
polynomials in L2 of that weighted measure then gives infinitely many
negative and positive directions, as in the parent's cutoff-index proof.
Multiplication by exp(-tau lambda) preserves these signs for every fixed
thermal shift tau>=0. This assertion concerns Gamma_2^bal, NOT Gamma_0.
The explicit test (29) already suffices to reject universal cutoff PSD.

The contemplated completion was to infer the desired sign from (19) and
a proposed universal positivity of Gamma_X^bal. Equation (29) refutes
that proposed positivity. Nothing here refutes positivity at a suitable
cofinal subsequence or a different compensated approximation. Establishing
an arithmetic bound on its negative part along such a subsequence would
be a new theorem; it has not been supplied.

What remains is still the literal full-source sign. The PNT estimate controls
the distance from a balanced arithmetic cutoff to Gamma_0; it does not
orient Gamma_0. At square width a bound Q_(X_r,r)>=-eta_r G_r, eta_r->0,
would combine with (27) and (26) to finish RH through the parent's exact
inertia theorem. Neither (12), the positive limiting trace, nor the
endpoint correction proves that inequality. No full completion is claimed.
