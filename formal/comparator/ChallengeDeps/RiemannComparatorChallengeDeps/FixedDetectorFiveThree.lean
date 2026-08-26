import Mathlib.Analysis.Complex.Basic

namespace ChallengeDeps.FixedDetectorFiveThree

def row2Numerator (a b : ℂ) : ℂ := 2 * a - 1 - b

def row3ScaledNumerator (a b : ℂ) : ℂ := 5 * b - a - 1 - 3 * a ^ 2

def fiveThreeNumerator (a b : ℂ) : ℂ :=
  5 * row2Numerator a b + row3ScaledNumerator a b

abbrev Statement : Prop :=
  ∀ a b : ℂ, ‖a‖ < 1 → fiveThreeNumerator a b ≠ 0

end ChallengeDeps.FixedDetectorFiveThree
