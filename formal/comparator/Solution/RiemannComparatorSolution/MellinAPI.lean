import RiemannComparatorChallengeDeps.MellinAPI

namespace Comparator.MellinAPI

/-- Mathlib-only proof of the exact trusted challenge statement. -/
theorem fixedMellinConsumerSolution : ChallengeStatement := by
  intro main defect multiplier total s₀ hdefect hmultiplier hmultiplier_ne htotal hmain htotalAnalytic
  apply hmain
  have hsum : AnalyticAt ℂ (fun s => multiplier s * main s + defect s) s₀ := by
    simpa [htotal] using htotalAnalytic
  have hproduct : AnalyticAt ℂ (fun s => multiplier s * main s) s₀ := by
    apply (hsum.sub hdefect).congr
    filter_upwards with s
    simp
  exact (analyticAt_iff_analytic_mul hmultiplier hmultiplier_ne).mpr hproduct

#print axioms fixedMellinConsumerSolution

end Comparator.MellinAPI
