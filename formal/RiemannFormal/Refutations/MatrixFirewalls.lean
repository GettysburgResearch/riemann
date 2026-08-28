import RiemannFormal.Operator.FiniteMatrix
import RiemannFormal.Operator.HeatQ4Finite

namespace RiemannFormal.Refutations

open RiemannFormal.Operator

/-- A positive Schur correction is adverse: subtracting `z^2/c` never raises
the visible scalar direction. -/
theorem positiveSchurCorrection_le
    {b z c : ℝ} (hc : 0 < c) : b - z ^ 2 / c ≤ b := by
  have hnonneg : 0 ≤ z ^ 2 / c := div_nonneg (sq_nonneg _) (le_of_lt hc)
  linarith

/-- Exact positive-Schur-rescue firewall. -/
theorem positiveSchurCannotRescue
    {b z c : ℝ} (hb : b < 0) (hc : 0 < c) :
    b - z ^ 2 / c < 0 := by
  exact lt_of_le_of_lt (positiveSchurCorrection_le hc) hb

/-- An `l2` coefficient budget does not imply contraction of coherent
summation.  The exact rational witness is `(3/5,3/5)`. -/
theorem coefficientBudgetDoesNotImplyOperatorContraction :
    ∃ a b : ℝ, a ^ 2 + b ^ 2 ≤ 1 ∧ 1 < (a + b) ^ 2 := by
  refine ⟨3 / 5, 3 / 5, ?_, ?_⟩
  · norm_num
  · norm_num

/-- Vanishing negative inertia does not bound a current parameter: PSD examples
exist with an arbitrarily large displayed current. -/
theorem smallNegativeInertiaDoesNotControlCurrent (M : ℝ) :
    ∃ I : ℝ, M < I ∧ IsPSD2 (I ^ 2) 0 1 := by
  refine ⟨M + 1, by linarith, ?_⟩
  intro x y
  simp [quad2]
  positivity

/-- A symmetric two-by-two form represented by two real squares is PSD. -/
def IsTwoPositiveSquares (a b c : ℝ) : Prop :=
  ∃ u1 u2 v1 v2 : ℝ, ∀ x y : ℝ,
    quad2 a b c x y = (u1 * x + u2 * y) ^ 2 + (v1 * x + v2 * y) ^ 2

/-- Two-square representations cannot contain a negative direction. -/
theorem twoPositiveSquares_psd
    {a b c : ℝ} (h : IsTwoPositiveSquares a b c) : IsPSD2 a b c := by
  rcases h with ⟨u1, u2, v1, v2, h⟩
  intro x y
  rw [h]
  exact add_nonneg (sq_nonneg _) (sq_nonneg _)

/-- The reviewed hyperbolic pole block `[[0,1],[1,0]]` has a negative
direction, so it is not two positive squares. -/
theorem hyperbolicPoleBlockNotTwoPositiveSquares :
    ¬ IsTwoPositiveSquares 0 1 0 := by
  intro h
  have hpsd : IsPSD2 0 1 0 := twoPositiveSquares_psd h
  have hneg := hpsd 1 (-1)
  norm_num [quad2] at hneg

/-- Positive excess in `Q = root^2 + excess` does not orient the root. -/
theorem positiveExcessDoesNotControlSquareRoot :
    ∃ root excess : ℝ,
      0 ≤ excess ∧ 0 ≤ root ^ 2 + excess ∧ ¬ 0 ≤ root := by
  refine ⟨-1, 1, by norm_num, by norm_num, by norm_num⟩

/-- The scalar diagonal `(1,1)` does not determine the polarized Gram:
one off-diagonal choice is PSD and another has a negative direction. -/
theorem scalarDiagonalDoesNotDeterminePolarizedGram :
    IsPSD2 1 0 1 ∧ ¬ IsPSD2 1 2 1 := by
  constructor
  · intro x y
    simp [quad2]
    positivity
  · intro h
    have hneg := h 1 (-1)
    norm_num [quad2] at hneg

end RiemannFormal.Refutations
