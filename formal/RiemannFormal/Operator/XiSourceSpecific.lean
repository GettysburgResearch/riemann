import RiemannFormal.Operator.ReciprocalConcavity
import RiemannFormal.Operator.XiExternalInputs

namespace RiemannFormal.Operator

noncomputable section

open ChallengeDeps.XiPickOrderThreeConditional
open scoped BigOperators

/-- Local kernel-facing version of one reflected off-line orbit. -/
def sourceOffLineJet (o : ReflectedOffLineOrbit) (t : ℝ) : Jet2 :=
  Jet2.offLineJet (o.multiplicity : ℝ) (orbitU o t) (orbitB o)

/-- One coefficient unit of the selected low critical orbit. -/
def sourceCriticalUnitJet (reserve : SelectedCriticalReserve) (t : ℝ) : Jet2 :=
  Jet2.criticalJet (t + reserveRadius reserve)

/-- The positive defect magnitude of one reflected off-line orbit. -/
def orbitDefect (o : ReflectedOffLineOrbit) (t : ℝ) : ℝ :=
  32 * (o.multiplicity : ℝ) ^ 2 * orbitB o ^ 2 /
    (orbitU o t ^ 2 + orbitB o ^ 2) ^ 3

/-- Complete pointwise domain used by the reviewed source-specific one-orbit
calculation.  These are mathematical inequalities, not an opaque
`PaymentWorks` premise. -/
structure ReviewedOneOrbitDomain
    (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) (t : ℝ) : Prop where
  t_gt_quarter : 1 / 4 < t
  gap_pos : 0 < orbitGap reserve o
  u_pos : 0 < orbitU o t
  s_pos : 0 < orbitS reserve o t
  s_lt_one : orbitS reserve o t < 1
  kappa_nonnegative : 0 ≤ orbitKappa reserve o
  kappa_lt_half : orbitKappa reserve o < 1 / 2
  kappa_le_nine_quarter_b2 :
    orbitKappa reserve o ≤ 9 / (4 * o.b ^ 2)

/-- The exact published height is positive. -/
theorem verifiedHeight_pos : 0 < verifiedHeight := by
  norm_num [verifiedHeight, verifiedHeightNat]

/-- A deliberately coarse exact numerical inequality used in the reviewed
high-orbit estimate. -/
theorem verifiedHeight_sq_ge_three : 3 ≤ verifiedHeight ^ 2 := by
  norm_num [verifiedHeight, verifiedHeightNat]

/-- The selected low critical reserve has squared ordinate at most `H*^2/4`. -/
theorem reserveRadius_le_height_sq_div_four
    (reserve : SelectedCriticalReserve) :
    reserveRadius reserve ≤ verifiedHeight ^ 2 / 4 := by
  have hgamma0 : 0 ≤ reserve.orbit.gamma := le_of_lt reserve.orbit.gamma_pos
  have hH0 : 0 ≤ verifiedHeight := le_of_lt verifiedHeight_pos
  have hgammaUpper := reserve.gamma_le_half_height
  unfold reserveRadius
  nlinarith [sq_nonneg (verifiedHeight / 2 - reserve.orbit.gamma)]

/-- The reviewed geometric hypotheses imply the decisive lower bound
`c-r ≥ (2/3)b²`; it is not installed as a payment premise. -/
theorem orbitGap_ge_two_thirds_b_sq
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit) :
    (2 / 3 : ℝ) * o.b ^ 2 ≤ orbitGap reserve o := by
  have ha2 : o.a ^ 2 < 1 / 4 := by
    nlinarith [o.a_pos, o.a_lt_half, sq_nonneg (o.a - 1 / 2)]
  have hbH : verifiedHeight < o.b := o.b_above_verified
  have hH0 : 0 < verifiedHeight := verifiedHeight_pos
  have hb2 : verifiedHeight ^ 2 ≤ o.b ^ 2 := by
    nlinarith [sq_nonneg (o.b - verifiedHeight)]
  have hr := reserveRadius_le_height_sq_div_four reserve
  have hH3 := verifiedHeight_sq_ge_three
  unfold orbitGap orbitC
  nlinarith

