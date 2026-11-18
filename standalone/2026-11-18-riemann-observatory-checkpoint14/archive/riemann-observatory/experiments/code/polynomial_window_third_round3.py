"""Independent exact coefficient checks of the unit-circle scalar-window theorem.
Uses rational Gaussian pairs, direct formal-series inversion and direct convolution.
No floating values, asymptotic inference, or formal build.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
B=Path(__file__).resolve().parents[2];Z=(F(0),F(0));O=(F(1),F(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,t):return a[0]*t,a[1]*t
def norm(a):return a[0]*a[0]+a[1]*a[1]
def convolution(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return c
q=(F(3,5),F(4,5));u=(F(5,13),F(12,13));i=(F(0),F(1));minus=(F(-1),F(0))
patterns=[(O,),(q,),(i,),(O,O),(q,q),(O,q),(O,minus),(q,u),(O,i),(O,O,O),(q,q,q),(O,O,q),(O,minus,i),(O,O,O,O),(q,q,q,q),(O,O,q,q),(O,q,i,minus)]
rows=[]
for roots in patterns:
 m=len(roots);assert all(norm(v)==1 for v in roots)
 Q=[O]
 for v in roots:Q=convolution(Q,[O,neg(v)])
 C=sum(k*comb(m,k)**2 for k in range(1,m+1));T={r:sum(comb(m,j)*(j-r)**m for j in range(r+1,m+1)) for r in range(1,m)};K=C*C+sum(v*v for v in T.values())
 assert C==m*comb(2*m-1,m-1)
 for M in range(1,13):
  b=[O]
  for n in range(1,M):
   v=Z
   for j in range(1,min(m,n)+1):v=add(v,mul(Q[j],b[n-j]))
   b.append(neg(v))
  a=[scale(v,F(M-n,M)**m) for n,v in enumerate(b)]
  R=[neg(v) for v in convolution(Q,a)];R[0]=add(R[0],O)
  assert R[0]==Z
  assert all(norm(R[n])<=F(C*C,M*M) for n in range(1,M+1))
  assert all(norm(R[M+r])<=F(T[r]*T[r],M*M) for r in range(1,m))
  E=sum(norm(v) for v in R)
  assert E<=F(C*C,M)+sum(F(v*v,M*M) for v in T.values())<=F(K,M)
  if m==1:assert E==F(1,M)
  if m==2:
   coalesced=F(4,M)+F(3,M*M)-F(2,M**3)
   relative=mul(roots[1],(roots[0][0],-roots[0][1]));power=O;gap=F(0)
   for k in range(1,M+1):
    power=mul(power,relative);lag=(M-k+1)*(2*(M-k)+1)
    gap+=F(2,M**4)*lag*(1-power[0])
   assert coalesced-E==gap and E<=coalesced<=F(5,M)
   if roots[0]==roots[1]:assert E==coalesced
  rows.append({'m':m,'M':M,'roots':[[str(x),str(y)] for x,y in roots],'squared_error':str(E),'K_m':K,'all_coefficient_and_energy_bounds_pass':True})
out={'kind':'independent_exact_direct_series_and_convolution_checks_NOT_general_proof','cases':len(rows),'root_patterns':len(patterns),'M_range':[1,12],'includes_complete_and_partial_collisions':True,'all_pass':True,'method':'Reciprocal coefficients obtained by Qb=1 recurrence, then direct QA convolution over exact rational Gaussian pairs; bounds checked coefficientwise and in energy.','independent_coalesced_m2_identity':'E_M=4/M+3/M^2-2/M^3','m2_sharp_uniform_constant':5,'m2_exact_lag_identity_cases':sum(1 for row in rows if row['m']==2),'scope':'Finite checks support the analytic proof review only; no formal build or growing-m asymptotic claim.','records':rows}
(B/'experiments/results/polynomial_window_third_round3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
