# Sources, exact boundaries, and same-author mathematical audit

This is a self-audit by the author of the proofs and checker. It is not an
independent referee report or a claim of worldwide mathematical priority.

## Sources actually used

1. **Parent #993:**
   https://github.com/GettysburgResearch/riemann/pull/993
   Head: `5569defd8d77f1f8f3586b326577aacb384ffb23`.
   Packet tree: `85a82f251b67a14ecd16836a23f8f737daae08e4`.
   The complete delivered packet was extracted, its proofs read, and its
   original normal/optimized replay and seven corruption cases rerun.
   RECTANGULAR_JETS.md provides the independent-jet rank lemma, ordinary
   Frobenius divisibility, normalized height and exact floor template.
   ZERO_PRESERVING_ROUTE.md provides the complete primitive integer and
   one-sided-continuum Mellin identity. The new proofs do not infer that
   the parent's infinite statements are certified by its finite checker.

2. **Original OpenAI source, classical analytic interface only:**
   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex
   TeX blob: `7e41c77c252348369ca0fb99cbe389271ba6ce86`.
   The source's Hadamard identity and prime-bias section were read through
   the live connector at this pin. Only the classical nonprincipal real
   Dirichlet logarithmic derivative is used. The paper's no-Siegel-zero
   conclusion, any quasi-RH bound and its formal implementation are NOT
   premises. Its standard analytic reference is Davenport, Sections 12,14.

3. **Akiyama--Kaneko, Curious congruences for cyclotomic polynomials:**
   https://arxiv.org/html/2204.11267v6
   Primary HTML read: the cyclotomic product (1)--(2), Remark 2's
   Phi_n(1)=exp Lambda(n), the first derivative and Jordan/Lehmer discussion.
   These identities are credited as classical. The paper is not claimed
   to prove our matrix regularization estimate. No source text or PDF is
   redistributed and no license to the paper is inferred.

4. **NIST Digital Library of Mathematical Functions:**
   https://dlmf.nist.gov/4.36  (sinh product)
   https://dlmf.nist.gov/2.10  (Euler summation)
   These primary formula references were read. The exact variation measure,
   noninteger endpoint and constants needed here are worked out in the proof,
   rather than asserted to appear verbatim in the reference.

5. **Classical analytic background:** finite Fourier inversion, resultants,
   Mertens' first prime estimate, Chebyshev's elementary bound, zeta's Euler
   product and functional equation, and Landau's nonnegative-transform lemma.
   The elementary forms necessary for the new deductions are restated or
   proved. Standard RH=>psi(x)-x=O(sqrt(x)log^2 x) is used only for the reverse
   direction of the stated equivalence, not for either unconditional estimate.

The supplied five-page note was already imported by #993. Its printed
identifier is hexagon:2610.00311v1, not an arXiv identifier. Its printed Ben
Green attribution remains unauthenticated. No new authorship or PDF-rendering
verification is claimed in this continuation.

## Audit of the main fixed-source route

- H_n retains complementary modes with eigenvalue one. Replacing the primitive
  projection by identity reintroduces a zero mode at mass zero.
- The resultant sign cancels the product of primitive roots. At n=2 it gives
  D_2(t)=t+4, not t or its square. All prime powers remain in Phi_n(1).
- The cycle-polynomial recurrence and the rational-matrix LDL construction
  are separate finite paths; they share elementary arithmetic and this author.
- The complete divisor regrouping removes n=1 explicitly. The unit correction
  cannot be discarded just because it is small asymptotically.
- Euler summation pays the derivative jump at the nonintegral endpoint N/m.
  First-order quadrature is insufficient for the logarithmic claim.
- The tail of B(c), the finite unit term, and the change from hyperbolic to
  rational mass all have separate explicit budgets. No finite expansion is
  substituted for the infinite constant in the theorem.
- Positivity controls a matrix, not its critical centered height. The O(log N)
  bound is a displacement estimate and must NOT be called an O(log N) prime
  error. OPEN-PH is still RH-strength.
- The one-sided Landau argument retains finite initial intervals, the real
  convergence abscissa, removal of the pole at one and every zero multiplicity.
- The drift's Mellin transform has denominator zeta(s+1). A sharp large-c
  asymptotic for it would need proof; it is not a free way around the zeros.
- The raw Hadamard bound and its N^3 scale are disclosed as a failed closure
  attempt. No claimed source-specific N^(3/2+epsilon) bound was obtained.

## Audit of the shorter conductor range and complex-zero budget

- The condition is R>=64 sqrt(q) ceil(log(2R))^2, NOT R>=sqrt(q) alone.
  Every floor/ceiling and the strict rank margin remain in the proof.
- The p-adic comparison uses only the template as a LOWER bound on valuations;
  it is not equality to the actual determinant valuation.
- Primes below P and all ramified primes/prime-power tails are paid explicitly.
- The initial y<log(q)/2 range uses classical Mertens, not the new bound outside
  its stated range. The extra logarithmic threshold is included before Laplace
  integration.
- The full Hadamard zero sum is positive. Nonreal conjugate pairs cost twice
  the multiplicity; a real zero is not duplicated. The example disks have
  compact scaled-coordinate qualifications and shrinking physical radius.
- No fixed complex strip, improved simple-real gap constant, unverified
  actual L-value or numerical zero is claimed.

## Priority independent review

Review the exact matrix/cyclotomic identity and the endpoint-aware variation
proof first; then the one-sided Landau consumer. Separately review the parent's
rank/divisibility lemmas and the new short-support constants, followed by the
complete Laplace transfer and conjugate-zero geometry. Finite agreement is
useful error detection, not acceptance of these infinite arguments.
