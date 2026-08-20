# R-100020 — Infinite Euler squaring destroys the reciprocal-zeta detector

Claim ID: `R-100020`  
Status: **PROVED EXACT ANALYTIC FIREWALL**  
Created: 2026-08-20  
RH status: **not assumed**

For finite \(Z\), the completion multiplier is

\[
A_Z(z)=
(1+67^{-z})^2
\prod_{\substack{p\le Z\\p\ne67}}(1+p^{-z}).
\tag{R-100020.1}
\]

If \(\Re z>0\), then \(|p^{-z}|<1\), so every factor in (R-100020.1) is
nonzero. A finite completion therefore preserves every reciprocal-zeta pole in
that half-plane.

If instead every prime is squared, then

\[
\begin{aligned}
\frac{1-67^{-z}}{\zeta(z)}
(1+67^{-z})^2
\prod_{p\ne67}(1+p^{-z})
&=
(1-67^{-2z})^2
\prod_{p\ne67}(1-p^{-2z})\\
&=
\boxed{\frac{1-67^{-2z}}{\zeta(2z)}}.
\end{aligned}
\tag{R-100020.2}
\]

The original factor \(1/\zeta(z)\) is gone. A zero \(\rho\) is moved to
\(z=\rho/2\), outside the translated conclusion half-plane.

Thus

\[
\boxed{
\text{finite Euler squaring is pole-preserving, whereas infinite Euler
squaring kills the detector.}
}
\tag{R-100020.3}
\]

No limit \(Z\to\infty\) may be used as though the finite pole-preserving
argument passed continuously to the infinite completion.
