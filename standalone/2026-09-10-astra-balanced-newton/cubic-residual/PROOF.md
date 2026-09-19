# CIR26 — cubic residual cancellation with a complete logarithmic diagonal

**PROPOSED component proofs. RH and the native all-scale covariance estimate
remain OPEN.** Date: 2026-09-10. Parent: PR848 at
`098acb780655eb81f8b842be201596a50198e757`.

This is an alternative arithmetic scale map, not a promotion of the parent's
quadratic sign conjecture. It advances an exact prefix from Y to (Y+1)^3-1
and allows cancellation BETWEEN the quadratic and cubic inverse terms. All
same-product interactions, including interactions between the two degrees,
are combined before defining the diagonal. The diagonal is polylogarithmic
at every scale, by an elementary finite hyperbola estimate.

The residual-polynomial identity is classical (see Huxley–Watt 2018 and its
Linnik/Vaughan predecessors). Harmonic hyperbola decomposition, projections,
and divisor-counting inequalities are also classical. No general novelty
claim is made for those ingredients. The contribution here is their explicit
combination in the bounded-completion native-energy interface, the complete
cubic diagonal estimate, and the correctly scoped cancellation target.

## 0. Objects, clocks, and what is a finite source

Let mu be the ordinary Mobius function, and define

    m(k)=sum_(n<=k) mu(n)/n, F_Y=sum_(k=1)^Y m(k)^2,
    b=Y+1, B=b^3-1.

For a finite real arithmetic source a, use

    P_a(s)=sum a_n n^(-s), A_a(x)=sum_(n<=x)a_n,
    J(a)=integral_1^infinity A_a(x)^2 dx/x^2.

Its whole future is included. The exact identity

    J(a)=sum_(k>=0)(P_a(1)-sum_(n<=k)a_n/n)^2                 (0.1)

follows from 1/max(r,s)=min(r,s)/(rs), including k=0. Thus at P_a(1)=0,
the reciprocal partial sums are orthonormal coordinates. This is inherited
motivation from NIR26, not a new attribution; the kernel argument proves it.
Dirichlet convolution is *, its identity is delta, and 1(n)=1.

Throughout, logarithms are natural. H(x)=sum_(n<=x)1/n (zero for x<1), and

    H2(x)=sum_(uv<=x)1/(uv)=sum_(n<=x)tau_2(n)/n.

The polynomial subscript 2 here counts divisor factors, not a second moment.

## 1. CIR26-1: retain the bounded native input, with its actual energy price

Preserve c_n=mu(n) for n<=Y. Put a=|m(Y)|, epsilon=sign(m(Y)), r_0=a.
Until r_j first reaches zero set

    c_(Y+j)=-epsilon min(3,(Y+j)r_(j-1)),
    r_j=max(0,r_(j-1)-3/(Y+j));                            (1.1)

all later coefficients are zero. If m(Y)=0 add nothing. Let L be Y or the
last added index. Then

    |c_n|<=3, P_c(1)=0, L<=Y+ceil(Y/2)<=2Y,
    F_Y<=J(c)<=2F_Y.                                      (1.2)

Here is the complete reused argument. Divisor inversion gives
Y m(Y)=1+sum_(d<=Y)mu(d){Y/d}, whence |m(Y)|<=1. The first ceil(Y/2)
correction slots have reciprocal capacity at least one. For each such j,
3/(Y+j)>=1/(Y-j+1). Consequently the remaining reciprocal magnitude satisfies

    r_j <= (|m(Y)|-sum_(i=1)^j1/(Y-i+1))_+ <= |m(Y-j)|.

Squaring and summing charges the entire new tail to F_Y. Identity (0.1)
proves (1.2). No future Mobius coefficient is supplied to this procedure.
This is the same clipped completion as PCR26, not a new optimum claim.

## 2. CIR26-2: cancel the residual to third order and recomplete exactly

Define finite product coefficients z2=c*c and z3=c*c*c, and the generally
infinite formal arithmetic sequence

    v=3c-3(1*z2)+(1*1*z3).                                (2.1)

For e=delta-1*c, multiplication in the arithmetic convolution ring gives

    v=c*(delta+e+e*e), mu-v=mu*e*e*e.                      (2.2)

Since e(n)=0 for n<b,

    v(n)=mu(n) for EVERY n<b^3,
    mu(b^3)-v(b^3)=e(b)^3.                                (2.3)

Every coefficient computation is finite, since only divisors of its index
occur. The equality at b^3 is an error formula, not an extra matched index.
All late completions of the same prefix give the SAME reproduced prefix.
The more general order-r identity c*sum_(j=0)^(r-1)e^j=mu-mu*e^r is classical;
this paper uses r=3 because its complete diagonal admits the elementary
logarithmic estimate below.

