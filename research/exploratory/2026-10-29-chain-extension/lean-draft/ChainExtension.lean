/- Experimental wiring only: neither gate parameter below has been discharged.
   This file has not been elaborated; it is not a proof of the endpoint. -/
import Submissions.arvi_density.ChainF50.Chain
import Submissions.arvi_density.Return.Endpoint

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace QRH.ArviDensity.ChainExtension
noncomputable section
open OAI OAI.SevenEighths OAI.SevenEighths.HeckeFamily
open QRH.ArviDensity.Hybrid
open QRH.Record1252270103Return
open QRH.Record12518109Source QRH.Record12518109Existence

abbrev Gate130 : Prop :=
  HybridGatesM (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ)
    (1 / 10 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)
    (1 / 10 : ℝ) (401 / 1000 : ℝ) (51 / 100 : ℝ)

abbrev Gate131 : Prop :=
  HybridGatesM (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ)
    (1 / 10 : ℝ) (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ)
    (1 / 10 : ℝ) (2 / 5 : ℝ) (1 / 10 : ℝ)

/-- A transition with its unproved scalar gate explicitly exposed. -/
theorem source130 (gate : Gate130)
    (hβ : (51 / 100 : ℝ) ≤ HeckeZeroSupremum.beta) :
    QRH.Record1252270103Source.GlobalSource
      (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ) :=
  QRH.ArviDensity.Density.density_step_marked
    (1 / 2 : ℝ) (96232839 / 100000000 : ℝ) (3853 / 2000 : ℝ) (1 / 10 : ℝ)
    (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ)
    (401 / 1000 : ℝ) (51 / 100 : ℝ)
    (by norm_num) (by norm_num) (by norm_num) gate
    ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩ hβ
    (QRH.ArviDensity.ChainF50.source_129 hβ)

