# Session report — positive-anchor Christoffel ladders beyond the closed scalar cone

Agent: `gpt56-03-i`  
Date: 2026-07-26  
Stacked base: draft PR #117  
Branch: `agent/gpt56-03-i/93-positive-anchor-ladder`  
Status: new theorem and proof checker; three empirical candidate packets; no counterexample

## Executive summary

The newest repository work has closed several previously active finite families:

- the historical `c=10^11`, `K=1024` carrier vector is directed and strictly
  positive;
- the first high-height same-ordinate Pick table contains exact feasible anchors;
- the PR #103 monomial-positive direct-xi portfolio cone is closed by PR #112;
- the entire degree-at-most-14 half-line nonnegative polynomial response cone is
  closed by PR #116;
- the support-gap, screw, and multiscale determinant branches have produced
  positive finite results at their current tables;
- PR #117 reduced the degree-15 zero-anchor extension to one new scalar, but its
  proof workflow had not yet retained a result during this session.

The important lesson is not to optimize harder inside a closed table. The
primitive space must enlarge in a way that preserves finite proof structure.

This session resolves one of PR #117's explicitly `UNVERIFIED` extensions:
adding an arbitrary positive node `w` is a one-moment transform. More
importantly, several positive nodes can be chained. Every new direct-xi value
raises the complete half-line response degree by one.

For the PR #103 table:

```text
old complete degree      14
new positive anchors      m
new direct-xi primitives  m
new complete degree       14+m
new zero-count work        0
```

The branch adds atomic proofs, a standard-library exact checker, positive and
negative rational controls, eight mutation tests, a reproducible ordinary
scout, and three candidate packets.

## 1. Survey of the current frontier

### Carrier route

The multi-billion-term X-2805 pass is complete and the recovered vector is
strictly positive. PR #85 converted that positive direction into a Schur-pivot
program for possible whole-matrix closure. The data no longer support treating
the historical vector as a live negative finalist.

### Same-height xi'/xi route

PRs #67, #68, #71, and #80 show that the strongest negative midpoint modes were
precision ghosts. The current finite value table has exact feasible anchors, so
portfolio optimization on the unchanged table cannot produce a robust negative.

### Direct-xi count-deflated route

This is now the sharpest finite-response frontier.

- PR #103 supplies atomized zero-count deflation and a directed near-boundary
  table.
- PR #112 proves every monomial-positive response basis row nonnegative.
- PR #116 closes every real polynomial response of degree at most 14 that is
  nonnegative on the half-line.
- PR #117 shows that adding `u=0` raises the degree to 15 with one scalar.
- PR #119 demonstrates why raw determinant normalization can be misleading and
  insists on exact completion budgets.

The natural unexplored move is therefore not another polynomial inside the old
sixteen-node table. It is to add new direct-xi nodes while preserving the
one-moment structure.

## 2. L-12101: one positive node, one moment, two gates

Let the old response moments be

\[
 a_k=\int y^k\,d\mu(y).
\]

Adjoining `w>0` gives

\[
 b_k=\int\frac{y^k}{y+w}\,d\mu(y),
\]

and therefore

\[
 a_k=b_{k+1}+wb_k.
\]

All new moments are affine functions of `b0`.

For degree 15, both moment matrices are `8 x 8`. Their dependence on `b0` is

\[
 H_0(b_0)=C_0+b_0zz^T,
\]

\[
 H_1(b_0)=C_1-wb_0zz^T,
\]

with

\[
 z=(1,-w,w^2,\ldots,-w^7)^T.
\]

A positive anchor thus gives a two-sided interval. If `t` is any exact interior
reference,

\[
 t-\frac1{z^TH_0(t)^{-1}z}
 \le b_0\le
 t+\frac1{wz^TH_1(t)^{-1}z}.
\]

Failure below the lower endpoint produces an explicit polynomial-square
witness. Failure above the upper endpoint produces an explicit
`y`-times-square witness.

This is strictly stronger than the zero-anchor gate, where only one matrix
changes.

## 3. Reduced new-point contraction

Write

\[
 D(y)=\prod_i(y+u_i).
\]

The coefficient of the new anchor in the response-1 portfolio is

\[
 \beta_w=-1/D(-w).
\]

Using one old reference node `u_r`, the new scalar is

\[
 b_0=\beta_w(F(w)-F(u_r))+\sum_{k=0}^{14}p_{r,k}a_k,
\]

where

\[
 P_r(y)=
 \frac{1-D(y)/D(-w)}{y+w}
 +\frac{D(y)}{D(-w)(y+u_r)}.
\]

The degree-15 terms cancel exactly. Therefore one new completed-xi primitive,
one old point, and the old directed moment table suffice.

The full extended-node barycentric contraction and reduced contraction must
overlap. This is an algebraic dual replay analogous to L-9313, but valid for
arbitrary positive anchors.

