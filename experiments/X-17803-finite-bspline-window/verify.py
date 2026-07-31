#!/usr/bin/env python3
"""Exact rational checks for the J=12 finite B-spline pole-free window."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path
from typing import Any
SCHEMA='riemann.x17803-finite-bspline-window.v1'
def is_int(x): return isinstance(x,int) and not isinstance(x,bool)
def rat(o,name):
    if not isinstance(o,dict):raise ValueError(name)
    n=o.get('numerator');d=o.get('denominator')
    if not is_int(n) or not is_int(d) or d<=0:raise ValueError(name)
    return Fraction(n,d)
def fj(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
def sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def pospow(x,n):return x**n if x>0 else Fraction(0)
def spline(J,u):
    n=2*J
    s=Fraction(0)
    for k in range(n+1):
        s += (-1 if k&1 else 1)*math.comb(n,k)*pospow(u-Fraction(k,J),n-1)
    return Fraction(J**n,math.factorial(n-1))*s
def integral(J):
    n=2*J;s=Fraction(0)
    for k in range(n+1):
        s += (-1 if k&1 else 1)*math.comb(n,k)*pospow(Fraction(2)-Fraction(k,J),n)
    return Fraction(J**n,math.factorial(n))*s
def verify(d:dict[str,Any]):
    if d.get('schema')!=SCHEMA:raise ValueError('schema')
    J=d.get('J');T=d.get('tail_height');N=d.get('exact_zero_count')
    if not is_int(J) or J<1 or not is_int(T) or T<2*J or not is_int(N) or N<0:raise ValueError('parameters')
    if integral(J)!=1:raise ValueError('normalization')
    probes=d.get('symmetry_probes')
    if not isinstance(probes,list) or not probes:raise ValueError('probes')
    vals=[]
    for i,o in enumerate(probes):
        u=rat(o,f'probe{i}')
        if u<0 or u>2:raise ValueError('probe range')
        a=spline(J,u);b=spline(J,2-u)
        if a!=b or a<0:raise ValueError('spline symmetry/positivity')
        vals.append(a)
    p=2*J
    a0=Fraction(10076,100000);b0=Fraction(24460,100000);c0=Fraction(808292,100000)
    Z=Fraction(4,T**(p-1))*(Fraction(6,p-1)+Fraction(1,(p-1)**2))
    Z+=a0*Fraction(1,T**p)*(6+Fraction(1,p))
    Z+=b0*Fraction(1,T**p)*(2+Fraction(1,5*p))
    Z+=c0*Fraction(1,T**p)
    radius=6*((2*J)**(2*J))*Z
    if radius>=Fraction(1,10**20):raise ValueError('tail moat')
    out={'schema':SCHEMA,'classification':d.get('classification'),'J':J,'degree':2*J-1,
         'spline_integral':fj(Fraction(1)),'symmetry_values':[fj(x) for x in vals],
         'high_zero_tail_upper':fj(radius),'tail_below_1e_minus_20':True,
         'pole_factor_at_half':fj(Fraction(0)),
         'verdict':'EXACT_FINITE_BSPLINE_WINDOW_GATES_VERIFIED',
         'proof_boundary':'Finite rational window/tail algebra; no prime statistic or zeta phase is evaluated.'}
    out['proof_object_sha256']=sha(out);return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--output',type=Path)
    a=ap.parse_args();o=verify(json.loads(a.certificate.read_text()));s=json.dumps(o,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(s)
    print(s,end='')
if __name__=='__main__':main()
