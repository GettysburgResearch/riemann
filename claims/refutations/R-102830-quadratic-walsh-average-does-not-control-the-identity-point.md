# R-102830 — Quadratic Walsh average does not control the identity point

Claim ID: `R-102830`  
Status: **PROVED SOURCE-BLIND POINT-EVALUATION COUNTERMODEL**  
Created: 2026-08-24  
Depends on: `L-102833`  
RH status: **not assumed**

For `N` independent signs define the degree-two Walsh polynomial

\[
F_N(\varepsilon)=\sum_{1\le i<j\le N}\varepsilon_i\varepsilon_j.
\]

Haar orthogonality gives

\[
\|F_N\|_{L^2(\{-1,1\}^N)}^2=\binom N2.
\]

At the physical identity point,

\[
F_N(1,\ldots,1)=\binom N2.
\]

Therefore

\[
\boxed{
{ |F_N(1)|\over\|F_N\|_2}
=\sqrt{\binom N2}\longrightarrow\infty.
}
\]

Thus the polylogarithmic quadratic-Walsh average in `L-102833` cannot by itself
bound physical collapse at `epsilon=1`, even though the polynomial has fixed
degree two.

The fixture is source-blind. It does not refute `L2SC102833` or
`LDPC102834`; it proves that a successful argument must use the literal
semiprime-squareclass geometry, the largest discrepancy prime, source signs or
an arithmetic large-sieve/dispersion theorem.