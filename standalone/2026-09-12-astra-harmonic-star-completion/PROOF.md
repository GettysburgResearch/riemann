# HSC26 — connected harmonic stars with theta jets and theta-scale tails

Date: 2026-09-12. Status: PROPOSED COMPONENT PROOFS, independent review required.
**RH and arbitrary-order theta realization are NOT proved.** The constructed
laws below are explicitly NOT the theta law. They match its first seven even
moments and three large-field growth coefficients, not its whole transform.

The new operation is a whole-law completion of a regular finite ferromagnetic
seed. It constructs a connected countably infinite star, pays its complete
probabilistic and complex-analytic limit, and gives exact theta-scale tail
asymptotics. It does not just add another moment. The finite fourteen-moment
seed and its nonsingular Jacobian are credited to PR #863 at
`0640c9c59be0bf20c18258460a7517fb09728e82`.

## 1. Statement, actual target, and the inherited input

The unchanged theta law is w(t)=phi(t)/Xi(0), where for t>=0

    phi(t)=sum_(n>=1) [4*pi^2*n^4*exp(9t/2)-6*pi*n^2*exp(5t/2)]
                         *exp(-pi*n^2*exp(2t)),

and phi is extended evenly. Its transform is Xi(z)/Xi(0), and its moment
generating function is M_theta(h)=xi(1/2+h)/xi(1/2). Let mu_(2r) be its
moments and v=mu_2>0. No zero locations define any of the following models.

The explicitly IMPORTED seed theorem ICR1 supplies positive parameters
u*=(x_0,...,x_5,y) in a fixed compact box, multiplicities
nu=(256,10,1,1,1,1), and the zero-field law

    X_*(u)=sqrt(v)[sum_i sqrt(x_i) sum_(l=1)^nu_i epsilon_il
                                      +sqrt(y)(sigma_0+sigma_1)/2].

Only sigma_0,sigma_1 interact: tanh J_01=1/5, so J_01=log(3/2)/2.
At u*, moments 2,...,14 equal the exact theta moments. The seven standardized
cumulant equations F(u)=0 have invertible Jacobian. The source-pinned interval
proof gives a box of radius rho=10^-14, a rational inverse R at its rational
center c0, and

    ||R||_infinity<75000000,
    ||R F(c0)||_infinity<6e-22,
    sup_box ||I-R DF||_infinity<1.01e-7.                   (1)

The standardized sixteenth-moment error is in
(0.2020747403,0.2020747702). These are dependencies, not new moment computations.
Our validation reruns the unchanged full source producer at its pinned bytes.

**Theorem HSC1.** For every sufficiently large integer N there is a symmetric
probability law X_N with all of the following properties.

(a) It is the L2 limit of finite connected zero-field Ising STARS, with positive
observable weights and strictly positive couplings. A single root is connected
to every other vertex. Its graph is genuinely infinite, not a growing number
of independent bounded components. No bounded-degree claim is made.

(b) Its characteristic function is even entire of order one, with only real
zeros, and its law has a real-analytic density on the real line.

(c) Exactly E X_N^(2r)=mu_(2r) for 1<=r<=7. Every odd moment is zero.
There are finite connected star approximants which have these same exact
seven moments at EVERY sufficiently long finite cutoff and converge to X_N.

(d) With N fixed and h->+infinity,

    log E exp(h X_N)
      = (h/2)log h -(h/2)[1+log(2*pi)] +(7/4)log h +C_N+o(1),     (2)

where C_N is finite. Thus the h log h, h, and log h coefficients agree with
those of the ACTUAL normalized xi function. The additive constant is not
matched. In particular, relative transform error is not claimed to tend to zero.

(e) The complete right tail has the sharp logarithmic asymptotic

    lim_(x->infinity) exp(-2x) log P(X_N>=x) = -pi.                 (3)

Symmetry gives the left tail. This is also the exact leading tail coefficient
of the actual theta law, but does not identify their densities.

(f) For all sufficiently large N,

    0.20 < [E X_N^16-mu_16]/v^8 <0.21.                            (4)

Consequently NONE of those laws is the theta law. As N->infinity the laws
converge back to the finite seed on every fixed complex transform disk.
The large-field asymptotic (2) is NOT uniform in N. The order of limits matters.

The theorem resolves construction and global-limit control for this class.
It is not a new unconditional zero statement for Xi.

## 2. Exact construction of a countable star

