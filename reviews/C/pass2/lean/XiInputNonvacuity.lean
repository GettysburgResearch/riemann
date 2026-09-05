/-
Reviewer C source-derived regression candidate. NOT COMPILED in this audit.
Target: Riemann baseline 8d16f8d9c475db290bc85e53d775b93b9bcdb336,
shared ChallengeDeps blob 7d3dd6c98fd453d1810d80b0e1a39e2e4fbc7ab5.
This file is review evidence, not a trusted-spine import or an RH theorem.
-/
import RiemannComparatorChallengeDeps.XiPickOrderThreeConditional

namespace ReviewerC.Pass2

open ChallengeDeps.XiPickOrderThreeConditional

/-- The raw totalized product, unlike the intended entire Xi, is zero at 1. -/
theorem rawXi_one_eq_zero : riemannXi (1 : ℂ) = 0 := by
  norm_num [riemannXi]

/-- The centered function therefore vanishes at the positive half-node. -/
theorem centeredXi_half_eq_zero : centeredXi ((1 / 2 : ℝ) : ℂ) = 0 := by
  norm_num [centeredXi, riemannXi]

/-- No evaluation of the derivative is needed: the denominator is zero. -/
theorem node_half_eq_zero : actualXiNodeP (1 / 2 : ℝ) = 0 := by
  simp [actualXiNodeP, centeredXi_half_eq_zero]

/-- The stored strict diagonal positivity contradicts that exact zero. -/
theorem noActualXiOrderThreeInputs : ¬ Nonempty ActualXiOrderThreeInputs := by
  rintro ⟨inputs⟩
  have h := inputs.diagonalPositive inputs.grouped (1 / 2 : ℝ) (by norm_num)
  rw [node_half_eq_zero] at h
  exact (lt_irrefl (0 : ℝ)) h

/-- Independently, the total enumeration requires at least one off-line orbit. -/
theorem noGroupedOfNoOffLine
    (h : ∀ o : ReflectedOffLineOrbit, False) :
    ¬ Nonempty GroupedActualXiC2Expansion := by
  rintro ⟨grouped⟩
  exact h (grouped.offLineEnumeration 0)

#print axioms rawXi_one_eq_zero
#print axioms centeredXi_half_eq_zero
#print axioms node_half_eq_zero
#print axioms noActualXiOrderThreeInputs
#print axioms noGroupedOfNoOffLine

end ReviewerC.Pass2
