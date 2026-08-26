import Mathlib.Analysis.Complex.Basic

namespace ChallengeDeps.ArithmeticRows23

def row2Numerator (a b : ℂ) : ℂ := 2 * a - 1 - b

def row3ScaledNumerator (a b : ℂ) : ℂ := 5 * b - a - 1 - 3 * a ^ 2

abbrev Statement : Prop :=
  ∀ a b : ℂ, ‖a‖ < 1 →
    row2Numerator a b ≠ 0 ∨ row3ScaledNumerator a b ≠ 0

end ChallengeDeps.ArithmeticRows23
