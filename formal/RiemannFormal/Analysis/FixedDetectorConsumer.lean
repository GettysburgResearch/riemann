import RiemannFormal.Analysis.LandauConsumer
import RiemannFormal.Analysis.Reflection
import RiemannFormal.Analysis.SingularityTransfer
import Mathlib.Tactic

open Complex MeasureTheory Set

namespace RiemannFormal.Analysis

/-- A fixed detector continuation is tied to its actual tail transform in one initial
absolute-convergence half-plane. -/
structure FixedDetectorMellinIdentity
    (detector : FixedDetector) (continuation : ℂ → ℂ) (σinitial : ℝ) : Prop where
  initialConvergence : ∀ s : ℂ, σinitial < s.re →
    TailMellinConvergent (fun x => (detector.value x : ℂ)) s
  agreesInitially : ∀ s : ℂ, σinitial < s.re →
    continuation s = tailMellin (fun x => (detector.value x : ℂ)) s

/-- Exact negative-part data for the same fixed detector. -/
structure FixedNegativeMassData
    (detector : FixedDetector) (σinitial : ℝ) : Prop where
  locallyIntegrable : LocallyIntegrableOn
    (fun x : ℝ => (negativePart detector.value x : ℂ)) (Set.Ici (1 : ℝ))
  initialConvergence : ∀ s : ℂ, σinitial < s.re →
    TailMellinConvergent
      (fun x : ℝ => (negativePart detector.value x : ℂ)) s
  subpowerMass : SubpowerLogNegativeMass detector.value

/-- The fixed continuation of the positive part is obtained by adding the negative-part tail
transform back to the signed continuation. -/
noncomputable def positiveTailContinuation
    (detector : FixedDetector) (continuation : ℂ → ℂ) : ℂ → ℂ :=
  fun s => continuation s +
    tailMellin (fun x : ℝ => (negativePart detector.value x : ℂ)) s

/-- The source identity and negative-part convergence force the correct positive-tail identity
throughout their common initial half-plane. -/
theorem positiveTailContinuation_agrees_initially
    {detector : FixedDetector} {continuation : ℂ → ℂ} {σinitial : ℝ}
    (hMellin : FixedDetectorMellinIdentity detector continuation σinitial)
    (hNegative : FixedNegativeMassData detector σinitial) :
    ∀ s : ℂ, σinitial < s.re →
      positiveTailContinuation detector continuation s =
        tailMellin (fun x : ℝ => (positivePart detector.value x : ℂ)) s := by
  intro s hs
  have hjordan :=
    tailMellin_positivePart_eq_add_negativePart
      (hMellin.initialConvergence s hs) (hNegative.initialConvergence s hs)
  simp [positiveTailContinuation, hMellin.agreesInitially s hs, hjordan.2]

/-- All zero-safe factors are fixed before a hypothetical zero is introduced. -/
structure FixedZeroSafeFactors
    (numerator multiplier defect : ℂ → ℂ) : Prop where
  numeratorAnalytic :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      (1 / 2 : ℝ) < ρ.re →
      AnalyticAt ℂ numerator (ρ - (1 / 2 : ℂ))
  numeratorNonzero :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      (1 / 2 : ℝ) < ρ.re →
      numerator (ρ - (1 / 2 : ℂ)) ≠ 0
  multiplierAnalytic :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      (1 / 2 : ℝ) < ρ.re →
      AnalyticAt ℂ multiplier (ρ - (1 / 2 : ℂ))
  multiplierNonzero :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      (1 / 2 : ℝ) < ρ.re →
      multiplier (ρ - (1 / 2 : ℂ)) ≠ 0
  defectAnalytic :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      (1 / 2 : ℝ) < ρ.re →
      AnalyticAt ℂ defect (ρ - (1 / 2 : ℂ))

/-- Reciprocal zeta in the shifted Mellin coordinate `s = ρ - 1/2`. -/
noncomputable def shiftedReciprocalZeta (s : ℂ) : ℂ :=
  (riemannZeta (s + (1 / 2 : ℂ)))⁻¹

/-- Exact fixed-detector reciprocal-zeta continuation package. It includes both the initial
source/tail identity and the fixed global continuation factorization; no sign estimate is asserted. -/
structure FixedDetectorReciprocalZetaIdentity
    (detector : FixedDetector) (continuation numerator multiplier defect : ℂ → ℂ)
    (σinitial : ℝ)
    extends FixedDetectorMellinIdentity detector continuation σinitial : Prop where
  continuationFormula :
    continuation =
      fun s => multiplier s * (numerator s * shiftedReciprocalZeta s) + defect s

/-- Exact shifted reciprocal-pole order required by the consumer. The unshifted
analytic-order/meromorphic-order and Zeta23 multiplicity bridge is proved upstream; this affine
composition statement remains an explicit argument until the corresponding library adapter is
compiled. -/
structure ShiftedReciprocalPoleOrder : Prop where
  order_eq :
    ∀ ρ : ℂ, RiemannFormal.Upstream.ProjectNontrivialZero ρ →
      meromorphicOrderAt shiftedReciprocalZeta (ρ - (1 / 2 : ℂ)) =
        -((RiemannFormal.Upstream.ProjectZeroMultiplicity ρ : ℤ) : WithTop ℤ)

