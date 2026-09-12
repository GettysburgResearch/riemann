# Collective ferromagnetic theta synthesis

Date: 2026-09-10. Continuation of PR #842.
Status: PROPOSED COMPONENT PROOFS; independent mathematical review required.
**The all-order construction and RH are NOT proved.**

This pass attempts the actual extension of the finite theta-moment seed. It
obtains a connected exact six-moment seed, a constructive reduction of the
all-order search to connected degree-three graphs with one common field weight,
and an arithmetic theorem showing why accumulating independent bounded-size
uniform-field blocks cannot reach the theta law. The latter obstruction would
remain true under RH. None of the results is a proof that the smaller search
class is feasible at unbounded moment order.

General Lee--Yang products, strong-coupling replication, the implicit-function
theorem, and random-cluster expansions are classical. No priority claim is made.
The connection with nonvanishing of zeta on arithmetic progressions is explicitly
source-specific. The published Li--Radziwill theorem is imported, not re-proved.

## 1. Exact source and elementary analytic facts

Use the unchanged source of FMS26, PR #842 at
7ff754c7347d6ee9d59608e562e469351b3d37e7:

    phi(t)=sum_(n>=1) exp(t/2)[4Q_n(t)^2-6Q_n(t)]exp(-Q_n(t)),
    Q_n(t)=pi n^2 exp(2t),
    Xi(z)=xi(1/2+iz)=integral_R phi(t)exp(izt)dt.

Xi uses the entire xi completion, with xi(0)=xi(1)=1/2. The exact Jacobi identity
makes phi even and strictly positive. Set w=phi/Xi(0),

    sigma^2=integral_R t^2 w(t)dt>0,   X=t/sigma,
    M_theta(h)=E exp(hX)=xi(1/2+h/sigma)/xi(1/2).             (1)

All source moments below refer to this variance-one X, not an auxiliary law.
The full theta series has the differentiated n=1 asymptotic

    phi(t)=4pi^2 exp(9t/2-pi exp(2t))(1+O(exp(-2t))), t->+infinity.

Its proof is inherited from the exact source manuscript: isolate n=1, bound the
remaining n>=2 series, and reflect. No spectral theorem or RH premise is used.
In particular

    E exp(b X^2)<infinity for EVERY b>0.                    (2)

For a finite zero-field pair Ising ferromagnet with J_e>=0 and field weights
 a_v>=0, let S=sum a_v sigma_v. The classical multivariate Lee--Yang theorem
implies that E exp(hS) has no zeros off iR. Zero weights follow by continuity.
Its even exponential-type Hadamard product consequently gives, with v=Var(S),

    E S^(2r) <= (2r-1)!! v^r,
    |E exp(hS)| <= exp(v |h|^2/2).                          (3)

For v=0 the variable is zero. For v>0 pair the imaginary roots +/-iy_j:
M_S(h)=product_j(1+h^2/y_j^2), sum_j y_j^-2=v/2. Evenness removes the linear
factor; exponential type excludes a quadratic exponential. Coefficientwise
comparison with exp(vh^2/2) proves (3). The usual locally uniform canonical
product argument retains all multiplicities. This is the parent argument,
reconstructed here to specify precisely the property used below.

A sequence of such symmetric variables with variances <=1 is tight, and its
MGFs are uniformly bounded on every complex compact. Any weakly convergent
subsequence has an entire limiting MGF and convergence on every compact. Indeed
uniform bounds on E exp(2R|S|)<=2exp(2R^2) give uniform integrability, while
Cauchy's formula or a finite-net argument upgrades pointwise convergence to
compact convergence. All fixed moments also converge. Hurwitz retains the
Lee--Yang property since M(0)=1. No assumption about the target's zeros enters
this closure assertion.

The one external arithmetic theorem needed in Section 4 is:

    For every FIXED alpha>0, beta in R,
    (1/T) #{integer ell in [T,2T]:
       zeta(1/2+i(alpha ell+beta)) !=0} >=1/3+o(1).          (4)

