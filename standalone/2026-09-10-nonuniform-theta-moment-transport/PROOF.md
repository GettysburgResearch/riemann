# Nonuniform pair-Ising moment transport for the exact theta source

Date: 2026-09-10. Continuation of GettysburgResearch/riemann PR #842.
Status: **PROPOSED COMPONENT PROOFS AND A COMPUTER-ASSISTED FINITE EXISTENCE
THEOREM. Independent mathematical and implementation review required.**
The whole-law pair realization and RH remain unproved.

This packet changes from uniform hidden-spin attachments to an interacting,
nonuniform two-block-and-hub graph. It proves existence of a connected 73-spin
PAIR ferromagnet matching the exact standardized theta moments through degree
TEN, with no independent bath. It also proves a finite-order local extension
theorem: at every fixed higher order there are connected realizations retaining
the first ten moments exactly and allowing independent local variation of the
higher moments. The higher-dimensional neighborhood is NOT proved to contain
the higher theta target. There is no all-order induction or global continuation
claim hidden in the local theorem.

Classical Lee--Yang theory, Taylor remainders, contraction mapping, implicit
functions and Vandermonde algebra are credited. No priority claim is made for
these general methods. Labels NMT1--NMT4 are local proposed result identifiers,
not canonical accepted claims. All earlier research files are preserved.

## 1. Fixed source and what is being matched

Use the literal full-line convention from the previous theta packets:

    Xi(z)=xi(1/2+i z)=integral_R phi(t) exp(i z t) dt,
    phi(t)=sum_(n>=1) exp(t/2)(4Q_n(t)^2-6Q_n(t))exp(-Q_n(t)),
    Q_n(t)=pi n^2 exp(2t).                                      (1)

Here xi is its entire completion, xi(0)=xi(1)=1/2. The classical Jacobi identity
for theta(x)=sum_(n in Z) exp(-pi n^2 x) makes
h(t)=exp(t/2)theta(exp(2t)) even, and phi=(h''-h/4)/2. The exponential terms
from n=0 cancel under that differential operation. Splitting the theta Mellin
integral at x=1 and integrating twice by parts gives (1), with coefficients
4 and 6 for this FULL-line Fourier convention. On t>=0 every displayed phi_n
is positive; evenness supplies positivity on the negative side. Locally uniform
convergence of the differentiated theta series and the n=1 double-exponential
tail justify these operations. We use this classical source identity, not any
unproved determinant, spectral-reality, or source-realization claim.

Put

    beta_m=2 integral_0^infinity t^m phi(t)dt  (m even),
    w(t)=phi(t)/beta_0, sigma^2=beta_2/beta_0>0,
    X=t/sigma under w(t)dt,
    theta_(2k)=E X^(2k)=beta_(2k) beta_0^(k-1)/beta_2^k.       (2)

Thus theta_2=1. All odd moments vanish, and the exact generating function is

    M_X(h)=xi(1/2+h/sigma)/xi(1/2).                           (3)

The numerical inputs below are reconstructed from (1)--(2), not from zeta
values, zeros, a model law, or the rounded moment values in an earlier report.

For a finite zero-field pair Ising model with J_e>=0 and observable weights
b_i>=0, the classical multivariate Lee--Yang theorem says that the MGF of
sum b_i sigma_i has no zeros for Re h !=0 [E1]. We import that theorem; we do
not prove it by root computation. Every graph constructed below is in its
literal class, with all observable weights strictly positive.

## 2. The nonuniform 73-spin graph

Take a core of 8 spins, a halo of 64 spins, and one hub spin e. Let s and t be
the two block sums. The graph has all 28 core pairs, all 2016 halo pairs, all
512 cross pairs, and 8 edges connecting the hub to the core. It is connected.
There are 2564 positive edges and no independent bath.

Four variable parameters are p=(q1,q2,a,b). Two ratios are fixed:

    r=101/100, c=1001/1000.

The couplings and the UNNORMALIZED observable are

    J_core=(log q1)/2,       J_halo=(log q2)/2,
    J_cross=(log r)/4,       J_hub-core=(log c)/2,
    A_p=s+a t+b e.                                           (4)

There are no one-site fields in the zero-field Gibbs distribution. Whenever
q1,q2>1 and a,b>0 all edges and observable weights are positive. Normalize by
sqrt(v(p)), where v(p)=E A_p^2, and call the resulting variable Y_p.

