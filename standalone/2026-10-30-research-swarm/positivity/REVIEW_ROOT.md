# Root review of the reciprocal-density packet

Reviewed source: `report.md`, SHA-256 `e3cfe184ea2aa3c7d1ec0b42a62225ce2ed789eb0dee98fe2c9627f21d6ba02b`.

Status: no blocking error found in the stated elementary proofs and finite source-qualified corollary. This is an internal mathematical review, not formal verification, external peer review, or an audit of every external probability theorem.

## What was reconstructed

- The differential removal operator and the fourth-order curvature identity, including the positivity condition needed before division.
- The score calculation: `f''/f=r²-r'`, the bound `0≤r≤a`, and the precise distinction between positivity after removal and preservation of log-concavity.
- The cofinal positive-series argument. A nonreal pole survives every finite real-zero product; positivity would force a positive-real singularity at its radius, which a sufficiently long deletion contradicts. This remains a conditional criterion.
- The finite `V≤U/8` corollary against Sra v2 Proposition 3.3 and Appendix C.2–C.4. The two retained ordinates are available from the stated counting bound. The gap `η−a≥U/12` pays the tilted derivative denominator. The bound `48U(log U+1)exp(-2πU/3)` covers both signs of the tilt.
- The countermodel's mass, bilateral transform, curvature, and two differential removals. In particular, `g''=4-g` and `g'^2=10-(g-4)^2` give the displayed curvature numerator `6-4g`.
- The global strict log-concavity estimate for the preceding Laplace convolution, with the bounds on its explicit coefficients and the exponential comparison valid on `x≥0`.
- The first absolute moment `11/10` and the total-variation translation estimate.
- The infinite smoothing construction: its rate counting gives an order-one entire reciprocal and super-exponential Fourier decay, while its variance is at most `12/R²`. The derivative bounds used in the Taylor errors are valid across zero: the even base density has the required continuous derivatives. The positive curvature after the first removal and negative value after the second survive the stated smoothing errors.

## Qualifications retained

The finite corollary proves strict log-concavity in the two-point sense. Real analyticity alone does not show that the second derivative of the logarithm is negative at every point; the report correctly avoids that stronger claim.

The countermodel is not asserted to be PF256 or to share all arithmetic and zero-distribution properties of xi. It refutes the stated generic PF2/total-variation/entireness bootstrap only.

The numerical probe evaluates the actual reciprocal xi characteristic function, but uses ordinary floating point and rounded zero centers. Agreement of two quadrature resolutions is not a tail or interval certificate. No proof conclusion depends on those samples.

The missing all-height source invariant is not supplied by this review or by the finite corollary.
