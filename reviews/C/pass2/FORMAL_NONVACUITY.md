# Reviewer C — exact-source nonvacuity and statement-fidelity audit

Status: **SOURCE-LEVEL PROOF OF EMPTY HEADLINE INPUT; LEAN REGRESSION NOT COMPILED.**

Baseline: `GettysburgResearch/riemann@8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Review publication target: PR #798, branch `review/C/2026-09-05-post-release-audit`.
This second-pass packet is prepared against review head `7466ad8081101508be7c7acf0065cb2e0944a639`; it is not a modification of the trusted formal source. Publication status is recorded separately in `PUBLICATION.json`.

## 1. Exact sources and extent of inspection

| Source | Exact Git blob | Inspection |
|---|---|---|
| `formal/comparator/ChallengeDeps/RiemannComparatorChallengeDeps/XiPickOrderThreeConditional.lean` | `7d3dd6c98fd453d1810d80b0e1a39e2e4fbc7ab5` | Entire file, contiguous windows 1–210, 211–420, 421–end |
| `formal/RiemannFormal/Operator/XiOrderThree.lean` | `8a57d165e4d585232d8976858871b99a0d39101e` | Entire declaration and proof file |
| `formal/RiemannFormal/Operator/XiSourceSpecific.lean` | `da684227de5443511b60d1fafa0b1ccafa1883ee` | Entire file, contiguous windows 1–210, 211–430, 431–end |
| `formal/RiemannFormal/Analysis/Foundations.lean` | `52b7a228c128d20dc5b57240b208fee104e624ed` | Entire file |
| `formal/RiemannFormal/Analysis/SingularityTransfer.lean` | `e598973cbd533750399d3bd7b3c5790b906d85f8` | Entire file |
| `Mathlib/NumberTheory/LSeries/RiemannZeta.lean` at Mathlib `51e6992efd06126df61a496bebf8f49482a4e129` | `3c92195fce20df7fda41cfd823b3266f83cf3070` | Lines 1–180 only; includes `completedRiemannZeta_eq`, the entire-function theorem and the residue theorem |

The first five rows refer to the Riemann baseline above. File identities, exact source URLs, inspected scopes and omissions are in `INSPECTED_SOURCES.tsv`. The supporting source reads are not a fresh Lean/Lake, Comparator or independent-kernel run. Mathematical assertions below are reconstructed directly from the displayed definitions; the accompanying `.lean` regression is an uncompiled candidate.

## 2. C2-F01 — an unconditional empty-input defect

**Verdict: FAIL_NONVACUITY_OF_HEADLINE_INPUT. Severity: P0 for promoting the actual-Xi headline as a usable source-faithful formalization.**

The shared ChallengeDeps file defines:

```lean
noncomputable def riemannXi (s : ℂ) : ℂ :=
  (1 / 2 : ℂ) * s * (s - 1) * completedRiemannZeta s

noncomputable def centeredXi (z : ℂ) : ℂ :=
  riemannXi ((1 / 2 : ℂ) + z)

noncomputable def actualXiNodeP (x : ℝ) : ℝ :=
  ((deriv centeredXi (x : ℂ)) /
    ((x : ℂ) * centeredXi (x : ℂ))).re
```

The same file defines an input structure with both a grouped expansion and:

```lean
  diagonalPositive :
    GroupedActualXiC2Expansion → ∀ x : ℝ, 0 < x → 0 < actualXiNodeP x
