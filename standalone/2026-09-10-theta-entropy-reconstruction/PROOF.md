# Whole-theta entropy reconstruction and the pair-interaction boundary

Date: 2026-09-10. Research continuation of PR #842.
Status: PROPOSED COMPONENT PROOFS; independent mathematical review required.
**The pair-ferromagnetic realization and RH remain UNPROVED.**

This note constructs a sequence of finite spin laws converging to the WHOLE
unmodified theta law, with all moments and locally uniform entire generating
functions. The construction has nonnegative even MANY-SPIN interactions. It
is not a solution of the parent's PAIR-Ising realization problem. An exact
four-spin example and a continuous sixth-cumulant certificate show why applying
Lee--Yang to the larger class would give a false proof.

The completed contribution is a prescribed source reconstruction, not more
moment fitting. Its mechanism is generalized Curie--Weiss entropy cancellation,
which is classical. No external novelty, priority, or independent acceptance is
claimed. Sections 1--4 prove the reconstruction. Section 5 states, but does not
prove, a source-specific pair replacement that would finish RH. Section 6
rules out a universal replacement assertion. Earlier packets are unchanged.

## 1. The exact source and a global envelope

Use the parent's full-line convention, with the ENTIRE completion of xi:

    Xi(z)=xi(1/2+iz)=integral_R phi(t) exp(izt)dt,
    phi(t)=sum_(n>=1) exp(t/2)[4Q_n(t)^2-6Q_n(t)] exp(-Q_n(t)),
    Q_n(t)=pi n^2 exp(2t),
    Z=Xi(0)>0, w=phi/Z.                                         (1)

Jacobi inversion makes phi even. On t>=0 each summand is strictly positive;
reflection, not termwise positivity on the negative half-line, gives phi>0 on
R. The locally differentiated series and its double-exponential tails are the
inherited classical theta facts. No determinant theorem, zero-location claim,
finite seed calculation, or new numerical theta integral is used here.

Let U have law w(t)dt. Its generating function is exactly

    M_U(h)=xi(1/2+h)/xi(1/2).                                   (2)

For the parent's standardized X=U/sigma, sigma^2=E U^2>0,
M_X(h)=xi(1/2+h/sigma)/xi(1/2). We work with U until the final standardization.

The elementary bound needed for the construction is

    0<phi(t)<256 exp(-t^2),  t in R.                            (3)

For t>=0, put q=Q_n(t)>3n^2 exp(2t). Since
 t^2+t/2 <= (3/2)exp(2t) <= q/2,
 e^(t^2) phi_n(t) <= 4q^2 exp(-q/2)
                    <= 256 exp(-q/4).
The first inequality follows already from exp(2t)>=1+2t+2t^2. The last uses
max_(q>=0) q^2 exp(-q/4)=64 exp(-2)<64. Finally
sum_n exp(-3n^2/4)<sum_n 2^(-n)=1: exp(3/4)>2 follows from its first four
Taylor terms. Reflection proves (3) on R. Since exp(6)>256, (3) also gives

    7-t^2-log phi(t)>1.                                        (4)

The constants are deliberately crude. They supply global domination, not an
estimate for the sign of a Fourier transform.

## 2. ER1: any confining even polynomial has an explicit positive many-spin lift

Fix an even real polynomial

    P(x)=v_0+sum_(r=1)^d v_r x^(2r),

of degree 2d>=2 with positive leading coefficient. For an integer L define

    N=L^(2d+1), S=sum_(i=1)^N sigma_i, sigma_i in {-1,1},
    m=S/N, X_(P,L)=S/L^(2d)=L m,
    I_d(m)=sum_(r=1)^d m^(2r)/[2r(2r-1)].

The probability of a configuration is proportional to exp(H_(P,L)), where

    H_(P,L)=N I_d(S/N)-P(S/L^(2d))
      =-v_0+sum_(r=1)^d b_(r,L)(S/N)^(2r),
    b_(r,L)=N/[2r(2r-1)]-v_r L^(2r).                         (5)

