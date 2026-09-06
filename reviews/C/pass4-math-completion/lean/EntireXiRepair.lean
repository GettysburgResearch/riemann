/-
Reviewer C4 candidate, NOT COMPILED in this pass.
Baseline Mathlib: 51e6992efd06126df61a496bebf8f49482a4e129.
Keep outside trusted imports. This file supplies no actual-zero, positivity,
reserve-tail, RH, or completeness assumption. Paper proof: C4-X1.
-/
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Tactic

noncomputable section
namespace ReviewerC4

/-- Entire normalization; no arbitrary value is assigned to a node quotient. -/
def entireXi (s : ℂ) : ℂ :=
  (1 / 2 : ℂ) + (1 / 2 : ℂ) * s * (s - 1) * completedRiemannZeta₀ s

def rawXi (s : ℂ) : ℂ :=
  (1 / 2 : ℂ) * s * (s - 1) * completedRiemannZeta s

@[simp] theorem entireXi_zero : entireXi 0 = 1 / 2 := by simp [entireXi]
@[simp] theorem entireXi_one : entireXi 1 = 1 / 2 := by simp [entireXi]
@[simp] theorem rawXi_zero : rawXi 0 = 0 := by simp [rawXi]
@[simp] theorem rawXi_one : rawXi 1 = 0 := by simp [rawXi]

theorem entireXi_eq_raw {s : ℂ} (h0 : s ≠ 0) (h1 : s ≠ 1) :
    entireXi s = rawXi s := by
  have hsub : 1 - s ≠ 0 := sub_ne_zero.mpr h1.symm
  unfold entireXi rawXi
  rw [completedRiemannZeta_eq]
  field_simp [h0, h1, hsub]
  <;> ring

theorem entireXi_differentiable : Differentiable ℂ entireXi := by
  unfold entireXi
  exact differentiable_const.add
    (((differentiable_const.mul differentiable_id).mul
      (differentiable_id.sub differentiable_const)).mul differentiable_completedZeta₀)

theorem entireXi_reflection (s : ℂ) : entireXi (1 - s) = entireXi s := by
  simp only [entireXi, completedRiemannZeta₀_one_sub]
  ring

def centeredEntireXi (z : ℂ) : ℂ := entireXi ((1 / 2 : ℂ) + z)

theorem centeredEntireXi_even (z : ℂ) :
    centeredEntireXi (-z) = centeredEntireXi z := by
  have heq : (1 / 2 : ℂ) + -z = 1 - ((1 / 2 : ℂ) + z) := by ring
  unfold centeredEntireXi
  rw [heq, entireXi_reflection]

/-- The old point-value problem does not depend on the numerator's derivative. -/
theorem raw_half_node_zero (numerator : ℂ) :
    (numerator / ((1 / 2 : ℂ) * rawXi 1)).re = 0 := by simp

/-- Reversing the index map is essential: an empty set cannot be Nat-indexed. -/
theorem no_nat_enumeration_of_empty {α : Type*} [IsEmpty α] (f : ℕ → α) : False :=
  isEmptyElim (f 0)

end ReviewerC4
end
