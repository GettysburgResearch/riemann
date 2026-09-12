# Exact auxiliary-spin synthesis: a positive lifting theorem and a source-specific boundary

Date: 2026-09-10. Continuation of GettysburgResearch/riemann PR #842.
Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
**The requested all-order Lee--Yang-compatible realization of the theta law
has NOT been proved. Neither RH nor its negation is established.**

This pass tests a concrete attempted completion, rather than assigning the
pair-replacement step to reviewers. A finite hidden ferromagnet can be lifted
into a completely specified pair-Ising construction whose limiting density is
`exp(-a*x^4-b*x^2) M_B(x)`, including its whole normalization and all tails.
But even the weak closure of this whole class does not contain the actual theta
law. Separately, uniform attachment of arbitrarily many interacting hidden
spins cannot replace the parent's entropy construction: an exact three-level
inequality gives a diverging log-weight error on its actual theta approximants.
These are restrictions on stated architectures, NOT on all pair ferromagnets.
A connected four-spin pair model explicitly violates the architecture-specific
inequality, identifying why the restriction must not be overgeneralized.

The Lee--Yang theorem, its canonical-product consequence, Curie--Weiss critical
scaling and log-concave compactness are classical mechanisms. No external
novelty or priority claim is made. All the needed deductions are supplied below.
Local labels HS1--HS5 are not canonical acceptance identifiers.

## 1. Source and classical input

Use the parent's unchanged full-line source:

    Xi(z)=xi(1/2+i*z)=integral_R phi(t) exp(i*z*t) dt,
    phi(t)=sum_(n>=1) exp(t/2) (4q_n^2-6q_n) exp(-q_n),
    q_n=pi*n^2*exp(2t),
    Z=Xi(0)>0, w=phi/Z.                                      (1)

The completion is entire, with xi(0)=xi(1)=1/2. Jacobi inversion makes phi
 even and positive; the displayed summands are individually positive on t>=0.
Let U have density w. Its MGF is

    M_U(h)=xi(1/2+h)/xi(1/2).                                 (2)

The standardized target is U/SD(U), not a different arithmetic source. Positive
rescaling does not affect any exclusion below. The inherited source series
and its derivatives give

    V(t):=-log w(t)
        =pi*exp(2t)-(9/2)t+C+O(exp(-2t)),  t->+infinity,      (3)

with the same type of bound after each of the first three t derivatives.
Indeed the n=1 term equals
`4*pi^2*exp(9t/2-pi*exp(2t))*(1-3*exp(-2t)/(2*pi))`, and all n>=2 terms and
their fixed derivatives have an exponentially smaller relative error. Local
positive lower bounds permit taking the logarithm. We do not use RH to obtain
(1)--(3).

The only zero-location input is the classical finite zero-field PAIR-Ising
Lee--Yang theorem [E1]: if B is a finite graph with couplings J_ab>=0 and
T=sum b_a*tau_a with b_a>=0, then its normalized MGF M_B(h) has no zeros with
Re(h)!=0. Auxiliary spins of zero observable weight are allowed: use positive
weights tending to zero and Hurwitz, with the nonzero real-positive values
excluding an identically zero limit. Spin flip makes M_B even.

Because T is bounded, M_B is entire of exponential type. Hadamard factorization,
paired at its imaginary zeros, gives

    M_B(h)=product_l (1+h^2/y_l^2),
    y_l>0, sum_l y_l^(-2)=Var(T)/2<infinity.                 (4)

Zeros are listed with multiplicity. The even entire exponential prefactor is
one; a nonzero quadratic exponential is excluded by exponential type. If T=0,
use the empty product. These are classical product facts, not a newly proved
Lee--Yang theorem. Formula (4) also follows from [E1, Proposition 13], noting
that its Gaussian prefactor vanishes for bounded T.

## 2. HS1: a complete pair-compatible lifting theorem

Fix ANY finite hidden zero-field pair ferromagnet B, its nonnegative weights
b_a, and hence M_B. Fix a>0 and b in R. Then the density

    rho_(a,b,B)(x)=C_(a,b,B)^(-1) exp(-a*x^4-b*x^2) M_B(x)  (5)

is a weak limit of explicit finite zero-field pair ferromagnets with
nonnegative couplings and nonnegative observable weights. Every moment and
every complex-compact MGF converge. Consequently (5) is Lee--Yang-compatible.
The normalizer is finite: M_B(x)<=exp(A*|x|), A=sum b_a.

### 2.1 The actual finite graphs

Let N visible spins be sigma_1,...,sigma_N, put S=sum sigma_i, and

    c=(12a)^(-1/4), X_N=c*S/N^(3/4).

