# L-99902 — Exact ratio-window Gram kernel for the half-order Möbius source

Claim ID: `L-99902`  
Status: **PROVED EXACT FINITE BLOCK IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99900`  
RH status: **not assumed**

For `R>1` and a finitely supported real sequence `(a_n)`, define

\[
\mathcal W_R(x)=\sum_{x/R<n\le x}a_n.
\]

For a logarithmic block `U<V`, put

\[
\ell_{U,V;R}(m,n)
=
\left[
\min\!\left(V,\log(R\min(m,n))\right)
-
\max\!\left(U,\log\max(m,n)\right)
\right]_+.
\]

The two interval indicators overlap for precisely this logarithmic length, so
finite Fubini gives

\[
\boxed{
\int_U^V|\mathcal W_R(e^u)|^2du
=
\sum_{m,n}a_ma_n\ell_{U,V;R}(m,n).
}
\tag{L-99902.1}
\]

The kernel is positive semidefinite because

\[
\ell_{U,V;R}(m,n)
=
\int_U^V
\mathbf1_{e^u/R<m\le e^u}
\mathbf1_{e^u/R<n\le e^u}
\,du.
\]

For the native collar take

\[
a_n=\beta(n)n^{-1/2},\qquad R=67.
\]

Then (L-99902.1) is the exact block energy of the coefficient in
`L-99900.3`. Expanding `beta` yields a finite three-band combination of the
same half-order squarefree-core correlations appearing in `GPMOC99800` and the
C4MBI/SACF lanes.

Positive semidefiniteness is not a sign theorem: it controls the square after
the Möbius signs have been inserted, while the required one-sided physical
orientation remains open.
