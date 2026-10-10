import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Arithmetic adapters for the low-kappa reflection and capacity inequalities

These statements concern real logarithmic lengths supplied by an analytic proof.
They do not formalize the arithmetic coefficients, reflection identity, fourth
moment, continuation argument, zero-free source input, or a theorem about RH.

The comparison hypotheses are copied from the September-30 plain-moment proof,
with the kappa threshold lowered to 13/18. The imported analytic range also has
kappa <= 1; the first three implications do not need that upper bound.
-/

namespace FourHourWave.LowKappaCapacity

theorem coefficient_lower (kappa : ℝ) (hkappa : 13 / 18 ≤ kappa) :
    (10 / 3 : ℝ) ≤ 6 * kappa - 1 := by
  linarith

theorem coefficient_range (kappa : ℝ)
    (hlower : 13 / 18 ≤ kappa) (hupper : kappa ≤ 1) :
    0 ≤ 6 * kappa - 1 ∧ 6 * kappa - 1 ≤ 5 := by
  constructor <;> linarith

/-- The non-strict high-length comparison allows equality at the width bound. -/
theorem slot_length_le (M A z kappa : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M) :
    z ≤ M / 20 := by
  have hscaled : (10 / 3 : ℝ) * z ≤ (6 * kappa - 1) * z :=
    mul_le_mul_of_nonneg_right (coefficient_lower kappa hkappa) hz
  nlinarith only [hscaled, hA, hcapacity]

/-- Strict high length gives the strict comparison width used in the source. -/
theorem slot_length_lt (M A z kappa : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 < A) (hcapacity : A + (6 * kappa - 1) * z ≤ M) :
    z < M / 20 := by
  have hscaled : (10 / 3 : ℝ) * z ≤ (6 * kappa - 1) * z :=
    mul_le_mul_of_nonneg_right (coefficient_lower kappa hkappa) hz
  nlinarith only [hscaled, hA, hcapacity]

/-- The reflected total-length bound is an explicit hypothesis, not an axiom. -/
theorem comparison_bounds (M A z kappa Acomp xi : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M)
    (hreflection : Acomp ≤ 3 * M / 2 - A + 2 * z + xi) :
    z ≤ M / 20 ∧
    Acomp ≤ 23 * M / 30 + xi ∧
    Acomp + (6 * kappa - 1) * z ≤ 14 * M / 15 + xi := by
  have hsmall := slot_length_le M A z kappa hz hkappa hA hcapacity
  refine ⟨hsmall, ?_, ?_⟩
  · linarith only [hreflection, hA, hsmall]
  · nlinarith only [hreflection, hA, hsmall, hcapacity]

/-- Exactly the requested comparison bounds when there is no support error. -/
theorem comparison_bounds_zero_error (M A z kappa Acomp : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M)
    (hreflection : Acomp ≤ 3 * M / 2 - A + 2 * z) :
    z ≤ M / 20 ∧
    Acomp ≤ 23 * M / 30 ∧
    Acomp + (6 * kappa - 1) * z ≤ 14 * M / 15 := by
  simpa using comparison_bounds M A z kappa Acomp 0 hz hkappa hA hcapacity
    (by simpa using hreflection)

/-- Support error at most M/30 leaves the two actual admissibility margins. -/
theorem comparison_margins (M A z kappa Acomp xi : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M)
    (hreflection : Acomp ≤ 3 * M / 2 - A + 2 * z + xi)
    (herror : xi ≤ M / 30) :
    Acomp + M / 30 ≤ 5 * M / 6 ∧
    Acomp + (6 * kappa - 1) * z + M / 30 ≤ M := by
  obtain ⟨_, hlength, hcap⟩ :=
    comparison_bounds M A z kappa Acomp xi hz hkappa hA hcapacity hreflection
  constructor <;> linarith only [hlength, hcap, herror]

