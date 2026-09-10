# EPD26: exact critical-line source control and the complete prime-discrepancy square

Status: PROPOSED COMPONENT THEOREMS; independent mathematical review pending.
The requested unconditional RH completion is NOT obtained. The missing
subpower upper bound is stated in Section 7, not assumed or certified.
Date: 2026-09-07. Author: Astra. This is new research, not Reviewer D acceptance.
Parent: PR811 at 9e05a2b345369cd16c0973c531650eb37727445e.

## 1. Normalization and the exact field decomposition

Use H=L2(0,infinity), conjugate-linear first inner-product slot,
Lf(z)=integral exp(-zt)f(t)dt, and the boundary norm
||Lf||_H2^2=(1/(2pi)) integral_R |Lf(iy)|^2dy. All convolution is causal.
Write dmu(y)=dy/[pi(1+y^2)], X>=2, L=log X, and Lambda=max(1,L).
The letter Lambda here is a real bandwidth, NOT the von Mangoldt function.
To avoid ambiguity below, von Mangoldt weights are written Lambda_VM(n).

Keep precisely the parent's ordinary-prime completion

    A_X(s)=exp(-gamma) exp(Ein((s-1)L))
                 product_(p<=X)(1-p^-s)^(-1)/(L s^2),
    U_X(y)=log|A_X(1/2+iy)|,
    E(X)=integral (U_X)_+ dmu.                              (1)

Every power of every included prime is present. Put L2=log 2, and define

    B(s)=-gamma-log L2+Ein((s-1)L2)-2log s,
    S_X(s)=sum_(p<=X)p^-s-integral_2^X x^-s/log x dx,
    V_X(s)=sum_(p<=X,k>=2)p^(-ks)/k.                        (2)

On Re s>0 all logarithms have their canonical analytic determination, real
on the positive axis. Direct differentiation of Ein in its cutoff and the
absolutely convergent local Euler logarithms prove

    log A_X(s)=B(s)+S_X(s)+V_X(s).                          (3)

At X=2 the prime-2 atom is fully included in S_X; the integral is zero.
No pole has been introduced at s=1. S_X(1/2+iy) is the Fourier transform of
the real finite signed measure

    dnu_X(r)=sum_(p<=X)p^-1/2 delta_(log p)(dr)
          -exp(r/2)/r 1_[L2,L](r)dr.                      (4)

In particular its frequencies lie in [log 2,L]. Only the first-prime part
has this bandwidth. V_X is NOT called bandlimited.

We use these two source bounds, also proved in EFB26 Sections 3-4:

    |integral U_X dmu|<3,
    integral |Re B(1/2+iy)|dmu<4.                         (5)

For clarity, their ingredients are not RH estimates. The first integral is
log A_X(3/2), by the Cauchy Fourier integral and the finite-u formula for Ein.
It lies between log(2/9) and -log(3/2)+2/log 2. To prove the second bound,
split at |y|=1. The inner part has |Re B|<4 and mu-mass 1/2. On |y|>=1,

    |Re B(1/2+iy)|<=log(3|y|/2)+9/(4|y|).

This follows from E1(w)=exp(-w) integral_0^infinity exp(-u)/(w+u)du for
Im w!=0 and Ein(w)=gamma+log w+E1(w), using real parts. Its full outer
integral is less than 3/2. Thus the total is less than 7/2<4. No finite
frequency cutoff is substituted for the outer integral.

The elementary bound P(X)=sum_(p<=X)1/p<3log(1+L) follows by comparing the
positive Euler logarithm at 1+1/L with zeta(1+1/L)<1+L and e<3.
Since (1-1/sqrt2)^-1<4 and sum_(n>=2)n^-3/2<2,

    sup_y |V_X(1/2+iy)| < (3/2)log(1+L)+3.                 (6)

This pays ALL k>=3 powers by a convergent series, and retains the k=2 term.
The differentiated series similarly gives

    sup_y |V_X'(1/2+iy)| < 2 Lambda^2+24.                  (7)

For k=2 use sum_(p<=X)log p/p<=L(1+L)<=2 Lambda^2.
For k>=3 use 4 sum_(n>=2)log n/n^3/2<24. One direct proof of the latter
sum bound is to write log n=integral_1^n du/u, interchange positive terms,
and bound sum_(n>=max(2,ceil u))n^-3/2<=3/sqrt u.
Also, directly from B',

    sup_y |B'(1/2+iy)|<5,                                (8)

