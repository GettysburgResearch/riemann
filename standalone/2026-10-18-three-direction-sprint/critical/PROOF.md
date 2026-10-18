# Growing primitive-ratio sectors and unavoidable signed compensation

Status: **PROPOSED component theorems, awaiting independent mathematical
review. No critical energy upper bound, new zero-free boundary or RH proof.**

Scope: ordinary zeta, with the complete fixed-shift coefficient

    a(1)=1, a(n)=n^(-1) product_(p|n)(1-p).

Source: #994 at `c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`critical/ARITHMETIC.md`, blob `56f0195a8b7471fc7409c0f8f55432d9c9ec44fc`.
The source's Gaussian kernel and a(n)^2 Euler product are rederived below.
The new deductions are a uniform primitive-ray mean, complete growing-sector
bounds, and a positive balanced-prime-ray obstruction valid for a broad class
of actual smoothing kernels. A prime number theorem is an explicitly named
classical input only in the last obstruction's prime-counting step.

## 1. Full source and complete physical kernel

Let psi be a nonzero real continuous function satisfying

    |psi(u)| <= C exp(-b u^2), u in R, C,b>0.                 (G)

Compactly supported continuous functions are also allowed. For X>0 put

    f_psi(X)=sum_(n>=1) a(n)n^(-1/2)psi(log(n/X)),
    E_psi(T)=integral_0^T |f_psi(X)|^2 dX/X.

All source and Gram sums converge absolutely for each finite T. This follows
from |a|<=1 and the Gaussian (or compact-support) envelope; the source is flat
as X tends to zero and has at most O(sqrt(X)) growth as X grows. The finite
horizon T is never replaced by infinity.

For u in R define

    g_u(y)=psi(y+u/2)psi(y-u/2),
    K(u)=integral_R g_u(y)dy.

Every ordered pair has a unique representation (n,m)=(rd,sd), (r,s)=1.
Its complete ray contribution is

    R_(r,s)(T)=1/sqrt(rs) sum_(d>=1) a(rd)a(sd)/d
       * integral_(log(d sqrt(rs)/T))^infinity g_log(r/s)(y)dy. (1)

Thus E_psi(T)=sum_((r,s)=1)R_(r,s)(T), absolutely at each finite T.
Equation (1) follows by setting y=log(d sqrt(rs)/X) in the exact Gram
integral. In particular the upper physical horizon remains in the lower
limit of the y integral. No term at d sharing a prime with r or s is removed.

For #994's original W_c(y)=y^(-c)exp(-log(y)^2/4)/(2sqrt(pi)), use

    psi(u)=exp(-(c-1/2)u-u^2/4)/(2sqrt(pi)).

Then f_psi(X)=X^(-1/2) sum_n a(n)W_c(n/X), and

    K(u)=C_c exp(-u^2/8),
    C_c=exp(2(c-1/2)^2)/(2sqrt(2pi)).                     (2)

The integral in (1) is C_c exp(-u^2/8) times the full normal CDF
Phi(log(T/(d sqrt(rs)))-2(c-1/2)), exactly as in the pinned source.

## 2. A uniform mean for every primitive ray

Define the multiplicative function

    beta(1)=1, beta(p^j)=-(p^2-1)/(p^j(p+2)), j>=1,
    C_a=product_p(1-3/(p^2+p+1))>0.                       (3)

**Theorem A (uniform ray mean).** Fix 1/2<theta<1 and epsilon>0.
For every coprime pair of positive integers r,s and every real x>=1,

    sum_(d<=x) a(rd)a(sd)
       =C_a beta(r)beta(s)x+O_(theta,epsilon)((rs)^epsilon x^theta), (4)
    sum_(d<=x) a(rd)a(sd)/d
       =C_a beta(r)beta(s)log x+O_(theta,epsilon)((rs)^epsilon).    (5)

For r,s distinct primes the constants in both errors are independent of
the primes and epsilon is unnecessary. The same uniformity holds when the
number of distinct prime divisors of rs is bounded in advance.

Proof. Put q(n)=a(n)^2. Direct Euler multiplication gives

    sum_n q(n)n^(-z)=zeta(z)G(z),
    G_p(z)=(1-p^(-z))(1+(1-2/p)p^(-z))/(1-p^(-z-2)).      (6)

