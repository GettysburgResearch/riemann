import RiemannFormal.Arithmetic.FixedRows
import RiemannFormal.MellinLandau.Contract
import RiemannFormal.Statement.RH

namespace RiemannFormal.MellinLandau

open RiemannFormal
open RiemannFormal.Arithmetic

/-- The arithmetic layer exposes a fixed detector and keeps the unresolved estimate explicit. -/
structure FixedNativeDetectorData where
  source : NativeSource ℝ
  detector : FixedArithmeticDetector ℝ
  sourceIdentity : detector.coefficient = source.coefficient

/-- Reviewer A supplies the exact analytic negative-mass predicate and its consumer theorem. -/
structure AnalyticConsumerAssumptions
    (SubpowerNegativeMass : FixedArithmeticDetector ℝ → Prop) where
  consumes : ∀ d : FixedArithmeticDetector ℝ, SubpowerNegativeMass d → RH

/-- Strongest arithmetic-to-consumer assembly available without duplicating analytic Landau work. -/
theorem fixed_native_subpower_negative_mass_implies_RH
    (SubpowerNegativeMass : FixedArithmeticDetector ℝ → Prop)
    (data : FixedNativeDetectorData)
    (analytic : AnalyticConsumerAssumptions SubpowerNegativeMass)
    (hneg : SubpowerNegativeMass data.detector) : RH :=
  analytic.consumes data.detector hneg

/-- A fixed finite family is chosen before a hypothetical zero; selecting a member later does not move it. -/
structure FixedDetectorPair where
  first : FixedArithmeticDetector ℝ
  second : FixedArithmeticDetector ℝ

end RiemannFormal.MellinLandau
