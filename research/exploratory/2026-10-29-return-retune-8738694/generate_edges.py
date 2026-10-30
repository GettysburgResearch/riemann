"""Generate retuned Lean edge certificates in an isolated submission source tree.
Usage: python generate_edges.py --windows PINNED_WINDOWS --out-src ISOLATED_SRC
This mutates Return/Rows/RetuneEdge*.lean and Return/EdgeCertificates.lean.
"""
import argparse, json, sys
from pathlib import Path
import sympy as s
parser=argparse.ArgumentParser();parser.add_argument('--windows',required=True);parser.add_argument('--out-src',required=True);args=parser.parse_args()
here=Path(__file__).resolve().parent
src=(here/'check_rows.py').read_text();src=src[:src.index(' stack=[(R(0)')]
src=src.replace('certificates = []','allchecks = []\ncertificates = []')+' allchecks.append(checks)\n'
oldargv=sys.argv;sys.argv=['check_rows.py','--windows',args.windows];ns={};exec(compile(src,'check_rows.py','exec'),ns);sys.argv=oldargv
R=ns['R']; cs=ns['allchecks'];edges=ns['edges'];windows=ns['windows'];cert=json.loads((here/'edge-certificates.json').read_text());D,P=ns['D'],ns['P']
out=Path(args.out_src)/'Submissions/arvi_density/Return';(out/'Rows').mkdir(parents=True,exist_ok=True)
assert len(cs)==4 and len(cert['edges'])==4

def show(q):
 q=R(q);return f'({q.p}/{q.q}:ℝ)' if q.q!=1 else f'({q.p}:ℝ)'
def values(pol,a,b,c,d,n=2,m=3):
 assert n>=max(i for i,j,q in pol) and m>=max(j for i,j,q in pol)
 powers={(k,l):sum((q*s.binomial(i,k)*a**(i-k)*(b-a)**k*s.binomial(j,l)*c**(j-l)*(d-c)**l for i,j,q in pol if i>=k and j>=l),R(0)) for k in range(n+1) for l in range(m+1)}
 return [[sum((powers[k,l]*s.binomial(i,k)/s.binomial(n,k)*s.binomial(j,l)/s.binomial(m,l) for k in range(i+1) for l in range(j+1)),R(0)) for j in range(m+1)] for i in range(n+1)]

edge_names=['oldSmall','oldSwitch','newSwitch','newTop'];counter=0;leaves=[];files=[]
for ei,ed in enumerate(cert['edges']):
 assert (R(ed['distance']),R(ed['capacity']))==edges[ei]
 pols={n:mar for n,guards,mar in cs[ei]}
 for leaf in ed['leaves']:
  counter+=1;name=f'retuneRow{counter:03}';branch=leaf['branch'];a,b,c,d=map(R,leaf['box']);bern=values(pols[branch],a,b,c,d);minimum=min(map(min,bern))/2
  assert minimum>0 and minimum*2==R(leaf['margin_bernstein_minimum'])
  coeff=[[s.factor((bern[i][j]-minimum)*s.binomial(2,i)*s.binomial(3,j)/(b-a)**2/(d-c)**3) for j in range(4)] for i in range(3)]
  assert all(q>=0 for row in coeff for q in row)
  original=sum(q*D**i*P**j for i,j,q in pols[branch])
  reconstructed=minimum+sum(coeff[i][j]*(D-a)**i*(b-D)**(2-i)*(P-c)**j*(d-P)**(3-j) for i in range(3) for j in range(4))
  assert s.Poly(reconstructed-original,D,P).is_zero, name
  txt=f'def {name}_coefficients : Fin 3 → Fin 4 → ℝ := !['+',\n'.join('!['+', '.join(map(show,row))+']' for row in coeff)+']\n'
  txt+=f'''theorem {name}_identity (δ p : ℝ) : rowMargin .{edge_names[ei]} .{branch} δ p =
 Record12518109.Bernstein.bsum 2 3 {show(minimum)} {name}_coefficients {show(a)} {show(b)} {show(c)} {show(d)} δ p := by
 norm_num [rowMargin,Ebase,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,naturalK,sMinus,mMinus,reserve,numeratorCap,edgeD_{edge_names[ei]},edgeC_{edge_names[ei]},Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,{name}_coefficients,Fin.sum_univ_succ] <;> ring
theorem {name}_pos {{δ p : ℝ}} (hδ : δ ∈ Set.Icc {show(a)} {show(b)})
 (hp : p ∈ Set.Icc {show(c)} {show(d)}) : 0 < rowMargin .{edge_names[ei]} .{branch} δ p := by
 rw [{name}_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [{name}_coefficients]
'''
  leaves.append((ei,leaf,name,txt))
# Keep each module reasonably small.
for first in range(0,len(leaves),18):
 group=leaves[first:first+18];name=f'RetuneEdge{first//18+1:02}'
 path=out/'Rows'/f'{name}.lean';files.append(name)
 path.write_text('/- Experimental retune: exact Bernstein certificates generated from the separately pinned PR94 source. -/\nimport Submissions.arvi_density.Return.Formulas\nset_option autoImplicit false\nset_option linter.unnecessarySeqFocus false\nnamespace QRH.ArviDensity.Return\nnoncomputable section\n'+''.join(v[3] for v in group)+'end\nend QRH.ArviDensity.Return\n')

