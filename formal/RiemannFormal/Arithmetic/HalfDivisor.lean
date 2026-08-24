import Mathlib.Algebra.BigOperators.NatAntidiagonal
import Mathlib.Data.Nat.Choose.Central
import Mathlib.NumberTheory.ArithmeticFunction.Moebius
import Mathlib.NumberTheory.ArithmeticFunction.Zeta
import Mathlib.RingTheory.PowerSeries.Binomial
import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.HalfDivisor

open scoped ArithmeticFunction ArithmeticFunction.Moebius ArithmeticFunction.zeta
open Finset

/-- The reviewed half-divisor prime-power coefficient. -/
def etaCoeff (k : ℕ) : ℚ :=
  (Nat.centralBinom k : ℚ) / (4 : ℚ) ^ k

/-- The same coefficient in generalized-binomial form. -/
def etaChoose (k : ℕ) : ℚ :=
  (-1 : ℚ) ^ k * Ring.choose (-(1 / 2 : ℚ)) k

@[simp]
theorem etaCoeff_zero : etaCoeff 0 = 1 := by
  norm_num [etaCoeff]

@[simp]
theorem etaChoose_zero : etaChoose 0 = 1 := by
  norm_num [etaChoose, Ring.choose_zero_right]

/-- Central-binomial recurrence after the exact `4^k` normalization. -/
theorem etaCoeff_recurrence (k : ℕ) :
    (k + 1 : ℚ) * etaCoeff (k + 1) =
      ((k : ℚ) + 1 / 2) * etaCoeff k := by
  have hcast :
      ((k + 1 : ℕ) : ℚ) * (Nat.centralBinom (k + 1) : ℚ) =
        2 * (2 * (k : ℚ) + 1) * (Nat.centralBinom k : ℚ) := by
    exact_mod_cast Nat.succ_mul_centralBinom_succ k
  unfold etaCoeff
  rw [pow_succ]
  calc
    (↑k + 1) * (↑(Nat.centralBinom (k + 1)) / ((4 : ℚ) ^ k * 4)) =
        (((k + 1 : ℕ) : ℚ) * (Nat.centralBinom (k + 1) : ℚ)) /
          ((4 : ℚ) ^ k * 4) := by ring
    _ = (2 * (2 * (k : ℚ) + 1) * (Nat.centralBinom k : ℚ)) /
          ((4 : ℚ) ^ k * 4) := by rw [hcast]
    _ = ((k : ℚ) + 1 / 2) *
          ((Nat.centralBinom k : ℚ) / (4 : ℚ) ^ k) := by
      field_simp
      ring

/-- Generalized-binomial recurrence for the same normalized sequence. -/
theorem etaChoose_recurrence (k : ℕ) :
    (k + 1 : ℚ) * etaChoose (k + 1) =
      ((k : ℚ) + 1 / 2) * etaChoose k := by
  have h := Ring.choose_smul_choose (R := ℚ) (-(1 / 2 : ℚ))
      (n := k + 1) (k := k) (Nat.le_succ k)
  simp only [Nat.choose_succ_self_right, Nat.cast_add, Nat.cast_one,
    Ring.choose_one_right, Nat.add_sub_cancel_left, nsmul_eq_mul] at h
  unfold etaChoose
  rw [pow_succ]
  calc
    (↑k + 1) * (((-1 : ℚ) ^ k * -1) * Ring.choose (-(1 / 2 : ℚ)) (k + 1)) =
        ((-1 : ℚ) ^ k * -1) *
          ((↑k + 1) * Ring.choose (-(1 / 2 : ℚ)) (k + 1)) := by ring
    _ = ((-1 : ℚ) ^ k * -1) *
          (Ring.choose (-(1 / 2 : ℚ)) k * (-(1 / 2 : ℚ) - k)) := by rw [h]
    _ = (↑k + 1 / 2) *
          ((-1 : ℚ) ^ k * Ring.choose (-(1 / 2 : ℚ)) k) := by ring

