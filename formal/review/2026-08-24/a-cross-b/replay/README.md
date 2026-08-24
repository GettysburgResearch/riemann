# Cross-review replay

`verify_cross_review.py` performs exact rational/symbolic checks of the finite algebra accepted in this review:

- rows 2/3 elimination and fixed 5:3 factorization;
- generic three-tap determinant and four-tap factorization;
- 51 half-divisor coefficient convolutions;
- 500 Dirichlet-convolution evaluations of `eta * eta`;
- 120 one-field convolution evaluations;
- generic first-owner fixtures;
- 41 finite Abel summation fixtures.

It deliberately does **not** claim Lean compilation or prove the stronger canonical first-owner, source-typing, wavelet-frame, or Mellin-consumer statements.