because B'(s)=integral_0^L2 exp((1-s)r)dr-2/s.
Finally put u_X(y)=Re S_X(1/2+iy). By (3)-(6) and
integral |U_X|dmu=2E(X)-integral U_X dmu,

    integral |u_X|dmu < 2E(X)+10+2log(1+L).                (9)

## 2. A frequency-selective derivative estimate, including its constants

The following elementary lemma is for a real finite signed measure nu
supported in [log 2,L], L>=log 2. Put

    S(y)=integral exp(-iyr)dnu(r), u(y)=Re S(y),
    S_z'(y)=-integral r exp(-iyr)dnu(r).

Here S_z' denotes differentiation of the analytic Laplace expression,
not differentiation with respect to the real variable y.

**Lemma EPD26.L1.** With Lambda=max(1,L),

    ||S_z'(y)/(1+iy)^3||_(L2(dy/(2pi)))
        <=24 Lambda^(3/2) integral |u(y)|dmu(y).            (10)

### Proof by one explicit Fourier multiplier

Define eta(r)=0 for r<=1/3, eta(r)=3v^2-2v^3 with v=3r-1 on [1/3,2/3],
and eta(r)=1 for r>=2/3. Define chi(v)=1 for v<=1,
chi(v)=1-3(v-1)^2+2(v-1)^3 on [1,2], and chi(v)=0 for v>=2.
Let

    m_Lambda(r)=-2r eta(r)chi(r/Lambda),
    K_Lambda(y)=(1/(2pi)) integral_R m_Lambda(r)exp(-iyr)dr.
                                                               (11)

The multiplier is C1 and compactly supported, with a piecewise polynomial
weak second derivative in L2. There are no omitted delta terms in m''.
K is in L1, and (1+y^2)K is in L2. On every actual positive frequency in
[log 2,L], m(r)=-2r, and m(-r)=0. It follows, including for atomic nu, that

    K_Lambda*u = S_z'.                                    (12)

The factor two restores the positive-frequency half of the real part.
This is why a lower cutoff, separated from frequency zero, was included.
Fubini is valid because nu has finite total variation and K is in L1.

For every real y,v,

    1+v^2 <= 2(1+y^2)(1+(y-v)^2).

Therefore

    ||K_Lambda(y-v)/(1+iy)^3||_(L2(dy/(2pi)))
      <= [2/(sqrt(2pi)(1+v^2))] ||(1+y^2)K_Lambda||_2.

Minkowski and Parseval give

    ||(K_Lambda*u)/(1+iy)^3||_(L2(dy/(2pi)))
      <= ||m_Lambda-m_Lambda''||_2 integral |u|dmu.        (13)

This remains valid for a bounded, non-L1 function u: the right side uses
its weighted L1 norm, and the preceding kernel majorant is integrable.
The original convolution is also absolutely defined pointwise.

Here is the complete multiplier constant, obtained by integrating its
three polynomial pieces on [1/3,2/3], [2/3,Lambda], [Lambda,2Lambda]:

    ||m_Lambda-m_Lambda''||_2^2
      = (1142/315)Lambda^3+(768/35)Lambda
                       +463514/1215+624/(5Lambda)
      <= (904696/1701)Lambda^3 <576 Lambda^3.              (14)

The last comparison uses Lambda>=1 and all four positive coefficients.
Equation (14) is a continuum identity/inequality, not a sampled multiplier
bound. This proves (10). The code checks the polynomial integrations with
exact rational arithmetic. Fourier inversion, Parseval, and Minkowski are
classical analytic inputs, not consequences of those finite checks.

## 3. Exact critical-line entropy-to-source control: no inward shift

Let w(t)=t^2 exp(-t)/2, so Lw(z)=(z+1)^-3 and ||w||_2=sqrt3/4.
Define the explicit finite-total-variation signed measure

    ell_X(dt)=[exp(t/2)1_[0,L](t)-2exp(-t/2)]dt
          -sum_(p<=X,k>=1)(log p)p^-k/2 delta_(k log p)(dt),
    q_X=w*ell_X.                                         (15)

For each finite X the prime-base set is finite and the k tails converge,
so q_X belongs to L1 intersection L2. In particular causality and H2
membership are established BEFORE estimating the boundary norm.
Its exact transform is

    Lq_X(z)=[partial_s log A_X(s)]_(s=1/2+z)/(z+1)^3.      (16)

