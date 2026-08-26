# L-102734 — Ratio-eight centering improves the one-octave stress contraction to `0.6882`

Claim ID: `L-102734`  
Status: **PROVED EXACT FUNCTIONAL-ANALYTIC THEOREM**  
Created: 2026-08-23  
Depends on: `L-102732`; PR #715 `L-102502`  
RH status: **not assumed**

Let `F` be any carrier-recombined centered filtered packet whose source
products lie in one multiplicative octave

\[
 e^a\le n<2e^a.
\]

By `L-102732`, every centered ray kernel is supported in `[1,8]`.  Therefore
`F(e^u)` is supported in one logarithmic interval of length at most

\[
 \log2+\log8=4\log2.
\]

Put

\[
 C=\partial_uF,
 \qquad
 X_1=\frac12(\partial_u+\tfrac32)F.
\]

The endpoint vanishing gives

\[
 \langle \partial_uF,F\rangle=0,
\]

and hence

\[
 \|X_1\|^2
 =\frac14\|C\|^2+\frac9{16}\|F\|^2.
 \tag{L-102734.1}
\]

Poincare on an interval of length `4 log 2` yields

\[
 \|F\|^2
 \le
 \frac{16(\log2)^2}{\pi^2}\|C\|^2.
\]

Consequently

\[
 \boxed{
 \|X_1\|^2
 \le
 \kappa_8\|C\|^2,
 \qquad
 \kappa_8
 =\frac14+\frac{9(\log2)^2}{\pi^2}.
 }
 \tag{L-102734.2}
\]

Numerically,

\[
 \boxed{
 \kappa_8=0.6881206124\ldots<0.689.
 }
 \tag{L-102734.3}
\]

Thus the exact diagonal reserve is

\[
 1-\kappa_8>0.3118.
\]

The earlier uncentered common-mother support `[1,16]` gave the weaker constant
`0.934563...`.  Exact affine-carrier subtraction therefore more than
quadruples the available contraction gap.

This is a deterministic theorem for arbitrary coefficients.  It controls the
local CV/XD geometry but does not create arithmetic one-sided cancellation by
itself.