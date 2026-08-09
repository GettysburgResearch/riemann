#!/usr/bin/env python3
"""Exact/floating replay for the radix-three quartic annular filter."""
from __future__ import annotations
import argparse, importlib.util, json, math
from fractions import Fraction
from pathlib import Path
from math import comb
import mpmath as mp
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'X-90015-annular-endpoint'/'verify.py'
spec=importlib.util.spec_from_file_location('x90015',BASE)
if spec is None or spec.loader is None: raise RuntimeError(BASE)
x90015=importlib.util.module_from_spec(spec); spec.loader.exec_module(x90015)
ANNULUS=81

# Q(sqrt(3)) pairs a+b sqrt(3), ascending coefficients of 18-|P|^2.
H_PAIRS=[
    (Fraction(22,3),Fraction(0)),
    (Fraction(32,3),Fraction(16,3)),
    (Fraction(32,3),Fraction(-16,3)),
    (Fraction(-32,3),Fraction(-16,3)),
    (Fraction(0),Fraction(16,3)),
]
SQRT3_LO=Fraction(1732050807568877,10**15)
SQRT3_HI=Fraction(1732050807568878,10**15)

def add(u,v): return (u[0]+v[0],u[1]+v[1])
def scale(u,r): return (u[0]*r,u[1]*r)
def lower(u):
    a,b=u
    return a+b*(SQRT3_LO if b>=0 else SQRT3_HI)

def compose(pairs,a,b):
    res=[(Fraction(0),Fraction(0))]
    h=b-a
    for c in pairs[::-1]:
        new=[(Fraction(0),Fraction(0)) for _ in range(len(res)+1)]
        for i,u in enumerate(res):
            new[i]=add(new[i],scale(u,a))
            new[i+1]=add(new[i+1],scale(u,h))
        new[0]=add(new[0],c)
        res=new
    while len(res)>1 and res[-1]==(0,0): res.pop()
    return res

def bernstein(power,n=4):
    c=power+[(Fraction(0),Fraction(0))]*(n+1-len(power))
    out=[]
    for k in range(n+1):
        u=(Fraction(0),Fraction(0))
        for j in range(k+1):
            u=add(u,scale(c[j],Fraction(comb(k,j),comb(n,j))))
        out.append(u)
    return out

def exact_sup_certificate():
    rows=[]
    global_min=None
    for i in range(4):
        a=Fraction(-1)+Fraction(i,2)
        b=a+Fraction(1,2)
        bs=bernstein(compose(H_PAIRS,a,b))
        lbs=[lower(u) for u in bs]
        ml=min(lbs)
        if ml<=0: raise AssertionError((i,ml))
        global_min=ml if global_min is None else min(global_min,ml)
        rows.append({'interval':[str(a),str(b)],'minimum_bernstein_lower_bound':str(ml)})
    return {'claim':'max_|y|=1 |P_3(y)|^2 <= 18','subintervals':rows,
            'global_minimum_certificate':str(global_min)}

def constants():
    mp.mp.dps=80; half=mp.mpf('.5')
    def xi(s): return mp.mpf('.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
    S=mp.diff(lambda s:mp.log(xi(s)),half,2)
    zh=mp.zeta(half)
    moat=(1+zh)*(1-1/mp.sqrt(3))*mp.log(3)**2
    zero=mp.sqrt(18)*S
    margin=moat+zero
    scaled=3*margin
    if not margin<mp.mpf('-.038'): raise AssertionError(margin)
    return {'moat':mp.nstr(moat,60),'zero_bound_sqrt18':mp.nstr(zero,60),
            'margin_upper_bound':mp.nstr(margin,60),'scaled_margin_upper_bound':mp.nstr(scaled,60)}

def value(a,x):
    r=math.sqrt(3.0)
    return float(a[x-1]-(1+1/r)*a[x//3-1]+(-1+1/r)*a[x//9-1]
                 +(1+1/r)*a[x//27-1]-(1/r)*a[x//81-1])

def scan(max_x):
    a,_,_=x90015.endpoint_sequence(max_x)
    xs=np.arange(81,max_x+1,81,dtype=np.int64)
    vals=np.array([value(a,int(x)) for x in xs])
    nonneg=xs[vals>=0]
    imax=int(vals.argmax()); imin=int(vals.argmin())
    return {'max_X':max_x,'annulus_factor':81,'tested_multiples':int(len(xs)),
            'nonnegative_count':int(len(nonneg)),
            'first_nonnegative_endpoints':[int(v) for v in nonneg[:20]],
            'last_nonnegative_endpoint':int(nonneg[-1]) if len(nonneg) else None,
            'maximum':{'X':int(xs[imax]),'value':float(vals[imax])},
            'minimum':{'X':int(xs[imin]),'value':float(vals[imin])},
            'last':{'X':int(xs[-1]),'value':float(vals[-1])}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-x',type=int,default=1000000)
    ap.add_argument('--output',type=Path,default=HERE/'results'/'verification.json');args=ap.parse_args()
    out={'classification':'PASS_RADIX3_QUARTIC_ANNULAR_REGRESSION',
         'exact_sup_certificate':exact_sup_certificate(),'constants':constants(),'finite':scan(args.max_x),
         'scope':'The Bernstein certificate is exact over Q(sqrt(3)); the finite endpoint scan is reconnaissance only.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']);print(args.output)
if __name__=='__main__':main()
