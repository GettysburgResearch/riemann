import Mathlib

namespace RiemannFormal.Operator

/-- A second-order jet.  The formalization records exactly the value and first
two derivatives needed by the reviewed order-three argument. -/
structure Jet2 where
  value : ℝ
  first : ℝ
  second : ℝ
  deriving Repr

namespace Jet2

/-- Pointwise sum of two second-order jets. -/
def add (f g : Jet2) : Jet2 :=
  ⟨f.value + g.value, f.first + g.first, f.second + g.second⟩

/-- Positive scalar multiplication of a jet. -/
def smul (c : ℝ) (f : Jet2) : Jet2 :=
  ⟨c * f.value, c * f.first, c * f.second⟩

/-- Reciprocal-concavity curvature `f f'' - 2 (f')^2`. -/
def energy (f : Jet2) : ℝ := f.value * f.second - 2 * f.first ^ 2

/-- Cross curvature appearing when two jets are added. -/
def cross (f g : Jet2) : ℝ :=
  f.value * g.second + g.value * f.second - 4 * f.first * g.first

/-- Exact expansion of reciprocal curvature under addition. -/
theorem energy_add (f g : Jet2) :
    energy (add f g) = energy f + energy g + cross f g := by
  simp [energy, add, cross]
  ring

/-- Exact scaling identity. -/
theorem energy_smul (c : ℝ) (f : Jet2) :
    energy (smul c f) = c ^ 2 * energy f := by
  simp [energy, smul]
  ring

/-- The cross term has an exact square certificate after multiplication by the
positive values. -/
theorem cross_square_certificate (f g : Jet2) :
    f.value * g.value * cross f g =
      f.value ^ 2 * energy g + g.value ^ 2 * energy f +
        2 * (g.value * f.first - f.value * g.first) ^ 2 := by
  simp [cross, energy]
  ring

/-- Finite positive-sum closure of reciprocal concavity (`L-92100`). -/
theorem reciprocalConcavity_add
    {f g : Jet2}
    (hfpos : 0 < f.value) (hgpos : 0 < g.value)
    (hf : 0 ≤ energy f) (hg : 0 ≤ energy g) :
    0 ≤ energy (add f g) := by
  have hcrossScaled : 0 ≤ f.value * g.value * cross f g := by
    rw [cross_square_certificate]
    exact add_nonneg (add_nonneg (mul_nonneg (sq_nonneg _) hg)
      (mul_nonneg (sq_nonneg _) hf)) (mul_nonneg (by norm_num) (sq_nonneg _))
  have hcross : 0 ≤ cross f g := by
    nlinarith [mul_pos hfpos hgpos]
  rw [energy_add]
  linarith

/-- Positive scaling preserves reciprocal concavity. -/
theorem reciprocalConcavity_smul
    {c : ℝ} {f : Jet2} (hc : 0 ≤ c) (hf : 0 ≤ energy f) :
    0 ≤ energy (smul c f) := by
  rw [energy_smul]
  exact mul_nonneg (sq_nonneg _) hf

/-- Exact energy of one off-line orbit jet. -/
def offLineJet (m U B : ℝ) : Jet2 :=
  ⟨4 * m * U / (U ^ 2 + B ^ 2),
   4 * m * (B ^ 2 - U ^ 2) / (U ^ 2 + B ^ 2) ^ 2,
   8 * m * U * (U ^ 2 - 3 * B ^ 2) / (U ^ 2 + B ^ 2) ^ 3⟩

/-- The off-line orbit has the exact negative reciprocal-curvature defect. -/
theorem offLineOrbit_defect_formula
    {m U B : ℝ} (hden : U ^ 2 + B ^ 2 ≠ 0) :
    energy (offLineJet m U B) =
      -32 * m ^ 2 * B ^ 2 / (U ^ 2 + B ^ 2) ^ 3 := by
  field_simp [energy, offLineJet, hden]
  ring

/-- One unit of a critical-line orbit. -/
def criticalJet (V : ℝ) : Jet2 :=
  ⟨2 / V, -2 / V ^ 2, 4 / V ^ 3⟩

/-- A critical-line orbit has zero reciprocal curvature. -/
theorem criticalOrbit_energy_zero {V : ℝ} (hV : V ≠ 0) :
    energy (criticalJet V) = 0 := by
  field_simp [energy, criticalJet, hV]
  ring

/-- Exact reserve-expansion identity used for one-orbit absorption. -/
theorem energy_add_scaled (q r : Jet2) (epsilon : ℝ) :
    energy (add q (smul epsilon r)) =
      energy q + epsilon * cross q r + epsilon ^ 2 * energy r := by
  simp [energy, add, smul, cross]
  ring

/-- Single-orbit reciprocal-concavity lemma.  Every numerical or analytic input
is visible: the orbit defect, the reserve's zero curvature, and the amount of
positive cross curvature paid by `epsilon`. -/
theorem oneOrbitAbsorption
    {q r : Jet2} {defect epsilon : ℝ}
    (hdefect : energy q = -defect)
    (hreserve : energy r = 0)
    (hpay : defect ≤ epsilon * cross q r) :
    0 ≤ energy (add q (smul epsilon r)) := by
  rw [energy_add_scaled, hdefect, hreserve]
  nlinarith [sq_nonneg epsilon]

/-- Finite reserve-allocation lemma.  This is the exact algebraic part of the
critical-orbit budget; it does not assert the external high-zero theorem or an
infinite zero-tail estimate. -/
theorem finiteReserveAllocation
    {n : Nat} (epsilon : Fin n → ℝ)
    (hsum : (∑ i, epsilon i) < 1) :
    ∃ epsilon0 : ℝ, 0 < epsilon0 ∧ epsilon0 + ∑ i, epsilon i = 1 := by
  refine ⟨1 - ∑ i, epsilon i, sub_pos.mpr hsum, ?_⟩
  ring

/-- A finite reciprocal-square tail bound controls the total reserve cost. -/
theorem reciprocalSquareTailBudget
    {n : Nat} (epsilon tail : Fin n → ℝ)
    (hpoint : ∀ i, epsilon i ≤ 9 * tail i)
    (htail : (∑ i, tail i) < 1 / 9) :
    (∑ i, epsilon i) < 1 := by
  have hsum : (∑ i, epsilon i) ≤ ∑ i, 9 * tail i :=
    Finset.sum_le_sum fun i _ => hpoint i
  have hscale : (∑ i, 9 * tail i) = 9 * ∑ i, tail i := by
    rw [Finset.mul_sum]
  rw [hscale] at hsum
  nlinarith

end Jet2

end RiemannFormal.Operator
