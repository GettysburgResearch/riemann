# Theta-source quotient and tensor coherence

Status: PROPOSED SOURCE-EXACT THEOREM; independent review required.
Authoring base: MP `fdd349dcf6ba1b104e27866ae66b4c89752d5f05`.
Sections1--6 retain the original preregistered design, not a computation
report. Section7 records the necessary regularity correction, itself frozen
before arithmetic at `e2c659ef1c1af926de63b69bf6c9ead6a95feaf5`.
Sections8--12 give the corrected theorem, proof and complete finite outcomes.

Target: an exact source-level closure/coherence theorem extending MP's
Petersson-vacuum theta completion. Quotient metrics, Schur complements,
minimum-energy lifts and their quotient formula are classical. The intended
contribution is the precise completion/source dictionary and its boundaries,
not a new abstract linear-algebra theorem or an Euler/RH assertion.

## 1. Proposed source class and theorem obligations

A source consists of a finite-dimensional nonzero complex vector space,
a positive Hermitian vacuum G, a weight alpha>0, and a measurable finite
Hermitian matrix field H(t)>=G for t>0. Require H locally integrable on
(0,infinity) and H(t)-G=O_A(t^-A) for EVERY A>0 as t tends to infinity.
The regularity assumption is essential; decay at infinity alone does not
control singularities on compact intervals. Require the exact identity

    H(t)=t^-alpha H(1/t).

For any fixed surjection pi:V->Q with1<=dim Q<=dim V, define

    H_Q=(pi H^-1 pi*)^-1,  G_Q=(pi G^-1 pi*)^-1,
    C_Q(t)=(H_Q(t)-G_Q)/2.

Prove all of the following, with the same fixed source and maps:

1. H_Q is the maximal quotient metric F with pi*F pi<=H. It is the
   minimum of H[v] over pi v=y. The unique minimum-energy lift is
   J_pi=H^-1 pi*H_Q. The assertion is about H_Q, NOT C_Q alone.
2. Nested surjections are associative, with compatible composition of
   their minimum-energy lifts. Direct sums of sources of the SAME weight
   commute with block-diagonal quotient maps.
3. Tensor sources (G1 tensor G2,H1 tensor H2) have weight alpha1+alpha2;
   their quotient under pi1 tensor pi2 is the tensor of their quotient
   metrics, including the vacuum. No tensor-unit assertion for alpha>0.
4. C_Q>=0 globally, but is strictly positive for0<t<1 by the affine law
   C_Q(t)=t^-alpha C_Q(1/t)+(t^-alpha-1)G_Q/2. Global strict positivity
   need not hold when H>=G is not strict. Rapid decay and local
   integrability descend using an adapted vacuum-orthonormal lift.
5. L_Q(s)=integral_0^infinity C_Q(t)t^(s-1)dt initially for Re s>alpha
   continues as

    alpha G_Q/[2s(s-alpha)]
       + integral_1^infinity [t^(s-1)+t^(alpha-s-1)]C_Q(t)dt.

   It has precisely the nonzero simple endpoint residues -G_Q/2 at0
   and+G_Q/2 at alpha, reflects by s->alpha-s, and satisfies Schwarz
   symmetry. Its Mellin feature kernel is positive on Re z>alpha/2.
   Actual MP theta sources have alpha1; integer tensor powers give
   actual source-derived integer-weight examples, not new automorphic
   representations or an Euler product.
6. For a finite nonzero positive compactly supported measure and an
   integrable positive block field H=[[A,B],[B*,D]], with D bounded
   below by a positive constant, prove

    Schur(integral H)-integral Schur(H)
      = integral (L-Lbar)*D(L-Lbar),
    L=D^-1 B*,  Lbar=(integral D)^-1 integral B*.

   Matrix equality holds exactly when L is constant almost everywhere.
   Do not apply this formula to the unrenormalized full Mellin integral
   of H: the vacuum would diverge. No silent interchange of Schur and
   Mellin or identification with MP's period-side quotient is permitted.

