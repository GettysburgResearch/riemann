# Review record and smallest failure points

## Scope and status

This is a proposed standalone contribution, not an integrated theorem. The
proofs were written and reviewed by AI agents in the same working session.
Separate reviewers read the arguments and identified concrete corrections;
this is not a claim of an independent human referee, a formal proof assistant
check, or a complete verification of the external quasi-RH papers.

The published commit and SHA256SUMS bind the delivered version. The PR body
records the frozen head SHA for subsequent exact-commit review. No inherited
research file is changed and no previous claim ID is reused.

## Review performed

| Note | Separate review during this session | Finding |
|---|---|---|
| CRITICAL_SCATTERING.md | Source analyst read the entire proof; main author also read it. | Gamma/conductor normalization, same-character functional equation, paired Hadamard argument, Hardy projections, Gram orientation and finite-S repair checked. |
| PRINCIPAL_TWO_VARIABLE_FACTOR.md | Source analyst checked against the primitive Poisson formula; main author rechecked local algebra and convergence. | Exterior Möbius coefficients and physical X factor corrected; final version reread. Profile construction and Gaussian tails checked. |
| PRIME_MEMORY.md | Pole/calibration analyst read the complete note; main author derived it. | Integer ceiling in the tail cutoff corrected. Convolution sign, all-past Gaussian bound, energy identity and conditional RH implication checked. |
| SCATTERING_CONTROL.md | Pole/calibration analyst independently checked the formulas. | Causal and anticausal inverses, exact residue, norm identity and exponential energy constant checked. |
| POLE_CALIBRATION.md | Source analyst checked the invoked Laplace/Gram theorem; main author read the full note. | No rightmost-zero, spacing or simplicity premise enters the lower bound. Optional Kummer construction reviewed algebraically by author and main reviewer. |
| PRIME_DETECTOR.md | Source analyst read the full note and final Dirichlet extension; main author read it. | Continuum, finite-S zeros, left contour, Gaussian convergence, equivalence and Cesàro mean checked. Complex character reflection and zero at zero checked separately. |
| FOURIER_TRANSFER_AND_COVARIANCE.md | Main author read the complete argument independently of its author. | Local forward/inverse norms, phase dilation, square mass, Parseval, filter bound and coherent countermodel checked. |

## Corrections incorporated

1. The prime-memory cutoff is `ceil(exp(U+R))`. An unrounded real cutoff
   would not justify the stated decreasing-sum comparison with an integral
   starting at that same point.
2. The free-z convolution identities use the exterior ideal Möbius function
   `mu_F^S`; unrestricted Möbius would be wrong at omitted primes.
3. The full principal-residue normalization retains
   `X^(1/2-z0) Z^(z0-1)`. The X factor is not a fixed scalar on linked scales.
4. The two-variable divisor list retains numerator zeros as well as the
   reciprocal factor `zeta_F^S(6z+1)` and all relevant poles.
5. The Hardy inner-product convention is stated, and the Mellin indicator
   example specifies that a single jump endpoint is immaterial.

The source-specific CT lemma-number issue is reported in AUDIT_SCOPE.md.
It is not treated as a disproof of #959.

## Smallest statements requiring external review

For the scattering result, a defect in the completed angular character's
archimedean parameters or in its paired Hadamard quotient would invalidate
the claimed operator. The note supplies both formulas and their proof. The
finite check does not certify the infinite canonical product.

For the free-z result, the primitive local `w=1` specialization and the
physical-scale normalization are the first load-bearing interfaces. Its
noncancellation theorem also needs the stated absolute local majorants.
Independent derivation of a signed projection estimate remains entirely open.

For the pole calibration, the critical points are the Gram orientation,
factorial in the differentiated Laplace evaluation, and the passage from
Abelian weighted energy to a limsup. All are written out. The lower bound
does not imply an effective onset or a bound at every large horizon.

For the prime detector, the classical logarithmic-derivative contour bound
and zero count justify the infinite formula. The source's continuum and all
finite-S zero grids are essential. Boundedness of the arithmetic detector is
unproved; no part of the review asserts it.

For Fourier transfer, the forward and inverse weighted coefficient norms
are uniform only at each fixed exponent greater than `1/2`. The unconditional
logarithmic result imports established uniform phase theorems. It gives
neither every growing-shift estimate nor an RH power bound.

## Verification boundary

The finite scripts independently reconstruct algebra, complete finite
coefficient streams, exact rational Gram examples, and normalization checks.
Normal and optimized Python are both run on the final packet. Some Gaussian
checks and the optional prime trajectory use binary64, explicitly without
directed rounding. No actual zero values, reciprocal derivatives, algebraic
number-field computation, transitive Lean audit, full repository test suite,
or remote CI result is claimed.

No component establishes OPEN-PR, OPEN-PM, or the prime detector's boundedness.
A defect in an analytic proof is not repaired by a passing finite checker.