/-- The reflected-orbit numerator satisfies `B²<b²` because `0<a<1/2`. -/
theorem orbitB_sq_lt_b_sq (o : ReflectedOffLineOrbit) :
    orbitB o ^ 2 < o.b ^ 2 := by
  have ha : 0 < 1 - 4 * o.a ^ 2 := by
    nlinarith [o.a_pos, o.a_lt_half, sq_nonneg (o.a - 1 / 2)]
  have hb : 0 < o.b := lt_trans verifiedHeight_pos o.b_above_verified
  have hprod : 0 < (1 - 4 * o.a ^ 2) * o.b ^ 2 :=
    mul_pos ha (sq_pos_of_pos hb)
  unfold orbitB
  nlinarith

/-- The source geometry proves the high-orbit kappa bound used by L-92101. -/
theorem orbitKappa_le_nine_quarter_b_sq
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit) :
    orbitKappa reserve o ≤ 9 / (4 * o.b ^ 2) := by
  have hb : 0 < o.b := lt_trans verifiedHeight_pos o.b_above_verified
  have hb2 : 0 < o.b ^ 2 := sq_pos_of_pos hb
  have hgap := orbitGap_ge_two_thirds_b_sq reserve o
  have hgap0 : 0 < orbitGap reserve o := by
    have : 0 < (2 / 3 : ℝ) * o.b ^ 2 := mul_pos (by norm_num) hb2
    linarith
  have hB : orbitB o ^ 2 ≤ o.b ^ 2 := le_of_lt (orbitB_sq_lt_b_sq o)
  have hlower0 : 0 ≤ (2 / 3 : ℝ) * o.b ^ 2 := by positivity
  have hsqProduct :
      0 ≤ (orbitGap reserve o - (2 / 3 : ℝ) * o.b ^ 2) *
        (orbitGap reserve o + (2 / 3 : ℝ) * o.b ^ 2) :=
    mul_nonneg (sub_nonneg.mpr hgap)
      (add_nonneg (le_of_lt hgap0) hlower0)
  have hgapSq :
      ((2 / 3 : ℝ) * o.b ^ 2) ^ 2 ≤ orbitGap reserve o ^ 2 := by
    nlinarith
  unfold orbitKappa
  apply (div_le_div_iff₀ (sq_pos_of_pos hgap0)
    (mul_pos (by norm_num) hb2)).2
  have hleft : 4 * o.b ^ 2 * orbitB o ^ 2 ≤ 4 * o.b ^ 2 * o.b ^ 2 :=
    mul_le_mul_of_nonneg_left hB (by positivity)
  nlinarith

/-- The same source geometry gives the strict `kappa<1/2` range. -/
theorem orbitKappa_lt_half
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit) :
    orbitKappa reserve o < 1 / 2 := by
  have hb : 0 < o.b := lt_trans verifiedHeight_pos o.b_above_verified
  have hb2 : 0 < o.b ^ 2 := sq_pos_of_pos hb
  have hbLarge : 9 / 2 < o.b ^ 2 := by
    have hH0 := verifiedHeight_pos
    have hH : verifiedHeight < o.b := o.b_above_verified
    have hbHsq : verifiedHeight ^ 2 < o.b ^ 2 := by
      nlinarith [sq_nonneg (o.b - verifiedHeight)]
    have hHlarge : 9 / 2 < verifiedHeight ^ 2 := by
      norm_num [verifiedHeight, verifiedHeightNat]
    linarith
  have hbound : 9 / (4 * o.b ^ 2) < 1 / 2 := by
    apply (div_lt_iff₀ (mul_pos (by norm_num) hb2)).2
    nlinarith
  exact lt_of_le_of_lt (orbitKappa_le_nine_quarter_b_sq reserve o) hbound

