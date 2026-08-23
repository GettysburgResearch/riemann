import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.SourceIdentities

open RiemannFormal.Arithmetic

/-- Accumulated parity is multiplicative under concatenation of labelled histories. -/
theorem paritySign_add (m n : ℕ) :
    paritySign (m + n) = paritySign m * paritySign n := by
  simp [paritySign, pow_add]

/-- Two labelled copies of one prime produce the exact `(1,-2,1)` fibre. -/
theorem duplicate_label_fiber (r : ℚ) :
    (1 - r) ^ 2 = 1 - 2 * r + r ^ 2 := by
  ring

/-- The native finite Euler product in a commuting coefficient algebra. -/
def nativeEuler {R : Type*} [CommRing R] : List (R × R) → R
  | [] => 1
  | (r, u) :: xs => (1 - r * u) * nativeEuler xs

/-- Sequential first-owner expansion: survive the first prime or stop there. -/
def firstOwner {R : Type*} [CommRing R] : List (R × R) → R
  | [] => 1
  | (r, u) :: xs =>
      (1 - r) * firstOwner xs + r * (1 - u) * nativeEuler xs

/-- The sequential first-owner decomposition exactly reproduces every finite native Euler coefficient. -/
theorem firstOwner_eq_nativeEuler {R : Type*} [CommRing R]
    (xs : List (R × R)) : firstOwner xs = nativeEuler xs := by
  induction xs with
  | nil => simp [firstOwner, nativeEuler]
  | cons x xs ih =>
      rcases x with ⟨r, u⟩
      simp [firstOwner, nativeEuler, ih]
      ring

/-- One-prime alpha-child algebra: the shifted coefficient cancels. -/
def alphaShiftedCoefficient (r : ℚ) : ℚ := -r * r + r ^ 2

/-- The native one-prime Euler shifted coefficient. -/
def nativeShiftedCoefficient (r : ℚ) : ℚ := -r

/-- Two contracted parity-labelled shifted copies have magnitude `2 r²`. -/
def parityContractedMagnitude (r : ℚ) : ℚ := 2 * r ^ 2

@[simp]
theorem alphaShiftedCoefficient_eq_zero (r : ℚ) :
    alphaShiftedCoefficient r = 0 := by
  simp [alphaShiftedCoefficient]
  ring

/-- Exact witness for the historical `r` versus `2 r²` source mismatch. -/
theorem r_vs_two_r_sq_witness :
    parityContractedMagnitude (1 / 3 : ℚ) ≠ (1 / 3 : ℚ) := by
  norm_num [parityContractedMagnitude]

/-- The mismatch is strict throughout the reviewed rough-prime range `0 < r < 1/2`. -/
theorem two_r_sq_lt_r {r : ℚ} (hr0 : 0 < r) (hr : r < 1 / 2) :
    parityContractedMagnitude r < r := by
  unfold parityContractedMagnitude
  nlinarith

/-- The alpha-child identity is an identity for the parent packet, not a native Euler factor. -/
theorem alpha_parent_identity (r parent shifted : ℚ) :
    (1 - r) * parent + r * (parent - r * shifted) + r ^ 2 * shifted = parent := by
  ring

/-- The native and alpha shifted coefficients are already separated at `r = 1/3`. -/
theorem alpha_not_native_witness :
    alphaShiftedCoefficient (1 / 3 : ℚ) ≠ nativeShiftedCoefficient (1 / 3 : ℚ) := by
  norm_num [alphaShiftedCoefficient, nativeShiftedCoefficient]

/-- A finite Radon--Nikodym ratio in an abstract target coordinate. -/
def rnRatio {α : Type*} (target : α → ℚ) (child parent : α) : ℚ :=
  target child / target parent

/-- Projective Radon--Nikodym cocycle. -/
theorem rnRatio_cocycle {α : Type*} (target : α → ℚ) (w z y : α)
    (hz : target z ≠ 0) (hy : target y ≠ 0) :
    rnRatio target w z * rnRatio target z y = rnRatio target w y := by
  simp [rnRatio]
  field_simp [hz, hy] <;> ring

/-- SHARP target evaluated at a rational square-root coordinate. -/
def sharpTargetRoot (r : ℚ) : ℚ := 4 * r - 3

/-- The reviewed raw-cutoff/RN-child hostile fixture gives the exact ratio `1/5`. -/
theorem rn_raw_cutoff_witness :
    rnRatio sharpTargetRoot 1 2 = (1 / 5 : ℚ) := by
  norm_num [rnRatio, sharpTargetRoot]

/-- A one-coordinate arithmetic function, used only for finite type witnesses. -/
def singletonAF (c : ℚ) : ArithmeticFunction ℚ where
  toFun n := if n = 1 then c else 0
  map_zero' := by simp

/-- Actual child response witness. -/
def responseWitness : ChildResponse ℚ :=
  ⟨singletonAF 1⟩

/-- Total child capacity witness. -/
def capacityWitness : ChildCapacity ℚ :=
  ⟨singletonAF 5⟩

/-- Even after forgetting the role index, actual response and total capacity differ. -/
theorem response_capacity_coefficients_differ :
    responseWitness.coefficient 1 ≠ capacityWitness.coefficient 1 := by
  norm_num [responseWitness, capacityWitness, singletonAF]

/-- Squared activity and unsquared amplitude are distinct throughout the nontrivial range. -/
theorem normalized_activity_ne_amplitude {r : ℚ} (hr0 : 0 < r) (hr1 : r < 1) :
    r ^ 2 ≠ r := by
  nlinarith

/-- Exact square-prime normalization witness: `p⁻¹` is not `p⁻¹/²`. -/
theorem normalized_p_inv_ne_p_inv_sqrt_witness :
    (1 / 4 : ℚ) ≠ (1 / 2 : ℚ) := by norm_num

/-- Signed observations and positive sources are distinct roles. -/
theorem signedObservation_ne_auxiliaryPositive :
    SourceRole.signedObservation ≠ SourceRole.auxiliaryPositiveSource := by decide

end RiemannFormal.Arithmetic.SourceIdentities
