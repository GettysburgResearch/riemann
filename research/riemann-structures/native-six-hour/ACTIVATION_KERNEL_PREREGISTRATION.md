# Native activation-kernel discovery: fixed questions before the first run

Recorded before the parent-run discovery on 2026-08-31, in the six-hour pass.
No discovery output had been read when this file was written.

The primary source is the exact real K_L in frozen L-102880. The input is the
monotone primewise deformation of the actual L-102707 half-geodesic, with the
full chain-rule derivative and measure 2 ds. On a squarefree three-prime cone,
activation weights q form a source-derived probability simplex. The variable
is this path parameter; arithmetic coefficients and kernel are not fitted.

The primary crowded set is (3,5,7). The independent crowded control is
(2,3,5). The separated control is (3,11,101), for which the exact support
argument predicts the uniform minimizing activation vector. These three sets
are fixed before the discovery run.

Compute the original autocorrelation Gamma from its nine piece intersections,
retaining exact Q(sqrt2) constants and rational logarithms. Use rational
upper/lower bounds for logarithms and sqrt2. Form the three-by-three Gram
matrix of the odd source fields, retain the fixed mean energy, and check:

1. Is the unconstrained stationary activation vector inside the simplex?
2. Is the uniform activation stationary? Do the source cross correlations
   force a different minimizer?
3. Can a concrete positive integer-power schedule lower the energy of the
   uniform path, with the improvement certified by rational intervals?
4. Does the separated control reproduce the exact uniform minimum?

A negative or uniform answer on either crowded set is a valid result. If the
unconstrained vector is outside the simplex, solve the boundary faces and
retain the full KKT inequalities; do not call the unconstrained point the
source minimizer. Approximate numbers are discovery/readout only. Any final
inequality requires an interval certificate and the original 1/K energy
normalization. No claim about the full amplified gamma source follows.