Here H is the exponent, the negative of the conventionally named energy.
Choose

    L>max(1, max_(r:v_r>0) 2r(2r-1)v_r).                       (6)

Every b_(r,L) is strictly positive, since N/L^(2r)=L^(2d+1-2r)>=L.
For rational P the number of spins, the common observable weight L^(-2d),
and ALL expanded interaction coefficients are rational at each L.

After reducing sigma_i^2=1, each S^(2r) is a nonnegative integer combination
of products over even subsets of distinct spins, plus a constant. Indeed its
expansion counts ordered tuples of 2r indices with a specified parity set.
For a specified subset A of size 2k the coefficient is precisely

    (2r)! [z^(2r)] sinh(z)^(2k) cosh(z)^(N-2k).               (7)

All coefficients in (7) are nonnegative, and odd subsets are absent. Thus (5)
has nonnegative even-subset interactions of orders at most 2d, zero external
field, and one common positive magnetization weight. Its pair terms are
strictly positive. This is NOT a pair-only Hamiltonian when d>1.

There is also literal conditional pair attraction: H, viewed as a polynomial
in S, is convex, so for every possible sum s of the other spins,

    H(s+2)+H(s-2)-2H(s)>=0.                                  (8)

This describes two-spin conditional log-supermodularity. It does not delete
the higher-body interactions or imply the pair-Ising Lee--Yang theorem.

**ER1.** As L tends to infinity through integers satisfying (6), X_(P,L)
converges to the law with density exp(-P)/integral exp(-P). Every moment
converges, and its generating functions converge uniformly on EVERY fixed
complex compact. No zero-location conclusion is part of ER1.

### 2.1 Exact magnetization weights and local cancellation

For k=0,...,N put m_k=(2k-N)/N, x_k=L m_k and Delta_L=2/L^(2d).
The unnormalized weight at x_k is

    binom(N,k) exp(N I_d(m_k)-P(x_k)).                       (9)

Define the Bernoulli entropy, with the endpoint values by continuity,

    I(m)=[(1+m)log(1+m)+(1-m)log(1-m)]/2
        =sum_(r>=1) m^(2r)/[2r(2r-1)], |m|<=1.             (10)

This expansion follows by differentiating and integrating the geometric
series, with I(0)=I'(0)=0. Its terms are nonnegative. In particular

 0<=N[I(x/L)-I_d(x/L)]
 <= |x|^(2d+2)/{L(2d+2)(2d+1)[1-(R/L)^2]}, |x|<=R<L.       (11)

Let

    A_(L,k)=sqrt(pi N/2) 2^(-N) binom(N,k) exp(N I_d(m_k)).

For |m_k|<=1/2, the factorial bounds
 log(n!)=(n+1/2)log n-n+log(2pi)/2+r_n, 0<r_n<1/(12n),
give the exact expression

 A_(L,k)=(1-m_k^2)^(-1/2)
          exp(r_N-r_k-r_(N-k)) exp(-N[I-I_d](m_k)).         (12)

These standard Stirling bounds are the only factorial asymptotic used. The
endpoints k=0,N are not inserted in (12); they are treated below. For large L,
A_(L,k)<=2 on |m_k|<=1/2, and (11)--(12) show

    A_(L,k)=1+O_(P,R)(1/L), uniformly when |x_k|<=R.         (13)

The implied bound is obtainable directly from (11), (12) and rational bounds
for exp and sqrt. No growing-order uniformity is asserted with d varying.

### 2.2 The complete endpoint and remote mass

The elementary binomial entropy bound is

    2^(-N)binom(N,k)<=exp(-N I(m_k)), 0<=k<=N.              (14)

For interior k, retain its single term in the binomial theorem with success
probability k/N; the endpoint cases follow directly. On |m|>1/2,

    I(m)-I_d(m)>=c_d:=2^(-2d-2)/[(2d+2)(2d+1)]>0.         (15)

