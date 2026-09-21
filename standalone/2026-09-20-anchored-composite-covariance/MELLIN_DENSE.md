# DMC31: a complete dense-covariance estimate above a Mellin cutoff

**Status: proposed component proof; independent mathematical review required.**
**The native low-Mellin remainder and RH are not proved here.**
Date: 20 September 2026. Additive continuation of ACC29/SFC30 on draft #905,
read at `dfd20b6a778941a3d0c5f671ba840a6b35e4d36e`.

This estimates a projection of the COMPLETE signed composite sum, including
all dense mixed-prime interactions. There is no bounded-partner-degree
hypothesis. It is not an estimate for the unprojected complete sum, nor for
every separately selected denominator subset. The new projection is in the
Mellin variable conjugate to log(x), NOT the reduced rational angle a/q in
NCL29. The two projections must not be silently identified or commuted.

The argument combines exact source algebra, elementary multiplicative
collision counting and mean values, a continuous Hardy isometry, and the
IMPORTED explicit Patel--Yang sub-Weyl theorem. It proves no new zeta
subconvexity estimate. External novelty of this application is not certified.

## 1. Source and complete covariance

Let c be a finite real source supported in 1,...,L, L>=2, satisfying

    |c(n)| <= K,       C(1)=sum_n c(n)/n=0.

Put N=L^2, z=c*c (Dirichlet convolution),

    C(s)=sum_n c(n)n^(-s),
    B_q=sum_(q|n) z(n)/n,
    r_q(k)=-sum_(d|q) mu(q/d)(k mod d),      q>=2.

Every source term and denominator through N is retained. ACC29's exact
anchored formula is

    P(k)=sum_(q>=2) B_q r_q(k)=sum_n z(n) floor(k/n),
    V(k)=2 A_c(k)-P(k).                                      (1.1)

For completeness, r_q=sum_(d|q)mu(q/d)d floor(k/d), since
sum_(d|q)mu(q/d)=0. Divisor inversion gives the second expression for P;
the q=1 term is zero because B_1=C(1)^2=0.

Extend P to x>0 by its same floor expression. It is zero for 0<x<1 and
bounded: sum z(n)/n=0 cancels the linear parts of all floors. Thus

    ||P||_ph^2 := integral_0^infinity |P(x)|^2 dx/x^2
                =sum_(k>=1) |P(k)|^2/[k(k+1)].               (1.2)

In particular this is the full physical norm, not a period average, a
finite annulus, or the diagonal of the denominator covariance matrix.

### Exact Mellin transform

For Re(s)>1, integrating each floor gives

    integral_0^infinity P(x)x^(-s-1) dx = zeta(s) C(s)^2/s.  (1.3)

The left side is holomorphic on Re(s)>0 because P is bounded and vanishes
below 1. The right side has a removable singularity at s=1: C has a zero
there and C^2 has at least a double zero. Analytic continuation proves (1.3)
throughout Re(s)>0, with removable values understood. In particular

    integral_0^infinity P(x) dx/x^2 = 0.                     (1.4)

Write s=1/2+it. Apply Fourier Plancherel to
F(u)=exp(-u/2)P(exp(u)). With the convention hat F(t)=integral F(u)e^(-itu)du,

    ||P||_ph^2 = (1/(2pi)) integral_R
          |zeta(1/2+it)|^2 |C(1/2+it)|^4/(1/4+t^2) dt.     (1.5)

The bounded floor source justifies the transform and Plancherel directly.
All denominators were summed BEFORE the absolute square. Their complete
signed covariance is therefore still present in (1.5).

An independently testable finite version of the transform algebra is

    J_w(q)=sum_(d|q)mu(q/d)d^w,
    sum_(q>=2) B_q J_(1-s)(q)=C(s)^2.                       (1.6)

This is an identity of finite Dirichlet polynomials. Its coefficient at
n^(-s) is n sum_(q:n|q) mu(q/n)B_q=z(n), including n=1.

