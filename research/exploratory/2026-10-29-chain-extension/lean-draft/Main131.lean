/- Experimental endpoint assembly. This is UNCOMPILED and depends on the
   full source-qualified chain, new gates, four-source return, and floor patch. -/
import Candidate.ChainExtension.Step_130
import Candidate.ChainExtension.Step_131
import Candidate.ChainExtension.Wiring
import Submissions.arvi_density.Return.Endpoint

set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace Candidate.ChainExtension
noncomputable section
open OAI OAI.SevenEighths OAI.SevenEighths.HeckeFamily

/-- Candidate numerical Dirichlet conclusion; no elaboration is claimed. -/
theorem bound131 {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (43693463 / 50000000 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    DirichletCharacter.LFunction χ s ≠ 0 := by
  apply QRH.ArviDensity.Return.dirichlet_of_sources
    (fun hβ => QRH.ArviDensity.ChainF50.source_129 hβ)
    (fun hβ => QRH.ArviDensity.ChainF50.source_64 hβ)
    (fun hβ => QRH.ArviDensity.ChainExtension.source131
      QRH.ArviDensity.ChainExtension.hybridGatesM_Step_130
      QRH.ArviDensity.ChainExtension.hybridGatesM_Step_131 hβ)
    (fun hβ => QRH.ArviDensity.ChainF50.source_66 hβ) χ hs hpole

end
end Candidate.ChainExtension
#print axioms Candidate.ChainExtension.bound131
