# CTC26: a connected infinite Ising law with theta-calibrated growth

Date: 2026-09-12. Status: **PROPOSED COMPONENT PROOFS; independent mathematical
and implementation review required.** This law is not the theta law. Its sixth
moment is proved different below. No RH proof, new zeta zero-free region, or
all-order inverse-Ising theorem is claimed.

The predecessor is PR #863 at
`0640c9c59be0bf20c18258460a7517fb09728e82`. It constructs a *finite* 272-spin
law matching theta moments through fourteen. The present contribution does
not improve that finite matched order. It constructs one genuinely *infinite,
connected* law, controls its complete complex limit and real-field growth,
and matches its second and fourth moments exactly. These are different scopes.

## 1. Target, chain, and exact parameters

Use the unchanged normalized theta density

    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                                  exp(-pi n^2 exp(2t)), t>=0,
    w_theta(t)=phi(t)/integral_R phi, with its even extension.

The classical normalized theta representation is

    chi_theta(z)=Xi(z)/Xi(0), Xi(z)=xi(1/2+iz),
    M_theta(h)=xi(1/2+h)/xi(1/2).

The apparent product singularities in xi at 0 and 1 are removed analytically.
Write mu_j=integral t^j w_theta(t)dt and v=mu_2. Every exponential moment
exists. The accepting computation reconstructs mu_2,mu_4,mu_6 from this full
source, including all omitted indices and time tails. It uses no zero list.

Let sigma_1 be a uniform sign, and let the subsequent signs form the stationary
Markov chain

    P(sigma_(n+1)=sigma_n)=3/5,    q=E sigma_n sigma_(n+1)=1/5.

Every finite marginal is the free-boundary zero-field ferromagnet with EACH
nearest-neighbour coupling

    J=atanh(1/5)=(1/2)log(3/2)>0.

In particular E sigma_i sigma_j=q^|i-j|. No independent-block replacement of
this process is made.

Here are the constants that define the observable. All logarithms are natural.
Set c=1/2, r=2/3 and

    lambda(u)=[(1+q)cosh u+sqrt((1-q)^2+(1+q)^2 sinh^2 u)]/2,
    f(u)=log lambda(u),
    m(u)=f'(u)=sinh u/sqrt(sinh^2 u+r^2),
    ell=log(3/5),             d=7/(8 ell),
    C=-1+integral_0^1 m(u)/u du+integral_1^infinity (m(u)-1)/u du,
    S=sum_(n>=32) log(n)/n^2, H31=sum_(n=1)^31 1/n,
    B0=(-log2+C+gamma)/2,    Btheta=-(1+log(2pi))/2,
    A=Btheta-B0+H31/2-d S.                                  (1)

Here gamma is Euler's constant. Both integrals and the sum in (1) converge.
They are explicit real constants, not values inferred from zeta zeros.
The certificate establishes

    .80716<A<.80717,       -1.71292<d<-1.71291.              (2)

For n>=32 define

    a_n=1/(2n)+d log(n)/n^2.                                (3)

These weights are positive and decreasing, and

    1/(4n)<a_n<1/(2n),  n>=32.                             (4)

For example use |d|<1.713 and log32<3.466. The functions log x/x and
(2log x-1)/x decrease in this range. They respectively prove (4) and
0<-a'(x)<=1/(2x^2) for the continuous extension of (3).

There are two head parameters t and lambda_0; the latter is unrelated to the
Perron eigenvalue lambda(u). For 0<=lambda_0<=1 put

    b_1=b_2=b_3=1/(3+lambda_0), b_4=lambda_0/(3+lambda_0),
    b_i=0 for 5<=i<=31,
    a_i=A[(1-t)/31+t b_i], 1<=i<=31.                       (5)

Thus sum_(i<=31)a_i=A, and all head weights are positive if 0<t<1. The exact
selection of t,lambda_0 by variance and fourth-moment equations is in Section 6.
Let X_N=sum_(n<=N)a_n sigma_n and X=lim X_N in L2, as constructed next.

## 2. CTC1: the full connected limit, real zeros, and an explicit cutoff error

For any finitely supported real coefficients u_i,

    Var(sum u_i sigma_i)<=kappa sum u_i^2,  kappa=(1+q)/(1-q)=3/2. (6)

Indeed the row sums of the matrix q^|i-j| are at most kappa, and
2|u_i u_j|<=u_i^2+u_j^2 proves (6). This also applies to differences of partial
sums. Equations (3),(6) construct X in L2 and give its finite variance V.