**Theorem EPD26.T1.** For every real X>=2,

    ||q_X||_2 < 24 Lambda^(3/2)[2E(X)+10+2log(1+L)]
                                     +Lambda^2+13.        (17)

Apply Lemma L1 and (9) to the S_X part of (3), and (7)-(8) to the rest.
Its latter norm is at most (2Lambda^2+29)sqrt3/4 <Lambda^2+13; one may
use sqrt3<7/4 to verify the last inequality entirely rationally.
Plancherel gives (17). Unlike OEC26.T1, there is NO auxiliary sigma>0.
This does not result from setting sigma=0 in the old bound. It uses the
cutoff's exact first-prime bandwidth and separately pays the unbounded
higher-power frequencies. The price Lambda^(3/2) is explicit.

## 4. Consequence in the original factorial-source domain

For t>=0 retain

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2.

The fractional-part identity g=1-{exp t}+integral_0^t {exp u}du proves
0<g<=1+t. Thus ||d||_1<=6 and ||t d||_2<=sqrt38<7.
Its Laplace formula follows from the floor integral, first in Re z>1/2
then in Re z>0 with the removable pole correctly canceled.

Set y_X=d*q_X and f=-w*(t d). Both are in H. The former lies in the ORIGINAL
closed source domain closure(D H2), and

    y_X(t)=f(t) for almost every 0<t<log X,
    Lf(z)=D'(z)/(z+1)^3,
    ||y_X||_2<=6||q_X||_2, ||f||_2<7.                    (18)

Indeed the uncut logarithmic derivative is the initial Laplace transform of
[exp(t/2)-2exp(-t/2)]dt - sum_(n>=2)Lambda_VM(n)n^-1/2 delta_(log n).
It agrees with ell_X before log X, including all active prime powers.
Laplace uniqueness in the initial absolute half-plane gives
 d*ell=-t d locally. Causality proves (18). No boundary integral is used to
identify a meromorphic quotient with an unproved causal vector.

**Theorem EPD26.T2 (endpoint-depth lower bound).** If rho=beta+i gamma is
ANY nontrivial zeta zero of exact multiplicity m, beta>1/2, let

    lambda=rho-1/2, delta=beta-1/2,
    kappa_rho=(2delta)^(m-1/2)|D^(m)(lambda)|
                           /[(m-1)! |lambda+1|^3]>0.

Then, for EVERY X>=2,

    E(X) >= kappa_rho X^delta/(288 Lambda^(3/2))
                                               -8sqrt(Lambda). (19)

This retains the full horizontal exponent delta, instead of every strictly
smaller exponent. No simplicity or lower bound for zeta^(m)(rho) is assumed.

Proof. Let e_X=y_X-f. Its transform vanishes at lambda through order m-2,
and its (m-1)-st derivative is -D^(m)(lambda)/(lambda+1)^3, because D has
order m there. By (18) e_X is supported after L. Its translated transform
is exp(Lz)Le_X(z). Its jets below m-1 are still zero, so the next jet is
exactly -exp(Llambda)D^(m)(lambda)/(lambda+1)^3, without a polynomial loss.
The unit vector

    v(u)=sqrt(2delta)exp(-conj(lambda)u)L_(m-1)(2delta u)

has inner product of magnitude kappa_rho exp(delta L) with e_X(L+u).
Only its top polynomial coefficient survives the vanishing jets. Laguerre
orthogonality proves ||v||=1; Cauchy--Schwarz and (17)-(18) give

    kappa_rho X^delta
      <=144 Lambda^(3/2)[2E+10+2log(1+L)]+6Lambda^2+85.

Rearranging proves a slightly stronger bound than (19), using
log(1+L)<=sqrt(Lambda) and Lambda>=1. Here
D^(m)(lambda)=(rho-1)zeta^(m)(rho)/rho^2 is nonzero. This is a conditional
obstruction under a hypothetical off-line zero, NOT evidence that one exists.
The construction itself uses no zero data.

## 5. The physical correlations have one exact positive-square factorization

Define, for 1<=x<=X,

    R_X(x)=sum_(max(2,x)<=p<=X)p^-3/2
                 -integral_(max(2,x))^X du/(u^3/2 log u),
    Q(X)=R_X(1)^2+integral_1^X x R_X(x)^2 dx.             (20)

Endpoint values of R at primes do not affect the Lebesgue integral. Its
prime-2 contribution IS included in R_X(1). This R is a weighted signed
tail of the literal prime-counting discrepancy, not its absolute variation.

