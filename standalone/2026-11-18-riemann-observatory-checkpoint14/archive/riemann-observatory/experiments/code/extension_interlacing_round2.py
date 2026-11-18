#!/usr/bin/env python3
"""Exact endpoint/count checks for a genuine two-sided boundary-extension example."""
from fractions import Fraction as Q
from math import floor
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
th0=Q(2,5);th1=Q(3,20);anchor=Q(0);K=Q(3,10)
def count(th,a,b):
 assert a<=b
 return floor(b-th)-floor(a-th) # spectrum {n+th:n∈Z}, interval(a,b]
def xi(x):
 if x>anchor:return count(th1,anchor,x)-count(th0,anchor,x)
 if x<anchor:return -count(th1,x,anchor)+count(th0,x,anchor)
 return 0
def delta(th,k):return count(th,2*k,4*k)-2*count(th,k,2*k)
heights=[K,2*K,4*K]
counts0=[count(th0,0,x) for x in heights];counts1=[count(th1,0,x) for x in heights]
assert counts0==[0,1,1] and counts1==[1,1,2]
assert delta(th1,K)-delta(th0,K)==3
# Grid includes actual eigenvalue endpoints for both phases.
grid=[Q(j,20) for j in range(-200,201)]
for x in grid:
 assert xi(x) in [0,1]
 if x==anchor:continue
 t=1/(x-anchor)
 # Exact reciprocal-tail reconstruction. Finite n-range contains every point
 # entering these fixed windows; this is a check, not the infinite-dimensional proof.
 def tail(th):
  eigs=[Q(n)+th for n in range(-100,101)]
  resolvents=[1/(lam-anchor) for lam in eigs]
  return sum(r>=t for r in resolvents) if x>anchor else sum(r<t for r in resolvents)
 reconstructed=(tail(th1)-tail(th0))*(1 if x>anchor else -1)
 assert reconstructed==xi(x)
for u in grid[::10]:
 for v in grid[::10]:
  if u<v:assert xi(v)-xi(u)==count(th1,u,v)-count(th0,u,v)
for j in range(1,201):
 k=Q(j,20)
 assert abs(delta(th1,k)-delta(th0,k))<=3
result={'operators':'H_theta=-i d/dx on L2(0,2pi), f(2pi)=exp(2pi i theta)f(0)','common_symmetric_restriction':'S=-i d/dx on H0^1(0,2pi), deficiency(1,1)','theta0':str(th0),'theta1':str(th1),'K':str(K),'heights':[str(x) for x in heights],'counts_H0':counts0,'counts_H1':counts1,'delta_H0':delta(th0,K),'delta_H1':delta(th1,K),'curvature_difference':delta(th1,K)-delta(th0,K),'relative_range_on_test_grid':sorted(set(xi(x) for x in grid)),'checks':'Exact Fraction arithmetic; eigenvalue endpoints included; both reciprocal branches, finite-window additivity and sharp curvature verified. Abstract operator/defect proof is separate.','proof_file':'audits/extension_interlacing_round2.md'}
(R/'experiments/results/extension_interlacing_round2.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
