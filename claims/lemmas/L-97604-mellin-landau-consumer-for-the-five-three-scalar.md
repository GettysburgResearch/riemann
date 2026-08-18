# L-97604 — A nonnegative 5:3 scalar gives a complete Mellin-Landau implication to RH

Claim ID: `L-97604`  
Status: **PROVED COMPLETE CONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-17  
RH status: **the arithmetic nonnegativity hypothesis is not proved here**

For `Re s>1/2`, absolute Fubini and the substitution `X=kY` give

\[
\int_1^\infty R_X X^{-s-1}\,dX
 ={6\over s^2}
 -{3(1-2^{-z})(2-2^{-z})\over s^2\zeta(z)},
\qquad z=s+\tfrac12.
\]

The factor `k^{-s-1/2}` is essential.  The initial Fubini region follows from
`R_X=O(sqrt(X) log(2X))`, which is obtained from `q_*(m)<=15` and elementary
harmonic estimates.

For real `s>0`, `z>1/2`.  The zeta function has no real zero there; at `z=1`
the reciprocal zeta factor vanishes and the apparent point is removable.
Hence the continued transform is analytic at every positive real `s`.

If `rho` is a zero of zeta with `Re rho>1/2`, then
`|2^{-rho}|<1`, so neither factor of the finite numerator vanishes.  A zero of
arbitrary multiplicity therefore gives a nonremovable pole at
`s=rho-1/2`.

If `R_X>=0` for all sufficiently large real `X`, set `f(t)=R_{e^t}` and subtract
the finite initial interval.  The resulting Laplace transform has a finite
abscissa of convergence.  Landau's theorem for a nonnegative locally
integrable function forces a singularity at a positive real abscissa, whereas
the displayed continuation is analytic at every positive real point.  Thus the
abscissa is at most zero, making the transform holomorphic in `Re s>0`.
The off-line pole is impossible.  Functional-equation symmetry then gives RH.
