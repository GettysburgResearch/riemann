# The actual signed correlations of the fixed-shift source

Status: PROPOSED exact deductions and one finite certificate. Ordinary zeta
only: F=Q and S empty. The deep logarithmic two-point correlation theorem
of Tao is explicitly imported in Section 3; it is not proved by our checker.
No estimate for the COMPLETE off-diagonal energy at RH strength is claimed.

## 1. The full, untruncated Gaussian Gram kernel

Keep a(n)=n^(-1) product_(p|n)(1-p), S(X)=sum_n a(n)W_c(n/X), and set

    v=c-1/2, C_c=exp(2v^2)/(2 sqrt(2 pi)),
    Phi(u)=(1/sqrt(2 pi)) integral_(-infinity)^u exp(-t^2/2)dt,
    K_T(n,m)=C_c (nm)^(-1/2) exp[-log(n/m)^2/8]
                    Phi(log T-(log n+log m)/2-2v).

For EVERY finite T>0,

    E(T)=integral_0^T |S(X)|^2 dX/X^2
                       =sum_(n,m>=1) a(n)a(m)K_T(n,m). (1)

Every double sum in (1), and every subseries used below, converges absolutely
at finite T. To prove this, use Tonelli on the positive Gaussian majorant
with |a(n)|<=1; its source grows at most O_c(X) at infinity and is flat at
zero. On x=log X, each normalized summand is

    n^(-1/2) psi(log n-x),
    psi(u)=exp[-vu-u^2/4]/(2 sqrt(pi)).

Completing the square in the product of two psi functions and integrating
x<=log T gives precisely K_T. In particular the Gaussian ratio factor,
the mean log norm, the normalization 1/sqrt(nm) and the shift 2v all belong
to the exact kernel. It is not a kernel for a sharp ideal cutoff.

## 2. An unconditional diagonal asymptotic with an explicit Euler constant

Define

    C_a=product_p (1-3/(p^2+p+1)) > 0.                  (2)

Then for every fixed 1/2<theta<1,

    sum_(n<=x) a(n)^2 = C_a x + O_theta(x^theta),
    sum_(n<=x) a(n)^2/n = C_a log x + O(1).             (3)

Consequently the complete diagonal in (1) satisfies

    D(T)=sum_n a(n)^2 K_T(n,n)=C_c C_a log T+O_c(1).     (4)

Proof. For Re s>1, the local squared-coefficient series is

    F_p(s)=1+(p-1)^2 p^(-s-2)/(1-p^(-s-2)).

Hence sum_n a(n)^2 n^(-s)=zeta(s)G(s), where

    G_p(s)=(1-p^(-s))(1+(1-2/p)p^(-s))/(1-p^(-s-2)).   (5)

The nonconstant local coefficients have absolute sum O(p^(-sigma-1)+
p^(-2sigma)) for each fixed sigma>1/2. Thus G has an absolutely convergent
Dirichlet series sum g(d)d^(-s) in that half-plane. Convolve with 1 and use
floor(x/d)=x/d+O(1); the truncated rounding error and the d>x main tail are
both O_theta(x^theta). At s=1,

    G_p(1)=(p-1)(p+2)/(p^2+p+1)=1-3/(p^2+p+1),

proving the first part of (3). Partial summation proves the second with a
bounded constant (indeed with a power-decaying remainder after its constant
is extracted). All factors in (2) are positive and their deficits summable.

Finally (4) is Gaussian smoothing on the logarithmic variable of the second
formula in (3): write the Phi factor as an integral of the normal density
and interchange absolutely. Its convolution with the linear function log x
changes it by a fixed constant, while its tail below x=1 is bounded. QED.

## 3. Every fixed additive band has a proved signed asymptotic

### Theorem 3

For each FIXED integer k>=1,

    sum_(n<=x) a(n)a(n+k)/n=o_k(log x).                 (6)

It follows that for every FIXED integer K>=0,

    sum_(|n-m|<=K) a(n)a(m)K_T(n,m)
                                = C_c C_a log T+o_K(log T). (7)

