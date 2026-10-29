/- Generated candidate dyadic cover; UNCOMPILED. -/
import Submissions.arvi_density.Return.FinalEnvelopeBounds
import Submissions.arvi_density.Return.Rows.Edges131
set_option autoImplicit false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.Return.FinalEdges
open QRH.Record1252270103Return
noncomputable section
theorem window01_mem : returnWindow01∈returnWindows := by simp [returnWindows]
theorem window02_mem : returnWindow02∈returnWindows := by simp [returnWindows]
theorem window03_mem : returnWindow03∈returnWindows := by simp [returnWindows]
theorem window04_mem : returnWindow04∈returnWindows := by simp [returnWindows]
theorem window05_mem : returnWindow05∈returnWindows := by simp [returnWindows]
theorem window06_mem : returnWindow06∈returnWindows := by simp [returnWindows]
theorem window07_mem : returnWindow07∈returnWindows := by simp [returnWindows]
theorem window08_mem : returnWindow08∈returnWindows := by simp [returnWindows]
theorem window09_mem : returnWindow09∈returnWindows := by simp [returnWindows]
theorem window10_mem : returnWindow10∈returnWindows := by simp [returnWindows]
theorem window11_mem : returnWindow11∈returnWindows := by simp [returnWindows]
theorem window12_mem : returnWindow12∈returnWindows := by simp [returnWindows]
theorem window13_mem : returnWindow13∈returnWindows := by simp [returnWindows]
theorem window14_mem : returnWindow14∈returnWindows := by simp [returnWindows]
theorem window15_mem : returnWindow15∈returnWindows := by simp [returnWindows]
theorem window16_mem : returnWindow16∈returnWindows := by simp [returnWindows]
theorem window17_mem : returnWindow17∈returnWindows := by simp [returnWindows]
theorem window18_mem : returnWindow18∈returnWindows := by simp [returnWindows]
theorem window19_mem : returnWindow19∈returnWindows := by simp [returnWindows]
theorem window20_mem : returnWindow20∈returnWindows := by simp [returnWindows]
theorem window21_mem : returnWindow21∈returnWindows := by simp [returnWindows]
theorem window22_mem : returnWindow22∈returnWindows := by simp [returnWindows]
theorem window23_mem : returnWindow23∈returnWindows := by simp [returnWindows]
theorem window24_mem : returnWindow24∈returnWindows := by simp [returnWindows]
theorem window25_mem : returnWindow25∈returnWindows := by simp [returnWindows]
theorem window26_mem : returnWindow26∈returnWindows := by simp [returnWindows]
theorem window27_mem : returnWindow27∈returnWindows := by simp [returnWindows]
theorem window28_mem : returnWindow28∈returnWindows := by simp [returnWindows]
theorem window29_mem : returnWindow29∈returnWindows := by simp [returnWindows]
theorem window30_mem : returnWindow30∈returnWindows := by simp [returnWindows]
theorem window31_mem : returnWindow31∈returnWindows := by simp [returnWindows]
theorem window32_mem : returnWindow32∈returnWindows := by simp [returnWindows]
theorem window33_mem : returnWindow33∈returnWindows := by simp [returnWindows]
theorem envelope_edge131_0_000 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .oldSmall) (edgeC .oldSmall) δ p+3/4*edgeD .oldSmall*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_0_000_pos hδ hp) hR
theorem edge_oldSmall_certificate {δ p:ℝ} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) :
 Ebase (edgeD .oldSmall) (edgeC .oldSmall) δ p+3/4*edgeD .oldSmall*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 exact envelope_edge131_0_000 (by simpa using hδ) (by simpa using hp)
