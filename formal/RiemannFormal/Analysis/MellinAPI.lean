import RiemannFormal.Analysis.Foundations
import Mathlib.Analysis.MellinTransform
import Mathlib.Tactic

open Complex Filter MeasureTheory Set
open scoped Topology

noncomputable section

namespace RiemannFormal.Analysis

/-- Project-facing alias for Mathlib's standard Mellin transform on `(0, ∞)`. -/
abbrev MellinTransform {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E] :=
  @mellin E _ _

/-- Positive dilation is handled by Mathlib's exact Mellin change-of-variables theorem. -/
theorem mellin_dilation (f : ℝ → ℂ) (s : ℂ) {a : ℝ} (ha : 0 < a) :
    mellin (fun x => f (a * x)) s = (a : ℂ) ^ (-s) * mellin f s := by
  simpa [smul_eq_mul] using mellin_comp_mul_left f s ha

/-- Scalar multiplication commutes with the standard Mellin transform. -/
theorem mellin_const_mul (c : ℂ) (f : ℝ → ℂ) (s : ℂ) :
    mellin (fun x => c * f x) s = c * mellin f s := by
  simpa [smul_eq_mul] using mellin_const_smul f s c

/-- A two-term complex linear combination has the expected standard Mellin transform whenever
both summands converge. This declaration intentionally promises two terms, not an arbitrary
finite family. -/
theorem hasMellin_linearCombination_two {f g : ℝ → ℂ} {s : ℂ}
    (a b : ℂ) (hf : MellinConvergent f s) (hg : MellinConvergent g s) :
    HasMellin (fun x => a * f x + b * g x) s
      (a * mellin f s + b * mellin g s) := by
  have hsum := hasMellin_add (hf.const_smul a) (hg.const_smul b)
  simp only [smul_eq_mul] at hsum
  rw [mellin_const_mul a f s, mellin_const_mul b g s] at hsum
  exact hsum

/-- Mathlib's compact power kernel supplies an exact reusable compact-kernel transform. -/
theorem compact_power_kernel_hasMellin (a : ℂ) {s : ℂ} (hs : 0 < s.re + a.re) :
    HasMellin (Set.indicator (Set.Ioc 0 1) (fun t : ℝ => (t : ℂ) ^ a)) s
      (1 / (s + a)) :=
  hasMellin_cpow_Ioc a hs

/-- Power bounds at zero and infinity imply analyticity of the standard Mellin transform in the
corresponding vertical strip. -/
theorem mellin_analyticAt_of_power_bounds
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    {a b : ℝ} {f : ℝ → E} {s : ℂ}
    (hfc : LocallyIntegrableOn f (Set.Ioi 0))
    (hf_top : f =O[Filter.atTop] (· ^ (-a))) (hs_top : s.re < a)
    (hf_bot : f =O[𝓝[>] 0] (· ^ (-b))) (hs_bot : b < s.re) :
    AnalyticAt ℂ (mellin f) s := by
  by_cases hE : CompleteSpace E
  · letI := hE
    rw [analyticAt_iff_eventually_differentiableAt]
    filter_upwards
        [(continuous_re.tendsto s).eventually (Iio_mem_nhds hs_top),
          (continuous_re.tendsto s).eventually (Ioi_mem_nhds hs_bot)] with z hz_top hz_bot
    exact mellin_differentiableAt_of_isBigO_rpow hfc hf_top hz_top hf_bot hz_bot
  · have hmellin : mellin f = 0 := by
      funext z
      simp [mellin, integral, hE]
    rw [hmellin]
    exact analyticAt_const

/-! ## Direct tail-Mellin convention used by the canonical consumer -/

/-- Integrand for the reviewed tail transform
`∫_[1,∞) f(x) x^(-s-1) dx`. -/
def tailMellinIntegrand (f : ℝ → ℂ) (s : ℂ) (x : ℝ) : ℂ :=
  f x * (x : ℂ) ^ (-s - 1)

/-- The reviewed Mellin tail transform. Its domain is exactly `[1, ∞)`, so no behavior below
`1` is silently imported from Mathlib's standard Mellin convention. -/
noncomputable def tailMellin (f : ℝ → ℂ) (s : ℂ) : ℂ :=
  ∫ x in Set.Ici (1 : ℝ), tailMellinIntegrand f s x

/-- Absolute convergence of the reviewed tail transform at one complex point. -/
def TailMellinConvergent (f : ℝ → ℂ) (s : ℂ) : Prop :=
  Integrable (tailMellinIntegrand f s) (volume.restrict (Set.Ici (1 : ℝ)))

