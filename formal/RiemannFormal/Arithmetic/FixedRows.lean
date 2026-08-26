import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.FixedRows

/-- The row-two reciprocal-zeta numerator, in variables `a = 2⁻ᶻ`, `b = 3⁻ᶻ`. -/
def row2Numerator (a b : ℂ) : ℂ := 2 * a - 1 - b

/-- Three times the row-three reciprocal-zeta numerator. -/
def row3ScaledNumerator (a b : ℂ) : ℂ := 5 * b - a - 1 - 3 * a ^ 2

/-- The numerator for the fixed positive `5 : 3` row combination. -/
def fiveThreeNumerator (a b : ℂ) : ℂ :=
  5 * row2Numerator a b + row3ScaledNumerator a b

/-- Exact elimination of the `3⁻ᶻ` variable under the row-two equation. -/
theorem row3_factorization_of_row2_zero {a b : ℂ}
    (h2 : row2Numerator a b = 0) :
    row3ScaledNumerator a b = -3 * ((a - 1) * (a - 2)) := by
  have hb : b = 2 * a - 1 := by
    unfold row2Numerator at h2
    linear_combination -h2
  rw [hb]
  simp [row3ScaledNumerator]
  ring

/-- Exact factorization of the fixed `5 : 3` numerator. -/
theorem fiveThree_factorization (a b : ℂ) :
    fiveThreeNumerator a b = -3 * ((a - 1) * (a - 2)) := by
  simp [fiveThreeNumerator, row2Numerator, row3ScaledNumerator]
  ring

private theorem norm_lt_one_ne_one {a : ℂ} (ha : ‖a‖ < 1) : a ≠ 1 := by
  intro h
  subst a
  norm_num at ha

private theorem norm_lt_one_ne_two {a : ℂ} (ha : ‖a‖ < 1) : a ≠ 2 := by
  intro h
  subst a
  norm_num at ha

/-- Rows two and three have no common zero whenever the dyadic parameter lies in the open unit disk. -/
theorem rows23_no_common_zero {a b : ℂ} (ha : ‖a‖ < 1) :
    row2Numerator a b ≠ 0 ∨ row3ScaledNumerator a b ≠ 0 := by
  by_cases h2 : row2Numerator a b = 0
  · right
    intro h3
    have hfac : (-3 : ℂ) * ((a - 1) * (a - 2)) = 0 := by
      calc
        (-3 : ℂ) * ((a - 1) * (a - 2)) = row3ScaledNumerator a b :=
          (row3_factorization_of_row2_zero h2).symm
        _ = 0 := h3
    rcases mul_eq_zero.mp hfac with hneg | hprod
    · norm_num at hneg
    · rcases mul_eq_zero.mp hprod with h1 | h2'
      · exact norm_lt_one_ne_one ha (sub_eq_zero.mp h1)
      · exact norm_lt_one_ne_two ha (sub_eq_zero.mp h2')
  · exact Or.inl h2

/-- The fixed `5 : 3` numerator is zero-free in the same open-unit-disk domain. -/
theorem fiveThree_nonzero {a b : ℂ} (ha : ‖a‖ < 1) :
    fiveThreeNumerator a b ≠ 0 := by
  rw [fiveThree_factorization]
  intro h
  rcases mul_eq_zero.mp h with hneg | hprod
  · norm_num at hneg
  · rcases mul_eq_zero.mp hprod with h1 | h2
    · exact norm_lt_one_ne_one ha (sub_eq_zero.mp h1)
    · exact norm_lt_one_ne_two ha (sub_eq_zero.mp h2)

/-- A packaged dyadic parameter carrying exactly the domain fact used by the algebra. -/
structure DyadicParameter where
  value : ℂ
  norm_lt_one : ‖value‖ < 1

/-- Exact two-row noncancellation, packaged for comparator and consumer APIs. -/
theorem rows23_nonCancellation (p : DyadicParameter) (b : ℂ) :
    row2Numerator p.value b ≠ 0 ∨ row3ScaledNumerator p.value b ≠ 0 :=
  rows23_no_common_zero p.norm_lt_one

/-- Exact fixed `5 : 3` noncancellation, packaged for comparator and consumer APIs. -/
theorem fiveThree_nonCancellation (p : DyadicParameter) (b : ℂ) :
    fiveThreeNumerator p.value b ≠ 0 :=
  fiveThree_nonzero p.norm_lt_one

end RiemannFormal.Arithmetic.FixedRows
