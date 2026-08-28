# Formalization Reviewer A report

Bootstrap base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`  
Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`  
Zeta23: `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e`  
Binding repair review: PR #747 at `ebe287cc85b122cbe3efd57b7c30ce17d150d74c`

## Upstream theorem reused

- Mathlib `RiemannHypothesis`, `riemannZeta`, the two completed-zeta normalizations, their functional equations, analytic and meromorphic order, zero discreteness, standard Mellin calculus and analytic arithmetic.
- Zeta23's exact open-strip zero convention, finite `zeroMult` convention, closed seam, bounded zero windows, centered coordinate, reflected zero and reflected multiplicity.
- Zeta23's literature-form Weil explicit formula and its Riemann-von Mangoldt package, with the latter retaining the explicit `GammaFacts` argument.

Every imported source is recorded by exact project commit, source path and declaration in `formal/registry/SOURCE_LOCKS.json`, mirrored in `RiemannFormal.Upstream.SourceLocks`, and consumed by `scripts/verify_source_locks.py`.

## Theorem proved locally

- Project/Mathlib RH identity and the restored Zeta23 compatibility theorem.
- Completed-zeta normalization and functional-equation adapters with exceptional points explicit.
- Centered-coordinate reconstruction and reflection adapters.
- Analytic-order to meromorphic-order conversion for zeta away from `1`.
- Exact identification of zeta meromorphic order with Zeta23 `zeroMult` at an open-strip zero, and reciprocal inversion.
- Standard Mellin dilation, scalar multiplication, the explicitly two-term linear-combination API, compact power kernels and strip holomorphy.
- The direct reviewed tail transform
  `tailMellin f s = ∫_[1,∞) f(x) x^(-s-1) dx`.
- Jordan decomposition for convergent tail transforms.
- The logarithmic-box multiplier `K_A(s)=(1-A^(-s))/s`, analytic and nonzero for fixed `A>1` and `Re(s)>0`.
- Fixed holomorphic-defect and fixed nonvanishing-multiplier singularity transfer.
- Conditional reflection closure once right-half-plane exclusion is supplied.
- The Mathlib-only comparator solution `Comparator.MellinAPI.fixedMellinConsumerSolution`.

## Theorem proved conditionally

`RiemannFormal.Analysis.fixedDetector_negativeMass_implies_RH` is the honest conclusion-facing theorem. It does not accept a function or structure that already returns RH. Its separate explicit arguments contain:

1. the fixed detector's initial tail convergence and source identity;
2. the fixed reciprocal-zeta continuation factorization;
3. fixed numerator, multiplier and holomorphic defect;
4. exact shifted reciprocal pole order and Zeta23 multiplicity;
5. positive-tail finite-abscissa and analytic-continuation data;
6. the exact tail-Landau proposition;
7. the exact subpower-negative-mass holomorphy proposition;
8. the open-strip localization and functional-equation reflection interfaces.

The theorem is therefore `PROVED_CONDITIONAL`, never `PROVED`.

## Blocked on library infrastructure

Pinned Mathlib and Zeta23 do not expose:

- the exact eventual-sign boundary-singularity theorem for the tail transform on `[1,∞)`;
- the exact integration-by-parts theorem converting subpower logarithmic negative mass on `[1,X]` into holomorphy of the negative-part tail transform on `Re(s)>0`;
- the affine shifted-coordinate meromorphic-order adapter needed to discharge `ShiftedReciprocalPoleOrder` without an explicit argument;
- a complete imported theorem localizing every Mathlib-RH-admissible zero into the Zeta23 open-strip convention in the precise form used by the generic consumer.

These are exact propositions or interfaces, not axioms.

## Blocked on open mathematics

No arithmetic producer estimate is formalized or assumed true. In particular, eventual positivity or subpower logarithmic negative mass for fixed rows 2 and 3, the fixed `5:3` scalar, or another fixed zero-safe native detector remains open.

## Validation status

The deterministic suite is preserved in
`formal/RiemannFormal/Analysis/replay/run_validation.sh`.

This repair environment contains no Lean/Lake executable, so this report does **not** claim `BUILD_PASS`. Static JSON/TSV/source-lock and no-custom-axiom checks are performed before publication; the exact remote head must receive the full Lake and axiom audit independently.

The Riemann Hypothesis remains unproved.