The one external zero-location input is the classical weighted Lee--Yang
theorem for finite zero-field Ising graphs with nonnegative couplings and
observable weights. The version after equation (21), page 11 of Newman--Wu
[LY], applies exactly here. It concerns Fourier zeros, not a spectrum inferred
from a positive matrix.

For completeness, its needed moment bound follows from elementary entire
factorization. The MGF of each finite symmetric model is even, of exponential
type, is 1 at zero, and has only imaginary zeros. Pairing these zeros in its
canonical product gives

    M_N(h)=product_k(1+h^2/gamma_k^2),
    sum_k gamma_k^-2=Var(X_N)/2.

Evenness and order at most one exclude an extra quadratic exponential factor;
the linear exponential vanishes by evenness. A finite spin system need not
have a finite number of Fourier zeros. Comparing elementary symmetric sums
in the paired product yields, for every integer j>=0,

    E X_N^(2j)/(2j)! <= (Var(X_N)/2)^j/j!,
    E exp(hX_N)<=exp(Var(X_N)h^2/2),  h real.                (7)

The same bounds hold for any finite segment and then for its L2 limit, by
uniform exponential integrability. For example the bound at twice any fixed
real h gives uniform integrability of exp(hX_N); the same device pays every
polynomial moment. Consequently X has all exponential moments, its transforms
are entire, and its finite transforms converge locally uniformly. Alternatively
the following explicit estimate proves that convergence. Hurwitz and chi(0)=1
then show that chi(z)=E exp(izX) has only real zeros.

### Complete complex truncation bound

Let N>=32, A_N=X_N and B_N=X-X_N. The notation A_N here is a random variable,
not the constant A in (1). Markov conditioning and L2 convergence give

    E(B_N | sigma_1,...,sigma_N)=b_N sigma_N,
    b_N=sum_(k>=1)q^k a_(N+k) <=1/[8(N+1)],
    V_B=Var(B_N)<=3/(8N).                                  (8)

All coefficients and covariances are nonnegative, so V_A+V_B<=V. For |z|<=R,
expand exp(izB_N) through first order. The linear term is bounded by
2 R b_N exp(V_A R^2/2). For the remainder use

    |exp(izb)-1-izb| <= R^2 b^2 exp(R|b|)/2,
    E B_N^4<=3 V_B^2,
    E exp(h|Y|)<=2 exp(Var(Y)h^2/2).

Cauchy--Schwarz twice, with no independence assumption between A_N and B_N,
gives a remainder at most
(sqrt6/2)R^2 V_B exp(2R^2(V_A+V_B)). Therefore

    sup_(|z|<=R)|chi(z)-chi_N(z)|
     <= [R/(4(N+1))] exp(VR^2/2)
        +[3sqrt6 R^2/(16N)] exp(2VR^2).                    (9)

This controls the ENTIRE complex disk and the full omitted chain. It is not
an empirical rate or a bound for a separately refitted theta model.
Cauchy's formula also gives the corresponding error for every fixed derivative.

### This limit has a density, not just an abstract probability law

One can also bound its complete real-frequency tail. Condition on all even
spins of a finite chain. The odd spins are conditionally independent and their
conditional biases have modulus at most tanh(2J)=5/13. Consequently an odd-spin
factor at phase u has modulus at most

    sqrt(1-(144/169)sin^2u) <= exp(-(72/169)sin^2u).

For T=|z|>=64, select the odd indices in [T,2T]. By (4), their phases satisfy
1/8<=T a_n<=1/2. Using sin u>=u/2 here, each factor costs at most exp(-1/640).
There are at least T/4 such indices. The other factors have modulus at most
one. First take a finite chain containing them, then pass to its full limit:

    |chi(z)|<=exp(-|z|/2560),  z real, |z|>=64.            (10)

Fourier inversion thus gives a symmetric nonnegative density, analytic in
|Im x|<1/2560. This is a conservative strip, not claimed optimal or equal
to the theta density's analytic strip. The proof uses the actual connected
conditional law, not a product of unconditional spin factors.

## 3. CTC2: an exact bounded-error Perron reduction

The central infinite-size estimate is

    log M(h)=sum_(n>=1) f(h a_n)+O(1), h>=0,              (11)

with a constant independent of h and the finite truncation N. We give the
matrix comparison because simply multiplying the largest eigenvalues of
noncommuting transfer matrices would not prove (11).

