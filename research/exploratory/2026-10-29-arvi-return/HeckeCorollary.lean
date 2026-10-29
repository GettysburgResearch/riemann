import Candidate.Main

/- Prepared source-level corollary; not compiled. The represented characters are
   the tracker's finite-order residue characters over CyclotomicField 3 ℚ. -/
namespace CandidateHecke
open OAI.SevenEighths
open OAI.SevenEighths.HeckeFamily

noncomputable section

theorem beta_le : HeckeZeroSupremum.beta ≤ (4369351 / 5000000 : ℝ) :=
  QRH.ArviDensity.Return.beta_le_theta_of_sources
    (fun h => QRH.ArviDensity.ChainF50.final_source h)
    (fun h => QRH.ArviDensity.ChainF50.source_64 h)

theorem finite_hecke_ne_zero (χ : Character) {s : ℂ}
    (hs : (4369351 / 5000000 : ℝ) < s.re)
    (hpole : s ≠ 1 ∨ χ.residue ≠ 1) : LFunction χ s ≠ 0 :=
  HeckeZeroSupremum.LFunction_ne_zero_of_beta_lt χ (lt_of_le_of_lt beta_le hs) hpole

end
end CandidateHecke

#check CandidateHecke.beta_le
#check CandidateHecke.finite_hecke_ne_zero
#print axioms CandidateHecke.finite_hecke_ne_zero
