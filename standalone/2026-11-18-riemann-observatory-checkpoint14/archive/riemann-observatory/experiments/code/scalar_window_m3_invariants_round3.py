#!/usr/bin/env python3
"""Exact symbolic m3 energy in v=|sum q|² and delta=Vandermonde norm².
No symbolic coefficient-sign test is accepted as a universal proof.
"""
import sympy as s,json
from pathlib import Path
S,T,v,u,t,d=s.symbols('S T v u t delta')
def energy(M):
 Q=[1,-S,T,-1];b=[s.Integer(1)]
 for n in range(1,M):b.append(s.expand(-sum(Q[k]*b[n-k] for k in range(1,min(3,n)+1))))
 a=[bn*s.Rational(M-n,M)**3 for n,bn in enumerate(b)]
 r=[s.Integer(0)]*(M+3)
 for i,qi in enumerate(Q):
  for j,aj in enumerate(a):r[i+j]-=qi*aj
 r[0]+=1
 E=s.Poly(s.expand(sum(x*x.xreplace({S:T,T:S}) for x in r)),S,T)
 # Pair conjugate monomials, then X^k+Y^k with X=S³,Y=T³,XY=v³.
 L={0:s.Integer(2),1:2*u}
 for k in range(2,M+5):L[k]=s.expand(2*u*L[k-1]-v**3*L[k-2])
 result=0
 for (aa,bb),c in E.terms():
  assert(aa-bb)%3==0
  if aa==bb:result+=c*v**aa
  elif aa>bb:result+=c*v**bb*L[(aa-bb)//3]
 return s.expand(result)
out=[]
for M in range(1,9):
 E=energy(M);gap=s.expand(E.subs({v:9,u:27})-E.subs({u:(d-27+18*v+v*v)/8}).subs(v,9-t))
 out.append({'M':M,'E_v_u':str(E),'gap_t_delta':str(s.factor(gap)),'gap_expanded':str(gap)})
root=Path(__file__).resolve().parents[2];(root/'experiments/results/scalar_window_m3_invariants_round3.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:print(r['M'],r['gap_t_delta'])
