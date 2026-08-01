# L-17804 — Local-cell and moment-sweep identities for finite spline prime windows

Claim ID: `L-17804`  
Status: **PROVED ALGEBRA; PRODUCTION MPFR IMPLEMENTATION REQUIRES INDEPENDENT CODE AUDIT**  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: `L-17802`, `L-17803`; elementary binomial algebra

## Statement

Let

\[
W(u)=\sum_{\ell=1}^L c_\ell(u-a_\ell)_+^d
\]

with real coefficients and knots, and define

\[
Q_W(x)=\sum_{q=p^r}\frac{\Lambda(q)}{\sqrt q}W(x-\log q).
\]

For `0<=m<=d`, put

\[
M_m(y)=\sum_{\log q\le y}\frac{\Lambda(q)}{\sqrt q}(\log q)^m.
\]

Then exactly

\[
\boxed{
Q_W(x)=\sum_{\ell=1}^L c_\ell
\sum_{m=0}^d(-1)^m{d\choose m}
(x-a_\ell)^{d-m}M_m(x-a_\ell).}
\tag{1}
\]

This is an independent cumulative-moment producer requiring only one sweep of the prime powers and `d+1` running moments.

There is a much better conditioned local producer. Sort the distinct knots as
`kappa_0<...<kappa_(L-1)`. On each cell write

\[
W(\kappa_i+t)=\sum_{m=0}^d b_{i,m}t^m.
\]

If `Delta_i=kappa_(i+1)-kappa_i`, then

\[
\boxed{
b_{i+1,m}=\sum_{j=m}^d {j\choose m}b_{i,j}\Delta_i^{j-m}
+\mathbf1_{m=d}c_{i+1}.}
\tag{2}
\]

Thus every prime-power term is evaluated by one exact cell lookup and one degree-`d` Horner contraction. With outward interval arithmetic, a term is accepted directly whenever its argument interval lies in one cell; a knot crossing is split or hulled.

## Proof

For (1), expand

\[
(y-\log q)^d=\sum_{m=0}^d(-1)^m{d\choose m}y^{d-m}(\log q)^m
\]

inside each positive-part support condition. Equation (2) is the translation identity

\[
\sum_jb_{i,j}(t+\Delta_i)^j
=\sum_m\left[\sum_{j\ge m}{j\choose m}b_{i,j}\Delta_i^{j-m}\right]t^m,
\]

followed by the new knot contribution `c_(i+1)t^d`. QED.

## `J=12`, five-difference specialization

For the exact packet of Issue #193:

- degree `d=23`;
- 32 difference shifts;
- 25 B-spline positive-part terms;
- exactly 800 rational knots for the base filtered spline;
- the pole shift `log 4` is evaluated as a second translated copy, rather than inserted repeatedly into the knot recursion;
- exact translation
  \[
  x=17730793345827/2^{40};
  \]
- exactly 103,384 prime powers in the support annulus.

The all-MPFR local-cell producer has zero ambiguous knot comparisons and emits nested intervals at 256, 320, 384 and 448 bits. The 448-bit interval is recorded in `X-17804`.

## Conditioning audit

At this cell, the global moment expansion has an ordinary condition diagnostic about

\[
3.1\times10^{44},
\]

whereas direct local prime contraction has diagnostic about

\[
3.2\times10^{11}.
\]

These numbers are not proof inputs. They explain why decimal or binary64 B-spline formulas can move the final value by `10^-14`, and why the local-cell recursion is the production representation.

## Proof boundary

- The identities are exact.
- The MPFR interval is proof-grade only after source review, compiler/backend reproduction, and manifest audit.
- The result encloses the prime side only. A zero-phase interval and the `T-15604` comparator are still needed for an RH verdict.
