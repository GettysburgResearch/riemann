import Mathlib.Tactic
import RiemannFormal.Arithmetic.Foundations

namespace RiemannFormal.Arithmetic.SourceIdentities

open RiemannFormal.Arithmetic

/-- Accumulated parity is multiplicative under concatenation of labelled histories. -/
theorem paritySign_add (m n : ℕ) :
    paritySign (m + n) = paritySign m * paritySign n := by
  simp [paritySign, pow_add]

/-- Two labelled copies of one prime produce the exact `(1,-2,1)` scalar fibre. -/
theorem duplicate_label_fiber (r : ℚ) :
    (1 - r) ^ 2 = 1 - 2 * r + r ^ 2 := by
  ring

/-- First labelled occurrence of the reviewed rough prime 67. -/
def duplicate67Left : PrimeLabel where
  prime := 67
  isPrime := by norm_num
  copy := 0

/-- Second labelled occurrence of the same reviewed rough prime 67. -/
def duplicate67Right : PrimeLabel where
  prime := 67
  isPrime := by norm_num
  copy := 1

/-- Duplicate labels can project to the same prime while remaining distinct occurrences. -/
theorem duplicate67_same_prime_distinct_labels :
    duplicate67Left.prime = duplicate67Right.prime ∧
      duplicate67Left ≠ duplicate67Right := by
  constructor
  · rfl
  · intro h
    have hcopy : duplicate67Left.copy = duplicate67Right.copy :=
      congrArg PrimeLabel.copy h
    norm_num [duplicate67Left, duplicate67Right] at hcopy

/-- Exact accumulated-parity fixture for one versus two labelled occurrences. -/
theorem duplicate67_parity_fixture :
    paritySign 1 = -1 ∧ paritySign 2 = 1 := by
  norm_num [paritySign]

/-!
## Generic scalar first-owner helper

The following list identity is useful finite algebra, but it is deliberately
not named as the canonical reviewed theorem `L-99601`.  It does not encode
labelled prime occurrences, commuting shifts, complete future-prime products,
disjoint ownership, or the positive source/signed observation interface.
-/

/-- Generic finite Euler product in a commuting scalar coefficient algebra. -/
def finiteEulerProduct {R : Type*} [CommRing R] : List (R × R) → R
  | [] => 1
  | (r, u) :: xs => (1 - r * u) * finiteEulerProduct xs

/-- Generic scalar first-owner recursion. -/
def scalarFirstOwnerExpansion {R : Type*} [CommRing R] : List (R × R) → R
  | [] => 1
  | (r, u) :: xs =>
      (1 - r) * scalarFirstOwnerExpansion xs +
        r * (1 - u) * finiteEulerProduct xs

/-- The generic scalar recursion exactly reproduces the finite Euler product. -/
theorem scalarFirstOwnerExpansion_eq_finiteEulerProduct
    {R : Type*} [CommRing R] (xs : List (R × R)) :
    scalarFirstOwnerExpansion xs = finiteEulerProduct xs := by
  induction xs with
  | nil => simp [scalarFirstOwnerExpansion, finiteEulerProduct]
  | cons x xs ih =>
      rcases x with ⟨r, u⟩
      simp [scalarFirstOwnerExpansion, finiteEulerProduct, ih]
      ring

/-! ## Exact one-prime coefficient firewalls -/

/-- One-prime alpha-child algebra: the shifted coefficient cancels. -/
def alphaShiftedCoefficient (r : ℚ) : ℚ := -r * r + r ^ 2

/-- Native one-prime Euler magnitude. -/
def nativeOnePrimeMagnitude (r : ℚ) : ℚ := r

/-- Two contracted parity-labelled shifted copies have magnitude `2 r²`. -/
def parityContractedMagnitude (r : ℚ) : ℚ := 2 * r ^ 2

@[simp]
theorem alphaShiftedCoefficient_eq_zero (r : ℚ) :
    alphaShiftedCoefficient r = 0 := by
  simp [alphaShiftedCoefficient]
  ring

/-- Exact representative witness for the historical `r` versus `2 r²` mismatch. -/
theorem r_vs_two_r_sq_witness :
    parityContractedMagnitude (1 / 3 : ℚ) ≠ nativeOnePrimeMagnitude (1 / 3 : ℚ) := by
  norm_num [parityContractedMagnitude, nativeOnePrimeMagnitude]

/-- The mismatch is strict throughout the reviewed rough-prime range `0 < r < 1/2`. -/
theorem two_r_sq_lt_r {r : ℚ} (hr0 : 0 < r) (hr : r < 1 / 2) :
    parityContractedMagnitude r < nativeOnePrimeMagnitude r := by
  unfold parityContractedMagnitude nativeOnePrimeMagnitude
  nlinarith

/-- Quantified source coefficient firewall, not merely one numerical example. -/
theorem native_one_prime_ne_contracted_two_child
    {r : ℚ} (hr0 : 0 < r) (hr : r < 1 / 2) :
    nativeOnePrimeMagnitude r ≠ parityContractedMagnitude r :=
  ne_of_gt (two_r_sq_lt_r hr0 hr)

/-- The alpha-child identity is an identity for the parent packet, not a native Euler factor. -/
theorem alpha_parent_identity (r parent shifted : ℚ) :
    (1 - r) * parent + r * (parent - r * shifted) + r ^ 2 * shifted = parent := by
  ring

/-! ## Exact endpoint Radon--Nikodym fixture -/

/-- The reviewed SHARP endpoint target `T(y)=(4 sqrt(y)-3) 1_{y≥1}`. -/
noncomputable def sharpTarget (y : ℝ) : ℝ :=
  if 1 ≤ y then 4 * Real.sqrt y - 3 else 0

