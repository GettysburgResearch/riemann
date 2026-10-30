/- To be checked after the retuned Candidate.Main build is complete. -/
import Candidate.Main
set_option autoImplicit false
namespace CandidateZetaRetuned
 theorem zeta_ne_zero {s : ℂ} (hs : (4369347 / 5000000 : ℝ) < s.re) (h1 : s ≠ 1) :
    riemannZeta s ≠ 0 := by
  have h := Candidate.bound (q := 1) (1 : DirichletCharacter ℂ 1) hs (by
    intro hpole
    exact h1 hpole.2)
  simpa only [DirichletCharacter.LFunction_modOne_eq] using h
#check zeta_ne_zero
#print axioms zeta_ne_zero
end CandidateZetaRetuned
