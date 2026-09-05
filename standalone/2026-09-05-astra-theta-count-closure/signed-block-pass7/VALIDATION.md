# Validation and execution boundary

Final clean executions reconstructed, rather than merely read, both result files:

    python verify.py --check result.json
    python -O verify.py --check result.json
    python verify_low_prefix.py --check low_prefix.json
    python -O verify_low_prefix.py --check low_prefix.json

The exact suite performs 495 rational/Gaussian-rational controls per mode.
Their complete outputs are byte-identical. The interval suite separately proves
six strict endpoint signs in both modes, again with byte-identical outputs.
The normal/optimized duplicates are NOT counted as additional distinct controls.

Six deliberately altered result files were rejected in each mode, for the
expected error: changed RH flag, a float numeric alias, a Boolean/integer alias,
wrong stated bound, wrong count, and a duplicate key. REPLAY.json retains the
completed subprocess exit codes, output hashes and twelve refusal records.

The unchanged prime-cutoff-pass6 checker was rerun against its checks.json in
both modes; all 16 parent test cases passed in each. Those are separate from
our 495 controls. The earlier heat-Hankel, signed-tail-pass6, whole-repository
and other-branch suites were not rerun. No Lean build or remote CI success
is claimed. The six endpoint signs are not a zero census; V100 is imported.

Arithmetic boundary:

- verify.py: Python standard-library exact integers, Fraction and a two-Fraction
  complex implementation. It checks finite beta/variance matrices, Jacobi
  identities, generalized interpolation with widely separated exponents, the
  explicit Schur factor, constants, rational transforms and synthetic controls.
- verify_low_prefix.py: mpmath.iv 1.3.0 at 80 decimal digits with exact rational
  finite weights and a proved 2^(-120) eta tail rectangle. The interval Gamma
  implementation is an explicit software trust dependency, not a Lean proof.
- An initial ordinary-precision evaluation of the six signs was used only as
  reconnaissance before the interval run and does not enter acceptance.

There was NO actual prime-sum computation, broad prime scan, actual high-order
xi Gram-matrix evaluation, independent referee acceptance, or all-rank sign
certificate. The analytic all-order proofs are in PROOF.md, not established
by the finite tests. The exact constants were chosen conservatively and no
claim of optimal constants, external novelty or RH completion is made.

SHA256SUMS covers every file in this directory except itself. Publication
receipts containing the final commit identity belong outside this immutable
packet or in the PR discussion, not inside a self-referential commit field.
