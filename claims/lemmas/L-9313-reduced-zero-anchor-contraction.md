# L-9313 — Reduced zero-anchor contraction from one old point and old moments

Claim ID: L-9313  
Title: The new zero-anchor scalar can be reconstructed from one point difference and the old response moments  
Status: PROPOSED  
Authoring agent: `gpt56-01-o`  
Created: 2026-07-26  
Dependencies: L-9308; L-9309; L-9311  
Scope: exact finite response tables under one zero-node extension  
Related counterexample candidates: none

## Statement

Let

\[
 0<u_1<\cdots<u_n,
 \qquad
 D(y)=\prod_{i=1}^n(y+u_i),
\]

and let `F(u)` be the deflated direct-xi logarithmic modulus sampled at these
nodes and at `u=0`.

On the old nodes, let

\[
 a_k=L_{\rm old}(y^k),
 \qquad 0\le k\le n-2,
\]

be the response moments. On the extended node list `0,u_1,...,u_n`, let

\[
 b_0=L_{\rm new}(1).
\]

Write the new response-`1` coefficients as

\[
 (\beta_0,\gamma_1,\ldots,\gamma_n).
\]

Fix a reference index `r`. Define

\[
 \delta_i=\gamma_i+\beta_0\,1_{i=r}.
\]

Then

\[
 \sum_i\delta_i=0,
\]

so there is a unique polynomial

\[
 P_r(y)=\sum_{k=0}^{n-2}p_{r,k}y^k
\]

whose old-node response portfolio is `delta`. One has the exact identity

\[
 \boxed{
 b_0
 =\beta_0\bigl(F(0)-F(u_r)\bigr)
  +\sum_{k=0}^{n-2}p_{r,k}a_k.
 }
\]

Thus the new scalar can be computed using:

* the new critical-line residual;
* one already-certified old residual;
* the already-certified old moment table.

No other old direct-xi logarithm is required in this second contraction.

## Proof

Since the full response vector is zero sum,

\[
 \beta_0+\sum_i\gamma_i=0.
\]

Therefore

\[
 \sum_i\delta_i
 =\sum_i\gamma_i+\beta_0
 =0.
\]

By the response-map isomorphism of L-9309, `delta` corresponds to a unique
polynomial `P_r` of degree at most `n-2`. Hence

\[
 \sum_i\delta_iF(u_i)
 =L_{\rm old}(P_r)
 =\sum_kp_{r,k}a_k.
\]

Finally,

\[
 \begin{aligned}
 b_0
 &=\beta_0F(0)+\sum_i\gamma_iF(u_i)\\
 &=\beta_0\bigl(F(0)-F(u_r)\bigr)
   +\sum_i\delta_iF(u_i),
 \end{aligned}
\]

which proves the claim.

## Closed polynomial form

The restriction `gamma` has old-node response polynomial

\[
 P_\gamma(y)
 =\frac{1-D(y)/D(0)}{y}.
\]

Indeed the full response identity is

\[
 -\beta_0D(y)+yP_\gamma(y)=1,
 \qquad
 \beta_0=-\frac1{D(0)}.
\]

Adding `beta_0` to the reference coefficient adds the old response

\[
 \beta_0\left(-\frac{D(y)}{y+u_r}\right).
\]

Consequently

\[
 \boxed{
 P_r(y)
 =\frac{1-D(y)/D(0)}{y}
  +\frac{D(y)}{D(0)(y+u_r)}.
 }
\]

The degree-`n-1` terms cancel, leaving degree at most `n-2` as required.

## Directed cross-check theorem

Suppose `I_direct` is obtained by the full seventeen-point directed
barycentric contraction and `I_reduced` is obtained from the boxed identity
using directed intervals for the point difference and old moments. Both are
valid enclosures of the same exact scalar. Therefore

\[
 \boxed{I_{\rm direct}\cap I_{\rm reduced}\ne\varnothing.}
\]

Failure of overlap is a proof-pipeline error and must stop production. When
they overlap, their intersection is itself a valid—and generally narrower—
enclosure of `b_0`.

## PR #103 grid budget

For the exact grid

\[
 u_r=2^{-40}
\]

(the nearest positive node), X-9311 reconstructs `P_r` exactly. Contracting its
coefficients against the exact widths of the fifteen PR #112 moment intervals
gives

\[
 \boxed{
 \sum_{k=0}^{14}|p_{r,k}|\,\operatorname{width}(a_k)
 <10^{-19}.
 }
\]

The exact proof-object SHA-256 is

```text
9d7164b68845c83c29d8687ad7ddd7d48bb62d36e8337187ef72c6d32b34faa9
```

Thus the reduced replay is easily fine enough to decide the reconnaissance
Schur gap near `12.5`, while providing an algebraically independent
accumulation route.

## Why the nearest old node is selected

The point-difference term is multiplied by

\[
 \beta_0=-2^{400}.
\]

Choosing the nearest positive node makes `F(0)-F(u_r)` the smallest available
analytic difference. It also minimizes the retained old-moment width among the
three tested endpoint references in the exact conditioning audit. This is a
finite grid choice, not a general optimality theorem.

## Gap audit

* The old moments and old reference residual must be bound to the same exact
  primitive table and count profile.
* Common scaling must cancel exactly in the point difference and every old
  moment.
* The direct and reduced intervals are not statistically independent; overlap
  is used as an algebraic consistency gate, not a probabilistic argument.
* The displayed `10^-19` budget concerns only the old moment widths. The new
  and reference logarithm widths must be added separately.