/-- The generalized-binomial and central-binomial definitions agree exactly. -/
theorem etaCoeff_eq_etaChoose (k : ℕ) : etaCoeff k = etaChoose k := by
  induction k with
  | zero => simp
  | succ k ih =>
      apply mul_left_cancel₀ (show (k + 1 : ℚ) ≠ 0 by positivity)
      calc
        (k + 1 : ℚ) * etaCoeff (k + 1) =
            ((k : ℚ) + 1 / 2) * etaCoeff k := etaCoeff_recurrence k
        _ = ((k : ℚ) + 1 / 2) * etaChoose k := by rw [ih]
        _ = (k + 1 : ℚ) * etaChoose (k + 1) := (etaChoose_recurrence k).symm

/-- Coefficient form of the central-binomial self-convolution identity. -/
theorem etaCoeff_antidiagonal (n : ℕ) :
    (∑ ij ∈ Finset.antidiagonal n, etaCoeff ij.1 * etaCoeff ij.2) = 1 := by
  simp_rw [etaCoeff_eq_etaChoose]
  have hv := Ring.add_choose_eq (R := ℚ)
    (r := -(1 / 2 : ℚ)) (s := -(1 / 2 : ℚ)) n (Commute.all _ _)
  have hsum :
      (∑ ij ∈ Finset.antidiagonal n,
        etaChoose ij.1 * etaChoose ij.2) =
        (-1 : ℚ) ^ n * Ring.choose (-1 : ℚ) n := by
    calc
      (∑ ij ∈ Finset.antidiagonal n,
        etaChoose ij.1 * etaChoose ij.2) =
          (∑ ij ∈ Finset.antidiagonal n,
            (-1 : ℚ) ^ n *
              (Ring.choose (-(1 / 2 : ℚ)) ij.1 *
                Ring.choose (-(1 / 2 : ℚ)) ij.2)) := by
            apply Finset.sum_congr rfl
            intro ij hij
            have hijsum : ij.1 + ij.2 = n := Finset.mem_antidiagonal.mp hij
            simp only [etaChoose, ← pow_add, hijsum]
            ring
      _ = (-1 : ℚ) ^ n *
          (∑ ij ∈ Finset.antidiagonal n,
            Ring.choose (-(1 / 2 : ℚ)) ij.1 *
              Ring.choose (-(1 / 2 : ℚ)) ij.2) := by
            rw [Finset.mul_sum]
      _ = (-1 : ℚ) ^ n * Ring.choose (-1 : ℚ) n := by
            rw [← hv]
            norm_num
  rw [hsum]
  have hneg := Ring.choose_neg' (R := ℚ) (1 : ℚ) n
  have hchoose : Ring.choose (-1 : ℚ) n = (-1 : ℚ) ^ n := by
    simpa [Ring.multichoose_one, Int.cast_negOnePow_natCast, Units.smul_def] using hneg
  rw [hchoose, ← pow_add]
  simp

/-- Range-indexed version used by prime-power Dirichlet convolution. -/
theorem etaCoeff_range (n : ℕ) :
    (∑ k ∈ Finset.range n.succ, etaCoeff k * etaCoeff (n - k)) = 1 := by
  rw [← Finset.Nat.sum_antidiagonal_eq_sum_range_succ
    (fun i j => etaCoeff i * etaCoeff j) n]
  exact etaCoeff_antidiagonal n

/-- Multiplicative arithmetic function with the reviewed prime-power coefficients. -/
noncomputable def eta : ArithmeticFunction ℚ where
  toFun n := if n = 0 then 0 else n.factorization.prod (fun _ k => etaCoeff k)
  map_zero' := by simp

@[simp]
theorem eta_apply_zero : eta 0 = 0 := by simp [eta]

@[simp]
theorem eta_apply_one : eta 1 = 1 := by simp [eta]

