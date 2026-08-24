import RiemannFormal.Analysis.MellinAPI
import RiemannFormal.Analysis.SingularityTransfer
import Mathlib.Tactic

open Complex Filter MeasureTheory Set

namespace RiemannFormal.Analysis

/-- A real finite abscissa package for the reviewed tail transform. Convergence is required at
every complex point strictly to the right of `σc`, and failure is required at every real point
strictly to its left. -/
def HasFiniteTailMellinAbscissa (f : Detector) (σc : ℝ) : Prop :=
  (∀ s : ℂ, σc < s.re →
    TailMellinConvergent (fun x => (f x : ℂ)) s) ∧
  (∀ σ : ℝ, σ < σc →
    ¬TailMellinConvergent (fun x => (f x : ℂ)) (σ : ℂ))

/-- The tail density is not almost everywhere zero on `[1, ∞)`. -/
def NotAEEqZeroOnTail (f : Detector) : Prop :=
  ¬∀ᵐ x : ℝ ∂(volume.restrict (Set.Ici (1 : ℝ))), f x = 0

/-- Exact missing library proposition: Landau's boundary-singularity theorem for the reviewed
tail transform. The transformed function, its support, eventual sign, finite abscissa, initial
convergence half-plane, and continuation identity are all quantified together. This is a `Prop`,
not an axiom; every theorem using it receives a proof term explicitly. -/
def MellinLandauBoundarySingularity : Prop :=
  ∀ (f : Detector) (F : ℂ → ℂ) (σc σinitial : ℝ),
    σc < σinitial →
    LocallyIntegrableOn (fun x : ℝ => (f x : ℂ)) (Set.Ici (1 : ℝ)) →
    EventuallyNonnegative f →
    NotAEEqZeroOnTail f →
    HasFiniteTailMellinAbscissa f σc →
    (∀ s : ℂ, σinitial < s.re →
      TailMellinConvergent (fun x : ℝ => (f x : ℂ)) s) →
    (∀ s : ℂ, σc < s.re →
      F s = tailMellin (fun x : ℝ => (f x : ℂ)) s) →
    NonremovableAt F (σc : ℂ)

/-- Analytic and growth data that do not themselves assert the tail-transform identity. -/
structure NonnegativeTailMellinCore
    (f : Detector) (F : ℂ → ℂ) (σc : ℝ) : Prop where
  locallyIntegrable :
    LocallyIntegrableOn (fun x : ℝ => (f x : ℂ)) (Set.Ici (1 : ℝ))
  eventuallyNonnegative : EventuallyNonnegative f
  nonzeroAE : NotAEEqZeroOnTail f
  finiteAbscissa : HasFiniteTailMellinAbscissa f σc
  initialAbscissa : ℝ
  boundary_lt_initial : σc < initialAbscissa
  initialConvergence : ∀ s : ℂ, initialAbscissa < s.re →
    TailMellinConvergent (fun x : ℝ => (f x : ℂ)) s
  analyticRightOfAbscissa : ∀ s : ℂ, σc < s.re → AnalyticAt ℂ F s
  analyticPositiveReal : ∀ σ : ℝ, 0 < σ → AnalyticAt ℂ F (σ : ℂ)

/-- Complete data required to invoke the exact tail-Landau proposition. -/
structure NonnegativeTailMellinData
    (f : Detector) (F : ℂ → ℂ) (σc : ℝ)
    extends NonnegativeTailMellinCore f F σc : Prop where
  agreesRight : ∀ s : ℂ, σc < s.re →
    F s = tailMellin (fun x : ℝ => (f x : ℂ)) s

/-- Strongest proof-complete tail-Landau result available in this pass: the exact missing theorem
is an explicit argument and the remaining assembly is verified. -/
theorem nonnegative_landau_boundary
    (hLandau : MellinLandauBoundarySingularity)
    {f : Detector} {F : ℂ → ℂ} {σc : ℝ}
    (hdata : NonnegativeTailMellinData f F σc) :
    NonremovableAt F (σc : ℂ) :=
  hLandau f F σc hdata.initialAbscissa hdata.boundary_lt_initial
    hdata.locallyIntegrable hdata.eventuallyNonnegative hdata.nonzeroAE
    hdata.finiteAbscissa hdata.initialConvergence hdata.agreesRight

