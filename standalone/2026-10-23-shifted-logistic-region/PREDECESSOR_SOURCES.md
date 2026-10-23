# Sources and review boundaries

The unchanged kernel, logistic explicit formula, finite RH verification,
published Littlewood region21.233, and zero-tail inputs are listed in
[BASELINE_SOURCES.md](BASELINE_SOURCES.md). Their original scope is
preserved. In particular, the finite verification to3*10^12 is imported,
and no thesis-dependent Littlewood coefficient19.62 is used.

The new inputs are:

1. Kevin Ford, *Zero-free regions for the Riemann zeta function*, corrected
   [arXiv:1910.08205v5](https://arxiv.org/pdf/1910.08205v5), dated
   18 February2025. The proof uses intermediate explicit-formula,
   Euler-product smoothing, and kernel-remainder lemmas, rederived for
   the new degree and weights. The final numerical theorem is not an
   input. The incompatible printed expressions after9.3 and in9.6 are
   avoided by using the compatible source7.5 and7.8 bounds directly.

2. Michael Revers, [arXiv:2602.05614v1](https://arxiv.org/html/2602.05614v1),
   equation3.32, the critical-line estimate for t>=8.97*10^17. This is a
   preprint dependency. The negative constant is discarded. The proof
   here constructs a global shifted envelope and integrates it over
   the complete smoothing line.

3. Hiary, Patel and Yang, *An improved explicit estimate for zeta(1/2+it)*,
   Journal of Number Theory256 (2024), Theorem1.1, supplying
   |zeta(1/2+it)|<=.618*t^(1/6)*log t for t>=3. This bounds the finite
   prefix of the shifted Revers envelope. Its full proof is imported.

4. The cosine hyperbolic product and the Bernstein representation of
   completely monotone functions supply the Gaussian-mixture positivity
   of the quadratic frequency profile. Exact source details and the
   closure proof are in three-hour-boundary/SHIFTED_SECH_POSITIVITY.md
   and QUADRATIC_SIGMA_LOGISTIC_DETECTOR.md.

The Hadamard-kernel comparison and the combined prime retention are
proved in this packet. Their numerical constants and polynomial covers
have separate exact checkers. The user reports guided the search; their
predictions and expert intuitions are not proof premises.

No claim of priority over unpublished work or author posts is made.
Internal agent review does not constitute journal review or repository
integration approval.

