# X-105221 square-defect and debt-free-flux replay

This lightweight standard-library replay checks:

- the exact moment identity
  `sum (1+lambda*rho)^2 = R - 2 lambda M1 + lambda^2 M2`;
- wrong-extremum domination by the square defect;
- a source-matched interpolation fixture for
  `p(x)=x^4-2x^2+2`;
- the exact multilevel descent arithmetic;
- the numerical value of the literature-instantiated `k=3` 90% threshold.

It does not prove a uniform interpolation boundary bound, 90%, density one,
or RH.
