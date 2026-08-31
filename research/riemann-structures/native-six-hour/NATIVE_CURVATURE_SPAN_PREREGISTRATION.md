# Complete finite native curvature span: acquisition plan

This declaration precedes execution. The calculation uses the original half-source on the fixed primes `(2,3,5)`, physical product horizon 25, and every ordered pair `(n,m)` with `nm <= 25`. The predecessor has exactly 63 such records. No prime search, field enumeration, coefficient fitting, or selection of successful rectangles is permitted.

## Source and normalization

Write the coefficient of the actual half-source as `Lambda_n(u)/sqrt(n)`, where

    Lambda_n(u) = [x^v(n)] product_p
        (u_p sqrt(1-x_p) + (1-u_p) sqrt(1-x_p^2)).

The new producer reconstructs these rational three-variable polynomials directly. It authenticates the global source certificate at `7ff5ddbb8f35055085faca7d46fdddb0f12715ae`, its acquisition at `5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4`, and the original source notes before importing any executable helper. The complete diagonal path is compared with the frozen literal 63-record source, not merely its final observed energy.

For each coordinate pair `i<j`, retain the complete rational coefficient vector

    C_ij(n,m;u) = 2 (partial_i Lambda_n partial_j Lambda_m
                       - partial_j Lambda_n partial_i Lambda_m).

The physical vector is `C_ij(n,m;u)/sqrt(nm)`. Product collapse, exchange, and unit-coordinate checks take place in the original 63-record space. They must hold coefficient by coefficient, before parameter evaluation or the observation.

## Predictions fixed before execution

The horizon excludes every product involving all three distinct primes. The predicted coefficient supports are:

- pair `(2,3)`: `1,u_2,u_3`;
- pair `(2,5)`: `1,u_2`;
- pair `(3,5)`: `1`.

The six coefficient vectors are predicted to be linearly independent. This is a prediction about actual rational source vectors, not a dimension inferred from a trace or Hilbert numerator. The scout retains the full vectors and exact rank pivots even if a prediction fails.

The observation first coalesces equal physical ratios. For a reduced ratio `a/b`, write `(n,m)=(ad,bd)`. After factoring the common nonzero scalar `1/sqrt(ab)`, the exact rational row is

    sum_d C_ij(ad,bd;u)/d.

The six resulting rational vectors are predicted to retain rank six. A separate normalization control records `C_23(2,3)=1/2`, the `u_2` coefficient `C_23(4,6)=3/16`, and the latter's coalesced ratio `2/3` coefficient `3/32`. Omitting the `1/d` factor must change this control. Interpreting the rank as an observed Hilbert-space rank additionally uses the original measure and independence of the distinct Mellin frequencies; no replacement observation is introduced by the rationalization.

## Fixed rectangle witnesses

All rectangles have half-width `1/16`; their unused coordinate is `1/2`. The ordered centers are:

1. pair `(2,3)`: `(1/4,1/4)`, `(3/4,1/4)`, `(1/4,3/4)`;
2. pair `(2,5)`: `(1/4,1/2)`, `(3/4,1/2)`;
3. pair `(3,5)`: `(1/2,1/2)`.

For each rectangle, compute its full curvature integral and independently integrate the native one-form `2 dLambda_n Lambda_m` on all four edges. With this convention, the difference is **j-then-i minus i-then-j**. The reversed sign is retained as a counterfeit. The two monotone paths have a common monotone prefix from the origin to the lower corner and a common suffix from the upper corner to `(1,1,1)`. The producer also integrates these common pieces and checks their exact cancellation record by record.

All six resulting source vectors and their ratio-coalesced images are predicted to have rank six. Relative to the six coefficient vectors above, the rectangle transition determinant is predicted to be `1/(8*64^6)`, from their common area and the fixed center differences. No rectangle is changed after seeing a rank.

## Resource and acceptance scope

Only `Fraction` arithmetic is used. Polynomial caps are three variables, coordinate degree two, total degree six, 64 terms, and 512-bit rational coordinates; one-variable edge polynomials have degree at most eight. Exact elimination has at most 63 rows and 12 columns. Frozen source inputs are capped at two MiB each and the discovery output at four MiB. All original-coordinate vectors, polynomial coefficients, ratio weights, rectangle edge integrals, and rank pivots are retained.

The scout has only `--discover`; root alone executes it under the existing RAM guard. Prediction mismatches are recorded, while a failed exact source or integration identity is an error. The output binds this declaration and the producer bytes. This is a finite native half-source span calculation. It does not identify the full post-renewal gamma field, the T106140 diagonal, every path-space holonomy, or a global moment obstruction.