Because P is confining, for every fixed R>=0 the finite constant
C_(P,R)=sup_x exp(-P(x)+R|x|) exists. The ENTIRE contribution of |m_k|>1/2
to the Delta_L-scaled sum with an exponential test of modulus at most
exp(R|x_k|) is bounded by

    Delta_L (N+1) sqrt(pi N/2) C_(P,R) exp(-N c_d)->0.       (16)

This includes the two all-aligned configurations, not just a central saddle.
In the remaining region A_(L,k)<=2. The functions exp(-P(x)+R|x|) and every
fixed polynomial times them have integrable, eventually decreasing tails on
both half-lines. Their grid sums outside a fixed compact are bounded uniformly
by tail integrals and one mesh endpoint term. This follows by comparison of
rectangles with an integral on each monotone tail; Delta_L->0.

On a fixed compact (13) and ordinary Riemann sums give

 Delta_L sum_k A_(L,k)exp(-P(x_k)) g(x_k)
        -> integral_R exp(-P(x))g(x)dx,                    (17)

for every monomial g and for g(x)=exp(hx), uniformly on |h|<=R. Uniformity
uses the common majorant exp(R|x|) and uniform continuity on a fixed compact.
The offset of the lattice when N is odd changes neither its mesh nor these
estimates. Apply (17) also with g=1; its limit is strictly positive. Ratios
therefore prove ER1, including normalization and all complex compact limits.

For fixed rational P these are effective bounds: choose a polynomial-tail
cutoff, use (11)--(12) inside it, and bound each Riemann error by the mesh times
an endpoint bound plus the length times a derivative bound. Equation (16)
pays the remaining endpoint region. They permit a finite search for L at any
prescribed finite moment/compact accuracy. No large such search was executed.

## 3. ER2: rational confining potentials reconstruct the whole theta density

Define the positive continuous EVEN function

    q(t)=sqrt(7-t^2-log phi(t)).                             (18)

For each integer j>=1 choose an even rational polynomial Q_j with

    sup_(|t|<=j) |Q_j(t)^2-q(t)^2|<=2^(-j),
    P_j(t)=t^2+Q_j(t)^2.                                   (19)

These are not polynomials chosen from zeros or fitted to a finite zero table.
They approximate the literal density. Each P_j is rational, even, confining,
and satisfies P_j(t)>=t^2 on the ENTIRE real line.

Here is a fully specified constructive way of choosing (19). A rational upper
bound B_j for sup|q| and a rational Lipschitz bound Lambda_j on [-j,j] can be
obtained from the source series. For example on [0,j],

 phi(t)>=18 exp(-4 exp(2j)),
 |phi'(t)|<=2238 exp(j/2),
 |q(t)|<=4exp(j),
 |q'(t)|<=j+63exp(j/2+4exp(2j)).                            (20)

The first bound retains just n=1. For the second, differentiate once and use
|P_1(Q)|<=8Q^3+30Q^2+15Q, Q^k exp(-Q/2)<=(2k)^k,
and sum exp(-3n^2/2)<1. Equations (4), (18) give the last two bounds;
reflection covers [-j,0]. Rational ceilings of (20) suffice.

Put delta_j=min(1,2^(-j)/(2B_j+1)). Map [-j,j] to [0,1], take a Bernstein
polynomial of degree n_j>=(2j Lambda_j/delta_j)^2, and approximate EACH of
its finitely many node values of q by a rational within delta_j/2. The binomial
variance identity gives Bernstein error at most j Lambda_j/sqrt(n_j), so the
combined error is at most delta_j. Replace the resulting polynomial R(t) by
[R(t)+R(-t)]/2. Evenness of q preserves the error, all coefficients are rational,
and |Q_j^2-q^2|<=delta_j(2B_j+delta_j)<=2^(-j).

All source evaluations in this prescription are computable from the locally
uniform theta series, its positive lower bounds, and complete geometric tails;
log and square root are evaluated on positive intervals. This is a constructive
paper specification, NOT a numerical execution of these potentially enormous
polynomials. One may use smaller verified bounds; no complexity claim is made.

