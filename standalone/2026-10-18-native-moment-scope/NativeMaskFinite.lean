module

public import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
public import Mathlib.Basic.Real.Basic
public import Mathlib.Tactic

@[expose] public section

/-!
# Finite algebra underlying the native Euler-mask average

This file formalizes finite double counting, its positive weighted bound,
finite moment transfer, and the cofinal fixed-order quantifier adapter.
It does NOT formalize the infinite Euler
product, Hecke source, Gaussian Mellin transform, an analytic bound, or RH.
The analytic and arithmetic hypotheses remain outside these finite lemmas.
-/

namespace NativeMaskFinite

open scoped BigOperators

variable {α β : Type*}

/-- The finite `f = 1 * g` summation identity, with the divisibility
relation abstracted as `R`. Every pair is retained, including equality. -/
theorem divisor_double_count
    (B : Finset β) (D : Finset α) (R : α → β → Prop)
    [∀ d b, Decidable (R d b)]
    (f : β → ℝ) (g : α → ℝ)
    (hf : ∀ b ∈ B, f b = ∑ d ∈ D, if R d b then g d else 0) :
    ∑ b ∈ B, f b = ∑ d ∈ D, g d * ((B.filter (R d)).card : ℝ) := by
  calc
    ∑ b ∈ B, f b = ∑ b ∈ B, ∑ d ∈ D, if R d b then g d else 0 :=
      Finset.sum_congr rfl hf
    _ = ∑ d ∈ D, ∑ b ∈ B, if R d b then g d else 0 := Finset.sum_comm
    _ = ∑ d ∈ D, g d * ((B.filter (R d)).card : ℝ) := by
      apply Finset.sum_congr rfl
      intro d hd
      simp [← Finset.sum_filter, mul_comm]

/-- A positive divisor expansion plus a counting bound gives the exact
finite precursor of the linear average-mask estimate in PROOF.md §3. -/
theorem average_mask_bound
    (B : Finset β) (D : Finset α) (R : α → β → Prop)
    [∀ d b, Decidable (R d b)]
    (f : β → ℝ) (g q : α → ℝ) (C X : ℝ)
    (hf : ∀ b ∈ B, f b = ∑ d ∈ D, if R d b then g d else 0)
    (hg : ∀ d ∈ D, 0 ≤ g d)
    (hcount : ∀ d ∈ D, ((B.filter (R d)).card : ℝ) ≤ C * X / q d) :
    ∑ b ∈ B, f b ≤ C * X * ∑ d ∈ D, g d / q d := by
  rw [divisor_double_count B D R f g hf]
  calc
    ∑ d ∈ D, g d * ((B.filter (R d)).card : ℝ)
        ≤ ∑ d ∈ D, g d * (C * X / q d) := by
      apply Finset.sum_le_sum
      intro d hd
      exact mul_le_mul_of_nonneg_left (hcount d hd) (hg d hd)
    _ = C * X * ∑ d ∈ D, g d / q d := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro d hd
      ring

/-- A literal pointwise transfer gives the corresponding complete finite
even moment. The premise is an input; this lemma does not prove it for a
native arithmetic row. -/
theorem moment_transfer
    (B : Finset β) (a mass : β → ℝ) (K : ℝ) (k : ℕ)
    (hbound : ∀ b ∈ B, |a b| ≤ K * mass b) :
    ∑ b ∈ B, |a b| ^ (2*k) ≤ K ^ (2*k) * ∑ b ∈ B, mass b ^ (2*k) := by
  calc
    ∑ b ∈ B, |a b| ^ (2*k) ≤ ∑ b ∈ B, (K * mass b) ^ (2*k) := by
      apply Finset.sum_le_sum
      intro b hb
      exact pow_le_pow_left₀ (abs_nonneg (a b)) (hbound b hb) (2*k)
    _ = K ^ (2*k) * ∑ b ∈ B, mass b ^ (2*k) := by
      simp only [mul_pow, Finset.mul_sum]

/-- Only an unbounded subsequence of FIXED orders is needed to make the
family-height and sublinear-excess exponent arbitrarily small. -/
theorem cofinal_exponent
    (K : Set ℕ) (loss : ℕ → ℝ) (h : ℝ)
    (hK : ∀ N : ℕ, ∃ k ∈ K, N ≤ k)
    (hloss : ∀ η : ℝ, 0 < η → ∃ N : ℕ,
      ∀ k ∈ K, N ≤ k → loss k / (k : ℝ) < η) :
    ∀ δ : ℝ, 0 < δ → ∃ k ∈ K, 0 < k ∧ (h + loss k) / (2*(k : ℝ)) < δ := by
  intro δ hδ
  obtain ⟨N, hN⟩ := hloss δ hδ
  obtain ⟨M, hM⟩ := exists_nat_gt (h/δ)
  obtain ⟨k, hkK, hk⟩ := hK (max N (M+1))
  have hNk : N ≤ k := le_trans (le_max_left N (M+1)) hk
  have hMk : M+1 ≤ k := le_trans (le_max_right N (M+1)) hk
  have hkposNat : 0 < k := lt_of_lt_of_le (Nat.zero_lt_succ M) hMk
  have hkpos : (0 : ℝ) < k := by exact_mod_cast hkposNat
  have hMkReal : (M : ℝ) < k := by
    exact_mod_cast lt_of_lt_of_le (Nat.lt_succ_self M) hMk
  have hh : h/δ < (k : ℝ) := lt_trans hM hMkReal
  have hhk : h/(k : ℝ) < δ := by
    apply (div_lt_iff₀ hkpos).2
    have hh' := (div_lt_iff₀ hδ).1 hh
    nlinarith
  have heloss : loss k/(k : ℝ) < δ := hN k hkK hNk
  have hexp : (h + loss k)/(2*(k : ℝ)) =
      (h/(k : ℝ) + loss k/(k : ℝ))/2 := by
    field_simp
  refine ⟨k, hkK, hkposNat, ?_⟩
  rw [hexp]
  linarith

/-- The property P can include an arbitrary constant and threshold after
each fixed order is chosen. No growing-order uniform constant is assumed.
This is a logical adapter, not a proved estimate for the native source. -/
theorem cofinal_fixed_order_extraction
    (K : Set ℕ) (loss : ℕ → ℝ) (h : ℝ) (P : ℝ → Prop)
    (hK : ∀ N : ℕ, ∃ k ∈ K, N ≤ k)
    (hloss : ∀ η : ℝ, 0 < η → ∃ N : ℕ,
      ∀ k ∈ K, N ≤ k → loss k / (k : ℝ) < η)
    (hmono : ∀ a b : ℝ, a ≤ b → P a → P b)
    (hstep : ∀ k ∈ K, 0 < k → ∀ η : ℝ, 0 < η →
      P (1/2 + (h + loss k)/(2*(k : ℝ)) + η)) :
    ∀ δ : ℝ, 0 < δ → P (1/2 + δ) := by
  intro δ hδ
  have hhalf : 0 < δ/2 := by linarith
  obtain ⟨k, hkK, hkpos, hexp⟩ := cofinal_exponent K loss h hK hloss (δ/2) hhalf
  exact hmono _ _ (by linarith) (hstep k hkK hkpos (δ/2) hhalf)

#print axioms divisor_double_count
#print axioms average_mask_bound
#print axioms moment_transfer
#print axioms cofinal_exponent
#print axioms cofinal_fixed_order_extraction

end NativeMaskFinite