After canceling a configuration-independent factor, the exact full weights are

    W_p(s,t,e)=binom(8,(s+8)/2) binom(64,(t+64)/2)
               q1^(s^2/4) q2^(t^2/4) r^(st/4) c^(s e/2),     (5)

for s=-8,-6,...,8, t=-64,-62,...,64, e in {-1,1}. Every exponent is an integer;
negative cross or hub exponents mean ordinary positive rational reciprocals.
The 1170 terms account for ALL 2^73 configurations with exact multiplicities.
They are not a sample, a truncated configuration sum or a selected aligned law.
The omitted common factor depends on q1,q2 but cancels from every normalized
moment and its covariance derivatives.

Define the real analytic map on this positive domain

    F(p)=(E Y_p^4, E Y_p^6, E Y_p^8, E Y_p^10).                (6)

The positive normalizer and variance ensure analyticity. Spin flip supplies
zero odd moments. Therefore F(p)=(theta_4,theta_6,theta_8,theta_10) is precisely
the remaining ten-moment problem, with variance already one.

## 3. NMT1: an entire-source directed moment certificate

The accepting implementation uses integers and Fractions and outward dyadic
intervals with denominator 2^512. Rounding is toward minus/plus infinity at
every arithmetic operation. A zero-containing divisor is rejected.

Pi uses Machin's identity 16 atan(1/5)-4 atan(1/239), with 110 alternating terms
and the full next-term remainder. For exp, range reduction gives |y|<=1/8; the
64th Taylor polynomial is widened by 2/(8^65 65!), followed by repeated interval
squaring. An input <=-512 is enclosed by [0,2^-512], using e>2. This tiny upper
bound, including its multiplication by high-degree polynomials, remains in
all intervals. On a nonpositive input interval, exp is 1-Lipschitz, which pays
the interval width. No hardware floating point or special-function oracle is
used for acceptance. Non-directed scouting only proposed the rational data
in parameters.json.

### 3.1 Integrated Taylor formula and all derivative costs

For phi_n^(j)(t)=exp(t/2-Q)P_j(Q), exact differentiation gives

    P_0(Q)=4Q^2-6Q,
    P_(j+1)(Q)=2Q P_j'(Q)+(1/2-2Q)P_j(Q).                    (7)

Compute the first EIGHT theta terms on [0,2]. Divide that interval into 128
closed midpoint cells, each with halfwidth h=1/128. At each of the 128 centers
c use, for f(t)=t^m sum_(n<=8)phi_n(t), the integrated degree-23 Taylor value

    2 sum_(k even, 0<=k<=22) f^(k)(c) h^(k+1)/(k+1)!.        (8)

All needed f derivatives are computed by Leibniz and (7). The complete error
is controlled by an L1 derivative bound, not an unverified sampled derivative.
On [0,2], exp(t/2)<=3. Substitution dQ=2Q dt shows that

    B_j=12 sum_(k>=1) |[Q^k]P_j| (k-1)!

bounds the L1 norm of sum_(n<=8)phi_n^(j). Consequently

    C_m=sum_(j=0)^min(24,m) binom(24,j) m!/(m-j)!
                                 2^(m-j) B_(24-j)           (9)

bounds the L1 norm of f^(24). For one cell the integral Taylor remainder is
at most h^24/24! times the L1 norm of f^(24) on that cell. Indeed, on the right
half integrate its remainder kernel (t-u)^23/23! first in t; it is bounded by
h^24/24!. The left half is identical in absolute value. Summing cells and
including the full-line factor TWO yields

    error_m <= 2 h^24 C_m/24!.                              (10)

Cell boundaries overlap only in measure zero. Odd Taylor terms integrate to
zero; (10) retains the entire even and odd omitted remainder. This proves the
formula for m=0,2,4,6,8,10 without extrapolating from lower derivative orders.

### 3.2 Every omitted theta index and the infinite t tail

For m>=0, t^m<=m! exp(t) on t>=0, and 4Q^2-6Q<=4Q^2. Substitution in the
positive half-line gives, for Q0=pi n^2 exp(2A)>=3,

    2 integral_A^infinity t^m phi_n(t)dt
      <=4m!(pi n^2)^(-3/4) integral_Q0^infinity Q^(7/4)e^-Q dQ
      <=4m!(Q0^2+2Q0+2)e^-Q0.                              (11)