## 2. A source-adaptive fourth-moment bound with complete off-diagonal cost

Define the exact, nonnegative source moments

    M_0=sum_(n<=N) z(n)^2/n,       M_1=sum_(n<=N) z(n)^2,
    H_m=sum_(n=1)^m 1/n.

For every R>0,

    integral_R^(2R) |C(1/2+it)|^4 dt
           <= R M_0 + 6 H_N M_1.                           (2.1)

Indeed C(s)^2=sum z(n)n^(-1/2-it). The integrated diagonal is R M_0.
The magnitude of each off-diagonal exponential integral is at most
2/|log(n/m)|. Consider the symmetric matrix, with zero diagonal,

    h_nm=1/[sqrt(nm)|log(n/m)|].

For positive weights w_n=1/sqrt(n), the Schur row is

    (1/w_n) sum_(m!=n) h_nm w_m
       =sum_(m!=n) 1/[m|log(n/m)|] <= 3H_N.                (2.2)

For m>n use log(m/n)>=(m-n)/m, obtaining 1/(m-n). For m<n use
log(n/m)>=(n-m)/n, obtaining 1/m+1/(n-m). Summing proves (2.2).
The weighted Schur inequality, or its proof by 2ab<=a^2+b^2 after inserting
the weights, bounds the quadratic form in |z(n)| by 3H_N M_1.
The factor 2 from the integrated exponential gives (2.1). No covariance
terms were declared zero; the full finite off-diagonal cost is paid.

### Multiplicative collision estimates, not a crude divisor-function bound

Uniformly for all sources above,

    M_0 <= K^4 H_L^4,           M_1 <= 2K^4 L^2 H_L.        (2.3)

Expand the positive majorants over ab=cd, with a,b,c,d<=L. There is a
unique representation

    a=g u, c=g v, b=h v, d=h u,
    gcd(u,v)=1, g,h<=floor(L/max(u,v)).

For M_0 this gives

    sum_(ab=cd) 1/(ab)
      =sum_(u,v coprime;u,v<=L)
          H_floor(L/max(u,v))^2/(uv) <= H_L^4.

For M_1 the exact unweighted collision count is

    E(L)=L^2 + 2 sum_(m=2)^L phi(m) floor(L/m)^2
        <= L^2+2L^2(H_L-1) <= 2L^2 H_L.                   (2.4)

The first term is u=v=1; for max(u,v)=m>1 there are 2phi(m) ordered
coprime pairs. Bounding four source factors by K^4 proves (2.3).
Actual M_0 and M_1 can be retained in (2.1) when smaller.

## 3. Imported analytic input and a completely explicit infinite tail

We use precisely the published theorem of Dhir Patel and Andrew Yang,
*An explicit sub-Weyl bound for zeta(1/2+it)*, arXiv:2302.13444 (2023):

    |zeta(1/2+it)| <= (667/10)t^(27/164),       t>=3.        (3.1)

Primary source: https://arxiv.org/abs/2302.13444 . The abstract explicitly
states (3.1); the theorem is imported, not independently re-proved or
numerically certified in this packet. No claim that it is the latest best
bound is needed. Only this fixed, unconditional estimate is used.

For T>=3, define the complete high-Mellin energy

    E_>T(c)=(1/(2pi)) integral_(|t|>T)
       |zeta(1/2+it)|^2 |C(1/2+it)|^4/(1/4+t^2) dt.

Then

    E_>T(c) <= 9000 M_0 T^(-55/82)
                   +27000 H_N M_1 T^(-137/82).            (3.2)

To prove this, use realness of c to combine positive and negative t.
On R<=t<=2R, (3.1), 1/4+t^2>=R^2, and (2.1) give a contribution at most

    [(667/10)^2 2^(27/82)/pi]
       [M_0 R^(-55/82)+6H_N M_1 R^(-137/82)].

Sum over R=2^j T, j>=0. BOTH resulting infinite geometric series are paid.
Use 2^(27/82)<2, pi>3,

    1/(1-2^(-55/82)) < 3,
    1/(1-2^(-137/82)) < 3/2.

