import Mathlib.Algebra.BigOperators.Module
import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.Wavelet

/-!
# Generic finite tap helpers

This module contains finite algebra used by the reviewed wavelet packet.  It
does **not** claim the full canonical ratio-eight kernel, factor-67 piecewise
copy, compact Abel--Mertens frame, or quantitative same-K1 translation.
-/

/-- Generic four-tap filter with polynomial `(1 - αD)(1 - D)^2`. -/
def fourTapValues {R : Type*} [Ring R] (α x0 x1 x2 x3 : R) : R :=
  x0 - (α + 2) * x1 + (2 * α + 1) * x2 - α * x3

/-- The same generic filter applied to a sequence at one index. -/
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

/-- No three-tap filter can annihilate constants, affine data, and a distinct
geometric mode.  This is generic minimality, not yet the complete canonical
wavelet theorem. -/
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

/-- The four sampled dyadic indices span three doublings.  This is only an
index-span helper; it is not the canonical piecewise support theorem. -/
theorem dyadic_four_tap_index_span : 2 ^ (3 : ℕ) = 8 := by norm_num

/-- Generic sign flip after affine nuisance terms are removed.  The theorem is
not named as the reviewed factor-67 kernel identity because no factor 67 or
piecewise endpoint convention occurs in its statement. -/
theorem affine_nuisance_sign_flip {R : Type*} [CommRing R]
    (α f0 f1 f2 f3 c d : R) :
    fourTapValues α
        (-f0 + c)
        (-f1 + c + d)
        (-f2 + c + 2 * d)
        (-f3 + c + 3 * d) =
      -fourTapValues α f0 f1 f2 f3 := by
  simp [fourTapValues]
  ring

/-- Forward index shift. -/
def shift {R : Type*} (k : ℕ) (f : ℕ → R) : ℕ → R := fun n => f (n + k)

/-- First finite difference. -/
def difference {R : Type*} [Sub R] (f : ℕ → R) : ℕ → R :=
  fun n => f n - f (n + 1)

/-- The generic `1 - αD` factor. -/
def alphaDifference {R : Type*} [Ring R] (α : R) (f : ℕ → R) : ℕ → R :=
  fun n => f n - α * f (n + 1)

/-- Exact operator factorization of the generic four-tap helper. -/
theorem fourTap_eq_factored {R : Type*} [CommRing R]
    (α : R) (f : ℕ → R) (n : ℕ) :
    fourTap α f n = alphaDifference α (difference (difference f)) n := by
  simp [fourTap, fourTapValues, alphaDifference, difference]
  ring

/-- Finite shift identity for the same kernel. -/
theorem fourTap_shift {R : Type*} [Ring R]
    (α : R) (f : ℕ → R) (k n : ℕ) :
    fourTap α (shift k f) n = fourTap α f (n + k) := by
  simp [fourTap, shift, add_assoc, add_left_comm, add_comm]

/-- Generic finite summation by parts.  The canonical compact Abel--Mertens
wavelet frame additionally requires the exact wavelet kernel and endpoint
conventions and is not asserted here. -/
theorem finite_sum_by_parts (f g : ℕ → ℚ) (n : ℕ) :
    (∑ i ∈ Finset.range n, f i * g i) =
      f (n - 1) * (∑ i ∈ Finset.range n, g i) -
        ∑ i ∈ Finset.range (n - 1),
          (f (i + 1) - f i) * (∑ j ∈ Finset.range (i + 1), g j) := by
  simpa [smul_eq_mul] using (Finset.sum_range_by_parts f g n)

/-- Kernel tags make direct K0/K1 substitution ill-typed. -/
inductive KernelId where
  | K0
  | K1
  deriving DecidableEq, Repr

structure KernelDetector (kernel : KernelId) where
  coefficient : ℕ → ℚ

/-- Type-level K0/K1 firewall.  This is not the analytic counterexample proving
the historical cross-kernel equivalence false. -/
@[simp]
theorem K0_ne_K1 : KernelId.K0 ≠ KernelId.K1 := by decide

/-- Identity on one already-fixed K1 detector.  This is only a type-preservation
helper, not the reviewed largest-prime/Vaughan `L¹(dX/X)` translation. -/
def sameKernelIdentity (d : KernelDetector .K1) : KernelDetector .K1 := d

@[simp]
theorem sameKernelIdentity_coefficient (d : KernelDetector .K1) :
    (sameKernelIdentity d).coefficient = d.coefficient := rfl

end RiemannFormal.Arithmetic.Wavelet
