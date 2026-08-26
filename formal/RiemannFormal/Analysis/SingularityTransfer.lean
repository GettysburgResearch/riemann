import RiemannFormal.Analysis.Foundations
import Mathlib.Analysis.Meromorphic.Order

namespace RiemannFormal.Analysis

/-- A fixed holomorphic defect cannot remove a nonremovable singularity. -/
theorem fixed_holomorphic_defect_transfer
    {main defect : ℂ → ℂ} {s₀ : ℂ}
    (hdefect : AnalyticAt ℂ defect s₀)
    (hmain : NonremovableAt main s₀) :
    NonremovableAt (fun s => main s + defect s) s₀ := by
  intro hsum
  apply hmain
  apply (hsum.sub hdefect).congr
  filter_upwards with s
  simp

/-- Multiplication by a fixed nonvanishing analytic multiplier preserves a nonremovable
singularity. -/
theorem nonvanishing_multiplier_preserves_nonremovable
    {multiplier main : ℂ → ℂ} {s₀ : ℂ}
    (hmultiplier : AnalyticAt ℂ multiplier s₀)
    (hmultiplier_ne : multiplier s₀ ≠ 0)
    (hmain : NonremovableAt main s₀) :
    NonremovableAt (fun s => multiplier s * main s) s₀ := by
  intro hproduct
  apply hmain
  exact (analyticAt_iff_analytic_mul hmultiplier hmultiplier_ne).mpr hproduct

/-- Complete fixed-detector transfer: a nonvanishing multiplier and a fixed holomorphic defect
cannot remove the detector's singularity. -/
theorem fixed_mellin_singularity_transfer
    {main defect multiplier total : ℂ → ℂ} {s₀ : ℂ}
    (hdefect : AnalyticAt ℂ defect s₀)
    (hmultiplier : AnalyticAt ℂ multiplier s₀)
    (hmultiplier_ne : multiplier s₀ ≠ 0)
    (htotal : total = fun s => multiplier s * main s + defect s)
    (hmain : NonremovableAt main s₀) :
    NonremovableAt total s₀ := by
  rw [htotal]
  exact fixed_holomorphic_defect_transfer hdefect
    (nonvanishing_multiplier_preserves_nonremovable hmultiplier hmultiplier_ne hmain)

/-- Any function of strictly negative meromorphic order is nonremovable. -/
theorem nonremovable_of_meromorphicOrderAt_neg
    {f : ℂ → ℂ} {s₀ : ℂ}
    (horder : meromorphicOrderAt f s₀ < 0) :
    NonremovableAt f s₀ := by
  intro hanalytic
  exact (not_lt_of_ge hanalytic.meromorphicOrderAt_nonneg) horder

/-- Reciprocal meromorphic order, specialized to ζ. -/
theorem reciprocalZeta_meromorphicOrderAt (ρ : ℂ) :
    meromorphicOrderAt (riemannZeta⁻¹) ρ = -meromorphicOrderAt riemannZeta ρ :=
  meromorphicOrderAt_inv

/-- If ζ has declared meromorphic order `m`, its reciprocal has order `-m`. -/
theorem reciprocalZeta_order_of_zeta_order {ρ : ℂ} {m : ℤ}
    (horder : meromorphicOrderAt riemannZeta ρ = (m : WithTop ℤ)) :
    meromorphicOrderAt (riemannZeta⁻¹) ρ = -(m : WithTop ℤ) := by
  rw [reciprocalZeta_meromorphicOrderAt, horder]

/-- Zeta23's exact zero multiplicity becomes the reciprocal pole order at an open-strip zero. -/
theorem reciprocalZeta_order_of_projectZero
    {ρ : ℂ} (hρ : RiemannFormal.Upstream.ProjectNontrivialZero ρ) :
    meromorphicOrderAt (riemannZeta⁻¹) ρ =
      -((RiemannFormal.Upstream.ProjectZeroMultiplicity ρ : ℤ) : WithTop ℤ) := by
  rw [reciprocalZeta_meromorphicOrderAt,
    RiemannFormal.Upstream.projectRiemannZeta_meromorphicOrderAt_eq_zeroMultiplicity hρ]

end RiemannFormal.Analysis
