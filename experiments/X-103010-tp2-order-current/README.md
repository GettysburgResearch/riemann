# X-103010 — TP2 order-current replay

This standard-library replay checks:

- the explicit logarithmic two-box spline;
- the equation `(D-1/2)A=A_-` away from knots;
- monotonicity of `A_-/A`;
- thousands of translated Wronskian signs;
- thousands of TP2 minors;
- a source-blind coefficient mutation which reverses the physical sign.

The analytic theorem is proved in the claim files. The replay is a finite regression and does not prove `DORI103010`, `BCI102990`, or RH.