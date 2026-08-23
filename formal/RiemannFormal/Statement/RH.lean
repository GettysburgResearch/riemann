import Mathlib.NumberTheory.LSeries.RiemannZeta

namespace RiemannFormal

/-- The project uses Mathlib's canonical formulation of the Riemann Hypothesis. -/
abbrev RH : Prop := RiemannHypothesis

/-- The project alias is definitionally the Mathlib proposition. -/
theorem rh_iff_mathlib : RH ↔ RiemannHypothesis := Iff.rfl

end RiemannFormal