The last inequality uses pi n^2>=1 and Q^(7/4)<=Q^2 for Q>=1. The function
(Q^2+2Q+2)e^-Q is decreasing for Q>0.

For n>=9 at A=0 use Q0>3n^2 and 3*9^2=243. Consecutive terms of
(9n^4+6n^2+2)e^(-3n^2) have ratio below 1/2 for n>=9: the polynomial ratio is
at most ((n+1)/n)^4<2, and exp[-3(2n+1)]<1/4. Thus their WHOLE sum is bounded
by twice its first term. The omitted-index allowance is

    8m!*59537*exp(-243).                                    (12)

For A=2 use pi e^4>150; e^4>50 follows already from its first 12 positive series
terms. Similarly the ratios for (150^2 n^4+300n^2+2)e^(-150n^2) are below 1/2
for n>=1, since the polynomial ratio is at most 16 and the exponential factor
is at most e^-450. The complete physical-tail allowance, summing ALL n, is

    8m!*22802*exp(-150).                                    (13)

Some omitted terms are covered by both allowances; that is safe upper-bound
double counting, not an equality. Every omitted term is nonnegative. Add their
upper intervals to the quadrature upper endpoint; widen both endpoints by
(10). The positive beta_0 and beta_2 intervals allow (2) to be evaluated with
outward division. No infinity passage is supplied by a finite numerical table.

### 3.3 Reconstructed target values

The complete accepting reconstruction gives the following outward decimal
intervals. The working dyadic endpoints are regenerated in every full run. The receipt
carries outward decimal summaries and exact rational error budgets; none of
these displayed decimals defines the target.

| Moment | Lower endpoint | Upper endpoint |
|---|---:|---:|
| theta_4 | 2.791102858170927391524526752879 | 2.791102858170927391524526752880 |
| theta_6 | 12.217206293689184141951747871455 | 12.217206293689184141951747871467 |
| theta_8 | 71.011785072177779870187897256083 | 71.011785072177779870187897257455 |
| theta_10 | 506.350474548639450117343426455724 | 506.350474548639450117343426617036 |

This is a fresh defining-integral computation. It does not reuse the earlier
seed's broad moment rectangles as precise numerical inputs.

## 4. NMT2: exact ten-moment existence, uniqueness in a box, and robustness

Let p0 be the four EXACT rational centers in parameters.json, starting

    q1=1.13213218673567624874178956649825394860051,
    q2=1.00477768431197281744304500763289525095803,
    a =0.363578933724246212711112802041944122347472,
    b =1.43442779050805879076771866581813807498240.

These are not asserted to be exact solutions. Set R=10^-16 and let
B=p0+[-R,R]^4. Throughout B, q1,q2>1, a,b>0, and the full unnormalized variance
is enclosed by

    27.220495587385463990 <= v(p) <=27.220495587385817104.     (14)

Let Y be the EXACT rational 4-by-4 preconditioner in parameters.json. A numerical
inverse suggested it; exact rational elimination verifies its nonsingularity.
The accepting code reconstructs the following two interval quantities:

    delta = ||Y(F(p0)-theta)||_infinity,
    beta  = sup_(p in B) ||I-Y DF(p)||_infinity.              (15)

Here theta is the vector of the four actual moments. Interval source enclosures
are used in the first quantity, and the WHOLE parameter box in the second.
Both symbols in (15) below denote certified upper bounds, not asserted exact
norms. Specifically,

    delta <1.809*10^-24,
    beta  <8.398*10^-7,
    ||Y||_infinity <26675.                                 (16)

The unrounded rational bounds are in the receipt. The observed image ratio
including target perturbation satisfies

    [delta+10^-22 ||Y||_infinity+beta R]/R
       <0.0266757850866247 <1/2.                            (17)

### 4.1 The derivatives used in the certificate

Writing U_k=E A_p^k, scores for q1,q2 are (s^2/4)/q1 and (t^2/4)/q2. Thus

    partial_q1 U_k=Cov(A_p^k,s^2/4)/q1,
    partial_q2 U_k=Cov(A_p^k,t^2/4)/q2,
    partial_a U_k=k E[t A_p^(k-1)],
    partial_b U_k=k E[e A_p^(k-1)].                         (18)

Observable weights do not change the zero-field law. For j>=2,

    partial(U_(2j)/v^j)
      =[partial U_(2j)-j U_(2j) partial v/v]/v^j.            (19)

