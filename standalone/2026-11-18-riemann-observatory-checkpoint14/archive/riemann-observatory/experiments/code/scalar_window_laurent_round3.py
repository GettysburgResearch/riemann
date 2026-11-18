#!/usr/bin/env python3
"""Exact integer Laurent coefficients of M^(2m) times squared residual norm.
Each residual coefficient is built from support-size finite differences, independently
of the convolution implementation used by the other exact checker.
"""
from math import comb
from collections import defaultdict
from pathlib import Path
import json

def compositions(n,m):
 if m==1:
  yield(n,);return
 for k in range(n+1):
  for t in compositions(n-k,m-1):yield(k,)+t

def coeffs(m,M):
 E=defaultdict(int)
 for n in range(1,M+m):
  bysize={s:-sum((-1)**k*comb(s,k)*max(M-n+k,0)**m for k in range(s+1)) for s in range(1,min(n,m)+1)}
  row=[(a,bysize[sum(x>0 for x in a)]) for a in compositions(n,m)]
  row=[(a,c) for a,c in row if c]
  for a,ca in row:
   for b,cb in row:
    d=tuple(x-y for x,y in zip(a,b));E[d]+=ca*cb
 return {a:c for a,c in E.items() if c}
summary=[];negative=[]
for m,Ms in [(2,range(1,11)),(3,range(1,11)),(4,range(1,7)),(5,range(1,4))]:
 for M in Ms:
  E=coeffs(m,M);v=[(a,c) for a,c in E.items() if c<0]
  summary.append({'m':m,'M':M,'nonzero_laurent_terms':len(E),'minimum_coefficient':min(E.values()),'negative_terms':len(v)})
  if v:negative.append({'m':m,'M':M,'example_d':v[0][0],'integer_coefficient':v[0][1]})
root=Path(__file__).resolve().parents[2]
out={'status':'exact finite integer computations; not an all-m proof','summary':summary,'negative_coefficient_witnesses':negative,'interpretation':'Any negative witness blocks a coefficientwise-nonnegative Laurent proof, but does not by itself refute the maximum conjecture.'}
(root/'experiments/results/scalar_window_laurent_round3.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(summary),'negative':negative,'maximum_terms':max(x['nonzero_laurent_terms'] for x in summary)},indent=2))
