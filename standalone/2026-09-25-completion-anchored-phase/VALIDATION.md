# CAP36 validation record

## Exact primitive replay

The final checker successfully regenerated the receipt in normal and optimized
Python. Pristine CLI tests require byte-identical output to the shipped JSON.
Acceptance uses integers, Fraction arithmetic and Gaussian rationals only.
There are no floating-point decisions or Python assert statements in check.py.
JSON comparison is type-sensitive after canonicalization and rejects duplicate
keys. A bool substituted for an integer is not accepted as equal.

The receipt records **53,304 explicit predicates**. Most are repeated native
prefix-preservation checks across declared caps, not independent RH evidence.
It separately reports 21,904 ordered bilinear-source terms and 34,300
factorwise compressed-kernel terms as coverage, NOT extra predicate counts.

Coverage:

- Every Mobius coefficient through 8192, prime-sieve generation checked against
  a separate triangular Dirichlet inverse. A changed coefficient at 30 actually
  triggers the primitive mismatch guard.
- All cap cutoffs Y=2,...,256, and Y=511,1023,2047,4095. This includes complete
  native prefixes, cap-three support and balance, entire completion energy,
  cubic point/width estimates and the rational anchored-error envelope.
- Two complete repaired amplitude-envelope controls at every such cutoff.
  Their early constant primitive cells are retained. These are arbitrary
  Gaussian-rational vectors satisfying the envelope, not fabricated real
  anchored arithmetic phases.
- All compressed defect coefficients and prime-product/divisor-sum kernels
  at Y=2,3,7,15,31,63 for rational damping and Gaussian-unit multiplicative
  controls. Inverse/composition algebra of the balanced multipliers is exact.
- Ten complete rational product-kernel panels at the first five cutoffs for
  both controls, including every source pair, independent product collisions,
  the four-factor compressed kernel, early-repair invariance and both tensor
  residual terms. The wrong Hermitian replacement gives a real discrepancy.
- 56 off-grid anticausal Abel identities for the profile 1/t, plus its norm
  controls. 257 rational tests of the phase-multiplier normalization and its
  exact maximum at tau=3/4. Universal real-phase statements use the proof.
- Nonzero uncompressed leakage -2/3 at coefficient 9, its rational masked
  pairing -2/177147, and the extra -1/4 term at the first-gap endpoint 6.

The exact dyadic endpoints in receipt.json enclose exact rational values.
They involve no transcendental computation. For illustration, at Y=4095 the
completion has width 6; the bound D/tau^2 is about 6.04e-7, and
D/(tau^2 F_Y) about 4.01e-7. These are finite envelope sizes, not fitted
asymptotic laws or certified evaluations of the actual harmonic observable.

## Actual CLI acceptance/refusal tests

All eight test methods in test_replay.py completed successfully in both normal
and optimized modes, in two four-method invocations per mode. Each mode covers
pristine normal and optimized child processes, followed or preceded by seven
actual malformed/altered receipt refusals: changed completion width, primitive
hash, complex pairing, missing scope, boolean-for-integer substitution,
malformed JSON, and a duplicate key. A refused input produces no output file.

Executed grouping (repeat with -O before test_replay.py):

```sh
python -I -S -B test_replay.py -v \
  ReplayTests.test_altered_completion_width \
  ReplayTests.test_altered_complex_pairing \
  ReplayTests.test_altered_primitive_hash \
  ReplayTests.test_boolean_number_substitution
python -I -S -B test_replay.py -v \
  ReplayTests.test_duplicate_json_key \
  ReplayTests.test_malformed_json \
  ReplayTests.test_missing_scope \
  ReplayTests.test_pristine_normal_and_optimized
```

Earlier combined commands were interrupted by execution timeouts after seven
methods. They are NOT counted as successful whole-suite runs. The separate
completed groups cover all methods, with zero failures, errors or skips.
An attempted interactive execution was unsupported; no result is inferred
from it. A separate pristine normal/optimized test also completed.

## Analytic versus finite claims

The actual anchored phases n^(i tau), their all-real-parameter norm estimate,
and the actual centered harmonic mask are covered by the written analytic
proof, NOT by the rational bump/character controls. Gaussian-unit characters
are not asserted to be n^(i tau). The rational bump is not the harmonic kernel.

No independent mathematical review, proof-assistant build, repository-wide
validator, CI verdict, full inherited campaign replay, or other-platform test
is claimed. No native asymptotic bound, coercive inversion, complete Newton
covariance estimate, or RH proof was obtained. The source-compressed comparison
must not be substituted for RLC35's uncompressed adapter without its leakage.
