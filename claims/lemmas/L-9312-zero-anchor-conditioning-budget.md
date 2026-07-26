# L-9312 — Exact conditioning budget for the PR #103 zero anchor

Claim ID: L-9312  
Title: The zero-anchor barycentric contraction has exact condition factor below `2^402`  
Status: PROPOSED  
Authoring agent: `gpt56-01-o`  
Created: 2026-07-26  
Dependencies: L-9311  
Scope: the exact seventeen-node grid `u=0,2^-40,2^-38,...,2^-10`  
Related counterexample candidates: none

## Statement

Let

\[
 u_0=0,
 \qquad
 (u_1,\ldots,u_{16})
 =(2^{-40},2^{-38},\ldots,2^{-10}),
\]

and let

\[
 \beta_i
 =-
 \frac{1}{\displaystyle\prod_{j\ne i}(u_j-u_i)}
\]

be the response-`1` portfolio from L-9311. Define

\[
 \kappa=\sum_{i=0}^{16}|\beta_i|.
\]

Then exact rational arithmetic gives

\[
 \boxed{\beta_0=-2^{400}}
\]

and

\[
 \boxed{\kappa<2^{402}.}
\]

Consequently, if directed residual intervals satisfy

\[
 F_i\in[m_i-r_i,m_i+r_i],
\]

then the zero-anchor scalar

\[
 b_0=\sum_i\beta_iF_i
\]

has radius at most

\[
 \boxed{
 \operatorname{rad}(b_0)
 \le\sum_i|\beta_i|r_i.
 }
\]

In particular, under a uniform radius bound `r_i <= 2^-p`,

\[
 \boxed{
 \operatorname{rad}(b_0)<2^{402-p}.
 }
\]

## Proof of the radius inequality

Write

\[
 F_i=m_i+e_i,
 \qquad |e_i|\le r_i.
\]

Then

\[
 \left|b_0-\sum_i\beta_im_i\right|
 =\left|\sum_i\beta_ie_i\right|
 \le\sum_i|\beta_i|r_i.
\]

This is exact and independent of the accumulation order.

## Exact critical-line coefficient

The denominator of the coefficient at `u_0=0` is

\[
 \prod_{i=1}^{16}u_i
 =\prod_{k=5}^{20}2^{-2k}
 =2^{-2\sum_{k=5}^{20}k}.
\]

Since

\[
 \sum_{k=5}^{20}k
 =\frac{(5+20)16}{2}
 =200,
\]

one obtains

\[
 \beta_0=-2^{400}.
\]

This explains the roughly 120-decimal-digit cancellation in the ordinary
reconnaissance computation.

## Exact `l1` certificate

The remaining inequality is finite rational arithmetic. X-9310 reconstructs
all seventeen coefficients using `fractions.Fraction`, sums their absolute
values exactly, and verifies

```text
kappa < 2^402.
```

The retained exact proof object has SHA-256

```text
b83841684a72c87c998d231bcc922d2e24f522836f7ee18936aca0075d0278e7
```

No floating approximation is used in this comparison.

## Production implication

The X-9309 workflow evaluates the new critical-line primitive at 512 and 640
bits. The exact checker measures the actual logarithmic interval radii, but the
present theorem supplies a planning gate:

* residual radii below `2^-420` force `rad(b0)<2^-18`;
* residual radii below `2^-450` force `rad(b0)<2^-48`;
* residual radii below `2^-500` force `rad(b0)<2^-98`.

Thus the apparent positive Schur gap near `12.5` does not require thousands of
bits. It requires correct directed arithmetic and at least about 420 reliable
bits in every residual channel.

## Gap audit

* The bound concerns interval width, not analytic correctness of the direct-xi
  rectangles.
* Common scale cancellation must be exact before applying the budget.
* Correlations could make the true uncertainty smaller, but they are not used.
* A midpoint agreement at two precisions is not a substitute for directed
  residual intervals.
