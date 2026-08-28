import Mathlib

namespace RiemannFormal.Operator

/-- Determinant of a symmetric two-by-two matrix `[[a,b],[b,c]]`. -/
def det2 (a b c : ℝ) : ℝ := a * c - b ^ 2

/-- Determinant of a symmetric three-by-three matrix
`[[a,b,c],[b,d,e],[c,e,f]]`. -/
def det3 (a b c d e f : ℝ) : ℝ :=
  a * d * f + 2 * b * c * e - a * e ^ 2 - d * c ^ 2 - f * b ^ 2

/-- Quadratic form of a symmetric two-by-two matrix. -/
def quad2 (a b c x y : ℝ) : ℝ := a * x ^ 2 + 2 * b * x * y + c * y ^ 2

/-- Quadratic form of a symmetric three-by-three matrix. -/
def quad3 (a b c d e f x y z : ℝ) : ℝ :=
  a * x ^ 2 + 2 * b * x * y + 2 * c * x * z +
    d * y ^ 2 + 2 * e * y * z + f * z ^ 2

/-- Scalar, kernel-checkable PSD predicate for a symmetric two-by-two matrix. -/
def IsPSD2 (a b c : ℝ) : Prop := ∀ x y : ℝ, 0 ≤ quad2 a b c x y

/-- Scalar, kernel-checkable positive-definite predicate for a symmetric two-by-two matrix. -/
def IsPD2 (a b c : ℝ) : Prop :=
  ∀ x y : ℝ, x ≠ 0 ∨ y ≠ 0 → 0 < quad2 a b c x y

/-- Scalar, kernel-checkable PSD predicate for a symmetric three-by-three matrix. -/
def IsPSD3 (a b c d e f : ℝ) : Prop :=
  ∀ x y z : ℝ, 0 ≤ quad3 a b c d e f x y z

/-- Scalar, kernel-checkable positive-definite predicate for a symmetric three-by-three matrix. -/
def IsPD3 (a b c d e f : ℝ) : Prop :=
  ∀ x y z : ℝ, x ≠ 0 ∨ y ≠ 0 ∨ z ≠ 0 → 0 < quad3 a b c d e f x y z

/-- Positive definiteness implies positive semidefiniteness, but not conversely. -/
theorem pd2_implies_psd2 {a b c : ℝ} (h : IsPD2 a b c) : IsPSD2 a b c := by
  intro x y
  by_cases hx : x = 0
  · subst x
    by_cases hy : y = 0
    · subst y
      simp [quad2]
    · exact le_of_lt (h 0 y (Or.inr hy))
  · exact le_of_lt (h x y (Or.inl hx))

/-- Positive definiteness implies positive semidefiniteness in dimension three. -/
theorem pd3_implies_psd3 {a b c d e f : ℝ} (h : IsPD3 a b c d e f) :
    IsPSD3 a b c d e f := by
  intro x y z
  by_cases hx : x = 0
  · subst x
    by_cases hy : y = 0
    · subst y
      by_cases hz : z = 0
      · subst z
        simp [quad3]
      · exact le_of_lt (h 0 0 z (Or.inr (Or.inr hz)))
    · exact le_of_lt (h 0 y z (Or.inr (Or.inl hy)))
  · exact le_of_lt (h x y z (Or.inl hx))

/-- Exact witness that PSD must not be silently strengthened to PD. -/
theorem zero_psd2_not_pd2 : IsPSD2 0 0 0 ∧ ¬ IsPD2 0 0 0 := by
  constructor
  · intro x y
    simp [quad2]
  · intro h
    have hpos := h 1 0 (Or.inl (by norm_num))
    norm_num [quad2] at hpos

/-- Exact two-by-two congruence/completion-of-squares identity. -/
theorem ldl2_identity (a b c x y : ℝ) :
    a * quad2 a b c x y = (a * x + b * y) ^ 2 + det2 a b c * y ^ 2 := by
  simp only [quad2, det2]
  ring

