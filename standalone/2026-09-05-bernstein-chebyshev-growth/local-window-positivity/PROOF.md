# Exact window tails and a full-source positive factorization on short intervals

Status: PROPOSED COMPLETE COMPONENT PROOFS, with a rational source certificate;
independent mathematical and code review required. RH is NOT proved.
Scope: the literal operator of PR #792, every finite observation window for the
tail identity, and every L2 test of support diameter at most 1/20 for positivity.
No zero locations, zero census, simplicity, or RH hypothesis is used.
The classical PNT is imported ONLY for the asymptotic rates in Section 3.
Publication parent: dc4bb9dbb49876732eb656339e79ee4ec43b157f.
Mathematical source: cross-route-hardy-laguerre/BRIDGE.md at
39c13367f4b3956631ea1e00fac6c3005fc32057, blob
81d7d5db7a25f5875a08c10235fdb514d67cc744.
Local names LW-1 through LW-3 have no canonical theorem status or priority claim.
Smallest unpaid step: full-source positivity on arbitrarily long intervals.

## 1. Preserve the full arithmetic operator

Set a=3/4, b=3/2=2a, c_j=2j+1/2, and

    C_b=(1-gamma_E-log(2pi))/3,
    P_2=-zeta'(2)/zeta(2)=sum_(n>=2) Lambda(n)n^(-2).

The source fixed in the parent is the even continuous function

    W(x)=exp(|x|/2)/2+C_b exp(-b|x|)
      +sum_(j>=1) exp(-c_j|x|)/(c_j^2-b^2)
      -(1/(2b))sum_(n>=2) Lambda(n)/sqrt(n)
          [exp(-b|x-log n|)+exp(-b|x+log n|)],               (1)

and the self-adjoint trace-class operator on L2(0,infinity)

    T(t,u)=b exp(-a(t+u)) W(t-u).                           (2)

All prime powers occur with the von Mangoldt coefficient log p at n=p^r.
The parent proves absolute trace-norm convergence of (2). This packet retains
that normalization; inner products are linear in the second argument.
Let T_X delete only the terms n>X, retaining the COMPLETE gamma series.
P_L is multiplication by the indicator of [0,L], not a Laguerre projection.

## 2. LW-1: the whole omitted prime tail is exactly rank two on a window

For L>0 and X>=exp(L), define the strictly positive safe-axis scalar

    tau_X=sum_(n>X) Lambda(n)n^(-2)
         =P_2-sum_(2<=n<=X) Lambda(n)n^(-2).                 (3)

The endpoint convention is n<=X in the retained part; n>X in the tail.
Let u_+(t)=1_[0,L](t)exp((-a+b)t), u_-(t)=1_[0,L](t)exp((-a-b)t).
Then the exact operator identity is

    P_L(T-T_X)P_L
      =-(tau_X/2)(|u_+><u_-|+|u_-><u_+|).                 (4)

### Proof

On this square, |t-u|<=L<log n for each omitted n. Therefore the bracket
in (1) is 2n^(-b)cosh(b(t-u)). Since b+1/2=2, the complete omitted kernel
is -tau_X exp(-a(t+u))cosh(b(t-u)). Expanding cosh proves (4). Absolute
convergence justifies the infinite sum before factorization. A retained
atom at log n=L causes no exception: it is not in the omitted set.

This is an EXACT completion of the compact-window arithmetic source,
not a continuum approximation and not a new positivity assertion.
The infinite tail uses one number evaluated at the safe point s=2.
On a translated interval [r,r+L], the corresponding operator is multiplied
by exp(-2ar) under translation; the difference kernel remains W.

### Exact error norm and inertia

Write

    A_L=(exp(bL)-1)/b,
    B_L=(1-exp(-3bL))/(3b),
    C_L=(1-exp(-bL))/b.                                    (5)

These are respectively ||u_+||^2, ||u_-||^2, and <u_+,u_->.
Strict Cauchy--Schwarz gives A_L B_L>C_L^2 for L>0. The two nonzero
eigenvalues of (4) are

    -(tau_X/2)(C_L+sqrt(A_L B_L)),
     (tau_X/2)(sqrt(A_L B_L)-C_L).                          (6)