Here is a useful general construction, separately from the theta parameters.
Let epsilon be a symmetric sign and eta_j be independent signs with
E eta_j=r_j, 0<=r_j<1. Given a_0>=0 and a_j>0, put

    X_L=epsilon [a_0+sum_(j<=L) a_j eta_j].                       (5)

The physical spins are sigma_0=epsilon, sigma_j=epsilon eta_j. Their law is
exactly the zero-field star Ising law with J_0j=atanh(r_j)>=0. This follows
from P(eta_j=e)=(1+r_j e)/2=exp(J_0j e)/(2 cosh J_0j). Its normalized partition
function is

    M_L(h)=1/2 [exp(a_0 h) product_j(cosh(a_j h)+r_j sinh(a_j h))
              +exp(-a_0 h) product_j(cosh(a_j h)-r_j sinh(a_j h))]. (6)

If sum a_j^2<infinity and sum a_j r_j<infinity, the bracket in (5) converges
in L2, by centering its independent summands. Its mean is
m=a_0+sum a_j r_j and its variance about that mean is
s2=sum a_j^2(1-r_j^2). Thus

    E X^2=m^2+s2.                                                 (7)

The products in (6) converge locally uniformly for COMPLEX h, since on any
fixed disk a small factor differs from 1 by O_R(a_j r_j+a_j^2). They equal
the moment generating function of the L2 limit. One proof of uniform
integrability uses the elementary bounded-sign Hoeffding bound

    E exp[h sum a_j(eta_j-r_j)] <= exp(h^2 sum a_j^2/2), h real.

For completeness that inequality follows by twice differentiating the
log-mgf of one sign: its second derivative is at most a_j^2; its value and
first derivative at zero vanish. Sum and integrate twice. The same estimate
at 2h supplies uniform integrability of exp(h X_L). All moments converge.

Weighted Lee--Yang for each finite graph and Hurwitz on both nonreal
half-planes prove that M(iz) has only real zeros. M(0)=1 prevents an identically
zero limit. No inverse spectral or positivity inference is needed. This uses
the classical theorem, not a newly proved Lee--Yang result.

For the harmonic leaves below, sum J_0j diverges. We define the law by the
explicit product probability and its finite-volume limits, NOT by pretending
that an absolutely summable infinite Hamiltonian has been constructed.

## 3. The harmonic leaves and their complete large-field asymptotic

Fix c>0, d>=0, and an integer N>d. Attach leaves indexed by n>=N with

    a_n=c/n,              r_n=d/n.                                (8)

Their positive-root conditional mgf is

    P_(N,+)(h)=product_(n>=N) [cosh(ch/n)+(d/n)sinh(ch/n)].         (9)

The negative-root version replaces d by -d. Both products are defined by
Section 2. Let H_k=sum_(n=1)^k 1/n, H_0=0, and

    A=2*EulerGamma-1+log(4/pi).

We prove, for x->+infinity with N,d FIXED,

    sum_(n>=N) log cosh(x/n)
       =x log x +(A-H_(N-1))x +(N-1/2)log 2+O(1/x),             (10)
    sum_(n>=N) log[1+(d/n)tanh(x/n)]
       =d log x +B_(N,d)+o(1),                                 (11)

with finite B_(N,d). Formula (11) also holds for -d, as N>d.
An optional explicit constant is

    B_(N,d)=d[EulerGamma+log(4/pi)]
                         +log Gamma(N)-log Gamma(N+d).          (12)

Only positive gamma arguments occur. The exact constant is not needed for
the root existence theorem, but makes the asymptotic fully specified.

### 3.1 Proof of (10), including evaluation of the constant

Set g(u)=log cosh(1/u)-exp(-u)/u. It extends smoothly to u=0 with
g(0)=1-log 2, g'(0)=-1/2. At infinity it and its derivatives have the
integrable inverse-power bounds obtained by Taylor expansion of log cosh.
In particular g'' is integrable. Euler--Maclaurin with its integrable
remainder gives

    sum_(n>=1)g(n/x)=x integral_0^infinity g(u)du -g(0)/2+O(1/x).

Also x sum exp(-n/x)/n=-x log(1-exp(-1/x))=x log x+1/2+O(1/x).
Adding proves (10) for N=1 with A=integral g. Subtract the finitely many
terms n<N, using log cosh(x/n)=x/n-log2+O_N(exp(-2x/(N-1))).
The N=1 subtraction is empty.

