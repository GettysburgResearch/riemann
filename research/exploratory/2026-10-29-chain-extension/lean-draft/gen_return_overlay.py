#!/usr/bin/env python3
"""Create partial, explicitly uncompiled return overlay; NEVER mutate source tree."""
from pathlib import Path
import hashlib
import re
from fractions import Fraction as F
src=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/Return')
dst=Path('/workspace/scratch/chain131-candidate/return-overlay')
dst.mkdir(parents=True,exist_ok=True)
# Windows.lean itself defines returnWindow33 below.  An earlier standalone
# draft used the same declaration, so retaining it would cause a duplicate if
# a full source glob imported both modules.
duplicate=dst/'Window33.lean'
if duplicate.exists(): duplicate.unlink()
expected={'Formulas.lean':'e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b',
 'Constants.lean':'96f2a770b68bc4d3ba34e896995514c040315dbc8584e19dbfe479dced8ce4b7'}
for f,h in expected.items():assert hashlib.sha256((src/f).read_bytes()).hexdigest()==h,f

def replace(s,old,new):
 assert s.count(old)==1,(old,s.count(old));return s.replace(old,new)
s=(src/'Constants.lean').read_text()
s=replace(s,'def c : ℝ := (6306383/50000000:ℝ)','def c : ℝ := (6306537/50000000:ℝ)')
s=replace(s,'def h : ℝ := (8044451/10000000:ℝ)','def h : ℝ := (80599/100000:ℝ)')
s=replace(s,'def numeratorCap : ℝ := (3/50:ℝ)','def numeratorCap : ℝ := (619/10000:ℝ)')
s=replace(s,'def physicalB : ℝ := (49283557/50000000:ℝ)','def physicalB : ℝ := (98507071/100000000:ℝ)')
s=replace(s,'def physicalLambda : ℝ := (4503/2000:ℝ)','def physicalLambda : ℝ := (4483/2000:ℝ)')
s=replace(s,'def countCB : ℝ :=', '''/-- Distinct capP count source, kept at step 64. -/
def capPB : ℝ := (49283557/50000000:ℝ)
def capPL : ℝ := (4503/2000:ℝ)
def capPC : ℝ := (31/500:ℝ)
/-- Extra uncapped count source at step 131. -/
def countNewB : ℝ := (120284089/125000000:ℝ)
def countNewL : ℝ := (192583/100000:ℝ)
def countCB : ℝ :=''')
# Recompute the arithmetic constants; admission and edge proof files still require
# a separate full regeneration and the floor-budget patch remains independent.
c=F(6306537,50000000);h=F(80599,100000);theta=1-c
ell=4*c-F(1,3);x=1+ell-h;y=h-2*ell;k=1-2*c
dp=h+F(1,10**10);dm=F(19,25);d0=F(1,200)
pb=F(98507071,100000000);pl=F(4483,2000);cap=F(619,10000)
old=lambda d:min(d,2*y-d)/(6*k)
new=lambda d:min(cap*d,(2*y-(2-pb)*d)/pl)
q=lambda z:f'{z.numerator}/{z.denominator}'
values=[('c',c),('theta',theta),('h',h),('ell',ell),('x',x),('y',y),('kappa',k),('dp',dp)]
proofs=[]
for name,val in values:
 proofs.append(f'theorem {name}_value : {name} = ({q(val)}:ℝ) := by norm_num [{name},c,h,ell]')
for ed,d,capacity in [('oldSmall',d0,old(d0)),('oldSwitch',dm,old(dm)),
 ('newSwitch',dm,new(dm)),('newTop',dp,new(dp))]:
 proofs.append(f'theorem edgeD_{ed} : edgeD .{ed} = ({q(d)}:ℝ) := by norm_num [edgeD,d0,dm,dp,h]')
 proofs.append(f'theorem edgeC_{ed} : edgeC .{ed} = ({q(capacity)}:ℝ) := by norm_num [edgeC,edgeD,oldCapacity,newCapacity,d0,dm,dp,y,ell,c,h,kappa,numeratorCap,physicalB,physicalLambda]')
proofs += ['theorem geometry_mellin : theta-(4+y-x)/6 = x/2+(y-x)/12 := by',
 ' norm_num [theta,x,y,ell,h,c]','end','end QRH.ArviDensity.Return']
