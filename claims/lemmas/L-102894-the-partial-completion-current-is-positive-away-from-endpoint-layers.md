# L-102894 — The partial-completion current is eventually positive away from endpoint layers

Claim ID: `L-102894`  
Status: **PROVED UNCONDITIONAL PARAMETRIC ASYMPTOTIC**  
Created: 2026-08-24  
Depends on: `L-102891`  
RH status: **not assumed**

Retain the partial-completion observation

\[
H_c(X)
=
\sum_n\frac{\gamma_c(n)}{\sqrt n}R_L(X/n),
\qquad 0<c<1.
\]

Let

\[
K(c)=
\frac{\widehat R_L(1/2)G_c(1)}{\Gamma(c-1)}>0.
\]

The analytic-parameter form of Selberg–Delange gives, uniformly for \(c\) in
any compact interval \(I\Subset(0,1)\),

\[
H_c(X)
=
K(c)X^{1/2}(\log X)^{c-2}
\left(1+O_I(1/\log X)\right),
\tag{L-102894.1}
\]

and the expansion may be differentiated with respect to \(c\).  Therefore

\[
\boxed{
\partial_cH_c(X)
=
K(c)X^{1/2}(\log X)^{c-2}
\left[
\log\log X+rac{K'(c)}{K(c)}+O_I(1/\log X)
\right].
}
\tag{L-102894.2}
\]

Since \(K(c)>0\) and \(K'/K\) is bounded on \(I\),

\[
\boxed{
\partial_cH_c(X)>0
}
\tag{L-102894.3}
\]

for all sufficiently large \(X\), uniformly for \(c\in I\).

Thus the completion homotopy is eventually increasing throughout every fixed
interior temperature interval.  Any conclusion-bearing adverse transfer is
confined to completion-parameter layers which shrink toward the endpoints.

## 1. The native endpoint derivative

The leading coefficient itself has the expansion

\[
\frac1{\Gamma(c-1)}=-c+O(c^2)
\qquad(c\downarrow0).
\]

Since \(G_c(1)=G_0(1)+O(c)\),

\[
K(c)
=
-\widehat R_L(1/2)G_0(1)c+O(c^2),
\]

where

\[
-\widehat R_L(1/2)G_0(1)>0.
\]

Differentiating the parameterized Hankel expansion at \(c=0\) gives

\[
\boxed{
\left.\partial_cH_c(X)\right|_{c=0}
=
-\widehat R_L(1/2)G_0(1)
\frac{\sqrt X}{(\log X)^2}
\left(1+O(1/\log X)\right)>0
}
\tag{L-102894.4}
\]

for sufficiently large \(X\).

So even the infinitesimal positive-completion direction at the native endpoint
has a favorable deterministic main term.

## 2. Exact boundary-layer identity

For every fixed \(0<\varepsilon<1\),

\[
\boxed{
H_0(X)
=
H_\varepsilon(X)
-
\int_0^\varepsilon\partial_cH_c(X)\,dc.
}
\tag{L-102894.5}
\]

The first term is eventually positive by `L-102891`.  Equation
(L-102894.5) identifies the native difficulty with the source-faithful endpoint
current rather than with the bulk completion path.

This does not prove RH: one-sided control of the integral in (L-102894.5) is
precisely a completion-defect estimate.  The theorem shows that the hard
current is a nonuniform endpoint phenomenon; no fixed interior completion
parameter carries the obstruction.
