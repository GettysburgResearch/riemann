# L-96504 — Two nonnegative native rows feed a complete reciprocal-zeta Mellin–Landau consumer

Claim ID: `L-96504`  
Status: **PROVED EXACT ANALYTIC COMPOSITION, CONDITIONAL ONLY ON THE PRODUCER SIGN**  
Created: 2026-08-17  
Depends on: `L-96503`; fixed-row calculation of PR #542/PR #552

For fixed `j>=2`, put `f_j(X)=c_X(j)`. Direct termwise integration in the
absolute-convergence half-plane gives

\[
\mathcal C_j(s)=\int_1^\infty f_j(X)X^{-s-1}\,dX
 ={C_j\over s^2}
 +{P_j(s+1/2)\over s^2\zeta(s+1/2)},
\tag{L-96504.1}
\]

where

\[
P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
      -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

For the two fixed rows,

\[
P_2(z)=2^{1-z}-1-3^{-z},
\tag{L-96504.2}
\]

\[
3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.
\tag{L-96504.3}
\]

They have no common zero in `Re z>0`. Indeed, if `a=2^{-z}` and
`b=3^{-z}`, (L-96504.2) gives `b=2a-1`; substitution in (L-96504.3) gives

\[
-3(a-1)(a-2)=0,
\]

impossible because `|a|=2^{-Re z}<1`.

By `L-96503`, `f_2,f_3>=0`. They are locally integrable and have a finite
Mellin abscissa. Landau's theorem for a nonnegative Mellin density says that a
positive real abscissa is singular unless the defining transform continues
through it. The right side of (L-96504.1) is analytic at every positive real
`s`; hence each defining integral is holomorphic throughout `Re s>0`.

If `zeta(rho)=0` with `Re rho>1/2`, at least one of `P_2(rho),P_3(rho)` is
nonzero. The corresponding transform has a nonremovable pole at
`s=rho-1/2`, contradicting holomorphy of its defining nonnegative integral.
The functional equation excludes the reflected half-plane. Thus the producer
signs (L-96503.2) imply RH.

This consumer never mentions `F_Lambda`, native `Y4` slack, or an endpoint
packing deficit; the PR #541 normalization firewall is therefore respected.
