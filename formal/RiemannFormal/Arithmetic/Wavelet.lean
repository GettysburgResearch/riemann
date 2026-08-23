import Mathlib.Algebra.BigOperators.Module
import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.Wavelet

/-- The four-tap compact filter with polynomial `(1 - αD)(1 - D)^2`. -/
def fourTapValues {R : Type*} [Ring R] (α x0 x1 x2 x3 : R) : R :=
  x0 - (α + 2) * x1 + (2 * α + 1) * x2 - α * x3

/-- The same filter applied to a sequence at one dyadic location. -/
def fourTap {R : Type*} [Ring R] (α : R) (f : ℕ → R) (n : ℕ) : R :=
  fourTapValues α (f n) (f (n + 1)) (f (n + 2)) (f (n + 3))

@[simp]
theorem fourTapValues_constant {R : Type*} [CommRing R] (α c : R) :
    fourTapValues α c c c c = 0 := by
  simp [fourTapValues]
  ring

@[simp]
theorem fourTapValues_affine {R : Type*} [CommRing R] (α x d : R) :
    fourTapValues α x (x + d) (x + 2 * d) (x + 3 * d) = 0 := by
  simp [fourTapValues]
  ring

/-- Exact factorization on a geometric four-sample block. -/
theorem fourTapValues_geometric {R : Type*} [CommRing R] (α q x : R) :
    fourTapValues α x (x * q) (x * q ^ 2) (x * q ^ 3) =
      x * (1 - q) ^ 2 * (1 - α * q) := by
  simp [fourTapValues]
  ring

/-- The third annihilated mode is the geometric mode satisfying `α q = 1`. -/
theorem fourTapValues_geometric_zero {R : Type*} [CommRing R]
    (α q x : R) (h : α * q = 1) :
    fourTapValues α x (x * q) (x * q ^ 2) (x * q ^ 3) = 0 := by
  rw [fourTapValues_geometric, h]
  ring

/-- No three-tap filter can annihilate constants, affine data, and a distinct geometric mode. -/
theorem threeTap_minimal (q c0 c1 c2 : ℂ) (hq : q ≠ 1)
    (hconst : c0 + c1 + c2 = 0)
    (haff : c1 + 2 * c2 = 0)
    (hgeom : c0 + c1 * q + c2 * q ^ 2 = 0) :
    c0 = 0 ∧ c1 = 0 ∧ c2 = 0 := by
  have hc1 : c1 = -2 * c2 := by
    linear_combination haff
  have hc0 : c0 = c2 := by
    linear_combination hconst - haff
  have hprod : c2 * (q - 1) ^ 2 = 0 := by
    calc
      c2 * (q - 1) ^ 2 = c0 + c1 * q + c2 * q ^ 2 := by
        rw [hc0, hc1]
        ring
      _ = 0 := hgeom
  have hc2 : c2 = 0 := by
    rcases mul_eq_zero.mp hprod with hc2 | hq2
    · exact hc2
    · have hqq : (q - 1) * (q - 1) = 0 := by simpa [pow_two] using hq2
      rcases mul_eq_zero.mp hqq with hq0 | hq0
      · exact (hq (sub_eq_zero.mp hq0)).elim
      · exact (hq (sub_eq_zero.mp hq0)).elim
  constructor
  · simpa [hc2] using hc0
  constructor
  · simpa [hc2] using hc1
  · exact hc2

/-- The support exponents `0,1,2,3` span the exact ratio eight. -/
theorem ratioEight_support : 2 ^ (3 : ℕ) = 8 := by norm_num

/-- Abstract factor-67 antisymmetry after the two polynomial nuisance modes are removed. -/
theorem factor67_antisymmetry {R : Type*} [CommRing R]
    (α f0 f1 f2 f3 c d : R) :
    fourTapValues α
        (-f0 + c)
        (-f1 + c + d)
        (-f2 + c + 2 * d)
        (-f3 + c + 3 * d) =
      -fourTapValues α f0 f1 f2 f3 := by
  simp [fourTapValues]
  ring

/-- Forward dyadic shift. -/
def shift {R : Type*} (k : ℕ) (f : ℕ → R) : ℕ → R := fun n => f (n + k)

/-- First finite difference. -/
def difference {R : Type*} [Sub R] (f : ℕ → R) : ℕ → R :=
  fun n => f n - f (n + 1)

/-- The `1 - αD` factor. -/
def alphaDifference {R : Type*} [Ring R] (α : R) (f : ℕ → R) : ℕ → R :=
  fun n => f n - α * f (n + 1)

/-- Exact operator factorization of the compact wavelet. -/
theorem fourTap_eq_factored {R : Type*} [CommRing R]
    (α : R) (f : ℕ → R) (n : ℕ) :
    fourTap α f n = alphaDifference α (difference (difference f)) n := by
  simp [fourTap, fourTapValues, alphaDifference, difference]
  ring

/-- Dilation/translation is performed with the same finite kernel. -/
theorem fourTap_shift {R : Type*} [Ring R]
    (α : R) (f : ℕ → R) (k n : ℕ) :
    fourTap α (shift k f) n = fourTap α f (n + k) := by
  simp [fourTap, shift, add_assoc, add_left_comm, add_comm]

/-- Finite Abel summation, kept entirely at the algebraic finite-sum level. -/
theorem finite_abel_mertens (f g : ℕ → ℚ) (n : ℕ) :
    (∑ i ∈ Finset.range n, f i * g i) =
      f (n - 1) * (∑ i ∈ Finset.range n, g i) -
        ∑ i ∈ Finset.range (n - 1),
          (f (i + 1) - f i) * (∑ j ∈ Finset.range (i + 1), g j) := by
  simpa [smul_eq_mul] using (Finset.sum_range_by_parts f g n)

/-- Kernel tags prevent the historical K0/K1 detector mutation. -/
inductive KernelId where
  | K0
  | K1
  deriving DecidableEq, Repr

structure KernelDetector (kernel : KernelId) where
  coefficient : ℕ → ℚ

@[simp]
theorem K0_ne_K1 : KernelId.K0 ≠ KernelId.K1 := by decide

/-- A same-K1 translation is definitionally source preserving. -/
def sameK1Translation (d : KernelDetector .K1) : KernelDetector .K1 := d

@[simp]
theorem sameK1Translation_coefficient (d : KernelDetector .K1) :
    (sameK1Translation d).coefficient = d.coefficient := rfl

end RiemannFormal.Arithmetic.Wavelet
