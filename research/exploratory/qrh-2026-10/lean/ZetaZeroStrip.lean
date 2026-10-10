/-
Exploratory (qrh-2026-10 wave). Not part of the imported OpenAI development.

The imported 7/8 theorem plus Mathlib's functional equation puts every nontrivial zero of
`riemannZeta` in the closed strip `1/8 ≤ Re s ≤ 7/8`. The statement is written in the shape of
Mathlib's `RiemannHypothesis` (same hypotheses: `ζ s = 0`, `s` not a trivial zero, `s ≠ 1`).

This is NOT RH. RH asks for `Re s = 1/2`; this file only reflects the half-plane `Re s > 7/8`
through `s ↦ 1 - s`.
-/
import OAI.NumberTheory.DirichletL.Nonvanishing

namespace QRHWave

open Complex

/-- The reflected half-plane: `ζ` has no zeros with `Re s < 1/8` other than the trivial zeros. -/
theorem riemannZeta_zero_re_lt_one_eighth {s : ℂ} (hs : riemannZeta s = 0)
    (hlo : s.re < 1 / 8) : ∃ n : ℕ, s = -2 * (n + 1) := by
  -- `s ≠ 0` because `ζ 0 = -1/2`.
  have hs0 : s ≠ 0 := by
    rintro rfl
    rw [riemannZeta_zero] at hs
    norm_num at hs
  -- Hypotheses of the functional equation at `1 - s`.
  have hn : ∀ n : ℕ, (1 - s) ≠ -n := by
    intro n h
    have hre := congrArg Complex.re h
    simp at hre
    have : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    linarith
  have h1 : (1 - s) ≠ 1 := by
    intro h
    apply hs0
    linear_combination -h
  have hfe := riemannZeta_one_sub hn h1
  rw [sub_sub_cancel, hs] at hfe
  -- Every factor except the cosine is nonzero.
  have hz : riemannZeta (1 - s) ≠ 0 := by
    apply OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
    simp
    linarith
  have hG : Gamma (1 - s) ≠ 0 := by
    apply Gamma_ne_zero_of_re_pos
    simp
    linarith
  have h2pi : (2 * (π : ℂ)) ≠ 0 := by
    have : (π : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
    exact mul_ne_zero two_ne_zero this
  have hpow : (2 * (π : ℂ)) ^ (-(1 - s)) ≠ 0 := by
    rw [cpow_def_of_ne_zero h2pi]
    exact exp_ne_zero _
  have hcos : cos (π * (1 - s) / 2) = 0 := by
    by_contra hc
    have : (2 : ℂ) * (2 * π) ^ (-(1 - s)) * Gamma (1 - s) * cos (π * (1 - s) / 2) *
        riemannZeta (1 - s) ≠ 0 := by
      apply mul_ne_zero (mul_ne_zero (mul_ne_zero (mul_ne_zero two_ne_zero hpow) hG) hc) hz
    exact this hfe.symm
  -- `cos (π (1 - s) / 2) = 0` forces `1 - s = 2k + 1`, so `s = -2k` with `k ≥ 1`.
  obtain ⟨k, hk⟩ := cos_eq_zero_iff.mp hcos
  have hpi : (π : ℂ) ≠ 0 := ofReal_ne_zero.mpr Real.pi_ne_zero
  have hsk : s = -2 * (k : ℂ) := by
    have : (π : ℂ) * (1 - s) = π * (2 * k + 1) := by linear_combination 2 * hk
    have := mul_left_cancel₀ hpi this
    linear_combination -this
  have hk1 : 1 ≤ k := by
    by_contra hk0
    push_neg at hk0
    have hre := congrArg Complex.re hsk
    simp at hre
    have hk' : (k : ℝ) ≤ 0 := by exact_mod_cast Int.lt_add_one_iff.mp hk0
    -- `Re s = -2k ≥ 0`, and `s = 0` is excluded, so `k ≤ -1` gives `Re s ≥ 2 > 1/8`.
    rcases lt_or_eq_of_le hk' with hlt | heq
    · have : (k : ℝ) ≤ -1 := by exact_mod_cast Int.le_sub_one_iff.mpr (by exact_mod_cast hlt)
      linarith
    · apply hs0
      rw [hsk]
      have : (k : ℂ) = 0 := by exact_mod_cast (by exact_mod_cast heq : (k : ℝ) = 0)
      rw [this]
      ring
  refine ⟨(k - 1).toNat, ?_⟩
  have : ((k - 1).toNat : ℤ) = k - 1 := Int.toNat_of_nonneg (by linarith)
  have hc : (((k - 1).toNat : ℕ) : ℂ) = (k : ℂ) - 1 := by
    have := congrArg (fun z : ℤ => (z : ℂ)) this
    simpa using this
  rw [hc, hsk]
  ring

/-- Quasi-critical strip: every nontrivial zero `s ≠ 1` of `ζ` has `1/8 ≤ Re s ≤ 7/8`.
Same hypotheses as Mathlib's `RiemannHypothesis`; the conclusion is the strip, not `Re s = 1/2`. -/
theorem quasi_critical_strip :
    ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1),
      1 / 8 ≤ s.re ∧ s.re ≤ 7 / 8 := by
  intro s hs hntriv _
  refine ⟨?_, ?_⟩
  · by_contra hlo
    push_neg at hlo
    exact hntriv (riemannZeta_zero_re_lt_one_eighth hs hlo)
  · by_contra hhi
    push_neg at hhi
    exact OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re hhi hs

end QRHWave