This is Li--Radziwill, IMRN 2015(2), 325--354, Theorem 4 in arXiv:1208.2684v1.
It is unconditional, including resonant steps. We use only that a complete
infinite progression of these zeros is impossible. Uniformity in alpha,beta is
NOT asserted or needed: a limiting finite block is fixed before (4) is applied.

## 2. CT1: the exact six-moment seed can be connected

This component uses the parent's computer-assisted FMS3 as an explicit
proposed dependency; that certificate is not newly independently accepted here.
Its definitions and strict inequalities are retained without numerical change.
Let q in I=[11/10,1101/1000], S_8 its K8 magnetization, and c_j(q) its cumulants.
Let L=4096, A=-kappa_4(X), B=kappa_6(X), d=-c_4>0, and

    D=d+2c_2^2/L,
    t_0(q)=[2c_2/L+sqrt(D A-2d/L)]/D,
    gamma(q,t)=1-c_2(q)t.                                 (5)

The parent proves on ALL of I that the radical is positive, t_0>0, gamma>0,
and that the sixth cumulant at q=11/10 lies strictly below B while that at
q=1101/1000 lies strictly above B. It supplies the full native moment integrals,
not guessed target values. In particular gamma is between 0.348620053078 and
0.352043930427 along t_0.

Connect one K8 vertex to the first bath spin, then join the 4096 bath spins in
a path. Give all these 4096 NEW edges the same coupling epsilon>0. Keep the 28
K8 edges at J=(log q)/2. For each q,t near the compact curve t_0(q), use the
positive unnormalized observable

    S(q,t,epsilon)=sqrt(t) sum_(K8) sigma_i
                  +sqrt(gamma(q,t)/L) sum_(bath) sigma_j,

and divide by its exact standard deviation. The resulting variable has variance
one, positive field weights, and a connected graph for epsilon>0.

Every finite-graph moment is real analytic in q,t,epsilon on a neighborhood of
I and this curve, since all partition weights are positive and the scales and
variance are nonzero there. Define

    F(q,t,epsilon)=kappa_4(S/SD(S))+A.

At epsilon=0, Var S=1 IDENTICALLY in t and

    F(q,t,0)=-d t^2-2(1-c_2t)^2/L+A,
    partial_t F(q,t_0(q),0)=-2sqrt(D A-2d/L)<0.             (6)

The derivative is bounded away from zero on the compact interval I. A uniform
implicit-function construction therefore gives epsilon_0>0 and a continuous
function t_epsilon(q) for all q in I and |epsilon|<epsilon_0, solving F=0 and
converging uniformly to t_0. One can justify uniformity by a finite cover of the
compact curve: strict negativity persists in a common tubular neighborhood,
so the locally unique roots agree on overlaps. Shrink epsilon_0 if necessary
to keep all weights and variances positive.

The normalized sixth cumulant along t_epsilon is continuous, uniformly in q.
Its strict endpoint signs at epsilon=0 therefore persist for sufficiently
small epsilon_0. The intermediate-value theorem gives q_epsilon in the OPEN
interval I with sixth cumulant B. Symmetry supplies all odd moments.

**Conclusion.** For every sufficiently small epsilon>0, there is a CONNECTED
4104-spin ferromagnet, with the same 28 K8 couplings and the prescribed 4096
positive connecting edges, whose moments through degree six equal the actual
standardized theta moments exactly. Here the 28 couplings vary together with
q_epsilon; their equality, not their previous numeric value, is preserved.

No numeric value for epsilon_0 or q_epsilon is certified. No extra finite theta
integration is claimed. This is a complete perturbative existence proof from
the parent's strict certified margins, not a numerical connected-model fit.
It matches only six moments and does not by itself solve an eighth-moment or
all-order extension.

## 3. CT2: equal-field, connected, degree-three graphs lose no possible solution