Let P be the symmetric transition matrix of the chain, v0=(1,1)/sqrt2,
and T(u)=P^(1/2) diag(exp u,exp(-u)) P^(1/2). Direct multiplication gives

    M_N(h)=v0^T T(h a_1)...T(h a_N)v0.                     (12)

The Perron eigenvalue of T(u) is the lambda(u) in (1). Its positive right
vector, normalized in its first coordinate, is r(u)=(1,tau(u)). Here

    tau_*=(1-sqrt q)/(1+sqrt q)<=tau(u)<=1,

and tau(u) decreases with u>=0. To verify monotonicity, the difference of
the diagonal entries is 2sqrt(q)sinh u, while the off-diagonal entry is
(1-q)cosh u/2. Their ratio increases with u; the positive eigenvector ratio
therefore decreases. The limiting vector at infinity is proportional to the
first column of P^(1/2), giving tau_*.

Write tau_i=tau(h a_i), tau_(N+1)=1 and r_i=(1,tau_i). Entrywise positivity
of T gives

    min(1,tau_(i+1)/tau_i) lambda_i r_i
      <= T_i r_(i+1)
      <= max(1,tau_(i+1)/tau_i) lambda_i r_i.

Induct through the full product, then multiply by v0^T. This bounds the ratio
M_N/product lambda_i between positive scalar products whose logarithms have
absolute value at most

    log2+sum_(i=1)^N |log(tau_(i+1)/tau_i)|.

The 31 initial transitions cost at most 31 log(1/tau_*). On the decreasing
weight tail, tau_i increases, so the REST telescopes and costs at most
log(1/tau_*). Thus, uniformly for N>=32 and h>=0,

    |log M_N(h)-sum_(n<=N)f(h a_n)|
       <= log2+32 log(1/tau_*).                            (13)

For fixed h the sum converges because f(u)=O(u^2) at zero. Passing to the
limit proves (11), retaining the original boundary vectors and every edge.
There is no scalar-product approximation error that grows with N or h.

## 4. CTC3: the complete three-term growth calibration

We now prove

    log M(h)= (h/2)log h -[(1+log(2pi))/2]h
                       +(7/4)log h+O(1), h->+infinity.    (14)

No theta zero assumption is involved. Its three coefficients are deliberately
encoded in the weights; it is not a consequence of just the variance match.

### 4.1 The unperturbed harmonic sum

For x>0 define

    g(t)=f(1/t)-t^-1 1_(0<t<=1).

It is integrable and of bounded variation. At zero it tends to ell with
exponentially small differentiated errors; at infinity it is O(t^-2), with
an integrable derivative. Its single jump at 1 is retained. An intervalwise
Riemann-sum error is bounded by its total variation. Hence

    sum_(n>=1)f(x/n)
       =x H_floor(x)+sum_(n>=1)g(n/x)
       =x log x+(gamma+C)x+O(1),                          (15)

since integral g=C. The latter identity follows by substituting u=1/t and
integrating by parts separately on (0,1) and (1,infinity). The boundary term
at u=1 contributes the -1 in (1). Harmonic-sum asymptotics need only the
integral/trapezoid estimate, not the prime number theorem.

### 4.2 The logarithmic correction has a finite linear mass but changes log h

Compare f(h a_n) with f(ch/n) for n>=32. Taylor's formula gives the first
variation h d log(n)n^-2 m(ch/n). Its complete second-order remainder sums
to O(log^2h/h): f''(u)<=C_1 exp(-2u) for u>=0, and all intermediate fields
are at least ch/(2n), by (4). Thus the absolute remainder is bounded by a
constant times

    h^2 sum_(n>=32) log^2(n)n^-4 exp(-ch/n)
       = O(log^2h/h).

The last estimate follows by integral comparison or dyadic blocks below and
above h; the exponential pays the lower blocks and n^-4 pays the upper ones.
No Taylor series is summed outside its domain of convergence.

Put x=ch and g1(t)=[m(1/t)-1]/t^2. Both g1 and log(t)g1 are integrable and
of bounded variation (use exponential decay at zero and t^-2 log t at infinity).
Their Riemann sums therefore give

    h d sum_(n>=32) log(n)n^-2[m(ch/n)-1]
       =(d/c) ell log h+O(1),                             (16)

because integral g1=integral_0^infinity[m(u)-1]du=ell.
The finitely many omitted small indices give exponentially small errors.
Adding the separated linear term yields

    sum_(n>=32)[f(h a_n)-f(ch/n)]
        =h d S+(d/c)ell log h+O(1).                       (17)