head,sep,_=s.partition('theorem c_value :')
assert sep
s=head+'\n'.join(proofs)+'\n'
(dst/'Constants.lean').write_text(s)
s=(src/'Formulas.lean').read_text()
s=replace(s,'inductive CountBranch | old | C | capC | weakC7 | capP','inductive CountBranch | old | C | capC | weakC7 | capP | C131')
s=replace(s,' | .capP => physicalB',' | .capP => capPB\n | .C131 => countNewB')
s=replace(s,' | .capP => physicalLambda',' | .capP => capPL\n | .C131 => countNewL')
s=replace(s,' | .C | .capC | .weakC7 => countCap',' | .C | .capC | .weakC7 | .C131 => countCap')
s=replace(s,' | .capP => physicalCap',' | .capP => capPC')
(dst/'Formulas.lean').write_text(s)
s=(src/'SourceInlet.lean').read_text()
s=replace(s,'def physicalGlobal : SourceFace := globalFace physicalB physicalLambda physicalCap', '''def physicalGlobal : SourceFace := globalFace physicalB physicalLambda physicalCap
/-- Sources below are count supplies, independent of the physical face. -/
def capPGlobal : SourceFace := globalFace capPB capPL capPC
def countNewGlobal : SourceFace := globalFace countNewB countNewL countCap''')
s=replace(s,'end\nend QRH.ArviDensity.Return', '''/-- Shared mesh for all three independent counting supplies and the physical supply. -/
theorem selected_four_sources_common_mesh
    (hC : UniformUnitFaceSource countGlobal) (hQ : UniformUnitFaceSource capPGlobal)
    (hN : UniformUnitFaceSource countNewGlobal) (hP : UniformUnitFaceSource physicalGlobal)
    {ε : ℝ} (hε : 0 < ε) : ∃mesh : ℝ, 0 < mesh ∧
      UnitFaceSource countGlobal mesh ε ∧ UnitFaceSource capPGlobal mesh ε ∧
      UnitFaceSource countNewGlobal mesh ε ∧ UnitFaceSource physicalGlobal mesh ε := by
  obtain ⟨a, ha, hsa⟩ := hC ε hε
  obtain ⟨b, hb, hsb⟩ := hQ ε hε
  obtain ⟨c, hc, hsc⟩ := hN ε hε
  obtain ⟨d, hd, hsd⟩ := hP ε hε
  refine ⟨min (min a b) (min c d), lt_min (lt_min ha hb) (lt_min hc hd), ?_, ?_, ?_, ?_⟩
  · exact hsa.mono_mesh ((min_le_left _ _).trans (min_le_left _ _))
  · exact hsb.mono_mesh ((min_le_left _ _).trans (min_le_right _ _))
  · exact hsc.mono_mesh ((min_le_right _ _).trans (min_le_left _ _))
  · exact hsd.mono_mesh ((min_le_right _ _).trans (min_le_right _ _))
end
end QRH.ArviDensity.Return''')
(dst/'SourceInlet.lean').write_text(s)
s=(src/'WindowSources.lean').read_text()
s=replace(s,' | .capP => physicalGlobal\n | _ => countGlobal',' | .capP => capPGlobal\n | .C131 => countNewGlobal\n | _ => countGlobal')
s=replace(s,'sourceSupplier,countingSource,broadFace,countGlobal,physicalGlobal,globalFace,\n   branchB,branchL,branchCap,countCB,countCL,countCap,physicalB,physicalLambda,physicalCap',
 '''sourceSupplier,countingSource,broadFace,countGlobal,capPGlobal,countNewGlobal,globalFace,
   branchB,branchL,branchCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL''')
(dst/'WindowSources.lean').write_text(s)
s=(src/'Facts.lean').read_text().replace('branchL,countCL,physicalLambda','branchL,countCL,capPL,countNewL')
s=replace(s,' | capP => exact add_pos_of_pos_of_nonneg (mul_pos hv (had .capP)) (mul_nonneg hdp (haa .capP))',
 ''' | capP => exact add_pos_of_pos_of_nonneg (mul_pos hv (had .capP)) (mul_nonneg hdp (haa .capP))
 | C131 => exact add_pos_of_pos_of_nonneg (mul_pos hv (had .C131)) (mul_nonneg hdp (haa .C131))''')
(dst/'Facts.lean').write_text(s)
s=(src/'CountDecode.lean').read_text().replace('branchL,countCL,physicalLambda','branchL,countCL,capPL,countNewL')
(dst/'CountDecode.lean').write_text(s)
s=(src/'CountWidth.lean').read_text().replace('branchZ,branchCap,countCap,physicalCap','branchZ,branchCap,countCap,capPC')
(dst/'CountWidth.lean').write_text(s)
s=(src/'FinalScheme.lean').read_text()
s=replace(s,' (hC:UniformUnitFaceSource countGlobal) (hP:UniformUnitFaceSource physicalGlobal)\n {ε:ℝ}',
 ''' (hC:UniformUnitFaceSource countGlobal) (hQ:UniformUnitFaceSource capPGlobal)
 (hN:UniformUnitFaceSource countNewGlobal) (hP:UniformUnitFaceSource physicalGlobal)
 {ε:ℝ}''')
