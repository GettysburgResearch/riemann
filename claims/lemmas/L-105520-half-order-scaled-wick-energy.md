# L-105520 — Half-order symbol normalization and the scaled Wick energy law

Claim ID: `L-105520`  
Status: **PROVED FROM THE PNT AT FROZEN MODEL SCOPE**  
Created: 2026-08-24  
Depends on: `L-105250/L-105252` on PR #731, prime-simplex PNT argument  
RH status: **not assumed**

## 1. Correct Hermitian symbol

Let

\[
a_{K,L,\alpha}(n)
=
\sum_{m=K+1}^{\Omega(n)}
q_{K,m}L^{-m}\Lambda^{*m}(n),
\qquad n\le e^{\alpha L}.
\]

The Hermitian Dirichlet symbol whose diagonal energy is
\(\sum |a(n)|^2/n\) is

\[
\boxed{
f_{K,L,\alpha}(t)
=
1+2\Re\sum_{n\le e^{\alpha L}}
a_{K,L,\alpha}(n)n^{-1/2-it}.
}
\tag{L-105520.1}
\]

Without the factor \(n^{-1/2}\), Montgomery--Vaughan gives
\(\sum |a(n)|^2\), not \(\sum |a(n)|^2/n\).  Thus the display formerly used in
`L-105322` and its standalone summary was missing a load-bearing half-order
factor.  The arithmetic coefficients and all `/n` energy formulae are retained;
the symbol is corrected.

For every fixed \(\alpha<2\) in the ordinary long-polynomial mean-value
range, and by the corresponding pinned endpoint-safe formulation at
\(\alpha=2\),

\[
\frac1T\int_T^{2T} f_{K,L,\alpha}(t)\,dt=1+o(1),
\]

\[
\frac1T\int_T^{2T}|f_{K,L,\alpha}(t)|^2dt
=
1+2\sum_{n\le e^{\alpha L}}
\frac{a_{K,L,\alpha}(n)^2}{n}
+o(1).
\tag{L-105520.2}
\]

The statement is a frozen model theorem.  It does not identify the model with
the actual Xi contour compression.

## 2. Scaled prime-simplex law

For a squarefree product \(n=p_1\cdots p_m\),

\[
\Lambda^{*m}(n)=m!\prod_{j=1}^m\log p_j.
\]

Set \(u_j=\log p_j/L\).  The cutoff \(n\le e^{\alpha L}\) becomes
\(\sum u_j\le\alpha\), so the PNT simplex integral is

\[
\int_{\substack{u_j\ge0\\\sum u_j\le\alpha}}
\prod_{j=1}^m u_j\,du
=
\frac{\alpha^{2m}}{(2m)!}.
\]

The repeated-prime and mixed-degree terms are treated exactly as in
`L-105321/L-105252`.  Therefore

\[
\boxed{
\lim_{L\to\infty}
\sum_{n\le e^{\alpha L}}
\frac{a_{K,L,\alpha}(n)^2}{n}
=
\mathcal D_K(\alpha)
:=
\sum_{m\ge K+1}
q_{K,m}^2\frac{m!}{(2m)!}\alpha^{2m}.
}
\tag{L-105520.3}
\]

The unscaled constant in the earlier packets is
\(\mathcal D_K(1)\).  It cannot be silently used at a different physical
cutoff.

## 3. Degree four survives the full physical scale

For the degree-four truncation of \(\sqrt{1-x}\),

\[
P_4(x)=1-\frac x2-\frac{x^2}{8}-\frac{x^3}{16}
-\frac{5x^4}{128}.
\]

Its positive quotient coefficients are

\[
q_{4,5}=\frac7{128},\qquad
q_{4,6}=\frac{35}{512},\qquad
q_{4,7}=\frac{75}{1024},\qquad
q_{4,m}=\frac{1225}{16384}\quad(m\ge8).
\]

At the full half-order bandwidth \(\alpha=2\), the first three terms are

\[
\frac7{69120},\qquad
\frac{35}{1216512},\qquad
\frac{125}{24600576}.
\]

For \(m\ge8\),

\[
\frac{2^{2(m+1)}(m+1)!/(2m+2)!}
     {2^{2m}m!/(2m)!}
=
\frac2{2m+1}\le\frac2{17}.
\]

Hence the complete tail is at most

\[
\frac{29155}{36436967424},
\]

and

\[
\boxed{
\mathcal D_4(2)
\le
\frac{173344649}{1275293859840}
<
\frac1{7000}.
}
\tag{L-105520.4}
\]

Thus the corrected, physically scaled degree-four frozen symbol still has
mean square below \(3501/3500+o(1)\).  The model reserve is not the obstacle to
ninety percent; the strip-to-contour transfer is.
