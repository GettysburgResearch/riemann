# L-105540 — Unimodular Bezout completion of the Hermitian bank

Claim ID: `L-105540`  
Status: **PROVED EXACT IN EVERY UNITAL OPERATOR ALGEBRA**  
Created: 2026-08-24  
Depends on: `L-105530`  
RH status: **not assumed**

Let `A` be a unital real or complex algebra and let `X in A`.  Define

\[
W_0=I-\frac X2-\frac{X^2}{4},
\qquad
W_1=\frac X2,
\qquad
B=I+\frac X2.
\tag{L-105540.1}
\]

Since all three entries are polynomials in the same element `X`, they commute,
and direct multiplication gives the Bezout identity

\[
\boxed{W_0+B W_1=I.}
\tag{L-105540.2}
\]

Consequently

\[
\boxed{
U(X)=
\begin{pmatrix}
W_0&-B\\
W_1&I
\end{pmatrix},
\qquad
U(X)^{-1}=
\begin{pmatrix}
I&B\\
-W_1&W_0
\end{pmatrix}.
}
\tag{L-105540.3}
\]

Both products are the identity.  In the scalar polynomial ring,
`det U(z)=1` identically.

For every left `A`-module `V`, the bank observation map

\[
\mathcal W_X:V\longrightarrow V\oplus V,
\qquad
v\longmapsto(W_0v,W_1v)
\tag{L-105540.4}
\]

has the exact left inverse

\[
\boxed{
\mathcal L_X(g_0,g_1)=g_0+B g_1.
}
\tag{L-105540.5}
\]

Hence `mathcal W_X` is injective and preserves the source dimension exactly.
If `X(z)` is holomorphic on a strip or domain, both `U(X(z))` and its inverse
are holomorphic there.  The bank therefore introduces no common zero, no
Fredholm loss, and no bank-induced Wiener--Hopf/strip partial index.

For bounded operators with `||X||<=r`,

\[
\|W_0\|\le1+\frac r2+\frac{r^2}{4},
\quad
\|W_1\|\le\frac r2,
\qquad
\|B \|\le1+\frac r2.
\tag{L-105540.6}
\]

If `||X||,||Y||<=r`, then

\[
\boxed{
\|W_0(X)-W_0(Y)\|
\le\left(\frac12+\frac r2\right)\|X-Y\|,
\qquad
\|W_1(X)-W_1(Y)\|\le\frac12\|X-Y\|.
}
\tag{L-105540.7}
\]

No normality, diagonalizability, or nilpotence is required.