Here the theorem applies to ANY finite weighted zero-field pair ferromagnet,
not just the seed or a theta model. It is a constructive density statement
WITHIN the ferromagnetic class, not universality for arbitrary probability laws.

Let the original graph have n vertices, m positive-coupling edges, degrees d_i,
nonnegative weights a_i, A=sum a_i, and Var(S)=1. Put K=2m+2n. Given delta>0,
choose

    k_i=max(d_i+2,ceil(a_i/delta)),    N=sum_i k_i.           (7)

Replace vertex i by a path of k_i spins. Attach its d_i incident original edges
to DISTINCT path vertices 1,...,d_i, retaining every original coupling J_ij.
Join path neighbors with a coupling L_0>0. All original disconnected components
can be linked in a chain through unused endpoints k_i, with nonnegative bridge
couplings of total strength tau>0. An intermediate component uses at most two
bridges at its chosen endpoint; that vertex has path degree one. Thus the
resulting graph is connected, simple, and has maximum degree THREE. Original
edges consume at most one external degree at any other path vertex. Each
spin has the SAME positive observable weight delta.

The rounded amplitude error and size obey

    0<=delta k_i-a_i<=delta(d_i+2),
    N<=A/delta+K,       sum_i |delta k_i-a_i|<=K delta.       (8)

Let G be the event that every replacement path is internally aligned. Conditioned
on G, the path signs have EXACTLY the original Ising law with the extra bridge
couplings: every internal path contributes the same constant energy, and each
original spin configuration has exactly one aligned clone configuration.

The probability of G^c is controlled without an independence assumption. Write
E_max for the all-plus energy. A bad configuration disagrees on at least one
path edge, losing at least 2L_0 from E_max. No other ferromagnetic edge can exceed
its all-plus contribution. There are at most 2^N configurations and the partition
function is at least 2exp(E_max). Consequently

    Prob(G^c)<=2^(N-1) exp(-2L_0)=:eta.                   (9)

This rough bound suffices; L_0 may grow with N. The bridge change in the aligned
spin law has Radon--Nikodym derivative in [exp(-2tau),exp(2tau)], hence total
variation at most exp(2tau)-1, with TV defined as sup_A |P(A)-Q(A)|.

Both the original and clone observables have modulus <=B_0:=A+Kdelta.
For every integer j>=1 their raw moments satisfy

 |E S_clone^j-E S^j|
 <=j B_0^(j-1) Kdelta+2 B_0^j[eta+exp(2tau)-1].           (10)

For every R>=0, the ENTIRE generating functions satisfy

 sup_(|h|<=R)|M_clone(h)-M_S(h)|
 <=exp(RB_0){R Kdelta+2eta+2[exp(2tau)-1]}.               (11)

To prove (10)--(11), compare S with its rounded observable under the original
spin law, then change the law by the bridges, then charge G^c. The first error
uses the derivative of x^j or exp(hx) on [-B_0,B_0]; the last two use bounded
expectations and total variation. This retains the complete finite spin law,
not only configurations with aligned paths.

Take delta->0, tau->0, and L_0 so that eta->0. The clone variance tends to one.
Dividing by its exact standard deviation preserves the common field weight,
the graph and couplings, and convergence of every fixed moment and every fixed
complex compact. For an explicit finite-error check, if |v_clone-1|<=b<1/2,
then |v_clone^-1/2-1|<=2b and v_clone^-1/2<=sqrt(2). Combining these inequalities
with (10) bounds every normalized moment too. All parameters remain finite at
each requested accuracy.

**Consequence for OPEN-FMS.** The following are equivalent:
(a) the parent all-order approximate theta-moment construction using arbitrary
    finite weighted pair ferromagnets;
(b) a sequence of variance-one COMMON-WEIGHT, CONNECTED pair ferromagnets of
    maximum degree three whose moments converge to all actual theta moments.
