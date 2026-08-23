import Mathlib

namespace ChallengeDeps.XiPickOrderThreeConditional

structure ExternalInputs
    (HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop) : Prop where
  highZeroVerified : HighZeroVerified
  correctedSourceLock : CorrectedSourceLock
  groupedC2Convergence : GroupedC2Convergence
  orbitConventionLocked : OrbitConventionLocked
  multiplicityResidualRetained : MultiplicityResidualRetained
  reciprocalSquareTailControlled : ReciprocalSquareTailControlled

def pickEntry (x p y q : ℝ) : ℝ := (x * p + y * q) / (x + y)

def quad3 (a b c d e f x y z : ℝ) : ℝ :=
  a * x ^ 2 + 2 * b * x * y + 2 * c * x * z +
    d * y ^ 2 + 2 * e * y * z + f * z ^ 2

def IsPSD3 (a b c d e f : ℝ) : Prop :=
  ∀ x y z : ℝ, 0 ≤ quad3 a b c d e f x y z

def pickDet2 (x p y q : ℝ) : ℝ := p * q - pickEntry x p y q ^ 2

def secondDivDiff (t1 t2 t3 y1 y2 y3 : ℝ) : ℝ :=
  y1 / ((t1 - t2) * (t1 - t3)) +
  y2 / ((t2 - t1) * (t2 - t3)) +
  y3 / ((t3 - t1) * (t3 - t2))

end ChallengeDeps.XiPickOrderThreeConditional
