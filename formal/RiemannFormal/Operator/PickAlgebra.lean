import RiemannFormal.Operator.FiniteMatrix

namespace RiemannFormal.Operator

/-- Off-diagonal entry of the finite infinitesimal Pick packet after writing
`F(x)=x p(x^2)`. -/
def pickEntry (x p y q : ℝ) : ℝ := (x * p + y * q) / (x + y)

/-- Exact two-node determinant. -/
def pickDet2 (x p y q : ℝ) : ℝ := p * q - pickEntry x p y q ^ 2

/-- Exact two-point Pick identity from `L-92000.4`. -/
theorem two_point_pick_identity
    {x y p q : ℝ} (hxy : x + y ≠ 0) :
    pickDet2 x p y q =
      -((p - q) * (x ^ 2 * p - y ^ 2 * q)) / (x + y) ^ 2 := by
  field_simp [pickDet2, pickEntry, hxy]
  ring

/-- The two-node determinant is nonnegative under the two scalar monotonicities
used by the reviewed Xi argument. -/
theorem two_point_pick_nonnegative
    {x y p q : ℝ}
    (hp : q ≤ p)
    (htp : x ^ 2 * p ≤ y ^ 2 * q)
    (hxy : x + y ≠ 0) :
    0 ≤ pickDet2 x p y q := by
  rw [two_point_pick_identity hxy]
  apply div_nonneg
  · nlinarith
  · exact sq_nonneg _

/-- Three-node Vandermonde factor in the squared node variables. -/
def delta3 (t1 t2 t3 : ℝ) : ℝ :=
  (t2 - t1) * (t3 - t1) * (t3 - t2)

/-- Second divided difference in barycentric form. -/
def secondDivDiff (t1 t2 t3 y1 y2 y3 : ℝ) : ℝ :=
  y1 / ((t1 - t2) * (t1 - t3)) +
  y2 / ((t2 - t1) * (t2 - t3)) +
  y3 / ((t3 - t1) * (t3 - t2))

/-- Second divided differences are linear in the sampled values. -/
theorem secondDivDiff_add
    {t1 t2 t3 a1 a2 a3 b1 b2 b3 : ℝ} :
    secondDivDiff t1 t2 t3 (a1 + b1) (a2 + b2) (a3 + b3) =
      secondDivDiff t1 t2 t3 a1 a2 a3 +
        secondDivDiff t1 t2 t3 b1 b2 b3 := by
  simp [secondDivDiff]
  ring

/-- Finite positive sums preserve a nonpositive companion curvature. -/
theorem secondDivDiff_add_nonpositive
    {t1 t2 t3 a1 a2 a3 b1 b2 b3 : ℝ}
    (ha : secondDivDiff t1 t2 t3 a1 a2 a3 ≤ 0)
    (hb : secondDivDiff t1 t2 t3 b1 b2 b3 ≤ 0) :
    secondDivDiff t1 t2 t3 (a1 + b1) (a2 + b2) (a3 + b3) ≤ 0 := by
  rw [secondDivDiff_add]
  linarith

/-- The first irreducible factor in the three-node Pick determinant. -/
def pickFactorA (t1 t2 t3 p1 p2 p3 : ℝ) : ℝ :=
  p1 * p2 * (t1 - t2) - p1 * p3 * (t1 - t3) +
    p2 * p3 * (t2 - t3)

/-- The companion-curvature factor in the three-node Pick determinant. -/
def pickFactorB (t1 t2 t3 p1 p2 p3 : ℝ) : ℝ :=
  t1 * p1 * (t2 - t3) + t2 * p2 * (t3 - t1) +
    t3 * p3 * (t1 - t2)

/-- Positive denominator appearing in the three-node factorization. -/
def pickDenominator3 (x1 x2 x3 : ℝ) : ℝ :=
  (x1 + x2) ^ 2 * (x1 + x3) ^ 2 * (x2 + x3) ^ 2

/-- Determinant of the symmetric three-node Pick packet. -/
def pickDet3 (x1 x2 x3 p1 p2 p3 : ℝ) : ℝ :=
  det3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
    p2 (pickEntry x2 p2 x3 p3) p3

/-- Direct determinant expansion into the two irreducible scalar factors. -/
theorem pickDet3_factorAB
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (h12 : x1 + x2 ≠ 0)
    (h13 : x1 + x3 ≠ 0)
    (h23 : x2 + x3 ≠ 0) :
    pickDet3 x1 x2 x3 p1 p2 p3 =
      pickFactorA (x1 ^ 2) (x2 ^ 2) (x3 ^ 2) p1 p2 p3 *
        pickFactorB (x1 ^ 2) (x2 ^ 2) (x3 ^ 2) p1 p2 p3 /
        pickDenominator3 x1 x2 x3 := by
  field_simp [pickDet3, pickEntry, pickFactorA, pickFactorB,
    pickDenominator3, det3, h12, h13, h23]
  ring