The easy direction is inclusion. For the other, apply the finite construction
to each hypothetical model with accuracy tending to zero through the required
moment order; choose the parent models at a higher index if needed to meet any
prescribed final tolerance. Thus no loss occurs in the all-order limiting
criterion. Graph size, coupling strength, degree-reduction cost and field
resolution are NOT bounded uniformly or claimed computationally efficient.

## 4. CT3: the exact theta law has no Gaussian or finite lattice LY factor

### 4.1 A nonzero independent Gaussian component is impossible

If X has distribution G_v+R with independent G_v~N(0,v), v>0, then for every real
y and b>=1/(2v), E exp(b(G_v+y)^2)=infinity. At the endpoint the quadratic term
in the defining Gaussian integral cancels and a constant or nonintegrable
linear exponential remains. Tonelli therefore makes E exp(bX^2)=infinity,
contradicting (2). The remainder need not be symmetric or have moments for this
argument. This is a tail statement, not a claim of full convolution
indecomposability of the theta law.

### 4.2 A finite lattice Lee--Yang component is impossible

Suppose independently X=B+R, where B is a NONDEGENERATE finite lattice law with
an entire Lee--Yang MGF, and R is any probability law. B is bounded, so the
whole-law equality implies that R has every exponential absolute moment:
E exp(c|R|)<=exp(c sup|B|)E exp(c|X|). Thus MGFs factor as ENTIRE functions.
Write, after removing empty extreme sites,

    M_B(h)=exp(b_0 h) P(exp(dh)),    d>0,                  (12)

where P is a nonconstant polynomial with nonzero constant and leading
coefficients. It has a nonzero root u. Lee--Yang implies |u|=1; P(1)>0 implies
u!=1. Writing u=exp(i theta), all

    h_k=i(theta+2pi k)/d, k in Z                         (13)

are zeros of M_B and hence M_theta. Equation (1) would make ALL of

    zeta(1/2+i[(2pi/(d sigma))k+theta/(d sigma)])           (14)

zero, for every sufficiently large positive integer k. The gamma and polynomial
completion factors are finite and nonzero at these points. This contradicts
(4) with the fixed positive step 2pi/(d sigma).

This proves absence of any finite lattice LY convolution divisor. It includes
any nondegenerate finite uniform-field ferromagnetic block, including limits
where some couplings tend to infinity. A finite set with incommensurable field
weights need not be a lattice; no assertion for every finite discrete factor
is made. No linear-independence conjecture about zeta zeros is used.

## 5. CT4: variance must escape every bounded uniform-field component class

Consider a sequence of finite variance-one zero-field pair ferromagnets S_n
converging weakly to the standardized theta law. In this section EACH connected
component has a common nonnegative field weight, allowed to differ between
components and with n. Couplings may be arbitrary finite nonnegative numbers.
For each fixed integer B>=1, put

    v_(n,C)=Var(a_(n,C) sum_(i in C) sigma_i),
    V_(n,B)=sum_(C:|C|<=B) v_(n,C).

Then necessarily

    V_(n,B) -> 0  for EVERY FIXED B.                      (15)

Connected components are independent because the zero-field Gibbs weight and
partition function factor. We give both possible failure mechanisms.

### 5.1 A quantitative infinitesimal-cloud bound

For independent symmetric LY variables Y_j with variances v_j and total V<=1,
Taylor's remainder and (3) give

 |E exp(itY_j)-(1-v_jt^2/2)|<=v_j^2 t^4/8,
 |exp(-v_jt^2/2)-(1-v_jt^2/2)|<=v_j^2 t^4/8.

Each characteristic function and each Gaussian comparison factor has modulus
at most one. Telescoping their products therefore proves

 |E exp(it sum_j Y_j)-exp(-Vt^2/2)|
     <=(t^4/4)sum_j v_j^2 <=(t^4/4)V max_j v_j.           (16)

