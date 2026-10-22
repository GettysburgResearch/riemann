# L-103200 — Every fixed half-order notch leaves a power-sized prime carrier

Claim ID: `L-103200`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC**  
Created: 2026-08-20  
Depends on: the classical quantitative prime number theorem  
RH status: **not assumed**

Let \(K\) be compactly supported in \([1,R]\), piecewise \(C^1\), and vanish at
the support endpoints.  Put

\[
\widehat K(s)=\int_1^R K(y)y^{-s-1}\,dy,
\qquad
\Pi_K(X)=\sum_p\frac1{\sqrt p}K(X/p).
\]

For every fixed \(J\ge0\),

\[
\boxed{
\Pi_K(X)
=
\sqrt X\sum_{j=0}^{J}
\frac{(-1)^j\widehat K^{(j)}(1/2)}
{\log^{j+1}X}
+
O_{K,J}\!\left(\frac{\sqrt X}{\log^{J+2}X}\right).
}
\tag{L-103200.1}
\]

Partial summation gives

\[
\Pi_K(X)
=
\sqrt X\int_1^R
\frac{K(y)y^{-3/2}}{\log X-\log y}\,dy
+
O_K(\sqrt Xe^{-c\sqrt{\log X}}),
\]

and the result follows by expanding the denominator on the fixed support.

For the ratio-eight kernel,

\[
\kappa_0=\widehat K_0(1/2)
=8\log2(1-2^{-1/2})^2>0.
\]

For

\[
K_1=(I-\sqrt2S_2)K_0,
\]

\[
\widehat K_1(1/2)=0,
\qquad
\widehat K_1'(1/2)=\log2\,\kappa_0>0.
\]

Hence

\[
\boxed{
\Pi_{K_1}(X)
=
-\log2\,\kappa_0\frac{\sqrt X}{\log^2X}
+
O(\sqrt X/\log^3X).
}
\tag{L-103200.2}
\]

The singleton Möbius sector is \(-\Pi_{K_1}\), and therefore has the opposite,
positive main term.

More generally, a fixed zero of exact order \(m\) at \(s=1/2\) leaves a
regional prime carrier of order

\[
\sqrt X/\log^{m+1}X.
\]

Thus no fixed number of safe notches makes a regional absolute value, square,
or Hilbert norm subpower.  The cancellation partner must remain present until
after exact recombination.
