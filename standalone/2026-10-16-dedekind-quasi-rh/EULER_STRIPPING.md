# Removing the shifted L-factor without concealing its cost

Status: PROPOSED component mathematics; complete written arguments below,
not independently reviewed. No new zero-free boundary or native moment bound.
Source: Cureton--Thorner, hexagon:2610.00200v2, equation (11.3), Lemma 11.1.
Classical ingredients: Euler multiplication, ideal counting, Mellin inversion,
Mertens' theorem, and Minkowski. No novelty claim for those methods.

## 1. Exact factorization and a nonvanishing numerator up to the critical line

Fix a number field F, a finite excluded prime set S, and a unitary Hecke
character eta. In the paper eta=vartheta^6. Write q=Np, x=q^(-s), r=q^(-1).
Its principal correction is

    H_p(s)=(1-r^2)(1-(1-r)x-eta(p)q^2 x^6)
                      /((1-eta(p)q^3 x^6)(1-x)).             (1)

Define

    J_p(s)=(1-r^2)(1-(1-r)x-eta(p)q^2 x^6)/(1-x).           (2)

**Proposition 1.** J=product_(p notin S) J_p is holomorphic and nowhere zero
on Re(s)>1/2. For every sigma0>1/2, J and 1/J are bounded uniformly on
Re(s)>=sigma0. On Re(s)>2/3,

    H(s)=L^S(6s-3,eta,F) J(s).                              (3)

Consequently (3), using the classical Hecke continuation, continues H
meromorphically to Re(s)>1/2. It does NOT make H nowhere zero there.

Proof. Put E=eta(p)q^(3-6s). The nonconstant numerator has absolute value at
most (1-r)|x|+r|E|. For sigma>1/2 this is strictly below
(1-r)q^(-1/2)+r<1. Thus every J_p is nonzero, with a uniform lower bound
for each fixed p on sigma>=sigma0. Also

    J_p=(1-r^2)[1+(r x-eta(p)q^2 x^6)/(1-x)],
    |J_p-1| <= C_sigma0(q^(-2)+q^(-1-sigma0)+q^(2-6sigma0)). (4)

All three prime-ideal sums converge when sigma0>1/2 (comparison with the
absolutely convergent ideal zeta series suffices). The product and its
logarithmic tail converge normally and uniformly, and the finitely many
initial factors stay bounded away from zero. This proves all assertions
about J. Equation (3) follows by multiplication in absolute convergence.
QED.

The paper's local nonzero argument already supplies the local part of this
proof. The additional observation is that extracting the weighted sixth-power
Euler factor changes the global absolute-convergence boundary from 2/3 to
1/2. It does not assert boundary nonvanishing at exactly 1/2.

**Character warning.** In the paper, vartheta contains the norm-pulled angular
character Lambda (Section 7, Lemma 7.3), as well as a finite ray character.
Hence eta=vartheta^6 is generally NOT finite order. The imported finite-order
Hecke corollary cannot simply be applied to this shifted L-function. Even
an appropriate zero-free statement for eta would have to be translated under
s -> 6s-3; its real-part boundary would not remain unchanged.

## 2. A very short exact arithmetic source

Let C_S=product_(p notin S)(1-q^(-2))=1/zeta_F^S(2)>0. Dividing (2) by
the local zeta factor gives the particularly simple identity

    J(s)/zeta_F^S(s)
      =C_S product_(p notin S)[1-(1-q^(-1))q^(-s)
                                  -eta(p)q^(2-6s)].        (5)

Let a_eta(n) be the normalized coefficients of the product in (5), WITHOUT
C_S. Their prime-power coefficients are

    a_eta(p)=-(1-q^(-1)),  a_eta(p^6)=-eta(p)q^2,
    a_eta(p^j)=0 for j notin {0,1,6},  a_eta(1)=1.           (6)

Equivalently, write n=b c^6 with b,c squarefree and coprime. Such a
representation is unique when it exists, and

    a_eta(n)=mu_F(b) product_(p|b)(1-1/Np)
                    mu_F(c) eta(c) (Nc)^2.                 (7)

Otherwise a_eta(n)=0. Here (b,c)=1 is REQUIRED by (6), not an invented
restriction on a general Dirichlet convolution. Conversely the convolution
identities below require shared factors and impose NO extra coprimality.