/-- All pointwise hypotheses of the one-orbit theorem follow from the concrete
representative convention, the selected low reserve, and `t>1/4`. -/
theorem reviewedOneOrbitDomain_of_source
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit)
    {t : ℝ} (ht : 1 / 4 < t) :
    ReviewedOneOrbitDomain reserve o t := by
  have hb : 0 < o.b := lt_trans verifiedHeight_pos o.b_above_verified
  have hr0 : 0 ≤ reserveRadius reserve := sq_nonneg _
  have hgapLower := orbitGap_ge_two_thirds_b_sq reserve o
  have hgap : 0 < orbitGap reserve o := by
    have : 0 < (2 / 3 : ℝ) * o.b ^ 2 :=
      mul_pos (by norm_num) (sq_pos_of_pos hb)
    linarith
  have hc : 0 < orbitC o := by
    unfold orbitGap at hgap
    linarith
  have hU : 0 < orbitU o t := by
    unfold orbitU
    linarith
  have hUminusGap : 0 < orbitU o t - orbitGap reserve o := by
    unfold orbitU orbitGap
    linarith
  have hs0 : 0 < orbitS reserve o t := by
    unfold orbitS
    exact div_pos hgap hU
  have hs1 : orbitS reserve o t < 1 := by
    unfold orbitS
    exact (div_lt_one hU).2 (by linarith)
  have hk0 : 0 ≤ orbitKappa reserve o := by
    unfold orbitKappa
    positivity
  exact
    { t_gt_quarter := ht
      gap_pos := hgap
      u_pos := hU
      s_pos := hs0
      s_lt_one := hs1
      kappa_nonnegative := hk0
      kappa_lt_half := orbitKappa_lt_half reserve o
      kappa_le_nine_quarter_b2 :=
        orbitKappa_le_nine_quarter_b_sq reserve o }

/-- Exact coordinate identity `V=U(1-s)`. -/
theorem orbitV_eq_U_mul_one_sub_s
    {reserve : SelectedCriticalReserve} {o : ReflectedOffLineOrbit} {t : ℝ}
    (hU : orbitU o t ≠ 0) :
    t + reserveRadius reserve =
      orbitU o t * (1 - orbitS reserve o t) := by
  unfold orbitS orbitGap orbitU orbitC reserveRadius
  field_simp [hU]
  ring

/-- Exact coordinate identity `B²=kappa*s²*U²`. -/
theorem orbitB_sq_eq_kappa_s_sq_U_sq
    {reserve : SelectedCriticalReserve} {o : ReflectedOffLineOrbit} {t : ℝ}
    (hgap : orbitGap reserve o ≠ 0)
    (hU : orbitU o t ≠ 0) :
    orbitB o ^ 2 =
      orbitKappa reserve o * orbitS reserve o t ^ 2 * orbitU o t ^ 2 := by
  unfold orbitKappa orbitS
  field_simp [hgap, hU]
  ring

/-- Algebraic cross-curvature identity in the reviewed `(U,s,kappa)`
coordinates. -/
theorem oneOrbit_cross_curvature_coordinates
    {m U B V s kappa : ℝ}
    (hU : U ≠ 0)
    (hOneSubS : 1 - s ≠ 0)
    (hOnePlus : 1 + kappa * s ^ 2 ≠ 0)
    (hV : V = U * (1 - s))
    (hB : B ^ 2 = kappa * s ^ 2 * U ^ 2) :
    Jet2.cross (Jet2.offLineJet m U B) (Jet2.criticalJet V) =
      16 * m * s ^ 2 * qKappa kappa s /
        (U ^ 4 * (1 + kappa * s ^ 2) ^ 3 * (1 - s) ^ 3) := by
  subst V
  rw [hB]
  have hden : U ^ 2 + kappa * s ^ 2 * U ^ 2 ≠ 0 := by
    have hU2 : U ^ 2 ≠ 0 := pow_ne_zero 2 hU
    have hfactor :
        U ^ 2 + kappa * s ^ 2 * U ^ 2 =
          U ^ 2 * (1 + kappa * s ^ 2) := by ring
    rw [hfactor]
    exact mul_ne_zero hU2 hOnePlus
  field_simp [Jet2.cross, Jet2.offLineJet, Jet2.criticalJet, qKappa,
    hU, hOneSubS, hOnePlus, hden]
  ring

