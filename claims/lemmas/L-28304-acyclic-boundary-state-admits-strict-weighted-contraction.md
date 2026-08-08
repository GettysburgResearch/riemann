# L-28304 — Acyclic boundary states admit a strict weighted contraction

Claim ID: `L-28304`  
Title: Finite block systems with contractive diagonal loops and an acyclic off-diagonal graph have a weighted sum norm with strict operator reserve  
Status: **PROPOSED COMPLETE FINITE-DIMENSIONAL LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Scope: abstract finite-state adapter for BJPR/RBJC; no arithmetic hypothesis and no RH conclusion

## 1. Statement

Let

\[
 \mathcal X=X_1\oplus\cdots\oplus X_d
\]

be a finite direct sum of normed spaces.  Let `T=(T_(ij))` be a bounded block
operator.  Form the directed graph with an edge

\[
 j\longrightarrow i
\]

whenever `i!=j` and `T_(ij)` is nonzero.

Assume:

1. the off-diagonal graph is acyclic;
2. every diagonal block is strictly contractive,
   \[
   \|T_{ii}\|\le\alpha_i<1.
   \tag{L-28304.1}
   \]

Then, for every

\[
 \max_i\alpha_i<\theta<1,
 \tag{L-28304.2}
\]

there exist positive weights `w_1,...,w_d` such that the weighted sum norm

\[
 \|x\|_w=\sum_{i=1}^dw_i\|x_i\|_{X_i}
 \tag{L-28304.3}
\]

satisfies

\[
 \boxed{
 \|Tx\|_w\le\theta\|x\|_w
 \qquad(x\in\mathcal X).
 }
 \tag{L-28304.4}
\]

No smallness assumption is imposed on the off-diagonal block norms.

## 2. Proof by topological weighting

Choose a topological ordering so that every off-diagonal edge points from a
smaller index to a larger index:

\[
 T_{ij}=0
 \qquad(i<j,\ i\ne j).
 \tag{L-28304.5}
\]

For an input in block `j`, the weighted column contribution is bounded by

\[
 {1\over w_j}
 \sum_{i=1}^{d}w_i\|T_{ij}\|.
 \tag{L-28304.6}
\]

Set `w_1=1`.  Having chosen `w_1,...,w_(j-1)`, choose `w_j>0` recursively so
small that, for every earlier input column `r<j`, the new contribution obeys

\[
 {w_j\|T_{jr}\|\over w_r}
 \le {\theta-\alpha_r\over2^{j-r+1}}.
 \tag{L-28304.7}
\]

This is possible because only finitely many inequalities are present and their
left sides tend to zero with `w_j`.

For a fixed input column `r`, the diagonal contribution is at most `alpha_r`,
while summing (L-28304.7) over `j>r` gives less than

\[
 {\theta-\alpha_r\over2}.
\]

If desired, replace the denominator in (L-28304.7) by a normalized finite
geometric ledger so that the sum is at most `theta-alpha_r`; then

\[
 {1\over w_r}
 \sum_iw_i\|T_{ir}\|
 \le\theta.
 \tag{L-28304.8}
\]

Summing the block estimates proves (L-28304.4).

An equivalent reverse recursion applies if the chosen topological ordering
points from larger indices to smaller indices.

## 3. Quantitative rational version

If every block norm has a rational upper bound and every `alpha_i,theta` is
rational, the weights may be chosen rational.  One may take, successively,

\[
 w_j
 =\min\left(
 1,
 \min_{r<j:T_{jr}\ne0}
 {w_r(\theta-\alpha_r)
  \over 2^{j-r+1}(1+\|T_{jr}\|)}
 \right).
 \tag{L-28304.9}
\]

A production checker can therefore emit:

```text
finite state list;
directed transition manifest;
proof that the off-diagonal graph is acyclic;
rational block-norm enclosures;
rational diagonal reserves;
rational weights;
exact weighted column sums below theta.
```

## 4. Acyclic export with lower-scale sinks

Suppose some off-diagonal states are exported to a strict lower-scale reservoir
rather than returned to the current state space.  Add one sink block with zero
diagonal and do not include its output in the current-scale norm.  The same
argument proves strict current-scale contraction; the sink is charged separately
in the scale recurrence.

Thus an arbitrary finite amount of forward jet generation is harmless if it is
acyclic and eventually exits to lower scale.

## 5. Consequence for the boundary-jet programme

The current exact state typing is:

```text
shifted analytic bulk                 diagonal <=6/7;
eta boundary residual/dipoles         diagonal <=theta_*<1;
Euler top remainder                   diagonal <=2^-M;
positive Peano derivative order       moves strictly upward in jet order;
strict half-scale exports             leave the current state;
zeroth endpoint collar                possible return channel.
```

Therefore every nonzeroth jet coupling can be absorbed into a strict weighted
norm once its transition graph is shown to be acyclic.  The sizes of those
couplings do not need independent small-constant estimates.

The only possible obstruction to the abstract contraction is a directed cycle
which passes through the zeroth collar or another retained bottom state.  This
reduces BJPR/RBJC to a finite cycle-exclusion or cycle-reserve theorem rather
than a complete collection of unrelated jet estimates.

## 6. Proof boundary

Closed exactly:

- strict weighted contraction for every finite acyclic block system;
- a rational proof-producing version;
- lower-scale sink handling;
- elimination of off-diagonal size as an independent obstruction.

Open in the RH application:

- the exact arithmetic transition graph for all common-destination endpoint
  rows;
- exclusion or strict reserve of cycles through the zeroth collar;
- BJPR and RH.
