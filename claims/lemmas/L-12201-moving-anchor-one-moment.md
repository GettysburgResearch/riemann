# L-12201 — Moving-anchor one-moment extension

Claim ID: L-12201  
Title: Adding any positive response node raises the degree by one while introducing exactly one new shifted moment  
Status: PROPOSED  
Authoring agent: `gpt56-05-j`  
Created: 2026-07-26  
Dependencies: L-9308; L-9309; the response-map notation of L-9311  
Scope: exact finite direct-completed-xi logarithmic response tables  
Related counterexample candidates: none

## Statement

Let

\[
 0<u_1<\cdots<u_n
\]

be distinct old nodes and let

\[
 D(y)=\prod_{i=1}^{n}(y+u_i).
\]

Fix a new exact node

\[
 t>0,\qquad t\notin\{u_1,\ldots,u_n\},
\]

and use the shifted spectral coordinate

\[
 z=y+t.
\]

For every polynomial `P` of degree at most `n-2`, let `L_old(P)` denote the old response contraction supplied by the unique zero-sum portfolio whose response polynomial is `P`. Define the old shifted moments

\[
 A_k=L_{\rm old}(z^k)
     =\sum_{j=0}^{k}\binom{k}{j}t^{k-j}a_j,
 \qquad 0\le k\le n-2,
\]

where `a_j=L_old(y^j)`.

Adjoin `t` to the node table. Its denominator is

\[
 \widetilde D(y)=(y+t)D(y)=zD(y).
\]

Let `c_0,...,c_(n-1)` be the new response moments whose response polynomials are

\[
 1,z,z^2,\ldots,z^{n-1}.
\]

Then

\[
 \boxed{c_{k+1}=A_k\qquad(0\le k\le n-2).}
\]

Thus the complete degree-`n-1` response table after adding `t` contains exactly one new scalar, `c_0`.

## Proof

Let `beta^(k)` be the old zero-sum portfolio with response polynomial

\[
 P_{\beta^{(k)}}(y)=z^k=(y+t)^k.
\]

Extend it to the new table by assigning coefficient zero to the new node. Its scalar contraction does not change. In the new response map, every old summand acquires the additional denominator factor `y+t=z`; hence the response polynomial becomes

\[
 zP_{\beta^{(k)}}(y)=z^{k+1}.
\]

By uniqueness of the new response portfolio,

\[
 c_{k+1}=L_{\rm old}(z^k)=A_k.
\]

This holds for all `0<=k<=n-2`. The remaining moment `c_0`, corresponding to the constant response polynomial, is not obtained by zero extension and is the sole new scalar. ∎

## Direct coefficient formula

Let `beta_t` be the coefficient of the new node in the new response-`1` portfolio. Then

\[
 \boxed{\beta_t=-\frac1{D(-t)}
 =-\frac1{\prod_i(u_i-t)}.}
\]

If `gamma_i` are the coefficients on the old nodes, their old response polynomial is

\[
 \boxed{
 P_\gamma(y)=\frac{1+\beta_tD(y)}{y+t}.
 }
\]

Indeed the full response identity is

\[
 -\beta_tD(y)+(y+t)P_\gamma(y)=1.
\]

The numerator in the displayed quotient vanishes at `y=-t`, so the quotient is a polynomial of degree at most `n-1`.

## Motivation

L-9311 establishes the special case `t=0`. The arbitrary-node identity permits a cheap moving-anchor search:

1. retain one proof-grade old moment table;
2. choose a new exact horizontal node `t`;
3. evaluate only one new direct completed-xi primitive;
4. reconstruct `c_0`;
5. decide the enlarged degree cone through T-12202.

No full new node table and no new high-dimensional eigensolve are required.

## Analytic domain audit

The lemma is finite interpolation algebra. In direct-xi applications, the logarithmic modulus at every node must be defined, with any completed-xi scale and count-deflation normalization shared exactly. The new node is positive, so no critical-line nonvanishing gate is needed merely to define `log H_T(t)` unless its completed-xi rectangle contains zero.

## Dependency audit

- L-9308 defines the response polynomial.
- L-9309 proves the response-map isomorphism and uniqueness.
- The direct-xi interpretation inherits the canonical-product and count-deflation gates of its parent table.

## Gap audit

- The shifted moments use powers of `z=y+t`, not powers of `y`.
- The identity fails if the old portfolio is not zero-extended.
- `t` must be distinct from every old node.
- A floating evaluation of `c_0` is discovery data only.
- The theorem introduces one scalar but does not by itself prove that the enlarged moment cone is positive.

## Adversarial tests

- Substitute `t=0` and recover `b_(k+1)=a_k` from L-9311.
- Use a three-node rational table and reconstruct every portfolio directly.
- Mutate one shifted binomial coefficient and require the moment identity to fail.
- Assign a nonzero coefficient to the new node and verify that zero-extension is no longer being tested.

## Remaining uncertainty

No algebraic gap is known. The useful numerical conditioning of particular moving anchors is empirical and must be audited separately.

## Suggested next attack

Apply T-12202 to the existing PR #103 moments at a deterministic ladder of positive anchors, beginning with `t in {1,4,16,64,256}` and then scanning every stored ordinate shift.