/-- Positive row width turns the certified margins into strict admissibility. -/
theorem comparison_strict_admissibility (M A z kappa Acomp xi : ℝ)
    (hM : 0 < M) (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : 5 * M / 6 ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M)
    (hreflection : Acomp ≤ 3 * M / 2 - A + 2 * z + xi)
    (herror : xi ≤ M / 30) :
    Acomp < 5 * M / 6 ∧ Acomp + (6 * kappa - 1) * z < M := by
  obtain ⟨hlength, hcap⟩ :=
    comparison_margins M A z kappa Acomp xi hz hkappa hA hcapacity
      hreflection herror
  constructor <;> nlinarith only [hlength, hcap, hM]

/-- The same lower kappa threshold preserves the terminal prime-cost loss. -/
theorem terminal_bounds (M A z kappa : ℝ)
    (hz : 0 ≤ z) (hkappa : 13 / 18 ≤ kappa)
    (hA : z ≤ A) (hcapacity : A + (6 * kappa - 1) * z ≤ M) :
    z ≤ 3 * M / 13 ∧ kappa * z ≤ M / 6 := by
  have hscaled : (13 / 3 : ℝ) * z ≤ (6 * kappa) * z :=
    mul_le_mul_of_nonneg_right (by linarith) hz
  constructor <;> nlinarith only [hscaled, hA, hcapacity]

/-- Arithmetic replacement for the deleted-column max-with-zero geometry.

`ell` is an upper bound on the surviving live length `z`; the upper kappa
bound is not needed for these two inequalities. No reflected scale is assumed
positive, so clipping at zero is treated directly in the proof.
-/
theorem clipped_reflection_bounds (M short along z ell kappa reflected xi : ℝ)
    (hM : 0 ≤ M) (hshort : short ≤ M / 4)
    (_hz : 0 ≤ z) (hzell : z ≤ ell) (hell : ell ≤ M / 20)
    (hkappa : 13 / 18 ≤ kappa) (hellcap : (6 * kappa - 1) * ell ≤ M / 6)
    (hhigh : 5 * M / 6 < short + max 0 along + z)
    (hreflected : reflected ≤ max 0 (M - along + xi)) (hxi : 0 ≤ xi) :
    reflected + short + z ≤ 23 * M / 30 + xi ∧
    reflected + short + 6 * kappa * z ≤ 14 * M / 15 + xi := by
  have hzsmall : z ≤ M / 20 := hzell.trans hell
  have hcoef : 0 ≤ 6 * kappa - 1 := by
    have := coefficient_lower kappa hkappa
    linarith
  have hzcap : (6 * kappa - 1) * z ≤ M / 6 :=
    (mul_le_mul_of_nonneg_left hzell hcoef).trans hellcap
  have halong : 0 < along := by
    by_contra hnot
    have hnonpos : along ≤ 0 := le_of_not_gt hnot
    rw [max_eq_left hnonpos] at hhigh
    linarith only [hhigh, hshort, hzsmall, hM]
  rw [max_eq_right halong.le] at hhigh
  have hlength : reflected + short + z ≤ 23 * M / 30 + xi := by
    by_cases hraw : 0 ≤ M - along + xi
    · rw [max_eq_right hraw] at hreflected
      linarith only [hreflected, hhigh, hshort, hzsmall]
    · have hrawle : M - along + xi ≤ 0 := le_of_not_ge hraw
      rw [max_eq_left hrawle] at hreflected
      linarith only [hreflected, hshort, hzsmall, hM, hxi]
  refine ⟨hlength, ?_⟩
  nlinarith only [hlength, hzcap]

/-! Positive real controls make the theorem hypotheses explicitly inhabited. -/