/-- A positive first pivot and nonnegative determinant imply two-by-two PSD. -/
theorem principal_minors_psd2
    {a b c : ℝ} (ha : 0 < a) (hdet : 0 ≤ det2 a b c) :
    IsPSD2 a b c := by
  intro x y
  have hscaled : 0 ≤ a * quad2 a b c x y := by
    rw [ldl2_identity]
    exact add_nonneg (sq_nonneg _) (mul_nonneg hdet (sq_nonneg _))
  nlinarith

/-- Strict two-by-two principal minors imply positive definiteness. -/
theorem principal_minors_pd2
    {a b c : ℝ} (ha : 0 < a) (hdet : 0 < det2 a b c) :
    IsPD2 a b c := by
  intro x y hne
  have hscaled : 0 < a * quad2 a b c x y := by
    rw [ldl2_identity]
    by_cases hy : y = 0
    · subst y
      have hx : x ≠ 0 := by simpa using hne
      have hx2 : 0 < (a * x) ^ 2 := by
        apply sq_pos_of_ne_zero
        exact mul_ne_zero (ne_of_gt ha) hx
      simpa using hx2
    · have hy2 : 0 < y ^ 2 := sq_pos_of_ne_zero hy
      have hfirst : 0 ≤ (a * x + b * y) ^ 2 := sq_nonneg _
      have hsecond : 0 < det2 a b c * y ^ 2 := mul_pos hdet hy2
      nlinarith
  nlinarith

/-- The leading two-by-two principal minor. -/
def leadingMinor2 (a b d : ℝ) : ℝ := a * d - b ^ 2

/-- Congruence identity for swapping the first two coordinates. -/
theorem quad3_swap12 (a b c d e f x y z : ℝ) :
    quad3 a b c d e f x y z = quad3 d b e a c f y x z := by
  simp only [quad3]
  ring

/-- PSD is invariant under the first coordinate transposition. -/
theorem psd3_swap12_iff (a b c d e f : ℝ) :
    IsPSD3 a b c d e f ↔ IsPSD3 d b e a c f := by
  constructor
  · intro h x y z
    rw [← quad3_swap12]
    exact h y x z
  · intro h x y z
    rw [quad3_swap12]
    exact h y x z

/-- Congruence identity for swapping the last two coordinates. -/
theorem quad3_swap23 (a b c d e f x y z : ℝ) :
    quad3 a b c d e f x y z = quad3 a c b f e d x z y := by
  simp only [quad3]
  ring

/-- PSD is invariant under the last coordinate transposition. -/
theorem psd3_swap23_iff (a b c d e f : ℝ) :
    IsPSD3 a b c d e f ↔ IsPSD3 a c b f e d := by
  constructor
  · intro h x y z
    rw [← quad3_swap23]
    exact h x z y
  · intro h x y z
    rw [quad3_swap23]
    exact h x z y

/-- A packet with duplicate first two rows/columns reduces exactly to a
single two-node packet. -/
theorem duplicate12_quad3 (a g h x y z : ℝ) :
    quad3 a a g a g h x y z = quad2 a g h (x + y) z := by
  simp only [quad3, quad2]
  ring

/-- PSD of the reduced two-node packet implies PSD of the duplicate packet. -/
theorem duplicate12_psd3 {a g h : ℝ} (h2 : IsPSD2 a g h) :
    IsPSD3 a a g a g h := by
  intro x y z
  rw [duplicate12_quad3]
  exact h2 (x + y) z

/-- Duplicate last two coordinates also reduce to a two-node packet. -/
theorem duplicate23_quad3 (a g h x y z : ℝ) :
    quad3 a g g h h h x y z = quad2 a g h x (y + z) := by
  simp only [quad3, quad2]
  ring

/-- PSD of the reduced packet implies PSD after duplicating the last node. -/
theorem duplicate23_psd3 {a g h : ℝ} (h2 : IsPSD2 a g h) :
    IsPSD3 a g g h h h := by
  intro x y z
  rw [duplicate23_quad3]
  exact h2 x (y + z)

