# L-99900 — The native normalized collar slope is a three-band half-order Möbius window

Claim ID: `L-99900`  
Status: **PROVED EXACT ALL-PRIME COEFFICIENT IDENTITY**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`; `R-99900`  
RH status: **not assumed**

Retain the notation of `R-99900` and take `R=67`. In logarithmic coordinate
`u=log y`, the normalized collar is

\[
\Phi(u)=8+(-8-3u)e^{-u/2},
\qquad 0\le u<\log67.
\tag{L-99900.1}
\]

The literal normalized scalar is

\[
B(X):=\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
 =\sum_{n\le X}\frac{\beta(n)}n\Phi(\log(X/n)).
\tag{L-99900.2}
\]

On a fixed activation cell, only indices

\[
X/67<n\le X
\]

use the collar formula. Their contribution to the coefficient of
`u e^-u/2` is

\[
\frac{\beta(n)}n
\left[-3(u-\log n)e^{-(u-\log n)/2}\right].
\]

Since

\[
\frac1n e^{\log n/2}=\frac1{\sqrt n},
\]

the exact collar slope is

\[
\boxed{
 c_{\rm native}(u)
 =-3\sum_{e^u/67<n\le e^u}\frac{\beta(n)}{\sqrt n}.
}
\tag{L-99900.3}
\]

Let

\[
B_{1/2}(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

Because

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

finite reindexing gives

\[
\sum_{X/67<n\le X}\frac{\beta(n)}{\sqrt n}
=
B_{1/2}(X)
-\left(1+67^{-1/2}\right)B_{1/2}(X/67)
+67^{-1/2}B_{1/2}(X/67^2).
\tag{L-99900.4}
\]

Hence

\[
\boxed{
 c_{\rm native}(\log X)
=-3\left[
B_{1/2}(X)
-(1+67^{-1/2})B_{1/2}(X/67)
+67^{-1/2}B_{1/2}(X/67^2)
\right].
}
\tag{L-99900.5}
\]

This is exactly the three-band half-order source already visible in the
squarefree-core/GPMOC lane. The activation problem therefore does not reduce
to an unweighted Mertens window. It reduces to a source-faithful half-order
annular correlation.

Equations (L-99900.3)--(L-99900.5) are coefficient identities. They do not by
themselves prove the one-sided collar estimate or RH.
