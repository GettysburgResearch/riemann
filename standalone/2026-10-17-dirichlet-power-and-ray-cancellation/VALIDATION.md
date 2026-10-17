# Reproduction and exact scope of the finite checks

Run `python replay.py` in this packet. The wrapper checks SHA256SUMS when
present, copies each standalone checker into a fresh temporary directory,
runs it in ordinary Python and with `python -O`, and compares its generated
report bytes to the archived report. All mathematical gates in the scripts
use explicit exceptions; optimization does not remove them.

The scripts use only the Python standard library. Reports contain finite
identities and normalization checks. They do not certify analytic
continuation, zero-free regions, asymptotic constants, or RH. The complete
analytic arguments and their exact hypotheses are in the proof documents.

## Finite inverse identity and complete norm source

`check_direct_identity.py` independently constructs fixed character arrays,
Dirichlet convolutions and formal inverses through 2048. Its archived
DIRECT_CHECKS.json records:

- 16 inverse-identity configurations and 32,768 exact coefficient comparisons.
- 25,536 complete q-supported cofactor cases, retaining the entire prime
  valuation rather than only gcd(n,q).
- 51,072 exact reduced rational-phase comparisons.
- Complete Eisenstein norm coefficients through 2048, checked against the
  split, inert and ramified local Euler factors.
- 62 exact rational exponent budgets, for kappa=1/3 through kappa=1/64.
- Five rejected corrupted constructions: a dropped final inverse term,
  gcd in place of q-infinity, erased ramified character zero, a false
  one-bounded native coefficient, and a wrong closed support endpoint.

The five negative controls are explicit corrupted constructions evaluated
inside the checker. They are not five external mutation-test processes or
independent proofs of the corresponding analytic lemmas. The rational
exponent fixtures verify arithmetic in their finite examples, not every
real parameter covered by the written theorem.

## Native ideal rays and the actual angular hull

`check_native_angular_rays.py` enumerates all 616 Eisenstein ideals modulo
the six units through norm 1024. It checks all 307 ideals good for Q=6,
including those with zero Mobius coefficient, against a separate exact
prime-ideal factorization. Fraction arithmetic verifies angular phases
and primitive-ray collision classes. Original ideal sums and the grouped
native ray source are compared without randomizing their coefficients.

At X=512 the exact native ray diagonal is 72. The finite fixture's unsigned
squarefree control has diagonal 76. This finite control differs from the
all-positive ideal source in Section 8 of the proof; the two comparisons
are not silently identified. The finite Gaussian mean at R=512 and t=0
is approximately 72.000000029983. Direct angular summation and the
periodized Gaussian kernel agree within 10^(-12) in the four tested cases.
These are ordinary binary64 normalization checks with truncated numerical
tails, not certified intervals. The mathematical proof retains full tails.

The separate hull fixture compares the direct split/inert Euler factors
with convolution of zeta_K^S(s) by 1/zeta_Q^Q(2s)^2 through rational norm
200000, coefficient by coefficient using exact integers. Its cumulative
density 0.25135 at that cutoff is compared with 9sqrt(3)/(2pi^3), about
0.251375833172. This is a finite normalization check. The asymptotic formula
comes from the written convolution and lattice-count proof.

## Capped completion and the maximal endpoint partition

`check_capped_norm_transfer.py` and CAPPED_CHECK_RESULTS.json contain exact
finite checks of the cap, local-source and endpoint operations in
COMPLETION_AND_COVARIANCE.md. The report records the actual fixture ranges
and rejected corruptions. These checks authenticate finite identities and
partition invariants; no observed finite cancellation is substituted for
the conditional native Fourier theorem.

All of these fixtures use exact integers and fractions. They include 40
complete norm cases with 2,380 ideal-local and 10,240 norm-aggregate
coefficient checks; 1,086 largest-factor tuples, retaining 156 ties and
437 shared-prime tuples; three complete cap cases with 228 correction
tuples and 288 output coefficients; and nine BV atomic terms checked in
96 coefficients. The maximal step has 24 endpoint partitions, 408
residual-prefix checks and 384 endpoint inequalities. Its 51 full-shift
quadratic expansions are exact finite correlation identities, not a
sampled Fourier transform. Six exponent cases and three explicit negative
controls complete this report. Odd powerful degrees are not numerically
sampled here; the written local mass proof covers every integer m>=2.

## Review and publication boundaries

REVIEW.md records the mathematical cross-reviews and corrections made in
this session. They are not external peer review. No fresh transitive Lean
build of OpenAI, Cureton--Thorner, Liu, or this repository is claimed.
No zero census, numerical L-value experiment, global repository validator,
or GitHub CI success is implied by these component checks.

SHA256SUMS authenticates the archived packet bytes, excluding itself.
REPLAY_RESULTS.json records a fresh replay of the three finite reports in
both Python modes. It is a reproducibility record, not a proof certificate.
Remote Git tree and blob identity are checked separately at publication.