```

### Complete algebraic proof of the defect

All the displayed functions return values in Lean's total field `ℂ`. Write `K = completedRiemannZeta 1`; its particular value is irrelevant. Direct substitution gives

\[
\operatorname{riemannXi}(1)=\tfrac12\cdot1\cdot(1-1)\cdot K=0,
\qquad
\operatorname{centeredXi}(\tfrac12)=0.
\]

Write `D = deriv centeredXi (1/2)`. Its value, differentiability and computation are also irrelevant. Lean's field division satisfies `D / 0 = 0`, so

\[
\operatorname{actualXiNodeP}(\tfrac12)
=\Re\frac{D}{(\tfrac12)\,0}=0.
\]

Now suppose `inputs : ActualXiOrderThreeInputs` exists. The expression

```lean
inputs.diagonalPositive inputs.grouped (1 / 2) (by norm_num)
```

would give `0 < actualXiNodeP (1/2)`, hence `0 < 0`, a contradiction. Therefore

\[
\boxed{\neg\operatorname{Nonempty}(\texttt{ActualXiOrderThreeInputs}).}
\]

No RH assumption, zero computation, asymptotic theorem, claimed finite-height theorem, derivative value, floating-point approximation or disputed external hypothesis is used. The issue occurs at the positive node `x = 1/2`, not at an excluded nonpositive node.

### Consequence for the comparator

The frozen `ChallengeStatement` is universally quantified over this input structure. An implication from an empty input type can have a correct Lean proof and match a comparator definition exactly while yielding no usable statement about Xi. Kernel acceptance and exact-type equality do not establish nonvacuity of hypotheses.

Five canonical catalog entries use this input package:

| Canonical ID | Declaration |
|---|---|
| `OPERATOR.XI.PICK_ORDER2` | `actualXiPickOrderTwo_of_inputs` |
| `OPERATOR.XI.PICK_ORDER3.TP_CURVATURE` | `actualXiCompanionCurvature_of_inputs` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.ACTUAL` | `actualXiReciprocalConcavity_of_inputs` |
| `OPERATOR.XI.PICK_ORDER3` | `actualXiPickOrderThreeConditional` |
| `OPERATOR.XI.LOEWNER_LOW_ORDER` | `actualXiLowOrderLoewner_of_inputs` |

The declaration namespace is `RiemannFormal.Operator`. The corresponding local, ordered-distinct and reciprocal-curvature wrappers must be traced as dependent consumers. `FORMAL_CATALOG_AUDIT.tsv` preserves the source's `PROVED_CONDITIONAL` labels in a separate field while adding C's nonvacuity verdict. This is not an alteration of the historical registry, a finding of Lean inconsistency, or a claim that the ordinary mathematical Xi theorem is false.

### What survives this finding

The finite Pick determinant identities, duplicate-row PSD reductions, positive-jet sum identity, scalar Schur counterexamples, and local reflected-orbit absorption calculation do not acquire a mathematical refutation merely because a separate headline input is empty. Each retains its own statement and assumptions. The global reserve construction still has explicit tail and numerical-budget inputs; its relevance to a usable actual-Xi package needs a repaired source interface.

## 3. A source-faithful normalization repair, not yet applied

The pinned Mathlib file explicitly totalizes the meromorphic completed zeta at its poles. Its proved identity is

\[
\Lambda(s)=\Lambda_0(s)-\frac1s-\frac1{1-s},
\]

where `completedRiemannZeta₀`, denoted `Λ₀`, is entire. Use the proved `completedRiemannZeta_eq` statement; introductory prose is not the authority for signs.

An entire definition matching the intended Xi normalization is

\[
\boxed{\xi_{\mathrm{entire}}(s)
=\frac12+\frac12s(s-1)\Lambda_0(s).}
\]

For `s ≠ 0,1`, multiplication of the proved identity gives

\[
s(s-1)\Lambda(s)
=s(s-1)\Lambda_0(s)-(s-1)+s
=s(s-1)\Lambda_0(s)+1.
\]

Thus the displayed entire definition agrees with the usual product off the poles, and has value `1/2` at both `s=0` and `s=1`, rather than the raw totalized product's zero. Its entire character follows from the entire `Λ₀` and polynomial operations.

This supplies a precise repair target, not a completed patch or proof of the remaining positivity/curvature inputs. A repaired formalization must prove its normalization, endpoint values and derivative adapters; revise both ChallengeDeps and consumers; regenerate statement/type/source locks; and rerun exact-SHA compilation, comparator, axiom and semantic audits. Merely excluding `x=1/2` would weaken the advertised all-positive-node theorem and leave the next defect unresolved.

