# Repair report for PR #747

Binding cross-review: PR #747, head `ebe287cc85b122cbe3efd57b7c30ce17d150d74c`.

## P0-1 — stale trusted audit reference

**Resolved.**

`RiemannFormal.Upstream.zeta23_bridge_preserves_RH` is restored as the definitionally exact compatibility theorem
`RiemannFormal.RH ↔ RiemannHypothesis`.

The top-level trusted audit still names it, and now also audits the multiplicity adapter, exact tail-Landau wrapper, exact negative-mass wrapper and final conditional consumer.

## P0-2 — misnormalized Landau proposition

**Resolved at statement level; proof remains `BLOCKED_LIBRARY`.**

The project now defines directly

```text
tailMellin f s = ∫_[1,∞) f(x) x^(-s-1) dx.
```

`MellinLandauBoundarySingularity` quantifies the same transformed detector throughout and includes:

- local integrability on `[1,∞)`;
- eventual nonnegativity;
- nonzero tail density;
- a finite real abscissa;
- convergence throughout the initial right half-plane;
- the exact tail-transform continuation identity;
- nonremovability at the boundary abscissa.

It is a `Prop`, not an axiom.

## P0-3 — misnormalized subpower negative-mass proposition

**Resolved at statement level; proof remains `BLOCKED_LIBRARY`.**

`SubpowerNegativeMassHolomorphy` now includes local integrability and initial tail convergence of the negative part, uses the exact logarithmic mass

```text
∫_[1,X] f_-(x) dx/x,
```

and concludes holomorphy of that same negative-part tail transform throughout `Re(s)>0`.

## P0-4 — missing honest conclusion-facing theorem

**Resolved conditionally.**

`fixedDetector_negativeMass_implies_RH` composes the actual fixed source identity, continuation factorization, zero-safe numerator/multiplier, fixed defect, shifted reciprocal pole order, positive-tail continuation, exact Landau and negative-mass propositions, right-zero exclusion and reflection. No argument already returns RH. Every unresolved analytic or arithmetic interface remains explicit.

Registry status: `PROVED_CONDITIONAL`.

## P1-1 — analytic/meromorphic order and Zeta23 multiplicity

**Resolved for the unshifted point.**

- `projectRiemannZeta_meromorphicOrderAt_eq_analyticOrderAt`
- `projectRiemannZeta_meromorphicOrderAt_eq_zeroMultiplicity`
- `reciprocalZeta_order_of_projectZero`

The affine shifted-coordinate order package remains explicit as `ShiftedReciprocalPoleOrder` and is conservatively `BLOCKED_LIBRARY`.

## P1-2 — finite Mellin linearity overstatement

**Resolved by scope clarification.**

The existing theorem remains named `hasMellin_linearCombination_two`; its documentation now explicitly promises only two terms. No arbitrary finite-family theorem is advertised.

## P1-3 — logarithmic box multiplier

**Resolved.**

`logBoxMultiplier A s = (1-A^(-s))/s` is defined. Analyticity and nonvanishing are proved for fixed `A>1` and `Re(s)>0`.

The arithmetic smoothing identity and sign estimate are not claimed.

## P1-4 — reflection and exceptional points

**Hardened.**

The accepted Zeta23 reflection bridge is retained. The final consumer separately requires the exact Mathlib-admissible/open-strip localization and reflection interfaces, so exceptional points and convention conversion are not hidden.

## QA and provenance

- `A.tsv`, `A_UPSTREAM_REUSE.tsv`, `content-A.tex` and `REVIEW_REPORT.md` are updated.
- `SOURCE_LOCKS.json` is schema version 2 and records exact source PR, SHA, path, claim ID, external commit and imported declaration.
- `verify_source_locks.py` checks those records against the canonical claim registry, dependency pins and `SourceLocks.lean`.
- `RiemannFormal/AxiomAudit.lean`, `Analysis/AxiomAudit.lean`, and both comparator print modules cover the new headline theorem.
- `Analysis/replay/run_validation.sh` preserves the complete deterministic command suite.
- `Analysis/replay/STATIC_CHECK.json` records the static checks and explicitly states that no Lake build was executed.

## Build status

No Lean or Lake executable is available in this repair environment. No `BUILD_PASS` is claimed. The full suite is requested on the exact remote head.

## Scientific boundary

```text
RH: UNPROVED
arithmetic fixed-detector negative-mass estimate: OPEN
custom axiom: NONE
sorry/admit in trusted A modules: NONE INTENDED
```