/-- The reciprocal-curvature factor is exactly a second divided difference. -/
theorem pickFactorA_divided_difference
    {t1 t2 t3 p1 p2 p3 : ℝ}
    (ht12 : t1 ≠ t2) (ht13 : t1 ≠ t3) (ht23 : t2 ≠ t3)
    (hp1 : p1 ≠ 0) (hp2 : p2 ≠ 0) (hp3 : p3 ≠ 0) :
    pickFactorA t1 t2 t3 p1 p2 p3 =
      -p1 * p2 * p3 * delta3 t1 t2 t3 *
        secondDivDiff t1 t2 t3 (1 / p1) (1 / p2) (1 / p3) := by
  field_simp [pickFactorA, delta3, secondDivDiff, ht12, ht13, ht23,
    hp1, hp2, hp3]
  ring

/-- The companion `t p(t)` curvature is the second determinant factor. -/
theorem pickFactorB_divided_difference
    {t1 t2 t3 p1 p2 p3 : ℝ}
    (ht12 : t1 ≠ t2) (ht13 : t1 ≠ t3) (ht23 : t2 ≠ t3) :
    pickFactorB t1 t2 t3 p1 p2 p3 =
      -delta3 t1 t2 t3 *
        secondDivDiff t1 t2 t3 (t1 * p1) (t2 * p2) (t3 * p3) := by
  field_simp [pickFactorB, delta3, secondDivDiff, ht12, ht13, ht23]
  ring

/-- Exact reviewed three-node determinant factorization. -/
theorem three_node_pick_determinant_identity
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (h12 : x1 + x2 ≠ 0) (h13 : x1 + x3 ≠ 0) (h23 : x2 + x3 ≠ 0)
    (ht12 : x1 ^ 2 ≠ x2 ^ 2) (ht13 : x1 ^ 2 ≠ x3 ^ 2)
    (ht23 : x2 ^ 2 ≠ x3 ^ 2)
    (hp1 : p1 ≠ 0) (hp2 : p2 ≠ 0) (hp3 : p3 ≠ 0) :
    pickDet3 x1 x2 x3 p1 p2 p3 =
      (p1 * p2 * p3 * delta3 (x1 ^ 2) (x2 ^ 2) (x3 ^ 2) ^ 2 /
        pickDenominator3 x1 x2 x3) *
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
        (1 / p1) (1 / p2) (1 / p3) *
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
        (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) := by
  rw [pickDet3_factorAB h12 h13 h23]
  rw [pickFactorA_divided_difference ht12 ht13 ht23 hp1 hp2 hp3]
  rw [pickFactorB_divided_difference ht12 ht13 ht23]
  ring

/-- Two nonpositive scalar curvatures make the three-node determinant
nonnegative.  The theorem is only a determinant statement; PSD still requires
the one- and two-node principal minors. -/
theorem three_node_pick_det_nonnegative
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (hx1 : 0 < x1) (hx2 : 0 < x2) (hx3 : 0 < x3)
    (hp1 : 0 < p1) (hp2 : 0 < p2) (hp3 : 0 < p3)
    (ht12 : x1 ^ 2 ≠ x2 ^ 2) (ht13 : x1 ^ 2 ≠ x3 ^ 2)
    (ht23 : x2 ^ 2 ≠ x3 ^ 2)
    (hrecip : secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (1 / p1) (1 / p2) (1 / p3) ≤ 0)
    (hcomp : secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
      (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) ≤ 0) :
    0 ≤ pickDet3 x1 x2 x3 p1 p2 p3 := by
  have h12 : x1 + x2 ≠ 0 := by positivity
  have h13 : x1 + x3 ≠ 0 := by positivity
  have h23 : x2 + x3 ≠ 0 := by positivity
  rw [three_node_pick_determinant_identity h12 h13 h23 ht12 ht13 ht23
    (ne_of_gt hp1) (ne_of_gt hp2) (ne_of_gt hp3)]
  have hpref : 0 ≤
      p1 * p2 * p3 * delta3 (x1 ^ 2) (x2 ^ 2) (x3 ^ 2) ^ 2 /
        pickDenominator3 x1 x2 x3 := by
    positivity
  have hcurv : 0 ≤
      secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (1 / p1) (1 / p2) (1 / p3) *
        secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (x1 ^ 2 * p1) (x2 ^ 2 * p2) (x3 ^ 2 * p3) :=
    mul_nonneg_of_nonpos_of_nonpos hrecip hcomp
  exact mul_nonneg hpref hcurv

/-- Principal-minor implication for a three-node packet.  A strict two-node
pivot plus a nonnegative three-node determinant yields PSD, not necessarily PD. -/
theorem three_node_pick_psd_of_principal_minors
    {x1 x2 x3 p1 p2 p3 : ℝ}
    (hp1 : 0 < p1)
    (hminor12 : 0 < pickDet2 x1 p1 x2 p2)
    (hdet3 : 0 ≤ pickDet3 x1 x2 x3 p1 p2 p3) :
    IsPSD3 p1 (pickEntry x1 p1 x2 p2) (pickEntry x1 p1 x3 p3)
      p2 (pickEntry x2 p2 x3 p3) p3 := by
  apply leading_principal_minors_psd3 hp1
  · simpa [leadingMinor2, pickDet2] using hminor12
  · simpa [pickDet3] using hdet3

end RiemannFormal.Operator