To evaluate A, integration by parts gives A=I+EulerGamma-1, where

    I=integral_0^1 tanh(t)dt/t
                         +integral_1^infinity [tanh(t)-1]dt/t.

The standard gamma integral and absolutely convergent sech-squared expansion
initially for Re s>1 give

    integral_0^infinity t^s sech(t)^2 dt
             =2^(1-s) Gamma(1+s) eta(s),
    eta(s)=(1-2^(1-s))zeta(s).

The integral is analytic for Re s>-1, and so is the right side there, hence
the identity continues to s=0. Differentiate there. The classical values
zeta(0)=-1/2, zeta'(0)=-log(2*pi)/2, Gamma'(1)=-EulerGamma give
integral log(t)sech(t)^2dt=log(pi/4)-EulerGamma. A separate integration by
parts on [epsilon,R], followed by both endpoint limits, makes that integral
-I. Thus I=EulerGamma+log(4/pi), giving A as stated. These classical special
values are credited to DLMF; no RH input enters them.

### 3.2 Proof of (11), and derivative estimates needed for the probability tail

Let S_N(x)=sum_(n>=N)log cosh(x/n). Convexity and (10), or difference
quotients with increment sqrt(x), give

    S_N'(x)=log x +A+1-H_(N-1)+o(1).                            (13)

Its second derivative is a Riemann sum:

    S_N''(x)=sum_(n>=N)sech(x/n)^2/n^2=1/x+O_N(1/x^2).           (14)

Indeed k(u)=u^-2 sech(1/u)^2 has integrable derivative and integral one.
The elementary bounded-variation Riemann-sum error is O(1); multiplying
by x^-2 proves (14). Deleting n<N adds an exponentially small error.

Subtract d S_N'(x) from the left side of (11). Its summands converge to
log(1+d/n)-d/n and are uniformly O_d(n^-2), so dominated summation proves
(11). The classical finite gamma product and H_(m)=log m+EulerGamma+o(1)
give (12). The argument with -d uses 1-d/n>=1-d/N>0.

Differentiating the actual series, not an unspecified remainder, gives for
the left side B_N(x) of (11)

    B_N'(x)=O_(N,d)(1/x),          B_N''(x)=O_(N,d)(1/x^2).        (15)

For the first bound compare with |d| sum sech(x/n)^2/n^2. The second is
bounded by constant multiples of sum n^-3 sech(x/n)^2 and sum n^-4
sech(x/n)^4, of orders x^-2 and x^-3 by the same Riemann-sum argument.
All denominators are bounded below by 1-|d|/N. These estimates justify all
later tilted-variance calculations.

## 4. Choose the theta growth exactly, without changing a finite jet appreciably

Return to the 272-spin core. Its root is sigma_0, one of the dimer spins.
Join each of the other 270 formerly independent signs to sigma_0 with coupling
j_N=N^-2. The old dimer coupling remains log(3/2)/2. Thus the finite core is
now one connected star. Its positive weights still depend on u in the
inherited box. Its total weight is

    A_core(u)=sqrt(v)[sum_i nu_i sqrt(x_i)+sqrt(y)].               (16)

Set c=1/2, d=7/4 in (8), take N>=3, and introduce ALSO M=N^2 finite leaves
with common weight b_N(u)/M and common correlation r_ball=M^-2, where

    b_N(u)=H_(N-1)/2-EulerGamma-log2-A_core(u).                    (17)

For every sufficiently large N, b_N is positive throughout the fixed compact
parameter box. Its size is O(log N); its first parameter derivatives are O(1).
Every ballast coupling is atanh(M^-2)>0. Attach these leaves to the SAME root.
Finally attach all harmonic leaves (8), n>=N, to that root.

This defines X_N(u) by Section 2. For each finite harmonic cutoff L>=N-1
it defines X_(N,L)(u), on 272+N^2+max(0,L-N+1) vertices, all in ONE connected
star. No table of its exponentially many configurations is needed: (6) is exact.

### 4.1 Small complete perturbation on each fixed complex disk

The harmonic part has sum a_n r_n=cd sum n^-2=O(1/N) and sum a_n^2=O(1/N).
Uniformly for |h|<=R, its two conditional products differ from 1 by O_R(1/N).
For example when N is large relative to R, each factor differs from one by
at most (c^2 R^2+2|d|cR)/n^2; summing logarithms proves the assertion with a
convergent complete tail, not a finite cutoff assumption.