Keep every hidden coupling. Give EVERY visible pair the coupling

    j_N=1/N-2*b*c^2/N^(3/2),                              (6)

which is nonnegative for all sufficiently large N. Couple visible i to hidden
a with coupling `c*b_a/N^(3/4)`, also nonnegative. The observable is X_N;
all hidden observable weights are zero. This is a finite ordinary pair model,
not a model in which aligned hidden configurations are selected by hand.

After dropping the configuration-independent visible constant and summing
ALL hidden configurations, the exact unnormalized visible level weight is

    binom(N,k) exp[S^2/(2N)-b*c^2*S^2/N^(3/2)] M_B(x),
    S=2k-N, x=c*S/N^(3/4).                                (7)

No MGF factor was assumed to be a probability mixture; it is obtained by the
literal finite hidden partition sum. The original graph can be disconnected;
HS1 does not require or claim a connected finite realization in every case.

### 2.2 Whole-law convergence

Use the Bernoulli entropy

    I(m)=sum_(r>=1) m^(2r)/[2r(2r-1)], |m|<=1.

For fixed |x|<=R, with m=x/(c*N^(1/4)),

    N*(I(m)-m^2/2)=x^4/(12c^4)+O_(c,R)(N^(-1/2))
                 =a*x^4+O_(c,R)(N^(-1/2)).                (8)

Stirling's formula, including its remainder, gives locally uniformly the
prefactor `(1-m^2)^(-1/2)*(1+O(1/N))` after multiplication by
`sqrt(pi*N/2)*2^(-N)`. The x lattice has spacing `2c/N^(3/4)`; its parity
shift is retained. Equations (7)--(8) therefore converge as Riemann sums to
`exp(-a*x^4-b*x^2) M_B(x)` on each fixed compact.

For |m|<=1/2 the same scaled binomial prefactor is bounded by 2 for all large N,
and I(m)-m^2/2>=m^4/12. Thus the whole central-region summand, even after a
complex exponential test |h|<=R, is bounded by

    2 exp(-a*x^4+|b|*x^2+(A+R)|x|).                       (9)

This is an integrable, eventually decreasing majorant on both tails. Grid
sums on each remote monotone tail are bounded by its integral and one endpoint
rectangle. For |m|>1/2, the entropy penalty is at least N/192. All positive
remaining exponent terms are at most `|b|*c^2*sqrt(N)+(A+R)*c*N^(1/4)`.
The entire outer contribution, including k=0,N, is consequently bounded by

    (2c/N^(3/4))*(N+1)*sqrt(pi*N/2)
    * exp[-N/192+|b|*c^2*sqrt(N)+(A+R)*c*N^(1/4)] ->0.     (10)

The elementary entropy binomial upper bound is valid also at the two extreme
levels, where the interior Stirling formula is not used. Monomials are handled
by the same domination with a fixed polynomial factor. Taking ratios with the
strictly positive limiting normalizer proves every assertion of HS1.

Each finite graph has the Lee--Yang property. The proved local uniform limit
and value one at zero transfer it by Hurwitz. More specifically, the finite
product (4) implies `E X_N^4<=3 Var(X_N)^2` and
`|M_N(h)|<=exp(Var(X_N)*|h|^2/2)`. Variances converge by the just-proved moment
passage, so both inequalities hold for (5) with its own variance.

HS1 is a constructive positive theorem, but it is NOT a realization of theta.
The failure of that proposed identification is proved next.

## 3. HS2: the whole weak closure of this hidden-weighted quartic class misses theta

Let C consist of all densities (5), with arbitrary a>0, arbitrary real b,
and ANY finite hidden pair ferromagnet and nonnegative hidden weights. The
number of hidden spins, their graph and their couplings may change without
bound along a sequence. The following statement is unconditional:

    Neither the theta law w(t)dt nor its standardized version belongs
    to the weak closure of C.                              (11)

This does not say that theta lies outside the closure of ALL pair-Ising
magnetizations. C is a particular one-collective-visible-variable construction.

### 3.1 The invariant in the squared coordinate