/-- Source-specific cross curvature from L-92101, with all domain hypotheses
visible. -/
theorem reflectedOffLine_cross_curvature_exact
    {reserve : SelectedCriticalReserve} {o : ReflectedOffLineOrbit} {t : ℝ}
    (hdom : ReviewedOneOrbitDomain reserve o t) :
    Jet2.cross (sourceOffLineJet o t) (sourceCriticalUnitJet reserve t) =
      16 * (o.multiplicity : ℝ) * orbitS reserve o t ^ 2 *
        qKappa (orbitKappa reserve o) (orbitS reserve o t) /
        (orbitU o t ^ 4 *
          (1 + orbitKappa reserve o * orbitS reserve o t ^ 2) ^ 3 *
          (1 - orbitS reserve o t) ^ 3) := by
  have hU : orbitU o t ≠ 0 := ne_of_gt hdom.u_pos
  have hgap : orbitGap reserve o ≠ 0 := ne_of_gt hdom.gap_pos
  have hOneSubS : 1 - orbitS reserve o t ≠ 0 :=
    ne_of_gt (sub_pos.mpr hdom.s_lt_one)
  have hOnePlus :
      1 + orbitKappa reserve o * orbitS reserve o t ^ 2 ≠ 0 := by
    have hnonneg :
        0 ≤ orbitKappa reserve o * orbitS reserve o t ^ 2 :=
      mul_nonneg hdom.kappa_nonnegative (sq_nonneg _)
    nlinarith
  exact oneOrbit_cross_curvature_coordinates hU hOneSubS hOnePlus
    (orbitV_eq_U_mul_one_sub_s hU)
    (orbitB_sq_eq_kappa_s_sq_U_sq hgap hU)

/-- Exact negative curvature defect of the actual reflected off-line block. -/
theorem reflectedOffLine_defect_formula
    {o : ReflectedOffLineOrbit} {t : ℝ}
    (hU : orbitU o t ≠ 0) :
    Jet2.energy (sourceOffLineJet o t) = -orbitDefect o t := by
  have hden : orbitU o t ^ 2 + orbitB o ^ 2 ≠ 0 := by
    have hU2 : 0 < orbitU o t ^ 2 := sq_pos_of_ne_zero hU
    nlinarith [sq_nonneg (orbitB o)]
  simpa [sourceOffLineJet, orbitDefect] using
    (Jet2.offLineOrbit_defect_formula
      (m := (o.multiplicity : ℝ)) (U := orbitU o t) (B := orbitB o) hden)

/-- The selected unit critical orbit has zero reciprocal curvature. -/
theorem selectedCriticalUnit_energy_zero
    {reserve : SelectedCriticalReserve} {t : ℝ}
    (hV : t + reserveRadius reserve ≠ 0) :
    Jet2.energy (sourceCriticalUnitJet reserve t) = 0 := by
  simpa [sourceCriticalUnitJet] using
    (Jet2.criticalOrbit_energy_zero (V := t + reserveRadius reserve) hV)