The ballast conditional log-products are bounded by

    O_R(b_N^2/M + b_N r_ball)=O_R(log^2(N)/N^2).                  (18)

Their first u derivatives satisfy the analogous bound with b_N replaced in
one factor by its bounded derivative. The finite core bridge perturbation
is O_R(N^-2), also after one u derivative. Square roots and their derivatives
are bounded on a slightly larger compact positive box.

Consequently, uniformly over that box and EACH fixed complex disk,

    ||M_(X_N(u))-M_(X_*(u))||_(C^1 in u)=O_R(1/N).                (19)

The same bound holds for ALL finite L>=N-1. The full infinite-to-finite tail
has C1 error O_R(1/(L+1)). For L=N-1 the harmonic sum is empty.
On a sufficiently small fixed h-disk the core mgf is uniformly separated
from zero. Hence local logarithms, Cauchy estimates and moment/cumulant
coefficients preserve the C1 convergence in (19). No global logarithm
through unknown zeros is taken.

### 4.2 Retune the core to preserve the seven exact theta moments

Let F_N(u) be the first seven even cumulants of X_N(u), divided by the same
nonzero constants c_(2r) v^r as in the inherited F, minus the exact theta
cumulant targets. Then F_N->F in C1 on the box, at O(1/N), and likewise for
F_(N,L), uniformly in L. The inherited strict bounds (1) imply that for all
sufficiently large N, u->u-R F_N(u) is a contraction of that SAME box into
itself. For example, if delta_N bounds ||F_N-F|| and epsilon_N bounds
||D F_N-D F||, the precise sufficient conditions are

    L0+||R|| epsilon_N<1,
    beta0+||R|| delta_N +(L0+||R|| epsilon_N)rho<rho.                (20)

Both errors tend to zero by (19). Banach gives a unique root u_N in the box,
and the same reasoning gives u_(N,L) for every finite L. Subtracting the
fixed-point equations proves

    u_N-u*=O(1/N),       u_(N,L)-u_N=O(1/(L+1)).                  (21)

Thus X_N:=X_N(u_N) has moments (c), and the retuned FINITE stars X_(N,L)
converge on each complex disk to it. The cutoffs are not a projectively
consistent parameter family after retuning; convergence, not consistency,
is the assertion. The unretuned law at fixed u_N has the product construction.

This is an all-sufficiently-large-N existence proof using a strict inherited
root. No explicit numerical N0 or new retuned parameter box is certified in
this packet. The estimates make N0 effectively obtainable, but it was not
computed. It is NOT asserted that the old rounded center itself is an exact
solution of the perturbed equations. The same argument works for any fixed
regular finite-star moment seed; it is not an arbitrary-order existence theorem.

## 5. Whole-function growth, analytic density, and the exact tail coefficient

Fix one sufficiently large N and its exact u_N. In the positive-root term
of (6), all finite leaves eventually align in a positive real field. Their
contribution has logarithm [A_core+b_N]h+constant+O_N(exp(-c_N h)), with c_N>0.
The negative-root term is smaller by an exponential exp(-2a_0 h), times a
fixed constant and h^(-2d+o(1)); a_0=sqrt(v y)/2>0. Equations (10)--(11) give

    log M_N(h)=c h log h
       +[A_core+b_N+c(log c+A-H_(N-1))]h+d log h+C_N+o(1).         (22)

Insert c=1/2, d=7/4, A=2*EulerGamma-1+log(4/pi), and (17). The bracket is
EXACTLY -[1+log(2*pi)]/2, proving (2). None of these constants is fitted to
a hypothetical zero or a high-frequency value of Xi.

For explicit bookkeeping, if p_all is the probability that the finite core
and all M ballast leaves are positive, including root probability 1/2, then

    C_N=log p_all +(N-1/2)log2
       +d log c+d[EulerGamma+log(4/pi)]
       +log Gamma(N)-log Gamma(N+d).                            (23)

The probability is a finite positive product in the stated correlations.
It can be extremely small; its logarithm is NOT bounded uniformly in N.
Classical Stirling, zeta(s)->1 for real s->infinity, and the definition of xi
show that log M_theta(h) has the same three growing terms in (2). Its constant
is different in general, and (4) already proves nonidentity of the transforms.

The series derivative bounds (13)--(15) and the finite positive alignment
calculation give, without differentiating (22) as a bare asymptotic,

    Lambda_N'(h)=c log h+c+ell+o(1),
    Lambda_N''(h)=c/h+O_N(h^-2),
    ell=-[1+log(2*pi)]/2.                                       (24)