s=replace(s,' obtain ⟨mesh,hm,hc,hp⟩ := selected_sources_common_mesh hC hP hε',
 ' obtain ⟨mesh,hm,hc,hq,hn,hp⟩ := selected_four_sources_common_mesh hC hQ hN hP hε')
s=replace(s,' cases v.branch <;> first | exact (v.nonold rfl).elim | exact hc | exact hp',
 ' cases v.branch <;> first | exact (v.nonold rfl).elim | exact hc | exact hq | exact hn')
(dst/'FinalScheme.lean').write_text(s)
s=(src/'EndpointFromSources.lean').read_text()
old=' (hC:UniformUnitFaceSource countGlobal) (hP:UniformUnitFaceSource physicalGlobal)'
new=''' (hC:UniformUnitFaceSource countGlobal) (hQ:UniformUnitFaceSource capPGlobal)
 (hN:UniformUnitFaceSource countNewGlobal) (hP:UniformUnitFaceSource physicalGlobal)'''
assert s.count(old)==5
s=s.replace(old,new)
s=replace(s,'final_windows_common_mesh hC hP hε','final_windows_common_mesh hC hQ hN hP hε')
assert s.count('literal_numerator_of_global_sources hC hP hcap')==4
s=s.replace('literal_numerator_of_global_sources hC hP hcap','literal_numerator_of_global_sources hC hQ hN hP hcap')
(dst/'EndpointFromSources.lean').write_text(s)
s=(src/'Endpoint.lean').read_text()
s=replace(s,'/-- The global face of the physical source `G(49283557/50000000, 4503/2000, 1/10)`. -/',
 '/-- The step-66 physical face; step 64 is supplied separately for capP. -/')
s,n=re.subn(r'/-- \*\*The two-source return\.\*\*.*? -/',
 '/-- Candidate four-source return; all generated inputs remain uncompiled. -/',s,flags=re.S)
assert n==1
s=replace(s,'abbrev physicalSourceFace : SourceFace := QRH.Record1252270103Source.globalFace (49283557/50000000) (4503/2000) (1/10)',
 '''abbrev physicalSourceFace : SourceFace := QRH.Record1252270103Source.globalFace (98507071/100000000) (4483/2000) (1/10)
abbrev capPSourceFace : SourceFace := QRH.Record1252270103Source.globalFace (49283557/50000000) (4503/2000) (1/10)
abbrev countNewSourceFace : SourceFace := QRH.Record1252270103Source.globalFace (120284089/125000000) (192583/100000) (1/10)''')
anchor='theorem uniform_restrict {strong weak : SourceFace} (h : strong.Restricts weak)'
s=replace(s,anchor,'''theorem source_restricts_capP : capPSourceFace.Restricts capPGlobal := by
 constructor <;> norm_num [capPSourceFace,QRH.Record1252270103Source.globalFace,capPGlobal,
  QRH.Record1252270103Return.globalFace,capPB,capPL,capPC]
theorem source_restricts_countNew : countNewSourceFace.Restricts countNewGlobal := by
 constructor <;> norm_num [countNewSourceFace,QRH.Record1252270103Source.globalFace,countNewGlobal,
  QRH.Record1252270103Return.globalFace,countNewB,countNewL,countCap]

'''+anchor)
s=replace(s,'''theorem beta_of_two_global_sources
 (hC:UniformUnitFaceSource countGlobal) (hP:UniformUnitFaceSource physicalGlobal) :
 HeckeZeroSupremum.beta≤theta :=
 Final.beta_of_global_sources hC hP natural_cap_return''', '''theorem beta_of_four_global_sources
 (hC:UniformUnitFaceSource countGlobal) (hQ:UniformUnitFaceSource capPGlobal)
 (hN:UniformUnitFaceSource countNewGlobal) (hP:UniformUnitFaceSource physicalGlobal) :
 HeckeZeroSupremum.beta≤theta :=
 Final.beta_of_global_sources hC hQ hN hP natural_cap_return''')
old='''    (hP : (51/100:ℝ) ≤ HeckeZeroSupremum.beta →
      QRH.Record1252270103Source.GlobalSource (49283557/50000000) (4503/2000) (1/10))'''
