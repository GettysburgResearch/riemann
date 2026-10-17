# Validation and scientific limits

Status: same-author proof and code checking, not independent review.

## What was executed

- python verify.py and python -O verify.py, with byte-identical CHECKS.json.
- Three separately executed optimized processes with --mutate tensor,
  --mutate dimension and --mutate inert_sign. Every process exits nonzero;
  MUTATIONS.json records the actual final error lines. Checks use explicit
  exceptions, not assertions removed by optimization.
- python numerical.py and python -O numerical.py, with byte-identical
  NUMERICAL.json. These require mpmath and use 45 decimal digits; they are
  not directed interval/ball arithmetic.
- The preceding norm-fiber manifest and ordinary/optimized exact checker
  were freshly replayed from the supplied archive. Both outputs agree with
  its historical CHECKS.json. This does not independently certify its proof.
- Every file in the local recovery archive was compared byte-for-byte to
  the earlier unpushed 14-file packet. The already-published ramified-dilation
  recovery is separately credited to #954, not republished as new work.

## Exact diagnostic coverage

35555 finite predicates are counted, including repeated setup and guards.
They are NOT 35555 independent arithmetic instances or asymptotic tests.

- 80 formal local cases: k=1,2; m=2,3,4,6; five splitting patterns; p=49,121.
  These square-valued formal prime parameters make odd-m critical weights
  rational. They are not asserted to be rational primes or actual field
  splitting computations. Balance, leading coefficient, signed inversion,
  and coefficient reconstruction through balanced degree 4 are checked.
- 262 complete transport-cap configurations, containing 6718 feasible
  matrices, including unequal cap sums. Deficit encoding is independently
  checked for injectivity, and the displayed count bounds are tested.
- A complete ideal enumeration through norm 1024 includes every good
  squarefree Eisenstein ideal, with 286 total ideals including the unit.
  Both split conjugate ideals are separate. Independent rational Euler
  assembly checks every norm fiber. The two assemblies share the classical
  splitting law; they are not independent number-field backends.
- 15 full norm-product census cases at orders 2,4,6 and six norm caps, with
  the exact case coverage in CHECKS.json. Direct ideal-k-tuple enumeration
  separately checks the six cases with caps 32 and 64. There is no random
  sampling, no selected-prime-semigroup substitution in these censuses,
  and no physical theta-row census claimed.
- 501 coprime transport arrays are reconstructed by gcd. Lower-bound
  interior grid points and margins are checked separately from the upper
  transport enumeration. Their finite counts do not prove asymptotic abundance.
- The Gaussian Gram constant is checked using an exact rational Taylor
  lower bound e^2>7. Three small finite actual native polynomials have their
  Gaussian-twist moments evaluated by direct high-precision quadrature and
  by the finite coefficient Gram formula. All errors are below 1e-32.
  Quadrature is not used to test a rapidly oscillating X^k-scale window.

## Proof audit

The written proof explicitly retains: individual column caps; both sides
of the norm-balance relation; the signed local quotient and its absolute
critical norm; bad primes; nonunit zeros; finite versus growing k; the
same physical row measure; the Gaussian tail; all unequal-norm terms in
the long average; and the exact X^k averaging price. In the dyadic Gaussian
extension, annuli with rescaled cap below 1 contain no ideals; rescaled caps
in [1,2] are bounded directly by their finite norm fibers. Thus Theorem 1
is not invoked outside its X>=2 domain.

The lower bound uses only the principal native source over the Eisenstein
field, a nonnegative hard annulus, and one fixed excluded-prime set. Its
small-prime cutoff is chosen ONCE before X tends to infinity. It is not a
lower bound for arbitrary row profiles, coupled sources or changing exclusions.

The earlier native equal-norm 'signed' sector actually has one sign termwise.
Its previous positive asymptotic is not disproved, but its interpretation as
an achievement in cancellation is corrected. The new complete mean estimate
also does NOT claim fixed-twist signed cancellation. The unsigned-profile
example in Section 8 authenticates that limitation at the power level.

No independent agent/human referee, proof-assistant elaboration, upstream
theta reconstruction, full-repository validator or remote CI was run.
Hashes authenticate bytes only. All claims remain PROPOSED pending review.