Each positive head weight contributes f(h a_i)=h a_i+ell+O(exp(-2h a_i)).
Replacing the first31 unperturbed harmonic weights therefore changes the sum
by h(A-cH31)+O(1). Combine this with (15) at x=ch, (17), and (13):

    log M(h)=ch log h+
       [c log c+c(gamma+C)+A-cH31+dS]h
       +(d/c)ell log h+O(1).

Equations (1) make these coefficients exactly those in (14). This proves (14).
All error constants are finite for the chosen positive head; no numerical
value for the asymptotic O(1) constant is certified.

### 4.3 Comparison with the actual theta law

The classical normalized xi representation, Stirling's expansion [ST], and
the absolutely convergent Euler series at large positive real s give

    log M_theta(h)=(h/2)log h-[(1+log(2pi))/2]h
                               +(7/4)log h+O(1).         (18)

Indeed log xi(s)=(s/2+3/2)log s-s(1+log(2pi))/2+O(1), and s=h+1/2.
This uses no RH-strength prime estimate. Reflection gives the negative-h side.
Thus the ratio M(h)/M_theta(h) is bounded above and below by positive constants
on the WHOLE real h-axis. This is NOT a complex ratio estimate or equality.

Two further consequences follow directly. First, the entire characteristic
function has order one: |M(z)|<=M(|z|), and (14) supplies both the upper and
lower order. Second, choosing h=2pi exp(2x) in the Chernoff bound gives

    P(X>=x)<=C_2 exp(-pi exp(2x)+(7/2)x), x sufficiently large. (19)

This is a one-sided probability bound with an unevaluated constant C_2,
not a matching density asymptotic or a lower-tail estimate. The support is
unbounded because log M(h)/h tends to infinity. There can be no nonzero
Gaussian convolution factor, since it would force at least quadratic log-MGF
growth (the remaining centered factor has MGF at least one by Jensen).

## 5. Exact chain cumulants and complete numerical tails

This section defines what the accepting interval calculation verifies. The
algebraic identities are proved here; executing them does not prove all of
the preceding analytic arguments.

For a finite segment let F(u)=E exp(iuX), G(u)=E sigma_last exp(iuX), and
S(u)=G(u)/(iF(u)). These quotients are used ONLY as formal Taylor series at
zero, where F(0)=1. If a positive weight a is appended, exact conditioning gives

    S_new=[tan(au)+q S]/[1-q tan(au)S],
    -log F_new=-log F-log cos(au)-log[1-q tan(au)S].       (20)

All coefficients of the odd series S and the even series -log F are
nonnegative. This also follows directly by induction from (20).

Retain S=s1 u+s3 u^3+s5 u^5+... and -logF=L2u^2+L4u^4+L6u^6+....
The positive cumulants are (kappa2,-kappa4,kappa6)=(2L2,24L4,720L6).
Expanding (20) gives precisely step() in verify.py. For two segments joined
by one edge, reverse the second segment so its recorded endpoint is adjacent
to the first. Then

    F_join=F_left F_right(1-q S_left S_right).             (21)

Expansion of its logarithm is combine(). All cross terms remain. Reversal is
valid because the stationary Markov chain is reversible; no endpoint is
incorrectly identified with an independent mean.

### 5.1 Forward coefficient majorants

For any positive first31 weights summing to A<.81, (20) with q<=1 gives
S_head coefficientwise at most tan(.81u). The accepting computation starts
from that larger formal vector and runs ALL weights32 through N=16384.
It verifies, at that endpoint, the appropriate truncated bounds

    S_N <= tan((3/4)u/N) through degree1;
    S_N <= tan((3/2)u/N) through degree3;
    S_N <= tan(3u/N)     through degree5.                 (22)

They continue by induction to every subsequent n. To check this without an
infinite numerical loop, in degree at most k=1,3,5 use respectively
alpha=1/5,3/5,3/4, so q<=alpha^j for all relevant positive odd j<=k.
For R=n/(n-1)<=65/64 and the corresponding a*=3/4,3/2,3, respectively,

    q tan(a*R x) <= tan(alpha a*R x),
    1/2+alpha a*R <= a*.

The tangent addition identity, with nonnegative coefficients, proves the
next instance of (22), since a_n<=1/(2n). The logarithmic increment in (20)
is bounded coefficientwise by -log cos(a*u/n). Summing the integral bounds
for n^-4 and n^-6 proves the COMPLETE cumulant tails

    0<=(-kappa4)_infinity-(-kappa4)_N<=27/(8N^3),
    0<=(kappa6)_infinity-(kappa6)_N<=11664/(5N^5).          (23)

