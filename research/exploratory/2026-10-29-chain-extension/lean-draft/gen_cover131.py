#!/usr/bin/env python3
"""Rebuild the dyadic edge cover and emit uncompiled Lean envelope proofs."""
import json,re
from pathlib import Path
from fractions import Fraction as F
root=Path(__file__).parent
cert=json.loads((root.parent/'return131-certificate.json').read_text())
wintext=Path('/workspace/scratch/chain131-candidate/return-overlay/Windows.lean').read_text()
pat=r'def returnWindow(\d+) : ReturnCountWindow where\s+branch := \.(\w+)\s+nonold := by decide\s+deltaLo := \(([^:]+):ℝ\)\s+deltaHi := \(([^:]+):ℝ\)\s+pLo := \(([^:]+):ℝ\)'
wins={int(i):(name,F(lo),F(hi),F(pl)) for i,name,lo,hi,pl in re.findall(pat,wintext)}
assert len(wins)==33
def q(v):return f'({v.numerator}/{v.denominator}:ℝ)'
edges=['oldSmall','oldSwitch','newSwitch','newTop']
def statement(edge,a,b,c,d):return f'{{δ p:ℝ}} (hδ:δ∈Set.Icc {q(a)} {q(b)}) (hp:p∈Set.Icc {q(c)} {q(d)}) : Ebase (edgeD .{edge}) (edgeC .{edge}) δ p+3/4*edgeD .{edge}*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve'
out=['/- Generated candidate dyadic cover; UNCOMPILED. -/',
 'import Submissions.arvi_density.Return.FinalEnvelopeBounds',
 'import Submissions.arvi_density.Return.Rows.Edges131',
 'set_option autoImplicit false','set_option maxHeartbeats 1000000',
 'namespace QRH.ArviDensity.Return.FinalEdges','open QRH.Record1252270103Return','noncomputable section']
for i in range(1,34):out.append(f'theorem window{i:02}_mem : returnWindow{i:02}∈returnWindows := by simp [returnWindows]')
for ee in cert['edges']:
 edge=edges[ee['index']];i=ee['index'];leaves=ee['leaves'];box_map={}
 for j,leaf in enumerate(leaves):
  a,b,c,d=map(F,leaf['box']);box=(a,b,c,d);assert box not in box_map;box_map[box]=j
  branch='C131' if leaf['branch']=='Cnew' else leaf['branch'];name=f'edge131_{i}_{j:03}';out.append(f'theorem envelope_{name} '+statement(edge,a,b,c,d)+' := by')
  out += [' have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]',
   ' have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]']
  if branch=='old':out.append(' have hR := finiteEnvelope_le_old hd0 hp0')
  else:
   w=leaf['window'];nm,lo,hi,pl=wins[w];assert nm==branch and a>=lo and b<=hi and c>=pl and d<=F(1,2),(i,j,leaf,wins[w])
   out += [f' have ha : returnWindow{w:02}.Available δ p := by',
    f'  change δ∈Set.Icc {q(lo)} {q(hi)} ∧ p∈Set.Icc {q(pl)} (1/2:ℝ)',
    '  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]',
    f' have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .{branch} δ p/countJ .{branch} δ p := finiteEnvelope_le_window returnWindow{w:02} window{w:02}_mem ha']
  out.append(f' exact exponent_lt_of_margin (countJ_pos .{branch} hd0 hp0) ({name}_pos hδ hp) hR')
 counter=[0]
 def visit(box,dep):
  if box in box_map:return f'envelope_edge131_{i}_{box_map[box]:03}'
  a,b,c,d=box
  if dep%2==0:
   mid=(a+b)/2;left=(a,mid,c,d);right=(mid,b,c,d);axis='δ'
  else:
   mid=(c+d)/2;left=(a,b,c,mid);right=(a,b,mid,d);axis='p'
  assert dep<50,(i,box)
  l=visit(left,dep+1);r=visit(right,dep+1);counter[0]+=1;name=f'cover131_{i}_{counter[0]:03}'
  out.append(f'theorem {name} '+statement(edge,a,b,c,d)+' := by')
  out.append(f' rcases le_total {axis} {q(mid)} with hsplit | hsplit')
  if axis=='δ':out.extend([f' · exact {l} ⟨hδ.1,hsplit⟩ hp',f' · exact {r} ⟨hsplit,hδ.2⟩ hp'])
  else:out.extend([f' · exact {l} hδ ⟨hp.1,hsplit⟩',f' · exact {r} hδ ⟨hsplit,hp.2⟩'])
  return name
 top=visit((F(0),F(3,4),F(0),F(1,2)),0)
 out += [f'theorem edge_{edge}_certificate {{δ p:ℝ}} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) :',
  f' Ebase (edgeD .{edge}) (edgeC .{edge}) δ p+3/4*edgeD .{edge}*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by',
  f' exact {top} (by simpa using hδ) (by simpa using hp)']
 print('edge',i,'checked leaf coverage',len(leaves),'internal nodes',counter[0])
out += ['theorem closed_envelope_return_cover (e : Edge) {δ p : ℝ} (hδ : δ ∈ Set.Icc 0 (3/4))',
 ' (hp : p ∈ Set.Icc 0 (1/2)) : Ebase (edgeD e) (edgeC e) δ p+3/4*edgeD e*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by',
 ' cases e with']+[f' | {e} => exact edge_{e}_certificate hδ hp' for e in edges]+['end','end QRH.ArviDensity.Return.FinalEdges','']
(root/'EdgeCertificates131.lean').write_text('\n'.join(out))
