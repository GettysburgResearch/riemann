# Independent review of the original-weight closed-triangle theorem

Reviewer: `/root/middle_joint`, independently of the author
`/root/hlc_joint_paths`. This is an internal mathematical review, not
external peer review of the full HLC paper.

| Reviewed object | SHA256 |
|---|---|
| `CLOSED_TRIANGLE_WEIGHT.md` | `169112b8b41ede59ba23009e5b23d06184e19c03cad209d40940edf1568f7e37` |
| `check_closed_triangle_weight.py` | `3aed0d03eda009fbe93b2f17de320c89d7ce94b93f5487c843114d9e8d6a6d1b` |

**Disposition: accepted.** The continuous theorem pays the stated
absolute, common-shared-list, list-diagonal raw three-edge subfamily
with the original source weights. The discrete theorem is a valid
deduction from its explicitly imported Appendix A.5 estimate. Neither
theorem bounds the complete raw or centered operator, an arbitrary
surrounding history, or the native inverse moment.

I read the note and checker, independently replayed the checker under
`python -O`, and checked the relevant source definitions against the
local text of the PDF whose SHA256 is
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.
The source locations are equations (4.9), (4.12)--(4.13), the original
K_1 and T_1 on page 18, equations (4.28)--(4.31), and Appendix A.5.
I also independently replayed the companion integer-bridge checker.

## 1. The source orbit and three-edge coefficients are correct

For each unordered complete list, exactly J! of the (J+1)! orderings
place a specified departing prime last. Thus the symmetric edge
coefficient is (J+1)^(-K) times the original product of V_i^(-1).
The source vector is one on all admissible root lists. Its squared
coordinate in the normalized unordered-state basis is therefore the
orbit cardinality ((J+1)!)^K times the state measure
product V_i^(-(J+1)). There is one such endpoint-orbit factor, not a
new factor for every intermediate state.

Combining it with three symmetric edges gives exactly equation (5).
The common shared sets are uniquely determined by their product,
because the prime groups are disjoint. Their reciprocal elementary
symmetric sum is bounded by product V_i^J/J!, so multiplication
reduces the complete coefficient to
(J+1)^(-2K) product V_i^(-4). I find no missing J!, J+1,
ordering, factorization or cyclic-root multiplicity.

The chronological products are explicitly (Db,Da,Dc,Db). Accordingly
the determinants D(b-a), D(a-c), D(c-b) follow the original
old-minus-new convention. The common-D and returning-unordered-list
conditions are part of the selected subfamily, not conclusions about
all source paths.

## 2. Prime-level legality pays precisely one line draw

The three legal replacements imply that a_i,b_i,c_i are pairwise
distinct in every prime group. They are also disjoint from its shared
J-set. This proves that D,a,b,c are squarefree and mutually coprime.
It is stronger than merely asking the three numerical products to
be distinct, and it is exactly the hypothesis required for (6).

For a shared prime, all three determinants vanish modulo that prime;
the primitive endpoint reductions are nonzero and hence have the same
projective line. For an unshared prime, the other incident determinants
are nonzero modulo that prime, so its active line differs from every
inactive endpoint line. Returning to the same root does not redraw
its line. Thus the active union costs exactly one 1/(p+1) per prime;
unused-prime damping is at most one. No independent repeated line
draw or Fock normalization enters the proof.

The source raw cutoff psi_1 is one on [-4,4]; the retained raw
arguments are in [-3,3]. The actual prefactor is d_0/D, bounded by
one for every retained edge. The three eta pairs are bounded by
||eta||_infty^6. There is no scalar 1/Y in an edge.

## 3. The root calculation counts multiplicity

With z_0=z_3=(1,0), a candidate is uniquely determined by h and the
displayed integral second vertex. Since j_0+j_1+j_2=0, the congruence
is h=1 modulo |j_0|/g. The source root is the unwrapped variable
R=-2r. The candidate multiplicity is 1/g-periodic in R, and the
interval [-2,0] covers exactly 2g periods. The Jacobian is 1/2.
This gives precisely Wg/|j_0| with W=255/16.

This quantity can exceed one; replacing it by a union probability
would lose paths. Primitivity is retained while assigning projective
lines. Only afterward does the proof enlarge to all integral
candidates in the multiplicity bound. That ordering is legitimate.

I checked the scalar gcd summation independently. Fixing b gives at
most four sign choices for h=a-b and k=c-b. The identity
gcd(h,k)=sum_{d|h,d|k} phi(d), followed by the harmonic divisor sum,
gives the stated 48/Y times (1+log(3Y))^2. The factor D cancels
from the gcd ratio. The remaining continuous root coordinates have
volume 15, and their source density is 1/(3 zeta(2)); both are kept
separate from the state and list measures.

## 4. The finite-root transfer has the stated explicit scope

Appendix A.5 supplies a normalized prescribed-line count with error
S^5 min(d_0YM,N)^(-1/100), uniform in the three intervals and in
the line choices, including the odd-coordinate density 1/(3 zeta(2)).
The note imports this theorem transparently.

For the positive upper count, dropping goodness, unused damping and
later position projectors leaves a single first-position interval in
r for each fixed label family and h. Taking the full s,t_0 rectangles
then allows A.5 directly. No approximation by cubes, smooth-boundary
count, or unproved odd-moment version of Proposition 4.4 is required.
The main terms are the same enlarged continuous majorant used in the
proof of Theorem 1, so they have its upper bound.

The three error costs are: at most x^((J+3) beta) label families,
at most O(x^((J+1) beta)) candidate h, and the per-candidate error
x^(5(J+3) beta-delta/100). Their product is exactly the exponent
(7J+19) beta-delta/100. The orbit and V coefficients are uniformly
bounded here because J,K are fixed and V_i have a fixed positive
lower bound. The discrepancy receives no invented 1/(Dabc) factor.
The explicit J=K=1 example has error exponent -37/20000.

The fixed-J redesign does not cover the source's original growing-J
scheme. Nor may a conditional path history be attached to this root
average for free. These restrictions are stated in the note and are
essential to its valid conclusion.

## 5. Replay

The optimized checker passed 14,049 literal ordered paths, 12 orbit
normalizations, 15 factorial cancellations, 720 shared-list sums,
3,050 actual prime-line averages, 560 retained primitive paths,
24 exact candidate-count integrals, 21 error budgets and six negative
controls. The companion integer-bridge checker also passed, including
756 multiplicity integrals and 54,540 weighted distinct-product
triples. These finite checks support the algebra and normalizers;
the analytic bounds and imported count are distinguished above.

A separate refinement of Appendix A's root count is being developed.
It is not used by this review or by the hashes reviewed here.