For a member rho of C, put `g(u)=-log rho(sqrt(u))`, u>0. From (4),

    g(u)=a*u^2+b*u-log M_B(sqrt(u))+constant,
    g''(u)=2a+sum_l (u+y_l^2)^(-2)>0,
    g'''(u)=-2 sum_l (u+y_l^2)^(-3)<=0.                    (12)

Termwise differentiation is justified uniformly on compact positive u
intervals by `sum y_l^(-2)<infinity`. The useful conclusion is not the sign of
one low cumulant: g is convex and its third FORWARD differences satisfy

    g(u+3h)-3g(u+2h)+3g(u+h)-g(u)<=0,
    u>0, h>0.                                             (13)

The positive quadratic and linear terms vanish from (13). Thus the constraint
survives arbitrary changes of a,b and of the hidden graph.

### 3.2 Weak convergence is strong enough here

We supply the compactness step instead of assuming convergence of densities
or derivatives. Suppose X_n from C converge weakly to the theta variable U.
Write v_n=Var(X_n). HS1 gives `E X_n^4<=3 v_n^2`. Paley--Zygmund, or its direct
Cauchy--Schwarz proof applied to X_n^2, gives

    Prob(|X_n|>=sqrt(v_n/2))>=1/12.                         (14)

Tightness forces sup_n v_n<infinity; otherwise the lower bound in (14) occurs
outside every fixed compact along a subsequence. Finite initial n do not affect
this conclusion. The same HS1 Gaussian MGF bound then gives uniform bounds
on every absolute exponential moment. In particular `E|X_n|->E|U|>0` and the
first moments are uniformly integrable.

Define probability densities on (0,infinity) by

    f_n(u)=rho_n(sqrt(u))/E|X_n|.                          (15)

Their total mass is one because `du=2x dx` and rho_n is symmetric. Equivalently,
for bounded continuous a(u),

    integral a(u) f_n(u) du
       =E[|X_n| a(X_n^2)]/E|X_n|.

Truncation, weak convergence and uniform integrability show that f_n converge
weakly to `f(u)=w(sqrt(u))/E|U|`, a continuous strictly positive density on
(0,infinity). By (12), every log f_n is concave.

Here is the elementary local compactness fact needed. On a compact interval
inside (0,infinity), choose small intervals strictly to its left and right.
Their limiting positive masses give points on both sides where f_n>=c>0.
Concavity supplies a uniform positive lower bound between these points. An
upper spike of height H on a smaller intervening compact, together with a
separated point of height at least c, would contribute at least
`delta*sqrt(c*H)/2` mass on the half-segment closest to that spike. Since total
mass is one, H is uniformly bounded. On a slightly larger compact we now have
both upper and lower bounds for log f_n. Concavity bounds its slopes uniformly
on the original compact by the external secants. Arzela--Ascoli and uniqueness
of the weak limit therefore give

    log f_n -> log f locally uniformly on (0,infinity).    (16)

This proof uses no convergence of derivatives. Constants in (15) disappear
from (13), so (16) passes (13) to `G(u)=-log w(sqrt(u))`.
Since G is smooth, division by h^3 followed by h down to zero implies

    G'''(u)<=0 for every u>0.                              (17)

### 3.3 The actual source has the opposite eventual sign

Set t=sqrt(u). Applying `(2t)^(-1)d/dt` three times to (3) gives

    G'''(u)= pi*exp(2t)*(4t^2-6t+3)/(4t^5)
              -27/(16t^5)+O(exp(-2t)/t^3), t->infinity.   (18)

The polynomial `4t^2-6t+3` is strictly positive (its discriminant is -12).
The leading term dominates, so G'''(u)>0 for every sufficiently large u.
This contradicts (17) and proves (11). Differentiated errors in (18) were paid
by the differentiated theta series in (3), not by differentiating an arbitrary
undifferentiated O-term.

Positive scaling preserves C: it rescales a,b and the nonnegative hidden
weights. Thus standardization cannot evade (11). No finite numerical theta
sample, known zeta zero, or hypothesis about unknown zeros is used.

## 4. HS3: uniform auxiliary attachment obeys an exact finite three-level test

The following finite statement targets the parent's proposed all-level pair
replacement BEFORE taking any limit. There are N visible spins sigma_i and an
arbitrary finite interacting hidden ferromagnet B with spins tau_a. Assume

    H(sigma,tau)=J sum_(i<j) sigma_i sigma_j
       +sum_(a<b) A_ab tau_a tau_b
       +(sum_i sigma_i)(sum_a b_a tau_a),
    J,A_ab,b_a>=0.                                        (19)

Every visible spin couples to hidden a with the same b_a. All visible-visible
couplings have the same J. Hidden couplings can be completely inhomogeneous;
there is no limit on their number or magnitude. All single-site fields are
zero, and the hidden spins have zero observable weight.

Let Q(S) be the FULL restricted partition sum at visible magnetization S.
Exact summation gives

    R(S):=Q(S)/binom(N,(N+S)/2)
         =exp[J*(S^2-N)/2] Z_B(0) M_B(S).                (20)

Suppose N is even and 0,s,2s are permitted visible levels. Formula (4), or
concavity of `log M_B(sqrt(u))`, gives

    R(2s) R(0)^3 <= R(s)^4.                               (21)

