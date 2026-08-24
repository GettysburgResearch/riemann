import RiemannFormal.Upstream.MathlibBridge
import RiemannFormal.Upstream.SourceLocks
import Zeta23.Statement.SeamClosed
import Zeta23.ZetaReflect
import Zeta23.WeilEF.Main
import Zeta23.RvM.Statement
import Mathlib.Tactic

open Complex

namespace RiemannFormal.Upstream

/-- Compatibility declaration retained for the trusted bootstrap axiom audit. The project and
Zeta23 both use Mathlib's canonical RH proposition; no new hypothesis is introduced. -/
theorem zeta23_bridge_preserves_RH : RiemannFormal.RH ↔ RiemannHypothesis := Iff.rfl

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

/-- At every point other than `1`, analytic and meromorphic zeta order agree under the canonical
`ENat → WithTop ℤ` map. -/
theorem projectRiemannZeta_meromorphicOrderAt_eq_analyticOrderAt
    {ρ : ℂ} (hρ1 : ρ ≠ 1) :
    meromorphicOrderAt riemannZeta ρ =
      (analyticOrderAt riemannZeta ρ).map (fun n : ℕ => (n : ℤ)) := by
  simpa using
    ((differentiableAt_riemannZeta hρ1).analyticAt.meromorphicOrderAt_eq)

/-- At a Zeta23 open-strip zero, the meromorphic order is exactly the finite natural
`zeroMult`, embedded in `WithTop ℤ`. -/
theorem projectRiemannZeta_meromorphicOrderAt_eq_zeroMultiplicity
    {ρ : ℂ} (hρ : ProjectNontrivialZero ρ) :
    meromorphicOrderAt riemannZeta ρ =
      ((ProjectZeroMultiplicity ρ : ℤ) : WithTop ℤ) := by
  have hρ1 : ρ ≠ 1 := hρ.not_trivial.2
  rw [projectRiemannZeta_meromorphicOrderAt_eq_analyticOrderAt hρ1]
  have hfinite : analyticOrderAt riemannZeta ρ ≠ ⊤ := by
    intro htop
    have hzero : ProjectZeroMultiplicity ρ = 0 := by
      change (analyticOrderAt riemannZeta ρ).toNat = 0
      rw [htop]
      simp
    have hone : 1 ≤ ProjectZeroMultiplicity ρ :=
      Zeta23.zetaSeam.one_le_mult ρ hρ
    rw [hzero] at hone
    omega
  obtain ⟨m, hm⟩ := ENat.ne_top_iff_exists.mp hfinite
  have hmult : ProjectZeroMultiplicity ρ = m := by
    change (analyticOrderAt riemannZeta ρ).toNat = m
    rw [← hm]
    simp
  rw [← hm]
  simp [hmult]

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
