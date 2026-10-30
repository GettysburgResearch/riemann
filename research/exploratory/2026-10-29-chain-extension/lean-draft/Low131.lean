/- Generated candidate UnifPos gate proofs, UNCOMPILED. -/
import Submissions.arvi_density.Source.HybridGatesMarked
set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.ChainExtension.Low131
noncomputable section
open QRH.ArviDensity QRH.ArviDensity.Hybrid
theorem cross_eq : cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) = (52 / 625 : ℝ) := by norm_num [cross]
theorem x_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < 1 + (1 / 10 : ℝ) * v := by nlinarith
theorem E_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < densE (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v := by
  unfold densE; nlinarith

def nQLower (v : ℝ) : ℝ := (514 : ℝ) * v ^ 0 + (-625 : ℝ) * v ^ 1
def dQLower (v : ℝ) : ℝ := (1923913132 : ℝ) * v ^ 0 + (1250 : ℝ) * v ^ 1
theorem clearedQLower (v : ℝ) (h0 : 0 ≤ v) : (gQLower (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dQLower v = nQLower v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQLower_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v he) ?_
  simp only [nQLower, dQLower, densE, densK, width, cross_eq]
  ring
theorem nQLower_bern (t : ℝ) : nQLower ((21 / 1250 : ℝ) * t) = bern1 (514 : ℝ) (1007 / 2 : ℝ) t := by
  unfold nQLower bern1; ring
theorem dQLower_bern (t : ℝ) : dQLower ((21 / 1250 : ℝ) * t) = bern1 (1923913132 : ℝ) (1923913153 : ℝ) t := by
  unfold dQLower bern1; ring
theorem unifQLower : UnifPos (gQLower (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(53 / 202517174 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQLower (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nQLower) (d := dQLower)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (1007 / 2 : ℝ)) (M := (1923913153 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQLower v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (1007 / 2 : ℝ) ≤ nQLower ((21 / 1250 : ℝ) * t) by
        rw [nQLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1923913132 : ℝ) ≤ dQLower ((21 / 1250 : ℝ) * t) := by
        rw [dQLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQLower ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQLower ((21 / 1250 : ℝ) * t) ≤ (1923913153 : ℝ) by
        rw [dQLower_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nQUpper (v : ℝ) : ℝ := (961955538 : ℝ) * v ^ 0 + (1875 : ℝ) * v ^ 1
def dQUpper (v : ℝ) : ℝ := (3847826264 : ℝ) * v ^ 0 + (2500 : ℝ) * v ^ 1
theorem clearedQUpper (v : ℝ) (h0 : 0 ≤ v) : (gQUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dQUpper v = nQUpper v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQUpper_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v he) ?_
  simp only [nQUpper, dQUpper, densE, densK, width, cross_eq]
  ring
theorem nQUpper_bern (t : ℝ) : nQUpper ((21 / 1250 : ℝ) * t) = bern1 (961955538 : ℝ) (1923911139 / 2 : ℝ) t := by
  unfold nQUpper bern1; ring
theorem dQUpper_bern (t : ℝ) : dQUpper ((21 / 1250 : ℝ) * t) = bern1 (3847826264 : ℝ) (3847826306 : ℝ) t := by
  unfold dQUpper bern1; ring
theorem unifQUpper : UnifPos (gQUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(480977769 / 1923913153 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nQUpper) (d := dQUpper)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (961955538 : ℝ)) (M := (3847826306 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQUpper v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (961955538 : ℝ) ≤ nQUpper ((21 / 1250 : ℝ) * t) by
        rw [nQUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (3847826264 : ℝ) ≤ dQUpper ((21 / 1250 : ℝ) * t) := by
        rw [dQUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQUpper ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQUpper ((21 / 1250 : ℝ) * t) ≤ (3847826306 : ℝ) by
        rw [dQUpper_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nQFloor (v : ℝ) : ℝ := (514 : ℝ) * v ^ 0 + (-625 : ℝ) * v ^ 1
def dQFloor (v : ℝ) : ℝ := (1923913132 : ℝ) * v ^ 0 + (1250 : ℝ) * v ^ 1
theorem clearedQFloor (v : ℝ) (h0 : 0 ≤ v) : (gQFloor (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dQFloor v = nQFloor v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQFloor_mul (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v he) ?_
  simp only [nQFloor, dQFloor, densE, densK, width, cross_eq]
  ring
theorem nQFloor_bern (t : ℝ) : nQFloor ((21 / 1250 : ℝ) * t) = bern1 (514 : ℝ) (1007 / 2 : ℝ) t := by
  unfold nQFloor bern1; ring
theorem dQFloor_bern (t : ℝ) : dQFloor ((21 / 1250 : ℝ) * t) = bern1 (1923913132 : ℝ) (1923913153 : ℝ) t := by
  unfold dQFloor bern1; ring
theorem unifQFloor : UnifPos (gQFloor (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(53 / 202517174 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQFloor (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nQFloor) (d := dQFloor)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (1007 / 2 : ℝ)) (M := (1923913153 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQFloor v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (1007 / 2 : ℝ) ≤ nQFloor ((21 / 1250 : ℝ) * t) by
        rw [nQFloor_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1923913132 : ℝ) ≤ dQFloor ((21 / 1250 : ℝ) * t) := by
        rw [dQFloor_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQFloor ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQFloor ((21 / 1250 : ℝ) * t) ≤ (1923913153 : ℝ) by
        rw [dQFloor_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nHLower (v : ℝ) : ℝ := (10 : ℝ) * v ^ 0 + (-239 : ℝ) * v ^ 1
def dHLower (v : ℝ) : ℝ := (100 : ℝ) * v ^ 0 + (10 : ℝ) * v ^ 1
theorem clearedHLower (v : ℝ) (h0 : 0 ≤ v) : (gHLower (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dHLower v = nHLower v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gHLower_mul (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nHLower, dHLower, densE, densK, width, cross_eq]
  ring
theorem nHLower_bern (t : ℝ) : nHLower ((21 / 1250 : ℝ) * t) = bern1 (10 : ℝ) (7481 / 1250 : ℝ) t := by
  unfold nHLower bern1; ring
theorem dHLower_bern (t : ℝ) : dHLower ((21 / 1250 : ℝ) * t) = bern1 (100 : ℝ) (12521 / 125 : ℝ) t := by
  unfold dHLower bern1; ring
theorem unifHLower : UnifPos (gHLower (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(7481 / 125210 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gHLower (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nHLower) (d := dHLower)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (7481 / 1250 : ℝ)) (M := (12521 / 125 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedHLower v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (7481 / 1250 : ℝ) ≤ nHLower ((21 / 1250 : ℝ) * t) by
        rw [nHLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (100 : ℝ) ≤ dHLower ((21 / 1250 : ℝ) * t) := by
        rw [dHLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dHLower ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dHLower ((21 / 1250 : ℝ) * t) ≤ (12521 / 125 : ℝ) by
        rw [dHLower_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRetainedCap (v : ℝ) : ℝ := (210 : ℝ) * v ^ 0 + (-10479 : ℝ) * v ^ 1 + (-1250 : ℝ) * v ^ 2
def dRetainedCap (v : ℝ) : ℝ := (12500 : ℝ) * v ^ 0 + (1250 : ℝ) * v ^ 1
theorem clearedRetainedCap (v : ℝ) (h0 : 0 ≤ v) : (gRetainedCap (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dRetainedCap v = nRetainedCap v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRetainedCap_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nRetainedCap, dRetainedCap, densE, densK, width, cross_eq]
  ring
theorem nRetainedCap_bern (t : ℝ) : nRetainedCap ((21 / 1250 : ℝ) * t) = bern2 (210 : ℝ) (304941 / 2500 : ℝ) (168 / 5 : ℝ) t := by
  unfold nRetainedCap bern2; ring
theorem dRetainedCap_bern (t : ℝ) : dRetainedCap ((21 / 1250 : ℝ) * t) = bern1 (12500 : ℝ) (12521 : ℝ) t := by
  unfold dRetainedCap bern1; ring
theorem unifRetainedCap : UnifPos (gRetainedCap (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(168 / 62605 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRetainedCap (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nRetainedCap) (d := dRetainedCap)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (168 / 5 : ℝ)) (M := (12521 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRetainedCap v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (168 / 5 : ℝ) ≤ nRetainedCap ((21 / 1250 : ℝ) * t) by
        rw [nRetainedCap_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (12500 : ℝ) ≤ dRetainedCap ((21 / 1250 : ℝ) * t) := by
        rw [dRetainedCap_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRetainedCap ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRetainedCap ((21 / 1250 : ℝ) * t) ≤ (12521 : ℝ) by
        rw [dRetainedCap_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRetainedWidth (v : ℝ) : ℝ := (520 : ℝ) * v ^ 0 + (3802 : ℝ) * v ^ 1 + (625 : ℝ) * v ^ 2
def dRetainedWidth (v : ℝ) : ℝ := (6250 : ℝ) * v ^ 0 + (625 : ℝ) * v ^ 1
theorem clearedRetainedWidth (v : ℝ) (h0 : 0 ≤ v) : (gRetainedWidth (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dRetainedWidth v = nRetainedWidth v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRetainedWidth_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nRetainedWidth, dRetainedWidth, densE, densK, width, cross_eq]
  ring
theorem nRetainedWidth_bern (t : ℝ) : nRetainedWidth ((21 / 1250 : ℝ) * t) = bern2 (520 : ℝ) (689921 / 1250 : ℝ) (11681 / 20 : ℝ) t := by
  unfold nRetainedWidth bern2; ring
theorem dRetainedWidth_bern (t : ℝ) : dRetainedWidth ((21 / 1250 : ℝ) * t) = bern1 (6250 : ℝ) (12521 / 2 : ℝ) t := by
  unfold dRetainedWidth bern1; ring
theorem unifRetainedWidth : UnifPos (gRetainedWidth (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(1040 / 12521 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRetainedWidth (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nRetainedWidth) (d := dRetainedWidth)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (520 : ℝ)) (M := (12521 / 2 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRetainedWidth v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (520 : ℝ) ≤ nRetainedWidth ((21 / 1250 : ℝ) * t) by
        rw [nRetainedWidth_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (6250 : ℝ) ≤ dRetainedWidth ((21 / 1250 : ℝ) * t) := by
        rw [dRetainedWidth_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRetainedWidth ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRetainedWidth ((21 / 1250 : ℝ) * t) ≤ (12521 / 2 : ℝ) by
        rw [dRetainedWidth_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nLowPerWidth (v : ℝ) : ℝ := (24073 : ℝ) * v ^ 0
def dLowPerWidth (v : ℝ) : ℝ := (31250000 : ℝ) * v ^ 0 + (3125000 : ℝ) * v ^ 1
theorem clearedLowPerWidth (v : ℝ) (h0 : 0 ≤ v) : (gLowPerWidth (24073 / 12500 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dLowPerWidth v = nLowPerWidth v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gLowPerWidth_mul (24073 / 12500 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nLowPerWidth, dLowPerWidth, densE, densK, width, cross_eq]
  ring
theorem nLowPerWidth_bern (t : ℝ) : nLowPerWidth ((21 / 1250 : ℝ) * t) = bern0 (24073 : ℝ) t := by
  unfold nLowPerWidth bern0; ring
theorem dLowPerWidth_bern (t : ℝ) : dLowPerWidth ((21 / 1250 : ℝ) * t) = bern1 (31250000 : ℝ) (31302500 : ℝ) t := by
  unfold dLowPerWidth bern1; ring
theorem unifLowPerWidth : UnifPos (gLowPerWidth (24073 / 12500 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(1267 / 1647500 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gLowPerWidth (24073 / 12500 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nLowPerWidth) (d := dLowPerWidth)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (24073 : ℝ)) (M := (31302500 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedLowPerWidth v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (24073 : ℝ) ≤ nLowPerWidth ((21 / 1250 : ℝ) * t) by
        rw [nLowPerWidth_bern]; exact bern0_ge (by norm_num)))
    (fun t ht ht' => by
      have hb : (31250000 : ℝ) ≤ dLowPerWidth ((21 / 1250 : ℝ) * t) := by
        rw [dLowPerWidth_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dLowPerWidth ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dLowPerWidth ((21 / 1250 : ℝ) * t) ≤ (31302500 : ℝ) by
        rw [dLowPerWidth_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nPrincipal (v : ℝ) : ℝ := (39445430 : ℝ) * v ^ 0 + (-2338767957 : ℝ) * v ^ 1 + (-9271250 : ℝ) * v ^ 2
def dPrincipal (v : ℝ) : ℝ := (1250000000 : ℝ) * v ^ 0 + (125000000 : ℝ) * v ^ 1
theorem clearedPrincipal (v : ℝ) (h0 : 0 ≤ v) : (gPrincipal (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dPrincipal v = nPrincipal v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gPrincipal_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nPrincipal, dPrincipal, densE, densK, width, cross_eq]
  ring
theorem nPrincipal_bern (t : ℝ) : nPrincipal ((21 / 1250 : ℝ) * t) = bern2 (39445430 : ℝ) (49499447903 / 2500 : ℝ) (94694753 / 625 : ℝ) t := by
  unfold nPrincipal bern2; ring
theorem dPrincipal_bern (t : ℝ) : dPrincipal ((21 / 1250 : ℝ) * t) = bern1 (1250000000 : ℝ) (1252100000 : ℝ) t := by
  unfold dPrincipal bern1; ring
theorem unifPrincipal : UnifPos (gPrincipal (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(94694753 / 782562500000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gPrincipal (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nPrincipal) (d := dPrincipal)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (94694753 / 625 : ℝ)) (M := (1252100000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedPrincipal v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (94694753 / 625 : ℝ) ≤ nPrincipal ((21 / 1250 : ℝ) * t) by
        rw [nPrincipal_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1250000000 : ℝ) ≤ dPrincipal ((21 / 1250 : ℝ) * t) := by
        rw [dPrincipal_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dPrincipal ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dPrincipal ((21 / 1250 : ℝ) * t) ≤ (1252100000 : ℝ) by
        rw [dPrincipal_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSecondRef (v : ℝ) : ℝ := (347336290 : ℝ) * v ^ 0 + (-3493403871 : ℝ) * v ^ 1 + (97186250 : ℝ) * v ^ 2
def dSecondRef (v : ℝ) : ℝ := (2500000000 : ℝ) * v ^ 0 + (250000000 : ℝ) * v ^ 1
theorem clearedSecondRef (v : ℝ) (h0 : 0 ≤ v) : (gSecondRef (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dSecondRef v = nSecondRef v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gSecondRef_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nSecondRef, dSecondRef, densE, densK, width, cross_eq]
  ring
theorem nSecondRef_bern (t : ℝ) : nSecondRef ((21 / 1250 : ℝ) * t) = bern2 (347336290 : ℝ) (794979243709 / 2500 : ℝ) (180421584259 / 625 : ℝ) t := by
  unfold nSecondRef bern2; ring
theorem dSecondRef_bern (t : ℝ) : dSecondRef ((21 / 1250 : ℝ) * t) = bern1 (2500000000 : ℝ) (2504200000 : ℝ) t := by
  unfold dSecondRef bern1; ring
theorem unifSecondRef : UnifPos (gSecondRef (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(180421584259 / 1565125000000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSecondRef (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nSecondRef) (d := dSecondRef)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (180421584259 / 625 : ℝ)) (M := (2504200000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSecondRef v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (180421584259 / 625 : ℝ) ≤ nSecondRef ((21 / 1250 : ℝ) * t) by
        rw [nSecondRef_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (2500000000 : ℝ) ≤ dSecondRef ((21 / 1250 : ℝ) * t) := by
        rw [dSecondRef_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSecondRef ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSecondRef ((21 / 1250 : ℝ) * t) ≤ (2504200000 : ℝ) by
        rw [dSecondRef_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSecondDiag (v : ℝ) : ℝ := (143445430 : ℝ) * v ^ 0 + (-828367957 : ℝ) * v ^ 1 + (115728750 : ℝ) * v ^ 2
def dSecondDiag (v : ℝ) : ℝ := (1250000000 : ℝ) * v ^ 0 + (125000000 : ℝ) * v ^ 1
theorem clearedSecondDiag (v : ℝ) (h0 : 0 ≤ v) : (gSecondDiag (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dSecondDiag v = nSecondDiag v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gSecondDiag_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nSecondDiag, dSecondDiag, densE, densK, width, cross_eq]
  ring
theorem nSecondDiag_bern (t : ℝ) : nSecondDiag ((21 / 1250 : ℝ) * t) = bern2 (143445430 : ℝ) (341217847903 / 2500 : ℝ) (80975944753 / 625 : ℝ) t := by
  unfold nSecondDiag bern2; ring
theorem dSecondDiag_bern (t : ℝ) : dSecondDiag ((21 / 1250 : ℝ) * t) = bern1 (1250000000 : ℝ) (1252100000 : ℝ) t := by
  unfold dSecondDiag bern1; ring
theorem unifSecondDiag : UnifPos (gSecondDiag (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(80975944753 / 782562500000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSecondDiag (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nSecondDiag) (d := dSecondDiag)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (80975944753 / 625 : ℝ)) (M := (1252100000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSecondDiag v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (80975944753 / 625 : ℝ) ≤ nSecondDiag ((21 / 1250 : ℝ) * t) by
        rw [nSecondDiag_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1250000000 : ℝ) ≤ dSecondDiag ((21 / 1250 : ℝ) * t) := by
        rw [dSecondDiag_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSecondDiag ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSecondDiag ((21 / 1250 : ℝ) * t) ≤ (1252100000 : ℝ) by
        rw [dSecondDiag_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRefUpper (v : ℝ) : ℝ := (3130 : ℝ) * v ^ 0 + (-59687 : ℝ) * v ^ 1 + (-3750 : ℝ) * v ^ 2
def dRefUpper (v : ℝ) : ℝ := (18750 : ℝ) * v ^ 0 + (1875 : ℝ) * v ^ 1
theorem clearedRefUpper (v : ℝ) (h0 : 0 ≤ v) : (gRefUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dRefUpper v = nRefUpper v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRefUpper_mul (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nRefUpper, dRefUpper, densE, densK, width, cross_eq]
  ring
theorem nRefUpper_bern (t : ℝ) : nRefUpper ((21 / 1250 : ℝ) * t) = bern2 (3130 : ℝ) (6571573 / 2500 : ℝ) (10631 / 5 : ℝ) t := by
  unfold nRefUpper bern2; ring
theorem dRefUpper_bern (t : ℝ) : dRefUpper ((21 / 1250 : ℝ) * t) = bern1 (18750 : ℝ) (37563 / 2 : ℝ) t := by
  unfold dRefUpper bern1; ring
theorem unifRefUpper : UnifPos (gRefUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(21262 / 187815 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRefUpper (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nRefUpper) (d := dRefUpper)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (10631 / 5 : ℝ)) (M := (37563 / 2 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRefUpper v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (10631 / 5 : ℝ) ≤ nRefUpper ((21 / 1250 : ℝ) * t) by
        rw [nRefUpper_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (18750 : ℝ) ≤ dRefUpper ((21 / 1250 : ℝ) * t) := by
        rw [dRefUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRefUpper ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRefUpper ((21 / 1250 : ℝ) * t) ≤ (37563 / 2 : ℝ) by
        rw [dRefUpper_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSelDeriv (v : ℝ) : ℝ := (40 : ℝ) * v ^ 0
def dSelDeriv (v : ℝ) : ℝ := (100 : ℝ) * v ^ 0 + (20 : ℝ) * v ^ 1 + (1 : ℝ) * v ^ 2
theorem clearedSelDeriv (v : ℝ) (h0 : 0 ≤ v) : (gSelDeriv (2 / 5 : ℝ) (1 / 10 : ℝ)) v * dSelDeriv v = nSelDeriv v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared (pow_ne_zero 2 hx) (gSelDeriv_mul (2 / 5 : ℝ) (1 / 10 : ℝ) v hx) ?_
  simp only [nSelDeriv, dSelDeriv, densE, densK, width, cross_eq]
  ring
theorem nSelDeriv_bern (t : ℝ) : nSelDeriv ((21 / 1250 : ℝ) * t) = bern0 (40 : ℝ) t := by
  unfold nSelDeriv bern0; ring
theorem dSelDeriv_bern (t : ℝ) : dSelDeriv ((21 / 1250 : ℝ) * t) = bern2 (100 : ℝ) (12521 / 125 : ℝ) (156775441 / 1562500 : ℝ) t := by
  unfold dSelDeriv bern2; ring
theorem unifSelDeriv : UnifPos (gSelDeriv (2 / 5 : ℝ) (1 / 10 : ℝ)) 0 ((1 / 10 : ℝ) - cross (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)) := by
  refine ⟨(62500000 / 156775441 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSelDeriv (2 / 5 : ℝ) (1 / 10 : ℝ))) (n := nSelDeriv) (d := dSelDeriv)
    (lo := (0 : ℝ)) (hi := (21 / 1250 : ℝ)) (m := (40 : ℝ)) (M := (156775441 / 1562500 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSelDeriv v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (40 : ℝ) ≤ nSelDeriv ((21 / 1250 : ℝ) * t) by
        rw [nSelDeriv_bern]; exact bern0_ge (by norm_num)))
    (fun t ht ht' => by
      have hb : (100 : ℝ) ≤ dSelDeriv ((21 / 1250 : ℝ) * t) := by
        rw [dSelDeriv_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSelDeriv ((21 / 1250 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSelDeriv ((21 / 1250 : ℝ) * t) ≤ (156775441 / 1562500 : ℝ) by
        rw [dSelDeriv_bern]; exact bern2_le ht ht' (by norm_num) (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb
end
end QRH.ArviDensity.ChainExtension.Low131