For each product factor this is exactly
`1+4t <= (1+t)^4`, t=s^2/y_l^2>=0. The visible pair energy and both constants
cancel. All hidden configurations are included in (20). Arbitrarily strong
hidden couplings, including limits obtained after each finite inequality,
cannot reverse (21).

## 5. HS4: a diverging error on the ACTUAL entropy approximants

Use the parent's notation for a fixed even confining polynomial of degree 2d:

    N=L^(2d+1), X=S/L^(2d),
    H_(P,L)(S)=N I_d(S/N)-P(S/L^(2d)),
    I_d(m)=sum_(r=1)^d m^(2r)/[2r(2r-1)].                 (22)

Take even L>=4, and impose the parent's additional coefficient threshold when
claiming its nonnegative many-spin couplings. The following contrast also holds
algebraically without that extra threshold. Then 0, L^(2d), 2L^(2d) are actual
permitted levels. Put

    D_P=P(2)-4P(1)+3P(0).

At these THREE levels the log-weight contrast is EXACTLY

    Delta H=sum_(r=2)^d
        [(2^(2r)-4)/(2r(2r-1))] L^(2d+1-2r) -D_P.

For d>=2 the quartic term alone gives

    Delta H>=L^(2d-3)-D_P.                                (23)

Suppose the uniform-hidden pair graph (19) achieves the parent's required
multiplicative comparison, up to a single common normalization exp(b), with
log error at most epsilon at every visible level. The binomial factors in (20)
and (22) cancel. The coefficients of Delta are 1,-4,3, whose absolute sum is 8
and whose sum is zero. Thus (21)--(23) imply

    epsilon >= max(0,L^(2d-3)-D_P)/8.                     (24)

This is a lower bound on error, not a missing estimate to be supplied by a
reviewer. It already uses three allowed levels, not a small-probability deletion.

### 5.1 Uniform control for the actual theta polynomial sequence

The parent constructs rational even P_j with

    P_j(t)>=t^2 on R,
    |P_j(t)-(7-log phi(t))|<=2^(-j), |t|<=j.              (25)

We show, without computing any large P_j, that for j>=4 its degree is at least
four and D_(P_j)<1328. Consequently, for ANY even L>=4,

    epsilon >= max(0,L-1328)/8                            (26)

whenever (19) attempts the specified replacement for P_j and its degree.
In particular the permissible diagonal choice L_j>=j, L_j even, cannot have
vanishing comparison error through this architecture. This strengthens the
choice of cutoffs within the parent's allowed construction; it does not
rewrite a previously fixed numerical sequence.

Here are the coarse source estimates paying both assertions. The parent proves
phi(t)<256*exp(-t^2) and, on 0<=t<=2,

    phi(t)>=18 exp(-4 exp(2t))>18 exp(-324).

Thus `0<=P_j(t)<332` at t=0,1,2 for j>=2, giving `|D_(P_j)|<1328`.
To exclude degree two, put W=7-log phi. We claim

    W(2)-4W(1)+3W(0)>3/4.                                (27)

Indeed e^2 is between 7 and 9, and pi is between 3 and 4. At t=1 the n=1 term
has 21<q<36 and `4q^2-6q>1638>2^10`, so phi(1)>2^10 exp(-36).
At t=2 its first q is greater than 147. For q>=3,
`sum_(n>=1) n^4 exp[-q(n^2-1)]<2`: the n=2 term is below 1/32 and subsequent
ratios are below 1/2. Since q^2 exp(-q) decreases for q>=2,

    phi(2)<24*147^2*exp(-147)<2^19*exp(-147).

Also phi(0)<2^8. It follows that

    phi(1)^4/[phi(2)*phi(0)^3]>exp(3)/8,

whose logarithm is `3-3log2>3/4`. This proves (27). All inequalities used for e
follow from its series (e>8/3, e<3, exp(3/4)>2); no directed zeta evaluation is
involved. By (25) the error in the contrast is at most `8*2^(-j)<=1/2`.
Therefore D_(P_j)>1/4 for j>=4. An even polynomial of degree at most two has
D_P=0, so these P_j have d_j>=2, proving (26).

### 5.2 General graphs must pay a quantitative departure from uniform attachment

This is a NECESSARY cost, not an impossibility theorem for general graphs.
For a general nonnegative pair graph on the same visible/hidden vertices,
let J_ij be visible couplings and B_ia the cross couplings. Define their means
`Jbar` over visible pairs and `bbar_a=(1/N)sum_i B_ia`, and put

    tau=sum_(i<j)|J_ij-Jbar|+sum_(i,a)|B_ia-bbar_a|.       (28)

