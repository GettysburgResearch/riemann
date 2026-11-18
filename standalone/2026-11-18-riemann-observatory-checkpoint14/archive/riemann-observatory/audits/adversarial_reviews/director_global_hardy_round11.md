# The global Hardy certificate and its parameter refinement

18 November 2026. The director read the original and independently reconstructed global proofs, their complete mathematical implementations and the parameter review. The result is the unconditional critical-line series enclosure

```text
0.61649875288731141829 < C2 < 1.075561.
```

There is no new zero census. The lower endpoint remains the complete finite sum through10000. The entire remaining tail is bounded by0.45906151 using the rational choices below. RH is used only to identify this critical-line series with the earlier tapered-array limit. The exact conditional quartic splice near0.65339 remains observational because its numerical error constant is unallocated.

## Why one global cutoff helps

Use G(t)=Q2(1/2+it)Z(t), and f=phi*G/t, with a cubic transition on[Y-w,Y] and phi=1 afterwards. Separate real-component variation gives the whole positive-height derivative tail bounded by ||f'||_2||f''||_2; reflection doubles this. The block estimates prove f',f'' in L2. Then each squared component derivative has integrable derivative and a limit at infinity, which must be zero by its integrability. This justifies the last endpoint of the variation argument without an unproved decay assertion or an omitted upper cutoff. The denominator1/(gamma^2+1/4) is bounded by1/gamma^2.

On a block[T,U], use a fixed Euler polynomial M=ceil(dT), phase center half log(sqrt(TU)/(2pi)), and weight t^-2. Integrating the off-diagonal Hilbert forms gives total endpoint/variation weight2/T^2. Hence its error is3pi*J_j/T^2, whereas the exact diagonal length is1/T-1/U. J_j retains the sparse even-frequency gaps and the first-tail-even exception. Finite centered moments are bounded by exact small sums and a trapezoid plus total-variation inequality, with every turning point included. The infinite geometric remainder uses decreasing normalized coefficients and an explicitly summable log-power envelope.

The Euler remainder uses both Fourier signs of the periodic Bernoulli function. Its amplitudes divided by their nonstationary phase derivatives decrease to zero; integration by parts, Abel damping and dominated convergence justify the summable mode bounds. The admissible complex rectangle keeps the positive mode away from stationarity and the gamma arguments in positive real parts. Horizontal digamma integration bounds the holomorphic Hardy multiplier; the circle maximum is attained at the lowest real part because M^2>T. Fixed Cauchy radii give derivative norms, followed by the real-axis Q2 product rule. Different block phase centers are permitted because the norm bounds are separately applied to the same G on disjoint intervals.

## Exact cutoff terms and rational replay

For H=G/t and the cubic phi, integration by parts gives

```text
||f'||² = integral phi²|H'|² − integral phi phi''|H|²,
||f''||² = integral phi²|H''|²
          + integral (2phi'²−4phi phi'')|H'|²
          +12|H(Y)|²/w³−12Re(H'(Y) conjugate(H(Y)))/w².
```

The second identity uses one-sided cubic derivatives at Y; f' remains continuous and f'' exists almost everywhere. The transition coefficient is24x^3(2-x)/w^2. Endpoint quantities are evaluated by Arb using Q2*zeta/t: its Hardy phase has modulus1 and adds only an imaginary term to H' conjugate(H). Thus no phase approximation is needed at that point. The signed correction is retained; here its real cross term is negative, so it increases the bound.

The selected rationals are r=1607/1000,d=143/500,w=22,a1=219/1000,a2=433/1000. All complex-rectangle, residual-envelope and monotonicity inequalities are explicitly asserted, valid from T0=9978 onward. The source search evaluated313 proposals and rejected five; it proves no optimality. Separate128-bit and192-bit replays give the complete tail upper expression0.4590615084631102969276294270... . The independent earlier global construction gives a weaker bound using different quadrature estimates, and the variable-phase alternative was also checked but is weaker. The original pinned programs remain unchanged.

At Y=2.8 million the same parameter proof bounds the tail below0.00591413. A complete finite sum there with width below0.00025 would suffice for a one-percent enclosure relative to the existing lower bound. It was not computed. A coefficient-series tail is still not the near-function tail in the separate finite-length prime-array remainder.

[Global proof](prime67_global_hardy_tail.md) · [Independent reconstruction](weighted67_global_skeptic.md) · [Parameter proof](prime69_parameterized_hardy_tail.md) · [Independent parameter audit](weighted69_hardy_parameter_review.md)
