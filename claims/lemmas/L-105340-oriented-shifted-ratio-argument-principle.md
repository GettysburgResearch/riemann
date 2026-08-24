# L-105340 — Oriented shifted-ratio argument principle

Claim ID: `L-105340`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
RH status: **not assumed**

Let `F` be entire and put

\[
E_\alpha=F'-\alpha F,
\qquad E_{-\alpha}=F'+\alpha F,
\qquad \mathcal M_\alpha=E_\alpha/E_{-\alpha}.
\]

Let `Omega` be a bounded positively oriented contour on whose boundary `F'`
does not vanish. For all sufficiently small complex `alpha`, neither shifted
function vanishes on the boundary. For `Psi` holomorphic near the closed
contour, define

\[
\mathcal Z_\alpha(\Psi;\Omega)
=\sum_{\rho\in\Omega}\operatorname{ord}_\rho(E_\alpha)\Psi(\rho)
-\sum_{\rho\in\Omega}\operatorname{ord}_\rho(E_{-\alpha})\Psi(\rho).
\]

Common factors occur with equal multiplicity and cancel. The argument
principle gives

\[
\boxed{
\mathcal Z_\alpha(\Psi;\Omega)
=\frac1{2\pi i}\int_{\partial\Omega}
\Psi(s)\frac{\mathcal M_\alpha'(s)}{\mathcal M_\alpha(s)}\,ds.}
\tag{L-105340.1}
\]

The integral is holomorphic in `alpha` near zero. Since

\[
\left.\partial_\alpha\log\mathcal M_\alpha(s)\right|_{0}
=-2F(s)/F'(s),
\]

closed-contour integration by parts yields

\[
\boxed{
\left.\partial_\alpha\mathcal Z_\alpha(\Psi;\Omega)\right|_{0}
=\frac2{2\pi i}\int_{\partial\Omega}\Psi'(s)\frac{F(s)}{F'(s)}\,ds.}
\tag{L-105340.2}
\]

Thus, with

\[
B_\Psi(F;\Omega)
=-\frac1{2\pi i}\int_{\partial\Omega}\Psi'(s)F(s)/F'(s)\,ds,
\]

one has

\[
\boxed{B_\Psi=-\tfrac12\partial_\alpha\mathcal Z_\alpha|_0.}
\tag{L-105340.3}
\]

No simplicity hypothesis is used. At a simple zero `c` of `F'`, the branch of
`E_alpha` satisfies `c'(0)=F(c)/F''(c)`. At a multiple critical point,
(L-105340.2) gives the complete confluent residue without selecting Puiseux
branches.
