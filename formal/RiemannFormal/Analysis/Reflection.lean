import RiemannFormal.Analysis.Foundations

open Complex
open scoped ComplexConjugate

namespace RiemannFormal.Analysis

/-- The exact conjunction of hypotheses appearing in Mathlib's `RiemannHypothesis`. -/
structure RHAdmissibleZero (s : ℂ) : Prop where
  zeta_zero : riemannZeta s = 0
  nontrivial : ¬∃ n : ℕ, s = -2 * (n + 1)
  ne_one : s ≠ 1

/-- Functional-equation reflection in Mathlib's centered convention. -/
def rhReflect (s : ℂ) : ℂ := 1 - conj s

/-- The project RH alias is equivalent to critical-line placement for every admissible zero. -/
theorem rh_iff_admissibleZerosOnLine :
    RiemannFormal.RH ↔ ∀ s : ℂ, RHAdmissibleZero s → s.re = 1 / 2 := by
  constructor
  · intro hRH s hs
    exact hRH s hs.zeta_zero hs.nontrivial hs.ne_one
  · intro h s hz htrivial h1
    exact h s ⟨hz, htrivial, h1⟩

/-- Explicit adapter proposition asserting that functional-equation reflection preserves the full
Mathlib admissible-zero convention, including exclusion of the trivial zeros and `s = 1`. -/
def ReflectsRHAdmissibleZeros : Prop :=
  ∀ s : ℂ, RHAdmissibleZero s → RHAdmissibleZero (rhReflect s)

/-- Exclusion of admissible zeros strictly to the right of the critical line. -/
def NoAdmissibleZeroRightOfCriticalLine : Prop :=
  ∀ s : ℂ, RHAdmissibleZero s → s.re ≤ 1 / 2

/-- Right-half-plane exclusion plus the exact reflection adapter closes Mathlib's RH statement. -/
theorem functionalEquationReflection_closes_RH
    (hreflect : ReflectsRHAdmissibleZeros)
    (hright : NoAdmissibleZeroRightOfCriticalLine) :
    RiemannFormal.RH := by
  rw [rh_iff_admissibleZerosOnLine]
  intro s hs
  have hle : s.re ≤ 1 / 2 := hright s hs
  have hrefle : (rhReflect s).re ≤ 1 / 2 := hright (rhReflect s) (hreflect s hs)
  have hge : 1 / 2 ≤ s.re := by
    simp [rhReflect] at hrefle
    linarith
  exact le_antisymm hle hge

end RiemannFormal.Analysis
