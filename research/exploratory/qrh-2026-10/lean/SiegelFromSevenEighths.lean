/-
Exploratory (qrh-2026-10 wave). Not part of the imported OpenAI development.

The two statements of `ComparatorChallenges/SiegelZeros.lean` (the Oct 1 Landau-Siegel
challenge), derived from the 7/8 Dirichlet theorem of the imported development
(`OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`), with the explicit
constant `c = log 3 / 8`. Primitivity and reality of `χ` are not used.

This file proves nothing about RH. It shows that the Siegel challenge statement is a short
corollary of the 7/8 zero-free half-plane, so the 7/8 theorem's correctness and this
corollary's correctness are separate questions from the Oct 1 paper's own proof.
-/
import OAI.NumberTheory.DirichletL.Nonvanishing

namespace OAI

namespace SiegelZeros
namespace WeightedTorusJets

/-- A real zero `β ∈ (0, 1)` of any Dirichlet `L`-function satisfies `β ≤ 7/8`. -/
theorem real_zero_le_seven_eighths {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q)
    {β : ℝ} (hβ1 : β < 1) (hzero : χ.LFunction (β : ℂ) = 0) : β ≤ 7 / 8 := by
  by_contra h
  push_neg at h
  have hre : (7 / 8 : ℝ) < (β : ℂ).re := by simpa using h
  have hpole : ¬ (χ = 1 ∧ (β : ℂ) = 1) := by
    rintro ⟨-, h1⟩
    have : β = 1 := by exact_mod_cast h1
    linarith
  exact OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re χ hre hpole hzero

theorem gap_of_real_zero {q : ℕ} [NeZero q] (hq : 3 ≤ q) (χ : DirichletCharacter ℂ q)
    {β : ℝ} (hβ1 : β < 1) (hzero : χ.LFunction (β : ℂ) = 0) :
    Real.log 3 / 8 ≤ (1 - β) * Real.log (q : ℝ) := by
  have hβ := real_zero_le_seven_eighths χ hβ1 hzero
  have hlog3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  have hlogq : Real.log 3 ≤ Real.log (q : ℝ) :=
    Real.log_le_log (by norm_num) (by exact_mod_cast hq)
  calc Real.log 3 / 8 ≤ (1 / 8) * Real.log (q : ℝ) := by linarith
    _ ≤ (1 - β) * Real.log (q : ℝ) :=
        mul_le_mul_of_nonneg_right (by linarith) (by linarith)

theorem exists_absolute_real_zero_gap :
    ∃ c : ℝ, 0 < c ∧
      ∀ (q : ℕ) [NeZero q], 3 ≤ q →
      ∀ χ : DirichletCharacter ℂ q,
        χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) →
        ∀ β : ℝ, 0 < β → β < 1 → χ.LFunction (β : ℂ) = 0 →
          c ≤ (1 - β) * Real.log (q : ℝ) := by
  refine ⟨Real.log 3 / 8, div_pos (Real.log_pos (by norm_num)) (by norm_num), ?_⟩
  intro q _ hq χ _ _ _ β _ hβ1 hzero
  exact gap_of_real_zero hq χ hβ1 hzero

theorem dirichletRealZeroBound_proof :
    ∃ c : ℝ, 0 < c ∧ ∀ (q : ℕ) [NeZero q], 3 ≤ q →
      ∀ χ : DirichletCharacter ℂ q,
        χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) →
        ∀ β : ℝ,
          (0 < β ∧ β < 1 ∧ DirichletCharacter.LFunction χ (β : ℂ) = 0) →
            c ≤ (1 - β) * Real.log (q : ℝ) := by
  refine ⟨Real.log 3 / 8, div_pos (Real.log_pos (by norm_num)) (by norm_num), ?_⟩
  intro q _ hq χ _ _ _ β ⟨_, hβ1, hzero⟩
  exact gap_of_real_zero hq χ hβ1 hzero

end WeightedTorusJets
end SiegelZeros

end OAI
