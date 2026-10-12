# Independent audit of the density refinement to order 900000

Verdict: **ACCEPT at the complete-source/imported-input scope.** Reviewed
D1--D7 in [DENSITY_RATIONAL_REFINEMENT.md](../heights/DENSITY_RATIONAL_REFINEMENT.md)
at SHA256
`6369e6f0417b2f31772fc1a2c315f6ae67bc7a6cfb1cc1b28c9ce4d03e9deb29`,
and read its exact checker. Review time: 2026-10-10 14:54 UTC. No independent
large computation or published input replay was performed; the previously
accepted [Volterra audit](VOLTERRA_HEIGHT_CROSS_REVIEW.md) supplies the
unchanged weighted operator and complete-source mechanisms.

The elementary logarithmic constants correctly bound log H0 from below,
log L0 and log(2*pi) from above, and pi on both sides. The count discrepancy
uses the decreasing functions log L/L and 1/L with L=log u>=L0, and the
same complete theta remainder. All rational substitutions in D2 are in
the safe direction. The exact main density is (1/pi)*log(u/(2*pi)); the
displayed lower and upper bounds therefore follow, and the lower ratio
improves at greater height. The endpoint convention is the unchanged
one-sided complete multiplicity count.

Only scalar constants in the already reviewed displacement argument change.
The same fixed-denominator polynomial sampling, arbitrary ordinate-dependent
complex shifts, whole exponential, signed-pole prefactor and Taylor depths
remain present. The exponent is below .173 and its complete exponential
below 1.19. The exact quadrature coefficient is 2*c_*(1+2d). The complete
conjugate-group quadratic lower polynomial decreases with q; its endpoint
q=.27 has the strictly positive rational gap checked in the author's
normal/optimized receipt. Every source factor and analytic multiplicity
is retained by the preceding accepted proof.

The global height condition is exactly 100*(900000)^2=27*H0, which is
allowed because the displayed endpoint gap is strict. The maximal even
order at H0 is therefore exactly 900000. Passing to smaller sizes by
appending distinct nodes and taking principal submatrices is valid.
The published complete critical-line census is used only to add back the
source below or at H0. The theorem remains finite global order and
increasing order for changing complete-tail kernels; it gives no RH proof.
