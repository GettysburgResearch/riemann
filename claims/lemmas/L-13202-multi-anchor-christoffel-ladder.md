# L-13202 — Multi-anchor Christoffel ladder and divided-difference reconstruction

Claim ID: L-13202  
Title: Each positive direct-xi anchor raises the complete finite response degree by one while adding one primitive scalar  
Status: PROPOSED  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-9308, L-9309, L-9310, L-13201  
Scope: finite count-deflated direct-completed-xi response tables  
Related counterexample candidates: none

> Canonical-ID note: this claim supersedes the temporary authoring ID
> `L-12102`, withdrawn after concurrent PR #125 allocated that identifier.

## Statement

Let

\[
 L_0(P)=\int_0^\infty P(y)\,d\mu(y)
\]

for a positive measure `mu`, and suppose the moments

\[
 a_k^{(0)}=L_0(y^k),\qquad 0\le k\le d,
\]

are known. Choose pairwise distinct positive anchors

\[
 0<w_1<\cdots<w_m
\]

distinct from the old node set. Define

\[
 L_r(P)=\int_0^\infty
 \frac{P(y)}{\prod_{j=1}^r(y+w_j)}\,d\mu(y),
 \qquad
 a_k^{(r)}=L_r(y^k).
\]

Then for every `r>=1`,

\[
 \boxed{
 a_k^{(r-1)}=a_{k+1}^{(r)}+w_r a_k^{(r)}
 }
 \qquad(0\le k\le d+r-1).
\]

Consequently, once the single scalar `a_0^(r)` is known, all moments through
order `d+r` follow from

\[
 \boxed{
 a_{k+1}^{(r)}=a_k^{(r-1)}-w_r a_k^{(r)}.
 }
\]

Thus `m` anchors raise the complete half-line response degree from `d` to
`d+m` while introducing exactly `m` new primitive scalars.

## Zeroth moments as divided differences

Define the one-anchor Stieltjes value

\[
 S(w)=\int_0^\infty\frac{d\mu(y)}{y+w}.
\]

For distinct anchors, let `S[w_1,...,w_r]` denote the ordinary divided
difference. Then

\[
 \boxed{
 a_0^{(r)}=(-1)^{r-1}S[w_1,\ldots,w_r].
 }
\]

### Proof

The recurrence follows from

\[
 y^k=(y+w_r)y^k-w_ry^k
\]

after division by the complete denominator and integration.

For the divided-difference formula, the identity

\[
 \frac{1}{y+v}-\frac{1}{y+u}
 =\frac{u-v}{(y+u)(y+v)}
\]

shows that one divided difference inserts one additional denominator factor and
one minus sign. Iterating `r-1` times gives the formula. ∎

## Anchor-order invariance

The final denominator

\[
 \prod_{j=1}^m(y+w_j)
\]

is symmetric in the anchors. Therefore every final moment is independent of the
order in which the recurrences are applied. A proof-producing checker should
construct the final moment list in at least two deterministic anchor orders and
require exact equality for rational data or directed overlap for interval data.

## Complete finite cone

Put `D=d+m`. Define

\[
 H_0^{(m)}=(a_{i+j}^{(m)})_
 {0\le i,j\le\lfloor D/2\rfloor},
\]

\[
 H_1^{(m)}=(a_{i+j+1}^{(m)})_
 {0\le i,j\le\lfloor(D-1)/2\rfloor}.
\]

By L-9310,

\[
 H_0^{(m)}\succeq0,
 \qquad
 H_1^{(m)}\succeq0
\]

is necessary and sufficient for every real response polynomial of degree at
most `D` that is nonnegative on `[0,infinity)` to have nonnegative value.

A rational vector `c` with

\[
 c^{\mathsf T}H_0^{(m)}c<0
\]

gives the explicit response witness

\[
 P(y)=\left(\sum_i c_i y^i\right)^2.
\]

A negative `H_1` quadratic gives

\[
 P(y)=y\left(\sum_i c_i y^i\right)^2.
\]

## Direct-xi primitive cost

Each `S(w_i)` is the one-anchor scalar of L-13201. It can be reconstructed from
one new direct completed-xi rectangle, one old reference residual, and the
already certified old moments. No new zero-count calculation and no
reevaluation of old direct-xi points is required.

The full contraction on all old and new nodes supplies an algebraically distinct
replay. Sequential and full contractions must overlap before a sign is trusted.

## Rational-function Gram interpretation

For exact coefficients `c_1,...,c_m`, RH implies

\[
 \int_0^\infty
 \left|\sum_{j=1}^m\frac{c_j}{y+w_j}\right|^2d\mu(y)\ge0.
\]

The off-diagonal kernel is determined by anchor values:

\[
 \boxed{
 \int_0^\infty\frac{d\mu(y)}{(y+u)(y+v)}
 =\frac{S(u)-S(v)}{v-u}.
 }
\]

Hence several anchors impose joint consistency conditions invisible to any
single-anchor interval.

## PR #103 specialization

The old table has `d=14`. The moderate packet

\[
 W_3=(1/8,3/16,1/4)
\]

raises the complete degree to seventeen using three new direct-xi values. The
packet

\[
 W_7=(1/8,3/16,1/4,3/8,1/2,3/4,1)
\]

raises it to twenty-one using seven new values; both final matrices are
`11 x 11`.

## Proof boundary

- Anchors must be positive, distinct, and source-bound to one ordinate,
  normalization, count profile, and old moment table.
- Divided differences can amplify primitive widths; production requires a
  complete sensitivity ledger.
- A floating minimum eigenvalue is only a vector nomination. The final object is
  a directed rational fixed-vector sign or interval positive-definiteness proof.
- A strict negative still requires independent completed-xi reproduction and
  review of the inherited response and count-deflation implications.
