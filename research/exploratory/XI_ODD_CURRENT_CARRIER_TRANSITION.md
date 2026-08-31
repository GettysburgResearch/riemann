# Actual Xi odd currents: a unique scalar carrier transition

Status: PROPOSED ANALYTIC THEOREM; independent frozen-source review pending.

This note changes the positive odd current order K. It retains the literal
Xi theta kernel and the parent's scalar gain and phase. It does not change
a prescribed physical gauge, assert innerness, or provide a zero-capture or
RH theorem. Numerical checks are non-directed scouts, not certificates.

Parent kernel and scalar source: `XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md`
at `3b6972320899a82c6caa3a98e2ada5ff703a605a`. The separate growing-order note
`XI_ODD_CURRENT_DOUBLE_SCALING.md` treats two earlier concentration scales.
The present boundary scale is outside its bounded-b saddle theorem.

## 1. Exact scalar sign and monotonicity, before asymptotics

For xi>0, positive odd K, and d>=0 define

    H(d)=Phi_Xi((xi-d)/2) Phi_Xi((xi+d)/2),
    P_K(z)=sum_(j=0)^((K-1)/2) binom(K,2j) z^j,
    dnu_K^+(d)=P_K(d^2/xi^2) H(d) dd / integral P_K H.

These are positive probability measures with every polynomial moment.
Write m_K^+=E_(nu_K^+)[d^2]. The parent's exact scalar definitions give

    p_K/g_K=m_K^+/xi^2,
    sign(g_K-p_K)=sign(xi^2-m_K^+).                    (1.1)

In particular these are PLUS-weight moments, not the moments of the
current probability mu proportional to d[(xi+d)^K-(xi-d)^K]H(d)dd.

**Theorem 1.** For each fixed xi>0, m_K^+ is strictly increasing as K runs
through the positive odd integers, and tends to infinity. Consequently
g_K-p_K changes sign at most once on that odd lattice. There can be at most
one exact equality. For all sufficiently large xi the sign is initially
positive at K=1 and eventually negative.

Proof. Put A=P_K and B=P_(K+2). For indices shared by A and B,

    [z^j]B/[z^j]A=(K+2)(K+1)/[(K+2-2j)(K+1-2j)],       (1.2)

strictly increasing with j. The extra highest coefficient of B is positive.
The coefficient-pair identity

    B'A-BA'=sum_(j>i) (j-i)(b_j a_i-b_i a_j)z^(i+j-1)

then has nonnegative coefficients and at least one positive coefficient.
Thus B/A is strictly increasing on z>0. Reweighting a continuous positive
measure by this ratio strictly increases E[z]: its covariance with z is
positive, as follows also from the double-integral covariance formula.
This proves strict monotonicity.

To prove escape, fix R and select a compact interval [D,D+1] with D>R.
On [0,R], P_K(d^2/xi^2)<=(1+R/xi)^K. On [D,D+1] the exact identity

    P_K(d^2/xi^2)=(1/2)(1+d/xi)^K
                       [1+((xi-d)/(xi+d))^K]

gives a lower bound c_(D,xi)(1+D/xi)^K with c_(D,xi)>0 independent of odd K.
Integration against the fixed positive H shows nu_K^+([0,R])->0. Since
R is arbitrary, its second moment tends to infinity. Finally, at K=1,
the parent's Gaussian kernel concentration, without the current d^2
weight, gives m_1^+~1/(2pi exp(xi))<xi^2 as xi->infinity. QED.

The exact scalar carrier is rho(eta)=g/eta+(p-g)eta for eta>0. Hence:

* if m_K^+<xi^2, it has one positive zero sqrt(g/(g-p));
* if m_K^+=xi^2, it is g/eta and has no positive zero;
* if m_K^+>xi^2, it has no positive zero and its minimum is
  2sqrt(g(p-g))>0.

These facts concern this scalar family only. In particular there is no
claim that selecting eta realizes a permitted physical companion.

## 2. The transition window and its correction

Set

    M=pi exp(2xi),  ell=1+1/(2xi),
    Delta=K-2xi M,
    C_(K,xi)=Delta+(7/2)xi+3/2+1/(4xi+2).                (2.1)

**Theorem 2.** For every fixed C>0, uniformly for positive odd K satisfying
|Delta|<=C xi as xi->infinity,

    M ell [m_K^+-xi^2]=C_(K,xi)+O_C(xi/M).              (2.2)

Thus whenever C_(K,xi) stays bounded away from zero, the eventual sign of
g_K-p_K is its opposite. The odd-lattice transition is located, up to the
rounding to odd orders and an O(xi exp(-2xi)) uncertainty in the threshold,
at

    2pi xi exp(2xi) -(7/2)xi -3/2 -1/(4xi+2).           (2.3)

Formula (2.3) does not assert that a noninteger K defines the original
polynomial current. If an odd integer is exceptionally close to the
displayed threshold, (2.2) alone may not determine its sign. The exact
monotonicity in Theorem 1 is unaffected.

### Proof: local expansion uses the low-argument kernel literally

