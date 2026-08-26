import RiemannFormal.Operator.PickAlgebra

namespace RiemannFormal.Operator

/-- Positive nodes are determined by their squares. -/
theorem positive_node_eq_of_sq_eq {x y : ℝ}
    (hx : 0 < x) (hy : 0 < y) (hxy : x ^ 2 = y ^ 2) : x = y := by
  have hsum : x + y ≠ 0 := ne_of_gt (add_pos hx hy)
  have hprod : (x - y) * (x + y) = 0 := by
    nlinarith
  rcases mul_eq_zero.mp hprod with hdiff | hsum0
  · linarith
  · exact (hsum hsum0).elim

/-- The Pick kernel evaluates to the function value on the diagonal. -/
theorem pickEntry_self {x p : ℝ} (hx : x ≠ 0) :
    pickEntry x p x p = p := by
  unfold pickEntry
  have hden : x + x ≠ 0 := by
    intro h
    apply hx
    linarith
  apply (div_eq_iff hden).2
  ring

/-- Duplicate first/third rows and columns reduce to a two-dimensional form. -/
theorem duplicate13_quad3 (a g d x y z : ℝ) :
    quad3 a g a d g a x y z = quad2 a g d (x + z) y := by
  simp only [quad3, quad2]
  ring

/-- PSD of the reduced two-node packet implies PSD after duplicating the first
node in the third position. -/
theorem duplicate13_psd3 {a g d : ℝ} (h2 : IsPSD2 a g d) :
    IsPSD3 a g a d g a := by
  intro x y z
  rw [duplicate13_quad3]
  exact h2 (x + z) y

/-- Repeating the first node duplicates the first two rows/columns.  Values are
not independent data: both are evaluations of the same function. -/
theorem repeated12_pick_psd
    (p : ℝ → ℝ) {x z : ℝ} (hx : 0 < x)
    (h2 : IsPSD2 (p x) (pickEntry x (p x) z (p z)) (p z)) :
    IsPSD3 (p x) (pickEntry x (p x) x (p x))
      (pickEntry x (p x) z (p z)) (p x)
      (pickEntry x (p x) z (p z)) (p z) := by
  rw [pickEntry_self (ne_of_gt hx)]
  exact duplicate12_psd3 h2

/-- Repeating the first node in the third position is the corresponding
first/third duplicate-row congruence. -/
theorem repeated13_pick_psd
    (p : ℝ → ℝ) {x y : ℝ} (hx : 0 < x)
    (h2 : IsPSD2 (p x) (pickEntry x (p x) y (p y)) (p y)) :
    IsPSD3 (p x) (pickEntry x (p x) y (p y))
      (pickEntry x (p x) x (p x)) (p y)
      (pickEntry y (p y) x (p x)) (p x) := by
  rw [pickEntry_self (ne_of_gt hx)]
  have hsym : pickEntry y (p y) x (p x) = pickEntry x (p x) y (p y) := by
    unfold pickEntry
    rw [add_comm (y * p y) (x * p x), add_comm y x]
  rw [hsym]
  exact duplicate13_psd3 h2

/-- Repeating the last node duplicates the last two rows/columns. -/
theorem repeated23_pick_psd
    (p : ℝ → ℝ) {x y : ℝ} (hy : 0 < y)
    (h2 : IsPSD2 (p x) (pickEntry x (p x) y (p y)) (p y)) :
    IsPSD3 (p x) (pickEntry x (p x) y (p y))
      (pickEntry x (p x) y (p y)) (p y)
      (pickEntry y (p y) y (p y)) (p y) := by
  rw [pickEntry_self (ne_of_gt hy)]
  exact duplicate23_psd3 h2

end RiemannFormal.Operator
