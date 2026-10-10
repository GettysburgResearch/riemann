/-
Exploratory (qrh-2026-10 wave). Not part of the imported OpenAI development.

For a primitive nontrivial Dirichlet character `χ`, the imported 7/8 Dirichlet theorem plus
Mathlib's functional equation puts every nontrivial zero of `L(s, χ)` in the closed strip
`1/8 ≤ Re s ≤ 7/8`. "Nontrivial" means that the Archimedean factor `gammaFactor χ s` (Mathlib's
`Gammaℝ s` or `Gammaℝ (s + 1)`) does not vanish; `gammaFactor_eq_zero_iff` spells out the
trivial zeros.

The functional equation is used for `χ⁻¹`, so no non-vanishing of the root number is needed.

This is NOT GRH. GRH asks for `Re s = 1/2`; this file only reflects the half-plane `Re s > 7/8`.
-/
import OAI.NumberTheory.DirichletL.Nonvanishing

namespace QRHWave

open Complex

variable {N : ℕ} [NeZero N]

omit [NeZero N] in
/-- The trivial zeros: `gammaFactor χ s = 0` exactly at `s = 0, -2, -4, …` for even `χ` and at
`s = -1, -3, -5, …` for odd `χ`. -/
theorem gammaFactor_eq_zero_iff (χ : DirichletCharacter ℂ N) (s : ℂ) :
    DirichletCharacter.gammaFactor χ s = 0 ↔
      (χ.Even ∧ ∃ n : ℕ, s = -(2 * n)) ∨ (¬ χ.Even ∧ ∃ n : ℕ, s = -(2 * n) - 1) := by
  classical
  unfold DirichletCharacter.gammaFactor
  split_ifs with h
  · simp [h, Gammaℝ_eq_zero_iff]
  · simp only [h, Gammaℝ_eq_zero_iff, false_and, not_false_eq_true, true_and, false_or]
    constructor
    · rintro ⟨n, hn⟩
      exact ⟨n, by linear_combination hn⟩
    · rintro ⟨n, hn⟩
      exact ⟨n, by linear_combination hn⟩

/-- Reflected half-plane: for primitive `χ ≠ 1`, a zero of `L(s, χ)` with `Re s < 1/8` is a zero
of the Archimedean factor, i.e. a trivial zero. -/
theorem LFunction_zero_re_lt_one_eighth {χ : DirichletCharacter ℂ N}
    (hχ : χ.IsPrimitive) (hχ1 : χ ≠ 1) {s : ℂ}
    (hs : DirichletCharacter.LFunction χ s = 0) (hlo : s.re < 1 / 8) :
    DirichletCharacter.gammaFactor χ s = 0 := by
  by_contra hG
  have hN : N ≠ 1 := fun h => hχ1 (DirichletCharacter.level_one' χ h)
  -- `Λ(χ, s) = 0`.
  have hΛ : DirichletCharacter.completedLFunction χ s = 0 := by
    have h := DirichletCharacter.LFunction_eq_completed_div_gammaFactor χ s (Or.inr hN)
    rw [hs, eq_comm, div_eq_zero_iff] at h
    exact h.resolve_right hG
  -- Functional equation for the (primitive) inverse character at `s`.
  have hprim : (χ⁻¹).IsPrimitive := by
    rw [DirichletCharacter.isPrimitive_def, DirichletCharacter.conductor_inv]
    exact hχ
  have hfe := DirichletCharacter.IsPrimitive.completedLFunction_one_sub hprim s
  rw [inv_inv, hΛ, mul_zero] at hfe
  -- Hence `L(χ⁻¹, 1 - s) = 0` with `Re (1 - s) > 7/8`, contradicting the 7/8 theorem.
  have hL : DirichletCharacter.LFunction χ⁻¹ (1 - s) = 0 := by
    rw [DirichletCharacter.LFunction_eq_completed_div_gammaFactor χ⁻¹ (1 - s) (Or.inr hN), hfe,
      zero_div]
  have hre : (7 / 8 : ℝ) < (1 - s).re := by
    simp
    linarith
  have hpole : ¬ (χ⁻¹ = 1 ∧ (1 - s) = 1) := by
    rintro ⟨h1, -⟩
    exact hχ1 (inv_eq_one.mp h1)
  exact OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re χ⁻¹ hre hpole hL

/-- Quasi-GRH strip: for primitive `χ ≠ 1`, every zero of `L(s, χ)` that is not a zero of the
Archimedean factor has `1/8 ≤ Re s ≤ 7/8`. -/
theorem LFunction_quasi_critical_strip {χ : DirichletCharacter ℂ N}
    (hχ : χ.IsPrimitive) (hχ1 : χ ≠ 1) {s : ℂ}
    (hs : DirichletCharacter.LFunction χ s = 0)
    (hntriv : DirichletCharacter.gammaFactor χ s ≠ 0) :
    1 / 8 ≤ s.re ∧ s.re ≤ 7 / 8 := by
  refine ⟨?_, ?_⟩
  · by_contra hlo
    exact hntriv (LFunction_zero_re_lt_one_eighth hχ hχ1 hs (not_le.mp hlo))
  · by_contra hhi
    exact OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re χ (not_le.mp hhi)
      (fun h => hχ1 h.1) hs

end QRHWave