The nonconstant local absolute coefficient mass at weight theta is
O(p^(-1-theta)+p^(-2theta)). Therefore G has a Dirichlet series with finite
weighted absolute norm at every theta>1/2. This includes its full infinite
prime tail and proves G(1)=C_a.

If p^j divides exactly one of r,s, divide its local ray coefficient by
a(p^j). At exponent ell>=1 the result is

    a(p^(ell+j))a(p^ell)/a(p^j)=-(p-1)p^(-2ell).

It is independent of j and replaces the ordinary coefficient
(p-1)^2 p^(-2ell). Thus the exact local correcting Dirichlet series is

    H_p(z)=(1-p^(-z-1))/(1+(1-2/p)p^(-z)),
    H_p(p^ell)=-(1-1/p)(-(1-2/p))^(ell-1), ell>=1.        (7)

Here the second line denotes its coefficient at p^ell, not its value.
For Re z>1, then as absolutely convergent coefficient identities at weight
theta after removing zeta, one has

    sum_d a(rd)a(sd)d^(-z)
      =a(r)a(s) zeta(z)G(z) product_(p|rs)H_p(z).         (8)

The weighted absolute norm of H_p is exactly

    1+(1-1/p)p^(-theta)/(1-(1-2/p)p^(-theta))
      =1+O_theta(p^(-theta)).                           (9)

The finite product in (9) is O_(theta,epsilon)((rs)^epsilon): choose a fixed
prime cutoff beyond which log of each factor is at most epsilon log p;
the finitely many smaller factors are one fixed constant. It is uniformly
bounded if rs has a bounded number of distinct prime divisors. Since
|a(r)a(s)|<=1, the entire non-zeta coefficient sequence h in (8) has

    sum_e |h(e)|e^(-theta) <<_(theta,epsilon) (rs)^epsilon.

Convolving with 1 and using floor(x/e)=x/e+O(1), both the rounding error and
the omitted e>x main tail are bounded by this norm times x^theta.
Finally H_p(1)=(p+1)/(p+2), so a(r)a(s)G(1)product H_p(1) is precisely
C_a beta(r)beta(s). This proves (4). Partial summation, with
integral_1^infinity t^(theta-2)dt=(1-theta)^(-1), proves (5) with its stated
uniformity. This proof retains arbitrary shared primes between d and rs.

## 3. Complete growing small-reduced-index sectors

Let S>=1 be an integer, and retain ALL primitive ratios with min(r,s)<=S:

    Small_S(T)=sum_((r,s)=1,min(r,s)<=S) R_(r,s)(T).       (10)

This includes infinitely many large r or s and every common factor d.
For any bounded measurable pair multiplier of magnitude at most one, the
absolute value of the corresponding sector is bounded as follows.

**Theorem B (full absolute sector bound).** Under (G), uniformly for T>=2,

    sum_((r,s)=1,min(r,s)<=S) |R_(r,s)(T)|
                         <<_psi S(1+log T).             (11)

The stronger bound obtained by putting absolute values INSIDE each ray's
d sum and y integral also holds. Thus arbitrary signed sector selectors
are covered; no positivity of an incomplete Gram sector is assumed.

Proof. Tonelli and |a|<=1 bound the d sum after interchanging integrals by

    sum_(d<=T exp(y)/sqrt(rs))1/d
       <=1+log_+(T exp(y)/sqrt(rs))<=1+log T+|y|.

The Gaussian envelope gives, with constants depending only on psi,

    integral_R (1+|y|)|g_u(y)|dy <=C_psi exp(-b_psi u^2). (12)

For each s, the sum over r>=1 of
(rs)^(-1/2)exp(-b_psi log(r/s)^2) is O_psi(1), uniformly in s>=1.
To verify this, the corresponding function of r>0 is unimodal. Its sum is
at most its integral plus twice its maximum. Substitute r=s exp(u) in the
integral; it becomes integral_R exp(u/2-b_psi u^2)du, independent of s.
The maximum contributes O_psi(1/s). Sum s<=S and double to cover the
union in (10). This proves (11), including all infinite r,s,d tails.
Compact-support kernels have the same proof with a compact u envelope.