**Theorem EPD26.T3.** For every X>=2,

    integral [Re S_X(1/2+iy)]^2 dmu(y)=Q(X),             (21)
    E(X) <=5+log(1+L)+(1/2)sqrt(Q(X)).                  (22)

Proof. For r,s>=0 the Cauchy Fourier identity gives

    integral cos(yr)cos(ys)dmu(y)
      =[exp(-|r-s|)+exp(-r-s)]/2
      =exp(-r-s)[1+integral_0^min(r,s) exp(2u)du].      (23)

Apply (23) to the complete real signed measure nu_X in (4). Finite total
variation and compact support justify every exchange of integrals, including
the signed cross terms. The result is

    [integral exp(-r)dnu_X(r)]^2
       +integral_0^L exp(2u)[integral_[u,L] exp(-r)dnu_X(r)]^2du.

Substitute x=exp u to obtain (20)-(21). No product measure on prime phases
is introduced. The kernel is the actual physical one, not the independent
prime gcd kernel. Finally use (3), (5)-(6), Cauchy--Schwarz on the probability
measure mu, and 2E=integral |U|dmu+integral U dmu to obtain (22).
At X=2, Q(2)=5/16 exactly, a normalization check with the full prime-2 atom.

The square in (20) contains all prime-prime, prime-continuum and continuum-
continuum interactions. It does not justify deleting their signs before
forming R_X. Its positivity is NOT an upper bound for its size.

## 6. What the two classical prime-counting estimates actually imply

Put Delta(x)=pi(x)-integral_2^x du/log u, including pi(2)=1.
For x>=2, Stieltjes integration by parts gives

    R_X(x)=X^-3/2 Delta(X)-x^-3/2 Delta(x-)
                      +(3/2)integral_x^X Delta(u)u^-5/2 du.   (24)

The left limit keeps a prime atom at the lower endpoint. Replacing it by
Delta(x) changes one such atom only; we do not silently do so.

### Conditional improvement, under RH only

The classical RH prime error gives |Delta(x)|<=C sqrt(x)log(2x).
For example this follows from |theta(x)-x|<=C sqrt(x)log^2(2x) by partial
summation, with the lower endpoint retained. We use it ONLY in this subsection.
Equation (24) then gives

    |R_X(x)|<=C'[log(2X)/X+(1+log(2x))/x].             (25)

On [1,2], R_X is constant and bounded independently of X by the absolutely
convergent sum/integral in (20). Squaring (25) and integrating x dx yields

    Q(X)=O((1+log X)^3),
    E(X)=O((1+log X)^(3/2)),                           (26)

UNDER RH. The same order bound for |W(X)| follows from the parent's exact
entropy balance. This improves the older conditional logarithmic exponent;
it does not prove RH, simplicity, or a new prime-counting error estimate.
All frequencies in (26) are handled by (21), not by a frequency cutoff.

### Unconditional PNT comparison

The established unconditional PNT bound has
|Delta(x)|<=C x exp(-c sqrt(log x)), after adjustment of constants.
Using (24) with an infinite weighted tail gives

    |R_X(x)|<=C'[x^-1/2 exp(-c' sqrt(log x))
                        +X^-1/2 exp(-c' sqrt(log X))].

The constants exist; they are NOT numerically certified in this packet.
Splitting the integral in (20) at sqrt X proves

    Q(X)=O(1+X exp(-c'' sqrt(log X))),
    E(X)=O(1+sqrt X exp(-c''' sqrt(log X))).            (27)

These are classical-scale bounds. They still retain a positive power of X.
No new unconditional zero-free region or endpoint upper bound results.

## 7. Exact remaining completion obligation

A sufficient theorem is an unbounded sequence X_j with

    log(1+Q(X_j))/log X_j ->0.                         (OPEN)

Indeed (22) gives subpower E on that sequence, contradicting (19) for every
hypothetical beta>1/2. The functional equation excludes beta<1/2 as well.
Then the original Hardy source domain is complete by its inner-factor
classification. Conversely RH implies (OPEN) by (26). This is in the
classical mean-square prime-error/Hardy criterion lineage, not a claim that
this restatement lowers the intrinsic arithmetic difficulty.

Neither (OPEN) nor the less restrictive direct entropy/work bound is proved
here. Section 6 and ATTEMPT.md show the exact upper estimates actually paid.
The endpoint transfer (17) closes the inward-shift issue, but not the
arithmetic estimate. Independent review should validate these component
proofs; it is not being asked to invent an omitted proof of (OPEN).