theorem envelope_edge131_1_000 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .oldSwitch) (edgeC .oldSwitch) δ p+3/4*edgeD .oldSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_1_000_pos hδ hp) hR
theorem envelope_edge131_1_001 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .oldSwitch) (edgeC .oldSwitch) δ p+3/4*edgeD .oldSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_1_001_pos hδ hp) hR
theorem cover131_1_001 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .oldSwitch) (edgeC .oldSwitch) δ p+3/4*edgeD .oldSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3/8:ℝ) with hsplit | hsplit
 · exact envelope_edge131_1_001 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_1_000 ⟨hsplit,hδ.2⟩ hp
theorem edge_oldSwitch_certificate {δ p:ℝ} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) :
 Ebase (edgeD .oldSwitch) (edgeC .oldSwitch) δ p+3/4*edgeD .oldSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 exact cover131_1_001 (by simpa using hδ) (by simpa using hp)
theorem envelope_edge131_2_000 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newSwitch) (edgeC .newSwitch) δ p+3/4*edgeD .newSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_2_000_pos hδ hp) hR
theorem envelope_edge131_2_001 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newSwitch) (edgeC .newSwitch) δ p+3/4*edgeD .newSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_2_001_pos hδ hp) hR
theorem cover131_2_001 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newSwitch) (edgeC .newSwitch) δ p+3/4*edgeD .newSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3/8:ℝ) with hsplit | hsplit
 · exact envelope_edge131_2_001 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_2_000 ⟨hsplit,hδ.2⟩ hp
theorem edge_newSwitch_certificate {δ p:ℝ} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) :
 Ebase (edgeD .newSwitch) (edgeC .newSwitch) δ p+3/4*edgeD .newSwitch*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 exact cover131_2_001 (by simpa using hδ) (by simpa using hp)
