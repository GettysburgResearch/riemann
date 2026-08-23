import RiemannFormal.Statement.RH
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.NumberTheory.LSeries.ZetaZeros

open Complex

namespace RiemannFormal.Upstream

/-- The project RH proposition is definitionally Mathlib's proposition. -/
theorem projectRH_is_mathlib : RiemannFormal.RH ↔ RiemannHypothesis := Iff.rfl

/-- Project-facing name for Mathlib's meromorphic continuation of ζ. -/
abbrev projectRiemannZeta : ℂ → ℂ := riemannZeta

/-- Project-facing name for Mathlib's completed ζ with poles at `0` and `1`. -/
abbrev projectCompletedZeta : ℂ → ℂ := completedRiemannZeta

/-- Project-facing name for Mathlib's entire completed ζ normalization. -/
abbrev projectEntireCompletedZeta : ℂ → ℂ := completedRiemannZeta₀

/-- ζ is analytic at every point except its pole convention at `1`. -/
theorem projectRiemannZeta_analyticAt {s : ℂ} (hs : s ≠ 1) :
    AnalyticAt ℂ projectRiemannZeta s :=
  (differentiableAt_riemannZeta hs).analyticAt

/-- The completed meromorphic normalization is analytic away from `0` and `1`. -/
theorem projectCompletedZeta_analyticAt {s : ℂ} (h0 : s ≠ 0) (h1 : s ≠ 1) :
    AnalyticAt ℂ projectCompletedZeta s :=
  (differentiableAt_completedZeta h0 h1).analyticAt

/-- Mathlib's entire completed normalization is analytic everywhere. -/
theorem projectEntireCompletedZeta_analyticAt (s : ℂ) :
    AnalyticAt ℂ projectEntireCompletedZeta s :=
  (differentiable_completedZeta₀ s).analyticAt

/-- Functional equation for the entire completed normalization, with no exceptional points. -/
theorem projectEntireCompletedZeta_one_sub (s : ℂ) :
    projectEntireCompletedZeta (1 - s) = projectEntireCompletedZeta s :=
  completedRiemannZeta₀_one_sub s

/-- Functional equation for the meromorphic completed normalization. -/
theorem projectCompletedZeta_one_sub (s : ℂ) :
    projectCompletedZeta (1 - s) = projectCompletedZeta s :=
  completedRiemannZeta_one_sub s

/-- The quotient normalization relating ζ and completed ζ; the point `s = 0` is explicit. -/
theorem projectRiemannZeta_eq_completed_div_gamma {s : ℂ} (hs : s ≠ 0) :
    projectRiemannZeta s = projectCompletedZeta s / Complex.Gammaℝ s :=
  riemannZeta_def_of_ne_zero hs

/-- Membership in Mathlib's discrete zero set is exactly vanishing of ζ. -/
theorem mem_projectRiemannZetaZeros {s : ℂ} :
    s ∈ riemannZetaZeros ↔ projectRiemannZeta s = 0 :=
  mem_riemannZetaZeros

/-- Any compact complex set contains only finitely many ζ zeros. -/
theorem compact_inter_projectRiemannZetaZeros_finite {K : Set ℂ} (hK : IsCompact K) :
    (K ∩ riemannZetaZeros).Finite :=
  hK.inter_riemannZetaZeros_finite

/-- The meromorphic order of the reciprocal is the negative meromorphic order. -/
theorem reciprocal_meromorphicOrderAt (f : ℂ → ℂ) (s : ℂ) :
    meromorphicOrderAt (f⁻¹) s = -meromorphicOrderAt f s :=
  meromorphicOrderAt_inv

/-- A zero of declared meromorphic order `m` becomes a reciprocal pole of order `-m`. -/
theorem reciprocal_order_of_order {f : ℂ → ℂ} {s : ℂ} {m : ℤ}
    (horder : meromorphicOrderAt f s = (m : WithTop ℤ)) :
    meromorphicOrderAt (f⁻¹) s = -(m : WithTop ℤ) := by
  rw [reciprocal_meromorphicOrderAt, horder]

end RiemannFormal.Upstream
