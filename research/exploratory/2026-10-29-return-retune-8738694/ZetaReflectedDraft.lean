/- Exploratory corollary. No status is implied until its separate build log succeeds. -/
import Candidate.Main
set_option autoImplicit false

namespace CandidateZetaReflected

theorem right_ne_zero {s : ℂ} (hs : (4369347 / 5000000 : ℝ) < s.re) (h1 : s ≠ 1) :
    riemannZeta s ≠ 0 := by
  have h := Candidate.bound (q := 1) (1 : DirichletCharacter ℂ 1) hs (by
    intro hpole
    exact h1 hpole.2)
  simpa only [DirichletCharacter.LFunction_modOne_eq] using h

theorem left_ne_zero {s : ℂ} (hpos : 0 < s.re)
    (hs : s.re < (630653 / 5000000 : ℝ)) : riemannZeta s ≠ 0 := by
  have hn : ∀ n : ℕ, s ≠ -n := by
    intro n heq
    have h := congrArg Complex.re heq
    simp only [Complex.neg_re, Complex.natCast_re] at h
    have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    linarith
  have h1 : s ≠ 1 := by
    intro heq
    have h := congrArg Complex.re heq
    simp only [Complex.one_re] at h
    norm_num at hs
    linarith
  have hright : (4369347 / 5000000 : ℝ) < (1 - s).re := by
    simp only [Complex.sub_re, Complex.one_re]
    linarith
  have hr1 : 1 - s ≠ 1 := by
    intro heq
    have h := congrArg Complex.re heq
    simp only [Complex.sub_re, Complex.one_re] at h
    linarith
  have hzero := right_ne_zero hright hr1
  intro hζ
  apply hzero
  rw [riemannZeta_one_sub hn h1, hζ, mul_zero]

theorem zero_localization {s : ℂ} (hpos : 0 < s.re) (hupper : s.re < 1)
    (hζ : riemannZeta s = 0) :
    (630653 / 5000000 : ℝ) ≤ s.re ∧ s.re ≤ (4369347 / 5000000 : ℝ) := by
  constructor
  · by_contra h
    exact left_ne_zero hpos (lt_of_not_ge h) hζ
  · by_contra h
    have hs : (4369347 / 5000000 : ℝ) < s.re := lt_of_not_ge h
    have h1 : s ≠ 1 := by
      intro heq
      have h := congrArg Complex.re heq
      simp only [Complex.one_re] at h
      linarith
    exact right_ne_zero hs h1 hζ

#check left_ne_zero
#check zero_localization
#print axioms zero_localization
end CandidateZetaReflected
