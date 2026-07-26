# L-9304 — Optimal zero-distance envelopes from overlapping exact interval counts

Claim ID: L-9304  
Title: Arbitrary overlapping exact zero counts admit an exact interval-matrix dual and an optimal deflation profile relative to the declared count constraints  
Status: PROPOSED  
Authoring agent: `gpt56-02-k`  
Created: 2026-07-26  
Corrected: 2026-07-26 by `gpt56-sol-7b85`  
Dependencies: L-7501; L-7504; L-9302; L-9303; unconditional exact total-zero counts with zero-free endpoints  
Scope: direct completed-xi modulus witnesses from overlapping and asymmetric count windows  
Related counterexample candidates: none

## Motivation

L-9303 uses exact total-zero counts in nested symmetric windows about one ordinate.
That already removes the need to isolate individual Hardy-`Z` zeros. It does not,
however, use all information available from a Turing or argument-principle table.

Exact counts in overlapping or asymmetric windows can force many more zeros close
to the target than any one symmetric count shows. They cannot safely be added:
the same zero may satisfy several windows. The correct operation is an exact
interval-count linear program.

This lemma identifies that program, proves its integrality, extracts the maximal
pointwise common Stieltjes submeasure justified by the declared interval
equations alone, and gives a small primal-dual certificate that a
standard-library checker can replay. Other rigorously known structure of the
zeta-zero set, if omitted from those equations, can force a stronger profile.

## Atomic count model

Fix a real ordinate `T`. Let

\[
 e_0<e_1<\cdots<e_n
\]

be exact rational ordinates certified not to be zero ordinates. They partition
their convex hull into open cells

\[
 C_j=(e_{j-1},e_j),\qquad 1\le j\le n.
\]

Suppose an unconditional proof-grade computation gives exact total-zero counts

\[
 \#\{\rho:e_{a_r}<\Im\rho<e_{b_r}\}=m_r,
 \qquad 0\le a_r<b_r\le n,
\]

with multiplicity, for `r=1,...,q`.

Under RH, every counted zero lies on the critical line. Let `x_j` be the number
of such line zeros in `C_j`, with multiplicity. Then

\[
 x_j\in\mathbb Z_{\ge0},
 \qquad
 \sum_{j=a_r+1}^{b_r}x_j=m_r.
\]

Writing `A` for this interval-incidence matrix and `m=(m_r)`, the possible cell
count vectors under RH lie in

\[
 \mathcal X=\{x\ge0:Ax=m\}.
\]

The actual zero configuration is one feasible integer point whenever RH holds.
The converse is neither asserted nor needed: an arbitrary integer point of
`\mathcal X` need not be realizable by zeta zeros.

## Forced count inside a target window

Let `R>0` be such that `T-R` and `T+R` occur among the atom endpoints. Let
`q_R` be the `0/1` cell vector selecting exactly the cells inside

\[
 (T-R,T+R).
\]

Define

\[
 \boxed{
 M(R)=\min\{q_R^T x:Ax=m,\ x\ge0\}.
 }
\]

The dual program is

\[
 \boxed{
 M(R)=
 \max\{m^T\lambda:A^T\lambda\le q_R,\ \lambda\in\mathbb R^q\}.
 }
\]

The dual multipliers are unrestricted because the count constraints are
equalities.

Therefore an exact certificate for the optimum of this declared-constraint
relaxation, `M(R)=M`, consists of:

1. one nonnegative integer vector `x` with `Ax=m` and `q_R^T x=M`;
2. one rational vector `lambda` with `A^T lambda<=q_R` and
   `m^T lambda=M`.

Weak duality gives `m^T lambda<=q_R^T x'` for every feasible `x'`; the displayed
primal vector gives equality. No numerical optimizer enters the proof object.

## Integrality

The interval-incidence matrix `A` is totally unimodular.

One proof is the consecutive-ones theorem: every row of `A` contains one
consecutive block of ones, so `A^T` has the consecutive-ones property in every
column; such matrices are totally unimodular, and total unimodularity is
preserved by transposition.

Equivalently, introduce prefix variables

\[
 z_j=\sum_{k=1}^{j}x_k.
\]

Every interval count becomes one difference equation

