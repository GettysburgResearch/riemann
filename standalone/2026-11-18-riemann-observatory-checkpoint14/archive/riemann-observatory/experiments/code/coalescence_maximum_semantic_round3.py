"""Exact rational search and algebraic diagnostics for the open coalescence maximum.
No floating optimization and no formal build. Absence of a witness is NOT a proof.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import combinations_with_replacement
import json,time
B=Path(__file__).resolve().parents[2];start=time.monotonic();Z=(F(0),F(0));O=(F(1),F(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def conj(a):return a[0],-a[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,t):return a[0]*t,a[1]*t
def norm(a):return a[0]*a[0]+a[1]*a[1]
def conv(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return c
def error(roots,M):
 m=len(roots);Q=[O]
 for q in roots:assert norm(q)==1;Q=conv(Q,[O,neg(q)])
 b=[O]
 for n in range(1,M):
  v=Z
  for j in range(1,min(m,n)+1):v=add(v,mul(Q[j],b[n-j]))
  b.append(neg(v))
 A=[scale(x,F(M-n,M)**m) for n,x in enumerate(b)];R=[neg(x) for x in conv(Q,A)];R[0]=add(R[0],O)
 return sum(norm(x) for x in R)
def key(roots):
 variants=[]
 for anchor in roots:
  v=tuple(sorted(mul(q,conj(anchor)) for q in roots));variants.extend([v,tuple(sorted(conj(q) for q in v))])
 return min(variants)
def serial(roots):return [[str(x),str(y)] for x,y in roots]
q35=(F(3,5),F(4,5));q513=(F(5,13),F(12,13));choices=[O,(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1)),q35,q513];Ms=[1,2,3,4,5,8,12,20]
patterns={};raw_counts={}
for m in [3,4]:
 raw=list(combinations_with_replacement(choices,m))
 for s in [F(1,10),F(1,100),F(1,1000)]:
  q=(F(1-s*s,1+s*s),F(2*s,1+s*s))
  for k in range(1,m):raw.append(tuple([O]*(m-k)+[q]*k))
  if m==3:raw.append((O,q,conj(q)))
  else:raw.extend([(O,O,q,conj(q)),(q,q,conj(q),conj(q))])
 uniq={}
 for roots in raw:uniq.setdefault(key(roots),roots)
 patterns[m]=list(uniq.values());raw_counts[m]=len(raw)
witnesses=[];summaries=[];cases=0
for m,rootslist in patterns.items():
 for M in Ms:
  coal=error([O]*m,M);closest=None
  for roots in rootslist:
   e=error(roots,M);gap=e-coal;cases+=1
   if (m,M) in [(4,2),(3,3)]:
    S=Z
    for q in roots:S=add(S,q)
    v=norm(S)
    if m==4:
     elem2=Z;power2sum=Z
     for i,q in enumerate(roots):
      power2sum=add(power2sum,mul(q,q))
      for j in range(i+1,m):elem2=add(elem2,mul(q,roots[j]))
     certificate=(16-v)*(131-7*v)/128+(36-norm(elem2))*(F(3,4)+v/256)+(16-norm(power2sum))/16
    else:
     disc=F(1)
     for i,q in enumerate(roots):
      for j in range(i+1,m):disc*=norm(add(q,neg(roots[j])))
     t=9-v;certificate=((119-5*t)*disc+t*(1016-41*t-t*t))/1458
    assert certificate==coal-e and certificate>=0
   if gap>0:witnesses.append({'m':m,'M':M,'roots':serial(roots),'error':str(e),'coalesced_error':str(coal),'positive_gap':str(gap)})
   if len(set(roots))>1 and (closest is None or gap>closest[0]):closest=(gap,roots,e)
  summaries.append({'m':m,'M':M,'coalesced_error':str(coal),'closest_nonaligned_gap':str(closest[0]),'closest_nonaligned_roots':serial(closest[1])})
# Exact one-root phase Hessian at complete coalescence. Values are t^2 coefficients.
def rconv(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
hess=[]
for m in range(2,8):
 for M in range(1,65):
  b=[F(comb(n+m-1,m-1)) for n in range(M)];w=[F(M-n,M)**m for n in range(M)]
  a0=[b[n]*w[n] for n in range(M)];a1=[b[n]*F(n,m)*w[n] for n in range(M)];a2=[b[n]*F(n*(2*n+m-1),m*(m+1))*w[n] for n in range(M)]
  q0=[F((-1)**j*comb(m,j)) for j in range(m+1)];q1=[F(0)]+[F(-(-1)**j*comb(m-1,j)) for j in range(m)]
  r0=[-x for x in rconv(q0,a0)];r0[0]+=1
  r1=[-x-y for x,y in zip(rconv(q1,a0),rconv(q0,a1))]
  r2=[-x-2*y-z for x,y,z in zip(rconv(q1,a0),rconv(q1,a1),rconv(q0,a2))]
  H=sum(x*x-y*z for x,y,z in zip(r1,r0,r2));hess.append({'m':m,'M':M,'one_root_phase_t_squared_coefficient':str(H),'sign':(H>0)-(H<0)})
# Independent exact Laurent witness for m3,M2, using scaled residual polynomials.
def pa(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def ps(a,t):return {k:t*v for k,v in a.items() if t*v}
def pm(a,b):
 c={}
 for x,v in a.items():
  for y,w in b.items():k=tuple(a+b for a,b in zip(x,y));c[k]=c.get(k,0)+v*w
 return {k:v for k,v in c.items() if v}
e1={(1,0,0):1,(0,1,0):1,(0,0,1):1};e2={(1,1,0):1,(1,0,1):1,(0,1,1):1};e3={(1,1,1):1}
R=[ps(e1,7),pa(pm(e1,e1),ps(e2,-8)),pa(ps(e3,8),ps(pm(e1,e2),-1)),pm(e1,e3)];target=(-1,-1,2);parts=[]
for row in R:parts.append(sum(v*w for a,v in row.items() for b,w in row.items() if tuple(x-y for x,y in zip(a,b))==target))
assert parts==[0,-6,2,0] and sum(parts)==-4
out={'kind':'exact_finite_counterexample_search_AND_proof_route_diagnostics_NOT_global_theorem','elapsed_seconds':time.monotonic()-start,'root_basis':serial(choices),'raw_pattern_counts':raw_counts,'symmetry_reduced_pattern_counts':{m:len(v) for m,v in patterns.items()},'symmetries_quotiented':'permutation, common rotation, complex conjugation, all exact','M_values':Ms,'exact_root_configuration_cases':cases,'positive_counterexamples':witnesses,'finite_grid_no_counterexample':not witnesses,'closest_cases_by_m_M':summaries,'new_m4_M2_gap_identity_checks':len(patterns[4]),'independent_m3_M3_gap_identity_checks':len(patterns[3]),'exact_hessian_cases':len(hess),'all_hessian_coefficients_strictly_negative':all(row['sign']<0 for row in hess),'hessian_records':hess,'negative_laurent_witness':{'m':3,'M':2,'scaled_energy_factor':64,'lag':list(target),'row_contributions':[str(x) for x in parts],'scaled_coefficient':-4,'unscaled_coefficient':'-1/16','meaning':'Blocks raw nonnegative-Laurent-coefficient argument; NOT a counterexample to coalescence maximum.'},'scope':'Finite exact search plus local Hessian and a failed proof-route witness only. The general maximum remains open; no novelty/RH claim.'}
(B/'experiments/results/coalescence_maximum_semantic_round3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['closest_cases_by_m_M','hessian_records']},indent=2))