There is no claimed rate uniform in K, no polynomially growing K range,
and no inference from (7) to (1)'s full energy bound.

Proof of (6), with the exact imported theorem. Tao's published Corollary 5
in *The logarithmically averaged Chowla and Elliott conjectures for two-point
correlations*, Forum of Mathematics, Pi 4 (2016), e8, applies to 1-bounded
multiplicative functions whose first member satisfies its uniform strong
nonpretentiousness condition (8). The text immediately following that
corollary verifies the condition for Liouville. Our a is multiplicative and
1-bounded, and a(p)=-1+1/p. Its prime distance in that condition differs from
Liouville's by at most sum_p 1/p^2, uniformly in the Dirichlet character and
the whole allowed t range. Thus the same divergent lower bound holds. Apply
the corollary with a1=a2=1, b1=0, b2=k and omega(x)=x. This proves (6).
The entropy-decrement proof is an EXTERNAL input. No version of natural-
density two-point Chowla or uniform growing-shift cancellation is imported.

To obtain (7), fix k. The difference between K_T(n,n+k)/C_c and

    n^(-1) Phi(log T-log n-2v)

is O_k(n^(-2)), uniformly in T. This follows from log(1+k/n)=O_k(1/n),
the bounded derivative of Phi, and the factor 1/sqrt(n(n+k)); the finitely
many small n cause only O_k(1). Therefore the off-diagonal ray of offset k
differs by O_k(1) from the Gaussian smoothing of the partial sums in (6).
Those partial sums are o(log x) and bounded by log x+O(1). Dominated
convergence against the Gaussian proves that the smoothed sum is o(log T).
Sum the finitely many offsets and add (4). QED.

## 4. All integer-divisibility rays can be summed: the result is NEGATIVE

Define the multiplicative function beta by

    beta(1)=1,
    beta(p^j)=-(p^2-1)/(p^j(p+2)), j>=1.               (8)

For each FIXED integer r>=1, an elementary Euler calculation gives

    sum_(n<=x) a(n)a(rn)/n = C_a beta(r) log x+O_r(1). (9)

To see this, at a prime with p^j||r the local series is

    a(p^j) + sum_(ell>=1) a(p^ell)a(p^(ell+j))p^(-ell s).

At s=1, its value divided by F_p(1) in Section 2 is exactly (8). The
finitely many altered factors leave a zeta(s) times absolutely convergent
Dirichlet series for Re s>1/2, so the same convolution and partial-summation
argument proves (9). This proof includes shared primes of n and r; replacing
them by coprime indices would give the wrong beta.

Let Div(T) be the COMPLETE sector of (1) whose two indices are comparable
by divisibility, with the diagonal included once:

    Div(T)=sum_(n|m or m|n) a(n)a(m)K_T(n,m).

### Theorem 4

The following absolutely convergent constant exists:

    L_div=1+2 sum_(r>=2) beta(r) r^(-1/2) exp[-(log r)^2/8]. (10)

It satisfies the certified strict inequalities

                         -21/10 < L_div < -7/5,        (11)

and the full infinite sector has asymptotic

    Div(T)=C_c C_a L_div log T+o(log T).                 (12)

Thus this is a genuine negative signed contribution to the complete positive
energy. No claim that an incomplete sector of a Gram matrix is positive is
being made. Its complement must compensate at logarithmic order.

Proof of (12). For fixed r, insert m=rn into K_T and apply (9), smoothed by
Phi, to obtain

    sum_n a(n)a(rn)K_T(n,rn)
      = C_c C_a beta(r) r^(-1/2) exp[-(log r)^2/8] log T
                                                       +O_r(1).

To pass to all r, do NOT sum the O_r constants. Since |a|<=1, the absolute
value of the smoothed harmonic sum over n, before the factor r^(-1/2)
exp[-(log r)^2/8], is bounded by C_c'(1+log T), uniformly in r>=1 and
T>=2: increasing r only lowers the argument of Phi. The factor is summable
over all r, even without cancellation. Dominated convergence after division
by log T proves (12). Diagonal r=1 is counted once and r>=2 twice.

