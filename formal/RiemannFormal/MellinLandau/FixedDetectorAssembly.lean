import RiemannFormal.Arithmetic.FixedRows
import RiemannFormal.MellinLandau.Contract

namespace RiemannFormal.MellinLandau

open RiemannFormal.Arithmetic

/-!
# Arithmetic-side fixed-detector interface

Reviewer B supplies only finite arithmetic/source/numerator data.  No theorem in
this module concludes RH, invokes Landau's theorem, or assumes a function whose
result is already RH.  The final analytic composition is intentionally deferred
until Reviewer A's repaired consumer API is reconciled.
-/

/-- A fixed detector whose coefficient family is identified with one native
arithmetic source. -/
structure FixedNativeDetectorData where
  source : NativeSource ℝ
  detector : FixedArithmeticDetector ℝ
  sourceIdentity : detector.coefficient = source.coefficient

/-- One fixed numerator together with its exact open-unit-disc noncancellation. -/
structure ZeroSafeNumeratorData where
  numerator : ℂ → ℂ → ℂ
  zeroSafe : ∀ a b : ℂ, ‖a‖ < 1 → numerator a b ≠ 0

/-- Arithmetic-side hypotheses for one fixed scalar consumer. -/
structure FixedNativeScalarInput where
  fixed : FixedNativeDetectorData
  numerator : ZeroSafeNumeratorData

/-- Two fixed numerators with exact common-zero exclusion. -/
structure TwoRowNumeratorData where
  firstNumerator : ℂ → ℂ → ℂ
  secondNumerator : ℂ → ℂ → ℂ
  noCommonZero : ∀ a b : ℂ, ‖a‖ < 1 →
    firstNumerator a b ≠ 0 ∨ secondNumerator a b ≠ 0

/-- Arithmetic-side hypotheses for a fixed pair of native detectors. -/
structure FixedNativeTwoRowInput where
  first : FixedNativeDetectorData
  second : FixedNativeDetectorData
  numerators : TwoRowNumeratorData

/-- Build a fixed detector directly from a supplied native source.  This proves
coefficient identity and data-shape fixedness only; it does not prove that the
source has the sign or Mellin transform required by the analytic consumer. -/
def detectorFromNative (semanticId : String) (source : NativeSource ℝ) :
    FixedArithmeticDetector ℝ where
  semanticId := semanticId
  coefficient := source.coefficient

@[simp]
theorem detectorFromNative_coefficient (semanticId : String)
    (source : NativeSource ℝ) :
    (detectorFromNative semanticId source).coefficient = source.coefficient := rfl

/-- Exact fixed `5:3` numerator certificate. -/
def fiveThreeNumeratorData : ZeroSafeNumeratorData where
  numerator := RiemannFormal.Arithmetic.FixedRows.fiveThreeNumerator
  zeroSafe := by
    intro a b ha
    exact RiemannFormal.Arithmetic.FixedRows.fiveThree_nonzero ha

/-- Exact rows `2,3` common-zero certificate. -/
def rows23NumeratorData : TwoRowNumeratorData where
  firstNumerator := RiemannFormal.Arithmetic.FixedRows.row2Numerator
  secondNumerator := RiemannFormal.Arithmetic.FixedRows.row3ScaledNumerator
  noCommonZero := by
    intro a b ha
    exact RiemannFormal.Arithmetic.FixedRows.rows23_no_common_zero ha

/-- Package any supplied native scalar source with the exact fixed `5:3`
numerator algebra.  The unresolved native sign/negative-mass and analytic
Mellin--Landau hypotheses are not fields of this arithmetic package. -/
def fixedFiveThreeArithmeticInput (source : NativeSource ℝ) :
    FixedNativeScalarInput where
  fixed :=
    { source := source
      detector := detectorFromNative "CONSUMER.MELLIN.FIVE_THREE" source
      sourceIdentity := rfl }
  numerator := fiveThreeNumeratorData

/-- Package supplied native row sources with the exact fixed rows `2,3`
common-zero algebra.  Supplying both native row sources remains an explicit
producer responsibility. -/
def fixedRows23ArithmeticInput (row2 row3 : NativeSource ℝ) :
    FixedNativeTwoRowInput where
  first :=
    { source := row2
      detector := detectorFromNative "CONSUMER.MELLIN.ROW2" row2
      sourceIdentity := rfl }
  second :=
    { source := row3
      detector := detectorFromNative "CONSUMER.MELLIN.ROW3" row3
      sourceIdentity := rfl }
  numerators := rows23NumeratorData

/-- All arithmetic fields of the fixed `5:3` package are operative and reduce
to the exact source identity and numerator noncancellation. -/
theorem fixedFiveThreeArithmeticInput_spec (source : NativeSource ℝ) :
    (fixedFiveThreeArithmeticInput source).fixed.detector.coefficient =
        source.coefficient ∧
      ∀ a b : ℂ, ‖a‖ < 1 →
        (fixedFiveThreeArithmeticInput source).numerator.numerator a b ≠ 0 := by
  constructor
  · rfl
  · intro a b ha
    exact RiemannFormal.Arithmetic.FixedRows.fiveThree_nonzero ha

/-- All finite algebraic fields of the fixed rows `2,3` package are operative. -/
theorem fixedRows23ArithmeticInput_spec (row2 row3 : NativeSource ℝ) :
    (fixedRows23ArithmeticInput row2 row3).first.detector.coefficient =
        row2.coefficient ∧
      (fixedRows23ArithmeticInput row2 row3).second.detector.coefficient =
        row3.coefficient ∧
      ∀ a b : ℂ, ‖a‖ < 1 →
        (fixedRows23ArithmeticInput row2 row3).numerators.firstNumerator a b ≠ 0 ∨
          (fixedRows23ArithmeticInput row2 row3).numerators.secondNumerator a b ≠ 0 := by
  constructor
  · rfl
  constructor
  · rfl
  · intro a b ha
    exact RiemannFormal.Arithmetic.FixedRows.rows23_no_common_zero ha

end RiemannFormal.MellinLandau