## 2. Fully fixed base sources and coordinate changes

All matrices below use conjugate-linear first input and i^2=-1. Set

    G1=[[2,1+i],[1-i,3]],       R1=[[2,i],[-i,1]],
    G2=[[1,0],[0,2]],           R2=[[3,1],[1,1]],
    alpha1=1, alpha2=2.

For t>=1 define H_i(t)=G_i+R_i on1<=t<=2 and H_i(t)=G_i on t>2.
For0<t<1 use H_i(t)=t^-alpha_i H_i(1/t). These are complete synthetic
locally integrable compact-tail sources, not actual modular theta values.
The tested upper-side parameters are exactly3/2,2,3, together with their
reciprocal mates. Thus the t=3 cases deliberately include H_i=G_i.

The fixed surjections and invertible coordinate matrices are

    pi1=[1,i],        pi2=[1,1-i],
    C1=[[1,i],[0,1]], C2=[[1,1+i],[i,2]],
    B1=[1+i],        B2=[2-i].

For coordinate covariance use H'=C*HC, G'=C*GC and pi'=B^-1 pi C.
The expected quotient matrices are B*H_Q B and B*G_Q B. Transform
BOTH vacuum and source; a nonunitary basis does not preserve an identity
vacuum. Record all six base source cells and their lifts, quotient
positivity, contraction pi*H_Q pi<=H, covariance and reciprocity.

## 3. Tensor, direct sum, and nested maps

At each of the same three upper parameters, test the four-dimensional
tensor source G1 tensor G2,H1 tensor H2 of weight3, with pi1 tensor pi2.
Verify the complete quotient and lift tensor identities, including their
vacuum versions and reflected values. This is three tensor cells.

For the direct-sum test, use the same upper-side G_i,H_i but reflect BOTH
components with weight1 (a declared second copy of source2 with weight1).
Use pi1 direct-sum pi2; this is three same-weight direct-sum cells. Do not
declare the original weight1/weight2 direct sum a common-weight source.

For each tensor cell, use the FULL fixed chain4->3->2->1:

    P43=[[1,0,0,i],[0,1,0,1],[0,0,1,0]],
    P32=[[1,i,0],[0,1,1]],
    P21=[1,1+i].

Compare every successive quotient with the quotient by its composite map,
and compare composed minimum-energy lifts with the direct lift. Repeat
for the vacuum. This is three chain cells, each with three stages; no
additional maps or points will be selected after seeing results.

## 4. Averaging defect: equality and strict inequality controls

Use the compact atomic measure with locations1,3/2,2 and weights1/6,2/6,3/6.
In quotient/block dimensions2+2 set

    D1=[[2,1],[1,2]], D2=[[3,i],[-i,2]], D3=[[1,0],[0,4]],
    L1=[[0,0],[0,0]],
    L2=[[1/2,i/2],[0,0]],
    L3=[[0,0],[1/2,1/2]].

For each j form the positive matrix

    H_j=[[I2+L_j*D_jL_j,L_j*D_j],[D_jL_j,D_j]].

The first control uses these three different lifts. The second uses
L1=L2=L3 equal to the displayed nonzero L2, leaving the D_j and weights
unchanged. Predicted outcomes: the exact averaging identity in both
cases; strict positive-definite defect in the variable-lift case; zero
defect in the common-lift case. The strict prediction is justified before
computation: a zero direction would be killed by both displayed L2 and
L3, whose kernels have zero intersection. The D_j need not commute.

These are two averaging controls, not actual period integrals. They may
be embedded in a positive source class after choosing a sufficiently
small common vacuum, but no such embedding is needed for this lemma.

## 5. Source tensor is not multiplication of completed observations

Use the scalar vacuum-only sources

    H_alpha(t)=max(1,t^-alpha), G=1, alpha in{1,2,3}.