For the exact Gaussian one can use exp(-u^2/8) in (12), and the r integral
is sqrt(8pi)e^(1/2); the maximum before the s factor is e^(1/2)s^(-1/2).
Constants are not inferred from a truncated numerical sum.

**Theorem C (uniform growing-sector asymptotic).** Define the absolutely
convergent coefficient for each fixed S by

    L_S=sum_((r,s)=1,min(r,s)<=S)
              beta(r)beta(s)K(log(r/s))/sqrt(rs).         (13)

For every epsilon>0, uniformly for T>=2 and S>=1,

    Small_S(T)=C_a L_S log T+O_(psi,epsilon)(S^(1+epsilon)). (14)

In particular if S(T)<=(log T)^eta with fixed eta<1, choose epsilon with
eta(1+epsilon)<1. Then (14)'s additive error is o(log T), even though the
complete retained primitive-ratio set grows without bound. No limit or sign
for L_S as S tends to infinity is asserted.

Proof. Interchange the complete y integral and d sum in (1). Equation (5),
extended by zero for x<1 and using log_+ x, gives the ray main term

    C_a beta(r)beta(s)/sqrt(rs)
       * integral_R g_u(y)(log(T/sqrt(rs))+y)_+ dy.

Replace the positive part by log T-(log rs)/2+y. The resulting error is
bounded by integral |g_u(y)|[(log rs)/2+|y|]dy, since T>=2. The error in
(5) costs O((rs)^epsilon integral|g_u|/sqrt(rs)). Bound the y mean, log rs
term, and errors using (12), with an arbitrarily small increase in epsilon.
The unimodal integral estimate from Theorem B, now with the factor (rs)^epsilon,
is O(s^(2epsilon)); summing s<=S gives O(S^(1+2epsilon)). Rename epsilon.
This proves (14), uniformly without discarding the physical upper horizon.

For S=1, (13) specializes to #994's complete divisibility-sector coefficient,
including the diagonal once. For the Gaussian it is C_c times that source's
L_div. This agreement is a normalization check, not an imported new proof.

## 4. A polynomially large POSITIVE prime-ray sector of the actual source

**Theorem D (kernel-stable coherent obstruction).** For every psi satisfying
the hypotheses above there is eta_psi>0 such that the following holds.
Fix 0<delta<1 and put S=T^delta. Retain exactly the ordered primitive ratios

    r=p, s=q, p!=q primes in [S,(1+eta_psi)S].

Their full signed contribution, including EVERY common factor d, satisfies

    Prime_S(T) >>_(psi,delta) T^delta/log T               (15)

for all sufficiently large T. The constants and threshold can depend on
psi and delta. This is a LOWER bound for a specified signed Gram sector,
not a lower bound for the complete energy E_psi(T).

Proof. K is continuous by translation continuity in L2, and
K(0)=||psi||_2^2>0. Choose eta_psi so K(u)>=K(0)/2 whenever
|u|<=log(1+eta_psi). The boundedness and Gaussian envelope imply
integral (1+|y|)|g_u(y)|dy is uniformly bounded in that compact u range.

For distinct primes p,q, Theorem A has an absolute error constant independent
of p,q. In (1), put L=T/sqrt(pq). When L>=2, its proof therefore gives

    R_(p,q)(T)=C_a beta(p)beta(q) K(log(p/q))/sqrt(pq)
                     *log(T/sqrt(pq))+O_psi(1/sqrt(pq)), (16)

uniformly for these p,q. Indeed integrate (5) against g_u; replacing log_+
by log costs at most a bounded first absolute moment when log L>=0.
Every beta(p) is negative and |beta(p)|>=3/8. Thus the leading constant
in (16) is uniformly positive. Also sqrt(pq) is comparable to S and
log(T/sqrt(pq))=(1-delta)log T+O_psi(1).

The classical prime number theorem in a fixed relative interval gives
#(primes in [S,(1+eta_psi)S]) ~ eta_psi S/log S. Sum (16) over the distinct
ordered prime pairs. The main term is >>S log T/(log S)^2, and its total
error is O(S/(log S)^2). Substituting S=T^delta proves (15).

Consequences, with their exact limits:

