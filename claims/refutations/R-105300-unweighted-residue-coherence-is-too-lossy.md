# R-105300 — Unweighted residue coherence is not a faithful low-order proxy

Claim ID: `R-105300`
Status: **PROVED EXACT COUNTERFAMILY**
Created: 2026-08-23
RH status: not assumed

Consider

\[
p_C(x)=x^3-3x+C,
\qquad |C|<2.
\]

Its discriminant is

\[
108-27C^2>0,
\]

so all three roots are real and simple. Its two critical points are `-1` and
`1`, and

\[
\rho_{-1}=-\frac{C+2}{6},
\qquad
\rho_1=\frac{C-2}{6}.
\]

Both residues are negative. Thus every real critical point is
Rolle-generating and the exact low-order descent has no defect.

Nevertheless the unweighted residue coherence is

\[
\mathfrak C(p_C)
=\frac{(-\rho_{-1}-\rho_1)^2}
{2(\rho_{-1}^2+\rho_1^2)}
=\frac4{4+C^2}.
\]

At `C=3/2`,

\[
\boxed{\mathfrak C(p_{3/2})=\frac{16}{25}=0.64.}
\]

Therefore a threshold such as `C>=0.9` is not necessary even for a polynomial
whose roots and critical points are all real and whose every critical residue
has the correct sign.

The failure is pure magnitude variance: the two good extrema have unequal
curvatures. A proof strategy that first collapses the low-order descent to one
unweighted mean/variance quotient can lose the sign theorem it is trying to
prove.

The Hermite--Pick trace form of `L-105300` repairs this. Its inertia sees only
the signs and conjugate-pair geometry. Polynomial preconditioning in
`L-105301` may reduce magnitude spread without depending on the unknown sign.