The code evaluates every term of (5), the normalizer, the scores, (18)--(19)
and the matrix product with Y by outward arithmetic. It bounds a row by the
sum of the maximum absolute values of its interval entries. All real-valued
mixed terms are retained. Finite tests separately enumerate individual spins
with disagreeing-edge penalties, a different route from block multiplicities.

### 4.2 The existence proof

For ANY real vector d with ||d||_infinity<=10^-22 define

    G_d(p)=p-Y(F(p)-theta-d).

Its derivative has infinity norm at most beta<1 on B. For p in B,

    ||G_d(p)-p0||_infinity
      <=delta+||Y||_infinity 10^-22+beta R <R/2.

Thus G_d maps the closed box strictly inside itself and is a contraction.
Banach's theorem gives a unique fixed point p_d in B. Since Y is nonsingular,
F(p_d)=theta+d. Conversely every solution in B is a fixed point, so uniqueness
holds in THIS box. Global uniqueness is not claimed. Positivity guards and
(14) ensure that every p_d is an actual connected pair ferromagnet.

For d=0, Y_(p_d) therefore has moments 1,...,10 equal to those of X; the odd
ones vanish by spin flip. Its MGF has only imaginary zeros by the classical
Lee--Yang theorem. No root-finding output was accepted as the equality itself.
The exact root is specified by this unique-box property.

This proves the stronger finite statement that a full four-dimensional box of
nearby standardized moment data is also realizable by the SAME graph and fixed
cross/hub couplings. The certified 10^-22 radius is conservative; optimal
conditioning, largest neighborhood and smallest possible graph are not claimed.

The graph has no hidden unobserved spins or independent bath. Its halo and hub
are both observed and genuinely coupled. It is outside the uniform single-field
attachment architecture addressed in HS3, and uses no density replacement by
higher-body interactions. Ten matching moments still do not identify a law.

## 5. NMT3: local moment steering at EVERY fixed order

This section proves a general finite-dimensional result and then applies it
without claiming that theta's remaining coordinates lie in the resulting open
sets. A local inverse is not a global source-realization theorem.

### 5.1 Exact full-rank directions from small positive observable weights

For an unbiased sign epsilon put c_k=kappa_(2k)(epsilon). Every c_k is nonzero.
A short proof uses

    tanh z=sum_(k>=1) (-1)^(k-1) a_k z^(2k-1),
    a_1=1, (2k-1)a_k=sum_(j=1)^(k-1)a_j a_(k-j)>0.

This follows from (tanh z)'=1-tanh(z)^2 in a neighborhood of zero. Therefore
c_k=(-1)^(k-1)(2k-1)!a_k. No statement about an infinite formal series outside
its disk of convergence is needed.

For ANY bounded symmetric base variable Z independent of r unbiased signs,
let T=Z+sum_(j=1)^r b_j epsilon_j, with distinct b_j>0. Independence gives

    kappa_(2k)(T)=kappa_(2k)(Z)+c_k sum_j b_j^(2k).

The Jacobian of its first r even cumulants with respect to b_1,...,b_r is

    J_(k,j)=2k c_k b_j^(2k-1), 1<=k,j<=r,
    det J=(product_k 2k c_k)(product_j b_j)
                           product_(i<j)(b_j^2-b_i^2) !=0.  (20)

This is ordinary Vandermonde factorization. The conversion from cumulants to
even moments is triangular with diagonal one for symmetric laws. Consequently
both coordinate systems have the same full-rank property. The finite tests
check (20) by rational elimination and a separate formal log-cosh calculation;
the proof above covers every fixed r.

If the base is a finite ferromagnet, connect every added spin by one positive
edge to a fixed base vertex. All moments are analytic in the couplings and
positive weights because the complete finite partition function is positive.
For each FIXED positive distinct b-vector, nonsingularity persists for all
sufficiently small added positive couplings. The graph is now connected when
the base is connected, and remains pair-ferromagnetic. If the base has several
components, additional sufficiently small positive bridges connect them and
the same continuity argument applies.

Taking b_j=t j with t down to zero approximates the base in every fixed moment
and every fixed complex MGF compact; bounded support and complete finite sums
justify this directly. Then choose the connecting couplings sufficiently small.
Thus regular finite-order connected realizations are dense within the class of
finite ferromagnetic moment data. This is not density among all probability
laws. At b_j=t j, determinant (20) is a nonzero constant times t^(r^2). The
neighborhoods may shrink very rapidly; no uniform continuation radius is implied.