header='/- Experimental retune: closed covering and envelope proof. -/\nimport Submissions.arvi_density.Return.FinalEnvelopeBounds\n'+''.join(f'import Submissions.arvi_density.Return.Rows.{n}\n' for n in files)+'set_option autoImplicit false\nset_option maxHeartbeats 1000000\nnamespace QRH.ArviDensity.Return.FinalEdges\nopen QRH.Record1252270103Return\nnoncomputable section\n'
for wi in sorted(set(leaf['window'] for _,leaf,_,_ in leaves if leaf['window'] is not None)):
 header+=f'theorem retuneWindow{wi:02}_mem : returnWindow{wi:02}∈returnWindows := by simp [returnWindows]\n'
for ei,leaf,name,_ in leaves:
 a,b,c,d=map(R,leaf['box']);branch=leaf['branch'];edge=edge_names[ei];win=leaf['window']
 header+=f'''theorem envelope_{name} {{δ p:ℝ}} (hδ:δ∈Set.Icc {show(a)} {show(b)}) (hp:p∈Set.Icc {show(c)} {show(d)}) : Ebase (edgeD .{edge}) (edgeC .{edge}) δ p+3/4*edgeD .{edge}*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 have hd0 : δ∈Set.Icc 0 (3/4) := by constructor <;> linarith [hδ.1,hδ.2]
 have hp0 : p∈Set.Icc 0 (1/2) := by constructor <;> linarith [hp.1,hp.2]
'''
 if branch=='old': header+=' have hR := finiteEnvelope_le_old hd0 hp0\n'
 else:
  bn,lo,hi,pl=windows[win-1];assert bn==branch and lo<=a<=b<=hi and pl<=c<=d<=R(1,2)
  header+=f''' have ha : returnWindow{win:02}.Available δ p := by
  change δ∈Set.Icc {show(lo)} {show(hi)} ∧ p∈Set.Icc {show(pl)} (1/2:ℝ)
  constructor <;> constructor <;> linarith [hδ.1,hδ.2,hp.1,hp.2]
 have hR : @GenericCount.envelope finalCountScheme kappa δ p≤countN .{branch} δ p/countJ .{branch} δ p := finiteEnvelope_le_window returnWindow{win:02} retuneWindow{win:02}_mem ha
'''
 header+=f' exact exponent_lt_of_margin (countJ_pos .{branch} hd0 hp0) ({name}_pos hδ hp) hR\n'
# Reconstruct and prove the original closed dyadic subdivision, bottom-up.
node=0
for ei in range(4):
 edge=edge_names[ei]
 lookup={tuple(map(R,v['box'])):n for j,v,n,_ in leaves if j==ei}
 assert len(lookup)==sum(j==ei for j,_,_,_ in leaves)
 visited=set()
 def cover(a,b,c,d,depth):
  global node,header
  box=(a,b,c,d);edge=edge_names[ei]
  if box in lookup:
   visited.add(box)
   return 'envelope_'+lookup[box]
  if depth>45:raise ValueError(('coverage',ei,box))
  if depth%2==0:
   mid=(a+b)/2;left=cover(a,mid,c,d,depth+1);right=cover(mid,b,c,d,depth+1);split='δ';use1=f'{left} ⟨hδ.1,hsplit⟩ hp';use2=f'{right} ⟨hsplit,hδ.2⟩ hp'
  else:
   mid=(c+d)/2;left=cover(a,b,c,mid,depth+1);right=cover(a,b,mid,d,depth+1);split='p';use1=f'{left} hδ ⟨hp.1,hsplit⟩';use2=f'{right} hδ ⟨hsplit,hp.2⟩'
  node+=1;name=f'retuneCover{node:03}'
  header+=f'''theorem {name} {{δ p:ℝ}} (hδ:δ∈Set.Icc {show(a)} {show(b)}) (hp:p∈Set.Icc {show(c)} {show(d)}) : Ebase (edgeD .{edge}) (edgeC .{edge}) δ p+3/4*edgeD .{edge}*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 rcases le_total {split} {show(mid)} with hsplit | hsplit
 · exact {use1}
 · exact {use2}
'''
  return name
 root=cover(R(0),R(3,4),R(0),R(1,2),0)
 assert visited==set(lookup)
 header+=f'''theorem edge_{edge}_certificate {{δ p:ℝ}} (hδ:δ∈Set.Icc 0 (3/4)) (hp:p∈Set.Icc 0 (1/2)) : Ebase (edgeD .{edge}) (edgeC .{edge}) δ p+3/4*edgeD .{edge}*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 exact {root} (by simpa using hδ) (by simpa using hp)
'''
header+='''theorem closed_envelope_return_cover (e : Edge) {δ p : ℝ} (hδ : δ ∈ Set.Icc 0 (3/4))
 (hp : p ∈ Set.Icc 0 (1/2)) : Ebase (edgeD e) (edgeC e) δ p+3/4*edgeD e*(@GenericCount.envelope finalCountScheme kappa δ p)<theta-reserve := by
 cases e with
 | oldSmall => exact edge_oldSmall_certificate hδ hp
 | oldSwitch => exact edge_oldSwitch_certificate hδ hp
 | newSwitch => exact edge_newSwitch_certificate hδ hp
 | newTop => exact edge_newTop_certificate hδ hp
end
end QRH.ArviDensity.Return.FinalEdges
'''
(out/'EdgeCertificates.lean').write_text(header)
print('generated',len(leaves),'rows,',len(files),'row modules and',node,'cover nodes')
