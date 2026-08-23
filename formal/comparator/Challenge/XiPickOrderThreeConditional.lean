import ChallengeDeps.XiPickOrderThreeConditional

open ChallengeDeps.XiPickOrderThreeConditional

/-- Trusted challenge for the strongest honest ordered-distinct actual-Xi
order-three theorem.  Every external or unproved analytic input is explicit. -/
theorem XiPickOrderThreeConditional_psd
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (_external : ExternalInputs HighZeroVerified CorrectedSourceLock
      GroupedC2Convergence OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled)
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (hp1 : 0 < p1) (hp2 : 0 < p2) (hp3 : 0 < p3)
    (ht12 : x1 ^ 2 ≠ x2 ^ 2) (ht13 : x1 ^ 2 ≠ x3 ^ 2)
    (ht23 : x2 ^ 2 ≠ x3 ^ 2)
    (hminor12 : 0 < pickDet2 x1 p1 x2 p2)
    (hrecip : secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (1 / p1) (1 / p2) (1 / p3) ≤ 0)
    (hcomp : secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) ≤ 0) :
    IsPSD3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
      p2 (pickEntry x2 p2 x3 p3) p3 := by
  sorry