Keep hidden-hidden couplings unchanged. Replacing the indicated couplings by
their nonnegative means gives a graph (19). For EVERY full spin configuration,
the two exponents differ by at most tau. Summing positive terms at any fixed
level proves `exp(-tau) Q_0(S)<=Q(S)<=exp(tau) Q_0(S)`.
Hence a general graph satisfying the parent's error-epsilon comparison must obey

    tau+epsilon >= max(0,L^(2d-3)-D_P)/8.                 (29)

For the actual approximants the right side is at least max(0,L-1328)/8.
This quantifies one architectural requirement; dense or strongly inhomogeneous
graphs can certainly have large tau. It does not imply failure of all pair
realizations, weak approximations using a different visible scale, or RH.

## 6. HS5: a literal connected pair graph escapes the three-level inequality

One must not extend (21) to all ferromagnets. On four visible spins take edges
(1,2),(3,4) with exp(2J)=2, and the connecting edge (2,3) with exp(2J)=101/100.
The graph is a CONNECTED path, all three couplings are positive, all observable
weights are equal, and no hidden spins are present.

Use the equivalent positive configuration weight which contributes r_e if an
edge is aligned and 1 otherwise. Complete enumeration gives, after division
by the visible binomial multiplicities,

    R(0)=601/300, R(2)=201/100, R(4)=101/25.

Therefore

    R(4) R(0)^3/R(2)^4 =87701047604/44070501627 >199/100>1. (30)

(The strict comparison with 199/100 is a rational arithmetic statement.)
This model is nevertheless Lee--Yang by the ordinary pair theorem. It exhibits
a concrete way nonuniform connections can change the effective level curvature.
It is NOT a theta model, an all-order extension, or an indication that a fixed
path family suffices. The previous no-independent-bounded-block theorem remains
unchanged. A uniform effective-field substitution would erase precisely the
structure visible in (30).

## 7. End-to-end status and the next construction that is actually required

HS1 supplies an unconditional all-order pair-compatible realization for a
precise nontrivial family. HS2 proves that even its weak closure cannot reach
theta. HS3--HS4 show that the uniform-hidden implementation of the parent's
specific all-level contract fails directly on the actual source approximants,
with quantitative error, while HS5 proves that this test is not a universal
condition on pair Ising magnetizations.

No general pair graph approximating theta has been constructed here. The
parent's sufficient contract remains OPEN for nonuniform graphs; the simpler
weak-limit version also remains OPEN. If finite pair-ferromagnetic
magnetizations converged weakly to the actual theta law, the classical
Lee--Yang weak-closure theorem [E1, Theorem 7] would give the zero-free half-planes
of (2), and hence RH. This conclusion cannot be used to assert graph existence.
The previously proved conditional moment/Hurwitz route remains valid as well.

A possible continuation must work with genuinely nonuniform collective
interactions and retain their complete restricted partition sums. Averaging
couplings, silently replacing many-body interactions by a uniform hidden field,
or passing only the quartic visible block to a limit is not a completion.
There is no full unconditional RH proof in this manuscript.

## References and review priorities

[P] Exact parent: c79c2f6c59640e5f5ef6e22b2ff745d3a8f5a0ff,
standalone/2026-09-10-theta-entropy-reconstruction/PROOF.md. Whole manuscript read
and local bytes authenticated. (1), the polynomial approximation (25), and the
specified entropy contract are the only prior mathematical construction inputs.
No old seed producer or numerical campaign was rerun or newly accepted.

[E1] C. M. Newman and W. Wu, Lee--Yang Property and Gaussian Multiplicative
Chaos, Communications in Mathematical Physics 369 (2019), 153--170,
https://doi.org/10.1007/s00220-019-03453-0 . Primary publisher HTML was read,
especially the finite pair-Ising statement in Section 1 and Theorem 7 / Proposition
13 in Section 3. Classical Lee--Yang is imported, not machine-proved here.

The quartic scaling mechanism is credited to the classical Griffiths--Simon
construction. HS1 gives the particular finite graph and a complete proof rather
than relying on an unstated universality assertion. Elementary Hadamard,
Stirling, dominated convergence, Paley--Zygmund and convex compactness are used
at the scopes proved above. No broad external novelty audit is claimed.

For review: check the positive sign and finite-N size of (6); preserve all outer
spin levels in (10); distinguish normalized densities from their square-coordinate
reweighting (15); retain tightness in the passage to (16); check all theta-tail
derivatives in (18); and keep the UNIFORM attachment hypothesis in (19).
The final open construction must not be accepted by verifying only these lemmas.