They satisfy the full source class and H1(t)H2(t)=H3(t), whereas their
Mellin observations are L_alpha(s)=alpha/[2s(s-alpha)]. Prove as rational
functions that L3 is NOT L1 times L2. Retain all three exact evaluations
at s=4,5,6, and the complete cross-multiplied polynomial identity. This
is an observation-operation firewall, not a failed tensor-source law.

Also record the unequal-weight direct-sum failure at t=2 and1/2: the
diagonal reciprocal scaling factors2 and4 cannot be one common scalar.
This is one fixed negative control, not an all-weight numerical survey.

## 6. Frozen coverage and acceptance boundary

Declared records: six base cells, three tensor cells, three direct-sum
cells, three nested-chain cells (each all three stages), two averaging
controls, three rational observation evaluations plus their polynomial
identity, and one unequal-weight direct-sum countercontrol. All matrix
dimensions are at most4. Gaussian-rational operations, complete principal
minors, independent exact elimination/Gram routes, and explicit resource
caps will be used. No floating-point logarithm, special function, numerical
theta integral or asymptotic limit is accepted by the finite checker.

The final packet will pin this preregistration, MP's proof/producer/fixture/
manifest/tests, and its own final artifacts. It must distinguish written
analytic proof from exact finite algebra. Full source equality, strict
types/caps, normal/-O replay, resealed hostile reports and source/artifact
tampering will be checked before scientific freeze and independent review.

## 7. Amended regularity design, still before finite computation

The first design is frozen at
`bd53c016dbd006ac5e40d4fff412162a68e99525`. Its unconditional tensor-closure
obligation for the locally L1 class is FALSE. It is not silently retained.
On the upper side take the scalar G=1, alpha=1 and

    H(t)=1+|t-3/2|^(-2/3) for 0<|t-3/2|<1/8,
    H(t)=1 otherwise (including at the single point t=3/2).

Extend below1 by the specified reciprocal law. Every value is finite,
the field is measurable, locally L1 and has compact upper tail. Its tensor
square has the nonintegrable local term |t-3/2|^(-4/3). Thus local L1
alone does not support tensor closure or even the tensor Mellin integral.
Indeed integral_0^epsilon u^(-2/3)du=3epsilon^(1/3), whereas
integral_eta^epsilon u^(-4/3)du=3(eta^(-1/3)-epsilon^(-1/3)) diverges
as eta decreases to0. Every fixed real Mellin weight is bounded above and
below by positive constants on this compact neighborhood of3/2.

The corrected target is two-tiered. Quotient, same-weight direct sum,
continuation, positivity and averaging hold under their stated local-L1
hypotheses. Tensor closure holds if the tensor field is locally integrable;
in particular the locally BOUNDED measurable subclass is tensor-closed.
The actual MP theta sources are locally bounded (indeed continuous), as
are all complete synthetic sources fixed in sections2--5. No finite panel,
matrix, point, measure or count changes. This amendment is to be frozen
as a new design identity BEFORE executing those controls.

## 8. Exact quotient theorem and the corrected source class

All spaces are finite-dimensional complex spaces, all maps are fixed
independently of t and s, and * is conjugate transpose. Matrix inequalities
are inequalities of Hermitian forms. A weak source (G,H,alpha) satisfies
section1's hypotheses: G>0, alpha>0, every H(t) is finite Hermitian and >=G,
H is measurable and locally integrable, H(t)=t^-alpha H(1/t) at every t>0,
and ||H(t)-G||=O_A(t^-A) as t->infinity for each A>0. A bounded source also
has H locally bounded. Bounds depend on the fixed source, not universally
on all sources. No dimension or regularity conclusion is inferred from
the finite panel.

**SC1 (quotient and its universal property).** For any fixed surjection
pi:V->Q with1<=dim Q<=dim V, set

    H_Q=(pi H^-1 pi*)^-1,    J_pi(H)=H^-1 pi* H_Q.             (SC1)

The matrix inside the inverse is positive definite because pi* is
injective. Direct multiplication gives

    pi J_pi=I_Q,  J_pi* H J_pi=H_Q,
    J_pi* H v=0 for v in ker pi.                             (SC2)