### Finite restriction is followed by an explicitly paid whole completion

Compute v(n) only for 1<=n<=B. Define a NEW finite source

    a_n=v(n) (n<=B), a_(B+1)=-(B+1)sum_(n<=B)v(n)/n.       (2.4)

Then P_a(1)=0 and J(a)=F_B exactly: its reciprocal coordinates vanish after B.
For another bounded-input round, apply (1.1) to this newly generated prefix;
its ENTIRE energy is at most 2F_B. Neither operation assumes a bound for the
infinite raw sequence (2.1). We do NOT call finite restriction an orthogonal
projection of v in a Hilbert space unless v's membership is separately proved.
The two-moment raw-Newton domain proof from the original packet is not silently
reused for this different degree. No raw future is declared zero; our state
is the finite completed source (2.4), or its bounded counterpart.

The cubic ladder starts 1,7,511,134217727,... . Only the first two extensions
on that ladder are replayed here. Additional complete single-stage checks at
other Y are explicitly identified; they are not relabelled later ladder stages.

## 3. CIR26-3: the entire elementary harmonic-hyperbola error

Let gamma=lim(H(n)-log n). Elementary integral bounds give 0<gamma<1 and

    |r1(x)|<=1/x for x>=1, r1(x)=H(x)-log x-gamma.          (3.1)

Let

    gamma1=lim_(u->infinity)(sum_(n<=u)log(n)/n-(log u)^2/2).

This limit exists and |gamma1|<1. To see this, f(t)=log(t)/t has
integrable |f'|, with integral_1^infinity |f'|=2/e<1.
Write the limit as sum_(n>=1)[f(n)-integral_n^(n+1)f(t)dt]. For integer u,

    |sum_(n<=u)log(n)/n-(log u)^2/2-gamma1|
         <=2(1+log u)/u.                                 (3.2)

The tail sum is bounded by integral_u^infinity |f'|, and the remaining
endpoint term is f(u). This proves the stated constant without any theorem
about primes or a nontrivial divisor-error exponent.

Define

    p2(t)=t^2/2+2gamma*t+gamma^2-2gamma1,
    r2(x)=H2(x)-p2(log x).

Then

    |r2(x)|<=16(1+log x)/sqrt(x), x>=1;
    |r2(x)|<=3(1+log(1/x))^2, 0<x<1.                      (3.3)

Proof: put u=floor(sqrt x), t=log x, w=log u. The EXACT hyperbola identity is

    H2(x)=2sum_(a<=u)H(x/a)/a-H(u)^2.

Insert H(x/a)=log(x/a)+gamma+r1(x/a). Its error is <=2u/x.
Write H(u)=w+gamma+epsilon with 0<epsilon<1/u, and use (3.2), with error eta.
After cancelling the polynomial main terms, the remaining expression is

    -2(w-t/2)^2+2(t-w)epsilon-epsilon^2-2eta+error.

Since |w-t/2|<=1/u, u>=sqrt(x)/2, and w<=t/2, its absolute value is at most

    3/u^2+(3t+4)/u+2u/x <= (16+6t)/sqrt x.

This proves the first line. The second follows directly from H2(x)=0,
0<gamma<1 and |gamma1|<1. No asymptotic formula with an unbounded remainder
is being used at a finite endpoint.

### Center the new packets exactly

For integers d,k>=1 put

    K_d(k)=[H(k/d)-H(k)+log d]/d,
    L_d(k)=[H2(k/d)-H2(k)+(log d)(H(k)+gamma)
                                   -(log d)^2/2]/d.      (3.4)

K is the parent's packet; L is the new second-divisor packet. L_1=K_1=0.
Precisely,

    d L_d(k)=r2(k/d)-r2(k)+(log d)r1(k).                  (3.5)

In particular gamma1 cancels and is NOT a numerical input to the checker.

For EVERY integer cutoff X>=1 and EVERY d>=1,

    sum_(k=1)^X K_d(k)^2 <=18/d,
    sum_(k=1)^X L_d(k)^2 <=3300(1+log X)^3/d.             (3.6)

For K, extend r1 to x<1 by r1(x)=-log x-gamma. A decreasing integral
gives sum_(k>=1)r1(k/d)^2<=7d: the small-argument part is at most 5d
and the reciprocal-square tail at most 2d. Since
K_d(k)=[r1(k/d)-r1(k)]/d and sum r1(k)^2<=2, its complete squared norm
is at most 14/d+4/d^2<=18/d. Thus the K estimate holds with X=infinity.
The L estimate here is FINITE-HORIZON and retains its logarithm; it is not
a uniform infinite-tail theorem.

