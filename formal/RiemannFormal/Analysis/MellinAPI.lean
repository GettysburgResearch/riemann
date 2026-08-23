import RiemannFormal.Analysis.Foundations
import Mathlib.Analysis.MellinTransform

open Complex Filter MeasureTheory Set

namespace RiemannFormal.Analysis

/-- Project-facing alias for Mathlib's Mellin transform. -/
abbrev MellinTransform {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E] :=
  @mellin E _ _

/-- Positive dilation is handled by Mathlib's exact Mellin change-of-variables theorem. -/
theorem mellin_dilation (f : ℝ → ℂ) (s : ℂ) {a : ℝ} (ha : 0 < a) :
    mellin (fun x => f (a * x)) s = (a : ℂ) ^ (-s) * mellin f s := by
  simpa [smul_eq_mul] using mellin_comp_mul_left f s ha

/-- Scalar multiplication commutes with the Mellin transform. -/
theorem mellin_const_mul (c : ℂ) (f : ℝ → ℂ) (s : ℂ) :
    mellin (fun x => c * f x) s = c * mellin f s := by
  simpa [smul_eq_mul] using mellin_const_smul f s c

/-- A two-term complex linear combination has the expected Mellin transform whenever both
summands converge. Iteration gives the finite-linear-combination API used by fixed detector
packets. -/
theorem hasMellin_linearCombination_two {f g : ℝ → ℂ} {s : ℂ}
    (a b : ℂ) (hf : MellinConvergent f s) (hg : MellinConvergent g s) :
    HasMellin (fun x => a * f x + b * g x) s
      (a * mellin f s + b * mellin g s) := by
  have hsum := hasMellin_add (hf.const_smul a) (hg.const_smul b)
  simpa [smul_eq_mul, mellin_const_smul] using hsum

/-- Mathlib's compact power kernel supplies an exact reusable compact-kernel transform. -/
theorem compact_power_kernel_hasMellin (a : ℂ) {s : ℂ} (hs : 0 < s.re + a.re) :
    HasMellin (Set.indicator (Set.Ioc 0 1) (fun t : ℝ => (t : ℂ) ^ a)) s
      (1 / (s + a)) :=
  hasMellin_cpow_Ioc a hs

/-- Power bounds at zero and infinity imply analyticity of the Mellin transform in the
corresponding vertical strip. This is a direct adapter around Mathlib's differentiability API. -/
theorem mellin_analyticAt_of_power_bounds
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    {a b : ℝ} {f : ℝ → E} {s : ℂ}
    (hfc : LocallyIntegrableOn f (Set.Ioi 0))
    (hf_top : f =O[Filter.atTop] (· ^ (-a))) (hs_top : s.re < a)
    (hf_bot : f =O[nhdsGT 0] (· ^ (-b))) (hs_bot : b < s.re) :
    AnalyticAt ℂ (mellin f) s :=
  (mellin_differentiableAt_of_isBigO_rpow hfc hf_top hs_top hf_bot hs_bot).analyticAt

end RiemannFormal.Analysis
