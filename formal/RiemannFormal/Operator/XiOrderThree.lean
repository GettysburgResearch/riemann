import RiemannFormal.Operator.PickAlgebra
import RiemannFormal.Operator.RepeatedNodes
import RiemannFormal.Operator.XiExternalInputs
import RiemannFormal.Operator.XiSourceSpecific

namespace RiemannFormal.Operator

open ChallengeDeps.XiPickOrderThreeConditional

private theorem sharedPSD2_to_local {a b c : ℝ}
    (h : ChallengeDeps.XiPickOrderThreeConditional.IsPSD2 a b c) :
    IsPSD2 a b c := by
  intro x y
  simpa [ChallengeDeps.XiPickOrderThreeConditional.IsPSD2,
    ChallengeDeps.XiPickOrderThreeConditional.quad2, IsPSD2, quad2] using h x y

private theorem localPSD2_to_shared {a b c : ℝ}
    (h : IsPSD2 a b c) :
    ChallengeDeps.XiPickOrderThreeConditional.IsPSD2 a b c := by
  intro x y
  simpa [ChallengeDeps.XiPickOrderThreeConditional.IsPSD2,
    ChallengeDeps.XiPickOrderThreeConditional.quad2, IsPSD2, quad2] using h x y

private theorem localPSD3_to_shared {a b c d e f : ℝ}
    (h : IsPSD3 a b c d e f) :
    ChallengeDeps.XiPickOrderThreeConditional.IsPSD3 a b c d e f := by
  intro x y z
  simpa [ChallengeDeps.XiPickOrderThreeConditional.IsPSD3,
    ChallengeDeps.XiPickOrderThreeConditional.quad3, IsPSD3, quad3] using h x y z

/-- Exact order-two actual-Xi bridge from the concrete verified-height theorem
and grouped expansion stored in the repaired input package. -/
theorem actualXiPickOrderTwo_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {x y : ℝ} (hx : 0 < x) (hy : 0 < y) :
    IsPSD2 (actualXiNodeP x)
      (pickEntry x (actualXiNodeP x) y (actualXiNodeP y))
      (actualXiNodeP y) := by
  apply sharedPSD2_to_local
  simpa [ChallengeDeps.XiPickOrderThreeConditional.pickEntry, pickEntry] using
    inputs.orderTwoPSD inputs.verified.criticalLineBelowHeight inputs.grouped
      x y hx hy


/-- Local uniform convergence on the declared domain gives pointwise filter
convergence.  This is the bridge used to derive energy convergence from the
three concrete C² component limits rather than assuming it as an extra field. -/
theorem locallyUniformSequence_tendsto_at
    {sequence : ℕ → ℝ → ℝ} {limit : ℝ → ℝ} {domain : Set ℝ}
    (h : LocallyUniformlyConvergesSequenceOn sequence limit domain)
    {t : ℝ} (ht : t ∈ domain) :
    Filter.Tendsto (fun n => sequence n t) Filter.atTop (𝓝 (limit t)) := by
  refine Metric.tendsto_atTop.2 ?_
  intro epsilon hepsilon
  obtain ⟨N, hN⟩ := h ({t} : Set ℝ) isCompact_singleton
    (by simpa only [Set.singleton_subset_iff] using ht) epsilon hepsilon
  refine ⟨N, ?_⟩
  intro n hn
  have hpoint := hN n hn t (by simp)
  simpa [Real.dist_eq] using hpoint

/-- Reciprocal energy converges because it is a polynomial in the value and
first two derivative coordinates.  No separate energy-limit hypothesis is
accepted by the repaired interface. -/
theorem regroupedActualXi_energy_tendsto
    {grouped : GroupedActualXiC2Expansion}
    {allocation : ActualXiReserveAllocation grouped}
    (approximation : RegroupedActualXiC2Approximation grouped allocation)
    {t : ℝ} (ht : 1 / 4 < t) :
    Filter.Tendsto
      (fun N => reciprocalEnergy
        (regroupedActualXiPrefix grouped allocation N t))
      Filter.atTop (𝓝 (reciprocalEnergy (actualXiTJet t))) := by
  have htDomain : t ∈ Set.Ioi (1 / 4) := ht
  have hvalue := locallyUniformSequence_tendsto_at
    approximation.valueConverges htDomain
  have hfirst := locallyUniformSequence_tendsto_at
    approximation.firstConverges htDomain
  have hsecond := locallyUniformSequence_tendsto_at
    approximation.secondConverges htDomain
  have htwo : Filter.Tendsto (fun _ : ℕ => (2 : ℝ)) Filter.atTop (𝓝 (2 : ℝ)) :=
    tendsto_const_nhds
  simpa [reciprocalEnergy] using
    (hvalue.mul hsecond).sub (htwo.mul (hfirst.mul hfirst))

