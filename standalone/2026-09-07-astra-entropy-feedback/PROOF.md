# EFB26: an exact critical-line entropy balance

Status: PROPOSED COMPONENT PROOFS; independent mathematical review pending.
The requested full RH proof is NOT obtained. The signed-work upper estimate
in Section 6 is unproved. This manuscript must not be submitted as a proof
of RH. Author: Astra. Date: 2026-09-07.
Scope: the unchanged ordinary-prime completion of PR811, at Re(s)=1/2;
every real cutoff X>=2 and the entire Cauchy-weighted frequency line.

## 1. Fixed source and the claim actually proved

Use dmu(y)=dy/[pi(1+y^2)]. This probability measure is not a product measure
on prime phases. All logarithms of positive real numbers are natural. Set

    A_X(s)=exp(-gamma) exp(Ein((s-1)log X))
                  product_(p<=X)(1-p^-s)^(-1)/[(log X)s^2],
    Ein(w)=integral_0^w (1-exp(-v))/v dv,
    U_X(y)=log|A_X(1/2+iy)|,
    E(X)=integral (U_X(y))_+ dmu(y).                      (1)

At an included prime all powers of that prime are present. Let U_(x-)
use the same continuum cutoff x but primes p<x. At nonprime x this is U_x.
Let U_* denote the field at cutoff 2 BEFORE its prime-2 jump. Define

    F(x)=integral tanh(U_(x-)(y)) cos(y log x) dmu(y),
    W(X)=sum_(p<=X) F(p)/sqrt(p)
                -integral_2^X F(x)/(sqrt(x)log x) dx.    (2)

This is a real, completely specified nonlinear observable of the actual
prime trajectory. In particular |F(x)|<=1. It has not been replaced by a
random-prime expectation, a chosen sign, or a freely optimized dual vector.

**Theorem EFB26.T1.** For all real X>=2,

    |2E(X)-W(X)| < 8+24 log(1+log X).                    (3)

A stronger accounting underlying (3) is given in Sections 3-4. Every
nonlinear jump remainder and every higher prime power is paid by a uniform
O(log log X) budget. The term W is NOT bounded subpower by this theorem.
No PNT, zero census, RH, or prime-correlation estimate is used in (3).