For completeness, sum the small-argument bound in (3.3) by a decreasing
integral: integral_0^1 (1+log(1/t))^4 dt=65. Hence

    sum_(k=1)^X r2(k/d)^2 <=[585+256(1+log X)^3]d
                           <=841d(1+log X)^3.

The large-argument part uses sum_(k=d)^X(1+log(k/d))^2/k
<= (1+log X)^2 H_X. Also sum r2(k)^2<=256(1+log X)^3 and sum r1(k)^2<=2.
Square (3.5) using three times the sum of squares. Since (log d)^2<=d,
the resulting constant is 3*841+3*256+6=3297<3300. This proves (3.6).

## 4. CIR26-4: combine Newton degrees BEFORE the collision diagonal

P_c(1)=0 implies the exact product moments

    sum_d z2(d)(log d)^j/d=0, j=0,1;
    sum_d z3(d)(log d)^j/d=0, j=0,1,2.                    (4.1)

These follow by differentiating the finite polynomials P_c(s)^2 and P_c(s)^3
at s=1. Equivalently, zeroth, prime-valuation, and prime-pair-valuation sums
vanish rationally. The implementation checks the latter, not an approximate
floating equality of logarithms.

Set z2(d)=0 or z3(d)=0 beyond the corresponding supports, and define ONE
combined atom per integer product:

    a_d(k)=z3(d)L_d(k)-3z2(d)K_d(k),
    S_Y(k)=sum_(d<=L^3)a_d(k).                            (4.2)

All quadratic and cubic contributions at the SAME d are combined, including
their internal cross term. This is not a diagonal over uncoalesced ordered
factorizations or artificially independent Newton degrees.

The moment identities give the exact, rational aggregate

    S_Y(k)=sum_d z3(d)H2(k/d)/d-3sum_d z2(d)H(k/d)/d,
    sum_(n<=k)v(n)/n=3m_c(k)+S_Y(k).                      (4.3)

On the entire native annulus b<=k<=B, the left side is m(k).
Let

    D_Y^(3)=sum_d sum_(k=b)^B a_d(k)^2,
    C_Y^(3)=sum_(d!=e)sum_(k=b)^B a_d(k)a_e(k),
    T_Y=sum_(k=b)^B m_c(k)^2, W_Y=sum_(k=b)^B m_c(k)S_Y(k).

C is ORDERED and signed. Then

    F_B=F_Y+9T_Y+D_Y^(3)+C_Y^(3)+6W_Y,                   (4.4)
    F_B<=19F_Y+2D_Y^(3)+2C_Y^(3).                        (4.5)

Indeed T_Y<=F_Y by the paid trace, and (3t+S)^2<=18t^2+2S^2.
No sign assumption on C was used: D+C=||S||^2 is nonnegative.

### Every same-product contribution is polylogarithmic

For j=2,3, |zj(d)|<=3^j tau_j(d), and

    tau_j(d)^2<=tau_(j^2)(d).

One proof prime-power by prime-power: a pair of j-part compositions of an
exponent gives two margins of a j-by-j nonnegative matrix; choose the canonical
northwest filling. Different margin pairs give different matrices. The number
of matrices with total e is binomial(e+j^2-1,j^2-1). This supplies the required
injection, rather than an assumed divisor-function inequality.
Consequently sum_(d<=L^j)zj(d)^2/d<=3^(2j) H_(L^j)^(j^2).
Using (u-3v)^2<=2u^2+18v^2 and (3.6),

    D_Y^(3) <= 4,811,400(1+log B)^3 H_(L^3)^9
                        +26,244 H_(L^2)^4
              =: A_Y^(3) = O((1+log Y)^12).               (4.6)

This holds for every native scale, in fact for every finite coefficient-cap-3
source with the stated support and moment. The constant is intentionally
conservative; reducing it does not establish the missing signed estimate.

## 5. CIR26-5: an alternative full-RH ending, and what is not proved

On the cubic ladder Y_j=2^(3^j)-1, either an eventual nonpositive C_Y^(3),
or an eventual fixed-polylog upper bound on it, gives by (4.5)--(4.6)

    F_X=O((1+log X)^K) for some fixed K.

For the nonpositive case K=12 suffices, since 19<3^12. Between consecutive
ladder points their log sizes differ by at most a factor 3, and F is monotone.
More generally a bound

    1+F_(b^3-1)<=C(1+log b)^K (1+F_(b-1))^(3-delta),
    0<delta<2 fixed,                                    (5.1)

would give log(1+F_X)=O((log X)^theta), with
theta=log_3(3-delta)<1. Indeed the logarithmic recurrence has a fixed
homogeneous factor 3-delta>1 and an additive O(j) loss at stage j.
No instance of (5.1) is proved here.

