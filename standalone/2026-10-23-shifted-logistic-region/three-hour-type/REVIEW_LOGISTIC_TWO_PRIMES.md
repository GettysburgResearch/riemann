# Independent review of the exact two-prime contribution

Reviewed 2026-10-21 against:

* `../three-hour-boundary/LOGISTIC_TWO_PRIME_GAIN.md`, SHA256
  `fd4773be0ce4d54ac8ec845c1cb3904a01224008660460973d7056066bde1405`;
* `../three-hour-boundary/verify_logistic_prime_minima.py`, SHA256
  `059c9c069618e2d8988faea5465403bb85442e513ab580d0233822b1c7dacda6`.

The logistic identity in (P1) is exact, and the cosh monotonicity gives
the stated direction for every sigma in [1/2,1]. The proof checks that
the Taylor lower bound for w is positive at every retained prime power
before multiplying this inequality. The linear term can then use the
uniform minima of G, while the negative cubic error uses P<=P(0).
The powers of log p and the two powers m^2 in the error are correct.

The checker reconstructs the exact source polynomial. Its Chebyshev
recurrence computes cos(mkx), its substitution y=2u-1 has the correct
binomial signs and powers of two, and the power-to-Bernstein formula
is valid at the declared full degree. In midpoint subdivision the
integer additions and final denominator multiplication by 2^degree
correctly represent every de Casteljau average. Strictly positive
Bernstein coefficients certify the entire closed subinterval. The
endpoint and adjacency checks give full coverage, not a grid sample.

The rational logarithm enclosures, linear/cubic comparisons, and
positivity checks were replayed successfully. The deliberately false
lower bound is rejected at an exact endpoint. The result is the stated
uniform prime-side contribution 1.1447 eta-2775 eta^3. No repair was
requested. The global zero-free deduction still requires the separate
master inequality and analytic wrapper.