/-- Tail-transform equality bundled with absolute convergence. -/
def HasTailMellin (f : ℝ → ℂ) (s value : ℂ) : Prop :=
  TailMellinConvergent f s ∧ tailMellin f s = value

/-- Jordan decomposition commutes with the tail transform whenever the full detector and its
negative part both converge. -/
theorem tailMellin_positivePart_eq_add_negativePart
    {f : Detector} {s : ℂ}
    (hf : TailMellinConvergent (fun x => (f x : ℂ)) s)
    (hneg : TailMellinConvergent (fun x => (negativePart f x : ℂ)) s) :
    TailMellinConvergent (fun x => (positivePart f x : ℂ)) s ∧
      tailMellin (fun x => (positivePart f x : ℂ)) s =
        tailMellin (fun x => (f x : ℂ)) s +
          tailMellin (fun x => (negativePart f x : ℂ)) s := by
  have hfun :
      tailMellinIntegrand (fun x => (positivePart f x : ℂ)) s =
        fun x =>
          tailMellinIntegrand (fun x => (f x : ℂ)) s x +
            tailMellinIntegrand (fun x => (negativePart f x : ℂ)) s x := by
    funext x
    simp [tailMellinIntegrand, positivePart_eq_add_negativePart, add_mul]
  have hf' :
      Integrable
        (tailMellinIntegrand (fun x => (f x : ℂ)) s)
        (volume.restrict (Set.Ici (1 : ℝ))) :=
    hf
  have hneg' :
      Integrable
        (tailMellinIntegrand (fun x => (negativePart f x : ℂ)) s)
        (volume.restrict (Set.Ici (1 : ℝ))) :=
    hneg
  constructor
  · change Integrable
      (tailMellinIntegrand (fun x => (positivePart f x : ℂ)) s)
      (volume.restrict (Set.Ici (1 : ℝ)))
    rw [hfun]
    exact hf'.add hneg'
  · unfold tailMellin
    rw [hfun, integral_add hf' hneg']

/-! ## Fixed logarithmic box multiplier -/

/-- Multiplier of one fixed multiplicative logarithmic box of width `A > 1`. -/
def logBoxMultiplier (A : ℝ) (s : ℂ) : ℂ :=
  (1 - (A : ℂ) ^ (-s)) / s

/-- The logarithmic-box multiplier is analytic at every point of the open right half-plane. -/
theorem logBoxMultiplier_analyticAt {A : ℝ} (hA : 1 < A) {s : ℂ} (hs : 0 < s.re) :
    AnalyticAt ℂ (logBoxMultiplier A) s := by
  have hA0 : (A : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (ne_of_gt (lt_trans zero_lt_one hA))
  have hpow : AnalyticAt ℂ (fun z : ℂ => (A : ℂ) ^ (-z)) s := by
    rw [analyticAt_iff_eventually_differentiableAt]
    filter_upwards with z
    exact (differentiableAt_id.neg).const_cpow (Or.inl hA0)
  have hs0 : s ≠ 0 := by
    intro h
    rw [h] at hs
    simp at hs
  apply ((analyticAt_const.sub hpow).div analyticAt_id hs0).congr
  filter_upwards with z
  rfl

/-- The logarithmic-box multiplier has no zero in `Re(s) > 0`. -/
theorem logBoxMultiplier_nonzero {A : ℝ} (hA : 1 < A) {s : ℂ} (hs : 0 < s.re) :
    logBoxMultiplier A s ≠ 0 := by
  have hApos : 0 < A := lt_trans zero_lt_one hA
  have hs0 : s ≠ 0 := by
    intro h
    rw [h] at hs
    simp at hs
  have hnorm : ‖(A : ℂ) ^ (-s)‖ < 1 := by
    rw [norm_cpow_eq_rpow_re_of_pos hApos]
    simp only [neg_re]
    rw [Real.rpow_neg hApos.le, inv_lt_one_iff₀]
    exact Or.inr (Real.one_lt_rpow hA hs)
  have hpow_ne : (A : ℂ) ^ (-s) ≠ 1 := by
    intro h
    have hnorm_eq : ‖(A : ℂ) ^ (-s)‖ = 1 := by simp [h]
    linarith
  exact div_ne_zero (sub_ne_zero.mpr hpow_ne.symm) hs0

end RiemannFormal.Analysis