No raw moment or signed cross term is discarded in these cumulant bounds.

### 5.2 A sharper full variance tail

Let I(x)=integral_x^infinity a(u)^2du, with the continuous weights (3).
Direct integration gives

    I(x)=1/(4x)+d(log x+1/2)/(2x^2)
       +d^2[(log x)^2+(2/3)log x+2/9]/(3x^3).             (24)

For the stationary omitted segment, its variance differs from
(3/2)sum_(n>N)a_n^2 by a nonpositive quantity of magnitude at most
5/(64N^2). Indeed use 0<=a_n-a_(n+k)<=k/(2n^2), a_n<=1/(2n), then sum
2 sum_(k>=1)q^k sum_(n>N)a_n(a_n-a_(n+k)).
The positive covariance between the omitted segment and the whole prefix
is at most 3/[16N(N+1)], using the first majorant in (22). Monotonicity gives
I(N+1)<=sum_(n>N)a_n^2<=I(N). Therefore, for EVERY head in this packet,

    (3/2)I(N+1)-5/(64N^2)
     <= V_infinity-V_N
     <= (3/2)I(N)+3/[16N(N+1)].                            (25)

This is the full stationary tail plus the complete prefix-to-tail interaction.
It is not an independent-tail substitution. At N=16384 the returned enclosure
is approximately (0.00002283770012097,0.00002284008084425).

## 6. CTC4: exact theta variance and fourth moment, with a sixth-moment separation

For each lambda_0 in [0,1], the full variance in (5) is a quadratic polynomial
in t, with strictly positive quadratic coefficient. That coefficient is the
variance of a nonzero finite linear combination of the first31 spins; all
finite configurations have positive probability. At t=0, (6) gives

    V0 <=(3/2)(A^2+1/4)/31 < .044 < v.

At t=1, nonnegative correlations and Cauchy--Schwarz on the four nonzero
head weights give V>=A^2/4>.16>v. Thus the equation V(t,lambda_0)=v has
exactly one positive root t(lambda_0), it lies in (0,1), and it is continuous.
The two quadratic roots have opposite signs, which also proves simplicity
of the positive root. This is an exact infinite-chain variance equation,
not a root of a variance with the tail removed.

The interval certificate, using (20)--(25) and the defining theta integrals,
proves the following two signs. The displayed differences use
[-kappa4_chain-(-kappa4_theta)]/(2v^2):

    lambda_0=13/40:  difference in (0.0000081657,0.0000082600),
    lambda_0=41/125: difference in (-0.000013871,-0.000013748). (26)

The t parameter in each statement is its exact variance root. It is enclosed
by strict interval sign evaluations on rational brackets, not substituted
with a fitted decimal. Continuity and (26) give at least one root of the
fourth-moment equation in [13/40,41/125]. Define lambda_* as the smallest
such root, and t_*=t(lambda_*). This minimum exists by compactness and strict
endpoint signs. No uniqueness of the lambda-root is asserted.

For that exact choice of parameters, ALL the preceding theorems hold and

    E X^2=mu_2,       E X^4=mu_4,       E X^(2j+1)=0.      (27)

The fourth moment follows from its cumulant and the already equal variance.

The checker additionally covers the WHOLE lambda interval with sixteen
closed rational subintervals. For each subinterval it encloses all its
variance roots by two strict variance signs, propagates that entire parameter
box through (20)--(25), and obtains

    .005 < (kappa6_chain-kappa6_theta)/v^3 < .05.          (28)

The retained enclosure is tighter, approximately (.0221714,.0229276).
Because (27) holds, (28) is exactly the standardized RAW sixth-moment error.
In particular the constructed law is not theta and its characteristic function
is not Xi/Xi(0). This is a proved distinction, not merely a numerical suspicion.
The finite restrictions X_N do not match (27) exactly; it is their complete
infinite limit that does. Their convergence is controlled by (9).

## 7. Primitive numerical contract

verify.py uses standard-library integer and Fraction arithmetic and outward
192-bit dyadic intervals. No scipy, mpmath, floating eigensolve, quadrature
oracle, zeta oracle, or input theta moment receipt is used in acceptance.

### Constants

The logarithm uses range reduction to [1,2) and 72 terms of the atanh series,
with remainder 2 z^145/[145(1-z^2)]. log2 has its separate 100-term version.
Exponentials are reduced to [0,1/8], use 96 positive Taylor terms with the
complete ratio remainder, then are squared outward. Machin's formula and
alternating arctangent remainder bound pi. All square roots use integer sqrt.

