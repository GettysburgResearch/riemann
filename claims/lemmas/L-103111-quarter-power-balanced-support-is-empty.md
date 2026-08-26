# L-103111 — The quarter-power balanced equal-pair source is support-empty

Claim ID: `L-103111`  
Status: **PROVED EXACT SUPPORT THEOREM**  
Created: 2026-08-26  
Depends on: PR #751 `L-106080`, `L-106132`, `L-106133`; support of `K_L`  
RH status: **not assumed**

On one source block

\[
Y\le X<2Y,
\qquad A\le P<2A,
\]

put

\[
V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

Every nonzero coefficient of

\[
\mathcal B_{V_A}
=a_{V_A}\star a_{V_A}\star\mu_{\rm sf}
\]

contains two disjoint core factors `r,s>V_A`. Hence its literal completed core
satisfies

\[
a\ge rs\ge(V_A+1)^2
\]

and

\[
a^2>(2Y/A).
\]

For the canonical owner product `P>=A`, the physical integer is

\[
N=Pa^2>2Y>X.
\]

Because the fixed derivative kernel is supported in `[1,8]`,
`K_L(X/N)` can be nonzero only if `N<=X`. Therefore

\[
\boxed{
\mathcal O_{K_L}
 [\Pi_A\mathfrak B_{V_A}^{\rm eq}](X)=0
\qquad(Y\le X<2Y).
}
\tag{L-103111.1}
\]

The statement is coefficientwise, survives every fixed differential image of
the common mother, and uses no cancellation.

## Scope

The theorem removes the quarter-power balanced term. It does not estimate the
coherent physical collapse of the complementary pair-indexed Type-I term.
That exact distinction is binding in `R-103110`.