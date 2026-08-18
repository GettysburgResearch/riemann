# R-98070 — Every fixed rough reciprocal-Möbius prefix changes sign infinitely often

Claim ID: `R-98070`  
Status: **PROVED CONDITIONAL ONLY ON A KNOWN CRITICAL-LINE ZERO**  
Created: 2026-08-18  
RH status: **not assumed**

For fixed `z>=2`, put

\[
A_z(x)=\sum_{\substack{n\le x\\P^-(n)\ge z}}\frac{\mu(n)}n .
\]

For `Re s>0`,

\[
\int_1^\infty A_z(x)x^{-s-1}dx
=
\frac1{s\zeta(s+1)}
\prod_{p<z}(1-p^{-s-1})^{-1}.
\]

The point `s=0` is removable. The right side is analytic at every real
`s>-1`, but every known nontrivial zero `rho=1/2+i gamma` of zeta gives a
nonremovable pole at `s=rho-1=-1/2+i gamma`; the finite Euler product is
nonzero there.

If `A_z` were eventually nonnegative, Landau's theorem for its Mellin/Laplace
transform would force a singularity on the real abscissa of convergence.
There is no real singularity in `(-1,infinity)`, while the complex pole above
forces the abscissa to be at least `-1/2`, a contradiction. Applying the same
argument to `-A_z` rules out eventual nonpositivity.

Hence every fixed `A_z` changes sign infinitely often.

This refutes the proposed raw-prefix positivity mechanism; it does not refute
the signed Stieltjes-transfer route.