/-- The polynomial `Q_kappa(s)` dominates `1-kappa` on the reviewed domain. -/
theorem qKappa_lower_bound
    {kappa s : ℝ}
    (hk : 0 ≤ kappa) (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    1 - kappa ≤ qKappa kappa s := by
  have htwo : 0 ≤ 2 - s := by linarith
  have hthree : 0 ≤ 3 - 2 * s := by linarith
  have hterm1 : 0 ≤ 3 * kappa * s * (2 - s) :=
    mul_nonneg (mul_nonneg (mul_nonneg (by norm_num) hk) hs0) htwo
  have hterm2 : 0 ≤ kappa ^ 2 * s ^ 2 * (3 - 2 * s) :=
    mul_nonneg (mul_nonneg (sq_nonneg kappa) (sq_nonneg s)) hthree
  unfold qKappa
  linarith

/-- Exact defect in the `(U,s,kappa)` coordinates. -/
theorem oneOrbit_defect_coordinates
    {m U B s kappa : ℝ}
    (hU : U ≠ 0)
    (hOnePlus : 1 + kappa * s ^ 2 ≠ 0)
    (hB : B ^ 2 = kappa * s ^ 2 * U ^ 2) :
    32 * m ^ 2 * B ^ 2 / (U ^ 2 + B ^ 2) ^ 3 =
      32 * m ^ 2 * kappa * s ^ 2 /
        (U ^ 4 * (1 + kappa * s ^ 2) ^ 3) := by
  rw [hB]
  have hden : U ^ 2 + kappa * s ^ 2 * U ^ 2 ≠ 0 := by
    have hU2 : U ^ 2 ≠ 0 := pow_ne_zero 2 hU
    have hfactor :
        U ^ 2 + kappa * s ^ 2 * U ^ 2 =
          U ^ 2 * (1 + kappa * s ^ 2) := by ring
    rw [hfactor]
    exact mul_ne_zero hU2 hOnePlus
  field_simp [hU, hOnePlus, hden]
  ring

/-- The reviewed choice `epsilon=2m*kappa/(1-kappa)` pays the complete local
curvature defect. -/
theorem oneOrbit_epsilon_pays_coordinates
    {m U s kappa crossValue defect : ℝ}
    (hm : 0 ≤ m) (hU : U ≠ 0)
    (hk0 : 0 ≤ kappa) (hk1 : kappa < 1)
    (hs0 : 0 < s) (hs1 : s < 1)
    (hcross : crossValue =
      16 * m * s ^ 2 * qKappa kappa s /
        (U ^ 4 * (1 + kappa * s ^ 2) ^ 3 * (1 - s) ^ 3))
    (hdefect : defect =
      32 * m ^ 2 * kappa * s ^ 2 /
        (U ^ 4 * (1 + kappa * s ^ 2) ^ 3)) :
    defect ≤ (2 * m * kappa / (1 - kappa)) * crossValue := by
  have hOneMinusK : 0 < 1 - kappa := sub_pos.mpr hk1
  have hOneMinusS : 0 < 1 - s := sub_pos.mpr hs1
  have hOnePlus : 0 < 1 + kappa * s ^ 2 := by
    nlinarith [mul_nonneg hk0 (sq_nonneg s)]
  have hU4 : 0 < U ^ 4 := by positivity
  let D : ℝ := U ^ 4 * (1 + kappa * s ^ 2) ^ 3
  have hD : 0 < D := by
    dsimp [D]
    exact mul_pos hU4 (pow_pos hOnePlus 3)
  have hsle : s ≤ 1 := le_of_lt hs1
  have hq : 1 - kappa ≤ qKappa kappa s :=
    qKappa_lower_bound hk0 (le_of_lt hs0) hsle
  have hr0 : 0 ≤ 1 - s := le_of_lt hOneMinusS
  have hr1 : 1 - s ≤ 1 := by linarith
  have hr_sq : (1 - s) ^ 2 ≤ 1 := by
    have hprod : 0 ≤ (1 - s) * (1 - (1 - s)) :=
      mul_nonneg hr0 (sub_nonneg.mpr hr1)
    nlinarith
  have hr_cube : (1 - s) ^ 3 ≤ 1 := by
    calc
      (1 - s) ^ 3 = (1 - s) ^ 2 * (1 - s) := by ring
      _ ≤ 1 * (1 - s) := mul_le_mul_of_nonneg_right hr_sq hr0
      _ ≤ 1 := by linarith
  have hdenSmall : D * (1 - s) ^ 3 ≤ D := by
    have hnonneg := mul_nonneg (le_of_lt hD) (sub_nonneg.mpr hr_cube)
    nlinarith
  have hdenSmallPos : 0 < D * (1 - s) ^ 3 :=
    mul_pos hD (pow_pos hOneMinusS 3)
  have hfrac :
      (1 - kappa) / D ≤
        qKappa kappa s / (D * (1 - s) ^ 3) := by
    apply (div_le_div_iff₀ hD hdenSmallPos).2
    calc
      (1 - kappa) * (D * (1 - s) ^ 3)
          ≤ (1 - kappa) * D :=
        mul_le_mul_of_nonneg_left hdenSmall (le_of_lt hOneMinusK)
      _ ≤ qKappa kappa s * D :=
        mul_le_mul_of_nonneg_right hq (le_of_lt hD)
  have hfactor : 0 ≤ 16 * m * s ^ 2 :=
    mul_nonneg (mul_nonneg (by norm_num) hm) (sq_nonneg s)
  have hlower :
      16 * m * s ^ 2 * ((1 - kappa) / D) ≤ crossValue := by
    rw [hcross]
    have hmul := mul_le_mul_of_nonneg_left hfrac hfactor
    simpa [D, mul_assoc] using hmul
  have hepsilon : 0 ≤ 2 * m * kappa / (1 - kappa) :=
    div_nonneg (mul_nonneg (mul_nonneg (by norm_num) hm) hk0)
      (le_of_lt hOneMinusK)
  have hmul := mul_le_mul_of_nonneg_left hlower hepsilon
  calc
    defect =
        (2 * m * kappa / (1 - kappa)) *
          (16 * m * s ^ 2 * ((1 - kappa) / D)) := by
      rw [hdefect]
      field_simp [D, ne_of_gt hOneMinusK, ne_of_gt hD]
      ring
    _ ≤ (2 * m * kappa / (1 - kappa)) * crossValue := hmul

/-- Under the reviewed high-orbit bound, the exact reserve share is at most
`9m/b²`. -/
theorem orbitEpsilon_le_nine_mul_tail
    {reserve : SelectedCriticalReserve} {o : ReflectedOffLineOrbit} {t : ℝ}
    (hdom : ReviewedOneOrbitDomain reserve o t) :
    orbitEpsilon reserve o ≤ 9 * orbitTail o := by
  let m : ℝ := o.multiplicity
  let kappa : ℝ := orbitKappa reserve o
  have hm : 0 ≤ m := by positivity
  have hk0 : 0 ≤ kappa := hdom.kappa_nonnegative
  have hkHalf : kappa ≤ 1 / 2 := le_of_lt hdom.kappa_lt_half
  have hden : 0 < 1 - kappa := by linarith
  have hfirst : 2 * m * kappa / (1 - kappa) ≤ 4 * m * kappa := by
    apply (div_le_iff₀ hden).2
    have hmk : 0 ≤ 2 * m * kappa := by positivity
    have hfactor : 0 ≤ 1 - 2 * kappa := by linarith
    have hproduct : 0 ≤ (2 * m * kappa) * (1 - 2 * kappa) :=
      mul_nonneg hmk hfactor
    nlinarith
  have hb : o.b ≠ 0 := by
    have hH : 0 < verifiedHeight := by
      norm_num [verifiedHeight, verifiedHeightNat]
    exact ne_of_gt (lt_trans hH o.b_above_verified)
  have hsecond : 4 * m * kappa ≤ 9 * m / o.b ^ 2 := by
    have h := mul_le_mul_of_nonneg_left hdom.kappa_le_nine_quarter_b2
      (show 0 ≤ 4 * m by positivity)
    calc
      4 * m * kappa ≤ 4 * m * (9 / (4 * o.b ^ 2)) := h
      _ = 9 * m / o.b ^ 2 := by field_simp [hb]; ring
  calc
    orbitEpsilon reserve o = 2 * m * kappa / (1 - kappa) := rfl
    _ ≤ 4 * m * kappa := hfirst
    _ ≤ 9 * m / o.b ^ 2 := hsecond
    _ = 9 * orbitTail o := by simp [orbitTail, m]; ring

/-- The trusted comparator-side payment predicate and the local kernel-side
energy statement are definitionally the same scalar inequality. -/
theorem oneOrbitPaid_iff_local
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit) (t : ℝ) :
    OneOrbitPaid reserve o t ↔
      0 ≤ Jet2.energy (Jet2.add (sourceOffLineJet o t)
        (Jet2.smul (orbitEpsilon reserve o)
          (sourceCriticalUnitJet reserve t))) := by
  rfl