* Uniform subpower estimates for every selected primitive-ratio sector are
  FALSE even for these literal arithmetic coefficients. Choosing epsilon<delta
  contradicts (15). A prime-ray selector is a specific legal selector; no
  synthetic replacement of a(n) was used.
* If the complete critical estimate E_psi(T)<<_epsilon T^epsilon holds, the
  complementary signed sector must be negative at size at least a constant
  times T^delta/log T, for every fixed delta<1. This follows from the exact
  equality E=Prime+Complement, choosing epsilon<delta. The complement has
  not been bounded here.
* #994's negative divisibility sector is only O(log T). By itself it cannot
  supply this compensating polynomial contribution. Further genuine signed
  cancellation among large primitive ratios is necessary.

Changing to another nonzero Gaussian or compactly supported smoothing kernel
does not avoid this obstruction: its autocorrelation remains positive near
zero. This conclusion concerns sectorwise upper-bound architectures, not an
impossibility theorem for RH or for correlated estimates of the complete sum.

## 5. Complete Gaussian coefficients change sign already at small cutoffs

Write L_S=C_c ell_S for the Gaussian. The complete infinite coefficients,
not just their finite numerical truncations, satisfy

    -9/5 < ell_1 < -17/10,
    -4/5 < ell_2 < -7/10,
     3/10 < ell_3 < 1/2.                                 (17)

These are finite directed computations with an analytic whole-tail proof.
They certify no limiting sign as S grows. Since the only coprime diagonal
is (1,1), a disjoint row formula is

    ell_S=1+2 sum_(s<=S) beta(s)/sqrt(s)
                    sum_(r>s,(r,s)=1) beta(r)/sqrt(r)
                                      exp(-log(r/s)^2/8).

At a ratio cutoff N>=S, |beta(r)|<=1 bounds the entire omitted tail by

    2 e^(1/2) sqrt(2pi) sum_(s<=S) |beta(s)|
          erfc((log(N/s)-2)/sqrt(8)).                     (18)

Indeed r^(-1/2)exp(-log(r/s)^2/8) is decreasing for r>=s. Its sum over
r>N is at most its integral from N to infinity. Substituting r=s exp(u)
and completing the square gives

    integral_N^infinity r^(-1/2) exp(-log(r/s)^2/8)dr
       =sqrt(s)e^(1/2)sqrt(2pi)
                   erfc((log(N/s)-2)/sqrt(8)).

The factor 2|beta(s)|/sqrt(s) proves (18). It pays every omitted r,
including all noncoprime r before they could be excluded.

The supplied python-flint 0.9.0 checker uses 192-bit balls, exact rational
beta values reconstructed from prime factors, N=16384, and both signs of
the entire (18) tail. Its enclosures have centers approximately
-1.7572726290, -0.7643578568 and +0.3841092420, with radii below
0.000969, 0.002382 and 0.006603 respectively. The strict rational gates
(17), rather than rounded decimal centers, are the accepted assertions.

The same checker evaluates nine full actual prime-ray fixtures at the fixed
Gaussian shift c=1/2, including every d>N via |a|<=1. At this shift, for
L=T/sqrt(pq), N>L and A=log(N/L)>0,

    sum_(d>N) Phi(log(L/d))/d
       <=integral_N^infinity Phi(log(L/t))dt/t
       <=exp(-A^2/2)/(sqrt(2pi) A^2).                    (19)

The first integrand is positive decreasing. For the second inequality,
Phi(-u)<=phi(u)/u and integral_A^infinity phi(u)du<=phi(A)/A.
The Gaussian prefactor in (2) and 1/sqrt(pq) multiply (19). These fixtures
are finite scope corroboration; Theorem D is proved analytically above.

## 6. A different completion: finite prime universes have growing POSITIVE means

The sign changes in (17) do not justify replacing the ordered physical
source by a formal Euler product. One can evaluate a different, precisely
defined completion and show why its limits must be kept separate.

For P>=2 let U_P be all positive integers supported on primes <=P. Define

    ell^(P)=sum_(r,s in U_P,(r,s)=1)
           beta(r)beta(s)/sqrt(rs) exp(-log(r/s)^2/8).     (20)

For each fixed P this infinite sum is absolutely convergent, even after
removing its Gaussian: at each of finitely many primes the exponents have
geometric decay p^(-3j/2). This is a finite-PRIME completion, distinct
from min(r,s)<=S and from any physical horizon truncation.