/-- The next source is conditional on both separate transition gates. -/
theorem source131 (gate130 : Gate130) (gate131 : Gate131)
    (hβ : (51 / 100 : ℝ) ≤ HeckeZeroSupremum.beta) :
    QRH.Record1252270103Source.GlobalSource
      (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (1 / 10 : ℝ) :=
  QRH.ArviDensity.Density.density_step_marked
    (1 / 2 : ℝ) (120284193 / 125000000 : ℝ) (24073 / 12500 : ℝ) (1 / 10 : ℝ)
    (120284089 / 125000000 : ℝ) (192583 / 100000 : ℝ) (1 / 10 : ℝ)
    (2 / 5 : ℝ) (1 / 10 : ℝ)
    (by norm_num) (by norm_num) (by norm_num) gate131
    ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩ hβ
    (source130 gate130 hβ)

/-- Count capP retains step 64 even when the physical face is step 66. -/
abbrev capPFace : SourceFace :=
  QRH.Record1252270103Return.globalFace (49283557 / 50000000) (4503 / 2000) (31 / 500)
/-- The physical numerator uses step 66 with the independently chosen cap. -/
abbrev physicalFace66 : SourceFace :=
  QRH.Record1252270103Return.globalFace (98507071 / 100000000) (4483 / 2000) (619 / 10000)
/-- The new count face is not a physical source: its lambda is less than 2. -/
abbrev countFace131 : SourceFace :=
  QRH.Record1252270103Return.globalFace (120284089 / 125000000) (192583 / 100000) (9999 / 100000)
abbrev countWindowFace131 : SourceFace :=
  QRH.Record1252270103Return.broadFace (120284089 / 125000000) (192583 / 100000) (9999 / 100000)
abbrev capPWindowFace : SourceFace :=
  QRH.Record1252270103Return.broadFace (49283557 / 50000000) (4503 / 2000) (31 / 500)

-- Literal restriction statements are separate so the two sources cannot be conflated.
theorem capP_restricts :
    (QRH.Record1252270103Source.globalFace (49283557 / 50000000) (4503 / 2000) (1 / 10)).Restricts capPFace := by
  constructor <;> norm_num [capPFace, QRH.Record1252270103Source.globalFace,
    QRH.Record1252270103Return.globalFace]

theorem physical66_restricts :
    (QRH.Record1252270103Source.globalFace (98507071 / 100000000) (4483 / 2000) (1 / 10)).Restricts physicalFace66 := by
  constructor <;> norm_num [physicalFace66, QRH.Record1252270103Source.globalFace,
    QRH.Record1252270103Return.globalFace]

theorem count131_restricts :
    (QRH.Record1252270103Source.globalFace (120284089 / 125000000) (192583 / 100000) (1 / 10)).Restricts countFace131 := by
  constructor <;> norm_num [countFace131, QRH.Record1252270103Source.globalFace,
    QRH.Record1252270103Return.globalFace]

theorem count131_broad_restricts : countFace131.Restricts countWindowFace131 := by
  exact QRH.Record1252270103Return.global_restricts_broad (by norm_num)

theorem capP_broad_restricts : capPFace.Restricts capPWindowFace := by
  exact QRH.Record1252270103Return.global_restricts_broad (by norm_num)

/-- Four independent supplies can use one mesh; this establishes no row bound. -/
theorem four_sources_common_mesh {a b c d : SourceFace}
    (ha : UniformUnitFaceSource a) (hb : UniformUnitFaceSource b)
    (hc : UniformUnitFaceSource c) (hd : UniformUnitFaceSource d)
    {ε : ℝ} (hε : 0 < ε) :
    ∃ mesh : ℝ, 0 < mesh ∧ UnitFaceSource a mesh ε ∧
      UnitFaceSource b mesh ε ∧ UnitFaceSource c mesh ε ∧ UnitFaceSource d mesh ε := by
  obtain ⟨ma, hma, hsa⟩ := ha ε hε
  obtain ⟨mb, hmb, hsb⟩ := hb ε hε
  obtain ⟨mc, hmc, hsc⟩ := hc ε hε
  obtain ⟨md, hmd, hsd⟩ := hd ε hε
  refine ⟨min (min ma mb) (min mc md), lt_min (lt_min hma hmb) (lt_min hmc hmd), ?_, ?_, ?_, ?_⟩
  · exact hsa.mono_mesh ((min_le_left _ _).trans (min_le_left _ _))
  · exact hsb.mono_mesh ((min_le_left _ _).trans (min_le_right _ _))
  · exact hsc.mono_mesh ((min_le_right _ _).trans (min_le_left _ _))
  · exact hsd.mono_mesh ((min_le_right _ _).trans (min_le_right _ _))

/-- Exact four-source interface. Both new gate assumptions remain visible. -/
theorem selected_four_sources (gate130 : Gate130) (gate131 : Gate131)
    (hβ : (51 / 100 : ℝ) ≤ HeckeZeroSupremum.beta) :
    UniformUnitFaceSource QRH.ArviDensity.Return.countGlobal ∧
    UniformUnitFaceSource capPFace ∧ UniformUnitFaceSource physicalFace66 ∧
    UniformUnitFaceSource countFace131 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · exact QRH.ArviDensity.Return.uniform_restrict QRH.ArviDensity.Return.source_restricts_count
      (QRH.ArviDensity.ChainF50.source_129 hβ)
  · exact QRH.ArviDensity.Return.uniform_restrict capP_restricts
      (QRH.ArviDensity.ChainF50.source_64 hβ)
  · exact QRH.ArviDensity.Return.uniform_restrict physical66_restricts
      (QRH.ArviDensity.ChainF50.source_66 hβ)
  · exact QRH.ArviDensity.Return.uniform_restrict count131_restricts
      (source131 gate130 gate131 hβ)

theorem selected_four_sources_common_mesh (gate130 : Gate130) (gate131 : Gate131)
    (hβ : (51 / 100 : ℝ) ≤ HeckeZeroSupremum.beta) {ε : ℝ} (hε : 0 < ε) :
    ∃ mesh : ℝ, 0 < mesh ∧ UnitFaceSource QRH.ArviDensity.Return.countGlobal mesh ε ∧
      UnitFaceSource capPFace mesh ε ∧ UnitFaceSource physicalFace66 mesh ε ∧
      UnitFaceSource countFace131 mesh ε := by
  obtain ⟨ha, hb, hc, hd⟩ := selected_four_sources gate130 gate131 hβ
  exact four_sources_common_mesh ha hb hc hd hε

/-- Count windows use these broad faces at that same selected mesh. -/
theorem selected_count_windows_common_mesh (gate130 : Gate130) (gate131 : Gate131)
    (hβ : (51 / 100 : ℝ) ≤ HeckeZeroSupremum.beta) {ε : ℝ} (hε : 0 < ε) :
    ∃ mesh : ℝ, 0 < mesh ∧ UnitFaceSource QRH.ArviDensity.Return.countGlobal mesh ε ∧
      UnitFaceSource capPWindowFace mesh ε ∧ UnitFaceSource physicalFace66 mesh ε ∧
      UnitFaceSource countWindowFace131 mesh ε := by
  obtain ⟨mesh, hm, ha, hb, hc, hd⟩ := selected_four_sources_common_mesh gate130 gate131 hβ hε
  exact ⟨mesh, hm, ha, unit_source_restrict capP_broad_restricts hb, hc,
    unit_source_restrict count131_broad_restricts hd⟩

end
end QRH.ArviDensity.ChainExtension