/-- Exact LDL/congruence identity for a symmetric three-by-three quadratic form. -/
theorem ldl3_identity (a b c d e f x y z : ℝ) :
    a * leadingMinor2 a b d * quad3 a b c d e f x y z =
      leadingMinor2 a b d * (a * x + b * y + c * z) ^ 2 +
      (leadingMinor2 a b d * y + (a * e - b * c) * z) ^ 2 +
      a * det3 a b c d e f * z ^ 2 := by
  simp only [leadingMinor2, quad3, det3]
  ring

/-- A positive first pivot, positive leading two-by-two minor, and nonnegative
three-by-three determinant imply PSD.  This is deliberately a PSD statement:
the determinant is allowed to vanish. -/
theorem leading_principal_minors_psd3
    {a b c d e f : ℝ}
    (ha : 0 < a)
    (hminor : 0 < leadingMinor2 a b d)
    (hdet : 0 ≤ det3 a b c d e f) :
    IsPSD3 a b c d e f := by
  intro x y z
  have h1 : 0 ≤ leadingMinor2 a b d * (a * x + b * y + c * z) ^ 2 :=
    mul_nonneg (le_of_lt hminor) (sq_nonneg _)
  have h2 : 0 ≤ (leadingMinor2 a b d * y + (a * e - b * c) * z) ^ 2 :=
    sq_nonneg _
  have h3 : 0 ≤ a * det3 a b c d e f * z ^ 2 :=
    mul_nonneg (mul_nonneg (le_of_lt ha) hdet) (sq_nonneg _)
  have hscaled : 0 ≤ a * leadingMinor2 a b d * quad3 a b c d e f x y z := by
    rw [ldl3_identity]
    exact add_nonneg (add_nonneg h1 h2) h3
  nlinarith [mul_pos ha hminor]

/-- Strict positivity of all three leading pivots gives positive definiteness. -/
theorem leading_principal_minors_pd3
    {a b c d e f : ℝ}
    (ha : 0 < a)
    (hminor : 0 < leadingMinor2 a b d)
    (hdet : 0 < det3 a b c d e f) :
    IsPD3 a b c d e f := by
  intro x y z hne
  have hscale : 0 < a * leadingMinor2 a b d := mul_pos ha hminor
  have hscaled : 0 < a * leadingMinor2 a b d * quad3 a b c d e f x y z := by
    rw [ldl3_identity]
    by_cases hz : z = 0
    · subst z
      by_cases hy : y = 0
      · subst y
        have hx : x ≠ 0 := by simpa using hne
        have hx2 : 0 < (a * x) ^ 2 := by
          apply sq_pos_of_ne_zero
          exact mul_ne_zero (ne_of_gt ha) hx
        have hfirst : 0 < leadingMinor2 a b d * (a * x) ^ 2 :=
          mul_pos hminor hx2
        simpa using hfirst
      · have hy2 : 0 < (leadingMinor2 a b d * y) ^ 2 := by
          apply sq_pos_of_ne_zero
          exact mul_ne_zero (ne_of_gt hminor) hy
        have hfirst : 0 ≤ leadingMinor2 a b d * (a * x + b * y) ^ 2 :=
          mul_nonneg (le_of_lt hminor) (sq_nonneg _)
        nlinarith
    · have hz2 : 0 < z ^ 2 := sq_pos_of_ne_zero hz
      have hthird : 0 < a * det3 a b c d e f * z ^ 2 :=
        mul_pos (mul_pos ha hdet) hz2
      have hfirst : 0 ≤ leadingMinor2 a b d * (a * x + b * y + c * z) ^ 2 :=
        mul_nonneg (le_of_lt hminor) (sq_nonneg _)
      have hsecond : 0 ≤ (leadingMinor2 a b d * y + (a * e - b * c) * z) ^ 2 :=
        sq_nonneg _
      nlinarith
  nlinarith

end RiemannFormal.Operator
