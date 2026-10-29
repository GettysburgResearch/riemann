/- Generated candidate UnifPos gate proofs, UNCOMPILED. -/
import Submissions.arvi_density.Source.HybridGatesMarked
set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.ChainExtension.Low130
noncomputable section
open QRH.ArviDensity QRH.ArviDensity.Hybrid
theorem cross_eq : cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) = (831 / 10000 : ℝ) := by norm_num [cross]
theorem x_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < 1 + (51 / 100 : ℝ) * v := by nlinarith
theorem E_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < densE (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v := by
  unfold densE; nlinarith

def nQLower (v : ℝ) : ℝ := (617033 : ℝ) * v ^ 0 + (-16830000 : ℝ) * v ^ 1
def dQLower (v : ℝ) : ℝ := (154349560634 : ℝ) * v ^ 0 + (33660000 : ℝ) * v ^ 1
theorem clearedQLower (v : ℝ) (h0 : 0 ≤ v) : (gQLower (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dQLower v = nQLower v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQLower_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v he) ?_
  simp only [nQLower, dQLower, densE, densK, width, cross_eq]
  ring
theorem nQLower_bern (t : ℝ) : nQLower ((169 / 10000 : ℝ) * t) = bern1 (617033 : ℝ) (332606 : ℝ) t := by
  unfold nQLower bern1; ring
theorem dQLower_bern (t : ℝ) : dQLower ((169 / 10000 : ℝ) * t) = bern1 (154349560634 : ℝ) (154350129488 : ℝ) t := by
  unfold dQLower bern1; ring
theorem unifQLower : UnifPos (gQLower (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(166303 / 77175064744 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQLower (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nQLower) (d := dQLower)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (332606 : ℝ)) (M := (154350129488 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQLower v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (332606 : ℝ) ≤ nQLower ((169 / 10000 : ℝ) * t) by
        rw [nQLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (154349560634 : ℝ) ≤ dQLower ((169 / 10000 : ℝ) * t) := by
        rw [dQLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQLower ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQLower ((169 / 10000 : ℝ) * t) ≤ (154350129488 : ℝ) by
        rw [dQLower_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nQUpper (v : ℝ) : ℝ := (77173546251 : ℝ) * v ^ 0 + (50490000 : ℝ) * v ^ 1
def dQUpper (v : ℝ) : ℝ := (308699121268 : ℝ) * v ^ 0 + (67320000 : ℝ) * v ^ 1
theorem clearedQUpper (v : ℝ) (h0 : 0 ≤ v) : (gQUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dQUpper v = nQUpper v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQUpper_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v he) ?_
  simp only [nQUpper, dQUpper, densE, densK, width, cross_eq]
  ring
theorem nQUpper_bern (t : ℝ) : nQUpper ((169 / 10000 : ℝ) * t) = bern1 (77173546251 : ℝ) (77174399532 : ℝ) t := by
  unfold nQUpper bern1; ring
theorem dQUpper_bern (t : ℝ) : dQUpper ((169 / 10000 : ℝ) * t) = bern1 (308699121268 : ℝ) (308700258976 : ℝ) t := by
  unfold dQUpper bern1; ring
theorem unifQUpper : UnifPos (gQUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(77173546251 / 308700258976 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nQUpper) (d := dQUpper)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (77173546251 : ℝ)) (M := (308700258976 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQUpper v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (77173546251 : ℝ) ≤ nQUpper ((169 / 10000 : ℝ) * t) by
        rw [nQUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (308699121268 : ℝ) ≤ dQUpper ((169 / 10000 : ℝ) * t) := by
        rw [dQUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQUpper ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQUpper ((169 / 10000 : ℝ) * t) ≤ (308700258976 : ℝ) by
        rw [dQUpper_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nQFloor (v : ℝ) : ℝ := (617033 : ℝ) * v ^ 0 + (-16830000 : ℝ) * v ^ 1
def dQFloor (v : ℝ) : ℝ := (154349560634 : ℝ) * v ^ 0 + (33660000 : ℝ) * v ^ 1
theorem clearedQFloor (v : ℝ) (h0 : 0 ≤ v) : (gQFloor (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dQFloor v = nQFloor v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared he (gQFloor_mul (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v he) ?_
  simp only [nQFloor, dQFloor, densE, densK, width, cross_eq]
  ring
theorem nQFloor_bern (t : ℝ) : nQFloor ((169 / 10000 : ℝ) * t) = bern1 (617033 : ℝ) (332606 : ℝ) t := by
  unfold nQFloor bern1; ring
theorem dQFloor_bern (t : ℝ) : dQFloor ((169 / 10000 : ℝ) * t) = bern1 (154349560634 : ℝ) (154350129488 : ℝ) t := by
  unfold dQFloor bern1; ring
theorem unifQFloor : UnifPos (gQFloor (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(166303 / 77175064744 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gQFloor (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nQFloor) (d := dQFloor)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (332606 : ℝ)) (M := (154350129488 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedQFloor v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (332606 : ℝ) ≤ nQFloor ((169 / 10000 : ℝ) * t) by
        rw [nQFloor_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (154349560634 : ℝ) ≤ dQFloor ((169 / 10000 : ℝ) * t) := by
        rw [dQFloor_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dQFloor ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dQFloor ((169 / 10000 : ℝ) * t) ≤ (154350129488 : ℝ) by
        rw [dQFloor_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nHLower (v : ℝ) : ℝ := (20 : ℝ) * v ^ 0 + (-471 : ℝ) * v ^ 1
def dHLower (v : ℝ) : ℝ := (200 : ℝ) * v ^ 0 + (102 : ℝ) * v ^ 1
theorem clearedHLower (v : ℝ) (h0 : 0 ≤ v) : (gHLower (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dHLower v = nHLower v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gHLower_mul (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nHLower, dHLower, densE, densK, width, cross_eq]
  ring
theorem nHLower_bern (t : ℝ) : nHLower ((169 / 10000 : ℝ) * t) = bern1 (20 : ℝ) (120401 / 10000 : ℝ) t := by
  unfold nHLower bern1; ring
theorem dHLower_bern (t : ℝ) : dHLower ((169 / 10000 : ℝ) * t) = bern1 (200 : ℝ) (1008619 / 5000 : ℝ) t := by
  unfold dHLower bern1; ring
theorem unifHLower : UnifPos (gHLower (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(120401 / 2017238 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gHLower (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nHLower) (d := dHLower)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (120401 / 10000 : ℝ)) (M := (1008619 / 5000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedHLower v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (120401 / 10000 : ℝ) ≤ nHLower ((169 / 10000 : ℝ) * t) by
        rw [nHLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (200 : ℝ) ≤ dHLower ((169 / 10000 : ℝ) * t) := by
        rw [dHLower_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dHLower ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dHLower ((169 / 10000 : ℝ) * t) ≤ (1008619 / 5000 : ℝ) by
        rw [dHLower_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRetainedCap (v : ℝ) : ℝ := (16900 : ℝ) * v ^ 0 + (-830981 : ℝ) * v ^ 1 + (-510000 : ℝ) * v ^ 2
def dRetainedCap (v : ℝ) : ℝ := (1000000 : ℝ) * v ^ 0 + (510000 : ℝ) * v ^ 1
theorem clearedRetainedCap (v : ℝ) (h0 : 0 ≤ v) : (gRetainedCap (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dRetainedCap v = nRetainedCap v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRetainedCap_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nRetainedCap, dRetainedCap, densE, densK, width, cross_eq]
  ring
theorem nRetainedCap_bern (t : ℝ) : nRetainedCap ((169 / 10000 : ℝ) * t) = bern2 (16900 : ℝ) (197564211 / 20000 : ℝ) (67769 / 25 : ℝ) t := by
  unfold nRetainedCap bern2; ring
theorem dRetainedCap_bern (t : ℝ) : dRetainedCap ((169 / 10000 : ℝ) * t) = bern1 (1000000 : ℝ) (1008619 : ℝ) t := by
  unfold dRetainedCap bern1; ring
theorem unifRetainedCap : UnifPos (gRetainedCap (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(67769 / 25215475 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRetainedCap (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nRetainedCap) (d := dRetainedCap)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (67769 / 25 : ℝ)) (M := (1008619 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRetainedCap v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (67769 / 25 : ℝ) ≤ nRetainedCap ((169 / 10000 : ℝ) * t) by
        rw [nRetainedCap_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1000000 : ℝ) ≤ dRetainedCap ((169 / 10000 : ℝ) * t) := by
        rw [dRetainedCap_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRetainedCap ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRetainedCap ((169 / 10000 : ℝ) * t) ≤ (1008619 : ℝ) by
        rw [dRetainedCap_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRetainedWidth (v : ℝ) : ℝ := (83100 : ℝ) * v ^ 0 + (641381 : ℝ) * v ^ 1 + (510000 : ℝ) * v ^ 2
def dRetainedWidth (v : ℝ) : ℝ := (1000000 : ℝ) * v ^ 0 + (510000 : ℝ) * v ^ 1
theorem clearedRetainedWidth (v : ℝ) (h0 : 0 ≤ v) : (gRetainedWidth (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dRetainedWidth v = nRetainedWidth v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRetainedWidth_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nRetainedWidth, dRetainedWidth, densE, densK, width, cross_eq]
  ring
theorem nRetainedWidth_bern (t : ℝ) : nRetainedWidth ((169 / 10000 : ℝ) * t) = bern2 (83100 : ℝ) (1770393389 / 20000 : ℝ) (94085 : ℝ) t := by
  unfold nRetainedWidth bern2; ring
theorem dRetainedWidth_bern (t : ℝ) : dRetainedWidth ((169 / 10000 : ℝ) * t) = bern1 (1000000 : ℝ) (1008619 : ℝ) t := by
  unfold dRetainedWidth bern1; ring
theorem unifRetainedWidth : UnifPos (gRetainedWidth (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(83100 / 1008619 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRetainedWidth (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nRetainedWidth) (d := dRetainedWidth)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (83100 : ℝ)) (M := (1008619 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRetainedWidth v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (83100 : ℝ) ≤ nRetainedWidth ((169 / 10000 : ℝ) * t) by
        rw [nRetainedWidth_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1000000 : ℝ) ≤ dRetainedWidth ((169 / 10000 : ℝ) * t) := by
        rw [dRetainedWidth_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRetainedWidth ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRetainedWidth ((169 / 10000 : ℝ) * t) ≤ (1008619 : ℝ) by
        rw [dRetainedWidth_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nLowPerWidth (v : ℝ) : ℝ := (1545053 : ℝ) * v ^ 0
def dLowPerWidth (v : ℝ) : ℝ := (2000000000 : ℝ) * v ^ 0 + (1020000000 : ℝ) * v ^ 1
theorem clearedLowPerWidth (v : ℝ) (h0 : 0 ≤ v) : (gLowPerWidth (3853 / 2000 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dLowPerWidth v = nLowPerWidth v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gLowPerWidth_mul (3853 / 2000 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nLowPerWidth, dLowPerWidth, densE, densK, width, cross_eq]
  ring
theorem nLowPerWidth_bern (t : ℝ) : nLowPerWidth ((169 / 10000 : ℝ) * t) = bern0 (1545053 : ℝ) t := by
  unfold nLowPerWidth bern0; ring
theorem dLowPerWidth_bern (t : ℝ) : dLowPerWidth ((169 / 10000 : ℝ) * t) = bern1 (2000000000 : ℝ) (2017238000 : ℝ) t := by
  unfold dLowPerWidth bern1; ring
theorem unifLowPerWidth : UnifPos (gLowPerWidth (3853 / 2000 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(1545053 / 2017238000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gLowPerWidth (3853 / 2000 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nLowPerWidth) (d := dLowPerWidth)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (1545053 : ℝ)) (M := (2017238000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedLowPerWidth v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (1545053 : ℝ) ≤ nLowPerWidth ((169 / 10000 : ℝ) * t) by
        rw [nLowPerWidth_bern]; exact bern0_ge (by norm_num)))
    (fun t ht ht' => by
      have hb : (2000000000 : ℝ) ≤ dLowPerWidth ((169 / 10000 : ℝ) * t) := by
        rw [dLowPerWidth_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dLowPerWidth ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dLowPerWidth ((169 / 10000 : ℝ) * t) ≤ (2017238000 : ℝ) by
        rw [dLowPerWidth_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nPrincipal (v : ℝ) : ℝ := (39454700 : ℝ) * v ^ 0 + (-2328203103 : ℝ) * v ^ 1 + (-47277000 : ℝ) * v ^ 2
def dPrincipal (v : ℝ) : ℝ := (1250000000 : ℝ) * v ^ 0 + (637500000 : ℝ) * v ^ 1
theorem clearedPrincipal (v : ℝ) (h0 : 0 ≤ v) : (gPrincipal (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dPrincipal v = nPrincipal v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gPrincipal_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nPrincipal, dPrincipal, densE, densK, width, cross_eq]
  ring
theorem nPrincipal_bern (t : ℝ) : nPrincipal ((169 / 10000 : ℝ) * t) = bern2 (39454700 : ℝ) (395627675593 / 20000 : ℝ) (9456477533 / 100000 : ℝ) t := by
  unfold nPrincipal bern2; ring
theorem dPrincipal_bern (t : ℝ) : dPrincipal ((169 / 10000 : ℝ) * t) = bern1 (1250000000 : ℝ) (1260773750 : ℝ) t := by
  unfold dPrincipal bern1; ring
theorem unifPrincipal : UnifPos (gPrincipal (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(9456477533 / 126077375000000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gPrincipal (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nPrincipal) (d := dPrincipal)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (9456477533 / 100000 : ℝ)) (M := (1260773750 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedPrincipal v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (9456477533 / 100000 : ℝ) ≤ nPrincipal ((169 / 10000 : ℝ) * t) by
        rw [nPrincipal_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1250000000 : ℝ) ≤ dPrincipal ((169 / 10000 : ℝ) * t) := by
        rw [dPrincipal_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dPrincipal ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dPrincipal ((169 / 10000 : ℝ) * t) ≤ (1260773750 : ℝ) by
        rw [dPrincipal_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSecondRef (v : ℝ) : ℝ := (347239100 : ℝ) * v ^ 0 + (-3362258059 : ℝ) * v ^ 1 + (495669000 : ℝ) * v ^ 2
def dSecondRef (v : ℝ) : ℝ := (2500000000 : ℝ) * v ^ 0 + (1275000000 : ℝ) * v ^ 1
theorem clearedSecondRef (v : ℝ) (h0 : 0 ≤ v) : (gSecondRef (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dSecondRef v = nSecondRef v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gSecondRef_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nSecondRef, dSecondRef, densE, densK, width, cross_eq]
  ring
theorem nSecondRef_bern (t : ℝ) : nSecondRef ((169 / 10000 : ℝ) * t) = bern2 (347239100 : ℝ) (6376560388029 / 20000 : ℝ) (29055850682599 / 100000 : ℝ) t := by
  unfold nSecondRef bern2; ring
theorem dSecondRef_bern (t : ℝ) : dSecondRef ((169 / 10000 : ℝ) * t) = bern1 (2500000000 : ℝ) (2521547500 : ℝ) t := by
  unfold dSecondRef bern1; ring
theorem unifSecondRef : UnifPos (gSecondRef (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(29055850682599 / 252154750000000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSecondRef (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nSecondRef) (d := dSecondRef)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (29055850682599 / 100000 : ℝ)) (M := (2521547500 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSecondRef v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (29055850682599 / 100000 : ℝ) ≤ nSecondRef ((169 / 10000 : ℝ) * t) by
        rw [nSecondRef_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (2500000000 : ℝ) ≤ dSecondRef ((169 / 10000 : ℝ) * t) := by
        rw [dSecondRef_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSecondRef ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSecondRef ((169 / 10000 : ℝ) * t) ≤ (2521547500 : ℝ) by
        rw [dSecondRef_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSecondDiag (v : ℝ) : ℝ := (143329700 : ℝ) * v ^ 0 + (-774601853 : ℝ) * v ^ 1 + (590223000 : ℝ) * v ^ 2
def dSecondDiag (v : ℝ) : ℝ := (1250000000 : ℝ) * v ^ 0 + (637500000 : ℝ) * v ^ 1
theorem clearedSecondDiag (v : ℝ) (h0 : 0 ≤ v) : (gSecondDiag (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dSecondDiag v = nSecondDiag v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gSecondDiag_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nSecondDiag, dSecondDiag, densE, densK, width, cross_eq]
  ring
theorem nSecondDiag_bern (t : ℝ) : nSecondDiag ((169 / 10000 : ℝ) * t) = bern2 (143329700 : ℝ) (2735686286843 / 20000 : ℝ) (13040750227533 / 100000 : ℝ) t := by
  unfold nSecondDiag bern2; ring
theorem dSecondDiag_bern (t : ℝ) : dSecondDiag ((169 / 10000 : ℝ) * t) = bern1 (1250000000 : ℝ) (1260773750 : ℝ) t := by
  unfold dSecondDiag bern1; ring
theorem unifSecondDiag : UnifPos (gSecondDiag (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(13040750227533 / 126077375000000 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSecondDiag (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nSecondDiag) (d := dSecondDiag)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (13040750227533 / 100000 : ℝ)) (M := (1260773750 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSecondDiag v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (13040750227533 / 100000 : ℝ) ≤ nSecondDiag ((169 / 10000 : ℝ) * t) by
        rw [nSecondDiag_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1250000000 : ℝ) ≤ dSecondDiag ((169 / 10000 : ℝ) * t) := by
        rw [dSecondDiag_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSecondDiag ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSecondDiag ((169 / 10000 : ℝ) * t) ≤ (1260773750 : ℝ) by
        rw [dSecondDiag_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nRefUpper (v : ℝ) : ℝ := (250700 : ℝ) * v ^ 0 + (-4676643 : ℝ) * v ^ 1 + (-1530000 : ℝ) * v ^ 2
def dRefUpper (v : ℝ) : ℝ := (1500000 : ℝ) * v ^ 0 + (765000 : ℝ) * v ^ 1
theorem clearedRefUpper (v : ℝ) (h0 : 0 ≤ v) : (gRefUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dRefUpper v = nRefUpper v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared hx (gRefUpper_mul (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nRefUpper, dRefUpper, densE, densK, width, cross_eq]
  ring
theorem nRefUpper_bern (t : ℝ) : nRefUpper ((169 / 10000 : ℝ) * t) = bern2 (250700 : ℝ) (4223647333 / 20000 : ℝ) (684911 / 4 : ℝ) t := by
  unfold nRefUpper bern2; ring
theorem dRefUpper_bern (t : ℝ) : dRefUpper ((169 / 10000 : ℝ) * t) = bern1 (1500000 : ℝ) (3025857 / 2 : ℝ) t := by
  unfold dRefUpper bern1; ring
theorem unifRefUpper : UnifPos (gRefUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(684911 / 6051714 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gRefUpper (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nRefUpper) (d := dRefUpper)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (684911 / 4 : ℝ)) (M := (3025857 / 2 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedRefUpper v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (684911 / 4 : ℝ) ≤ nRefUpper ((169 / 10000 : ℝ) * t) by
        rw [nRefUpper_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)))
    (fun t ht ht' => by
      have hb : (1500000 : ℝ) ≤ dRefUpper ((169 / 10000 : ℝ) * t) := by
        rw [dRefUpper_bern]; exact bern1_ge ht ht' (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dRefUpper ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dRefUpper ((169 / 10000 : ℝ) * t) ≤ (3025857 / 2 : ℝ) by
        rw [dRefUpper_bern]; exact bern1_le ht ht' (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb

def nSelDeriv (v : ℝ) : ℝ := (4010 : ℝ) * v ^ 0
def dSelDeriv (v : ℝ) : ℝ := (10000 : ℝ) * v ^ 0 + (10200 : ℝ) * v ^ 1 + (2601 : ℝ) * v ^ 2
theorem clearedSelDeriv (v : ℝ) (h0 : 0 ≤ v) : (gSelDeriv (401 / 1000 : ℝ) (51 / 100 : ℝ)) v * dSelDeriv v = nSelDeriv v := by
  have hx := (x_pos v h0).ne'
  have he := (E_pos v h0).ne'
  refine mul_eq_of_cleared (pow_ne_zero 2 hx) (gSelDeriv_mul (401 / 1000 : ℝ) (51 / 100 : ℝ) v hx) ?_
  simp only [nSelDeriv, dSelDeriv, densE, densK, width, cross_eq]
  ring
theorem nSelDeriv_bern (t : ℝ) : nSelDeriv ((169 / 10000 : ℝ) * t) = bern0 (4010 : ℝ) t := by
  unfold nSelDeriv bern0; ring
theorem dSelDeriv_bern (t : ℝ) : dSelDeriv ((169 / 10000 : ℝ) * t) = bern2 (10000 : ℝ) (1008619 / 100 : ℝ) (1017312287161 / 100000000 : ℝ) t := by
  unfold dSelDeriv bern2; ring
theorem unifSelDeriv : UnifPos (gSelDeriv (401 / 1000 : ℝ) (51 / 100 : ℝ)) 0 ((1 / 10 : ℝ) - cross (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)) := by
  refine ⟨(401000000000 / 1017312287161 : ℝ), by norm_num, fun v h0 h1 => ?_⟩
  rw [cross_eq] at h1
  have hb := box_lower (g := (gSelDeriv (401 / 1000 : ℝ) (51 / 100 : ℝ))) (n := nSelDeriv) (d := dSelDeriv)
    (lo := (0 : ℝ)) (hi := (169 / 10000 : ℝ)) (m := (4010 : ℝ)) (M := (1017312287161 / 100000000 : ℝ)) (by norm_num) (by norm_num)
    (fun v h0 _ => clearedSelDeriv v (by linarith))
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show (4010 : ℝ) ≤ nSelDeriv ((169 / 10000 : ℝ) * t) by
        rw [nSelDeriv_bern]; exact bern0_ge (by norm_num)))
    (fun t ht ht' => by
      have hb : (10000 : ℝ) ≤ dSelDeriv ((169 / 10000 : ℝ) * t) := by
        rw [dSelDeriv_bern]; exact bern2_ge ht ht' (by norm_num) (by norm_num) (by norm_num)
      have hd : (0 : ℝ) < dSelDeriv ((169 / 10000 : ℝ) * t) := lt_of_lt_of_le (by norm_num) hb
      simpa only [zero_add, sub_zero] using hd)
    (fun t ht ht' => by
      simpa only [zero_add, sub_zero] using (show dSelDeriv ((169 / 10000 : ℝ) * t) ≤ (1017312287161 / 100000000 : ℝ) by
        rw [dSelDeriv_bern]; exact bern2_le ht ht' (by norm_num) (by norm_num) (by norm_num)))
    v h0 (by linarith)
  exact le_trans (by norm_num) hb
end
end QRH.ArviDensity.ChainExtension.Low130