No limiting central-limit theorem is imported. If a subcloud has maximum
variance tending to zero and total variance tending to v>0, (16) proves a
Gaussian weak limit N(0,v). Its independent complement is tight, since its
variance is <=1. Along a convergent subsequence the complete law would have a
nonzero Gaussian factor, contradicting Section 4.1. Thus every such
infinitesimal independent subcloud has total variance tending to zero in a
successful construction. This assertion itself permits arbitrary component
weights; the equal-field hypothesis is only needed in the next alternative.

### 5.2 A persistent small block has a forbidden lattice limit

If (15) fails, take a subsequence with V_(n,B)>=delta>0. If the largest small
block variance has a subsequence tending to zero, Section 5.1 is already a
contradiction after taking a further subsequence of V_(n,B). Otherwise select
one small component of variance >=epsilon>0 at every index. Pass to a further
subsequence with its vertex count b<=B fixed.

Both all-plus and all-minus configurations maximize every ferromagnetic edge.
Each consequently has probability >=2^-b. If a is the common field weight,
spin-flip symmetry and Var block<=1 give

    epsilon <= Var block <=b^2 a^2,
    Var block >=2^(1-b)b^2 a^2,
    sqrt(epsilon)/b <= a <=2^((b-1)/2)/b.                 (17)

Take a convergent subsequence of a and all 2^b configuration probabilities.
The limit has bounded support in a nonzero fixed lattice and retains both
extreme probabilities, so it is nondegenerate. Its MGFs converge on compacts;
Hurwitz retains Lee--Yang. The independent complement has variance <=1 and
is tight, so a further limit expresses the theta law as this block plus an
independent remainder. Section 4.2 is a contradiction. This exhausts the cases
and proves (15), without needing eigenvalue data or actual zero locations.

Consequences and important boundaries:

* No family assembled from independent common-weight components of uniformly
  bounded size can match the theta moments to all orders. Arbitrary numbers of
  copies, arbitrary nonnegative couplings and varying positive scales are allowed.
* The parent's K8-plus-independent-spin design remains a VALID six-moment seed.
  Repeating such independent bounded blocks is not a valid all-order induction.
* For each fixed B there is some finite r_B for which accuracy <=1/r_B through
  moments 2,...,2r_B is impossible in the variance-one bounded-component class.
  Otherwise selecting a model at every r and using (3) gives the forbidden
  weak limit. Neither r_B nor a separating moment inequality is computed here.
* The conclusion does not require or assert a single dominant connected
  component. Many components with growing sizes are permitted. It does not
  rule out the general FMS programme, incommensurate fixed blocks, or RH.

The quantitative cutoff in (4) may depend badly on the limiting lattice.
No uniform progression theorem or effective r_B is inferred.

### 5.3 Vanishing total bridge strength cannot disguise bounded components

More generally suppose deleting some edges of total coupling tau_n->0 leaves
components of size <=B and a common field weight within each remaining
component. The original and cut Gibbs densities differ by a ratio in
[exp(-2tau_n),exp(2tau_n)], hence TV tends to zero. Their second moments compare
by the same ratios, so the cut variance tends to one. Standardizing it gives a
variance-one cut model converging to the same theta law, contrary to (15).
Thus connecting fixed-size modules by edges with VANISHING TOTAL coupling
cannot rescue the construction. A small maximum edge, bounded degree, or small
coupling per vertex is a different condition and is not excluded by this result.
In particular the strong-coupling degree-three reduction in Section 3 is not
contradicted: its replacement modules grow and its wire strengths do not vanish.

## 6. CT5: a growing independent bath must lose its variance quantitatively

The source tail also yields the all-order moment asymptotic

    (E |X|^p)^(1/p) ~ log p/(2sigma), p->infinity.         (18)