Consequently

    ||P_L(T-T_X)P_L||_1=tau_X sqrt(A_L B_L),
    ||P_L(T-T_X)P_L||=(tau_X/2)(C_L+sqrt(A_L B_L)).          (7)

The tail has one positive and one negative eigenvalue. It is not a
positive correction. A scalar interval error of width eta in tau_X has
trace-norm error at most eta sqrt(A_L B_L), by the same exact calculation.
Neither a pointwise kernel bound nor the global tail ceiling is needed.

### A finite-prime formula on every finite interval

For x>=0, reorganizing each atom on the two sides of x=log n gives

    W(x)=exp(x/2)/2+C_b exp(-bx)+S_gamma(x)
          -(P_2/b)cosh(bx)
          +(1/b)sum_(2<=n<=exp x) Lambda(n)/sqrt(n)
                          sinh(b(x-log n)),               (8)
    S_gamma(x)=sum_(j>=1) exp(-c_j x)/(c_j^2-b^2).

At equality the added sinh term is zero. Its derivative has jump
Lambda(n)/sqrt(n). Thus the exact local formula has a finite prime sum,
one safe scalar, and a classical gamma function. It still contains all
arithmetic data needed on that interval, rather than discarding a tail.

## 3. LW-2: the raw global prime-cutoff exponent 1/4 is sharp

The classical PNT implies Psi(x)=sum_(n<=x)Lambda(n)~x. For every fixed
s>1, Stieltjes integration by parts on (X,infinity) gives

    sum_(n>X)Lambda(n)n^(-s)
      =-Psi(X)X^(-s)+s int_X^infinity Psi(t)t^(-s-1)dt
      ~ X^(1-s)/(s-1).                                    (9)

The lower endpoint is retained, and the PNT error is uniform for t>=X
in the asymptotic epsilon argument. In particular tau_X~1/X.
At L=log X, formulas (5)--(7) give

    ||P_(log X)(T-T_X)P_(log X)||_1
          ~ [2/(3sqrt(3))] X^(-1/4),
    ||P_(log X)(T-T_X)P_(log X)||
          ~ [1/(3sqrt(3))] X^(-1/4).                       (10)

Compression is contractive for both norms. The parent's atom estimate is

    ||T_n||_1 <= c_* Lambda(n)n^(-5/4),
    c_*=(1+1/sqrt(3))/b.

Combining this estimate, (9) with s=5/4, and (10) proves

    2/(3sqrt(3))
      <=liminf_(X->infinity) X^(1/4)||T-T_X||_1
      <=limsup_(X->infinity) X^(1/4)||T-T_X||_1
      <=(8/3)(1+1/sqrt(3)).                                (11)

Thus ||T-T_X||_1=Theta(X^(-1/4)); it cannot be o(X^(-1/4)) for this raw
arithmetic truncation. There is no claim that the GLOBAL scaled norm has
a limit or equals the lower constant. The operator norm has the analogous
positive lower bound in (10) and the upper bound from (11).
For a fixed L, the exact local error instead decays as sqrt(A_L B_L)/X.
These are approximation rates, not RH or zero-free estimates.

## 4. LW-3: an actual full-source sum of squares, on diameter 1/20

Let L0=1/20. For EVERY nonzero f in L2(0,infinity) supported in an
interval of length at most L0,

    <f,Tf> > 0.                                            (12)

This concerns all functions in an infinite-dimensional subspace, not
finitely many vectors or a finite positive matrix. It is a LOCAL theorem.
The interval length is explicit, conservative, and not claimed optimal.

### 4.1 Exact evaluation of the prime-free local expression

Since L0<log 2, the finite sum in (8) is empty on [0,L0], but its
infinite arithmetic tail is retained in P_2. For x>0 put v=exp(-x).
The exact partial-fraction identity

    1/(c_j^2-b^2)=1/[3(2j-1)]-1/[6(j+1)]