new='''    (hQ : (51/100:ℝ) ≤ HeckeZeroSupremum.beta →
      QRH.Record1252270103Source.GlobalSource (49283557/50000000) (4503/2000) (1/10))
    (hN : (51/100:ℝ) ≤ HeckeZeroSupremum.beta →
      QRH.Record1252270103Source.GlobalSource (120284089/125000000) (192583/100000) (1/10))
    (hP : (51/100:ℝ) ≤ HeckeZeroSupremum.beta →
      QRH.Record1252270103Source.GlobalSource (98507071/100000000) (4483/2000) (1/10))'''
assert s.count(old)==2
s=s.replace(old,new)
s=replace(s,'''  · exact beta_of_two_global_sources (uniform_restrict source_restricts_count (hC hbeta))
      (uniform_restrict source_restricts_physical (hP hbeta))''',
'''  · exact beta_of_four_global_sources (uniform_restrict source_restricts_count (hC hbeta))
      (uniform_restrict source_restricts_capP (hQ hbeta))
      (uniform_restrict source_restricts_countNew (hN hbeta))
      (uniform_restrict source_restricts_physical (hP hbeta))''')
s=replace(s,'(beta_le_theta_of_sources hC hP).trans_lt hs',
 '(beta_le_theta_of_sources hC hQ hN hP).trans_lt hs')
s=replace(s,'HeckeZeroSupremum.beta ≤ (43693617/50000000 : ℝ)',
 'HeckeZeroSupremum.beta ≤ (43693463/50000000 : ℝ)')
s=replace(s,'(hs : (43693617 / 50000000 : ℝ) < s.re)',
 '(hs : (43693463 / 50000000 : ℝ) < s.re)')
(dst/'Endpoint.lean').write_text(s)
# Supply the original windows, with window 09 widened as in the external
# certificate, and add the separately certified capC and C131 windows.
s=(src/'Windows.lean').read_text()
s=replace(s,'import Submissions.arvi_density.Return.Rows.Admission31',
 '''import Submissions.arvi_density.Return.Rows.Admission31
import Submissions.arvi_density.Return.Rows.Admission32
import Submissions.arvi_density.Return.Rows.Admission33''')
old='''def returnWindow09 : ReturnCountWindow where
 branch := .weakC7
 nonold := by decide
 deltaLo := (51/128:ℝ)
 deltaHi := (27/64:ℝ)
 pLo := (7/16:ℝ)'''
new='''def returnWindow09 : ReturnCountWindow where
 branch := .weakC7
 nonold := by decide
 deltaLo := (397/1000:ℝ)
 deltaHi := (27/64:ℝ)
 pLo := (43/100:ℝ)'''
s=replace(s,old,new)
marker='def returnWindows : List ReturnCountWindow := ['
extra='''def returnWindow32 : ReturnCountWindow where
 branch := .capC
 nonold := by decide
 deltaLo := (39/100:ℝ)
 deltaHi := (3971/10000:ℝ)
 pLo := (43/100:ℝ)
 deltaBounds := by norm_num
 pBounds := by norm_num
 certificate := admission32_all
def returnWindow33 : ReturnCountWindow where
 branch := .C131
 nonold := by decide
 deltaLo := (11/25:ℝ)
 deltaHi := (9/20:ℝ)
 pLo := (49/100:ℝ)
 deltaBounds := by norm_num
 pBounds := by norm_num
 certificate := admission33_all
'''
s=replace(s,marker,extra+marker)
s=replace(s,'returnWindow29,returnWindow30,returnWindow31]',
 'returnWindow29,returnWindow30,returnWindow31,returnWindow32,returnWindow33]')
(dst/'Windows.lean').write_text(s)
rows=dst/'Rows';rows.mkdir(exist_ok=True)
here=Path(__file__).parent
for i in range(1,34):
 f=f'Admission{i:02}.lean'
 if i in (9,32,33):
  s=(here/f).read_text()
 else:
  s=(src/'Rows'/f).read_text()
  # Existing arithmetic certificate values are unchanged by the split of
  # capP constants, but the simplifier must unfold the new definitions.
  s=s.replace('countCB,countCL,countCap,naturalK',
   'countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK')
 (rows/f).write_text(s)
for fname in ['Constants.lean','Formulas.lean','SourceInlet.lean','WindowSources.lean',
              'Facts.lean','CountDecode.lean','CountWidth.lean','FinalScheme.lean',
              'EndpointFromSources.lean','Endpoint.lean','Windows.lean']:
 p=dst/fname
 p.write_text('/- PARTIAL UNCOMPILED OVERLAY: inherited geometry and certificate comments are stale. -/\n'+p.read_text())
print('Partial overlay in',dst)
print('Incomplete: final-source use, exact retune, windows, cover and certificates.')