Here is a direct proof, included instead of a numerical extrapolation. Put
b=2sigma. The density f_X has log f_X(x)=-pi exp(bx)+O(x) at +infinity and is
even. For each fixed 0<epsilon<1, integrate over the unit interval beginning
at (1-epsilon)log p/b. Its mass is exp(-O(p^(1-epsilon))-O(log p))=exp(-o(p)),
and its minimum x^p supplies the lower moment bound. For the upper bound take
r=(1+epsilon)log p/b. The part |X|<=r contributes at most r^p. On x>=r,
f_X(x)<=C exp(-c exp(bx)), for fixed C,c>0, and
x^p exp(-(c/2)exp(bx)) is decreasing for sufficiently large p: its logarithmic
derivative is p/x-(cb/2)exp(bx)<0 at r and only decreases thereafter. The
remaining integrable factor exp(-(c/2)exp(bx)) bounds the complete tail by
C' r^p exp(-(c/2)p^(1+epsilon)). Taking pth roots, then epsilon down to zero,
proves (18). Every limit is in the actual source variable; no RH input is used.

Suppose a variance-one model is a sum of an independent symmetric remainder
and an unbiased sign bath

    B_r=sqrt(gamma_r/L_r) sum_(j=1)^(L_r) epsilon_j.

For integers 1<=r<=L_r, the contributions in which r distinct signs each appear
exactly twice in the 2rth power give

    E B_r^(2r) >= (2r-1)!! gamma_r^r (L_r)_r/L_r^r.        (19)

All other even contributions and the symmetric-remainder contributions are
nonnegative. If the whole model matches the target 2rth moment with error
<=delta_r, then

 gamma_r <= [(m_(2r)+delta_r)/((2r-1)!! ((L_r)_r/L_r^r))]^(1/r). (20)

If L_r>=r(r-1), r>=2, the product is >=1/2, by
product_(j=0)^(r-1)(1-j/L_r)>=1-r(r-1)/(2L_r). Taking delta_r<=1/r,
using (18) and log((2r-1)!!)=r log(2r)-r+O(log r), gives

    gamma_r <= [e/(8sigma^2)+o(1)] (log(2r))^2/r ->0.     (21)

The factorial estimate follows by bounding sums of logarithms by integrals.
Thus keeping the seed's approximately 0.35 variance in an increasingly fine
independent bath is incompatible with all-order matching. No numeric first
failing moment is claimed; finite bath sizes not meeting L_r>=r(r-1) remain
covered by (20), and a persistent fixed bath is excluded by Section 4.2.

## 7. Exact interacting coordinates: random-cluster moments

This section describes the genuinely coupled finite source to which an
all-order construction must apply, rather than replacing it by independent
moment fits. It is the standard Edwards--Sokal expansion, derived here.
For r_e=exp(-2J_e), expand

    exp(J_e sigma_i sigma_j)
      =exp(J_e)[r_e+(1-r_e)1_(sigma_i=sigma_j)].

For an open-edge set omega, summing spins gives the weight

    W(omega)=2^(k(omega)) product_(open e)(1-r_e)
                             product_(closed e)r_e.       (22)

Conditioned on omega, each connected open cluster has an independent unbiased
sign. Its observable amplitude is A_C=sum_(i in C)a_i. Therefore EXACTLY

    M_G(h)=E_RC product_C cosh(A_C h).                     (23)

This is a particular random-cluster mixture generated by positive pair edges;
arbitrary mixtures of Lee--Yang measures are NOT being declared Lee--Yang.
Put V=sum A_C^2, W=sum A_C^4 and U=sum A_C^6. Coefficient extraction gives

    E S^2=E_RC V,
    kappa_4(S)=3 Var_RC(V)-2 E_RC W,
    kappa_6(S)=15 kappa_3_RC(V)-30 Cov_RC(V,W)+16 E_RC U.   (24)

The third cumulant of V and the covariance in (24) cannot be dropped or signed
without proof. The finite theta targets 1,-A,B constrain all these interacting
terms. For arbitrary order 2j, the exact equation is

    (2j)! [h^(2j)] E_RC product_C cosh(A_C h)=m_(2j).       (25)

