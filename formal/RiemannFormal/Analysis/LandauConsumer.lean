import RiemannFormal.Analysis.MellinAPI
import RiemannFormal.Analysis.SingularityTransfer

open Complex Filter MeasureTheory Set

namespace RiemannFormal.Analysis

/-- A concrete real abscissa package for a Mellin transform. Convergence is required strictly to
the right of `σc`, and failure on every real point strictly to its left. -/
def HasFiniteMellinAbscissa (f : ℝ → ℂ) (σc : ℝ) : Prop :=
  (∀ s : ℂ, σc < s.re → MellinConvergent f s) ∧
  (∀ σ : ℝ, σ < σc → ¬ MellinConvergent f (σ : ℂ))

/-- The detector is not almost everywhere zero on `[1, ∞)`. -/
def NotAEEqZeroOnOne (f : Detector) : Prop :=
  ¬∀ᵐ x : ℝ ∂(volume.restrict (Set.Ici 1)), f x = 0

/-- Exact missing library proposition: Landau's boundary-singularity theorem for nonnegative
Mellin densities. It is a `Prop`, not an axiom. Every theorem using it receives a proof term as an
explicit argument. -/
def MellinLandauBoundarySingularity : Prop :=
  ∀ (f : Detector) (F : ℂ → ℂ) (σc : ℝ),
    LocallyIntegrableOn (fun x : ℝ => (f x : ℂ)) (Set.Ioi 0) →
    (∀ x : ℝ, 1 ≤ x → 0 ≤ f x) →
    NotAEEqZeroOnOne f →
    HasFiniteMellinAbscissa (fun x : ℝ => (f x : ℂ)) σc →
    (∀ s : ℂ, σc < s.re → F s = mellin (fun x : ℝ => (f x : ℂ)) s) →
    NonremovableAt F (σc : ℂ)

/-- Data required to invoke the exact nonnegative-density Landau proposition. -/
structure NonnegativeMellinData (f : Detector) (F : ℂ → ℂ) (σc : ℝ) : Prop where
  locallyIntegrable : LocallyIntegrableOn (fun x : ℝ => (f x : ℂ)) (Set.Ioi 0)
  nonnegative : ∀ x : ℝ, 1 ≤ x → 0 ≤ f x
  nonzeroAE : NotAEEqZeroOnOne f
  finiteAbscissa : HasFiniteMellinAbscissa (fun x : ℝ => (f x : ℂ)) σc
  agreesRight : ∀ s : ℂ, σc < s.re → F s = mellin (fun x : ℝ => (f x : ℂ)) s

/-- Strongest proof-complete eventual/nonnegative Landau result available in this pass: the exact
missing theorem is an explicit argument and the remaining assembly is verified. -/
theorem nonnegative_landau_boundary
    (hLandau : MellinLandauBoundarySingularity)
    {f : Detector} {F : ℂ → ℂ} {σc : ℝ}
    (hdata : NonnegativeMellinData f F σc) :
    NonremovableAt F (σc : ℂ) :=
  hLandau f F σc hdata.locallyIntegrable hdata.nonnegative hdata.nonzeroAE
    hdata.finiteAbscissa hdata.agreesRight

/-- Logarithmic negative mass up to `X`. -/
def logNegativeMass (f : Detector) (X : ℝ) : ℝ :=
  ∫ x in Set.Icc (1 : ℝ) X, negativePart f x / x

/-- The reviewed subpower logarithmic negative-mass hypothesis, with all constants and thresholds
explicit. -/
def SubpowerLogNegativeMass (f : Detector) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ C X₀ : ℝ, 0 ≤ C ∧ 1 ≤ X₀ ∧
    ∀ X : ℝ, X₀ ≤ X → logNegativeMass f X ≤ C * X ^ ε

/-- Exact missing analytic proposition: subpower logarithmic negative mass produces a holomorphic
negative-part Mellin transform throughout `re s > 0`. This is deliberately a proposition rather
than a custom axiom. -/
def SubpowerNegativeMassHolomorphy : Prop :=
  ∀ (f : Detector),
    LocallyIntegrableOn (fun x : ℝ => ((negativePart f x : ℝ) : ℂ)) (Set.Ioi 0) →
    SubpowerLogNegativeMass f →
    ∀ s : ℂ, 0 < s.re →
      AnalyticAt ℂ (mellin (fun x : ℝ => ((negativePart f x : ℝ) : ℂ))) s

/-- The subpower-negative-mass correction is holomorphic when the exact missing analytic
proposition is supplied. -/
theorem subpower_negative_mass_holomorphic
    (hSubpower : SubpowerNegativeMassHolomorphy)
    {f : Detector}
    (hlocal : LocallyIntegrableOn
      (fun x : ℝ => ((negativePart f x : ℝ) : ℂ)) (Set.Ioi 0))
    (hmass : SubpowerLogNegativeMass f)
    {s : ℂ} (hs : 0 < s.re) :
    AnalyticAt ℂ (mellin (fun x : ℝ => ((negativePart f x : ℝ) : ℂ))) s :=
  hSubpower f hlocal hmass s hs

/-- Once negative-part holomorphy is available, it is a fixed holomorphic defect and cannot cancel
a nonremovable singularity. -/
theorem subpower_negative_mass_singularity_transfer
    {main : ℂ → ℂ} {f : Detector} {s₀ : ℂ}
    (hnegative : AnalyticAt ℂ
      (mellin (fun x : ℝ => ((negativePart f x : ℝ) : ℂ))) s₀)
    (hmain : NonremovableAt main s₀) :
    NonremovableAt
      (fun s => main s + mellin (fun x : ℝ => ((negativePart f x : ℝ) : ℂ)) s) s₀ :=
  fixed_holomorphic_defect_transfer hnegative hmain

end RiemannFormal.Analysis