Put q=xi and r=d-q. On |r|<=1 the higher kernel argument is q+r/2 and the
lower one is -r/2. The full Xi kernel is even, so the lower factor is
Phi_Xi(r/2), which is NOT replaced by a first-orbit approximation. The
parent's exact theta formula for the higher factor is

    Phi_Xi(q+r/2)=4pi^2 exp[(9/2)q+(9/4)r-M exp(r)]
                      theta_*(exp(2q+r)),
    theta_*(X)=1-3/(2pi X)+O(exp(-3pi X)).               (2.4)

All fixed derivatives of log(theta_*(exp(2q+r))) are O(1/M), uniformly on
this interval. This follows by termwise differentiation of its absolutely
convergent theta series; the differentiated n>=2 tail is exponentially
small. The fixed function log Phi_Xi(r/2) is even and smooth here.

The density differs locally from (2q+r)^K H(q+r) by a relative error
smaller than every power of 1/M, because its additional factor is
1+[(-r)/(2q+r)]^K. Set y=sqrt(M)r and

    u=Delta/(2q)+9/4,
    A=1-1/(2q^2),
    L_1(y)=u y-A y^3/6.                                (2.5)

Taylor expansion of K log(1+r/(2q)), -M(exp(r)-1), and the two exact
kernel correction terms gives, uniformly on |y|<=M^(1/24),

    log[f(q+y/sqrt(M))/f(q)]
       =-ell y^2/2+M^(-1/2)L_1(y)+M^(-1)L_2(y)
          +O_C(M^(-3/2)(|y|+|y|^3+|y|^5)),             (2.6)

where L_2 is an even polynomial of degree at most four with coefficients
bounded independently of q>=2 and |Delta|/q<=C. Explicitly, ignoring an
O(M^(-2)y^2) term already inside the remainder bound,

    L_2(y)=[-Delta/(8q^2)+(log Phi_Xi)''(0)/8]y^2
                  -[1/24+1/(32q^3)]y^4.               (2.7)

Here f denotes the full plus-weight density; constant normalizations
cancel in the ratio. In particular the linear 9/4 in (2.5) is retained.
Dropping it would give an incorrect order-xi correction to the threshold.

After exponentiation, the term of order M^(-1/2) is the odd L_1 and that
of order M^(-1) is the even L_2+L_1^2/2. The weighted integral remainder
is O_C(M^(-3/2)) for every fixed polynomial weight, by the tail argument
below. Oddness therefore gives

    E[r]=(1/M)[u/ell-A/(2ell^2)]+O_C(M^(-2)),
    E[r^2]=1/(M ell)+O_C(M^(-2)).                        (2.8)

These expectations are under the true plus-weight probability. Since
m_K^+-q^2=2q E[r]+E[r^2], equations (2.8) yield

    M ell(m_K^+-q^2)
       =Delta+(9/2)q+1-qA/ell+O_C(q/M).

The exact rational identity

    qA/ell=q-1/2-1/(4q+2)

proves (2.2).

### Proof: normalization and all tails

No lower-argument theta approximation is needed outside the local
interval. The parent's global estimate bounds the density by a constant
times exp F_0(d), where

    F_0(d)=K log(q+d)-2pi exp(q) cosh d.

The ratio of this majorant to the exact density at d=q stays bounded
above and below: the lower factor there is the fixed positive Phi_Xi(0)
and the higher factor satisfies (2.4). Also F_0'(q)=Delta/(2q)+pi=O_C(1).
On |d-q|<=1, F_0''(d)<=-cM with c>0 independent of q large. Consequently
the relative majorant is bounded by C exp[-cM(d-q)^2], after adjusting C.

Outside this interval, global strict concavity and the slopes at q+/-1
give a bound C exp[-cM-cM(|d-q|-1)] on the domain d>=0. Thus its polynomial
moments outside the interval are exponentially small. Inside the
interval, the portion |y|>M^(1/24) is also smaller than every inverse
power of M. The local lower bound supplies a normalization comparable
to M^(-1/2). These estimates justify integrating the expansion (2.6),
extending the central Gaussian integrals to the whole real y-line, and
the uniform weighted remainders used in (2.8). QED.

## 3. Interpretation and checks still required

There are now three different scales in the changed-order family:

    K~xi exp(xi/2): change of the microscopic rescaled profile;
    K~xi exp(xi):   separation to two bounded nonzero d locations;
    K~2pi xi exp(2xi): plus-weight second moment reaches xi^2,
                      eliminating the positive scalar carrier zero.

The third scale is not a consequence of substituting large K into a
fixed-order formula. Its lower-argument kernel visits zero, and its
order-xi correction uses that kernel's evenness together with the exact
9/4 high-argument amplitude derivative.

Independent review must check the monotone-likelihood-ratio argument,
the distinction between plus and current measures, all constants in the
local expansion, and the global tail normalization. A separate exact
producer can check rational identities and parity cancellations. A
non-directed theta scout can falsify the expansion but cannot certify
its asymptotic quantifiers or the sign of a finite near-critical case.

No claim is made about external novelty, positive even/noninteger
currents, full current-order moduli, complex saddle geometry, prescribed
fixed-lambda admissibility, source accessibility, or the Riemann hypothesis.