For C in (1), integrate m(u)/u on [0,1] and (m(u)-1)/u on [1,8] by composite
Simpson with 512 and4096 equal subintervals. On a complex radius-1/4 disk,

    Re[r^2+sinh^2z]>=4/9-sin^2(1/4)>55/144.

Choose the analytic square root with positive real-axis value. This gives
|m(z)|<3/2. On the second interval |z|>=3/4, so |(m-1)/z|<4. On the first,
|sinh z/z|<=cosh(5/4)<2, giving |m(z)/z|<4, including its removable origin.
Cauchy's formula bounds the fourth derivatives by24576. The two Simpson
errors are therefore at most24576 L^5/(180 n^4). Finally
0<1-m(u)<exp(-2u) for u>=8, so the signed omitted integral has magnitude at
most exp(-16)/16. Every one of these errors is retained in C's interval.

Euler's constant is enclosed by H_M-logM-1/(2M), M=8192, with symmetric
error1/[6(M-1)^2]. This follows by summing the positive trapezoid errors
of1/x, each at most1/(6n^3). For S, sum n32 through255 and use Euler--Maclaurin
at256 through B4. The complete remainder is at most|f'''(256)|/720 for
f(x)=logx/x^2: |B4(t)|<=1/30 and f'''' is positive there. The fourth-order
Bernoulli polynomial bound follows directly from its explicit polynomial.

### Complete theta source

The Taylor/dyadic routines are ADAPTED from ICR26 (#863), not an independent
transcendental backend. All values are newly reconstructed. For indices1,2,3,4
use32,24,16,12 cells of width1/16, degree80 at the rational midpoints, and
integrate moments0,2,4,6 by exact polynomial moments. A complex radius1/8
Cauchy circle gives the full polynomial remainder. On those circles the
negative exponential has modulus at most one; with n<=4, Re(u)<=17/8,
pi<4 and e<3 the prefactor is below10^11. The half-cell/radius ratio is1/4.
The code pays the resulting remainder over the full summed length, multiplied
by2^j for each moment, including the even-reflection factor. The individual tails use
exp(2u)>=exp(2U)[1+2(u-U)] and retain all moment polynomial terms. The entire
n>=5 tail is bounded by

    16 pi^2*625 exp(-25pi) j!/(50pi-9/2)^(j+1), j=0,2,4,6.

The Cauchy errors, four time tails, and index tail are individually recorded.
The normalizing integral is bounded away from zero before forming moments.
No independence of prime phases, zero data, or unproved continuation is used.

### What finite execution proves and does not prove

It authenticates the numerical signs, finite interval recurrences and stated
coverage, conditional on the written analytic remainder arguments. It is not
a formal proof of Lee--Yang, Hurwitz, the infinite limit, Perron asymptotics,
or the Riemann-sum arguments. SOURCES.json states imported theorem scopes;
VALIDATION.md distinguishes successful replay from failed preliminary commands.

## 8. The remaining full-problem question

This is a concrete global Ising family that has the right zero geometry,
non-Gaussian unbounded law, the specified theta growth on the whole real
field axis, and exact low-moment agreement. It also has a demonstrably wrong
sixth moment. Neither comparability on the real field axis nor low-moment
matching identifies two entire functions.

A new construction would have to adjust the correlated process to recover
ALL actual theta moments (or the full transform), keeping nonnegative
couplings and the appropriate tightness/complex convergence. No theorem here
says that the one-chain class is universal for Lee--Yang laws, or that theta
belongs to it. Finite-head redistribution with its sum fixed preserves the
three growth coefficients, and (20) gives explicit inverse moment equations;
it does not prove arbitrary-order reachability. The separate programme note
sets out that attack and its unresolved step without assigning it to reviewers.

### Primary references

[LY] Charles M. Newman and Wei Wu, *Constants of de Bruijn--Newman type in
analytic number theory and statistical physics*, arXiv:1901.06596v2, p.11,
equation(21) and the following weighted-magnetization statement. General
Lee--Yang and weak/entire closure mechanisms are classical, not new here.

[ST] NIST DLMF5.11.1, Stirling expansion of log Gamma; DLMF25.4.3--25.4.4,
xi normalization and reflection. Only their classical real-axis consequences
are used. The chain comparison and weight-tail calculations are proved above.

No exhaustive novelty or priority determination is claimed.