Every lift of y has the unique form J_pi y+v with v in ker pi. Its
H-energy is y*H_Q y+v*Hv. This proves the unique minimum-energy property.
It also proves pi*H_Q pi<=H. Conversely, if a Hermitian F on Q satisfies
pi*F pi<=H, then evaluating on the minimizing lift gives F<=H_Q. Thus H_Q
is the MAXIMAL quotient metric under that inequality. This maximality is
not a statement that C_Q=(H_Q-G_Q)/2 is a maximal metric without its vacuum.

For another surjection rho:Q->R, inversion yields

    (H_Q)_R=(rho pi H^-1 pi* rho*)^-1=H_R,
    J_pi(H) J_rho(H_Q)=J_(rho pi)(H).                         (SC3)

These are associativity of the actual quotient and of its canonical lifts,
not just equality of dimensions. Repeat the same operations on G to obtain
G_Q and G_R. Iteration acts on H_Q=G_Q+2C_Q; applying it to C_Q alone would
be a different operation and may fail even to be invertible.

Under coordinates H'=C*HC,G'=C*GC,pi'=B^-1 pi C, with C,B invertible,

    H'_Q=B*H_Q B,  G'_Q=B*G_Q B,
    J_pi'(H')=C^-1 J_pi(H) B.                                (SC4)

This follows by substituting the inverses. Both source and vacuum must
transform. A nonunitary basis change does not leave the identity vacuum
fixed. The formulas are invariant statements on quotient Hermitian spaces.

**SC2 (descent of regularity and positivity).** Quotienting a weak source
produces a weak source of the same weight. It preserves local boundedness
when that is imposed. To see all assertions without differentiability,
choose fixed G-orthonormal coordinates adapted to ker pi and quotient
coordinates adapted to its G-minimal lift. Write H=I+R with R>=0. Then

    H_Q-G_Q=R11-R12(I+R22)^-1 R21,
    0<=H_Q-G_Q<=R11.                                         (SC5)

The lower bound is the energy minimum or monotonicity derived from SC2;
the upper bound comes from choosing the vacuum-minimal lift with zero
kernel component. Fixed coordinate changes preserve integrability and
decay. Inversion is continuous on the positive cone, so measurability also
descends. SC5 pays local L1, local boundedness when available, and the
all-order rapid tail. Homogeneity of SC1 gives

    H_Q(t)=t^-alpha H_Q(1/t),
    C_Q(t)=t^-alpha C_Q(1/t)+(t^-alpha-1)G_Q/2.                (SC6)

Consequently C_Q>=0 everywhere and C_Q>0 on0<t<1. On t>=1 strictness is
not forced: the preregistered t=3 cases have C_Q=0. For the actual MP
theta source H>G everywhere, strictness everywhere follows separately.

## 9. Tensor/direct-sum closure and completed observations

**SC3 (tensor coherence, with necessary function-space scope).** Let
(G_i,H_i,alpha_i),i=1,2 be bounded sources. Then

    G=G1 tensor G2, H(t)=H1(t) tensor H2(t),
    alpha=alpha1+alpha2                                      (SC7)

is a bounded source. The pointwise order follows from

    H-G=(H1-G1) tensor H2+G1 tensor (H2-G2)>=0.

Finite products of locally bounded measurable functions are locally
bounded. Both H_i tend to G_i, so the same expansion pays every rapid-tail
bound. The reciprocal weights add. These arguments also work for weak
sources IF their tensor field is locally integrable; the counterexample
of section7 proves this extra condition cannot be discarded.

For pi=pi1 tensor pi2, the inverse/product rules give exactly

    H_Q=(H1)_Q1 tensor (H2)_Q2,
    G_Q=(G1)_Q1 tensor (G2)_Q2,
    J_pi=J_pi1 tensor J_pi2.                                 (SC8)