/-- The source-specific one-orbit theorem: exact defect, exact cross curvature,
reviewed epsilon, `epsilon <= 9m/b²`, and paid reciprocal curvature. -/
theorem reflectedOffLineOrbit_absorbed
    {reserve : SelectedCriticalReserve} {o : ReflectedOffLineOrbit} {t : ℝ}
    (hdom : ReviewedOneOrbitDomain reserve o t) :
    orbitEpsilon reserve o ≤ 9 * orbitTail o ∧
      OneOrbitPaid reserve o t := by
  have hU : orbitU o t ≠ 0 := ne_of_gt hdom.u_pos
  have hgap : orbitGap reserve o ≠ 0 := ne_of_gt hdom.gap_pos
  have hV : t + reserveRadius reserve ≠ 0 := by
    have hr : 0 ≤ reserveRadius reserve := sq_nonneg _
    nlinarith [hdom.t_gt_quarter]
  have hOnePlus :
      1 + orbitKappa reserve o * orbitS reserve o t ^ 2 ≠ 0 := by
    have hnonneg :
        0 ≤ orbitKappa reserve o * orbitS reserve o t ^ 2 :=
      mul_nonneg hdom.kappa_nonnegative (sq_nonneg _)
    nlinarith
  have hcross := reflectedOffLine_cross_curvature_exact hdom
  have hdefCoordinates := oneOrbit_defect_coordinates
    (m := (o.multiplicity : ℝ)) (U := orbitU o t) (B := orbitB o)
    (s := orbitS reserve o t) (kappa := orbitKappa reserve o)
    hU hOnePlus (orbitB_sq_eq_kappa_s_sq_U_sq hgap hU)
  have hpay :
      orbitDefect o t ≤ orbitEpsilon reserve o *
        Jet2.cross (sourceOffLineJet o t) (sourceCriticalUnitJet reserve t) := by
    apply oneOrbit_epsilon_pays_coordinates
      (m := (o.multiplicity : ℝ)) (U := orbitU o t)
      (s := orbitS reserve o t) (kappa := orbitKappa reserve o)
      (crossValue := Jet2.cross (sourceOffLineJet o t)
        (sourceCriticalUnitJet reserve t))
      (defect := orbitDefect o t)
    · positivity
    · exact hU
    · exact hdom.kappa_nonnegative
    · linarith [hdom.kappa_lt_half]
    · exact hdom.s_pos
    · exact hdom.s_lt_one
    · exact hcross
    · simpa [orbitDefect] using hdefCoordinates
  have hlocal :
      0 ≤ Jet2.energy (Jet2.add (sourceOffLineJet o t)
        (Jet2.smul (orbitEpsilon reserve o) (sourceCriticalUnitJet reserve t))) :=
    Jet2.oneOrbitAbsorption
      (reflectedOffLine_defect_formula hU)
      (selectedCriticalUnit_energy_zero hV) hpay
  constructor
  · exact orbitEpsilon_le_nine_mul_tail hdom
  · exact (oneOrbitPaid_iff_local reserve o t).2 hlocal