Both last inequalities follow from the exact integer inequality
2^137>3^82. The two constants are less than 2(667/10)^2<9000 and
6(667/10)^2<27000, respectively. This proves (3.2) for the ENTIRE tail.
No numerical frequency truncation enters the theorem.

### Polylogarithmic control above a power cutoff

Set

    T_L=max(3, ceil(L^(164/137))).

Then

    E_>T_L(c) <= 2^17 K^4 H_L^2.                           (3.3)

Indeed, H_(L^2)<=2H_L. Equations (2.3) and (3.2) give

    E_>T_L(c) <= 9000 K^4 H_L^4 L^(-110/137)
                          +108000 K^4 H_L^2.

We have H_L^2<=2L^(4/5)<=2L^(110/137). For the first inequality,
H_L<=1+log L and the maximum of (1+x)^2 exp(-4x/5), x>=0, is
25/(4 exp(6/5))<2; the latter strict bound follows already by retaining
the first five terms of the positive exponential series. Consequently the
last display is <=126000 K^4 H_L^2<2^17 K^4 H_L^2.

Thus frequencies above about L^1.197 have a full polylogarithmic energy
budget. The cutoff grows with L and leaves a substantial low band. This
is not an estimate for E_>3 or for the whole covariance.

## 4. The ENTIRE dense mixed component, without a partner-degree hypothesis

Let Pi_>T denote the orthogonal projection in H=L^2((0,infinity),dx/x^2)
obtained by Fourier projection |t|>T after the log-unitary transform.
Equation (1.5) says E_>T(c)=||Pi_>T P||_ph^2.

For squarefree-supported c, SFC30 gives the exact decomposition

    P=D+O,
    D=sum_(d squarefree,d>=2) U_d^2 K_(d;1),
    O=sum_(d,u,v pairwise coprime squarefree,u!=v,ordered)
                  U_(du)U_(dv) K_(d;uv),
    K_(d;b)=sum_(a|d)mu(d/a) r_(adb),
    U_d=sum_(d|n)c(n)/n,
    ||D||_ph^2 <=648 K^4 H_L^6.                            (4.1)

SFC30's component proof, not independent acceptance of it, is imported
here from CONTINUATION.md. Orthogonal projection is a contraction, so

    ||Pi_>T_L O||_ph^2
       <=2 E_>T_L(c)+2||D||_ph^2
       <=2^19 K^4 H_L^6.                                  (4.2)

This is simultaneous control of ALL ordered coprime partner pairs, all
common factors, and all surviving composite denominators in this projected
component. Neither bounded degree nor a bounded cofactor gap is assumed.
It is a stronger coverage statement than the previous sparse graph result,
but for a different, projected object: (4.2) does NOT replace that prior
unprojected bound or prove the full unprojected dense estimate.

## 5. An exact continuous-to-native transfer; no sampling a projected function

A Mellin projection of a step function need not be a step function. It
would be incorrect to sample the projected functions at integers and
apply the old discrete tail map without proof. Instead define

    (Hcal f)(x)=f(x)/x - integral_x^infinity f(y)dy/y^2.     (5.1)

Hcal is an isometry from L^2(dx/x^2) onto L^2(dx). To see this, let
F(u)=exp(-u/2)f(exp u), G(u)=exp(u/2)(Hcal f)(exp u). Then

    G(u)=F(u)-integral_0^infinity exp(-v/2)F(u+v)dv.

With s=1/2+it its Fourier multiplier is s/(s-1), whose modulus is one.
The integral operator is bounded by its integrable kernel; approximation
from compactly supported functions extends this calculation to the whole
space. In particular

    transform(Hcal P)(t)=zeta(s)C(s)^2/(s-1).              (5.2)

For our original step source, direct integration on [k,k+1), k>=1, gives

    (Hcal P)(x)=P(k)/(k+1)-sum_(j>k)P(j)/[j(j+1)]
               =(T_discrete P)(k).                       (5.3)