Classical ingredients (Euler's product, the Cauchy Fourier integral, and
Taylor's theorem) are used below with their needed calculations. This is
an explicit source application, not a novelty claim for convex calculus.

## 2. Exact path as the cutoff increases

For a prime p put r_p=p^-1/2 and

    j_p(y)=-log|1-r_p exp(-iy log p)|
          =sum_(k>=1) r_p^k cos(k y log p)/k.            (4)

The series is absolutely and uniformly convergent for each p. Direct
cutoff differentiation, before taking any bound, gives

    U_X(y)=U_*(y)+sum_(p<=X)j_p(y)
                  -integral_2^X x^-1/2 cos(y log x)/log x dx.
                                                               (5)

Indeed d/dx[Ein((s-1)log x)-log log x]=-x^-s/log x.
There is no missing unit contact or half-weight at prime 2. At a composite
prime power the dependence on cutoff is continuous: its base was already
included, and its k-th harmonic already occurs in (4).

For each fixed bounded cutoff interval, U_X-U_* is uniformly bounded in y.
The initial field is Cauchy-integrable, as is proved in Section 4. Thus all
quantities used here are integrable on the COMPLETE frequency line.
Differentiation on a prime-free x interval is justified by the integrable
majorant x^-1/2/log x, since the nonlinear derivative below is bounded by 1.
There are only finitely many prime jumps up to any X. These observations
justify the cutoff integrals and changes of order, with no asymptotic limit.

## 3. Convex jump accounting, including all higher powers

Put f(u)=log cosh u and S(X)=integral f(U_X)dmu; similarly define S_*.
Then f'=tanh, 0<f''=sech^2<=1, and

    0<=|u|-f(u)<=log 2.                                (6)

Taylor's theorem in integral form, valid for positive OR negative j, gives

    R(u,j)=f(u+j)-f(u)-tanh(u)j
          =j^2 integral_0^1 (1-t)sech^2(u+t j)dt,
    0<=R(u,j)<=j^2/2.                                  (7)

Applying (7) at each prime and the ordinary chain rule between primes yields

    S(X)=S_*+W(X)+R_pow(X)+R_curv(X),                  (8)

where the exact remainders are

    R_pow=sum_(p<=X) integral tanh(U_(p-))
                          [j_p-r_p cos(y log p)]dmu,
    R_curv=sum_(p<=X) integral R(U_(p-),j_p)dmu.         (9)

In particular R_curv is nonnegative, but R_pow may have either sign.
For 0<r<=1/sqrt(2), the full logarithmic series proves pointwise

    |j-r cos theta|<=r^2/[2(1-r)],
    |j|<=r/(1-r).                                     (10)

The first estimate retains the COMPLETE k>=2 series: 1/k<=1/2 there.
Write P(X)=sum_(p<=X)1/p and a=1/(1-1/sqrt(2))=2+sqrt(2).
Equations (7)-(10) imply

    |R_pow|<= (a/2)P(X) <2P(X),
    0<=R_curv<= (a^2/2)P(X),
    -2P(X)<R_pow+R_curv<8P(X).                         (11)

For the last upper constant, (a+a^2)/2=4+(5/2)sqrt(2)<8.
No claim that j_p itself is everywhere positive has been used.

The prime harmonic sum needs only an elementary bound. For L=log X,
put q=1+1/L. Since p^(1/L)<=e for p<=X, the positive Euler expansion and
a decreasing integral comparison give

    P(X)<=e sum_p p^-q <=e log zeta(q)
         <3 log(1+L).                                 (12)

Here zeta(q)<1+1/(q-1)=1+L and e<3. This is not an imported PNT error bound.
Equations (8)-(12) are the full nonlinear remainder estimate.

## 4. Signed mean, initial data, and the explicit constant in (3)

The elementary Cauchy identities are

    integral cos(vy)dmu(y)=exp(-|v|),
    integral log|b+iy|dmu(y)=log(b+1),        b>0.       (13)

The first follows by residues in the upper/lower half-plane. For the second,
differentiate in b, evaluate the rational integral to get 1/(b+1), and fix
the constant at b=1 by y=tan theta and the integral of log cos theta.
The latter integral follows by doubling theta and symmetry, so (13) does
not require an unproved boundary continuation of the Euler product.

Apply (13) termwise to the absolutely convergent prime logarithms. For Ein,
use its finite real-u integral and split 1-exp(u/2)cos(yu) into
1-exp(u/2) and exp(u/2)(1-cos(yu)); the second term is nonnegative, and its
Cauchy mean is exp(u/2)(1-exp(-u)). This also justifies integrability near u=0.
It follows directly that

    m_X:=integral U_X dmu=log A_X(3/2),
    |m_X|<3.                                         (14)

For clarity the bound in (14) uses

    log(2/9)<m_X<-log(3/2)+2/log 2<3,

and log(2/9)>-2. This follows from 1<Z_X(3/2)<3 and
0<E1((log X)/2)<2/log 2, with
E1(w)=Ein(w)-gamma-log w. Both estimates concern the safe real line.

Here is a complete bound for the initial frequency tail: S_*<4.
Let L0=log 2, so 2/3<L0<7/10. For |y|<=1, write U_* using (1) with
no prime factor. We have 0<gamma<1, |log L0|<1/2,
2|log|1/2+iy||<7/5, and

    |Re Ein((-1/2+iy)L0)|
       <=sqrt(2)[L0/2+y^2 L0^2/4]<1.

Thus |U_*|<4 there, contributing less than 2 to its weighted integral.
For |y|>=1, the real parts of the two logarithms satisfy
log|s-1|=log|s| on Re s=1/2. Therefore

    U_*(y)=-log|1/2+iy|+Re E1((-1/2+iy)L0),
    |U_*(y)|<=log((3/2)|y|)+9/(4|y|).                 (15)

The E1 estimate follows from
E1(w)=exp(-w) integral_0^infinity exp(-u)/(w+u)du for Im w!=0.
The entire outer-frequency integral is less than

    2/pi + (1/2)log(3/2) + (9/(4pi))log 2 <3/2.

The first term bounds the log|y| integral using (1+y^2)^-1<=y^-2.
Consequently integral |U_*|dmu<7/2<4 and S_*<4.

Finally let chi_X=integral[|U_X|-f(U_X)]dmu, so 0<=chi_X<=log 2<1.
The identity u_+=(|u|+u)/2 gives

    2E(X)=m_X+S_*+W(X)+R_pow(X)+R_curv(X)+chi_X.       (16)

Together with (11), (12), and (14), this proves (3), with every additive
constant and every nonlinear prime contribution accounted for.

### A small actual-source lower check (not a growth theorem)

For 0<=y<=1/4 at X=2, use |s|^2<=5/16, gamma<1,
Re Ein>=-sqrt(2)L0/2>-21/40 and -log L0>0. Also
cos(yL0)>=1-(7/40)^2/2 and sqrt(2)>7/5 give

    |1-2^(-1/2-iy)|^2 <=1943/16000<1/8.

Thus j_2>(1/2)log 8>1 and -2log|s|>=log(16/5)>1,
so U_2(y)>19/40. Since arctan(1/4)>=4/17 and pi<4,

    E(2)>19/340>1/20.                                (17)

The parent's complete upper estimate is E(2)<4. This sanity check excludes
an accidental zero returned by a quadrature that misses the central interval.
No general entropy bound is inferred from this single cutoff.

## 5. Bounded feedback and what its positivity does not say

There is an exact alternative description of the feedback:

    q_x(y)=|A_(x-)(1/2+iy)|^2/[1+|A_(x-)(1/2+iy)|^2],
    0<q_x<1,
    F(x)=-1/x+2 integral q_x(y)cos(y log x)dmu(y).       (18)

It follows from tanh(log r)=(r^2-1)/(r^2+1) and (13). The kernel

    K_x(u,v)=integral q_x(y)exp(iy(u-v))dmu(y)

is positive semidefinite on every finite packet. But F(x) uses a signed
OFF-DIAGONAL correlation and a subtraction. This positive kernel is not the
critical Xi Pick kernel and supplies no decay bound for F(x).
The deterministic -1/x contribution to (2) is absolutely bounded, since
sum p^-3/2 and integral_2^infinity x^-3/2/log x dx converge. The unresolved
work is thus in the bounded, saturated correlation in (18), not a divergent
normalization term.

The construction also works for fixed b>1/2, replacing p^-1/2,x^-1/2 by
p^-b,x^-b. Its nonlinear remainder is bounded by 8 sum_p p^-2b, uniformly
in X; the initial and mean constants depend on b. The critical case above
is exactly where this uniform bound becomes O(log log X). No continuation
below b=1/2 is asserted with the same budget.

## 6. The full intended conclusion, and the missing theorem

An adequate upper estimate would be

    W(X)<=C_epsilon X^epsilon for every epsilon>0,     (OPEN)

or such estimates along one unbounded subsequence with exponent tending to
zero. By (3) these imply the corresponding subpower bound for E(X).
The frozen parent OEC26.T3 proves that any zero beta>1/2 forces
E(X)>=c X^nu-C for every 0<nu<beta-1/2 and all X>=2, including multiplicity.
Thus (OPEN), followed by that proved conditional deduction and reflection,
would establish RH and the original source-domain completion.

Under RH, the parent's supplied conditional bound E(X)=O((1+log X)^3)
and (3) give W(X)=O((1+log X)^3). This converse is CONDITIONAL and is not
used as an upper bound in this manuscript's unconditional work.

Equation (3) itself yields only a LOWER bound W(X)>-8-24log(1+log X).
From |F|<=1 one obtains merely

    |W(X)|<=sum_(p<=X)p^-1/2+integral_2^X x^-1/2/log x dx
          <5 sqrt(X).

The constant 5 follows from sum_(n<=X)n^-1/2<2sqrt X and log 2>2/3.
This is not a subpower estimate. The parent's classical PNT-scale entropy
bound gives a smaller classical-scale upper bound but still no fixed-power
breakthrough. No new unconditional zero-free region is established here.

ATTEMPT.md identifies the specific failed final inference. The component
proofs above settle the nonlinear/higher-power accounting, not the signed
arithmetic upper bound. Independent review should not be asked to supply it.
