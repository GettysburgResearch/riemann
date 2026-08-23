import ChallengeDeps.XiPickOrderThreeConditional
import RiemannFormal.Operator.XiOrderThree

open ChallengeDeps.XiPickOrderThreeConditional

/-- Sorry-free solution.  The source lock, external high-zero verification,
grouped C2 convergence, orbit convention, multiplicity residual, and tail
budget remain hypotheses. -/
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
  let external' : RiemannFormal.Operator.XiOrderThreeExternalInputs
      HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled :=
    ⟨_external.highZeroVerified, _external.correctedSourceLock,
      _external.groupedC2Convergence, _external.orbitConventionLocked,
      _external.multiplicityResidualRetained,
      _external.reciprocalSquareTailControlled⟩
  have h := RiemannFormal.Operator.actualXiOrderedDistinctPickOrderThree_of_inputs
    external' hx1 hx2 hx3 hp1 hp2 hp3 ht12 ht13 ht23 hminor12 hrecip hcomp
  simpa [ChallengeDeps.XiPickOrderThreeConditional.IsPSD3,
    ChallengeDeps.XiPickOrderThreeConditional.quad3,
    ChallengeDeps.XiPickOrderThreeConditional.pickEntry,
    ChallengeDeps.XiPickOrderThreeConditional.pickDet2,
    ChallengeDeps.XiPickOrderThreeConditional.secondDivDiff,
    RiemannFormal.Operator.IsPSD3,
    RiemannFormal.Operator.quad3,
    RiemannFormal.Operator.pickEntry,
    RiemannFormal.Operator.pickDet2,
    RiemannFormal.Operator.secondDivDiff] using h
