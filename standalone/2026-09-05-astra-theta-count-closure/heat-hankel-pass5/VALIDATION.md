# Executed validation and review contract

Status: finite execution completed; mathematical review PENDING; RH unproved.
The final immutable identity belongs in the external publication receipt.

## What was executed

- `python verify.py --check result.json`: 2,300 exact rational and
  Gaussian-rational controls, with the complete output equal to result.json.
- `python -O verify.py --check result.json`: the same 2,300 controls, with
  byte-identical complete output. Acceptance does not use Python assertions.
- `python rejection_tests.py`: 14 rejections, seven corruptions in each mode.
  They change the RH flag, an integer to its equal floating-point value, the
  counterexample determinant sign, a dimension, one group, the proof bytes,
  or the frozen parent identity. A saved PASS string is not sufficient.
- The unchanged original #790 `verify_exact.py --check exact_result.json`
  replayed its 225 controls in both modes with matching complete outputs.
  This is a separate parent count, not added to the 2,300 new controls.
- All entries of this directory's SHA256SUMS were checked after the final
  files were written. The publication receipt records remote blob readback.

The 2,300 controls include 56 confluent model-space residual checks, 316
safe-source confluent matrix entries, 144 orthonormal partial-fraction
compiler controls, 36 orthonormal metric entries, finite inertia cases with
up to three nonreal pairs, and the exact negative test. Repeated dyadic
parameter samples corroborate the all-parameter polynomial proof; they are
not substituted for it. The complete grouping is in result.json.

No actual-xi matrix was numerically evaluated. The finite atoms, weights and
matrices in the checker are synthetic. No directed integration, new zero
census, finite-height RH verification, parent interval-zero replay, Lean
build, independent reviewer acceptance, or remote CI success is claimed.
The #792 and #793 code suites were not run in this pass.

## Trust boundary

The analytic proofs use the standard xi product, the unconditional explicit
formula, Hardy/Laplace/model-space theory, elementary finite interpolation,
and trace-class operator theory. The exact checker authenticates selected
finite identities and the final text hashes; it does not machine-prove those
infinite theorems. A source hash is an identity, not a proof of its contents.
No local computation discharges the final all-rank arithmetic PSD condition.

## Author self-audit

The kernel orientation is Hankel S(s+t), not Toeplitz S(s-t). The rank-one
pair is f_A paired with f_barA; replacing it by a positive rank-one summand
would assume away the problem. Multiplicities change weights, not the number
of independent zero locations. Every omitted background node enters the
Blaschke product; no uniform separation is used.

The raw metric G is mandatory for norm bounds. The thermal and unheated
hierarchies use different source formulas and rank counts. The complete
explicit formula retains its 4pi R(0)^2 endpoint term. The trace-norm error
proves convergence of INDEFINITE compressions; it is not a construction of
positive approximants. The integer negative index has no uniform spectral
gap, as demonstrated by the small-negative-mass family.

During checker development, the initial synthetic source budget fixture had
H>=1/2 and was rejected. It was replaced by a fixture satisfying the stated
hypothesis. No theorem constant or actual-xi source was changed to make that
invalid fixture pass. The final records reconstruct only admissible fixtures.

## Priority independent review

1. Source constant H and the inference sum 1/Re A<=H/(1-H).
2. Trace-class kernel identity and the zero-thermal corner.
3. Infinite-background Blaschke interpolation and exact inertia, including
   infinitely many nonreal pairs and multiple zeros.
4. Confluent projection formula, dyadic 1/3 bound, and the factor in the
   rank-one trace-norm error.
5. Safe resolvent tail, digamma estimate and the two rank/error choices.
6. Orthonormal source-derivative compiler and raw metric conditioning.
7. Rational explicit-formula admissibility, endpoint and Fourier factors.
8. One-sided negative-trace enclosure and its perturbation error.
9. The exact synthetic negative witness and the absence of any inference
   from positive heat, a controlled diagonal, or small negative mass to RH.