On (0,1), Hcal P=0 by (1.4). Individual low/high projected pieces need not
vanish there; their entire global norms include that region and they
cancel there in the sum. No below-source or future contribution is dropped.

Define

    Q_low=Hcal Pi_<=T_L P,       Q_high=Hcal Pi_>T_L P.

Exactly, Q=Hcal P=Q_low+Q_high, and

    ||Q_high||_(L^2(0,infinity))^2 = E_>T_L(c).             (5.4)

This controls every restriction of Q_high as well. Low/high are orthogonal
GLOBALLY, not in general after restriction to a native observation interval.
We use a triangle inequality below rather than assert local orthogonality.

### Native square-step budget, retaining the actual squarefree completion

Use the SFC30 completed native source: c(n)=mu(n) through Y, correction
only at squarefree indices, cap K=16, L<=2Y, C(1)=0. Its proved component
budget is J(c)=sum_(k>=1)m_c(k)^2<=33F_Y, where

    m_c(k)=sum_(n<=k)c(n)/n,
    F_Y=sum_(k<=Y)(sum_(n<=k)mu(n)/n)^2.

Let b=Y+1 and B=b^2-1. Native Newton reconstruction and (5.3) give

    m(floor x)=2m_c(floor x)-Q_low(x)-Q_high(x),
                          b<=x<b^2.

Therefore

    sqrt(F_(b^2-1)-F_Y)
      <=2sqrt(33F_Y)+256sqrt(2)K^2 H_L
                            +||Q_low||_(L^2([b,b^2))).    (5.5)

This pays the whole high-Mellin contribution on the entire native annulus,
with completion and full future already included. The remaining norm in
(5.5) is NOT bounded by this packet. It is the restricted low-Mellin
component, not unnecessarily its full future energy.

A fixed source-power exponent strictly below two for that remaining
squared norm, with only polylogarithmic cutoff losses, would be useful for
the existing square-step recurrence. No such exponent is obtained here.
The exact Mellin reformulation alone must not be called the missing bound.

## 6. Relation to the concurrent work and limits

The read of #904 was frozen at
`d0d7ad05f9d4504e9d752518b34a9fd0609a06f7`, including NCL29 and ATC29.
NCL29 pays rational ANGLES away from zero, and ATC29 pays activation tails
while exhibiting large actual-source positive semiprime subsets. DMC31
keeps the COMPLETE signed sum and projects its log-scale frequencies.
There is no conflict with those subset obstructions. There is no assertion
that an arbitrary high-denominator mask has the same C(s)^2 factorization.

This application is source-generic apart from its last native transfer;
the genuinely source-specific difficulty can and does remain in Q_low.
It is not a new zero-free region, a proof of RH, an improved classical
Mertens estimate, or an unconditional gain for the whole native recurrence.
Nor is the cutoff exponent a percentage of progress toward RH.

The classical Newton/Mertens ancestor is Huxley--Watt,
*Mertens Sums requiring Fewer Values of the Mobius function*,
https://arxiv.org/abs/1807.05890 . The floor/Mellin/Plancherel and Hardy
identities are standard mechanisms rederived here with this normalization;
claims of novelty are limited to a proposed packet/application for this
repository, not priority over the literature.

## 7. Reproduction and status of evidence

Run `python -I -S -B verify_mellin_dense.py` (or with `-O`) from this directory.
The checker uses explicit exceptions, exact integers and Fractions. It checks
finite coefficient identities, collision counts, source moment bounds,
constant inequalities, native reconstruction, and the continuous/discrete
Hardy bridge. `--mutate` is a deliberate erroneous coefficient sign and must
exit nonzero. Its finite checks do not prove the infinite analytic theorem,
independently verify the imported zeta bound, or formalize Plancherel.

See MELLIN_VALIDATION.md for the commands actually executed and their
limits. Optional numerical spectral panels, if present, are explicitly
floating-point finite-band diagnostics, not interval certificates and not
part of the accepting exact checker.
