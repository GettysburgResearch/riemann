# Source quotient and tensor coherence: preregistered proof/control target

Status: PREREGISTRATION, frozen BEFORE executing any new finite control.
Authoring base: MP `fdd349dcf6ba1b104e27866ae66b4c89752d5f05`.
No result in this note is a report of a completed computation.

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

The corrected target is two-tiered. Quotient, same-weight direct sum,
continuation, positivity and averaging hold under their stated local-L1
hypotheses. Tensor closure holds if the tensor field is locally integrable;
in particular the locally BOUNDED measurable subclass is tensor-closed.
The actual MP theta sources are locally bounded (indeed continuous), as
are all complete synthetic sources fixed in sections2--5. No finite panel,
matrix, point, measure or count changes. This amendment is to be frozen
as a new design identity BEFORE executing those controls.
