#!/usr/bin/env python3
"""Exact rational-complex checks for the unit-circle scalar-window theorem.
QA is computed by polynomial convolution independently of the subset identity.
These checks supplement the analytic proof; they do not prove its universal quantifiers.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations
from pathlib import Path
import json
Z=(F(0),F(0)); O=(F(1),F(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,b):return a[0]*b,a[1]*b
def norm2(a):return a[0]*a[0]+a[1]*a[1]
def convolution(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return c
def polynomial(roots):
 q=[O]
 for r in roots:q=convolution(q,[O,neg(r)])
 return q
def reciprocal_by_Q(q,count):
 b=[O]
 for n in range(1,count):
  t=Z
  for j in range(1,min(n,len(q)-1)+1):t=add(t,mul(q[j],b[n-j]))
  b.append(neg(t))
 return b
def homogeneous(roots,count):
 # Independently form the product of geometric series, one factor at a time.
 h=[O]+[Z]*(count-1)
 for r in roots:
  for n in range(1,count):h[n]=add(h[n],mul(r,h[n-1]))
 return h
def taper(n,M,m):return F(M-n,M)**m if n<=M else F(0)
def window_energy(roots,M,power=None,check_identity=True):
 m=len(roots);power=m if power is None else power;q=polynomial(roots)
 b=reciprocal_by_Q(q,M);a=[scale(b[n],F(M-n,M)**power) for n in range(M)]
 qa=convolution(q,a);r=[neg(c) for c in qa];r[0]=add(O,r[0]);assert r[0]==Z
 if check_identity:
  assert power==m
  cache=[]
  for k in range(1,m+1):
   for S in combinations(range(m),k):
    qs=O
    for j in S:qs=mul(qs,roots[j])
    hs=homogeneous([roots[j] for j in S],M+m)
    cache.append((k,qs,hs))
  for n in range(M+m):
   v=O if n==0 else Z
   for k,qs,hs in cache:
    if n<k:continue
    delta=sum(((-1)**j*comb(k,j)*taper(n-j,M,m) for j in range(k+1)),F(0))
    v=add(v,scale(mul(qs,hs[n-k]),delta))
   assert v==qa[n],('subset identity',m,M,n,v,qa[n])
 return sum(map(norm2,r),F(0)),r
if __name__ == "__main__":
    q=(F(3,5),F(4,5));qb=(q[0],-q[1]);i=(F(0),F(1));minus=(F(-1),F(0))
    configs=[(O,),(i,),(q,),(O,O),(O,minus),(O,q),(q,q),
     (O,O,O),(O,q,qb),(O,i,minus),(q,q,q),
     (O,)*4,(O,O,q,q),(O,i,minus,neg(i)),(O,)*5,(O,q,qb,i,minus)]
    checks=[]
    for roots in configs:
     assert all(norm2(v)==1 for v in roots)
     m=len(roots);C=m*comb(2*m-1,m-1);T=[sum(comb(m,j)*(j-r)**m for j in range(r+1,m+1)) for r in range(1,m)]
     K=C*C+sum(t*t for t in T)
     for M in [1,2,3,4,7,10,20]:
      energy,r=window_energy(roots,M)
      assert energy<=F(K,M)
      assert energy<=F(C*C,M)+F(sum(t*t for t in T),M*M)
      assert all(norm2(r[n])<=F(C*C,M*M) for n in range(1,M+1))
      for rr,t in enumerate(T,1):assert norm2(r[M+rr])<=F(t*t,M*M)
      if m==1:assert energy==F(1,M)
      checks.append({'m':m,'M':M,'roots':[[str(v[0]),str(v[1])] for v in roots],'energy':str(energy),'K_m':K})
    profiles=[]
    for m in range(1,7):
     for M in [10,30,100,300]:
      energy,_=window_energy((O,)*m,M,check_identity=False)
      profiles.append({'m':m,'M':M,'M_times_energy':str(M*energy),'decimal_display':float(M*energy),'proved_limit':m*m})
    negative=[]
    for m in range(2,6):
     M=30
     for power in range(m):
      energy,r=window_energy((O,)*m,M,power=power,check_identity=False)
      terminal=F(comb(M+m-2,m-1),M**power)
      assert norm2(r[-1])==terminal*terminal
      negative.append({'m':m,'M':M,'power':power,'terminal_squared':str(terminal*terminal),'energy':str(energy)})

    # Exact two-root Laurent identity, including sharp uniform constant5.
    qmax=[]
    for M in [1,2,3,4,7,10,20,30]:
     for qv in [O,minus,i,q,qb]:
      energy,_=window_energy((O,qv),M,check_identity=False)
      ecoal=F(4,M)+F(3,M*M)-F(2,M**3)
      qp=O;gap=F(0)
      for k in range(1,M+1):
       qp=mul(qp,qv);R=(M-k+1)*(2*(M-k)+1)
       gap+=F(2*R,M**4)*(1-qp[0])
      assert ecoal-energy==gap and gap>=0
      assert energy<=F(5,M)
      qmax.append({'M':M,'q':[str(qv[0]),str(qv[1])],'coalescence_gap':str(gap)})

    result={'status':'exact rational-complex supplemental checks; analytic proof supplies universal theorem','identity_and_bound_cases':len(checks),'cases':checks,'coalescence_profiles':profiles,'lower_integer_power_terminal_checks':negative,'exact_two_root_maximum_cases':qmax,'limitations':'Fractions exact; decimal_display approximate for readability. No zeta arithmetic conclusion; no novelty claim.'}
    root=Path(__file__).resolve().parents[2]
    (root/'experiments/results/unit_circle_scalar_window_round3.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'identity_and_bound_cases':len(checks),'coalescence_profiles':len(profiles),'lower_power_cases':len(negative),'K_m':[m*m*comb(2*m-1,m-1)**2+sum(sum(comb(m,j)*(j-r)**m for j in range(r+1,m+1))**2 for r in range(1,m)) for m in range(1,6)]}))