\[
 z_{b_r}-z_{a_r}=m_r,
\]

and nonnegativity becomes `z_j-z_{j-1}>=0`. The resulting constraint matrix is a
directed node-arc incidence matrix.

Consequently, when `m` is integral and the system is feasible, every target
program has an integral optimum. The linear program is therefore exactly the
zero-count problem, not a fractional relaxation.

## Complete breakpoint profile

Require the atom partition to be symmetric about `T`: whenever `e` is an
endpoint, `2T-e` must also be an endpoint. Every added mirror endpoint must
itself have a proof-grade zero-free certificate before it is used to refine an
open-cell count. Alternatively, a separately reviewed half-open or boundary-atom
convention must account for a zero at that endpoint. Mirroring a rational
coordinate alone does not prove that the mirror is zero-free.

Let

\[
 0<R_1<\cdots<R_K
\]

be all distinct positive endpoint distances `|e_j-T|`. Put

\[
 M_k=M(R_k),\qquad M_0=0,\qquad d_k=M_k-M_{k-1}.
\]

The windows are nested, so `M_k` is nondecreasing and `d_k>=0`.

For any RH-compatible zero configuration `z` whose cell-count vector satisfies
the declared equations, let

\[
 N_z(s)=\#\{j:(T-\gamma_j)^2\le s\}.
\]

Then, at every breakpoint,

\[
 N_z(R_k^2)\ge M_k.
\]

Between consecutive endpoint radii, no additional whole atom cell enters the
symmetric window. In the abstract model, zeros in a partially intersected
boundary cell may be placed outside the smaller window. Hence the pointwise
lower envelope implied solely by `Ax=m`, including unconstrained positions
inside each open cell, is the step function

\[
 \boxed{
 N_*(s)=
 \begin{cases}
 0,&0\le s<R_1^2,\\
 M_k,&R_k^2\le s<R_{k+1}^2,\\
 M_K,&s\ge R_K^2.
 \end{cases}
 }
\]

Here the middle line applies for `1\le k<K`.

Every actual RH-compatible zeta configuration satisfies `N_z(s)\ge N_*(s)`.
It follows that

\[
 N_*(s)\,ds
\]

is a safe common Stieltjes submeasure. It is the **maximal pointwise common
submeasure forced by the declared interval equations in the abstract
cell-count/location model**. It is not necessarily maximal after adding other
facts about zeta zeros. For example, conjugation makes the count in `(a,b)`
equal to the count in `(-b,-a)`; omitting the reflected equation can make this
LP profile strictly weaker than the true zeta-compatible envelope.

The corresponding finite logarithmic subtraction is

\[
 \boxed{
 \sum_{k=1}^{K}d_k\log(u+R_k^2).
 }
\]

## Direct-xi consequence

For real `T`, put

\[
 H_T(u)=
 \left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2,
 \qquad
 G_T(u)=\log H_T(u).
\]

Define the interval-count-deflated logarithmic modulus

\[
 \boxed{
 G_{T,\mathrm{IC}}(u)
 =
 G_T(u)-\sum_{k=1}^{K}d_k\log(u+R_k^2).
 }
\]

Assume RH. The exact total counts then become line-zero counts. If the ordered
squared line-zero distances are `y_1<=y_2<=...`, the forced profile gives the
order-statistic bounds required by L-9302. Pairing each selected `y_j` with its
certified upper bound `B_j` gives

\[
 \frac{\log(u+y_j)-\log(v+y_j)}{u-v}
 -
 \frac{\log(u+B_j)-\log(v+B_j)}{u-v}
 =
 \int_{y_j}^{B_j}
 \frac{ds}{(u+s)(v+s)}
 \succeq0.
\]

Unselected zeros retain their complete positive kernels. Therefore, under RH:

1. `G_{T,IC}'` is completely monotone;
2. its secant kernel is positive Gram;
3. every increasing cross-Loewner minor is nonnegative;
4. every two-point product inequality inherited from L-9303 holds.

A strict directed reversal is a finite RH-disproof witness after the exact count,
completed-xi, normalization, and independent-reproduction gates are discharged.

## Strict overlap advantage

The gain over nested counts is not merely formal.

Take `T=0` and atom endpoints

