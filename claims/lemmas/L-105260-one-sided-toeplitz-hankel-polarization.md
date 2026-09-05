# L-105260 — Exact one-sided Toeplitz–Hankel polarization

Claim ID: `L-105260`  
Status: **PROVED EXACT AT FINITE DIRICHLET / PALEY–WIENER SCOPE**  
Created: 2026-08-24  
Depends on: L-105340--L-105343; L-105520  
RH status: not assumed

## 1. One-sided transform

Let \(\mathcal H=L^2(0,B)\), and for \(f\in\mathcal H\) define

\[
\Phi_f(s)=\int_0^B f(u)e^{(s-\frac12)u}\,du .
\tag{1}
\]

For \(s=\sigma+it\), put \(\eta=\sigma-\frac12\). If \(a=\log n\), Fourier inversion gives

\[
\frac1{2\pi}\int_{\mathbb R}n^{-s}\Phi_f(s)\Phi_g(1-s)\,dt
=n^{-1/2}\int_0^{B-a}f(v+a)g(v)\,dv,
\tag{2}
\]

and

\[
\frac1{2\pi}\int_{\mathbb R}n^{-s}\Phi_f(s)\Phi_g(s)\,dt
=n^{-1/2}\int_{\max(0,a-B)}^{\min(B,a)}f(u)g(a-u)\,du.
\tag{3}
\]

The factors \(e^{\eta u}\), \(e^{-\eta v}\), and \(n^{-\sigma}\) combine to \(n^{-1/2}\). Thus the physical half order is forced by reflection.

Equation (2) is a truncated Toeplitz shift. Equation (3) is a truncated Hankel reflection. At \(n=1\), (2) is the ordinary inner product, whereas (3) vanishes: \(u+v=0\) has measure zero in \((0,B)^2\). Hence the same-sign Hankel channel has no constant carrier.

## 2. Realification without the false square identity

Let \(\mathscr B\) be a conjugation-invariant symmetric contour form and let \(u_j^\#(s)=\overline{u_j(\bar s)}\). Put

\[
A_{ij}=\mathscr B(u_i,u_j),\qquad D_{ij}=\mathscr B(u_i,u_j^\#).
\]

Then \(A=A^T\) and \(D=D^*\). For the real-symmetric observations

\[
c_j=\frac{u_j+u_j^\#}{\sqrt2},\qquad s_j=\frac{u_j-u_j^\#}{i\sqrt2},
\]

the two diagonal real compressions are

\[
C_c=\operatorname{Re}(D+A),\qquad C_s=\operatorname{Re}(D-A).
\tag{4}
\]

This is the exact off-real polarization. No assertion \(p(z)p^\#(z)=p(z)^2\) is made.

For the one-sided source, the constant term occurs only in \(D\). The same-sign block \(A\) is a carrier-free Hankel block. Thus one may retain the \(c\)-channel and write

\[
C_c=D_{\rm acc}+H_{\rm Hankel}+E_{\rm edge}.
\tag{5}
\]

## 3. Accretive reflected channel

If the reflected safe-line source is represented by a strict contraction \(X\), \(R=(I-X)^{-1}\), and a source-fixed polynomial coordinate \(P\), then

\[
P^*(R+R^*)P\succeq P^*P.
\tag{6}
\]

On every fixed right safe line, the normalized Xi reciprocal source satisfies \(X=O(1/\log T)\). Hence, for every fixed degree \(K\),

\[
P_K(X)^*P_K(X)=I+O_K(1/\log T)
\tag{7}
\]

in operator norm, and after normalization

\[
D_{\rm acc}\succeq(1-o(1))I.
\tag{8}
\]

Equations (2)--(8) replace the false formal-square promotion by one positive Toeplitz anchor plus one explicitly owned Hankel perturbation.