/-- Raw support cutoff used by the historically false child substitution. -/
noncomputable def rawSupportCutoff (z t : ℝ) : ℝ :=
  if t ≤ z then 1 else 0

/-- Exact endpoint Radon--Nikodym child density. -/
noncomputable def sharpRNDensity (y z t : ℝ) : ℝ :=
  if t ≤ z then sharpTarget (z / t) / sharpTarget (y / t) else 0

@[simp]
theorem sharpTarget_one : sharpTarget 1 = 1 := by
  norm_num [sharpTarget]

@[simp]
theorem sharpTarget_four : sharpTarget 4 = 5 := by
  norm_num [sharpTarget]

/-- At `(Y,Z,t)=(16,4,4)`, the parent capacity coefficient is exactly five. -/
theorem rn_fixture_parent_capacity :
    sharpTarget ((16 : ℝ) / 4) = 5 := by
  norm_num [sharpTarget]

/-- At `(Y,Z,t)=(16,4,4)`, the child response coefficient is exactly one. -/
theorem rn_fixture_child_response :
    sharpTarget ((4 : ℝ) / 4) = 1 := by
  norm_num [sharpTarget]

/-- The exact reviewed RN density at `(16,4,4)` is `1/5`. -/
theorem sharpRNDensity_16_4_4 :
    sharpRNDensity 16 4 4 = (1 / 5 : ℝ) := by
  norm_num [sharpRNDensity, sharpTarget]

/-- The raw support cutoff is one at the same cell. -/
theorem rawSupportCutoff_4_4 : rawSupportCutoff 4 4 = 1 := by
  norm_num [rawSupportCutoff]

/-- Exact hostile fixture: raw cutoff and RN child are different objects. -/
theorem raw_cutoff_ne_rn_child_16_4_4 :
    rawSupportCutoff 4 4 ≠ sharpRNDensity 16 4 4 := by
  norm_num [rawSupportCutoff, sharpRNDensity, sharpTarget]

/-- The RN density transports the parent coefficient to the actual child response. -/
theorem rn_density_times_capacity_eq_response_16_4_4 :
    sharpRNDensity 16 4 4 * sharpTarget ((16 : ℝ) / 4) =
      sharpTarget ((4 : ℝ) / 4) := by
  norm_num [sharpRNDensity, sharpTarget]

/-- A generic finite RN ratio.  This proves only the algebraic cocycle after all
support and nonzero hypotheses have already been supplied. -/
def rnRatio {α : Type*} (target : α → ℚ) (child parent : α) : ℚ :=
  target child / target parent

/-- Projective ratio cocycle at generic finite algebraic scope. -/
theorem rnRatio_cocycle {α : Type*} (target : α → ℚ) (w z y : α)
    (hz : target z ≠ 0) (hy : target y ≠ 0) :
    rnRatio target w z * rnRatio target z y = rnRatio target w y := by
  simp [rnRatio]
  field_simp [hz, hy] <;> ring

/-- A one-coordinate arithmetic function used for exact typed finite fixtures. -/
def singletonAFReal (c : ℝ) : ArithmeticFunction ℝ where
  toFun n := if n = 1 then c else 0
  map_zero' := by simp

/-- Actual child response at the reviewed `(16,4,4)` cell. -/
noncomputable def rnFixtureResponse : ChildResponse ℝ :=
  ⟨singletonAFReal (sharpTarget ((4 : ℝ) / 4))⟩

/-- Total parent-side capacity at the reviewed `(16,4,4)` cell. -/
noncomputable def rnFixtureCapacity : ChildCapacity ℝ :=
  ⟨singletonAFReal (sharpTarget ((16 : ℝ) / 4))⟩

/-- Exact typed response/capacity coefficient separation at the reviewed cell. -/
theorem response_capacity_coefficients_differ_16_4_4 :
    rnFixtureResponse.coefficient 1 ≠ rnFixtureCapacity.coefficient 1 := by
  norm_num [rnFixtureResponse, rnFixtureCapacity, singletonAFReal, sharpTarget]

/-! ## Quantified normalization firewall -/

/-- Normalized activity after a `p^{-1/2}` amplitude has been squared. -/
noncomputable def normalizedPrimeActivity (p : ℝ) : ℝ := 1 / p

/-- Unsquared prime amplitude. -/
noncomputable def primeAmplitude (p : ℝ) : ℝ := 1 / Real.sqrt p

/-- For every `p>1`, normalized `p^{-1}` activity is strictly smaller than
unnormalized `p^{-1/2}` amplitude. -/
theorem normalized_p_inv_lt_p_inv_sqrt {p : ℝ} (hp : 1 < p) :
    normalizedPrimeActivity p < primeAmplitude p := by
  have hp0 : 0 < p := lt_trans zero_lt_one hp
  have hspos : 0 < Real.sqrt p := Real.sqrt_pos.2 hp0
  have hsq : (Real.sqrt p) ^ 2 = p := Real.sq_sqrt (le_of_lt hp0)
  have hslt : Real.sqrt p < p := by
    nlinarith [Real.sqrt_nonneg p]
  simpa [normalizedPrimeActivity, primeAmplitude] using
    (one_div_lt_one_div_of_lt hspos hslt)

/-- Quantified normalization mismatch. -/
theorem normalized_p_inv_ne_p_inv_sqrt {p : ℝ} (hp : 1 < p) :
    normalizedPrimeActivity p ≠ primeAmplitude p :=
  ne_of_lt (normalized_p_inv_lt_p_inv_sqrt hp)

end RiemannFormal.Arithmetic.SourceIdentities