A subpower upper bound on (C_Y^(3))_+ along this ladder is sufficient by (4.5)
and the logarithmic diagonal. Conversely

    (C_Y^(3))_+ <= ||S_Y||^2 <=2(F_B-F_Y)+18T_Y<=18F_B.    (5.2)

Thus this cancellation target retains the strength of the earlier native
energy target. Higher order is a different attack surface, NOT proof that
its source-specific estimate is easier or already settled.

For clarity, the complete implication from subpower F to RH is as follows.
With M(k)=sum_(n<=k)mu(n), direct finite summation by parts yields

    E_Y=sum_(k<=Y)M(k)^2/[k(k+1)]
        =F_Y-(Y+1)[(sum_(k=0)^Y m(k))/(Y+1)]^2 <=F_Y.

Hence integral_1^X M(x)^2/x^2 dx is subpower. On each dyadic interval,
Cauchy--Schwarz gives absolute convergence of

    G(s)=integral_1^infinity M(x)x^(-s-1)dx, Re s>1/2,

uniformly on compact subsets: the interval contribution is O(2^(-j eta/2))
when Re s>=1/2+eta, after choosing a sufficiently small energy exponent.
For Re s>1, G(s)=1/[s zeta(s)] by ordinary summation by parts. Therefore the
holomorphic identity (s-1)zeta(s)*sG(s)=s-1 continues to Re s>1/2, handling
the pole at one removably. A zeta zero in that half-plane would contradict
this identity. The classical functional equation reflects the other half.

THE UNPROVED STEP is the all-scale native cancellation bound on C_Y^(3), or
an alternative subcubic gain. Finite negative panels below do not supply it.
The quadratic covariance C_Y from PCR26 and this cubic mixed-degree covariance
are DIFFERENT objects with different annuli; their numbers are not combined.

## 6. CIR26-6: the coefficient cap and safe moment do not force a gain

Use the same clipped completion for the NON-NATIVE prefix c_1=1 and
c_n=0 for 2<=n<=Y. It still has |c_n|<=3, P_c(1)=0, support<2b, and
J(c)<=2Y. Let beta_r=-c_r/r on its tail. Then beta_r>=0 and sum beta_r=1.

There are constants c>0 and b0, independent of Y, for which its cubic output
has annular reciprocal energy >=c b^3 for every b>=b0. Thus there is no generic
subcubic native-style bound on this coefficient/moment/energy class.

Here is an all-parameter proof, not a fitted numerical trend. Take integer k
in [2^(-16)b^3,2^(-15)b^3]. For b sufficiently large, every product with at most
TWO tail indices is <=k, and every product of THREE tail indices is >k.
For each included triple, k/d>=b/2^18, so (3.3) gives a uniform o(1) error
in replacing H2(k/d) by p2(log(k/d)); total absolute reciprocal coefficient
mass is <=(sum |c_n|/n)^3=8. The analogous H error in the quadratic term is
o(1), with total mass <=4. All logarithmic polynomial terms cancel by (4.1).
Consequently, uniformly on this interval,

    sum_(n<=k)v(n)/n
       =sum_(r,s,t tail)beta_r beta_s beta_t
                            p2(log(k/(rst)))+o(1).        (6.1)

For these missing triples, log(rst/k)>=15 log2>10, while
p2(-u)>=u^2/2-2u-3>=27 for u>=10. Their weights sum to one.
Thus the output is >=26 eventually throughout an interval containing
at least 2^(-17)b^3 integers. In particular its energy is >=2^(-17)b^3
for all sufficiently large b. This is an explicit asymptotic lower constant;
a practical first b0 is not evaluated or claimed tested.

Combining with (4.6) shows C_Y^(3)=Omega(Y^3) for this family as well:
S equals the output on the displayed interval because the source tail has
ended, and D is only polylogarithmic. The fake prefix violates native divisor
inversion already at n=2. This does NOT refute the native covariance target
or RH. It proves that even the cubic cancellation must use the full arithmetic
constraints, not just normalizations or a broad coefficient norm.

## 7. Evidence and next mathematical task

The two implementations rederive the whole declared FINITE coefficient outputs,
all coalesced product lists and their rational valuation moments, harmonic
hyperbola identities, and directed finite covariance panels. No all-scale
sign is extrapolated. The analytic proof of (3.6) is finite-horizon; the state
completion (2.4), not an assumed uniform raw-stage tail, supplies whole physical
energy. SOURCE_LOCK.json and VALIDATION.md distinguish all these scopes.

The next real theorem must bound the NATIVE mixed-degree sum C_Y^(3) before
absolute values erase cancellation, or give a subcubic source-relative bound.
The complete divisor constraints characterize its input. A higher-order
identity, logarithmic diagonal, or finite list of signs is not that theorem.