### 5.2 Preserve the actual first ten moments during higher-order steering

**NMT3.** For every FIXED integer r>=6 and every desired proximity to the
NMT2 73-spin law on a finite set of moments and complex MGF compacts, there is
a connected (73+r)-spin pair ferromagnet with positive observable weights and
exact theta moments through degree ten, for which the higher moment coordinates
12,14,...,2r can vary independently in a nonempty open neighborhood while those
first ten moments remain EXACT. The neighborhood is centered at the constructed
model's higher moments, not asserted to be centered at the theta values.

Proof. Let p_* be the exact root in NMT2. Its four-by-four standardized moment
Jacobian is nonsingular: (16) makes Y DF(p_*) invertible by a Neumann series,
and Y is nonsingular. Add an observable scale alpha>0 to Y_p. The five controls
(alpha,p) give a nonsingular map to cumulants of orders 2,4,6,8,10 near (1,p_*).
Indeed alpha controls variance alpha^2, while the four standardized moments
are unaffected by alpha; passage to unnormalized moments and then cumulants
is locally invertible. This proves nonsingularity without requiring the exact
root to be represented by a finite decimal.

Add r independent signs with weights b_j. At b=0, the five lower target
cumulants are solved by (alpha,p)=(1,p_*). The implicit-function theorem gives
smooth base controls (alpha(b),p(b)) for all sufficiently small b, making those
five cumulants EXACTLY the theta ones. Choose b_j=t j>0 with t sufficiently
small. At this point the FULL joint map in all controls to the first r cumulants
has rank r, since its leaf-only Jacobian (with base controls held fixed) is the
nonsingular matrix (20). This remains true after the base controls have been
adjusted to the lower target.

The lower-five Jacobian in the base controls remains invertible. Linear algebra
therefore says that the map from the tangent space preserving these five
coordinates onto the other r-5 coordinates is surjective. Explicitly, eliminate
the first five rows using the invertible base block; the remaining block must
have rank r-5 because the whole matrix has rank r. This is a rank statement,
not an estimate that discards physical correlations.

Now give each leaf one positive coupling epsilon to the same core vertex.
For this fixed t and r, apply the implicit-function theorem again to adjust
the five base controls, preserving the five low cumulants. Full rank and the
rank of the low block persist for all sufficiently small epsilon>0 by openness
of nonsingularity. The submersion theorem, or an implicit-function theorem on
a selected nonzero (r-5)-minor, supplies the asserted neighborhood of higher
cumulants on the EXACT lower-moment fiber. Moment conversion is triangular,
so the same holds for higher moments. All couplings remain positive and all
weights remain positive near the chosen point. The graph has 2564+r edges.

Choose t sufficiently small and then epsilon sufficiently small to meet the
given finite moment/MGF proximity. This uses only bounded finite probability
laws at each step, not a limit at growing r. The theorem is proved.

There is no assertion that the theta coordinates 12,...,2r are in this local
neighborhood. No numerical t or epsilon has been certified for any particular
r in this pass. The result cannot be iterated to RH without estimates for target
reachability, parameter boundaries and conditioning. Infinitesimal added leaves
are not a persistent independent bath; the final constructed graph is connected.
This respects, rather than contradicts, the earlier independent-component
obstruction.

## 6. NMT4: the remaining global problem and a checkable continuation plan

The positive result is a regular exact point on the actual low-moment fiber,
plus freely controllable LOCAL higher directions at any fixed finite order.
This gives a concrete route for certified continuation instead of uniformly
attaching a hidden partition function to one visible sum.

For a chosen order r, introduce a finite positive-parameter graph family and
use its full moment/cumulant covariance Jacobian. A chain of parameter boxes
can carry a target-moment path whenever each box has the same kind of strict
inclusion and contraction bounds as (15)--(17), with overlaps binding the path.
The estimates must cover the actual graph law and the whole parameter boxes;
ordinary numerical homotopy points are not a certificate. The graph and the
number of extra parameters may be enlarged between stages. NMT3 supplies local
regular realizations, not a guarantee that such a chain reaches the theta jet.

The still-missing theorem is

    For every r there exists a finite zero-field pair ferromagnet S_r,
    with J_e>=0, nonnegative observable weights and Var(S_r)=1, such that
    |E S_r^(2k)-theta_(2k)|<=1/r for 1<=k<=r.                 OPEN