**Theorem F.** For every P>=2, ell^(P)>0, and

                log ell^(P) ~ 4 sqrt(P)/log P            (21)

as P tends to infinity. The asymptotic imports the classical prime number
theorem only. For fixed P and the original Gaussian kernel (2), the actual
complete signed Gram sector with r,s in U_P obeys

    E^(P)_psi(T)=C_a C_c ell^(P) log T+O_(P,c)(1).        (22)

No uniformity in P is claimed in (22), and P may not be allowed to grow
with T using its displayed error. The sector E^(P) includes every common
factor d, without restricting d's prime support.

Proof of positivity. The Gaussian Fourier identity gives

    ell^(P)=sqrt(2/pi) integral_R exp(-2t^2)
                       product_(p<=P) lambda_p(t)dt,
    lambda_p(t)=1-2c_p Re[z_p/(1-z_p)],
    c_p=(p^2-1)/(p+2), z_p=p^(-3/2)exp(i t log p).        (23)

Absolute convergence in (20) justifies all exchanges. Coprimality permits
at each p a positive exponent on r OR on s, or neither, giving exactly
the local factor in (23). If h=p^(-3/2), its minimum over real t is

    1-2c_p h/(1-h)>0.                                  (24)

For p>=3, use c_p<=p-1 and
p^(3/2)-1>2(p-1), since
(sqrt(p)-1)(p-sqrt(p)-1)>0. For p=2 the required inequality is
2sqrt(2)>5/2. Thus every lambda_p is positive everywhere, proving
strict positivity of the integral.

Proof of the growth rate. At every real t,

    lambda_p(t)<=1+2c_p h/(1+h)<=1+2/sqrt(p).

Consequently log ell^(P)<=2 sum_(p<=P)p^(-1/2). Partial summation of
the prime number theorem gives sum_(p<=P)p^(-1/2)~2sqrt(P)/log P.
This is the upper bound in (21).

For the lower bound put V=P/(log P)^4 and integrate only over

    |t-pi/log P|<=1/(log P)^2.                           (25)

For V<p<=P the phase t log p=pi+O(log log P/log P) uniformly.
Since p>=V tends to infinity,

    log lambda_p(t)=(2+o(1))/sqrt(p)

uniformly on this interval. The omitted primes p<=V have total logarithm
bounded below by -O(sqrt(V))-O(1), uniformly in t. To see this directly,
(24) is positive for each small prime, and for all sufficiently large p
its logarithm is >=-C/sqrt(p); bound the remaining prime sum by the full
integer sum <=2sqrt(V). This loss is o(sqrt(P)/log P). The large primes
therefore supply (4-o(1))sqrt(P)/log P. The Gaussian mass of (25) is
comparable to (log P)^(-2), whose logarithm is also negligible on that
scale. Positivity everywhere allows restriction to (25), proving (21).

For (22), retain the factor |a(r)a(s)| in the convolution proof of (4)
instead of replacing it by 1. In the fixed universe U_P, the finite local
correction norm is bounded by a constant depending only on P. Thus (5)'s
error is O_P(|a(r)a(s)|). The sum

    sum_(r in U_P) |a(r)|(1+log r)/sqrt(r)

is finite by its finite product of convergent geometric series and their
derivatives. Integrating the full ray formula and summing its errors,
including the log(rs) horizon shift, is therefore justified and O_P(1).
The resulting main coefficient is exactly (20), proving (22).

This gives a concrete noncommutation warning: fixed-prime full common-factor
means are positive and become very large with the prime universe, whereas
other complete retained sectors can be negative. Neither completion can
be substituted for the original horizon-dependent sum without a uniform
error theorem. Any use of (22) with P=P(T) must first pay its full P cost.

## 7. Verification boundary

Exact checks reconstruct the arithmetic coefficients and the shared-prime
Euler identities. Directed Gaussian fixtures, when run, include the entire
omitted common-factor tail; their scope is their displayed finite parameters.
The proof of the uniform estimates is Sections 1--4, not a fit to those fixtures.
No checker can certify the unproved complete signed cancellation merely by
agreeing with a deposited report. The complete energy upper estimate remains
open after all of these sector results.