A connected equal-field degree-three model has A_C=a|C|, so (25) involves an
ordinary random-cluster distribution of integer cluster sizes with ONE field
scale. There is no temperature/field substitution or altered theta law.

## 8. The attempted end-to-end completion and its still-unproved line

Section 3 permits the following precise sufficient target, equivalent to the
parent's finite-ferromagnet moment approximation problem:

    For every r there is a finite connected graph of maximum degree three,
    with nonnegative pair couplings and ONE common positive field weight,
    whose standardized magnetization has errors <=1/r in the actual theta
    moments of degrees 2,4,...,2r.                          OPEN-COLLECTIVE

This pass proves no all-r version of (25) or OPEN-COLLECTIVE. Section 2 gives
only a connected sixth-order starting point. Section 5 shows why the simplest
independent-block continuation is unavailable, rather than providing the
needed interacting construction by contradiction.

For completeness the full conditional ending has no additional infinite-tail
premise. Were OPEN-COLLECTIVE true, (3) would imply Gaussian bounds for each
fixed target moment by passage to the limit. For each R<infinity the MGFs obey

 sup_(|h|<=R)|M_r(h)-M_theta(h)|
 <=(cosh R-1)/r+2 exp(R^2/2)(R^2/2)^(r+1)/(r+1)! ->0.     (26)

Both models and target are even, and their MGFs are entire. Every M_r is
zero-free on Re h>0 and Re h<0 by Lee--Yang. Hurwitz and M_theta(0)=1 transfer
both nonvanishing statements. Equation (1) would exclude every off-critical
nontrivial zeta zero and prove RH, without assuming simplicity.

The missing assertion is the existence of these graphs with the source-specific
all-order cluster moments, not Lee--Yang, compactness, graph connectedness,
field homogenization, a negligible bath, or the limit theorem. We do not
relabel (26) as an unconditional RH proof. The new necessary conditions are
compatible with an as-yet-unknown successful interacting construction.

## References and inherited scopes

[P] PR #842 at 7ff754c7347d6ee9d59608e562e469351b3d37e7,
standalone/2026-09-10-theta-ferromagnetic-synthesis/PROPOSAL.md.
Full supplied manuscript read and authenticated to its Git blob. FMS3's exact
native seed and interval margins are inherited proposed results; its defining
integral code is NOT rerun or independently reimplemented here.

[LY] C. M. Newman and W. Wu, Lee--Yang Property and Gaussian Multiplicative
Chaos, Commun. Math. Phys. 369 (2019), 153--170; arXiv:1708.08820v3.
https://arxiv.org/abs/1708.08820
The classical weighted Ising theorem, canonical-product statement and closure
were inspected. Their full external proofs are imported, not claimed newly
verified. This manuscript supplies its needed elementary domination and limit
arguments. The source-dependent moment construction is not an external theorem.

[LR] X. Li and M. Radziwill, The Riemann Zeta Function on Vertical Arithmetic
Progressions, IMRN 2015(2), 325--354, DOI 10.1093/imrn/rnt197;
arXiv:1208.2684v1, Theorem 4, PDF page 3 (zero-index page 2).
https://arxiv.org/abs/1208.2684
The definitions and theorem statement were read; the complete mollifier proof
was not independently audited. The weaker no-full-progression consequence
also has classical antecedents, including Putnam. No new zero-density or
arithmetic-progression theorem is claimed.

[RC] R. G. Edwards and A. D. Sokal, Generalization of the Fortuin--Kasteleyn--
Swendsen--Wang representation and Monte Carlo algorithm, Phys. Rev. D 38 (1988),
2009--2012. Only the finite expansion, fully derived in (22)--(24), is used.

The infinite mathematical arguments remain paper proofs awaiting independent
review. Finite checks do not establish the external theorem or the all-order
theta feasibility. No new numerical zero, theta-moment certificate, RH proposal
with its central estimate silently assumed, or independent acceptance is claimed.