Primary source: [pinned Mathlib RiemannZeta](https://github.com/leanprover-community/mathlib4/blob/51e6992efd06126df61a496bebf8f49482a4e129/Mathlib/NumberTheory/LSeries/RiemannZeta.lean).

## 4. C2-F02 — finite/empty off-line strata cannot inhabit the grouped interface

**Verdict: source-domain coverage defect, independent of C2-F01.**

`GroupedActualXiC2Expansion` requires

```lean
  offLineEnumeration : ℕ → ReflectedOffLineOrbit
  offLineRepresentativeUnique : Function.Injective offLineEnumeration
```

A `ReflectedOffLineOrbit` includes an actual zero at `1/2 + a + i b`, with `0 < a < 1/2`, ordinate above the fixed verified height, and analytic multiplicity and reflected zero conditions. Evaluating the enumeration at zero already produces an off-line orbit. Requiring injectivity further rules out a finite orbit type. In particular, this cannot be the universal source package for an empty or finite off-line spectrum.

This observation neither assumes nor disproves RH. It identifies a defect in the formal representation of the cases the intended theorem must cover. Fixing the entire Xi definition is not enough.

The `offLineComplete` field equates occurrence in the main `orbits` sequence with occurrence in the secondary sequence; it should not be described, without an additional argument, as an independently certified complete zero census. The convergence identities are separate strong hypotheses, not a substitute for auditing this source-coverage contract.

A suitable redesign can use a countable actual index type with finite exhaustions, or an `Option`-valued sequence with zero contribution for `none`. Injectivity should concern active representatives, not padding. Require explicit empty and finite examples, multiplicity-aware coverage of all intended source orbits, exclusion of the selected reserve from the other-critical list, and a proof that regrouping preserves the source exactly once. No such repair has been applied here.

## 5. C2-F03 — pointwise nonanalyticity is not punctured nonremovability

`Analysis/Foundations.lean` defines

```lean
def NonremovableAt (F : ℂ → ℂ) (s₀ : ℂ) : Prop := ¬ AnalyticAt ℂ F s₀
```

This predicate concerns the assigned value at the point. It is weaker than saying that the analytic function on a punctured neighborhood has no analytic extension across the puncture. For example, let `F(0)=1` and `F(z)=0` for `z≠0`. The assigned function is not continuous, hence not analytic, at zero, but its punctured restriction extends as the identically zero analytic function.

The frozen holomorphic-defect and nonvanishing-multiplier lemmas are valid for the weaker predicate: subtracting an analytic function or dividing by a nonzero analytic multiplier would otherwise make the original assigned function analytic. This is a naming/statement-strength distinction, not a counterexample to those formal implications. The reciprocal-zeta application additionally carries negative meromorphic order; that stronger source condition prevents the isolated-value example from being a counterexample to the stated conditional pole application.

Rename the predicate to `NotAnalyticAt`, or define punctured nonextendability and prove the needed bridge at the exact source. Preserve this distinction in canonical claim maps and any future Landau library statement. C does not infer a false conditional RH proof from the name alone.

## 6. Reproduction and reconciliation contract

`lean/XiInputNonvacuity.lean` contains candidate source-level regression lemmas. It has **not** been compiled. `scripts/run_xi_regression.sh` checks the exact shared-source blob before attempting a build and Lean run in a disposable checkout; it has likewise **not** been run in this pass.

C's independent disposition does not await A or B. The integrator should compare exact source versions and ask: whether A/B inspected this same shared definition; whether a later repair exists at another SHA; which canonical and comparator consumers import the defective normalization; and whether the proposed repaired input covers empty, finite and infinite off-line spectra. Their outstanding scientific dispositions remain **pending integrator reconciliation**. A later corrected version is a new review object; it does not erase the present exact-SHA finding.
