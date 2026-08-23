import RiemannFormal.Operator.PickAlgebra
import RiemannFormal.Operator.ReciprocalConcavity

namespace RiemannFormal.Operator

/-- The external and grouped analytic inputs which are not silently converted
into axioms.  An inhabitant supplies proofs of every named proposition. -/
structure XiOrderThreeExternalInputs
    (HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop) : Prop where
  highZeroVerified : HighZeroVerified
  correctedSourceLock : CorrectedSourceLock
  groupedC2Convergence : GroupedC2Convergence
  orbitConventionLocked : OrbitConventionLocked
  multiplicityResidualRetained : MultiplicityResidualRetained
  reciprocalSquareTailControlled : ReciprocalSquareTailControlled

/-- One ordered three-node scalar Pick packet. -/
structure ThreeNodePickData where
  x1 : ℝ
  x2 : ℝ
  x3 : ℝ
  p1 : ℝ
  p2 : ℝ
  p3 : ℝ

/-- Canonical finite conclusion through packet size three.  This records PSD,
not distinct-node positive definiteness. -/
structure PickPSDThroughThree (P : ThreeNodePickData) : Prop where
  one1 : 0 ≤ P.p1
  one2 : 0 ≤ P.p2
  one3 : 0 ≤ P.p3
  pair12 : IsPSD2 P.p1 (pickEntry P.x1 P.p1 P.x2 P.p2) P.p2
  pair13 : IsPSD2 P.p1 (pickEntry P.x1 P.p1 P.x3 P.p3) P.p3
  pair23 : IsPSD2 P.p2 (pickEntry P.x2 P.p2 P.x3 P.p3) P.p3
  triple : IsPSD3 P.p1 (pickEntry P.x1 P.p1 P.x2 P.p2)
    (pickEntry P.x1 P.p1 P.x3 P.p3) P.p2
    (pickEntry P.x2 P.p2 P.x3 P.p3) P.p3

/-- Exact order-two PSD consequence of the reviewed pair of scalar
monotonicities. -/
theorem actualXiPickOrderTwo_of_monotonicity
    {x y p q : ℝ}
    (hp0 : 0 < p)
    (hp : q ≤ p)
    (htp : x ^ 2 * p ≤ y ^ 2 * q)
    (hxy : x + y ≠ 0) :
    IsPSD2 p (pickEntry x p y q) q := by
  apply principal_minors_psd2 hp0
  have hdet : 0 ≤ pickDet2 x p y q :=
    two_point_pick_nonnegative hp htp hxy
  simpa [det2, pickDet2] using hdet

/-- Conditional grouped actual-Xi reciprocal-concavity assembly.  The grouped
`C^2` passage and every external source proposition are explicit parameters;
Lean proves only the finite positive-sum curvature step. -/
theorem actualXiReciprocalConcavity_of_grouped_inputs
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (_external : XiOrderThreeExternalInputs HighZeroVerified CorrectedSourceLock
      GroupedC2Convergence OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled)
    {critical offLine total : Jet2}
    (hcriticalPos : 0 < critical.value)
    (hoffLinePos : 0 < offLine.value)
    (hcritical : 0 ≤ Jet2.energy critical)
    (hoffLine : 0 ≤ Jet2.energy offLine)
    (htotal : total = Jet2.add critical offLine) :
    0 ≤ Jet2.energy total := by
  rw [htotal]
  exact Jet2.reciprocalConcavity_add hcriticalPos hoffLinePos hcritical hoffLine

/-- Conditional grouped companion-curvature closure.  This is the exact finite
linearity step; grouped convergence remains a visible external hypothesis. -/
theorem actualXiCompanionCurvature_of_grouped_inputs
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (_external : XiOrderThreeExternalInputs HighZeroVerified CorrectedSourceLock
      GroupedC2Convergence OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled)
    {t1 t2 t3 a1 a2 a3 b1 b2 b3 : ℝ}
    (ha : secondDivDiff t1 t2 t3 a1 a2 a3 ≤ 0)
    (hb : secondDivDiff t1 t2 t3 b1 b2 b3 ≤ 0) :
    secondDivDiff t1 t2 t3 (a1 + b1) (a2 + b2) (a3 + b3) ≤ 0 :=
  secondDivDiff_add_nonpositive ha hb

