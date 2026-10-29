#!/usr/bin/env python3
"""Emit candidate edge leaf certificates from exact geometry and leaf boxes.
No trust is placed in JSON minima: recompute every margin and Bernstein array.
"""
import json, hashlib
from pathlib import Path
from math import comb
import sympy as s
root=Path(__file__).parent
cert=json.loads((root.parent/'return131-certificate.json').read_text())
src=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/Return')
for f,h in [('Formulas.lean','e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b'),('Constants.lean','96f2a770b68bc4d3ba34e896995514c040315dbc8584e19dbfe479dced8ce4b7')]:assert hashlib.sha256((src/f).read_bytes()).hexdigest()==h
R=s.Rational;D,P,x,z=s.symbols('D P x z');theta=R(43693463,50000000);h=R(80599,100000)
c=1-theta;ell=4*c-R(1,3);y=h-2*ell;k=1-2*c;sm=R(3,100);nat=(1-R(9,2)*sm)/2;eps=R(1,10**7)
assert R(cert['theta'])==theta and R(cert['h'])==h
B=R(96232839,10**8);L=R(3853,2000);cap=R(9999,100000)
branches={'C':(B,L,cap,False),'weakC7':(B-R(7,4000),L,cap,False),'capC':(B,L,cap,True),'capP':(R(49283557,50000000),R(4503,2000),R(31,500),True),'Cnew':(R(962272712,10**9),R(192583,100000),cap,False)}
def expr(name,dist,capacity):
 V=R(5,6)-D
 if name=='old':
  dd=3-P-2*P/(3*k);aa=2*(1-P)*(1-P/(3*k));J=V*dd+D*aa;N=(1-D)*J+D*aa*V/2
 else:
  b,l,ca,ic=branches[name]; zz=ca-eps
  dd=3-P if ic else 3-P-4*P/l;aa=2 if ic else 2-4*P/l
  c0=1-2*P*zz if ic else 1-2*P*b/l;U=(1-P)*c0
  J=V*dd+D*(1-P)*aa;N=(1-D)*J+V*D*U
 base=R(1,2)+R(13,75)*h-y/2-ell/2-R(9,100)*dist+D/2+D*P*(ell-capacity/2)
 return s.expand((theta-R(1,10**8)-base)*J-R(3,4)*dist*N)
def qstr(q):
 q=R(q);n,d=int(s.numer(q)),int(s.denom(q));return str(n) if d==1 else f'{n}/{d}'
def real(q):return f'({qstr(q)}:ℝ)'
def compute(g,a,b,c,d):
 poly=s.Poly(s.expand(g.subs({D:a+(b-a)*x,P:c+(d-c)*z})),x,z)
 n=max(0,poly.degree(x));m=max(0,poly.degree(z))
 bs={(i,j):sum(poly.nth(k,l)*R(comb(i,k),comb(n,k))*R(comb(j,l),comb(m,l)) for k in range(i+1) for l in range(j+1)) for i in range(n+1) for j in range(m+1)}
 floor=min(bs.values())/2;assert floor>0
 cs={(i,j):s.factor((bs[i,j]-floor)*comb(n,i)*comb(m,j)/((b-a)**n*(d-c)**m)) for i in range(n+1) for j in range(m+1)}
 assert min(cs.values())>=0
 return n,m,floor,cs
unfold='rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm'
out=['/- Generated candidate edges; uncompiled and dependent on the retuned overlay. -/',
 'import Submissions.arvi_density.Return.Formulas','set_option autoImplicit false','set_option linter.unnecessarySeqFocus false','set_option maxHeartbeats 1000000',
 'namespace QRH.ArviDensity.Return','noncomputable section']
edges=['oldSmall','oldSwitch','newSwitch','newTop']
for edge in cert['edges']:
 i=edge['index'];dist=R(edge['distance']);capacity=R(edge['capacity'])
 for j,leaf in enumerate(edge['leaves']):
  a,b,c,d=map(R,leaf['box']);branch=leaf['branch'];g=expr(branch,dist,capacity)
  n,m,f,co=compute(g,a,b,c,d)
  matrix='!['+', '.join('!['+', '.join(real(co[u,v]) for v in range(m+1))+']' for u in range(n+1))+']'
  name=f'edge131_{i}_{j:03}';leanbranch='C131' if branch=='Cnew' else branch
  out += [f'def {name}_coefficients : Fin {n+1} → Fin {m+1} → ℝ := {matrix}',
  f'theorem {name}_identity (δ p : ℝ) : rowMargin .{edges[i]} .{leanbranch} δ p =',
  f' Record12518109.Bernstein.bsum {n} {m} {real(f)} {name}_coefficients {real(a)} {real(b)} {real(c)} {real(d)} δ p := by',
  f' norm_num [{unfold},{name}_coefficients,Fin.sum_univ_succ] <;> ring',
  f'theorem {name}_pos {{δ p : ℝ}} (hδ : δ ∈ Set.Icc {real(a)} {real(b)})',
  f' (hp : p ∈ Set.Icc {real(c)} {real(d)}) : 0 < rowMargin .{edges[i]} .{leanbranch} δ p := by',
  f' rw [{name}_identity]',
  ' apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp',
  ' intro i j',
  f' fin_cases i <;> fin_cases j <;> norm_num [{name}_coefficients]']
 print('edge',i,'generated',len(edge['leaves']),'leaves',flush=True)
out += ['end','end QRH.ArviDensity.Return','']
(root/'Edges131.lean').write_text('\n'.join(out))