Proof of the finite certificate (11). Since |beta(r)|<=1 and
w(t)=t^(-1/2)exp[-(log t)^2/8] is decreasing for t>=1,

    2 sum_(r>N) |beta(r)|w(r)
      <=2 integral_N^infinity w(t)dt
      <=8 exp[1/2-(log N-2)^2/8]/(log N-2), N>e^2.     (13)

The second inequality is the elementary Gaussian tail bound obtained from
u>=log N-2 in the derivative of exp(-u^2/8). The executable certificate
uses N=512, exact rational beta values, outward dyadic interval arithmetic,
an atanh series with an explicit logarithm tail, and alternating Taylor
bounds for exp(-x) after fixed range reduction. It encloses the finite
part in (10) and adds BOTH signs of the whole tail (13). Its final interval
lies strictly within (-21/10,-7/5). It never substitutes a finite sum for
the infinite sector or samples an unproved asymptotic. The arithmetic
constant C_a is positive by its convergent Euler product; no numerical
evaluation of it is needed for the sign. QED.

## 5. The exact unsolved correlation sector

There is a complete primitive-ratio parametrization, but its infinite limit
cannot be exchanged with the large-T limit used above. Every ordered pair
has a unique representation (n,m)=(rd,sd) with gcd(r,s)=1. For EACH FIXED
coprime pair r,s, the same local Euler calculation gives

    sum_(d<=x) a(rd)a(sd)/d=C_a beta(r)beta(s)log x+O_(r,s)(1),

and hence

    sum_d a(rd)a(sd)K_T(rd,sd)/log T
       -> C_c C_a beta(r)beta(s)(rs)^(-1/2)
                                      exp[-log(r/s)^2/8].  (14)

At any prime only one of r,s has a positive valuation; this coprimality is
WHY the local constant is beta(r)beta(s). It is not a condition imposed on
d. All common factors of d with r or s remain. The two-variable formula
also shows exactly why the domination argument for integer rays fails:

    sum_(gcd(r,s)=1) |beta(r)beta(s)|(rs)^(-1/2)
                                      exp[-log(r/s)^2/8]=infinity. (15)

Indeed take distinct primes r,s in [R,2R]. Their beta magnitudes are bounded
below by a positive constant; their Gaussian factor is bounded below by
exp[-(log 2)^2/8]; and (rs)^(-1/2)>=1/(2R). The prime number theorem gives
gg R^2/(log R)^2 such ordered pairs, so this block alone contributes
gg R/(log R)^2. This establishes divergence, not an arithmetic lower bound
for the SIGNED complete energy. Large primitive ratios with comparable
numerator and denominator retain a large Gaussian weight. The finite-T Phi
factor in (1) is what controls their common size and must remain present.

Consequently (14) is valid on every FIXED finite set of primitive ratios;
(12) is valid on the special infinite union r=1 or s=1; neither authorizes
an infinite double exchange on the complete set. This is the precise bulk
correlation issue left by the signed calculation.

Put Nondiv(T)=sum_(n does not divide m, m does not divide n)
a(n)a(m)K_T(n,m). Then exactly

    E(T)=Div(T)+Nondiv(T).

Since E(T)>=0, Theorem 4 implies

    liminf_(T->infinity) Nondiv(T)/log T >=-C_c C_a L_div>0.

This is a lower requirement on a signed complementary sector, not the
upper estimate needed for RH. Theorem 1 of PROOF.md makes the missing
statement concrete: an upper bound E(T)<<_epsilon T^epsilon for every
epsilon would prove ordinary RH. Equivalently, because Div(T)=O(log T),
one needs the corresponding ONE-SIDED upper bound for Nondiv(T).

The fixed-offset estimate (7) does not control offsets comparable with the
summation scale. The divisibility result (12) is also insufficient: its
large negative term demands compensating correlations elsewhere. We have
proved a bounded exact interface and actual signed subseries asymptotics,
including an infinite sector's certified sign. We have not estimated that
complete complement, assumed independence of Mobius signs, or proved RH.
