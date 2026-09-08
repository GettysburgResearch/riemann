# Full-source coercivity outside an explicit finite-dimensional obstruction

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
The Riemann Hypothesis, positivity of the complete operator, and the original
subexponential coefficient inequality are NOT proved.
Scope: the literal PR #792 operator on EVERY fixed finite interval; complex L2
tests, arbitrary signs, all prime powers, and the complete archimedean source.
Source parent: PR #792 @ 2c3184545bafb4f5d873d2fa0ffc2c335a25d048.
Local labels FW-1--FW-3 are confined to this packet, not canonical claim IDs.
Computation: exact rational identities and elementary source enclosures only.
Smallest missing step: a sign bound for the exceptional directions together
with their coupling to the positive subspace. A dimension bound is not that bound.

## 1. Why change the attempted completion

The parent proves strict full-source positivity for support diameter <=1/20,
not for sums of functions in distant short intervals. Its exact local tail
identity supplies a way to keep the complete arithmetic source on any finite
window. Here we combine that identity with an explicit archimedean frequency
barrier. This pays an infinite-dimensional part of the sign problem even on
arbitrarily long, but fixed, windows.

The general phenomenon is NOT claimed new. Yoshida's finite-codimension Weil
positivity and the localized operators reviewed by Suzuki (2026, introduction,
Theorems 1.1--1.4) are relevant prior art. Our assertion below is a quantitative,
source-matched specialization to the damped resolvent kernel already in #792.
It does not identify this compact operator with Suzuki's unbounded operator.

## 2. Full source, exact tail, and Fourier conventions

Fix a=3/4, b=3/2, c=1/2. Let

    W(x) = exp(|x|/2)/2 + C_b exp(-b|x|)
       + sum_(j>=1) exp(-(2j+1/2)|x|)/((2j+1/2)^2-b^2)
       - (1/(2b)) sum_(n>=2) Lambda(n)/sqrt(n)
          [exp(-b|x-log n|)+exp(-b|x+log n|)],
    C_b=(1-gamma_E-log(2pi))/3,
    T(t,u)=b exp(-a(t+u))W(t-u).

The parent constructs T in trace norm from this arithmetic series. No zeros
are used to define it here. Let T_L be its restriction to L2(0,L). Let T_X
retain all prime powers n<=X and the ENTIRE gamma series. Choose an integer
X>=max(2,exp(L)), and set

    Q_X=sum_(2<=n<=X) Lambda(n)/sqrt(n),
    tau_X=sum_(n>X) Lambda(n)/n^2 > 0.

For f in L2(0,L), put h(t)=exp(-at)f(t). The exact parent window identity is

    <f,(T_L-(T_X)_L)f>
      = -tau_X |int_0^L cosh(bt)h(t)dt|^2
        +tau_X |int_0^L sinh(bt)h(t)dt|^2.                 (1)

Indeed the omitted kernel is -tau_X exp(-a(t+u))cosh(b(t-u)). Equation (1)
keeps BOTH signs of the rank-two correction. In particular, the one condition

    int_0^L cosh(bt)h(t)dt=0                              (2)

makes the exact tail nonnegative. One need not impose both exponential
moments at b merely to get a lower bound.

Our Fourier convention is hhat(w)=int_R h(t)exp(-iwt)dt, with zero extension.
Define

    Omega(w)=Re digamma(1/4+iw/2)-log pi,
    V_X(w)=Omega(w)-2 sum_(2<=n<=X) Lambda(n)/sqrt(n) cos(w log n).

For h satisfying the TWO additional constraints

    int_0^L exp(ct)h(t)dt=int_0^L exp(-ct)h(t)dt=0,         (3)

the exact cutoff multiplier identity is

    <f,(T_X)_L f> = b/(2pi) int_R
                  V_X(w)/(b^2+w^2) |hhat(w)|^2 dw.        (4)

This identity is proved for the literal normalization in the parent's
arithmetic-cutoff-inertia/PROOF.md, Section 2. We give the domain argument
needed below, rather than applying it to an exponentially growing kernel
without qualification.

Let

    phi(t)=(1/c) int_0^t sinh(c(t-u))h(u)du,  0<=t<=L.     (5)

Then phi''-c^2 phi=h, phi(0)=phi'(0)=0. Conditions (3) imply
phi(L)=phi'(L)=0 by the two exponential formulas for sinh and cosh. Thus
phi belongs to H0^2(0,L), its zero extension is in H^2(R), and

    hhat(w)=-(w^2+c^2) phihat(w).                         (6)