theorem envelope_edge131_3_000 {δ p:ℝ} (hδ:δ∈Set.Icc (9/16:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_000_pos hδ hp) hR
theorem envelope_edge131_3_001 {δ p:ℝ} (hδ:δ∈Set.Icc (141/256:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_001_pos hδ hp) hR
theorem envelope_edge131_3_002 {δ p:ℝ} (hδ:δ∈Set.Icc (69/128:ℝ) (141/256:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow31.Available δ p := by
  change δ∈Set.Icc (69/128:ℝ) (141/256:ℝ) ∧ p∈Set.Icc (31/64:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow31 window31_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_002_pos hδ hp) hR
theorem envelope_edge131_3_003 {δ p:ℝ} (hδ:δ∈Set.Icc (69/128:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (31/64:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_003_pos hδ hp) hR
theorem envelope_edge131_3_004 {δ p:ℝ} (hδ:δ∈Set.Icc (33/64:ℝ) (69/128:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow30.Available δ p := by
  change δ∈Set.Icc (33/64:ℝ) (69/128:ℝ) ∧ p∈Set.Icc (15/32:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow30 window30_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_004_pos hδ hp) hR
theorem envelope_edge131_3_005 {δ p:ℝ} (hδ:δ∈Set.Icc (33/64:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (15/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_005_pos hδ hp) hR
theorem envelope_edge131_3_006 {δ p:ℝ} (hδ:δ∈Set.Icc (15/32:ℝ) (33/64:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow29.Available δ p := by
  change δ∈Set.Icc (15/32:ℝ) (33/64:ℝ) ∧ p∈Set.Icc (7/16:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow29 window29_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_006_pos hδ hp) hR
theorem envelope_edge131_3_007 {δ p:ℝ} (hδ:δ∈Set.Icc (15/32:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_007_pos hδ hp) hR
theorem envelope_edge131_3_008 {δ p:ℝ} (hδ:δ∈Set.Icc (117/256:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_008_pos hδ hp) hR
theorem envelope_edge131_3_009 {δ p:ℝ} (hδ:δ∈Set.Icc (231/512:ℝ) (117/256:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_009_pos hδ hp) hR
theorem envelope_edge131_3_010 {δ p:ℝ} (hδ:δ∈Set.Icc (459/1024:ℝ) (231/512:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_010_pos hδ hp) hR
theorem envelope_edge131_3_011 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (459/1024:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_011_pos hδ hp) hR
theorem envelope_edge131_3_012 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (231/512:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (127/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_012_pos hδ hp) hR
theorem envelope_edge131_3_013 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (117/256:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (63/128:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_013_pos hδ hp) hR
theorem envelope_edge131_3_014 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (31/64:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_014_pos hδ hp) hR
theorem envelope_edge131_3_015 {δ p:ℝ} (hδ:δ∈Set.Icc (3645/8192:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (1023/2048:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_015_pos hδ hp) hR
theorem envelope_edge131_3_016 {δ p:ℝ} (hδ:δ∈Set.Icc (7287/16384:ℝ) (3645/8192:ℝ)) (hp:p∈Set.Icc (2047/4096:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_016_pos hδ hp) hR
theorem envelope_edge131_3_017 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (7287/16384:ℝ)) (hp:p∈Set.Icc (2047/4096:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_017_pos hδ hp) hR
theorem envelope_edge131_3_018 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (3645/8192:ℝ)) (hp:p∈Set.Icc (1023/2048:ℝ) (2047/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_018_pos hδ hp) hR
theorem envelope_edge131_3_019 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (511/1024:ℝ) (1023/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_019_pos hδ hp) hR
theorem envelope_edge131_3_020 {δ p:ℝ} (hδ:δ∈Set.Icc (909/2048:ℝ) (1821/4096:ℝ)) (hp:p∈Set.Icc (511/1024:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_020_pos hδ hp) hR
theorem envelope_edge131_3_021 {δ p:ℝ} (hδ:δ∈Set.Icc (909/2048:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (255/512:ℝ) (511/1024:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_021_pos hδ hp) hR
theorem envelope_edge131_3_022 {δ p:ℝ} (hδ:δ∈Set.Icc (453/1024:ℝ) (909/2048:ℝ)) (hp:p∈Set.Icc (255/512:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow33.Available δ p := by
  change δ∈Set.Icc (11/25:ℝ) (9/20:ℝ) ∧ p∈Set.Icc (49/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C131 δ p/countJ .C131 δ p := finiteEnvelope_le_window returnWindow33 window33_mem ha
 exact exponent_lt_of_margin (countJ_pos .C131 hd0 hp0) (edge131_3_022_pos hδ hp) hR
theorem envelope_edge131_3_023 {δ p:ℝ} (hδ:δ∈Set.Icc (453/1024:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (255/512:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_023_pos hδ hp) hR
theorem envelope_edge131_3_024 {δ p:ℝ} (hδ:δ∈Set.Icc (225/512:ℝ) (453/1024:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_024_pos hδ hp) hR
theorem envelope_edge131_3_025 {δ p:ℝ} (hδ:δ∈Set.Icc (225/512:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (127/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_025_pos hδ hp) hR
theorem envelope_edge131_3_026 {δ p:ℝ} (hδ:δ∈Set.Icc (111/256:ℝ) (225/512:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_026_pos hδ hp) hR
theorem envelope_edge131_3_027 {δ p:ℝ} (hδ:δ∈Set.Icc (111/256:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (63/128:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_027_pos hδ hp) hR
theorem envelope_edge131_3_028 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (111/256:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_028_pos hδ hp) hR
theorem envelope_edge131_3_029 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (31/64:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_029_pos hδ hp) hR
theorem envelope_edge131_3_030 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (15/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_030_pos hδ hp) hR
theorem envelope_edge131_3_031 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_031_pos hδ hp) hR
theorem envelope_edge131_3_032 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow08.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (51/128:ℝ) ∧ p∈Set.Icc (7/16:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow08 window08_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_032_pos hδ hp) hR
theorem envelope_edge131_3_033 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (15/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_033_pos hδ hp) hR
theorem envelope_edge131_3_034 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (15/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow08.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (51/128:ℝ) ∧ p∈Set.Icc (7/16:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow08 window08_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_034_pos hδ hp) hR
theorem envelope_edge131_3_035 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow07.Available δ p := by
  change δ∈Set.Icc (27/64:ℝ) (15/32:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .C δ p/countJ .C δ p := finiteEnvelope_le_window returnWindow07 window07_mem ha
 exact exponent_lt_of_margin (countJ_pos .C hd0 hp0) (edge131_3_035_pos hδ hp) hR
theorem envelope_edge131_3_036 {δ p:ℝ} (hδ:δ∈Set.Icc (105/256:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_036_pos hδ hp) hR
theorem envelope_edge131_3_037 {δ p:ℝ} (hδ:δ∈Set.Icc (207/512:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_037_pos hδ hp) hR
theorem envelope_edge131_3_038 {δ p:ℝ} (hδ:δ∈Set.Icc (207/512:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (111/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_038_pos hδ hp) hR
theorem envelope_edge131_3_039 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (207/512:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_039_pos hδ hp) hR
theorem envelope_edge131_3_040 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (207/512:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (111/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_040_pos hδ hp) hR
theorem envelope_edge131_3_041 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (55/128:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_041_pos hδ hp) hR
theorem envelope_edge131_3_042 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (13/32:ℝ) (27/64:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_042_pos hδ hp) hR
theorem envelope_edge131_3_043 {δ p:ℝ} (hδ:δ∈Set.Icc (1629/4096:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_043_pos hδ hp) hR
theorem envelope_edge131_3_044 {δ p:ℝ} (hδ:δ∈Set.Icc (3255/8192:ℝ) (1629/4096:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_044_pos hδ hp) hR
theorem envelope_edge131_3_045 {δ p:ℝ} (hδ:δ∈Set.Icc (6507/16384:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_045_pos hδ hp) hR
theorem envelope_edge131_3_046 {δ p:ℝ} (hδ:δ∈Set.Icc (13011/32768:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3583/8192:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_046_pos hδ hp) hR
theorem envelope_edge131_3_047 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (13011/32768:ℝ)) (hp:p∈Set.Icc (3583/8192:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_047_pos hδ hp) hR
theorem envelope_edge131_3_048 {δ p:ℝ} (hδ:δ∈Set.Icc (13011/32768:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (3583/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_048_pos hδ hp) hR
theorem envelope_edge131_3_049 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (13011/32768:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (3583/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_049_pos hδ hp) hR
theorem envelope_edge131_3_050 {δ p:ℝ} (hδ:δ∈Set.Icc (6507/16384:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_050_pos hδ hp) hR
theorem envelope_edge131_3_051 {δ p:ℝ} (hδ:δ∈Set.Icc (13011/32768:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3581/8192:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_051_pos hδ hp) hR
theorem envelope_edge131_3_052 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (13011/32768:ℝ)) (hp:p∈Set.Icc (3581/8192:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_052_pos hδ hp) hR
theorem envelope_edge131_3_053 {δ p:ℝ} (hδ:δ∈Set.Icc (13011/32768:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (3581/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_053_pos hδ hp) hR
theorem envelope_edge131_3_054 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (13011/32768:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (3581/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_054_pos hδ hp) hR
theorem envelope_edge131_3_055 {δ p:ℝ} (hδ:δ∈Set.Icc (3255/8192:ℝ) (1629/4096:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_055_pos hδ hp) hR
theorem envelope_edge131_3_056 {δ p:ℝ} (hδ:δ∈Set.Icc (6507/16384:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (1789/4096:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_056_pos hδ hp) hR
theorem envelope_edge131_3_057 {δ p:ℝ} (hδ:δ∈Set.Icc (13011/32768:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3579/8192:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow09.Available δ p := by
  change δ∈Set.Icc (397/1000:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .weakC7 δ p/countJ .weakC7 δ p := finiteEnvelope_le_window returnWindow09 window09_mem ha
 exact exponent_lt_of_margin (countJ_pos .weakC7 hd0 hp0) (edge131_3_057_pos hδ hp) hR
theorem envelope_edge131_3_058 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (13011/32768:ℝ)) (hp:p∈Set.Icc (3579/8192:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_058_pos hδ hp) hR
theorem envelope_edge131_3_059 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (1789/4096:ℝ) (3579/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_059_pos hδ hp) hR
theorem envelope_edge131_3_060 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (1789/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_060_pos hδ hp) hR
theorem envelope_edge131_3_061 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (447/1024:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_061_pos hδ hp) hR
theorem envelope_edge131_3_062 {δ p:ℝ} (hδ:δ∈Set.Icc (405/1024:ℝ) (813/2048:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_062_pos hδ hp) hR
theorem envelope_edge131_3_063 {δ p:ℝ} (hδ:δ∈Set.Icc (405/1024:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (223/512:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_063_pos hδ hp) hR
theorem envelope_edge131_3_064 {δ p:ℝ} (hδ:δ∈Set.Icc (201/512:ℝ) (405/1024:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_064_pos hδ hp) hR
theorem envelope_edge131_3_065 {δ p:ℝ} (hδ:δ∈Set.Icc (201/512:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (111/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_065_pos hδ hp) hR
theorem envelope_edge131_3_066 {δ p:ℝ} (hδ:δ∈Set.Icc (801/2048:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow32.Available δ p := by
  change δ∈Set.Icc (39/100:ℝ) (3971/10000:ℝ) ∧ p∈Set.Icc (43/100:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow32 window32_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_066_pos hδ hp) hR
theorem envelope_edge131_3_067 {δ p:ℝ} (hδ:δ∈Set.Icc (399/1024:ℝ) (801/2048:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_067_pos hδ hp) hR
theorem envelope_edge131_3_068 {δ p:ℝ} (hδ:δ∈Set.Icc (399/1024:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (223/512:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_068_pos hδ hp) hR
theorem envelope_edge131_3_069 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (399/1024:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_069_pos hδ hp) hR
theorem envelope_edge131_3_070 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (111/256:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_070_pos hδ hp) hR
theorem envelope_edge131_3_071 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (55/128:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_071_pos hδ hp) hR
theorem envelope_edge131_3_072 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (99/256:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_072_pos hδ hp) hR
theorem envelope_edge131_3_073 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (13/32:ℝ) (27/64:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_073_pos hδ hp) hR
theorem envelope_edge131_3_074 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (13/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow04.Available δ p := by
  change δ∈Set.Icc (3/8:ℝ) (27/64:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow04 window04_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_074_pos hδ hp) hR
theorem envelope_edge131_3_075 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (3/8:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_075_pos hδ hp) hR
theorem envelope_edge131_3_076 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/4:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_076_pos hδ hp) hR
theorem envelope_edge131_3_077 {δ p:ℝ} (hδ:δ∈Set.Icc (21/64:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow03.Available δ p := by
  change δ∈Set.Icc (21/64:ℝ) (3/8:ℝ) ∧ p∈Set.Icc (7/16:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capC δ p/countJ .capC δ p := finiteEnvelope_le_window returnWindow03 window03_mem ha
 exact exponent_lt_of_margin (countJ_pos .capC hd0 hp0) (edge131_3_077_pos hδ hp) hR
theorem envelope_edge131_3_078 {δ p:ℝ} (hδ:δ∈Set.Icc (9/32:ℝ) (21/64:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow01.Available δ p := by
  change δ∈Set.Icc (9/32:ℝ) (3/8:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow01 window01_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_078_pos hδ hp) hR
theorem envelope_edge131_3_079 {δ p:ℝ} (hδ:δ∈Set.Icc (9/32:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have ha : returnWindow01.Available δ p := by
  change δ∈Set.Icc (9/32:ℝ) (3/8:ℝ) ∧ p∈Set.Icc (3/8:ℝ) (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .capP δ p/countJ .capP δ p := finiteEnvelope_le_window returnWindow01 window01_mem ha
 exact exponent_lt_of_margin (countJ_pos .capP hd0 hp0) (edge131_3_079_pos hδ hp) hR
theorem envelope_edge131_3_080 {δ p:ℝ} (hδ:δ∈Set.Icc (3/16:ℝ) (9/32:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_080_pos hδ hp) hR
theorem envelope_edge131_3_081 {δ p:ℝ} (hδ:δ∈Set.Icc (3/16:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (3/8:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_081_pos hδ hp) hR
theorem envelope_edge131_3_082 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/16:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_082_pos hδ hp) hR
theorem envelope_edge131_3_083 {δ p:ℝ} (hδ:δ∈Set.Icc (3/16:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/4:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_083_pos hδ hp) hR
theorem envelope_edge131_3_084 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/16:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/4:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
 have hR := finiteEnvelope_le_old hd0 hp0
 exact exponent_lt_of_margin (countJ_pos .old hd0 hp0) (edge131_3_084_pos hδ hp) hR
theorem cover131_3_001 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/4:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3/16:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_084 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_083 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_002 {δ p:ℝ} (hδ:δ∈Set.Icc (9/32:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (21/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_078 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_077 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_003 {δ p:ℝ} (hδ:δ∈Set.Icc (9/32:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (7/16:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_079 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_002 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_004 {δ p:ℝ} (hδ:δ∈Set.Icc (3/16:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (9/32:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_080 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_003 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_005 {δ p:ℝ} (hδ:δ∈Set.Icc (3/16:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (3/8:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_081 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_004 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_006 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3/16:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_082 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_005 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_007 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/8:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (1/4:ℝ) with hsplit | hsplit
 · exact cover131_3_001 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_006 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_008 {δ p:ℝ} (hδ:δ∈Set.Icc (399/1024:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (801/2048:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_067 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_066 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_009 {δ p:ℝ} (hδ:δ∈Set.Icc (399/1024:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (223/512:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_068 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_008 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_010 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (399/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_069 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_009 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_011 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (201/512:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (111/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_070 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_010 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_012 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3579/8192:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (13011/32768:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_058 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_057 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_013 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (1789/4096:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (3579/8192:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_059 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_012 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_014 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (1789/4096:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (6507/16384:ℝ) with hsplit | hsplit
 · exact cover131_3_013 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_056 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_015 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (1789/4096:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_060 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_014 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_016 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (1629/4096:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (895/2048:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3255/8192:ℝ) with hsplit | hsplit
 · exact cover131_3_015 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_055 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_017 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (3581/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (13011/32768:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_054 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_053 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_018 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3581/8192:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (13011/32768:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_052 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_051 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_019 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (3581/8192:ℝ) with hsplit | hsplit
 · exact cover131_3_017 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_018 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_020 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (1791/4096:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (6507/16384:ℝ) with hsplit | hsplit
 · exact cover131_3_019 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_050 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_021 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (3583/8192:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (13011/32768:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_049 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_048 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_022 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (3583/8192:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (13011/32768:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_047 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_046 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_023 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (6507/16384:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (3583/8192:ℝ) with hsplit | hsplit
 · exact cover131_3_021 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_022 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_024 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (1791/4096:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (6507/16384:ℝ) with hsplit | hsplit
 · exact cover131_3_023 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_045 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_025 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (3255/8192:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (1791/4096:ℝ) with hsplit | hsplit
 · exact cover131_3_020 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_024 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_026 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (1629/4096:ℝ)) (hp:p∈Set.Icc (895/2048:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3255/8192:ℝ) with hsplit | hsplit
 · exact cover131_3_025 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_044 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_027 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (1629/4096:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (895/2048:ℝ) with hsplit | hsplit
 · exact cover131_3_016 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_026 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_028 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (447/1024:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (1629/4096:ℝ) with hsplit | hsplit
 · exact cover131_3_027 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_043 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_029 {δ p:ℝ} (hδ:δ∈Set.Icc (813/2048:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (447/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_061 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_028 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_030 {δ p:ℝ} (hδ:δ∈Set.Icc (405/1024:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (223/512:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (813/2048:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_062 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_029 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_031 {δ p:ℝ} (hδ:δ∈Set.Icc (405/1024:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (223/512:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_063 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_030 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_032 {δ p:ℝ} (hδ:δ∈Set.Icc (201/512:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (111/256:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (405/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_064 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_031 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_033 {δ p:ℝ} (hδ:δ∈Set.Icc (201/512:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (111/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_065 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_032 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_034 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (201/512:ℝ) with hsplit | hsplit
 · exact cover131_3_011 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_033 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_035 {δ p:ℝ} (hδ:δ∈Set.Icc (99/256:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (55/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_071 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_034 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_036 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (99/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_072 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_035 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_037 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (51/128:ℝ)) (hp:p∈Set.Icc (13/32:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (27/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_073 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_036 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_038 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (207/512:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (111/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_040 hδ ⟨hp.1,hsplit⟩
 · exact envelope_edge131_3_039 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_039 {δ p:ℝ} (hδ:δ∈Set.Icc (207/512:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (111/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_038 hδ ⟨hp.1,hsplit⟩
 · exact envelope_edge131_3_037 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_040 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (55/128:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (207/512:ℝ) with hsplit | hsplit
 · exact cover131_3_038 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_039 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_041 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (105/256:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (55/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_041 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_040 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_042 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (27/64:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (105/256:ℝ) with hsplit | hsplit
 · exact cover131_3_041 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_036 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_043 {δ p:ℝ} (hδ:δ∈Set.Icc (51/128:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (13/32:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (27/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_042 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_042 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_044 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (13/32:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (51/128:ℝ) with hsplit | hsplit
 · exact cover131_3_037 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_043 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_045 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (13/32:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_074 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_044 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_046 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (7/16:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (27/64:ℝ) with hsplit | hsplit
 · exact cover131_3_045 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_035 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_047 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (15/32:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (51/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_034 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_033 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_048 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (51/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_032 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_031 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_049 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (27/64:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (15/32:ℝ) with hsplit | hsplit
 · exact cover131_3_047 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_048 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_050 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (3645/8192:ℝ)) (hp:p∈Set.Icc (2047/4096:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (7287/16384:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_017 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_016 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_051 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (3645/8192:ℝ)) (hp:p∈Set.Icc (1023/2048:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (2047/4096:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_018 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_050 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_052 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (1023/2048:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3645/8192:ℝ) with hsplit | hsplit
 · exact cover131_3_051 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_015 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_053 {δ p:ℝ} (hδ:δ∈Set.Icc (1821/4096:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (511/1024:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (1023/2048:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_019 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_052 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_054 {δ p:ℝ} (hδ:δ∈Set.Icc (909/2048:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (511/1024:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (1821/4096:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_020 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_053 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_055 {δ p:ℝ} (hδ:δ∈Set.Icc (909/2048:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (255/512:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (511/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_021 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_054 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_056 {δ p:ℝ} (hδ:δ∈Set.Icc (453/1024:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (255/512:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (909/2048:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_022 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_055 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_057 {δ p:ℝ} (hδ:δ∈Set.Icc (453/1024:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (255/512:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_023 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_056 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_058 {δ p:ℝ} (hδ:δ∈Set.Icc (225/512:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (453/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_024 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_057 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_059 {δ p:ℝ} (hδ:δ∈Set.Icc (225/512:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (127/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_025 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_058 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_060 {δ p:ℝ} (hδ:δ∈Set.Icc (111/256:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (225/512:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_026 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_059 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_061 {δ p:ℝ} (hδ:δ∈Set.Icc (111/256:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (63/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_027 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_060 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_062 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (111/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_028 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_061 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_063 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (57/128:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (31/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_029 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_062 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_064 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (231/512:ℝ)) (hp:p∈Set.Icc (127/256:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (459/1024:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_011 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_010 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_065 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (231/512:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (127/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_012 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_064 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_066 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (117/256:ℝ)) (hp:p∈Set.Icc (63/128:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (231/512:ℝ) with hsplit | hsplit
 · exact cover131_3_065 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_009 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_067 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (117/256:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (63/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_013 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_066 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_068 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (117/256:ℝ) with hsplit | hsplit
 · exact cover131_3_067 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_008 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_069 {δ p:ℝ} (hδ:δ∈Set.Icc (57/128:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (31/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_014 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_068 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_070 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (57/128:ℝ) with hsplit | hsplit
 · exact cover131_3_063 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_069 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_071 {δ p:ℝ} (hδ:δ∈Set.Icc (27/64:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (15/32:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_030 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_070 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_072 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (27/64:ℝ) with hsplit | hsplit
 · exact cover131_3_049 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_071 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_073 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (15/32:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (7/16:ℝ) with hsplit | hsplit
 · exact cover131_3_046 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_072 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_074 {δ p:ℝ} (hδ:δ∈Set.Icc (69/128:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (31/64:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (141/256:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_002 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_001 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_075 {δ p:ℝ} (hδ:δ∈Set.Icc (69/128:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (31/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_003 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_074 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_076 {δ p:ℝ} (hδ:δ∈Set.Icc (33/64:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (15/32:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (69/128:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_004 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_075 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_077 {δ p:ℝ} (hδ:δ∈Set.Icc (33/64:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (15/32:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_005 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_076 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_078 {δ p:ℝ} (hδ:δ∈Set.Icc (15/32:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (7/16:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (33/64:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_006 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_077 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_079 {δ p:ℝ} (hδ:δ∈Set.Icc (15/32:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (7/16:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_007 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_078 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_080 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (3/8:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (15/32:ℝ) with hsplit | hsplit
 · exact cover131_3_073 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_079 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_081 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (9/16:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (3/8:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_075 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_080 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_082 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (1/4:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (9/16:ℝ) with hsplit | hsplit
 · exact cover131_3_081 ⟨hδ.1,hsplit⟩ hp
 · exact envelope_edge131_3_000 ⟨hsplit,hδ.2⟩ hp
theorem cover131_3_083 {δ p:ℝ} (hδ:δ∈Set.Icc (3/8:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total p (1/4:ℝ) with hsplit | hsplit
 · exact envelope_edge131_3_076 hδ ⟨hp.1,hsplit⟩
 · exact cover131_3_082 hδ ⟨hsplit,hp.2⟩
theorem cover131_3_084 {δ p:ℝ} (hδ:δ∈Set.Icc (0:ℝ) (3/4:ℝ)) (hp:p∈Set.Icc (0:ℝ) (1/2:ℝ)) : Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total δ (3/8:ℝ) with hsplit | hsplit
 · exact cover131_3_007 ⟨hδ.1,hsplit⟩ hp
 · exact cover131_3_083 ⟨hsplit,hδ.2⟩ hp
theorem edge_newTop_certificate {δ p:ℝ} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) :
 Ebase (edgeD .newTop) (edgeC .newTop) δ p+3/4*edgeD .newTop*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 exact cover131_3_084 (by simpa using hδ) (by simpa using hp)
theorem closed_envelope_return_cover (e : Edge) {δ p : ℝ} (hδ : δ ∈ Set.Icc 0 (3/4))
 (hp : p ∈ Set.Icc 0 (1/2)) : Ebase (edgeD e) (edgeC e) δ p+3/4*edgeD e*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 cases e with
 | oldSmall => exact edge_oldSmall_certificate hδ hp
 | oldSwitch => exact edge_oldSwitch_certificate hδ hp
 | newSwitch => exact edge_newSwitch_certificate hδ hp
 | newTop => exact edge_newTop_certificate hδ hp
end
end QRH.ArviDensity.Return.FinalEdges