This exhibits the coupled prime and sixth-power source that a modified theta
calculation would have to estimate. The q^2 coefficient must not be erased.

## 3. Reversible physical moment comparison with only logarithmic cost

For this section eta(p) may even be arbitrary with |eta(p)|<=1; a global
Hecke interpretation is unnecessary. Let xi_u be any completely
multiplicative ideal function with |xi_u(n)|<=1, retaining all original
nonunit zeros. Fix a bounded test W supported in [a,b] subset (0,infinity),
and ANY finite nonnegative row measure w. Define

    A_u(X)=sum_n mu_F(n) xi_u(n) W(Nn/X),
    B_u(X)=sum_n a_eta(n) xi_u(n) W(Nn/X).                  (8)

All ideals are prime to S. For p>=1 set, with the SAME row measure at every X,

    E_A,p(D)=sup_(0<X<=D) X^(-1/2) ||A(X)||_Lp(w),
    E_B,p(D)=sup_(0<X<=D) X^(-1/2) ||B(X)||_Lp(w).          (9)

These are suprema of norms, not norms of maxima.

**Proposition 2.** If d=[F:Q], then for D>=1,

    E_B,p(D) <= C_(F,b) log(3+bD)^(12d) E_A,p(D),
    E_A,p(D) <= C_(F,b) log(3+bD)^(12d) E_B,p(D).           (10)

The constant is independent of the row measure, p, xi and eta profile. It
requires no extra small-prime exclusion. At any FIXED moment order the
logarithmic factors can be absorbed in D^epsilon. This is a comparison,
not a proof that either side has diagonal size. A bound supplied only along
H=X^h does not automatically provide the same-height envelopes in (9).

Proof. Normalize j_p=J_p/(1-q^(-2)). Formally a_eta=mu_F*j and
mu_F=a_eta*j^(-1). Both kernels have constant coefficient one locally.
We bound the absolute local series at t=q^(-1/2). With a=1-r,

    j_p(x)=1+(r x-eta(p)q^2x^6)/(1-x),

so its absolute coefficient mass is at most

    1+(r t+q^2t^6)/(1-t)=1+r(1+t)/(1-t).                  (11)

For the inverse use the identity

    j_p(x)^(-1)=(1-x)/(1-a x)
                  * [1-eta(p)q^2x^6/(1-a x)]^(-1).

The first factor equals 1-r x/(1-a x); the second admits a geometric
coefficient majorant. Since q^2t^6=r<1-a t, its absolute mass is at most

    [1+r t/(1-a t)]/[1-r/(1-a t)]
      =1+r(1+t)/[(1-r)(1-t)] <= 1+12/q.                  (12)

The final inequality follows from q>=2 and
(1+t)/[(1-r)(1-t)] <= 2(3+2sqrt(2))<12. This also majorizes (11).
All these are coefficientwise nonnegative majorants, uniform in eta.
For either kernel, restrict its ideal norm to Nn<=T. Every contributing
prime ideal then has norm <=T, and extending each local sum gives

    sum_(Nn<=T) |j^(+/-1)(n)|/sqrt(Nn)
      <= product_(Np<=T)(1+12/Np)
      <= product_(rational prime ell<=T)(1-1/ell)^(-12d)
      <= C_F log(3+T)^(12d).                              (13)

At most d prime ideals lie over each rational prime; their norms are at
least that prime. The last step is the classical Mertens product estimate.
For T<1 the truncated sum is empty; bounded T is harmless.

The literal finite convolution identities are

    B_u(X)=sum_n j(n)xi_u(n) A_u(X/Nn),
    A_u(X)=sum_n j^(-1)(n)xi_u(n) B_u(X/Nn).               (14)

No condition (n,residual ideal)=1 is imposed. Multiplication by xi_u(n)
is an Lp contraction, including at nonunit rows. Apply Minkowski, use (13)
with T=bD, divide by sqrt(X), and take the supremum. This proves (10).
QED.