Thus tensoring commutes with the quotient AND with its minimal lift.
Iterated tensors associate using the canonical linear tensor identifications;
weights add, and quotient compositions associate by SC3. No unit at weight0
is asserted in this alpha>0 class. Direct sums preserve a fixed common
weight and commute with block-diagonal quotient maps; this follows directly
from block-diagonal inversion. Distinct weights generally have no common
scalar reciprocity, as the retained factors2 and4 demonstrate.

**SC4 (completed matrix observation).** For a weak source and any fixed
quotient define L_Q(s)=integral_0^infinity C_Q(t)t^(s-1)dt for Re s>alpha.
This is absolutely convergent: at infinity use rapid decay; at zero SC6
is the explicit O(t^-alpha) vacuum term plus a rapidly flat remainder.
Compact intervals are covered by local L1. Splitting at1 and substituting
u=1/t gives

    L_Q(s)=alpha G_Q/[2s(s-alpha)]
          + integral_1^infinity
              [t^(s-1)+t^(alpha-s-1)] C_Q(t)dt.               (SC9)

For every compact s-set, a sufficiently strong rapid-tail bound dominates
the integrand and every s derivative (powers of log t). Hence the integral
term is entire. This proves meromorphic continuation, reflection
L_Q(s)=L_Q(alpha-s), Schwarz symmetry L_Q(bar s)=L_Q(s)*, and exactly the
nonzero simple matrix residues -G_Q/2 at0 and+G_Q/2 at alpha. There are no
other entrywise poles; no claim that a determinant has simple endpoint
poles is intended. Its endpoint pole order can equal the quotient rank.

The kernel L_Q(z+bar w) is positive on Re z>alpha/2. Its finite quadratic
sum is the integral of the C_Q-energy of sum_j t^(bar z_j)v_j with measure
dt/t. Convergence follows from pairwise Cauchy--Schwarz in the positive
measure and Re z_j>alpha/2. The strict positivity on0<t<1 also makes each
L_Q(sigma)>0 for real sigma>alpha. This is a Mellin feature kernel, not a
pointwise Herglotz assertion or a zero-location theorem.

The actual MP source is H=G+2B(t),alpha1, with the exact Petersson vacuum
and theta density MP1. MP's cusp domination is locally uniform in t, so
dominated convergence gives continuity of B(t), hence local boundedness.
MP proves its all-order tail and reciprocal identity. SC7--SC9 therefore
give integer-weight tensor/quotient completions from that actual source.
They are source-derived globally completed matrix families, not new
automorphic representations or independently established Euler products.

Tensor coherence holds BEFORE observation. Put C_i=((H_i)_Qi-(G_i)_Qi)/2.
Then the tensor excess is

    C_tensor=C1 tensor G_Q2+G_Q1 tensor C2+2C1 tensor C2.       (SC10)

This is a pointwise product rule, not multiplication of the Mellin
transforms. The complete scalar control H_alpha(t)=max(1,t^-alpha) has
H1H2=H3 and L_alpha=alpha/[2s(s-alpha)], but

    L3-L1 L2=(3s^3-9s^2+5s+3)
                /[2s^2(s-1)(s-2)(s-3)] !=0.                 (SC11)

There is a genuine pole at3 absent from L1L2. Thus the source tensor law
does not turn observation into a multiplicative functor on these Mellin
functions. This sharply separates an honest source operation from an
unjustified scalar multiplication prescription.

## 10. Averaging: exact obstruction to commuting elimination and integration

Let mu be a finite nonzero positive compactly supported measure, and let
H(t)=[[A,B],[B*,D]] be positive definite, measurable and entrywise integrable
with respect to mu. Suppose D(t)>=d I for some fixed d>0 almost everywhere.
Put L(t)=D(t)^-1 B(t)*, Dbar=integral D, and
Lbar=Dbar^-1 integral B*. The block coefficient L is the NEGATIVE of the
kernel part in the minimum-energy lift [I;-L]. Since
0<=L*DL=B D^-1 B*<=A, all quadratic terms below are integrable. Dbar>0.

