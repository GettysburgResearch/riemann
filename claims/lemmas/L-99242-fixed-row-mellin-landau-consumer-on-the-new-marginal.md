# L-99242 — The fixed-row Mellin–Landau consumer applies directly to the T-99240 marginal

Claim ID: `L-99242`  
Status: **PROPOSED COMPLETE SELF-CONTAINED ANALYTIC LEMMA — REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99240/L-99241` only for nonnegativity of the exact row  
RH status: **not assumed**

Fix `j>=2` and retain

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]

The canonical row expansion of `L-99240` gives, for `Re(s)>1/2`,

\[
 \int_1^\infty Q_X(j)X^{-s-1}dX
 =\frac{H_j(s+1/2)}{s^2},
\]

where

\[
 H_j(z)=C_j\zeta(z)+P_j(z)
\]

and

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
        -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

Absolute Fubini with the Möbius Dirichlet series therefore yields

\[
 \boxed{
 \mathcal C_j(s):=\int_1^\infty c_X(j)X^{-s-1}dX
 =\frac{C_j}{s^2}
  +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
 }
\tag{L-99242.1}
\]

The right side is analytic at every positive real `s`. At `s=1/2`, the pole
of zeta makes the reciprocal term vanish. Away from that point, zeta has no
real zero on `(1/2,infinity)`; on `(1/2,1)` this follows from the alternating
eta representation and on `(1,infinity)` from the Euler product.

For fixed `z` with `0<Re(z)<1`, Euler--Maclaurin gives

\[
 \sum_{m=1}^{j+1}m^{-z}
 =\frac{(j+1)^{1-z}}{1-z}
  +\frac12(j+1)^{-z}
  +O_z(j^{-\Re z-1}).
\]

Substitution of the exact rational coefficients gives

\[
 \boxed{
 P_j(z)
 =-\frac{z(z+1)}{1-z}j^{-z-1}
  +O_z(j^{-\Re z-2}).
 }
\tag{L-99242.2}
\]

The leading coefficient is nonzero at every nontrivial zeta zero. Hence each
hypothetical open-strip zero survives in every sufficiently large fixed row.

Now suppose `c_X(j)>=0`, as supplied by the T-99240 source construction. Its
Mellin integral has a finite abscissa of convergence because
`c_X(j)=O_j(sqrt(X)log(2X))`. Landau's theorem for a nonnegative Mellin density
says that a finite abscissa is a singularity on the real axis.

If `zeta(rho)=0` with `Re(rho)>1/2`, choose a fixed large `j` with
`P_j(rho)!=0`. Equation (L-99242.1) then has a genuine pole at
`s=rho-1/2`, so the defining integral cannot converge throughout `Re(s)>0`.
Its abscissa is therefore positive. Landau forces a positive-real singularity,
but (L-99242.1) is analytic at every positive real point. Contradiction.

Thus positivity of the exact T-99240 row excludes all zeros to the right of the
critical line. Functional-equation symmetry excludes zeros to the left.

This argument imports no assertion from the refuted `FRONTIER-CHAIN`: only the
row formula, elementary Mellin integration, Euler--Maclaurin, and Landau are
used.
