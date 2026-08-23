import Mathlib.Analysis.Analytic.Constructions

namespace Comparator.MellinAPI

/-- Trusted Mathlib-only challenge statement for the abstract fixed Mellin consumer. Every analytic,
nonvanishing, identity, and singularity hypothesis is explicit. -/
def ChallengeStatement : Prop :=
  ∀ (main defect multiplier total : ℂ → ℂ) (s₀ : ℂ),
    AnalyticAt ℂ defect s₀ →
    AnalyticAt ℂ multiplier s₀ →
    multiplier s₀ ≠ 0 →
    total = (fun s => multiplier s * main s + defect s) →
    (¬AnalyticAt ℂ main s₀) →
    ¬AnalyticAt ℂ total s₀

end Comparator.MellinAPI