Writing S(H)=A-BD^-1B*, direct expansion gives

    S(integral H)-integral S(H)
       = integral L*DL-Lbar*Dbar Lbar
       = integral (L-Lbar)*D(L-Lbar)>=0.                     (SC12)

The cross terms simplify because integral DL=integral B*=Dbar Lbar.
This proves the formula for a finite, not necessarily probability, measure.
Equality of the full matrices holds iff L=Lbar almost everywhere: take
the trace of the nonnegative integrand and use D>=dI. Directional equality
on v only requires L(t)v=Lbar v almost everywhere, a weaker condition.
No commutation of D_j is assumed. The preregistered variable-lift control
has zero common kernel for L2 and L3 after L1=0, hence strict defect.

Applied to a compact positive weighting of an actual source, SC12 precisely
measures the failure of a single minimizing lift to minimize at every t.
It cannot be applied to an unrenormalized Mellin integral of H on(0,infinity):
the vacuum G has a divergent integral. SC9 performs the required pointwise
subtraction and endpoint continuation instead. In particular neither SC12
nor tensor closure identifies the new source quotient with the old
period-side Schur quotient, whose genuine interior poles survive in FI.

## 11. Completed finite replay and source contract

All declared controls were run only after both frozen design commits.
The exact Gaussian-rational producer independently builds the full matrices,
not just target booleans. It records all six base source cells, three
tensor cells, three common-weight direct sums, three nested chains each
with all three stages for BOTH source and vacuum, two averaging controls,
and the three rational observation values plus their polynomial identity.
The variable-lift defect has determinant77/2316>0; the common-lift defect
is the zero matrix. The t=3 base excesses are zero while their reciprocal
excesses are strictly positive. No failed t-value or panel is discarded.

The source manifest binds all five MP scientific files and both frozen
design notes by literal Git blob and LF-normalized SHA256. It also binds
the final note, producer, manifest and tests through the fixture, with a
canonical full-payload digest. Arithmetic is MIXED with EXACT_RATIONAL
and CERTIFIED_INTEGER_COVERAGE components; rounding is NONE. These are
finite algebra and complete declared coverage, not analytic certificates.
No floating theta, special function, integral or asymptotic limit is used.

The acceptance rule is equality with a complete fresh, source-authenticated
primitive reconstruction. Merely resealing an altered fixture is insufficient.
The tests include independent permutation determinants/adjugate inverses,
energy and averaging routes, strict type/dimension/bit/work/JSON bounds,
source and artifact tampering and resealed scope/coverage attacks. The
producer's 4-dimensional matrix bound is a computational cap, not the
dimension scope of SC1--SC12. Final command counts and fresh-SHA results
are supplied with the frozen handoff; independent review remains necessary.

## 12. Classical credit, exact contribution and remaining burden

The underlying extremal shorted form and quotient identities are classical:
[Anderson, Shorted operators, 1971](https://doi.org/10.1137/0120053),
[Anderson--Trapp, Shorted Operators II, 1975](https://doi.org/10.1137/0128007),
and [Ando, Generalized Schur complements, 1979](https://doi.org/10.1016/0024-3795(79)90040-5).
Their publisher abstracts were checked for the maximality/quotient context;
no inaccessible full-text theorem is silently imported. SC1--SC12 have
complete finite-dimensional proofs above. The Mellin split is the classical
theta-completion mechanism with the specified transformed vacuum.

The programme application is a coherent, positive-source completion class
generated by MP's actual theta matrix, including nested quotients and tensor
weights, together with precise observation-operation and regularity boundaries.
It does not select a privileged flag, give a categorical archimedean/Euler
description, establish critical-line zeros, or prove RH/GRH. The scalar
Mellin functions are not claimed to multiply under source tensoring.
External priority has not been exhaustively researched. The smallest
load-bearing analytic obligations are local integrability of the actual
source, its all-order tail, and the homogeneous source identity; MP pays
them for the actual example, while section7 prevents extending the tensor
claim to an insufficient function space.
