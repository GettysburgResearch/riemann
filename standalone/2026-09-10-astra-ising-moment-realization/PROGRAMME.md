# Constructive programme and actual stopping point

Status: exploratory research direction with proposed supporting theorems.
**The all-order realization (IR) is open. This is not a complete RH proof.**

## A. The change of architecture

The arithmetic-feedback family now has complete causal admissibility but lacks
a small full-energy upper bound. The whole-theta determinant has an exact
characteristic identity but lacks spectral reality. Both are valuable, but this
pass does not improve either missing estimate by changing its name.

The alternative is to manufacture every approximant INSIDE an independently
zero-controlled class. Finite ferromagnetic partition functions have the right
zero geometry by Lee–Yang. Matching the exact theta moments then identifies the
limit. Variance control pays every complex tail, so the last step is not an
unpaid continuation from a safe half-plane or a fixed frequency window.

This is established statistical-mechanics territory. Newman–Wu review the RH
and spin-model connection, and Dimitrov explicitly discusses Xi as a possible
partition function. The present proposal is a concrete inverse-moment problem,
with an exact arithmetic starting point and a necessary coupling restriction.
It does not claim that these papers were missing the Lee–Yang idea.

## B. The first nontrivial block is in place

The complete theta calculation constructs an exact first-four-even-moment
solution using 28 spins, four different positive magnetization weights, and
zero couplings. The four weights have multiplicities (25,1,1,1). Its moment
Jacobian is nonsingular, so the actual finite target is an interior point of
that finite feasible set, not an isolated boundary coincidence.

There are also connected strictly ferromagnetic solutions to these same four
equations, by implicit continuation of a common coupling J>0 from zero. No
numerical J0 threshold is supplied. A fixed-J packet must certify its own
root and signs; it cannot inherit a numerical interval from this existence
argument. The supplied seed misses the tenth moment by a certified amount.

A small J therefore gives a controllable laboratory in which to choose graph
perturbations without immediately sacrificing the lower moments. This does
not prove that the tenth moment can be reached, much less every later one.

## C. A finite, checkable search rather than fitting arbitrary probability atoms

For each m the required object is a finite graph G_m, nonnegative edge
couplings and nonnegative observable weights, whose moments match the first
m even theta moments to tolerance 2^(-m). At any candidate use the actual
Gibbs sum. Arbitrary positive quadrature weights are NOT enough: most positive
discrete measures do not have the Lee–Yang property. Nor is a convex mixture
of two certified spin laws automatically admissible as a single ferromagnet.

The function grouped_moments(counts,weights,q,max_order) in check.py computes
EXACT moments of complete-graph grouped models, for rational weights and
rational q>=1 corresponding to coupling J=log(q)/2. Its state count is
product_i(counts_i+1). This uses symmetry, not a discarded configuration tail.
Independent direct enumeration checks it for six small ferromagnetic panels.
The four-group 28-spin graph has 208 grouped configurations even when J>0.

The next finite experiment should preserve moments 2,4,6,8 by interval Newton
on four weight variables while varying graph couplings and additional spin
blocks, and examine the tenth-moment residual in the resulting constrained
family. Exact derivatives are Gibbs covariances:

 d/dJ_ij E[X^k] = Cov(X^k,sigma_i sigma_j),
 d/da_i E[X^k] = k E[sigma_i X^(k-1)]                    (J fixed).

These are finite sums. Positive coupling is an inequality constraint, not a
regularizer that may be violated for a better fit. A numerical fit with some
negative edges does not feed Lee–Yang. For more than a few groups, graph
structure and a theorem controlling its realization are necessary; exhaustive
2^n enumeration is not a proposed scalable proof algorithm.

The supplied exact arithmetic moment quadrature extends to higher orders by
increasing the Taylor and tail constants. It must be revalidated at those
orders. The hard-coded j<=12 ceilings are not an unbounded-order certificate.

## D. What a genuine global advance would look like

A sufficient theorem would be a theta-specific moment-extension statement:
for every m, one can enlarge an admissible finite graph to achieve (IR) at
order m+1 while keeping all earlier moment errors below their required common
tolerance. It need not literally contain its predecessor as a subgraph; it
must retain the fixed limiting moment vector.

A stronger but still sufficient route is membership of the complete theta law
in the weak closure of finite weighted ferromagnets. That membership is NOT
proved by calling it a Lee–Yang law, which would assume the desired zero
statement. We do not assert that every Lee–Yang law is in this Ising closure.
Thus (IR) is a sufficient route and could conceivably fail even if RH is true.

The eight-moment construction and local inverse-function theorem give a start
but NOT this induction. Adding infinitesimal independent spins is particularly
limited: it mostly changes variance and produces a small constrained pattern
of higher cumulants. The next extension must control the shape of the higher
moment changes rather than count free parameters.

## E. The criticality restriction changes the search design

If every weighted pair retains Jij>=tau ai aj with a fixed tau>0, then subtracting
tau X^2/2 leaves a ferromagnet. A realizing sequence with that reserve would
therefore make a NEGATIVELY heated theta law Lee–Yang, contrary to Rodgers–Tao.
Successful approximants must lose this removable complete-graph reserve.
Sparse graphs automatically have zero reserve whenever an edge between two
weighted vertices is absent. The result does not force every coupling small
and does not rule out sparse or strongly coupled local structures.

Consequently a fixed-temperature homogeneous complete-graph picture with a
uniform reserve should NOT be treated as the final model. An increasing sparse
or block family, or a sequence approaching the boundary of that reserve
condition, is more appropriate. This is a proved necessary design condition
for success, not evidence that one of these families actually realizes theta.

## F. Attempts actually made

This pass used ordinary floating scouts for (i) a 20-spin six-moment fit,
(ii) a few common-coupling and two-spin-interaction continuations, and (iii)
four-weight independent fits. The latter found the 28-spin exact-root candidate.
The accepting calculation ignores the floating fit and defines its coefficients
by the full theta moment integrals, scalar sign brackets, and Newton identities.
The six-moment prototype is superseded; no separate six-moment theorem or
claimed successful interacting high-order continuation is being published.
An attempted high-order mpmath derivative scout timed out. Installing an Arb
backend failed because local DNS was unavailable. Neither is a verification.
The final certificate uses a newly written integer interval implementation.

No all-order search, actual Xi zero calculation, heat-zero computation,
positive-J numerical realization, or proof of (IR) was performed. The mathematical
proposal must be judged on that boundary. It creates a new constructive target
with a certified interior starting point, not a completed global sign proof.
