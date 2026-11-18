#!/usr/bin/env python3
"""Exploratory search; every apparent counterexample is rechecked exactly.
Floating searches do not prove the conjecture. Seed and rational root parameters saved.
"""
import random,math,json,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import unit_circle_scalar_window_round3 as exact
rng=random.Random(20261117)
def energy_float(params,M):
 roots=[complex((r*r-p*p)/(r*r+p*p),2*p*r/(r*r+p*p)) for p,r in params]
 b=np.zeros(M,dtype=complex);b[0]=1
 for q in roots:
  for n in range(1,M):b[n]+=q*b[n-1]
 a=b*(1-np.arange(M)/M)**len(roots)
 Q=np.array([1+0j])
 for q in roots:Q=np.convolve(Q,[1,-q])
 res=-np.convolve(Q,a);res[0]+=1
 return float(np.vdot(res,res).real)
def roots_exact(params):return tuple((F(r*r-p*p,r*r+p*p),F(2*p*r,r*r+p*p)) for p,r in params)
summary=[];witness=[]
for m in [3,4,5,6]:
 for M in [1,2,3,5,10,20,40]:
  coal=energy_float([(0,1)]*m,M);best=(0,None)
  for trial in range(1200):
   mode=trial%4
   if mode==0:params=[(0,1)]+[(rng.randint(-100,100),50) for _ in range(m-1)]
   elif mode==1:params=[(0,1)]+[(rng.randint(-10,10),M*5) for _ in range(m-1)]
   elif mode==2:
    t=(rng.randint(-50,50),30);params=[(0,1)]+[t if rng.randrange(2) else(0,1) for _ in range(m-1)]
   else:params=[(0,1)]+[(rng.choice([-1,0,1]),1) for _ in range(m-1)]
   v=energy_float(params,M);ratio=v/coal
   if ratio>best[0]:best=ratio,params
   if ratio>1+1e-7:
    e,_=exact.window_energy(roots_exact(params),M,check_identity=False)
    c,_=exact.window_energy((exact.O,)*m,M,check_identity=False)
    if e>c:
     witness.append({'m':m,'M':M,'params':params,'energy':str(e),'coalesced_energy':str(c),'positive_difference':str(e-c)});break
  summary.append({'m':m,'M':M,'float_best_ratio':best[0],'best_rational_parameters':best[1],'trials':trial+1})
  if witness:break
 if witness:break
out={'status':'exploratory floating search; any witness separately exact-rational verified','seed':20261117,'summary':summary,'exact_counterexamples':witness,'conclusion':'Conjecture refuted by exact witness' if witness else 'No counterexample found; not a proof'}
root=Path(__file__).resolve().parents[2];(root/'experiments/results/scalar_window_coalescence_search_round3.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(summary),'trials':sum(x['trials'] for x in summary),'witness':witness,'max_ratio':max(x['float_best_ratio'] for x in summary)},indent=2))
