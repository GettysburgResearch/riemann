# Standalone proof extract

For fixed \(j\), the prime-sieved theorem gives \(f_j(X)=c_X(j)\ge0\).

Termwise Mellin integration and the Möbius Dirichlet series give

\[
\mathcal C_j(s)=
\frac{C_j}{s^2}+
\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\]

The continuation is analytic at every positive real \(s\), so Landau's theorem
puts the abscissa of convergence at most zero.

At a hypothetical zero \(\rho\) with \(\Re\rho>1/2\),

\[
P_j(\rho)=
-\frac{\rho(\rho+1)}{1-\rho}j^{-\rho-1}
+O_\rho(j^{-\Re\rho-2}),
\]

so \(P_j(\rho)\ne0\) for sufficiently large fixed \(j\). The transform would
have a pole in its domain of holomorphy, a contradiction. The functional
equation completes the proposed proof.

The sole load-bearing finite producer is the universal prime-sieved row
positivity theorem inherited from PR #537.
