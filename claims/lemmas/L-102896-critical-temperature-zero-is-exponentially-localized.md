# L-102896 — The finite-horizon temperature zero is exponentially localized around one half

Claim ID: `L-102896`  
Status: **PROVED UNCONDITIONAL UNIFORM TRANSITION THEOREM**  
Created: 2026-08-24  
Depends on: `L-102895`; classical Vinogradov--Korobov zero-free region  
RH status: **not assumed**

For fixed \(X\), the finite source sum \(\mathscr S_t(X)\) is a real polynomial
in \(t\): only finitely many binomial coefficients of the local factors can
contribute.

Put

\[
V(X)
=
(\log X)^{3/5}(\log\log X)^{-1/5}.
\]

There exist absolute constants \(a,C,X_0>0\), depending only on the fixed outer
kernel and duplicate-67 convention, such that for \(X\ge X_0\),

\[
\Delta_X
=
C(\log X)^2e^{-aV(X)}
\tag{L-102896.1}
\]

satisfies

\[
\boxed{
\mathscr S_{1/2-\Delta_X}(X)<0
<
\mathscr S_{1/2+\Delta_X}(X).
}
\tag{L-102896.2}
\]

Moreover,

\[
\boxed{
\partial_t\mathscr S_t(X)
\asymp
{\sqrt X\over(\log X)^2}
}
\tag{L-102896.3}
\]

uniformly for

\[
|t-1/2|\le\Delta_X.
\]

Hence there is one and only one real zero

\[
\boxed{
\vartheta(X)\in
[1/2-\Delta_X,\,1/2+\Delta_X]
}
\tag{L-102896.4}
\]

of \(\mathscr S_t(X)\) in this transition layer.

## Proof

Write

\[
t={1\over2}+\delta.
\]

The uniform Hankel expansion at \(z=1\), together with the classical
zero-free-contour remainder, gives for \(|\delta|\le\delta_0\),

\[
\begin{aligned}
\mathscr S_{1/2+\delta}(X)
={}&
\kappa\,\delta\,
{\sqrt X\over(\log X)^2}
e^{2\delta\log\log X}\\
&+
O\left(
{\sqrt X\over(\log X)^2}
e^{2|\delta|\log\log X}
\left(\delta^2+{|\delta|\over\log X}\right)
\right)\\
&+
O\left(\sqrt X\,e^{-a_0V(X)}\right),
\end{aligned}
\tag{L-102896.5}
\]

where

\[
\boxed{
\kappa
=
-2\widehat R_L(1/2)G_{1/2}(1)^2>0.
}
\tag{L-102896.6}
\]

The same contour differentiated in \(t\) gives

\[
\partial_t\mathscr S_{1/2+\delta}(X)
=
\kappa{\sqrt X\over(\log X)^2}
+
o\left({\sqrt X\over(\log X)^2}\right)
\tag{L-102896.7}
\]

uniformly on the much thinner layer in (L-102896.1).

Choose \(a<a_0\) and then \(C\) sufficiently large.  The first term of
(L-102896.5) dominates the zero-free remainder with the sign of \(\delta\),
proving (L-102896.2).  Equation (L-102896.7) gives strict monotonicity and
uniqueness.

## Meaning

The detector-bearing midpoint is not merely a formal endpoint.  The sign
transition of the strict source squares occurs inside an exponentially thin
temperature window:

\[
\boxed{
|\vartheta(X)-1/2|
\ll
(\log X)^2
\exp\!\left[
-a(\log X)^{3/5}(\log\log X)^{-1/5}
\right].
}
\]

Determining the **side** of this tiny displacement remains equivalent to
controlling the midpoint square.
