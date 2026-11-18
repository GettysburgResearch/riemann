import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Observatory

/-- The scalar minimum estimate with `h = u²` and inverse scale `v`. -/
theorem twoScaleScalarBound (u v C X : ℝ)
    (hu : 0 ≤ u) (hu1 : u ≤ 1) (hv : 0 < v) (_hv1 : v ≤ 1)
    (hC : 0 ≤ C) (coarse : X ≤ C * (u ^ 4 + v ^ 6))
    (fine : X * v ^ 2 ≤ C * u ^ 4) :
    X ≤ 2 * C * u ^ 3 := by
  have hu3 : 0 ≤ u ^ 3 := pow_nonneg hu 3
  have hCu3 : 0 ≤ C * u ^ 3 := mul_nonneg hC hu3
  by_cases cut : u ≤ v ^ 2
  · have hmul : X * v ^ 2 ≤ (C * u ^ 3) * v ^ 2 := calc
      X * v ^ 2 ≤ C * u ^ 4 := fine
      _ = (C * u ^ 3) * u := by ring
      _ ≤ (C * u ^ 3) * v ^ 2 := mul_le_mul_of_nonneg_left cut hCu3
    have hX : X ≤ C * u ^ 3 := le_of_mul_le_mul_right hmul (pow_pos hv 2)
    linarith
  · have hv6 : v ^ 6 ≤ u ^ 3 := calc
      v ^ 6 = (v ^ 2) ^ 3 := by ring
      _ ≤ u ^ 3 := pow_le_pow_left₀ (sq_nonneg v) (le_of_not_ge cut) 3
    have hu4 : u ^ 4 ≤ u ^ 3 := calc
      u ^ 4 = u ^ 3 * u := by ring
      _ ≤ u ^ 3 * 1 := mul_le_mul_of_nonneg_left hu1 hu3
      _ = u ^ 3 := mul_one _
    calc
      X ≤ C * (u ^ 4 + v ^ 6) := coarse
      _ ≤ C * (u ^ 3 + u ^ 3) := mul_le_mul_of_nonneg_left (add_le_add hu4 hv6) hC
      _ = 2 * C * u ^ 3 := by ring

end Observatory

#check Observatory.twoScaleScalarBound
#print axioms Observatory.twoScaleScalarBound