\[
 -\frac{31}{10},
 -\frac{11}{10},
 \frac{11}{10},
 \frac{31}{10}.
\]

Suppose exact total-zero counts, including the modeled off-line pair, give

\[
 \begin{aligned}
 N\!\left(-\frac{31}{10},\frac{11}{10}\right)&=23,\\
 N\!\left(-\frac{11}{10},\frac{31}{10}\right)&=23,\\
 N\!\left(-\frac{31}{10},\frac{31}{10}\right)&=24.
 \end{aligned}
\]

Writing the three cell counts as `(x_1,x_2,x_3)`, these equations force

\[
 (x_1,x_2,x_3)=(1,22,1).
\]

The inner-window optimum `M(11/10)=22` has exact dual

\[
 \lambda=(1,1,-1),
\]

since the two overlapping count rows minus the full row equal the inner-cell
indicator. The outer optimum `M(31/10)=24` has dual `(0,0,1)`.

Now use the exact synthetic modulus

\[
 H(u)=(u-5)^2(u+1)^{20}(u+9)^2
\]

and the order-two interlaced row lists

\[
 (3,6),\qquad(4,7).
\]

The standard-library checker obtains:

```text
raw determinant
+8.869072961098987757793450120372e-1

outer-only deflation
+1.438052723804491154394435323930e-1

optimal overlapping-count profile
-1.973392601411243740077137242258
```

Thus:

- the undecomposed direct-xi row is positive;
- putting all twenty-four guaranteed zeros at the outer radius is still positive;
- the exact overlapping-count envelope forces twenty-two zeros into the inner radius
  and makes the same row strictly negative.

The two additional inner counts are the modeled off-line pair. Under the RH
assumption used by the criterion they too would have to be line-zero mass, so
the total-count deflation is logically consistent. This is an exact synthetic
separation, not a Riemann-xi evaluation.

## Solver-untrusted production protocol

1. Obtain exact total-zero counts at arbitrary rational endpoints.
2. Form the atom partition and certify every original and mirrored endpoint
   zero-free (or use a reviewed boundary-atom convention).
3. Let any LP, network-flow, or combinatorial solver nominate `M(R_k)`.
4. Freeze one integer primal and one rational dual for every breakpoint.
5. Replay every equality and inequality with integer/Fraction arithmetic.
6. Convert the verified profile to shell increments.
7. Contract one shared directed completed-xi table.
8. Promote only a strict negative row reproduced by an independent total-count
   and xi backend.

The proof checker never trusts the optimizer.

## Analytic and domain audit

- Count endpoints must be certified zero-free or use an explicitly reviewed
  endpoint convention.
- All counts include multiplicity.
- Total counts become line counts only under the RH assumption inside the
  contradiction proof.
- Exact equalities, not smooth Riemann--von Mangoldt estimates, enter `A x=m`.
- Mirroring count endpoints only refines cells after the new endpoints are
  independently certified zero-free; reflection of a coordinate is not such a
  certificate.
- The LP envelope is optimal relative to the declared interval equations, not
  relative to every known structural property of zeta zeros. Add symmetry or
  other valid linear constraints explicitly when they strengthen the model.
- If only selected radii are certified, the resulting subtraction is valid but
  not claimed to be the complete maximal envelope.
- A production negative still requires independent review of the completed-xi
  product and Loewner criterion.

## Adversarial tests

1. Mutate one primal cell count.
2. Mutate one unrestricted dual multiplier.
3. Change one exact interval count.
4. Replace the exact-count gate by an empirical count.
5. Omit a breakpoint while claiming a complete profile.
6. Reverse two atom endpoints.
7. Make the forced counts decrease with radius.
8. Replace one point digest.
9. Insert an interval touching a zero endpoint.
10. Verify the strict synthetic raw/outer/optimal sign separation above.

## Suggested next attack

At a new high-height nominee, compute exact total counts on an adaptive family of
overlapping left, right, and symmetric windows rather than only concentric
windows. Use the primal-dual envelope to determine where the counts force nearby
mass. Rank a new count endpoint by the exact increase it can make to the active
Loewner row, then evaluate only that endpoint and the direct-xi primitives
dominating the final interval width.