By (19), on [-j,j], |P_j-(7-log phi)|<=2^(-j). Both exp(-P_j) and exp(-7)phi
are bounded by exp(-t^2), by (3) and exp(7)>256. Hence, for every fixed R,

 integral_R exp(R|t|)|exp(-P_j(t))-exp(-7)phi(t)|dt
 <=(exp(2^(-j))-1)exp(-7) integral_R exp(R|t|)phi(t)dt
      +2 integral_(|t|>j) exp(-t^2+R|t|)dt ->0.              (21)

Normalization constants converge to exp(-7)Z>0. Thus the normalized polynomial
laws converge to w in every exponentially weighted L1 norm, in every moment,
and uniformly on every complex compact of their generating functions.

## 4. ER3: an all-order finite spin reconstruction -- in the larger class

Apply ER1 to each P_j. Choose an integer L_j satisfying (6), large enough that
its normalized spin law agrees with exp(-P_j)/integral exp(-P_j) to accuracy
2^(-j) on |h|<=j and in each moment through order 2j. The effective estimates
after (17) permit this choice without inspecting any zeros. Combining with
(21) gives finite zero-field spin laws mu_j, each with a common positive field
weight and nonnegative even MANY-SPIN couplings, for which

    M_(mu_j)(h) -> xi(1/2+h)/xi(1/2)
              locally uniformly for ALL h in C.             (22)

Every fixed moment converges to its exact theta value. Standardizing each law
by its own positive standard deviation gives the parent's variance-one theta
law and the corresponding limit with h/sigma. The variances converge to the
positive sigma^2 by (17), (21). Spin counts and interaction orders may grow;
neither an efficient bound nor a small explicit high-order instance is claimed.

ER3 is an unconditional whole-source realization, but in a strictly larger
class than the PAIR-Ising class needed for the parent's Lee--Yang ending.
The procedure also works for other even positive densities with a global
Gaussian envelope. That universality is a warning: it cannot itself establish
an arithmetic zero theorem. Section 6 supplies exact counterexamples.

## 5. The attempted pair reduction: sufficient statement, still OPEN

For the prescribed j-th model let N_j be its visible spin count, a_j its common
field weight, and H_j(S) the exponent (5). Define the unnormalized weight of
a magnetization level by

    q_j(k)=binom(N_j,k)exp(H_j(2k-N_j)), 0<=k<=N_j.           (23)

Seek a finite ZERO-FIELD PAIR graph with J_e>=0, whose N_j visible spins have
weight a_j and whose auxiliary spins have weight zero. Let Q_j(k) be its FULL
restricted partition sum over every visible configuration of that level and
every auxiliary-spin configuration. The following is a sufficient premise:

 There are b_j in R and epsilon_j->0 such that, for EVERY k=0,...,N_j,

 exp(-epsilon_j) q_j(k) <= exp(-b_j) Q_j(k)
                       <= exp(epsilon_j) q_j(k).           OPEN-PAIR (24)

Neither existence of these graphs nor (24) has been proved. The auxiliary
sum is essential: selecting only aligned hidden configurations is insufficient.
The criterion is sufficient, not asserted necessary or equivalent to RH.

If (24) holds, normalized magnetization probabilities have density ratio in
[exp(-2epsilon_j),exp(2epsilon_j)]. For |h|<=R, symmetry gives the COMPLETE
complex-field comparison

 |M_(pair,j)(h)-M_(mu_j)(h)|
 <=(exp(2epsilon_j)-1) M_(mu_j)(R)->0.                       (25)

Equation (22) bounds M_(mu_j)(R) uniformly at each fixed R. Every finite pair
model's generating function is zero-free on Re h>0 and Re h<0 by classical
multivariate Lee--Yang. Zero weights of the auxiliary spins follow by adding
positive weights tending to zero and applying Hurwitz; finite-model positivity
at a real field excludes an identically zero limit.

