# L-91545 — A no-upward target-Hall output splits into a hereditary positive source measure and a target-null positive row bonus

Claim ID: `L-91545`  
Status: **PROVED EXACT HALL-DISINTEGRATION / TYPE-STABILITY THEOREM**  
Created: 2026-08-13  
Depends on: `L-91454`; normalized component-row monotonicity; `L-91540/L-91543`  
RH status: **unproved pending the merged one-prime producer replay**

## 1. Abstract target-Hall data

Let `E` and `O` be finite or countable sets of positive and negative source
nodes.  At a fixed endpoint let each node carry strictly positive target and
score atoms

\[
 T(n)>0,
 \qquad
 S(n)>0,
 \tag{L-91545.1}
\]

and a nonnegative exact component-row vector

\[
 R(n)=(R_j(n))_{j\ge2}\ge0.
 \tag{L-91545.2}
\]

Put

\[
 q(n)=\frac{T(n)}{S(n)},
 \qquad
 h_j(n)=\frac{R_j(n)}{T(n)}.
 \tag{L-91545.3}
\]

Assume a directed support order `e<=o` on Hall edges and the two monotonicities

\[
 \boxed{
 e\le o
 \Longrightarrow
 q(e)\ge q(o),
 \qquad
 h_j(e)\ge h_j(o)\quad(j\ge2).
 }
 \tag{L-91545.4}
\]

The first is the target-per-score monotonicity of `L-91454`; the second is the
normalized component-row monotonicity.

Let the signed source coefficients be

\[
 a_e\ge0\quad(e\in E),
 \qquad
 b_o\ge0\quad(o\in O).
 \tag{L-91545.5}
\]

A target-Hall transport is a nonnegative matrix `t_(o,e)` satisfying

\[
 \boxed{
 \sum_e t_{o,e}=b_oT(o),
 \qquad
 \sum_o t_{o,e}\le a_eT(e),
 \qquad
 t_{o,e}>0\Longrightarrow e\le o.
 }
 \tag{L-91545.6}
\]

Thus every odd target demand is matched and no even target capacity is
overdrawn.

## 2. The hereditary residual source measure

Define the residual coefficient at an even node by

\[
 \boxed{
 c_e
 =a_e-\frac1{T(e)}\sum_o t_{o,e}\ge0.
 }
 \tag{L-91545.7}
\]

This is an ordinary positive source measure on the **same target/score kernel
type** as the incoming branch.  No matched edge is retained in its source
ledger.

Its target is exactly the signed target:

\[
\begin{aligned}
 \sum_e c_eT(e)
 &=\sum_ea_eT(e)-\sum_{o,e}t_{o,e}\\
 &=\sum_ea_eT(e)-\sum_ob_oT(o).
\end{aligned}
\]

Hence

\[
 \boxed{
 T(c)=T(E)-T(O).
 }
 \tag{L-91545.8}
\]

The target-bearing output of Hall is therefore a genuine positive source
measure, not merely a positive row vector.

## 3. The residual source is score-superordinate

Using `S=T/q`,

\[
\begin{aligned}
 S(c)-[S(E)-S(O)]
 &=\sum_{o,e}t_{o,e}
   \left(\frac1{q(o)}-\frac1{q(e)}\right).
\end{aligned}
\tag{L-91545.9}
\]

Every summand is nonnegative by (L-91545.4).  Therefore

\[
 \boxed{
 S(c)\ge S(E)-S(O).
 }
 \tag{L-91545.10}
\]

All recursively useful target is carried by a source whose score is already at
least the signed branch score.  No matched-edge score debt is inherited.

## 4. The row difference is a target-null positive bonus

The signed component row minus the row of the residual source is

\[
\begin{aligned}
 &[R(E)-R(O)]_j-R_j(c)\\
 &\quad=
 \sum_{o,e}t_{o,e}
 \left(
  \frac{R_j(e)}{T(e)}-
  \frac{R_j(o)}{T(o)}
 \right).
\end{aligned}
\tag{L-91545.11}
\]

Hence define

\[
 \boxed{
 B_j=\sum_{o,e}t_{o,e}[h_j(e)-h_j(o)]\ge0.
 }
 \tag{L-91545.12}
\]

Then, coefficientwise in every exact finite row,

\[
 \boxed{
 R(E)-R(O)=R(c)+B,
 \qquad B\ge0.
 }
 \tag{L-91545.13}
\]

The bonus `B` has no target source mass: all target is already accounted for by
`c`.  It is a current-generation positive row packet and is never propagated as
a child type.

This is the precise source/row distinction missing from the earlier
all-generation formulation.

## 5. Application to the binary survival and hazard branches

For the frozen one-prime target-Hall theorem `L-91454`, both branches satisfy
(L-91545.4):

```text
survival: q_s increasing and alpha_s>=1;
hazard:   q_h increasing and alpha_h>=1;
rows:     Q_Y(j)/(alpha sqrt(Y)-1) increasing.
```

Apply Sections 1--4 separately to the disjoint survival and hazard labels.  One
obtains positive residual source measures

\[
 c_s,
 \qquad
 c_h,
 \tag{L-91545.14}
\]

of the survival and hazard paired types, together with target-null positive row
bonuses `B_s,B_h`, such that

\[
 \boxed{
 T(c_s)+T(c_h)=T_{\rm parent},
 }
 \tag{L-91545.15}
\]

\[
 \boxed{
 S(c_s)+S(c_h)\ge S_s+S_h\ge S_{\rm parent},
 }
 \tag{L-91545.16}
\]

and

\[
 \boxed{
 R_{\rm signed,parent}
 =R(c_s)+R(c_h)+B_s+B_h,
 \qquad B_s,B_h\ge0,
 }
 \tag{L-91545.17}
\]

in the exact one-prime normalization of `L-91454`.

## 6. Type stability without colored Hall recursion

The target-bearing outputs `c_s,c_h` are ordinary positive source measures in
the paired type class of `L-91540`.  The Hall transports themselves and their
matched-edge labels are finished; only `c_s,c_h` are propagated.

Now apply `L-91543`:

```text
hazard residual source -> affine child at X/p <= X/67;
survival residual source -> deterministic positive 67-split;
Hall row bonuses -> current generation only.
```

Both target-bearing children are at endpoint at most `X/67`, their target
weights sum to at most one, and every other term is a nonnegative current row.
No unique-next-prime color, repeated Hall disintegration, or return to the
single common `W_Psi/W_S` measure cone is required.

Thus the recursive source-identification gate left open in `L-91454` is removed.

## 7. Countable version

For a countable Hall graph, truncate to finitely many odd demands and even
capacities.  All transported masses, residual measures and row bonuses are
nonnegative.  Monotone convergence gives (L-91545.8)--(L-91545.13) whenever the
parent target is finite.

## 8. Boundary

This theorem proves the abstract and source-faithful decomposition of any
no-upward target-Hall output.  Its application to the factor-54 route still
requires that the frozen directed Hall certificates and their row atoms are
replayed against the current live `P_61/P_79` branch at identical normalization.

```text
positive hereditary Hall residual source           EXACT
residual target exactness                           EXACT
residual score superordination                      EXACT
matched-edge target-null row bonus                  EXACT
binary branch type stability                        CLOSED
ordered-prime Hall color propagation                NOT NEEDED
merged live one-prime certificate replay             REQUIRED
Riemann Hypothesis                                  UNPROVEN
```