/-- A nonnegative scalar sequence cannot converge in absolute difference to
a negative limit. -/
theorem nonnegative_of_absolute_convergence
    {sequence : ℕ → ℝ} {limit : ℝ}
    (hsequence : ∀ n : ℕ, 0 ≤ sequence n)
    (hconverges : ∀ epsilon : ℝ, 0 < epsilon →
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → |sequence n - limit| < epsilon) :
    0 ≤ limit := by
  by_contra hlimit
  have hnegative : limit < 0 := lt_of_not_ge hlimit
  let epsilon : ℝ := -limit / 2
  have hepsilon : 0 < epsilon := by
    dsimp [epsilon]
    linarith
  obtain ⟨N, hN⟩ := hconverges epsilon hepsilon
  have hclose := abs_lt.mp (hN N le_rfl)
  have hnonnegative := hsequence N
  dsimp [epsilon] at hclose
  linarith

/-- The actual-Xi differential reciprocal-concavity statement is derived from
nonnegative source-faithful paid prefixes and their explicit componentwise local C2
convergence; energy convergence is proved by polynomial continuity.  Final curvature is not an input field. -/
theorem actualXiReciprocalConcavity_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {t : ℝ} (ht : 1 / 4 < t) :
    0 ≤ reciprocalEnergy (actualXiTJet t) := by
  refine isClosed_Ici.mem_of_tendsto
    (regroupedActualXi_energy_tendsto inputs.paidC2Approximation ht) ?_
  exact Filter.Eventually.of_forall fun N =>
    inputs.paidC2Approximation.prefixEnergyNonnegative N t ht