/-- If the continuation is analytic at every positive real point, tail Landau forces its finite
abscissa to be nonpositive. -/
theorem landau_abscissa_nonpositive
    (hLandau : MellinLandauBoundarySingularity)
    {f : Detector} {F : ℂ → ℂ} {σc : ℝ}
    (hdata : NonnegativeTailMellinData f F σc) :
    σc ≤ 0 := by
  by_contra hnot
  have hpos : 0 < σc := lt_of_not_ge hnot
  exact (nonnegative_landau_boundary hLandau hdata)
    (hdata.analyticPositiveReal σc hpos)

/-- Consequently the defining nonnegative tail continuation is analytic throughout `Re(s) > 0`. -/
theorem nonnegative_tail_continuation_analytic
    (hLandau : MellinLandauBoundarySingularity)
    {f : Detector} {F : ℂ → ℂ} {σc : ℝ}
    (hdata : NonnegativeTailMellinData f F σc)
    {s : ℂ} (hs : 0 < s.re) :
    AnalyticAt ℂ F s :=
  hdata.analyticRightOfAbscissa s
    (lt_of_le_of_lt (landau_abscissa_nonpositive hLandau hdata) hs)

/-- Logarithmic negative mass up to `X`, exactly
`∫_[1,X] f_-(x) dx/x`. -/
noncomputable def logNegativeMass (f : Detector) (X : ℝ) : ℝ :=
  ∫ x in Set.Icc (1 : ℝ) X, negativePart f x / x

/-- The reviewed subpower logarithmic negative-mass hypothesis, with every exponent, constant,
and threshold explicit. -/
def SubpowerLogNegativeMass (f : Detector) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ C X₀ : ℝ, 0 ≤ C ∧ 1 ≤ X₀ ∧
    ∀ X : ℝ, X₀ ≤ X → logNegativeMass f X ≤ C * X ^ ε

/-- Exact missing analytic proposition: subpower logarithmic negative mass on `[1,∞)` produces a
holomorphic negative-part *tail* transform throughout `Re(s) > 0`. Local integrability and an
initial absolute-convergence half-plane are explicit. This is a proposition, never an axiom. -/
def SubpowerNegativeMassHolomorphy : Prop :=
  ∀ (f : Detector) (σinitial : ℝ),
    LocallyIntegrableOn
      (fun x : ℝ => (negativePart f x : ℂ)) (Set.Ici (1 : ℝ)) →
    (∀ s : ℂ, σinitial < s.re →
      TailMellinConvergent (fun x : ℝ => (negativePart f x : ℂ)) s) →
    SubpowerLogNegativeMass f →
    ∀ s : ℂ, 0 < s.re →
      AnalyticAt ℂ
        (tailMellin (fun x : ℝ => (negativePart f x : ℂ))) s

/-- The negative-part tail transform is holomorphic when the exact missing proposition is
supplied. -/
theorem subpower_negative_mass_holomorphic
    (hSubpower : SubpowerNegativeMassHolomorphy)
    {f : Detector} {σinitial : ℝ}
    (hlocal : LocallyIntegrableOn
      (fun x : ℝ => (negativePart f x : ℂ)) (Set.Ici (1 : ℝ)))
    (hinitial : ∀ s : ℂ, σinitial < s.re →
      TailMellinConvergent (fun x : ℝ => (negativePart f x : ℂ)) s)
    (hmass : SubpowerLogNegativeMass f)
    {s : ℂ} (hs : 0 < s.re) :
    AnalyticAt ℂ
      (tailMellin (fun x : ℝ => (negativePart f x : ℂ))) s :=
  hSubpower f σinitial hlocal hinitial hmass s hs

/-- Once negative-part tail holomorphy is available, it is a fixed holomorphic defect and cannot
cancel a nonremovable singularity. -/
theorem subpower_negative_mass_singularity_transfer
    {main : ℂ → ℂ} {f : Detector} {s₀ : ℂ}
    (hnegative : AnalyticAt ℂ
      (tailMellin (fun x : ℝ => (negativePart f x : ℂ))) s₀)
    (hmain : NonremovableAt main s₀) :
    NonremovableAt
      (fun s => main s +
        tailMellin (fun x : ℝ => (negativePart f x : ℂ)) s) s₀ :=
  fixed_holomorphic_defect_transfer hnegative hmain

end RiemannFormal.Analysis
