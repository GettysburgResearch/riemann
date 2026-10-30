/- Generated candidate assembly; UNCOMPILED and dependent on the Low/High modules. -/
import Candidate.ChainExtension.Low131
import Candidate.ChainExtension.High131
set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.ChainExtension
noncomputable section
open QRH.ArviDensity QRH.ArviDensity.Hybrid
theorem markedHigh131 : ∃ r : ℝ, 0 < r ∧ ∀ v, 0 ≤ v → v ≤ (1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) → ∀ ν,
    dens (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v ≤ ν → ν ≤ 3 / 4 →
      r ≤ highJ (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (width (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) v) (sel (2 / 5 : ℝ) (1 / 10 : ℝ) v) ν +
        QRH.RepeatedMarks.Source.gainC ν (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ)
          (width (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) v - sel (2 / 5 : ℝ) (1 / 10 : ℝ) v) (packed (2 / 5 : ℝ) (1 / 10 : ℝ) v) :=
  Reflect.high_marked_of_checks High131.stepQ (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (by norm_num [High131.stepQ]) (21 / 1250)
    (by rw [Low131.cross_eq]; norm_num) (by norm_num) (by norm_num [High131.stepQ]) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (fun v h0 _ => Low131.x_pos v h0) (fun v h0 _ => Low131.E_pos v h0) Low131.unifQLower Low131.unifQUpper Low131.unifRetainedWidth Low131.unifHLower
    100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 5 78125000000000000000000000000000000 78125000000000000000000000000000000 976562500000000000000000000000000000000 78125000000000000000000000000000000 78125000000000000000000000000000000 976562500000000000000000000000000000000
    High131.tree00 High131.tree01 High131.tree02 High131.tree10 High131.tree11 High131.tree12
    High131.check00 High131.check01 High131.check02 High131.check10 High131.check11 High131.check12
theorem hybridGatesM_Step_131 :
    HybridGatesM (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (1 / 10 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) where
  width_pos := by rw [Low131.cross_eq]; norm_num
  sel_den_pos := fun v h0 _ => Low131.x_pos v h0
  dens_den_pos := fun v h0 _ => Low131.E_pos v h0
  low_identity := fun v h0 _ =>
    lowDefect_eq _ _ _ _ _ v (Low131.x_pos v h0).ne' (Low131.E_pos v h0).ne'
  low_div_eq := fun v h0 _ =>
    lowDefect_div_eq _ _ _ _ _ v h0.ne' (Low131.x_pos v h0.le).ne' (Low131.E_pos v h0.le).ne'
  sel_hasDerivAt := fun v h0 _ => sel_hasDerivAt _ _ v (Low131.x_pos v h0).ne'
  q_lower := Low131.unifQLower
  q_upper := Low131.unifQUpper
  q_floor := Low131.unifQFloor
  H_lower := Low131.unifHLower
  retained_cap := Low131.unifRetainedCap
  retained_width := Low131.unifRetainedWidth
  low_per_excess_width := Low131.unifLowPerWidth
  principal_reference := Low131.unifPrincipal
  second_reference := Low131.unifSecondRef
  second_diagonal := Low131.unifSecondDiag
  reference_upper_positive := Low131.unifRefUpper
  selection_monotonicity := Low131.unifSelDeriv
  high_marked := markedHigh131
end
end QRH.ArviDensity.ChainExtension