/-- The source-specific companion curvature is likewise an exact conditional
bridge, not generic divided-difference linearity mislabeled as the Xi theorem. -/
theorem actualXiCompanionCurvature_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {x1 x2 x3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (h12 : x1 ^ 2 ≠ x2 ^ 2) (h13 : x1 ^ 2 ≠ x3 ^ 2)
    (h23 : x2 ^ 2 ≠ x3 ^ 2) :
    secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (x1 ^ 2 * actualXiNodeP x1)
      (x2 ^ 2 * actualXiNodeP x2)
      (x3 ^ 2 * actualXiNodeP x3) ≤ 0 := by
  simpa [ChallengeDeps.XiPickOrderThreeConditional.secondDivDiff,
    secondDivDiff] using
    inputs.companionCurvature inputs.grouped x1 x2 x3
      hx1 hx2 hx3 h12 h13 h23

/-- Exact conditional reciprocal divided-difference bridge. -/
theorem actualXiReciprocalCurvature_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {x1 x2 x3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (h12 : x1 ^ 2 ≠ x2 ^ 2) (h13 : x1 ^ 2 ≠ x3 ^ 2)
    (h23 : x2 ^ 2 ≠ x3 ^ 2) :
    secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (1 / actualXiNodeP x1) (1 / actualXiNodeP x2)
      (1 / actualXiNodeP x3) ≤ 0 := by
  simpa [ChallengeDeps.XiPickOrderThreeConditional.secondDivDiff,
    secondDivDiff] using
    inputs.reciprocalCurvature inputs.verified.sourceLockExact
      inputs.verified.criticalLineBelowHeight inputs.grouped inputs.residual
      inputs.reserve inputs.paidC2Approximation
      (fun t ht => actualXiReciprocalConcavity_of_inputs inputs ht)
      x1 x2 x3 hx1 hx2 hx3 h12 h13 h23

/-- Honest low-order Loewner interface: one actual-Xi two-node PSD statement
and the exact three-node companion curvature.  No all-order monotonicity is
asserted. -/
theorem actualXiLowOrderLoewner_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {x1 x2 x3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (h12 : x1 ^ 2 ≠ x2 ^ 2) (h13 : x1 ^ 2 ≠ x3 ^ 2)
    (h23 : x2 ^ 2 ≠ x3 ^ 2) :
    IsPSD2 (actualXiNodeP x1)
        (pickEntry x1 (actualXiNodeP x1) x2 (actualXiNodeP x2))
        (actualXiNodeP x2) ∧
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
        (x1 ^ 2 * actualXiNodeP x1)
        (x2 ^ 2 * actualXiNodeP x2)
        (x3 ^ 2 * actualXiNodeP x3) ≤ 0 :=
  ⟨actualXiPickOrderTwo_of_inputs inputs hx1 hx2,
    actualXiCompanionCurvature_of_inputs inputs hx1 hx2 hx3 h12 h13 h23⟩

/-- Ordered-distinct actual-Xi order-three PSD.  Every analytic/source input is
consumed through a concrete field of `ActualXiOrderThreeInputs`. -/
theorem actualXiOrderedDistinctPickOrderThree_of_inputs
    (inputs : ActualXiOrderThreeInputs)
    {x1 x2 x3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (h12 : x1 ^ 2 ≠ x2 ^ 2) (h13 : x1 ^ 2 ≠ x3 ^ 2)
    (h23 : x2 ^ 2 ≠ x3 ^ 2) :
    IsPSD3 (actualXiNodeP x1)
      (pickEntry x1 (actualXiNodeP x1) x2 (actualXiNodeP x2))
      (pickEntry x1 (actualXiNodeP x1) x3 (actualXiNodeP x3))
      (actualXiNodeP x2)
      (pickEntry x2 (actualXiNodeP x2) x3 (actualXiNodeP x3))
      (actualXiNodeP x3) := by
  have hp1 : 0 < actualXiNodeP x1 :=
    inputs.diagonalPositive inputs.grouped x1 hx1
  have hp2 : 0 < actualXiNodeP x2 :=
    inputs.diagonalPositive inputs.grouped x2 hx2
  have hp3 : 0 < actualXiNodeP x3 :=
    inputs.diagonalPositive inputs.grouped x3 hx3
  have hminor :
      0 < pickDet2 x1 (actualXiNodeP x1) x2 (actualXiNodeP x2) := by
    simpa [ChallengeDeps.XiPickOrderThreeConditional.pickDet2,
      ChallengeDeps.XiPickOrderThreeConditional.pickEntry,
      pickDet2, pickEntry] using
      inputs.distinctPairDetPositive inputs.verified.criticalLineBelowHeight
        inputs.grouped x1 x2 hx1 hx2 h12
  have hrecip := actualXiReciprocalCurvature_of_inputs inputs
    hx1 hx2 hx3 h12 h13 h23
  have hcomp := actualXiCompanionCurvature_of_inputs inputs
    hx1 hx2 hx3 h12 h13 h23
  have hdet :
      0 ≤ pickDet3 x1 x2 x3 (actualXiNodeP x1)
        (actualXiNodeP x2) (actualXiNodeP x3) :=
    three_node_pick_det_nonnegative hx1 hx2 hx3 hp1 hp2 hp3
      h12 h13 h23 hrecip hcomp
  exact three_node_pick_psd_of_principal_minors hp1 hminor hdet

/-- Full positive-node packet theorem.  Repeated nodes are proved by equality
of function evaluations and duplicate-row congruence, then reduced to the
actual-Xi order-two PSD theorem. -/
theorem actualXiPickOrderThreeConditional_local
    (inputs : ActualXiOrderThreeInputs)
    {x1 x2 x3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3) :
    IsPSD3 (actualXiNodeP x1)
      (pickEntry x1 (actualXiNodeP x1) x2 (actualXiNodeP x2))
      (pickEntry x1 (actualXiNodeP x1) x3 (actualXiNodeP x3))
      (actualXiNodeP x2)
      (pickEntry x2 (actualXiNodeP x2) x3 (actualXiNodeP x3))
      (actualXiNodeP x3) := by
  by_cases h12 : x1 ^ 2 = x2 ^ 2
  · have hxy : x1 = x2 := positive_node_eq_of_sq_eq hx1 hx2 h12
    subst x2
    exact repeated12_pick_psd actualXiNodeP hx1
      (actualXiPickOrderTwo_of_inputs inputs hx1 hx3)
  by_cases h13 : x1 ^ 2 = x3 ^ 2
  · have hxz : x1 = x3 := positive_node_eq_of_sq_eq hx1 hx3 h13
    subst x3
    exact repeated13_pick_psd actualXiNodeP hx1
      (actualXiPickOrderTwo_of_inputs inputs hx1 hx2)
  by_cases h23 : x2 ^ 2 = x3 ^ 2
  · have hyz : x2 = x3 := positive_node_eq_of_sq_eq hx2 hx3 h23
    subst x3
    exact repeated23_pick_psd actualXiNodeP hx2
      (actualXiPickOrderTwo_of_inputs inputs hx1 hx2)
  exact actualXiOrderedDistinctPickOrderThree_of_inputs inputs
    hx1 hx2 hx3 h12 h13 h23

/-- Comparator-facing repaired headline.  Its type is literally the shared
Mathlib-only `ChallengeStatement`: one-node, every two-node principal packet,
and the full three-node packet are PSD.  Repeated nodes are reduced rather than
assumed. -/
theorem actualXiPickOrderThreeConditional : ChallengeStatement := by
  intro inputs x1 x2 x3 hx1 hx2 hx3
  have h12local := actualXiPickOrderTwo_of_inputs inputs hx1 hx2
  have h13local := actualXiPickOrderTwo_of_inputs inputs hx1 hx3
  have h23local := actualXiPickOrderTwo_of_inputs inputs hx2 hx3
  have htripleLocal := actualXiPickOrderThreeConditional_local inputs hx1 hx2 hx3
  refine
    { one1 := le_of_lt (inputs.diagonalPositive inputs.grouped x1 hx1)
      one2 := le_of_lt (inputs.diagonalPositive inputs.grouped x2 hx2)
      one3 := le_of_lt (inputs.diagonalPositive inputs.grouped x3 hx3)
      pair12 := ?_
      pair13 := ?_
      pair23 := ?_
      triple := ?_ }
  · simpa [ChallengeDeps.XiPickOrderThreeConditional.pickEntry, pickEntry] using
      localPSD2_to_shared h12local
  · simpa [ChallengeDeps.XiPickOrderThreeConditional.pickEntry, pickEntry] using
      localPSD2_to_shared h13local
  · simpa [ChallengeDeps.XiPickOrderThreeConditional.pickEntry, pickEntry] using
      localPSD2_to_shared h23local
  · simpa [ChallengeDeps.XiPickOrderThreeConditional.pickEntry, pickEntry] using
      localPSD3_to_shared htripleLocal

end RiemannFormal.Operator
