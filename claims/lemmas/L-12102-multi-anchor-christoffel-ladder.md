# L-12102 — Multi-anchor Christoffel ladder and divided-difference moment reconstruction

Claim ID: L-12102  
Title: Each additional positive direct-xi anchor raises the complete response degree by one and requires one new primitive value  
Status: PROPOSED  
Authoring agent: `gpt56-03-i`  
Created: 2026-07-26  
Dependencies: L-9308; L-9309; L-9310; L-12101  
Scope: finite count-deflated direct-completed-xi response tables  
Related counterexample candidates: none

## Setup

Let the old RH-conditional positive functional be

\[
 L_0(P)=\int_0^\infty P(y)\,d\mu(y),
\]

with known moments

\[
 a_k^{(0)}=L_0(y^k),
 \qquad 0\le k\le d.
\]

Choose pairwise distinct positive anchors

\[
 0<w_1<\cdots<w_m
\]

that are distinct from the old node set. Define the successively transformed
functionals

\[
 L_r(P)=\int_0^\infty
 \frac{P(y)}{\prod_{j=1}^r(y+w_j)}\,d\mu(y),
 \qquad 1\le r\le m,
\]

and moments

\[
 a_k^{(r)}=L_r(y^k).
\]

The direct-xi node table after `r` anchors has response degree `d+r`.

## One new moment per anchor

For every `r>=1`,

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

Thus `m` new anchors raise the complete half-line response degree from `d` to
`d+m` while introducing exactly `m` new primitive scalars.

## Zeroth moments from one Stieltjes function

Define the one-anchor transform

\[
 S(w)=\int_0^\infty\frac{d\mu(y)}{y+w}.
\]

For distinct anchors, let `S[w_1,...,w_r]` be the ordinary divided difference.
Then

\[
 \boxed{
 a_0^{(r)}=(-1)^{r-1}S[w_1,\ldots,w_r].
 }
\]

### Proof

For `r=1` the claim is the definition. Suppose the formula holds at order
`r-1`. The elementary identity

\[
 \frac1{y+v}-\frac1{y+u}
 =\frac{u-v}{(y+u)(y+v)}
\]

shows that one divided difference introduces one additional factor
`-(y+w)^(-1)`. Iteration gives the sign `(-1)^(r-1)` and the complete product.
Equivalently, the explicit formula is

\[
 a_0^{(r)}=
 \sum_{i=1}^r
 \frac{S(w_i)}{\prod_{j\ne i}(w_j-w_i)}.
\]

The displayed expression is positive under RH even though its barycentric
coefficients alternate.

## Anchor-order independence

The product

\[
 \prod_{j=1}^r(y+w_j)
\]

is independent of anchor order. Therefore every final moment is order
independent. A proof-producing checker should exploit this redundancy:

1. construct all moments in increasing-anchor order;
2. construct them again in decreasing-anchor order;
3. require exact equality for rational inputs, or directed interval overlap for
   interval inputs.

Failure is an algebra or provenance error.

## Complete half-line cone after `m` anchors

Put

\[
 D=d+m.
\]

The complete finite response cone is represented by

\[
 H_0^{(m)}=(a_{i+j}^{(m)})_{
 0\le i,j\le\lfloor D/2\rfloor},
\]

\[
 H_1^{(m)}=(a_{i+j+1}^{(m)})_{
 0\le i,j\le\lfloor(D-1)/2\rfloor}.
\]

By the half-line sum-of-squares theorem atomized in L-9310,

\[
 \boxed{
 H_0^{(m)}\succeq0,
 \qquad
 H_1^{(m)}\succeq0
 }
\]

is necessary and sufficient for every real response polynomial of degree at
most `D` that is nonnegative on `[0,infinity)` to have nonnegative value.

If an exact rational vector `c` gives

\[
 c^{\mathsf T}H_0^{(m)}c<0,
\]

then

\[
 P(y)=\left(\sum_i c_i y^i\right)^2
\]

is the explicit nonnegative response witness. If instead

\[
 c^{\mathsf T}H_1^{(m)}c<0,
\]

then the witness is

\[
 P(y)=y\left(\sum_i c_i y^i\right)^2.
\]