sums the gamma series to

    S_gamma(x)=[exp(-bx)log((1+v)/(1-v))
                +exp(bx)log(1-v^2)+exp(-x/2)]/6,            (13)
    S_gamma'(x)=[-exp(-bx)log((1+v)/(1-v))
                 +exp(bx)log(1-v^2)+exp(-x/2)]/4.           (14)

The apparent divergence at x=0 cancels; S_gamma(0)=1/6+log(2)/3.
These formulas follow by summing the two ordinary logarithm series for
0<v<1 and differentiating there. At x=0 continuity follows from the
original absolutely convergent coefficient series.

The rational checker proves the actual-source bounds

    0<P_2<3/5,       -1/2<C_b<0,
    1/250<W(L0)<1/200,       W'(L0)<-1/3.                  (15)

No prime sample or zero information is input. Section 5 supplies the
analytic remainder contract behind the finite arithmetic certificate.

### 4.2 Positivity of the curvature, at every point in the interval

For 0<x<=L0, direct differentiation of the original gamma series gives

    W''(x)=exp(x/2)/8+b^2 C_b exp(-bx)
       +sum_(j>=1) [c_j^2/(c_j^2-b^2)]exp(-c_j x)
       -b P_2 cosh(bx).                                   (16)

The positive sum is at least

    exp(-5x/2)/(1-exp(-2x))
       >=(1-(5/2)L0)/(2L0)=35/4.

Also cosh(bL0)<101/100, certified by its convergent exponential series.
Using (15), dropping the first positive term, and keeping inequality
orientations gives

    W''(x) >=35/4-9/8-(9/10)(101/100)>6.                   (17)

This is a uniform analytic inequality, not a grid check. Moreover
c_j^2/(c_j^2-b^2)<=25/16, so W''(x)=O(1+1/x) near zero.
Thus int_0^L0 t W''(t)dt is finite. W' may diverge logarithmically at
zero; it is not assumed bounded there.

### 4.3 The factorization and a quantitative lower bound

Set p=-W'(L0)>1/3, delta=W(L0)>1/250. Twice integrating W'' gives,
for 0<=s<=L0,

    W(s)=delta+p(L0-s)+int_s^L0 (t-s)W''(t)dt.              (18)

The formula at zero follows by continuity and the preceding integrability.
For h supported in an interval of length at most L0, extend it by zero
and put

    Q_t(h)=int_R |int_r^(r+t) h(u)du|^2 dr.

Fubini gives the exact triangle-kernel identity

    Q_t(h)=int int (t-|u-v|)_+ conjugate(h(u))h(v)dudv >=0.

Since every pair in the support has separation at most L0, (18) implies

    int int W(u-v)conjugate(h(u))h(v)dudv
      =delta |int h|^2+p Q_L0(h)+int_0^L0 W''(t)Q_t(h)dt.   (19)

All three terms are nonnegative. Absolute Fubini follows from
Q_t(|h|)<=t^2||h||_2^2 and W''(t)=O(1/t). This is a genuine full-source
sum of squares on the stated support class.

For an explicit coercivity estimate translate h to [0,L0] and write

    M=int_0^L0 h(t)dt, H(t)=int_0^t h(u)du.

An independent primitive calculation gives

    Q_L0(h)=(L0/2)|M|^2+2int_0^L0 |H(t)-M/2|^2dt.

Consequently the left side of (19) is at least

    (37/3000)|M|^2+(2/3)int_0^L0 |H(t)-M/2|^2dt.           (20)

To recover (12), set h(t)=exp(-at)f(t) before translation and multiply
(19)--(20) by b. Thus the explicit lower bound for <f,Tf> is

    (37/2000)|M|^2+int_0^L0 |H(t)-M/2|^2dt >0              (21)

unless f=0. If the expression vanished, M=0 and H=0 almost everywhere;
H is absolutely continuous and h=H'=0 almost everywhere. The damping
is invertible on each finite interval. This proves strict positivity for
all the stated L2 functions. No uniform positive L2 eigenvalue gap is
claimed: the right side is a weaker primitive norm, as compactness requires.

