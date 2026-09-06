# Classical and software inputs

These are inputs, not newly proved results of the repository review.

* MPFR4 correctly rounded elementary/zeta primitives and directed conversion;
  GMP and Boost arbitrary-precision integers;64-bit platform/ABI and compilers.
  The exact MPFR4.2.2 library was used, with a fallback public ABI header because
  the vendor header was absent. Official documentation:
  `https://www.mpfr.org/mpfr-4.2.2/mpfr.html` (rounding and conversion sections).
  The C++ replay turns directed bounds into integer endpoints before all sums.
  Two compilers do not constitute two independent special-function backends.
* Classical theta/xi functional equation, the sinh product, gamma duplication,
  Mellin/Laplace inversion and Rouché. R27 derives the Brownian normalization
  from these identities and checks the moment/continuation conditions.
* Gamma/trigamma integral and Euler logarithm on sigma>1. R26 reconstructs the
  compensated safe source. Nakamura's reference is T.Nakamura, "A complete
  Riemann zeta distribution and the Riemann hypothesis", Bernoulli21(2015),
  604–617, DOI10.3150/13-BEJ581; `https://arxiv.org/abs/1504.03438`.
  The paper's abstract distinguishes quasi-infinite from infinite divisibility;
  this review imports no RH-conditional positive continuation.
* Euler–Maclaurin/Hurwitz-zeta ramp bound L-93600 as reconstructed in pass3R21,
  with the actual source fixed. This analytic input is necessary for the new
  all-real P61 tail, independently of the new finite computation.
* Elementary Chebyshev and the classical quantitative PNT/Mertens bounds for
  S26/S27. Only a decay faster than any fixed inverse logarithm is needed for
  the long-sector asymptotic; no RH bound or explicit numerical threshold is
  asserted. Haar fine-mode bounds need only Chebyshev.
* Python integers/Fraction and SymPy exact symbolic simplification in the
  bounded checker. Numerical approximations used during authoring do not enter
  acceptance. The retained proofs and bounded checks remain subject to normal
  mathematical and implementation review.

No external zero census, original high-ordinate xi primitive, Lean build,
Comparator, Nanoda or remote CI run was performed in this pass.