## Direct-xi data cost

Every value `S(w_i)` is exactly the one-anchor scalar `b_0` of L-12101. It can
be computed from:

* one new direct completed-xi rectangle at `u=w_i`;
* one old reference residual;
* the already certified old moments.

No new zero-count computation and no reevaluation of old direct-xi points is
required. With `m` anchors, the expensive new primitive count is exactly `m`.

A second, algebraically independent route is the full barycentric contraction on
the old nodes plus all `m` anchors. The direct and sequential divided-difference
intervals must overlap.

## Rational-function Gram interpretation

For any exact coefficients `c_1,...,c_m`,

\[
 \int_0^\infty
 \left|\sum_{j=1}^m\frac{c_j}{y+w_j}\right|^2
 d\mu(y)\ge0
\]

under RH. Its off-diagonal kernel is reconstructed from anchor values alone:

\[
 \boxed{
 \int_0^\infty
 \frac{d\mu(y)}{(y+u)(y+v)}
 =\frac{S(u)-S(v)}{v-u}.
 }
\]

Thus several anchors impose joint consistency conditions that are invisible to
any one-anchor scalar gate. Sequential Christoffel transformation is a
proof-convenient way to encode those joint constraints without evaluating a
derivative on the diagonal.

## Candidate ladder on the PR #103 table

The old table has `d=14`. The moderate rational anchor sequence

\[
 W_7=
 \left(
 \frac18,\frac{3}{16},\frac14,\frac38,
 \frac12,\frac34,1
 \right)
\]

raises the complete response degree to

\[
 14+7=21.
\]

It requires seven new direct-xi points at

\[
 x=\sqrt{w_i}.
\]

The final matrices are both `11 x 11`. Ordinary high-precision reconnaissance
reported in O-12101 gives positive, but small, scale-normalized minimum
eigenvalues. Those values are nominations only; the proof target is an exact
fixed-vector negative interval or complete directed positive-definiteness
certificate.

A cheaper three-point packet

\[
 W_3=\left(\frac18,\frac{3}{16},\frac14\right)
\]

raises the complete degree to seventeen and is suitable as the first directed
end-to-end control.

## Conditioning and honest ranking

Large anchors make raw scalar Schur intervals algebraically tiny because powers
of `w` enter the rank-one direction. Raw `b_0` distance to a boundary must not be
used as a progress metric by itself.

For discovery, O-12101 reports the diagonally normalized matrices

\[
 \widehat H_{ij}=
 \frac{H_{ij}}{\sqrt{H_{ii}H_{jj}}}
\]

and their smallest eigenvalues. This removes common moment scale, but it is still
only a ranking statistic: high-degree moment matrices can become naturally
ill-conditioned even for benign positive measures.

Production must rank candidates by the final directed moat divided by a complete
primitive sensitivity budget, not by a floating determinant or eigenvalue.

## Directed certificate protocol

For a fixed anchor packet:

1. preserve exact rational anchors and source fingerprints;
2. evaluate every new completed-xi point with directed balls at two precisions;
3. compute every one-anchor `S(w_i)` by full and reduced contractions;
4. require contraction overlap and precision nesting;
5. reconstruct all higher transformed moments in two anchor orders;
6. freeze any negative midpoint direction to a rational vector before final
   interval contraction;
7. otherwise prove both moment matrices positive through exact rational LDL plus
   an interval operator moat;
8. reject every zero-touching result.

A strict negative remains subject to independent completed-xi reproduction and
review of L-9308/L-9309/L-9310 and the atomized count-deflation gates.

## Gap audit

1. Every anchor must be positive and distinct from old and new nodes.
2. All one-anchor values must share one ordinate, normalization, count profile,
   and old moment table.
3. Divided differences can strongly amplify primitive widths; candidate packets
   require an explicit sensitivity ledger before production.
4. Anchor-order agreement is an algebraic consistency gate, not statistical
   independence.
5. A positive finite packet closes only its exact degree, table, ordinate, and
   anchors.
6. A small normalized eigenvalue is not a counterexample nomination unless a
   directed fixed-vector upper endpoint is negative.