theorem strict_positive_example :
    ∃ M A z kappa Acomp : ℝ,
      0 < M ∧ 0 < A ∧ 0 < z ∧ 0 < kappa ∧ 0 < Acomp ∧
      13 / 18 ≤ kappa ∧ kappa < 3 / 4 ∧
      5 * M / 6 < A ∧ A + (6 * kappa - 1) * z ≤ M ∧
      Acomp ≤ 3 * M / 2 - A + 2 * z ∧
      z < M / 20 ∧ Acomp ≤ 23 * M / 30 ∧
      Acomp + (6 * kappa - 1) * z ≤ 14 * M / 15 := by
  refine ⟨60, 51, 2, 13 / 18, 43, ?_⟩
  norm_num

/-- At the threshold all three non-strict upper constants can be attained. -/
theorem equality_example :
    ∃ M A z kappa Acomp : ℝ,
      0 < M ∧ 0 < z ∧ kappa = 13 / 18 ∧
      A = 5 * M / 6 ∧ A + (6 * kappa - 1) * z = M ∧
      Acomp = 3 * M / 2 - A + 2 * z ∧
      z = M / 20 ∧ Acomp = 23 * M / 30 ∧
      Acomp + (6 * kappa - 1) * z = 14 * M / 15 := by
  refine ⟨60, 50, 3, 13 / 18, 46, ?_⟩
  norm_num

theorem positive_error_example :
    ∃ M A z kappa Acomp xi : ℝ,
      0 < M ∧ 0 < A ∧ 0 < z ∧ 0 < kappa ∧ 0 < Acomp ∧ 0 < xi ∧
      13 / 18 ≤ kappa ∧ kappa < 3 / 4 ∧
      5 * M / 6 < A ∧ A + (6 * kappa - 1) * z ≤ M ∧
      Acomp ≤ 3 * M / 2 - A + 2 * z + xi ∧ xi ≤ M / 30 ∧
      Acomp + M / 30 ≤ 5 * M / 6 ∧
      Acomp + (6 * kappa - 1) * z + M / 30 ≤ M := by
  refine ⟨60, 51, 2, 13 / 18, 44, 1, ?_⟩
  norm_num

/-- The comparison constants cannot be kept uniformly below kappa = 13/18. -/
theorem below_threshold_failure_example :
    ∃ M A z kappa Acomp : ℝ,
      0 < M ∧ 0 < A ∧ 0 < z ∧ 0 < kappa ∧ kappa < 13 / 18 ∧
      5 * M / 6 ≤ A ∧ A + (6 * kappa - 1) * z ≤ M ∧
      Acomp ≤ 3 * M / 2 - A + 2 * z ∧
      M / 20 < z ∧ 23 * M / 30 < Acomp ∧
      14 * M / 15 < Acomp + (6 * kappa - 1) * z := by
  refine ⟨60, 50, 25 / 8, 7 / 10, 185 / 4, ?_⟩
  norm_num

theorem positive_clipped_example :
    ∃ M short along z ell kappa reflected xi : ℝ,
      0 < M ∧ 0 < short ∧ 0 < z ∧ 0 < ell ∧ 0 < reflected ∧
      short ≤ M / 4 ∧ z ≤ ell ∧ ell ≤ M / 20 ∧
      13 / 18 ≤ kappa ∧ kappa < 3 / 4 ∧
      (6 * kappa - 1) * ell ≤ M / 6 ∧
      5 * M / 6 < short + max 0 along + z ∧
      reflected ≤ max 0 (M - along + xi) ∧ 0 ≤ xi := by
  refine ⟨60, 10, 50, 1, 3, 13 / 18, 10, 0, ?_⟩
  norm_num

#print axioms coefficient_lower
#print axioms coefficient_range
#print axioms slot_length_le
#print axioms slot_length_lt
#print axioms comparison_bounds
#print axioms comparison_bounds_zero_error
#print axioms comparison_margins
#print axioms comparison_strict_admissibility
#print axioms terminal_bounds
#print axioms clipped_reflection_bounds
#print axioms strict_positive_example
#print axioms equality_example
#print axioms positive_error_example
#print axioms below_threshold_failure_example
#print axioms positive_clipped_example

end FourHourWave.LowKappaCapacity