/-- The factorization definition is multiplicative. -/
theorem eta_isMultiplicative : eta.IsMultiplicative := by
  refine ArithmeticFunction.IsMultiplicative.iff_ne_zero.2 ⟨eta_apply_one, ?_⟩
  intro m n hm hn hcop
  simp only [eta, hm, hn, mul_ne_zero hm hn, if_false]
  rw [Nat.factorization_mul_of_coprime hcop]
  exact Finsupp.prod_add_index_of_disjoint hcop.disjoint_primeFactors
    (fun _ k => etaCoeff k)

/-- Exact reviewed prime-power normalization. -/
@[simp]
theorem eta_prime_pow {p k : ℕ} (hp : p.Prime) :
    eta (p ^ k) = etaCoeff k := by
  by_cases hk : k = 0
  · subst k
    simp [eta]
  · have hpk : p ^ k ≠ 0 := pow_ne_zero _ hp.ne_zero
    simp [eta, hpk, hp.factorization_pow, Finsupp.prod_single_index, etaCoeff_zero]

private theorem pow_div_pow_of_le {p i k : ℕ} (hp : 0 < p) (hi : i ≤ k) :
    p ^ k / p ^ i = p ^ (k - i) := by
  calc
    p ^ k / p ^ i = (p ^ i * p ^ (k - i)) / p ^ i := by
      congr 1
      rw [← pow_add, Nat.add_sub_of_le hi]
    _ = p ^ (k - i) := Nat.mul_div_cancel_left _ (pow_pos hp i)

/-- Exact arithmetic-function identity: the half-divisor is a Dirichlet square root of zeta. -/
theorem eta_mul_eta : eta * eta = (ArithmeticFunction.zeta : ArithmeticFunction ℚ) := by
  apply (ArithmeticFunction.IsMultiplicative.eq_iff_eq_on_prime_powers
    (eta * eta) (eta_isMultiplicative.mul eta_isMultiplicative)
    (ArithmeticFunction.zeta : ArithmeticFunction ℚ)
    ArithmeticFunction.isMultiplicative_zeta.natCast).2
  intro p k hp
  rw [ArithmeticFunction.mul_apply,
    Nat.sum_divisorsAntidiagonal (fun i j => eta i * eta j),
    Nat.sum_divisors_prime_pow hp]
  calc
    (∑ i ∈ Finset.range (k + 1), eta (p ^ i) * eta (p ^ k / p ^ i)) =
        ∑ i ∈ Finset.range k.succ, etaCoeff i * etaCoeff (k - i) := by
          apply Finset.sum_congr (by simp)
          intro i hi
          have hik : i ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
          rw [eta_prime_pow hp, pow_div_pow_of_le hp.pos hik, eta_prime_pow hp]
    _ = 1 := etaCoeff_range k
    _ = (ArithmeticFunction.zeta : ArithmeticFunction ℚ) (p ^ k) := by
      simp [ArithmeticFunction.zeta_apply_ne (pow_ne_zero _ hp.ne_zero)]

/-- Generic arithmetic-function convolution identity following from
`eta * eta = zeta` and Möbius inversion.

This is not the complete reviewed ratio-four one-field packet: no `b_U/h_U`
field, Hardy norm-three estimate, endpoint localization, or signed
near-collision theorem is asserted here. -/
theorem genericOneFieldConvolution (b : ArithmeticFunction ℚ) :
    (b * eta) * (b * eta) * (ArithmeticFunction.moebius : ArithmeticFunction ℚ) = b * b := by
  calc
    (b * eta) * (b * eta) * (ArithmeticFunction.moebius : ArithmeticFunction ℚ) =
        (b * b) * (eta * eta) * (ArithmeticFunction.moebius : ArithmeticFunction ℚ) := by
          ac_rfl
    _ = (b * b) * (ArithmeticFunction.zeta : ArithmeticFunction ℚ) *
        (ArithmeticFunction.moebius : ArithmeticFunction ℚ) := by rw [eta_mul_eta]
    _ = b * b := by
      rw [mul_assoc, ArithmeticFunction.coe_zeta_mul_coe_moebius, mul_one]

end RiemannFormal.Arithmetic.HalfDivisor
