import RiemannFormal.Operator.FiniteMatrix

namespace RiemannFormal.Operator

/-- First four physicists' Hermite polynomials, used only at finite algebraic
scope. -/
def hermite0 (_x : ℝ) : ℝ := 1
def hermite1 (x : ℝ) : ℝ := 2 * x
def hermite2 (x : ℝ) : ℝ := 4 * x ^ 2 - 2
def hermite3 (x : ℝ) : ℝ := 8 * x ^ 3 - 12 * x

/-- Finite Hermite recurrence at order two. -/
theorem hermite2_recurrence (x : ℝ) :
    hermite2 x = 2 * x * hermite1 x - 2 * hermite0 x := by
  simp [hermite0, hermite1, hermite2]
  ring

/-- Finite Hermite recurrence at order three. -/
theorem hermite3_recurrence (x : ℝ) :
    hermite3 x = 2 * x * hermite2 x - 4 * hermite1 x := by
  simp [hermite1, hermite2, hermite3]
  ring

/-- The first finite scale-four filter. -/
def q4Filter1 (a b : ℝ) : ℝ := a - 2 * b

/-- The exact square of the first-difference filter. -/
def q4Filter2 (a b c : ℝ) : ℝ := a - 2 * b + c

/-- A second finite difference is a difference of adjacent first differences. -/
theorem q4Filter2_factor (a b c : ℝ) :
    q4Filter2 a b c = (a - b) - (b - c) := by
  ring

/-- Filter composition identity used by finite Q4 packets. -/
theorem q4Filter_composition (a b c : ℝ) :
    q4Filter1 (a - b) (b - c) = a - 3 * b + 2 * c := by
  simp [q4Filter1]
  ring

/-- Determinant of the reviewed zero-bare Q4 two-by-two block. -/
def q4ZeroBareDet (R E T I : ℝ) : ℝ :=
  det2 (R * I ^ 2) (E * I - T / 2) 1

/-- Exact finite Q4 determinant identity. -/
theorem q4ZeroBareDet_identity (R E T I : ℝ) :
    q4ZeroBareDet R E T I =
      (R - E ^ 2) * I ^ 2 + E * T * I - T ^ 2 / 4 := by
  simp [q4ZeroBareDet, det2]
  ring

/-- The hyperbolic pole block has determinant `-1`. -/
theorem hyperbolicPoleBlock_det : det2 0 1 0 = -1 := by
  norm_num [det2]

end RiemannFormal.Operator