## 4. L-12102: several anchors form a degree ladder

For anchors `w1,...,wm`, define

\[
 L_m(P)=\int
 \frac{P(y)}{\prod_{j=1}^m(y+w_j)}\,d\mu(y).
\]

At each step,

\[
 a_k^{(r-1)}=a_{k+1}^{(r)}+w_ra_k^{(r)}.
\]

The new zeroth moment is a signed divided difference of the one-anchor
Stieltjes transform:

\[
 a_0^{(r)}=(-1)^{r-1}S[w_1,\ldots,w_r],
\qquad
S(w)=\int\frac{d\mu(y)}{y+w}.
\]

Thus `m` direct-xi values determine all moments through order `14+m`. The final
`H0/H1` pair decides the complete degree-`14+m` half-line cone.

The moment output is independent of anchor order. The exact checker reconstructs
it in increasing and decreasing order and requires equality.

## 5. Exact finite checker

X-12101's `verify.py` uses only integers and `Fraction`.

It supports:

- exact anchor divided differences;
- exact recursive moment construction;
- exact order-invariance replay;
- exact Hankel matrix construction;
- fixed rational `H0` and `H1` vector checks;
- exact rational LDL pivots for full positive controls;
- closed check manifests and deterministic digests.

### Positive control

A five-atom positive measure and anchors `1/2,3/2` yield a strictly positive
complete degree-six cone. Digest:

```text
0423469c646627ca5d9c5c2d21bf67638c3e7f36cf8f350b5b92d0aedd2cb196
```

### Negative control

Changing the second one-anchor value by exactly `1/100` yields the rational
witness

```text
(7064, -6917, 1497, -85)
```

with exact quadratic

```text
-987306740595163 / 1734163200.
```

Digest:

```text
3e9234290746c786f22522d0577ac76d4f85c7d4591d7b7156d8dd2d9552d6dc
```

Eight adversarial tests pass.

## 6. Empirical anchor scan

The scout uses the directed PR #112 old moments at their midpoints and ordinary
50--60 digit Riemann--Siegel evaluation for new points. It reproduces PR #117's
zero-anchor midpoint gap, providing a normalization check.

No tested anchor or packet was negative.

### Why large-anchor tiny gaps were rejected as fake progress

At anchors `w=1,2,8,32`, the lower scalar boundary distances are approximately

```text
4.05e-6
5.88e-9
5.95e-16
4.82e-24.
```

This collapse is mainly algebraic: the rank-one direction contains powers of
`w`. It is not evidence for an off-line zero.

The report therefore uses diagonally normalized moment matrices only as a
ranking statistic, and preserves the warning that even this statistic can
shrink naturally with degree.

## 7. Candidate packets

### PA-1

```text
anchors       {1}
new points    1
final degree  15
```

Empirical two-sided distances:

```text
lower  4.0503336772e-6
upper  1.4585952792e-5.
```

This is the cheapest positive-anchor directed control. Since `w=1`, the new
point has real part `3/2`, which is computationally attractive.

### PA-3

```text
anchors       {1/8, 3/16, 1/4}
new points    3
final degree  17
```

Normalized minima:

```text
H0  3.7035390171e-11
H1  1.7756286345e-10.
```

PA-3 is the recommended first joint directed packet.

### PA-7

```text
anchors       {1/8,3/16,1/4,3/8,1/2,3/4,1}
new points    7
final degree  21
matrices      11 x 11, 11 x 11
```

Ordinary midpoint values:

```text
raw min H0         1.0255423430e-8
raw min H1         3.1927594705e-8
normalized min H0  3.8037205202e-13
normalized min H1  2.6692027329e-12.
```

PA-7 is not a negative candidate. It is a scale-balanced candidate table that
substantially enlarges the finite cone with seven new primitives.

## 8. Best computation handoffs

1. Run PA-1 first at 512/640 bits to validate the two-sided theorem and direct
   versus reduced overlap.
2. Run PA-3 at the current center.
3. Reuse PA-3 across the 65 exact PR #103 shifts; this changes the ordinate
   dimension rather than overfitting one center.
4. Escalate only the strongest directed packet to PA-7.
5. If every packet is positive, close the corresponding degree cone and use its
   exact Schur margin to rank the next ordinate window.

The seven-point calculation requires no new zero counts and can share one
patched completed-xi producer invocation.

## 9. Honest boundary

- No directed new-anchor value was computed.
- No negative Riemann-xi matrix or response was found.
- No `Z-####` candidate is allocated.
- The old directed intervals are used only through their midpoints in the scout.
- A future negative requires a fixed rational witness, outward primitive
  contraction, independent completed-xi reproduction, and review of all
  inherited response and count-deflation gates.

The contribution is a new exact search architecture and a concrete, inexpensive
candidate ladder—not an RH conclusion.