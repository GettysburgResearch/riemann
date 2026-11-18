#!/usr/bin/env python3
"""Exact rational checks; no packages. Unit-circle H² norms by Parseval.
Run from repository root: python experiments/code/multiple_root_smoothing.py
"""
from fractions import Fraction as F
import json
from pathlib import Path

def residual(w):
    c=[F(0)]*(len(w)+2)
    c[0]=1
    for n,a in enumerate(w):
        c[n]-=a;c[n+1]+=2*a;c[n+2]-=a
    return c

def sqnorm(c):return sum(x*x for x in c)
rows=[]
for N in [1,2,3,5,10,30,100]:
    L=N+2;D=(L+1)*(L+2)
    w=[F(n+1)*(1-F(n,N)) for n in range(N+1)]
    c=residual(w)
    # BCF window has nominal degree N and vanishing top coefficient.
    assert c==[F(0)]+[F(2,N)]*N+[F(-1),F(0)]
    assert sqnorm(c)==1+F(4,N)
    opt=[F((n+1)*(L-n)*(L-n-1),D) for n in range(N+1)]
    r=residual(opt)
    target=[F(2*(2*L+1)-6*k,D) for k in range(L+1)]
    assert r==target
    assert sum(r)==1 and sum(k*x for k,x in enumerate(r))==0
    assert sqnorm(r)==F(2*(2*L+1),D)
    # Projection optimality: residual orthogonal to every (1-z)^2 z^j.
    assert all(r[j]-2*r[j+1]+r[j+2]==0 for j in range(N+1))
    rows.append({'N':N,'linear_window_error_squared':str(sqnorm(c)),
                 'optimal_error_squared':str(sqnorm(r)),
                 'N_times_optimal_error_squared':str(N*sqnorm(r)),
                 'constraints_and_normal_equations':'exactly_verified'})
out=Path(__file__).resolve().parents[1]/'results'/'multiple_root_smoothing.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'arithmetic':'fractions.Fraction','rows':rows},indent=2)+'\n')
print(out)
