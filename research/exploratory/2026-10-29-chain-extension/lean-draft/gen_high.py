#!/usr/bin/env python3
"""Generate candidate Reflect.checkF HIGH checks. No Lean was run.

Replicates Reflect.Fpoly, elevates its t,p Bernstein degree to 3, and searches
simple tm1Y interval covers in y. This is a producer, not authentication;
Lean's checkF must verify generated values against the pinned Lean source.
"""
import sympy as s
from itertools import product
from math import comb, lcm
from pathlib import Path
R=s.Rational
y,t,p=s.symbols('y t p')
STEPS=[
 (130,R(96232839,10**8),R(3853,2000),R(962273544,10**9),R(24073,12500),R(401,1000),R(51,100)),
 (131,R(962273544,10**9),R(24073,12500),R(962272712,10**9),R(192583,100000),R(2,5),R(1,10))]

def branches(B,L,c):
 return [(1,17*p,0,0),(1,16*p,c*p,0),(L-2*p,16*p*(L-2*p),B*p,p),
  (1-p,p*(1-p),p,p),(1-p,0,p+c*p*(1-p),p),
  ((1-p)*(L-2*p),0,p*(L-2*p)+B*p*(1-p),p*(L-2*p)+p*(1-p))]

def expr(B0,L0,B,L,A,D,v,branch):
 U,a,b,e=branch; w=(B0-B)/(L0-L)+v; X=1+D*v; AV=A*v
 E=(L0-L)*X+(6*B0-L0)*A; K=R(999,1000)*L0*A; Y=K*(1-t)+R(3,4)*t*E
 den=R(15,2)*E*U-3*Y*U+(5*E-6*Y)*e
 return s.expand(Y*(5*(X-6*AV)*U*E+(5*E-6*Y)*(a*(w*X-AV)+b*(X-6*AV)))
  +Y*((1-2*p)*(w*X-AV)-((B-(L-1)*w)*X-AV))*den+E*AV*den
  -R(1,10**12)*E*X*den)

def coeff_list(q):
 q=s.Poly(q,y);return [q.nth(i) for i in range(max(0,q.degree())+1)]

def cover(q,k=0,e=0):
 # tm1Y applied to q((k+y)/2^e), up to a positive common scale.
 c=coeff_list(s.expand(q.subs(y,(k+y)/2**e)))
 c += [0]*(5-len(c)); tail=sum(abs(a) for a in c[2:])
 if c[0]>tail and c[0]+c[1]>tail:return [(k,e)]
 if e>=16: raise RuntimeError(('unresolved tm1Y',k,e,c))
 return cover(q,2*k,e+1)+cover(q,2*k+1,e+1)

def qstr(q):
 n,d=map(int,(s.numer(q),s.denom(q)))
 return str(n) if d==1 else f'{n} / {d}'

for idx,B0,L0,B,L,A,D in STEPS:
 width=R(1,10)-(B0-B)/(L0-L)
 print('step',idx,'width',width,flush=True)
 br=branches(B0,L0,R(1,10)); data=[]
 for branch in br:
  P=expr(B0,L0,B,L,A,D,width*y,branch)
  poly=s.Poly(P,y,t,p)
  assert poly.degree(t)<=3 and poly.degree(p)<=3 and poly.degree(y)<=4
  den=lcm(*[int(s.denom(c)) for c in poly.coeffs()])
  p2=s.Poly(s.expand(P.subs(p,p/2)),t,p)
  trees=[]
  for I,J in product(range(4),repeat=2):
   # 72 times the bicubic Bernstein coefficient on [0,1]x[0,1/2].
   q=s.expand(72*sum(p2.nth(i,j)*R(comb(I,i),comb(3,i))*R(comb(J,j),comb(3,j))
      for i in range(I+1) for j in range(J+1))*den)
   trees.append(cover(q))
  data.append((den,trees))
  print('  ',len(data), 'den digits',len(str(den)),'intervals',sum(map(len,trees)),
        'max depth',max(e for tree in trees for _,e in tree),flush=True)
 # Huge base bounds intermediate signed-PP coefficient sums for these small
 # polynomials in practice, but is intentionally NOT claimed proven here.
 base='1'+'0'*500
 out=['/- Generated candidate checks, UNCOMPILED; proof requires kernel elaboration. -/',
  'import Submissions.arvi_density.Cert.Reflect',
  'set_option autoImplicit false','set_option maxHeartbeats 1000000',
  f'namespace QRH.ArviDensity.ChainExtension.High{idx}',
  'noncomputable section',
  'def stepQ : QRH.ArviDensity.Reflect.StepQ :=',
  f'  ⟨{qstr(B0)}, {qstr(L0)}, 1 / 10, {qstr(B)}, {qstr(L)}, {qstr(A)}, {qstr(D)}, 1 / 1000000000000⟩']
 for (i,j),(den,trees) in zip(product(range(2),range(3)),data):
  tr='['+', '.join('['+', '.join(f'({k}, {e})' for k,e in tree)+']' for tree in trees)+']'
  out += [f'def tree{i}{j} : QRH.RepeatedMarks.Faceless.IPoly.UTreeI := .leaf {tr}',
   f'theorem check{i}{j} : QRH.ArviDensity.Reflect.checkF',
   f'    (QRH.ArviDensity.Reflect.fOf stepQ (QRH.ArviDensity.Reflect.br{i}{j} stepQ))',
   f'    ({qstr(width)}) {den} {base} 5 tree{i}{j} = true := by',
   '  decide +kernel']
 out += ['end',f'end QRH.ArviDensity.ChainExtension.High{idx}','']
 (Path(__file__).parent/f'High{idx}.lean').write_text('\n'.join(out))