The principle overlaps the native completions of PRs #935/#939/#945. The
specific weighted sixth-power coefficient in (6), its inverse, and the bound
(12) are the application here. Unlike #945's bounded degree-three correction,
this kernel has a logarithmic critical cost. For growing p=2k its moment
cost is log(D)^(24dk), and it must be priced, not silently called D^epsilon.

## 4. Why stripping a previously estimated detector is NOT a free improvement

Put b0=61/100 and G(s)=exp((s-5/6)^2). Define on the initial line Re(s)=2

    f(Z)=(1/(2pi i)) integral Z^(s-b0) G(s) H(s)/zeta_F^S(s) ds,
    g(Z)=(1/(2pi i)) integral Z^(s-b0) G(s) J(s)/zeta_F^S(s) ds.

**Proposition 3.** There is an exact identity, absolutely convergent for each Z>0,

    g(Z)=sum_n mu_F(n)eta(n)(Nn)^(3-6b0) f(Z/(Nn)^6).      (15)

If f(Z)<<_epsilon Z^(beta-b0+epsilon) for Z>=1 and every epsilon>0,
then taking absolute values in (15) proves only

    g(Z)<<_epsilon Z^(max(beta,2/3)-b0+epsilon).            (16)

Here beta>=1/2 is enough for the stated application. No optimal operator-norm
lower bound or impossibility of signed improvement is asserted.

Proof. On Re(s)=2, 1/L^S(6s-3,eta)=sum mu_F(n)eta(n)(Nn)^(3-6s)
converges absolutely. The Gaussian makes the Mellin integral integrable,
so substitution gives (15). Moving the initial contours arbitrarily far
RIGHT gives f(Z)=O_A(Z^A) and g(Z)=O_A(Z^A) as Z -> 0 for every A>0.
All factors are in absolute convergence there; no zero hypothesis is used.
This small-Z estimate also proves absolute convergence in (15).

Split at Nn=Z^(1/6). Above that cutoff use small-Z decay. Below it the
termwise bound, ignoring epsilon for legibility, is

    Z^(beta-b0) sum_(Nn<=Z^(1/6)) |mu_F(n)|(Nn)^(3-6beta).

Ideal counting O_F(T) makes this bounded, logarithmic, or
O(Z^(2/3-beta)), according as beta is above, equal to, or below 2/3.
The tail has the same O(Z^(2/3-b0)) bound after choosing A large. Small
power losses cover endpoints and prove (16). QED.

At beta=1/2 the termwise critical mass is the number of squarefree ideals
through Z^(1/6), of order Z^(1/6); this is the classical squarefree ideal
count from mu^2=sum_(d^2|n)mu(d) and ideal counting. It is a statement about
this ABSOLUTE budget, not about the signed sum or a norm after equal-norm
coefficients have been grouped. In particular, the paper's beta=31/32 is
preserved, not improved, by (15).

There is no contradiction between (10) and (16). Equation (10) compares the
native coefficients with the COUPLED source (6), including the cancellation
of two weighted sixth-power terms inside J. Equation (15) instead strips
an isolated shifted L-factor AFTER a bound for f has been taken. Those are
different operators with different absolute masses.

## 5. A precise target for the new route

By (5), g has the absolutely convergent physical expansion

    g(Z)=C_S Z^(-b0) sum_n a_eta(n) w(Nn/Z),
    w(y)=(1/(2sqrt(pi))) y^(-5/6) exp(-(log y)^2/4).        (17)

The Gaussian formula follows by a one-dimensional Fourier Gaussian integral.
It is not compactly supported, so (10) is NOT by itself a theorem about
(17). Using it for (17) requires a dyadic decomposition and control of all
scales and test seminorms; that extra interface remains explicit.

A bound g(Z)<<_epsilon Z^(1/2-b0+epsilon), for every epsilon>0, would
exclude every zero of zeta_F with real part >1/2: its Mellin transform
would be holomorphic there, whereas GJ is nonvanishing there. This is an
OPEN arithmetic estimate, not supplied by Propositions 1--3.

The productive next calculation is to insert the coupled local factor (6)
into the TWO evaluations of the paper's average before Cauchy or absolute
values, retaining the common-prime terms. One must then prove a matching
transformed-family estimate. Merely multiplying the final inequality by
1/L, treating eta as finite-order, or keeping only the positive completed
energy does not do it.