A whole-law weak-limit realization would be an alternative. No converse from
RH to this possibly smaller Ising realization class is claimed.

For completeness the ending from OPEN has no additional tail gap. For a finite
variance-one pair model, its even entire MGF has exponential type and only
imaginary zeros. The paired Hadamard product gives

    M(h)=product_l(1+h^2/y_l^2), sum_l y_l^-2=1/2.

There is no quadratic exponential for a bounded variable of exponential type;
evenness removes a linear exponential. Coefficientwise comparison with
exp(h^2/2) yields E S^(2k)<=(2k)!/(2^k k!) and |M(h)|<=exp(|h|^2/2).
These are standard Lee--Yang product facts, credited to [E1]. Under OPEN, the
same bounds hold for each target moment by passage to its fixed-order limit.
Then for any fixed R,

 sup_(|h|<=R)|M_(S_r)(h)-M_X(h)|
 <=(cosh R-1)/r+2 exp(R^2/2)(R^2/2)^(r+1)/(r+1)! ->0.         (21)

The theta law has every exponential moment, so its entire Taylor series is
its moment series. Hurwitz on each open half-plane Re h>0 and Re h<0 transfers
zero-freeness; the limit is not identically zero since M_X(0)=1. Equation (3)
then gives RH. This classical conditional closure argument does not prove OPEN.

No new actual zero-free region, all-order source realization, optimum spin
count, high-order continuation campaign, or full RH proof is asserted here.
Ten exact moments and a local extension theorem are not a completed induction.

## 7. Provenance, experiments and review priority

The architecture was found using non-directed NumPy/SciPy/mpmath scouting.
Two-block models produced an eight-moment candidate; adding the nonuniform hub
produced the rational center for ten moments. The scout also evaluated an
unmatched twelfth moment, but that number is not a proved output of this packet.
No scouting value is a target input or an accepting numerical certificate.

The fresh source integrator, complete graph sums and four-dimensional box
inequalities are independently recomputed on every `certify.py --check` call.
The interval primitives are adapted from the earlier seed code, with explicit
source identity in SOURCES.json; normal and optimized replays use the SAME
arithmetic implementation. The separate finite tests use individual spin
configurations rather than binomial compression, formal exponential composition
rather than derivative-polynomial recursion, and formal log-cosh plus elimination
rather than the general Vandermonde proof. This is implementation diversity in
bounded controls, not independent authorship or independent theorem acceptance.

Review (7)--(13), the normalizer and derivative factors in (5),(18),(19), the
strict box predicates and exact rational parameter file, and the distinction
between full-rank local neighborhoods and target-containing neighborhoods in
NMT3. Nothing here asks reviewers to fill the OPEN all-order theorem.

### References and source identities

[E1] C. M. Newman and W. Wu, *Lee--Yang Property and Gaussian Multiplicative
Chaos*, Communications in Mathematical Physics 369 (2019), 153--170,
DOI 10.1007/s00220-019-03453-0. The HTML overview gives the weighted finite Ising
Lee--Yang theorem; Section 3, Theorem 7 and Proposition 13 give the weak-closure
and canonical-product context. Those statements and their local product/closure
arguments were inspected; a new proof of Lee--Yang is not claimed.
https://link.springer.com/article/10.1007/s00220-019-03453-0

[P1] Original FMS proposal and source integrator, PR #842 at
7ff754c7347d6ee9d59608e562e469351b3d37e7, path
standalone/2026-09-10-theta-ferromagnetic-synthesis/.
The `certify_seed.py` blob is 19ff7484e9d82ec16d483c0018e1aedcf1664362.

[P2] Immediate parent, PR #842 at bc561659684f50a6374bcd8d4afb0caf9fb65027,
standalone/2026-09-10-lee-yang-hidden-spin-transfer/PROOF.md,
blob c9707fa6e7db99b8e7f7d7c487cf1f553a75632c. Its full manuscript was read;
the new graph does not inherit its architecture-specific restrictions.

The theta Fourier identity and Jacobi inversion are classical and reconstructed
in the project's exact-theta-pencil packet at
2787339f8f1feb619f1679afb96cb9995e440958. No spectral claim of that packet is
used here. Sources and reading depths are recorded separately from the finite
executions. All component statements remain proposed until independently reviewed.
