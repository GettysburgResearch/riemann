# formal-v0.1 results

This file summarizes the strongest resident formal results. The generated
registry and exact Lean declarations control over prose.

## Unconditional trusted results

### Analytic infrastructure

- Mathlib's `RiemannHypothesis` is the unique project RH proposition.
- Completed-zeta, centered-coordinate, zero-multiplicity and functional-
  equation conventions are bridged to the pinned Mathlib/Zeta23 definitions.
- Fixed Mellin dilation and finite linear-combination identities are proved.
- The logarithmic-box multiplier is analytic and nonzero in the required open
  right half-plane.
- Fixed holomorphic-defect and nonvanishing-multiplier singularity transfer is
  proved.

### Arithmetic and finite detector algebra

- Rows 2 and 3 have no common zero on the reviewed open-unit-disc domain.
- The fixed `5:3` numerator factors exactly as `-3(a-1)(a-2)` and is nonzero
  on that domain.
- The exact SHARP `(16,4,4)` RN/response/capacity fixture and source-role
  distinctions are formalized at finite scope.
- Native `r` cannot be promoted to contracted `2r²` on `0<r<1/2`.
- The half-divisor central-binomial coefficients satisfy the formalized
  arithmetic-function convolution identity.
- Generic finite first-owner, tap-factorization, minimality, shift and
  summation-by-parts helpers are proved under their honest names.

### Xi/operator algebra

- Exact two-point Pick identities and the three-node determinant factorization
  are proved.
- Finite reciprocal-concavity is closed under positive sums with an exact
  square certificate.
- Repeated-node three-by-three packets reduce to the order-two PSD case.
- The reviewed reflected-orbit cross-curvature and finite reserve-allocation
  algebra are formalized.

### Formalized firewalls

The trusted library proves exact finite forms of these no-go statements:

- a positive Schur-complement correction cannot rescue an already negative
  visible direction;
- coefficient energy alone does not imply coherent operator contraction;
- small negative inertia does not control positive current;
- the hyperbolic pole block is not a sum of two positive squares;
- positive excess does not orient an arbitrary square root;
- a scalar diagonal does not determine a polarized Gram;
- the finite heat displacement fixture changes parity.

The last item is only a finite fixture and is not the full analytic
uniform-center heat theorem.

## Conditional trusted results

### Fixed-detector Mellin–Landau spine

`RiemannFormal.Analysis.fixedDetector_negativeMass_implies_RH` proves RH from
one fixed source package together with all of the following explicit inputs:

- the exact fixed detector Mellin identity;
- fixed zero-safe numerator, multiplier and holomorphic defect data;
- the exact tail-Mellin Landau boundary-singularity proposition;
- the exact subpower-negative-mass holomorphy proposition;
- reciprocal-zeta pole-order and zero-localization inputs;
- a fixed arithmetic negative-mass producer estimate;
- functional-equation reflection.

No input already returns RH, and no missing premise is installed as an axiom.
The theorem is an honest implication, not an unconditional proof.

### Actual-Xi positivity through order three

`RiemannFormal.Operator.actualXiPickOrderThreeConditional` proves the reviewed
PSD conclusion after receiving explicit source-locked inputs for:

- the published verified-height theorem;
- the concrete centered actual-Xi expansion;
- grouped local `C²` convergence through two derivatives;
- multiplicity and reflected-orbit conventions;
- the residual `(m₀-1)R₀` contribution;
- reciprocal-square tail and numerical reserve budgets;
- one-use reserve allocation and paid-prefix approximation;
- the order-two and companion-curvature bridges.

Repeated-node branches are included. The conclusion is PSD through order three
only. Positive definiteness, order four and RH are not conclusions.

## Exact comparator topics

The seven release statements are separately locked and proved in:

```text
RH
MellinAPI
ArithmeticRows23
FixedDetectorFiveThree
OperatorPositiveSchurRescue
XiPickThreeNode
XiPickOrderThreeConditional
```

The exact Challenge/Solution type hashes are recorded in
`registry/FORMAL_V0_1_MANIFEST.json`.