These are the mean and variance under exponential tilting.

For clarity, (22) implies order one: for complex h, |M_N(h)|<=M_N(|h|),
while the positive real axis realizes exp(c h log h+O(h)). Section 2 already
proves the Fourier zeros are real. No claim about their exact counting
constant, individual positions, or simplicity is made.

The distribution has an analytic density. At real t and n>=max(N,2d,2c|t|),

    |cos(ct/n)+i(d/n)sin(ct/n)|^2
       =1-[1-d^2/n^2]sin^2(ct/n).

Use sin^2 u>=u^2/4 for |u|<=1/2. Summing the resulting logarithmic upper
bounds and using sum_(n>=k)n^-2>=1/k proves, for all sufficiently large |t|,

    |M_N(it)|<=exp(-c|t|/64).                                  (25)

Finite factors have modulus at most one. Fourier inversion therefore gives a
nonnegative real-analytic density; no claim of an entire density is made.

### 5.1 Proof of the complete probability-tail asymptotic

For any law satisfying (22),(24), Chernoff at
h=exp[(x-c-ell)/c] gives

    limsup exp(-x/c)log P(X>=x) <= -c exp[-(c+ell)/c].             (26)

For the reverse inequality fix epsilon>0 and choose a tilt h_x with
Lambda'(h_x)=x+epsilon/2. Such h_x exists for large x by strict convexity
and (24). Its tilted variance tends to zero. Chebyshev gives tilted
probability at least 1/2 on [x,x+epsilon] for sufficiently large x. Undoing
the tilt yields

    P(X>=x)>= (1/2) exp[Lambda(h_x)-h_x(x+epsilon)].               (27)

Equation (24) says h_x=exp[(x+epsilon/2-c-ell)/c+o(1)]. Substitution in (27),
then epsilon down to zero, matches (26). Thus the limit equals
-c exp[-(c+ell)/c]. At c=1/2 and the displayed ell it is exactly -pi.
This proves (3), over the full unbounded probability tail.

For the actual theta density, its first positive summand and the geometrically
bounded remaining summands give log phi(x)=-pi exp(2x)+O(x). Integrating over
[x,infinity), and using an interval of length exp(-2x) for a lower bound,
gives the same limit -pi. This comparison is unconditional and does not use
any real-zero assertion for the target.

## 6. What this accomplishes and why it does not complete RH

By (19),(21), X_N converges to X_*(u*) in every fixed moment, including order
sixteen. The inherited strict error interval therefore proves (4) for all
sufficiently large N. All these connected, analytic, unbounded-support,
real-zero laws are still NOT Xi. This is a mathematical nonidentity, not
merely an absence of a proof of equality.

The construction removes three design difficulties simultaneously: it has a
single genuinely infinite correlated component, it preserves the existing
seven exact theta moments, and it has the correct theta-scale large-field
and probability-tail constants. Those properties do not control the missing
higher theta moments. The limit N->infinity here is the old finite seed, NOT
the theta law. The asymptotic regime escapes with N; exchanging those two
limits would be invalid.

For a successful RH route one must instead construct finite ferromagnets
whose moment order tends to infinity and whose moments approach the actual
theta moments. Weighted Lee--Yang gives

    E X^(2r)/(2r)! <= [Var(X)/2]^r/r!,

by the paired canonical product. A bounded variance then pays complete
complex Taylor tails. Moment convergence implies locally uniform convergence
to Xi/Xi(0); Hurwitz would finish. The missing all-order reachability is not
proved by (20), which is a FIXED-order perturbation theorem. The new model is
a globally controlled family in which to seek that construction, not an
unconditional RH proposal with a hidden final lemma.

## References and claim provenance

ICR1: PR #863, exact source in SOURCES.json; this packet replays its producer,
not an independent transcendental backend or a new referee acceptance.
Weighted Lee--Yang: Newman--Wu, arXiv:1901.06596v2, p.11, (21) and following
weighted specialization. The theorem is imported; the product probability,
limits, asymptotics and grafting calculation above are supplied here.
Euler--Maclaurin and gamma special values: DLMF 2.10, 5.4, 5.11, 25.6.
Independent-sign convergence, Cauchy/Hurwitz, Banach and elementary exponential
tilting are classical mechanisms. No exhaustive novelty or priority claim.
