# L-102504 — The common mother is a fixed zero-safe Mellin–Landau detector

Claim ID: `L-102504`  
Status: **PROVED CONDITIONAL ANALYTIC CONSUMER**  
Created: 2026-08-22  
Depends on: `L-102500`; specialized Landau theorem  
Arithmetic sign premise: **open**  
RH status: **unproved**

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\]

and define

\[
\boxed{
H_\Phi(X)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}\Phi_*(X/n).
}
\tag{L-102504.1}
\]

The sum is finite at every `X`, since `supp(Phi_*) subset [1,16]`.

For `Re(s)` initially large,

\[
\boxed{
\int_1^\infty H_\Phi(X)X^{-s-1}\,dX
=
m_\Phi(s)\frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}.
}
\tag{L-102504.2}
\]

The right side is holomorphic at every positive real `s`. At `s=1/2` the
zeta pole and explicit dyadic zero make the apparent singularity removable.

If `rho` is a zeta zero with `1/2<Re(rho)<1`, then
`s_rho=rho-1/2` lies in `0<Re(s)<1/2`. By `L-102500`, neither

\[
m_\Phi(s_\rho),\qquad 1-67^{-\rho}
\]

vanishes. Hence the zero produces a genuine pole of (L-102504.2).

The specialized negative-mass Landau argument therefore gives

\[
\boxed{
\int_1^Y(H_\Phi(X))_-\frac{dX}{X}=Y^{o(1)}
\quad\Longrightarrow\quad \mathrm{RH}.
}
\tag{L-102504.3}
\]

This is one detector fixed before any hypothetical zero. The fixed `5:3`
scalar and simultaneous rows `2,3` remain independent audits, not
zero-dependent choices.

The arithmetic estimate in (L-102504.3) is not proved here.
