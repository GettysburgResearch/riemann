import RiemannFormal.Upstream.MathlibBridge
import RiemannFormal.Upstream.SourceLocks
import Zeta23.Statement.SeamClosed
import Zeta23.ZetaReflect
import Zeta23.WeilEF.Main
import Zeta23.RvM.Statement

open Complex

namespace RiemannFormal.Upstream

/-- The project reuses Zeta23's exact open-strip zero convention. -/
abbrev ProjectNontrivialZero : ℂ → Prop := Zeta23.IsNontrivialZero

/-- Zeta23 multiplicity is the natural-valued analytic order of Mathlib's ζ. -/
abbrev ProjectZeroMultiplicity : ℂ → ℕ := Zeta23.zeroMult

/-- Centered coordinate `γ_ρ = (ρ - 1/2) / i`. -/
abbrev ProjectCenteredZero : ℂ → ℂ := Zeta23.gammaOf

/-- Functional-equation reflection `ρ ↦ 1 - conj ρ`. -/
abbrev ProjectReflectedZero : ℂ → ℂ := Zeta23.reflect

/-- The multiplicity convention is definitionally `analyticOrderAt ... |>.toNat`. -/
theorem projectZeroMultiplicity_def (ρ : ℂ) :
    ProjectZeroMultiplicity ρ = (analyticOrderAt riemannZeta ρ).toNat :=
  rfl

/-- Reconstruction from the centered coordinate. -/
theorem projectCenteredZero_reconstruct (ρ : ℂ) :
    (1 / 2 : ℂ) + Complex.I * ProjectCenteredZero ρ = ρ := by
  change (1 / 2 : ℂ) + Complex.I * ((ρ - 1 / 2) / Complex.I) = ρ
  field_simp [Complex.I_ne_zero]

/-- Reflection preserves the exact Zeta23 nontrivial-zero convention. -/
theorem projectReflectedZero_mem {ρ : ℂ} (hρ : ProjectNontrivialZero ρ) :
    ProjectNontrivialZero (ProjectReflectedZero ρ) :=
  Zeta23.zeta_reflect_zero ρ hρ

/-- Reflection preserves analytic-order multiplicity. -/
theorem projectReflectedZero_multiplicity {ρ : ℂ} (hρ : ProjectNontrivialZero ρ) :
    ProjectZeroMultiplicity (ProjectReflectedZero ρ) = ProjectZeroMultiplicity ρ :=
  Zeta23.zeta_mult_reflect ρ hρ

/-- Every bounded ordinate window of nontrivial zeros is finite. -/
theorem projectZeroWindow_finite (T₁ T₂ : ℝ) :
    (Zeta23.zerosIn T₁ T₂).Finite :=
  Zeta23.zerosIn_finite T₁ T₂

/-- Project RH implies every Zeta23 nontrivial zero lies on the critical line. -/
theorem projectRH_implies_zeta23_onLine (hRH : RiemannFormal.RH)
    {ρ : ℂ} (hρ : ProjectNontrivialZero ρ) : ρ.re = 1 / 2 :=
  Zeta23.RH_implies_on_line hRH hρ

/-- Zeta23's literature-form Weil explicit formula, specialized to the closed ζ seam. -/
theorem zeta23_weilExplicitFormula : Zeta23.EF.EF_lit Zeta23.zetaZeroConfig :=
  Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam

/-- Zeta23's Riemann–von Mangoldt package remains explicitly conditional on its Gamma facts. -/
theorem zeta23_riemannVonMangoldt (hΓ : Zeta23.GammaFacts) :
    Zeta23.RiemannVonMangoldt Zeta23.zetaZeroConfig :=
  Zeta23.RvM.riemannVonMangoldt hΓ

end RiemannFormal.Upstream
