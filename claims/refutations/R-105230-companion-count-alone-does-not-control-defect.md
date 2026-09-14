# R-105230 — Companion-pole count alone does not control square-defect mass

Claim ID: `R-105230`  
Status: **EXACT FIREWALL**

Consider
\[
f_C(x)=\frac{x^3}{3}-x+C,
\qquad p=f_C'=x^2-1.
\]
For `delta=1/2`,
\[
G_\delta(z)=p'(z)+i\delta p(z)
=2z+\frac{i}{2}(z^2-1)
\]
has the two roots
\[
z=i(2\pm\sqrt3),
\]
both in the upper half-plane.  Thus its lower companion-pole count is zero,
in agreement with L-105231 because `p` is real-rooted.

The two critical residues are
\[
\rho_+=\frac{C-2/3}{2},
\qquad
\rho_-=-\frac{C+2/3}{2}.
\]
For every fixed `lambda>0`,
\[
(1+\lambda\rho_+)^2+(1+\lambda\rho_-)^2
\sim\frac{\lambda^2C^2}{2}
\qquad(|C|\to\infty).
\]
Hence the square-defect mass is unbounded while the lower companion-pole count
remains zero.  L-105230 removes interpolation blowup, but a conclusion still
needs quantitative boundary flux and pole-amplitude control; index counting
alone is insufficient.