/-- Source-specific theorem under only the reviewed orbit/reserve
assumptions; no kappa/payment inequality is supplied by the caller. -/
theorem reflectedOffLineOrbit_absorbed_reviewed
    (reserve : SelectedCriticalReserve) (o : ReflectedOffLineOrbit)
    {t : ℝ} (ht : 1 / 4 < t) :
    orbitEpsilon reserve o ≤ 9 * orbitTail o ∧ OneOrbitPaid reserve o t :=
  reflectedOffLineOrbit_absorbed
    (reviewedOneOrbitDomain_of_source reserve o ht)

/-- Exact external inputs needed to construct the global one-use reserve
allocation. -/
structure ReserveTailInputs
    (grouped : GroupedActualXiC2Expansion) : Prop where
  reciprocalSquareTail :
    ∀ N : ℕ,
      (∑ i ∈ Finset.range N, orbitTail (grouped.offLineEnumeration i)) ≤
        2 * (Real.log verifiedHeight + 1) / verifiedHeight
  numericalBudget :
    18 * (Real.log verifiedHeight + 1) / verifiedHeight < 1

/-- Construct the exact finite-prefix global reserve ledger. Every share is
nonnegative, every orbit is paid, total use is at most one, and the leftover is
nonnegative and used exactly once. -/
theorem buildActualXiReserveAllocation
    {grouped : GroupedActualXiC2Expansion}
    (inputs : ReserveTailInputs grouped) :
    ActualXiReserveAllocation grouped := by
  let share : ℕ → ℝ := fun i =>
    orbitEpsilon grouped.selectedReserve (grouped.offLineEnumeration i)
  let leftover : ℕ → ℝ := fun N => 1 - ∑ i ∈ Finset.range N, share i
  have hshareNonnegative : ∀ i : ℕ, 0 ≤ share i := by
    intro i
    have hdom := reviewedOneOrbitDomain_of_source grouped.selectedReserve
      (grouped.offLineEnumeration i) (by norm_num)
    have hden : 0 < 1 - orbitKappa grouped.selectedReserve
        (grouped.offLineEnumeration i) := by
      linarith [hdom.kappa_lt_half]
    dsimp [share, orbitEpsilon]
    positivity
  have htailNonnegative :
      ∀ i : ℕ, 0 ≤ orbitTail (grouped.offLineEnumeration i) := by
    intro i
    unfold orbitTail
    positivity
  have hshareLe :
      ∀ i : ℕ, share i ≤ 9 * orbitTail (grouped.offLineEnumeration i) := by
    intro i
    simpa [share] using
      orbitEpsilon_le_nine_mul_tail
        (reviewedOneOrbitDomain_of_source grouped.selectedReserve
          (grouped.offLineEnumeration i) (by norm_num))
  have htotal : ∀ N : ℕ, (∑ i ∈ Finset.range N, share i) ≤ 1 := by
    intro N
    have hsum :
        (∑ i ∈ Finset.range N, share i) ≤
          ∑ i ∈ Finset.range N,
            9 * orbitTail (grouped.offLineEnumeration i) :=
      Finset.sum_le_sum fun i _ => hshareLe i
    have hscale :
        (∑ i ∈ Finset.range N,
          9 * orbitTail (grouped.offLineEnumeration i)) =
          9 * ∑ i ∈ Finset.range N,
            orbitTail (grouped.offLineEnumeration i) := by
      rw [Finset.mul_sum]
    rw [hscale] at hsum
    have htail := inputs.reciprocalSquareTail N
    nlinarith [inputs.numericalBudget]
  refine
    { share := share
      share_eq := ?_
      share_nonnegative := hshareNonnegative
      tail_nonnegative := htailNonnegative
      share_le_nine_tail := hshareLe
      reciprocalSquareTail := inputs.reciprocalSquareTail
      numericalBudget := inputs.numericalBudget
      everyOrbitPaid := ?_
      totalShare_le_one := htotal
      leftover := leftover
      leftover_eq := ?_
      leftover_nonnegative := ?_
      oneUse := ?_ }
  · intro i
    rfl
  · intro i t ht
    exact (reflectedOffLineOrbit_absorbed_reviewed grouped.selectedReserve
      (grouped.offLineEnumeration i) ht).2
  · intro N
    rfl
  · intro N
    dsimp [leftover]
    nlinarith [htotal N]
  · intro N
    dsimp [leftover]
    ring

/-- Source-locked existence wrapper for the canonical critical-reserve semantic
node.  The external theorem lock is returned alongside existence of an exact
one-use allocation; `buildActualXiReserveAllocation` remains the concrete
data-producing API. -/
theorem buildLockedActualXiReserveAllocation
    {grouped : GroupedActualXiC2Expansion}
    (verified : PublishedVerifiedHeightTheorem)
    (inputs : ReserveTailInputs grouped) :
    SourceLockExact verified.sourceLock ∧
      Nonempty (ActualXiReserveAllocation grouped) :=
  ⟨verified.sourceLockExact, ⟨buildActualXiReserveAllocation inputs⟩⟩

end

end RiemannFormal.Operator