The convolution v=exp(c|.|)*h vanishes outside [0,L], because of (3), and
satisfies (D^2-c^2)v=2c h. Hence v=2c phi and its Fourier transform is
-2c hhat(w)/(w^2+c^2). This validates the growing-exponential part of (4).
The other terms are ordinary integrable kernels, with a normally summable
gamma series and a finite prime sum. Their multipliers sum to (4) by the
digamma partial fractions. The resulting multiplier V_X/(b^2+w^2) is
bounded; approximation therefore extends (4) to every L2 h satisfying (3).
All expressions are sesquilinear, with complex conjugation retained.

## 3. FW-1: an explicit all-frequency archimedean barrier

For k>=0 write c_k=2k+1/2. Digamma partial fractions give exactly

    Omega(w)-Omega(0)
       =sum_(k>=0) (2/c_k) w^2/(c_k^2+w^2).               (7)

Each summand is nonnegative for real w. Also

    Omega(0)=-gamma_E-pi/2-3log 2-log pi > -6.             (8)

For instance use gamma_E<1, pi/2<11/7, log 2<7/10, log pi<6/5.
Their sum is 411/70<6. All inequalities are strict elementary bounds;
no zeta zero or prime-distribution estimate enters them.

Let qbar>=Q_X be any certified upper bound. Choose an integer m>=0 such that

    S_m:=sum_(k=0)^m 4/(4k+1) >= 7+2qbar,               (9)
    C_m:=(m+1)(2m+1).

Then for EVERY real w,

    V_X(w) >= 1-C_m/(w^2+1/4).                          (10)

Proof. Bound each prime cosine above by one. In (7), keep k<=m and write

    (2/c_k) w^2/(c_k^2+w^2)
      =2/c_k-2c_k/(c_k^2+w^2).

Equations (8)--(9) give a constant at least one, and

    sum_(k=0)^m 2c_k/(c_k^2+w^2)
      <= [sum_(k=0)^m 2c_k]/(c^2+w^2)
      =C_m/(c^2+w^2).

This proves (10). The inequalities are uniform in frequency, not finite
sampling of the multiplier. We used an absolute prime bound only for this
high-frequency sector, NOT as a proposed global Weil positivity argument.

A completely explicit finite choice always exists without summing a huge
harmonic prefix. For qbar>=0 put

    r=ceil(5/2+3qbar),   m=5*2^r.                        (11)

Since

    S_m >= 4+log((4m+5)/5)
         >4+(r+2)log 2
         >4+(2/3)(r+2) >=7+2qbar,

(11) suffices. The first inequality is decreasing-function integral
comparison of sum_(k=1)^m 1/(k+1/4); log 2>2/3 follows from strict Jensen
for 1/x on [1,2]. The bound may be extremely large. It is not an efficiency
or uniform-in-L claim. A much smaller m can be certified directly by (9).

## 4. FW-2: full-source coercivity on a finite-codimension subspace

Let K>=0 be any integer such that

    pi^2 (K+1)^2/L^2 >= 2C_m+7/2.                        (12)

The explicitly sufficient choice

    K=ceil(2(m+2)L/3)                                    (13)

uses only pi>3 and
4(m+2)^2-(2C_m+7/2)=10m+21/2>0.

Define V_(L,X,m,K) to be the subspace of f in L2(0,L) for which h=exp(-at)f
satisfies (2), (3), and

    int_0^L phi(t)sin(j pi t/L)dt=0,  1<=j<=K,            (14)

where phi is the fixed Volterra transform (5). All these are bounded linear
functionals of f. Consequently V is a closed subspace of codimension at
most K+3. It is infinite-dimensional. It is defined from arithmetic cutoffs,
elementary functions and specified frequencies; no zero-dependent choices
are made.

**Theorem FW-2.** For every f in V,

    <f,T_L f> >= (b/2)||phi'||_2^2
        +tau_X |int_0^L sinh(bt)h(t)dt|^2.                (15)

The right side is strictly positive for every nonzero f in V.

Proof. Use (4), (6) and (10). With x=w^2 and C=C_m, the EXACT division is

    [(x+c^2)^2-C(x+c^2)]/(x+b^2)
       = x-(C+7/4)+(4+2C)/(x+9/4).                       (16)