### 4.4 This also gives a positive extension, but not the actual global source

Let ell=L0+delta/p. Bounds (15) give ell<1/10. Define on the whole line

    W_ext(x)=p(ell-|x|)_+
             +int_0^L0 (t-|x|)_+ W''(t)dt.                 (22)

This is globally positive definite by the same triangle factorization,
and agrees exactly with W for |x|<=L0. However W_ext is zero for
|x|>=ell, whereas the same source certificate proves

    W(1/10)<-1/200.                                        (23)

Thus W_ext is NOT the actual full arithmetic W. Local positive extension
cannot be identified with the required global source. Negative W(1/10)
is NOT evidence against positive definiteness: positive-definite kernels
can take negative pointwise values. It only stops this particular
nonnegative convex continuation from being the global arithmetic solution.

## 5. The rational certificate's analytic contract

All finite signs in (15), (17), and (23) are recomputed with rational
outward interval operations on the grid 10^(-40). No floating-point or
special-function library enters acceptance. Put N=32 and m=6.

Euler--Maclaurin for zeta has remainder

    R(s)=-(s)_12/12! int_N^infinity B_12({x})x^(-s-12)dx.

The standard periodic Bernoulli bound |B_12({x})|<=|B_12| and the circle
|s-2|=1/4 give

    |R(s)|<=r0=|B_12|prod_(j=0)^11(j+9/4)/(12! *12*N^12).

Indeed Re s>=7/4, so the actual integral bound is smaller than N^-12/12.
Cauchy then bounds |R(2)| by r0 and |R'(2)| by 4r0. The finite expressions
used are

    Z=sum_(n<N)n^-2+1/N+1/(2N^2)
        +sum_(k=1)^6 B_(2k)/N^(2k+1),
    Z'= -sum_(n<N)log(n)n^-2-(log N+1)/N-log N/(2N^2)
        +sum_(k=1)^6 [B_(2k)/N^(2k+1)](H_(2k)-1-log N).

Thus -(Z'+error)/(Z+error) encloses P_2. The denominator interval is
strictly positive. Euler's constant is enclosed by

    H_(N-1)-log N+1/(2N)+sum_(k=1)^6 B_(2k)/(2k N^(2k))

with error at most |B_12|/(12 N^12). This follows from the usual real
Euler--Maclaurin integral remainder for the harmonic sum.

Pi uses 16 atan(1/5)-4 atan(1/239), with 50 alternating terms and the
next-term enclosure for each arctangent. Logarithms use power-of-two
reduction and 60 terms of 2sum y^(2j+1)/(2j+1), |y|<=1/3, with its
positive geometric-tail bound. Exponentials use scaling to 0<=x<=1,
60 Taylor terms with a geometric remainder, squaring, and reciprocation
for negative arguments. Monotonicity encloses logarithms of interval
arguments in (13)--(14). Those arguments are strictly positive.
The analytic identities and remainders remain subject to mathematical
review; the checker verifies their finite instances, not their own proof.

## 6. Outcome of the continuation

Proved components: exact finite-window prime-tail completion, its complete
rank-two norm/inertia, sharp global raw-cutoff exponent, and strict positivity
of the FULL source on every support interval of diameter at most 1/20.

Not proved: positivity on unbounded window lengths, an all-section sign,
the original d_n or c_n subexponential bound, or RH. Arbitrarily translated
short intervals do not control cross terms between separated intervals.
The positive extension (22) is deliberately not substituted for W.

This does not conflict with the parent's all-cutoff negative witness:
its support length is 30(1+log X), much LONGER than the log X locality
window. Exact truncation, local correction, and source compression remain
different operations. General small-support Weil positivity is classical;
no first-in-literature claim is made for that phenomenon. The work here
is the explicit resolvent-source factorization, quantitative interval,
exact tail completion and sharp cutoff rate in the inherited normalization.