/-- The exact shifted order and the positive Zeta23 multiplicity make the reciprocal singularity
nonremovable. -/
theorem shiftedReciprocalZeta_nonremovable_of_order
    (hPole : ShiftedReciprocalPoleOrder)
    {ρ : ℂ} (hρ : RiemannFormal.Upstream.ProjectNontrivialZero ρ) :
    NonremovableAt shiftedReciprocalZeta (ρ - (1 / 2 : ℂ)) := by
  apply nonremovable_of_meromorphicOrderAt_neg
  rw [hPole.order_eq ρ hρ]
  have hmNat : 0 < RiemannFormal.Upstream.ProjectZeroMultiplicity ρ :=
    lt_of_lt_of_le Nat.zero_lt_one (Zeta23.zetaSeam.one_le_mult ρ hρ)
  have hmInt :
      (0 : ℤ) < (RiemannFormal.Upstream.ProjectZeroMultiplicity ρ : ℤ) := by
    exact_mod_cast hmNat
  exact_mod_cast (neg_neg_of_pos hmInt)

/-- Every Mathlib-RH-admissible zero is represented by the project's open-strip convention. This
classical zero-localization adapter is kept explicit in the conclusion-facing theorem. -/
def AdmissibleZerosInProjectStrip : Prop :=
  ∀ ρ : ℂ, RHAdmissibleZero ρ →
    RiemannFormal.Upstream.ProjectNontrivialZero ρ

/-- Honest conditional fixed-detector consumer. No argument already returns RH. The theorem uses:
the fixed source/tail identity; initial convergence; the fixed reciprocal-zeta continuation;
the fixed numerator, multiplier and holomorphic defect; exact shifted pole multiplicity; the exact
tail-Landau and subpower-negative-mass propositions; analytic continuation of the positive tail;
right-half-plane exclusion; and functional-equation reflection. -/
theorem fixedDetector_negativeMass_implies_RH
    {detector : FixedDetector}
    {continuation numerator multiplier defect : ℂ → ℂ}
    {σinitial σc : ℝ}
    (hMellin :
      FixedDetectorReciprocalZetaIdentity
        detector continuation numerator multiplier defect σinitial)
    (hNegative : FixedNegativeMassData detector σinitial)
    (hZeroSafe : FixedZeroSafeFactors numerator multiplier defect)
    (hPoleOrder : ShiftedReciprocalPoleOrder)
    (hPositiveCore :
      NonnegativeTailMellinCore
        (positivePart detector.value)
        (positiveTailContinuation detector continuation) σc)
    (hContinuationExtension :
      (∀ s : ℂ, σinitial < s.re →
        positiveTailContinuation detector continuation s =
          tailMellin
            (fun x : ℝ => (positivePart detector.value x : ℂ)) s) →
      ∀ s : ℂ, σc < s.re →
        positiveTailContinuation detector continuation s =
          tailMellin
            (fun x : ℝ => (positivePart detector.value x : ℂ)) s)
    (hLandau : MellinLandauBoundarySingularity)
    (hNegMass : SubpowerNegativeMassHolomorphy)
    (hOpenStrip : AdmissibleZerosInProjectStrip)
    (hReflect : ReflectsRHAdmissibleZeros) :
    RiemannHypothesis := by
  have hInitialPositive :=
    positiveTailContinuation_agrees_initially
      hMellin.toFixedDetectorMellinIdentity hNegative
  have hPositiveAgreement := hContinuationExtension hInitialPositive
  let hPositive :
      NonnegativeTailMellinData
        (positivePart detector.value)
        (positiveTailContinuation detector continuation) σc :=
    { toNonnegativeTailMellinCore := hPositiveCore
      agreesRight := hPositiveAgreement }
  apply functionalEquationReflection_closes_RH hReflect
  intro ρ hρ
  by_contra hnot
  have hright : (1 / 2 : ℝ) < ρ.re := lt_of_not_ge hnot
  have hProject : RiemannFormal.Upstream.ProjectNontrivialZero ρ :=
    hOpenStrip ρ hρ
  have hs0 : 0 < (ρ - (1 / 2 : ℂ)).re := by
    simp
    linarith
  have hnegativeAnalytic :
      AnalyticAt ℂ
        (tailMellin
          (fun x : ℝ => (negativePart detector.value x : ℂ)))
        (ρ - (1 / 2 : ℂ)) :=
    subpower_negative_mass_holomorphic hNegMass
      hNegative.locallyIntegrable hNegative.initialConvergence
      hNegative.subpowerMass hs0
  have hreciprocal :
      NonremovableAt shiftedReciprocalZeta (ρ - (1 / 2 : ℂ)) :=
    shiftedReciprocalZeta_nonremovable_of_order hPoleOrder hProject
  have hnumerator :
      NonremovableAt
        (fun s => numerator s * shiftedReciprocalZeta s)
        (ρ - (1 / 2 : ℂ)) :=
    nonvanishing_multiplier_preserves_nonremovable
      (hZeroSafe.numeratorAnalytic ρ hProject hright)
      (hZeroSafe.numeratorNonzero ρ hProject hright) hreciprocal
  have hcontinuation :
      NonremovableAt continuation (ρ - (1 / 2 : ℂ)) :=
    fixed_mellin_singularity_transfer
      (hZeroSafe.defectAnalytic ρ hProject hright)
      (hZeroSafe.multiplierAnalytic ρ hProject hright)
      (hZeroSafe.multiplierNonzero ρ hProject hright)
      hMellin.continuationFormula hnumerator
  have hpositiveNonremovable :
      NonremovableAt
        (positiveTailContinuation detector continuation)
        (ρ - (1 / 2 : ℂ)) := by
    unfold positiveTailContinuation
    exact fixed_holomorphic_defect_transfer
      hnegativeAnalytic hcontinuation
  have hpositiveAnalytic :
      AnalyticAt ℂ
        (positiveTailContinuation detector continuation)
        (ρ - (1 / 2 : ℂ)) :=
    nonnegative_tail_continuation_analytic hLandau hPositive hs0
  exact hpositiveNonremovable hpositiveAnalytic

end RiemannFormal.Analysis
