# L-93284 - Explicit two-row Riesz filters and the large-prime smooth-reservoir reduction

Claim ID: `L-93284`  
Status: **PROPOSED COMPLETE EXACT REDUCTION - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93283`; the canonical row formula of PR #542  
Scope: exact physical producer formulas; positivity is not claimed

## 1. One Mobius Riesz state

Put

\[
R_\mu(X)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}\log\frac Xn,
\qquad R_\mu(X)=0\quad(X<1).
\tag{L-93284.1}
\]

The two fixed rows are exactly

\[
\boxed{
\begin{aligned}
c_X(2)={}&\log X-R_\mu(X)
+\sqrt2R_\mu(X/2)-\frac1{\sqrt3}R_\mu(X/3),\\
c_X(3)={}&\frac13\log X-\frac13R_\mu(X)
-\frac1{3\sqrt2}R_\mu(X/2)\\
&+\frac5{3\sqrt3}R_\mu(X/3)-\frac12R_\mu(X/4).
\end{aligned}
}
\tag{L-93284.2}
\]

Thus the direct consumer requires only two finite scale filters of one scalar
Mobius state.

## 2. Removing the small-prime front

Let `mu_>3` be the multiplicative sequence whose Dirichlet series is

\[
\sum_{n\ge1}\frac{\mu_{>3}(n)}{n^z}
=\prod_{p>3}(1-p^{-z})
=\frac1{\zeta(z)(1-2^{-z})(1-3^{-z})}.
\tag{L-93284.3}
\]

Define the large-prime-sieved rows

\[
c_X^{>3}(j)
=\sum_{k\le X/j}\frac{\mu_{>3}(k)}{\sqrt k}Q_{X/k}(j),
\qquad j=2,3.
\tag{L-93284.4}
\]

The finite factors in (L-93284.3) have no zero in the open strip, so positivity
of these two rows is just as conclusion-producing as positivity of the full
rows.

## 3. Exact smooth reservoir plus defects

Let `R_3` be the squarefree integers all of whose prime factors exceed three.
The coefficient sequence before the logarithmic Riesz integration has the
following exact decomposition.

For row two,

\[
\boxed{
\begin{aligned}
a_{2,>3}(n)
={}&\mathbf1_{n=2^a3^b}\quad(a,b\ge0)\\
&+\sum_{d\in R_3}\mu(d)
[-\mathbf1_{n=d}+2\mathbf1_{n=2d}-\mathbf1_{n=3d}].
\end{aligned}
}
\tag{L-93284.5}
\]

For row three,

\[
\boxed{
\begin{aligned}
a_{3,>3}(n)
={}&\frac13\mathbf1_{n=2^a3^b}\\
&+\sum_{d\in R_3}\mu(d)
\left[-\frac13\mathbf1_{n=d}-\frac13\mathbf1_{n=2d}
+\frac53\mathbf1_{n=3d}-\mathbf1_{n=4d}\right].
\end{aligned}
}
\tag{L-93284.6}
\]

The first line in each formula is a positive `2,3`-smooth reservoir. All
remaining signs are confined to one three- or four-knot packet for each large
squarefree owner `d`. No small-prime overlap or hidden infinite Euler product
remains.

The concrete producer is

\[
\boxed{
\mathrm{LPTRP}_{23}:
\quad c_X^{>3}(2)\ge0,\qquad c_X^{>3}(3)\ge0
\quad(X\ge1).
}
\tag{L-93284.7}
\]

`LPTRP_23` is not proved here. Equations (L-93284.5)--(L-93284.6) reduce it to
a global one-use allocation from an explicit smooth reservoir to explicit
large-prime packets. This is strictly smaller than the failed all-row
`FRONTIER-CHAIN` interface on PR #537.