The last term is positive. Plancherel yields

    <f,(T_X)_L f>
      >= b[||phi'||_2^2-(C_m+7/4)||phi||_2^2].            (17)

The Dirichlet sine expansion is legitimate for phi in H0^1(0,L).
Conditions (14) remove its first K coefficients. Hence

    ||phi'||_2^2 >= ((K+1)pi/L)^2 ||phi||_2^2.

Equation (12) makes (17) at least (b/2)||phi'||_2^2. Finally use the
NONNEGATIVE exact tail in (1)--(2), giving (15). If phi'=0, the endpoint
condition phi(0)=0 makes phi=0, and h=phi''-c^2phi=0. The finite-interval
damping is invertible, so f=0. This proves strictness.

The lower bound is NOT a positive constant times ||f||_2^2. Its weaker
primitive norm is compatible with compactness. The prime powers beyond X
are neither replaced by an average nor omitted in (15).

## 5. FW-3: a quantitative finite negative-index theorem at every length

Let n_-(T_L) count strictly negative eigenvalues with multiplicities, and
let n_0(T_L) be the dimension of its kernel. Then

    n_-(T_L)+n_0(T_L) <= K+3.                             (18)

Also T_L has infinitely many strictly positive eigenvalues. Both statements
hold unconditionally for every finite L>0, with the explicit choices above.

Proof. The spectral subspace consisting of the negative eigenspaces and
kernel is nonpositive for the quadratic form. If its dimension exceeded
K+3, it would intersect the codimension-at-most-K+3 space V nontrivially,
contradicting (15). For an infinite-dimensional putative nonpositive space,
apply the same argument to a finite-dimensional subspace of dimension K+4.
This proves (18). The infinite-dimensional strictly positive space V forces
infinitely many positive eigenvalues by the spectral theorem and the same
finite-dimensional intersection argument. T_L is compact and self-adjoint,
so no further spectral component away from zero occurs.

There is no conflict with the preceding infinite-negative-index theorem for
a RAW cutoff on the entire half-line. A fixed finite interval is a different
operator. The constants here depend on L and are not bounded as L grows.

### An actual explicit example at support length one

Take L=1 and X=3. The only prime powers <=3 are 2 and 3, so

    Q_3=log(2)/sqrt(2)+log(3)/sqrt(3) < 9/8.

The checker certifies this strict inequality using rational log series and
integer-square-root bounds. It also certifies e<3, so X>=exp(L).
The exact rational sum S_152 is greater than 37/4=7+2(9/8). Thus m=152
is permitted and C_m=46665. Set K=101. Since pi>3,

    pi^2*102^2 > 9*102^2=93636 > 93333+1/2=2C_m+7/2.

Therefore every nonzero test obeying the 104 displayed linear constraints
has strictly positive FULL-source energy on [0,1], and

    n_-(T_1)+n_0(T_1) <=104.                              (19)

This is not a proof that any negative eigenvalues exist, and certainly not
an assertion that their count equals 104. It is a coarse upper bound, not
an optimal record. Translated intervals of the same length obey the same
inertia statement, since translation changes only the positive damping
factor in the undamped difference-kernel description.

## 6. What the attempted completion still needs

The attempted continuation was: use the local full-source sign, control the
long-range high-frequency sector arithmetically, and remove all remaining
negative directions. The second step is now paid in the explicit sense
(15). The third is not.

A positive subspace of finite codimension does NOT prove positivity of the
whole operator. Nor is the restriction to an arbitrary complementary finite
subspace by itself a complete sign test: its cross terms with V matter.
For example the exact matrix [[1,2],[2,1]] has positive restrictions to both
coordinate axes and a negative eigenvalue. In infinite dimensions the inverse
of a positive compact block may also be unbounded, so an unqualified ordinary
Schur-complement formula is not supplied by (15).

Thus (18) is not a claim that a leading 104-by-104 matrix alone decides the
sign on [0,1]. A validated form-domain Schur reduction or a source-specific
bound on the exceptional directions AND their coupling is still required.
Neither has been proved in this packet. Merely increasing a finite matrix
size, quoting a positive diagonal, or taking absolute prime bounds in the
remaining low-frequency sector would not fill this gap.

For the original route the desired conclusion remains T>=0, which would
imply |d_n|<=d_0 via A*TA=T and d_n=(9/8)Tr(TA^n), then the original
subexponential c_n(2) inequality. We have NOT proved that conclusion.
The all-length family of finite index bounds is not a uniform zero-index
bound and is not a proof of RH.

## 7. Input and novelty boundary

Inputs from the repository: the literal arithmetic kernel and trace-class
construction; the constrained cutoff multiplier identity; the EXACT rank-two
window tail. Their precise commits and Git blob identities are in SOURCES.md.
The local 1/20 sign is motivation, not a hypothesis used in FW-1--FW-3.

Classical inputs: digamma series and special values, Plancherel, elementary
Dirichlet sine expansion, and the compact self-adjoint spectral theorem.
No PNT, zero census, zero simplicity, spacing, or RH premise is used here.

Suzuki explicitly credits Yoshida (1992) for finite-codimension local Weil
positivity and explains the discrete lower-bounded spectrum of related
localized Weil operators. This packet does not claim the general phenomenon
as new. Its contribution for repository use is the explicit gamma barrier,
source-preserving one-constraint treatment of the prime tail, exact differential
adapter, and computable bound for THIS compact resolvent normalization.
Finite rational replay authenticates only the stated algebra and constants;
it does not machine-prove the infinite analytic statements.
