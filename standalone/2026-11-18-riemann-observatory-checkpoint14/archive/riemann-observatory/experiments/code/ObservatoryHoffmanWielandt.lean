-- A scoped finite perturbation lemma, importing the already locally built rank-trace cone.
-- This is not a build of the full zeta theorem or a formal weak-convergence proof.
import Zeta23.LinAlg.RankTrace
noncomputable section
open Matrix Finset RHLinalg
namespace ObservatoryFormal
variable {𝕜 : Type*} [RCLike 𝕜]
variable {n : Type*} [Fintype n] [DecidableEq n]
theorem hoffmanWielandtSquared {A B : Matrix n n 𝕜}
    (hA : A.IsHermitian) (hB : B.IsHermitian) :
    (∑ i, (hA.eigenvalues₀ i - hB.eigenvalues₀ i)^2) ≤ frobSq (A-B) := by
  have hvn := vonNeumann_trace_ineq hA hB
  have hA2 : frobSq A = ∑ i, (hA.eigenvalues₀ i)^2 := by
    rw [frobSq_hermitian_eq_sum_sq_eigenvalues hA]
    exact sum_eigenvalues_reindex hA (·^2)
  have hB2 : frobSq B = ∑ i, (hB.eigenvalues₀ i)^2 := by
    rw [frobSq_hermitian_eq_sum_sq_eigenvalues hB]
    exact sum_eigenvalues_reindex hB (·^2)
  have hneg : frobSq (-B) = frobSq B := by
    simp [frobSq]
  have hexp : frobSq (A-B) = frobSq A - 2 * RCLike.re (A*B).trace + frobSq B := by
    rw [sub_eq_add_neg, frobSq_add_hermitian hA hB.neg, hneg]
    simp [mul_neg, trace_neg]
    ring
  have hs : (∑ i, (hA.eigenvalues₀ i - hB.eigenvalues₀ i)^2) =
      (∑ i, (hA.eigenvalues₀ i)^2) - 2*(∑ i, hA.eigenvalues₀ i*hB.eigenvalues₀ i)
        + (∑ i, (hB.eigenvalues₀ i)^2) := by
    simp_rw [sub_sq, mul_assoc]
    rw [sum_add_distrib, sum_sub_distrib, ← mul_sum]
  rw [hs, hexp, hA2, hB2]
  linarith

theorem lipschitzEigenvalueTestSquared {A B : Matrix n n 𝕜}
    (hA : A.IsHermitian) (hB : B.IsHermitian) (f : ℝ → ℝ) (C : ℝ)
    (hC : 0 ≤ C) (hf : ∀ x y, |f x - f y| ≤ C * |x-y|) :
    ((∑ i, f (hA.eigenvalues₀ i)) - ∑ i, f (hB.eigenvalues₀ i))^2 ≤
      C^2 * (Fintype.card n : ℝ) * frobSq (A-B) := by
  let a := hA.eigenvalues₀
  let b := hB.eigenvalues₀
  have habs : |(∑ i, f (a i)) - ∑ i, f (b i)| ≤ C * ∑ i, |a i-b i| := by
    rw [← sum_sub_distrib]
    calc
      |∑ i, (f (a i)-f (b i))| ≤ ∑ i, |f (a i)-f (b i)| := abs_sum_le_sum_abs _ _
      _ ≤ ∑ i, C * |a i-b i| := sum_le_sum fun i _ => hf _ _
      _ = C * ∑ i, |a i-b i| := by rw [mul_sum]
  have hsquare : ((∑ i, f (a i)) - ∑ i, f (b i))^2 ≤ (C * ∑ i, |a i-b i|)^2 := by
    have hh : 0 ≤ C * ∑ i, |a i-b i| := mul_nonneg hC (sum_nonneg fun _ _ => abs_nonneg _)
    have ht := mul_nonneg (sub_nonneg.mpr habs) (add_nonneg hh (abs_nonneg ((∑ i, f (a i)) - ∑ i, f (b i))))
    nlinarith [sq_abs ((∑ i, f (a i)) - ∑ i, f (b i))]
  have hcs := sum_mul_sq_le_sq_mul_sq (univ : Finset (Fin (Fintype.card n)))
    (fun i => |a i-b i|) (fun _ => (1 : ℝ))
  simp only [mul_one, one_pow, sum_const, nsmul_eq_mul, Fintype.card_fin, card_univ,
    sq_abs] at hcs
  have hhw := hoffmanWielandtSquared hA hB
  change (∑ i, (a i-b i)^2) ≤ frobSq (A-B) at hhw
  calc
    ((∑ i, f (hA.eigenvalues₀ i)) - ∑ i, f (hB.eigenvalues₀ i))^2
        ≤ (C * ∑ i, |a i-b i|)^2 := hsquare
    _ = C^2 * (∑ i, |a i-b i|)^2 := by ring
    _ ≤ C^2 * ((∑ i, (a i-b i)^2) * (Fintype.card n : ℝ)) :=
      mul_le_mul_of_nonneg_left hcs (sq_nonneg C)
    _ ≤ C^2 * (frobSq (A-B) * (Fintype.card n : ℝ)) := by gcongr
    _ = C^2 * (Fintype.card n : ℝ) * frobSq (A-B) := by ring

#check hoffmanWielandtSquared
#print axioms hoffmanWielandtSquared
#check lipschitzEigenvalueTestSquared
#print axioms lipschitzEigenvalueTestSquared
end ObservatoryFormal