Apply Hurwitz again to (22), (25). The limit is nonzero identically because
its value at zero is one. Thus xi(1/2+h) has no zero off the imaginary h-axis,
and RH follows. This proves the CONDITIONAL ENDING from (24), not (24).
No hidden infinite-tail condition is needed after the stated comparison.

This direct test differs from free moment fitting: the target level weights
are fixed by the exact theta-density prescription. A source-specific pair
replacement, or a weaker comparison that still pays the full compact-field
error, is the missing new theorem. It is not delegated to reviewers as routine.

## 6. Why a generic positive-interaction completion is false

### 6.1 Four spins already separate pair Lee--Yang from positive many-spin weights

Let four spins have zero-field weight exp(J sigma_1 sigma_2 sigma_3 sigma_4),
J>0, and observable sum sigma_i. Put r=exp(-2J) in (0,1), u=exp(2h).
After a nonzero exponential normalization, its field partition polynomial is

    P_r(u)=u^4+4r u^3+6u^2+4r u+1.                         (26)

This follows by grouping the sixteen configurations by the number of minus
spins: even numbers have weight exp(J), odd numbers exp(-J). Dividing by u^2
and putting y=u+1/u gives

    P_r(u)/u^2=y^2+4ry+4.                                  (27)

Its discriminant is 16(r^2-1)<0. If |u|=1, y is real, so P_r has NO unit-circle
root. Its four nonzero roots therefore give generating-function zeros off the
imaginary h-axis. This holds for EVERY J>0, arbitrarily small. The coefficient
sign alone is not a Lee--Yang theorem. This example changes the source; none
of its zeros is asserted to be a zeta zero.

The failure persists WITH positive pair interactions and conditional attraction.
Take four spins with H=J S^4, S=sum sigma_i, and q=exp(16J)=101/100. Exactly,

    S^4=40+32 sum_(i<j) sigma_i sigma_j+24 sigma_1 sigma_2 sigma_3 sigma_4.

Thus all six pair couplings and the four-body coupling are positive, and H(S)
is convex. Its field polynomial is

    q^16(u^4+1)+4q(u^3+u)+6u^2.

After division by q^16 u^2 its quadratic in y=u+1/u has discriminant

    8(q^30-3q^14+2)/q^30 < 0,  q=101/100.                  (27a)

The last inequality is checked as an exact rational inequality, as is the
complete sixteen-configuration polynomial. Thus all roots are again off the
unit circle. Adding conditional attraction or a connected positive pair part
to a general many-spin model does not fix the invalid inference.

### 6.2 The same entropy construction can have a non-Lee--Yang limit

Take the explicit even potential

    P_*(x)=x^2/2+10^(-6)x^6.                               (28)

