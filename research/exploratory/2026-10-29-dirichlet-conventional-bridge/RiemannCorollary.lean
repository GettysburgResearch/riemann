import Candidate.Main

example {s : ℂ} (hs : (4369351 / 5000000 : ℝ) < s.re) (hne : s ≠ 1) :
    riemannZeta s ≠ 0 := by
  have hpole : ¬ ((1 : DirichletCharacter ℂ 1) = 1 ∧ s = 1) := by
    intro h
    exact hne h.2
  have h := Candidate.bound (q := 1) (1 : DirichletCharacter ℂ 1) hs hpole
  simpa only [DirichletCharacter.LFunction_modOne_eq] using h

#print axioms Candidate.bound
