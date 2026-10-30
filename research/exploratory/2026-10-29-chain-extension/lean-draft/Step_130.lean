/- Generated candidate assembly; UNCOMPILED and dependent on the Low/High modules. -/
import Candidate.ChainExtension.Low130
import Candidate.ChainExtension.High130
set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.ChainExtension
noncomputable section
open QRH.ArviDensity QRH.ArviDensity.Hybrid
theorem markedHigh130 : ∃ r : ℝ, 0 < r ∧ ∀ v, 0 ≤ v → v ≤ (1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) → ∀ ν,
    dens (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v ≤ ν → ν ≤ 3 / 4 →
      r ≤ highJ (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (width (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) v) (sel (401 / 1000 : ℝ) (51 / 100 : ℝ) v) ν +
        QRH.RepeatedMarks.Source.gainC ν (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ)
          (width (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) v - sel (401 / 1000 : ℝ) (51 / 100 : ℝ) v) (packed (401 / 1000 : ℝ) (51 / 100 : ℝ) v) :=
  Reflect.high_marked_of_checks High130.stepQ (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (by norm_num [High130.stepQ]) (169 / 10000)
    (by rw [Low130.cross_eq]; norm_num) (by norm_num) (by norm_num [High130.stepQ]) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (fun v h0 _ => Low130.x_pos v h0) (fun v h0 _ => Low130.E_pos v h0) Low130.unifQLower Low130.unifQUpper Low130.unifRetainedWidth Low130.unifHLower
    100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 5 10000000000000000000000000000000000000000 10000000000000000000000000000000000000000 20000000000000000000000000000000000000000000 10000000000000000000000000000000000000000 10000000000000000000000000000000000000000 20000000000000000000000000000000000000000000
    High130.tree00 High130.tree01 High130.tree02 High130.tree10 High130.tree11 High130.tree12
    High130.check00 High130.check01 High130.check02 High130.check10 High130.check11 High130.check12
theorem hybridGatesM_Step_130 :
    HybridGatesM (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) where
  width_pos := by rw [Low130.cross_eq]; norm_num
  sel_den_pos := fun v h0 _ => Low130.x_pos v h0
  dens_den_pos := fun v h0 _ => Low130.E_pos v h0
  low_identity := fun v h0 _ =>
    lowDefect_eq _ _ _ _ _ v (Low130.x_pos v h0).ne' (Low130.E_pos v h0).ne'
  low_div_eq := fun v h0 _ =>
    lowDefect_div_eq _ _ _ _ _ v h0.ne' (Low130.x_pos v h0.le).ne' (Low130.E_pos v h0.le).ne'
  sel_hasDerivAt := fun v h0 _ => sel_hasDerivAt _ _ v (Low130.x_pos v h0).ne'
  q_lower := Low130.unifQLower
  q_upper := Low130.unifQUpper
  q_floor := Low130.unifQFloor
  H_lower := Low130.unifHLower
  retained_cap := Low130.unifRetainedCap
  retained_width := Low130.unifRetainedWidth
  low_per_excess_width := Low130.unifLowPerWidth
  principal_reference := Low130.unifPrincipal
  second_reference := Low130.unifSecondRef
  second_diagonal := Low130.unifSecondDiag
  reference_upper_positive := Low130.unifRefUpper
  selection_monotonicity := Low130.unifSelDeriv
  high_marked := markedHigh130
end
end QRH.ArviDensity.ChainExtension