/-- Conditional finite reserve allocation.  The published high-zero statement,
corrected source lock, grouped convergence, and reciprocal-square tail are all
arguments rather than axioms. -/
theorem criticalReserveAllocation_of_inputs
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (_external : XiOrderThreeExternalInputs HighZeroVerified CorrectedSourceLock
      GroupedC2Convergence OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled)
    {n : Nat} (epsilon tail : Fin n → ℝ)
    (hpoint : ∀ i, epsilon i ≤ 9 * tail i)
    (htail : (∑ i, tail i) < 1 / 9) :
    ∃ epsilon0 : ℝ, 0 < epsilon0 ∧ epsilon0 + ∑ i, epsilon i = 1 := by
  have hsum : (∑ i, epsilon i) < 1 :=
    Jet2.reciprocalSquareTailBudget epsilon tail hpoint htail
  exact Jet2.finiteReserveAllocation epsilon hsum

/-- Strongest honest ordered-distinct order-three theorem.  All analytic inputs
and both scalar curvature signs are explicit.  The conclusion is PSD. -/
theorem actualXiOrderedDistinctPickOrderThree_of_inputs
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (_external : XiOrderThreeExternalInputs HighZeroVerified CorrectedSourceLock
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
  have hdet : 0 ≤ pickDet3 x1 x2 x3 p1 p2 p3 :=
    three_node_pick_det_nonnegative hx1 hx2 hx3 hp1 hp2 hp3
      ht12 ht13 ht23 hrecip hcomp
  exact three_node_pick_psd_of_principal_minors hp1 hminor12 hdet

/-- Honest conditional actual-Xi PSD theorem for one packet of size three.
Repeated-node reduction is a functional hypothesis.  On the distinct-node
branch Lean derives PSD from the exact determinant factorization and the two
scalar curvature signs. -/
theorem actualXiPickOrderThreeConditional
    {HighZeroVerified CorrectedSourceLock GroupedC2Convergence
      OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled : Prop}
    (external : XiOrderThreeExternalInputs HighZeroVerified CorrectedSourceLock
      GroupedC2Convergence OrbitConventionLocked MultiplicityResidualRetained
      ReciprocalSquareTailControlled)
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (hp1 : 0 < p1) (hp2 : 0 < p2) (hp3 : 0 < p3)
    (hrepeated :
      (x1 ^ 2 = x2 ^ 2 ∨ x1 ^ 2 = x3 ^ 2 ∨ x2 ^ 2 = x3 ^ 2) →
        IsPSD3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
          p2 (pickEntry x2 p2 x3 p3) p3)
    (hminor12 : x1 ^ 2 ≠ x2 ^ 2 → 0 < pickDet2 x1 p1 x2 p2)
    (hrecip :
      x1 ^ 2 ≠ x2 ^ 2 → x1 ^ 2 ≠ x3 ^ 2 → x2 ^ 2 ≠ x3 ^ 2 →
        secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (1 / p1) (1 / p2) (1 / p3) ≤ 0)
    (hcomp :
      x1 ^ 2 ≠ x2 ^ 2 → x1 ^ 2 ≠ x3 ^ 2 → x2 ^ 2 ≠ x3 ^ 2 →
        secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) ≤ 0) :
    IsPSD3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
      p2 (pickEntry x2 p2 x3 p3) p3 := by
  by_cases h12 : x1 ^ 2 = x2 ^ 2
  · exact hrepeated (Or.inl h12)
  by_cases h13 : x1 ^ 2 = x3 ^ 2
  · exact hrepeated (Or.inr (Or.inl h13))
  by_cases h23 : x2 ^ 2 = x3 ^ 2
  · exact hrepeated (Or.inr (Or.inr h23))
  exact actualXiOrderedDistinctPickOrderThree_of_inputs external
    hx1 hx2 hx3 hp1 hp2 hp3 h12 h13 h23 (hminor12 h12)
      (hrecip h12 h13 h23) (hcomp h12 h13 h23)

end RiemannFormal.Operator