Its derivative is convex on [0,infinity), since P_*'''(x)=120*10^(-6)x^3>=0.
Nevertheless its normalized density has STRICTLY NEGATIVE sixth cumulant.
This statement is certified using rational arithmetic, with the whole real
integral retained. If G is standard Gaussian, e=10^(-6), and
mu_n=E G^n=(n-1)!! for even n (mu_0=1), then for n=0,2,4,6,

 mu_n-e mu_(n+6) <= A_n:=E[G^n exp(-eG^6)]
 <= mu_n-e mu_(n+6)+(e^2/2)mu_(n+12).                       (29)

Indeed 1-v<=exp(-v)<=1-v+v^2/2 for v>=0. All lower bounds in (29) are positive.
Normalize m_n=A_n/A_0, with positive interval division, and evaluate

    kappa_6=m_6-15m_4 m_2+30m_2^3.

The exact rational reconstruction yields the safe strict enclosure

    -740/10^6 < kappa_6 < -696/10^6 < -1/2000.               (30)

For a finite symmetric PAIR-ferromagnetic magnetization, Lee--Yang and the
exponential-type even Hadamard product give

    M(h)=product_l (1+h^2/y_l^2),
    kappa_6=240 sum_l y_l^(-6)>=0.                          (31)

Degenerate constant magnetization has kappa_6=0. Thus a moment-convergent pair
sequence cannot have density (28) as its limit. Equivalently, the density's
entire MGF (of order at most 6/5) cannot have only imaginary zeros: its even
Hadamard product would again imply (31). Only the first statement is needed.

ER1 with d=3, N=L^7, and P=P_* has ALL the positive interaction coefficients
in (5), as well as the conditional attraction (8). Yet its sixth cumulant is
eventually negative by the proved moment convergence. Thus the very entropy
mechanism used for theta, not merely an unrelated four-spin law, fails to
preserve the pair-Ising zero property in general. There can be no universal
pair replacement satisfying (24) for every confining polynomial construction.

This is NOT a negative theta cumulant calculation: the actual theta seed has
positive sixth cumulant. No nonreal zero of the actual xi is produced. The
example tests a proposed generic proof step, not the RH conclusion.

Newman's 1991 paper proves convexity of the derivative of the theta potential
(in its rescaled convention). The publisher's abstract was read, not its full
proof re-audited. The example (28)--(30) shows directly that this smoothness/
convexity property alone cannot replace the missing Lee--Yang assertion.
No full correlation-inequality theorem is asserted for the example here.

## 7. Exact research outcome and independent-review questions

ER1--ER3 supply a complete all-order construction, including the extreme spin
levels, physical tails, normalizers and entire-function convergence. They do
so ONLY in the stated many-spin class. The original pair-Ising all-order
realization remains open. The four-spin and sixth-cumulant tests prove that
forgetting this distinction would turn the manuscript into a false proof.

The new source-specific candidate for the remaining step is (24). Its full
consumer is (25) followed by Lee--Yang and Hurwitz. No candidate graph family
satisfying it is supplied. More accurate finite minima, the connected seed,
classical zero-density facts and positivity of many-spin couplings do not prove
that comparison. RH remains unproved in this pass.

Review (11)--(17) including endpoint mass and lattice offset; the global source
envelope and polynomial domination in (18)--(21); the diagonal choice with d
fixed before L grows; and the distinction between log-supermodularity, even
many-spin signs, and the pair-Ising zero theorem. Finite tests do not prove the
analytic convergence. The counterexamples' laws are not the native theta law.

## Sources and attribution

[P] PR #842 at 8f1f457b0b92e76a0a75bd3d8a8921c205fa75b0,
standalone/2026-09-10-collective-theta-ferromagnets/PROOF.md,
blob 4f3cd5a983b651425ee659d021ce2875a711ef44. Literal theta normalization,
pair-Ising class and preceding open construction; full supplied proof read.
Its seed certificate and code are not rerun or independently accepted here.

[E1] R. S. Ellis and C. M. Newman, The statistics of Curie--Weiss models,
J. Stat. Phys. 19 (1978), 149--161, DOI 10.1007/BF01012508.
Historical attribution for mean-field entropy/critical scaling. Publisher
abstract read; no theorem from the subscription text is used as an unproved
step in ER1. Equations (9)--(17) give the needed argument.

[E2] T. D. Lee and C. N. Yang, Statistical Theory of Equations of State and
Phase Transitions. II. Lattice Gas and Ising Model, Phys. Rev. 87 (1952),
410--419, DOI 10.1103/PhysRev.87.410. Classical pair-ferromagnetic Lee--Yang
input, also used explicitly in the parent. It is not an even-many-body theorem.

[E3] C. M. Newman and W. Wu, Lee--Yang Property and Gaussian multiplicative
chaos, arXiv:1708.08820v3. Public abstract read for scope; the variance/product
and compact-convergence ingredients used here are stated explicitly rather
than claiming a new closure theorem or replay of that entire paper.

[E4] C. M. Newman, The GHS inequality and the Riemann hypothesis,
Constructive Approximation 7 (1991), 389--399, DOI 10.1007/BF01888165.
Publisher abstract/reference page read for the already-known theta convexity.
No result from the reference with a warned erroneous proof is used.

Elementary Stirling bounds, Bernstein approximation, Hadamard factorization
and Hurwitz are classical. No external novelty or completed RH claim is made.
