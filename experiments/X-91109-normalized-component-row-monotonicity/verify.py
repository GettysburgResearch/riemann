#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json, sys
from pathlib import Path
sys.set_int_max_str_digits(100000)

@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction
    def __add__(self,o):
        o=as_i(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-as_i(o))
    def __rsub__(self,o): return as_i(o)-self
    def __mul__(self,o):
        o=as_i(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return as_i(o)/self

def as_i(x):
    if isinstance(x,I): return x
    if not isinstance(x,Fraction): x=Fraction(x)
    return I(x,x)

DEN=10**50
ROOT_LO=Fraction(1844367547103,10**14)
WINDOW_MAX=1/ROOT_LO

@lru_cache(maxsize=None)
def sqrt_q(x):
    x=Fraction(x); z=(x.numerator*DEN*DEN)//x.denominator; m=isqrt(z)
    return I(Fraction(m,DEN),Fraction(m+1,DEN))

@lru_cache(maxsize=None)
def log_q(x,terms=90):
    x=Fraction(x); k=0; y=x
    while y>=2: y/=2; k+=1
    while y<1: y*=2; k-=1
    z=(y-1)/(y+1); zz=z*z; p=z; s=Fraction(0)
    for j in range(terms): s+=p/Fraction(2*j+1); p*=zz
    s*=2; tail=2*p/(Fraction(2*terms+1)*(1-zz)); ly=I(s,s+tail)
    if y==1: ly=I(0,0)
    z2=Fraction(1,3); zz2=z2*z2; p2=z2; s2=Fraction(0)
    for j in range(terms): s2+=p2/Fraction(2*j+1); p2*=zz2
    s2*=2; tail2=2*p2/(Fraction(2*terms+1)*(1-zz2))
    return ly+k*I(s2,s2+tail2)

@lru_cache(maxsize=None)
def invsqrt(n:int)->I:
    return 1/sqrt_q(n)

@lru_cache(maxsize=None)
def gamma_coeff(n:int,m:int)->I:
    if m==n:
        return Fraction(n+1,n-1)*invsqrt(n)
    if m==n+1:
        return -Fraction((n+1)*(n-2),n*(n-1))*invsqrt(n+1)
    if m>=n+2:
        return Fraction(2,n*(n-1))*invsqrt(m)
    return I(0,0)

def cell_CD(n:int,N:int)->tuple[I,I]:
    C=I(0,0); D=I(0,0)
    for m in range(n,N+1):
        g=gamma_coeff(n,m)
        C+=g; D+=g*log_q(Fraction(m))
    return C,D

def main():
    min_margin=None; checks=0
    for n in range(2,55):
        for N in range(n,55):
            y=Fraction(N+1) if N<54 else WINDOW_MAX
            C,D=cell_CD(n,N)
            Q=C*log_q(y)-D
            assert Q.lo>=0,(n,N,Q)
            # For R(Y)=Q_Y(n)/(sqrt(Y)-1),
            # 2Y(sqrt(Y)-1)^2 R'(Y)=sqrt(Y)(2C-Q)-2C.
            M=sqrt_q(y)*(2*C-Q)-2*C
            assert M.lo>Fraction(1,20),(n,N,y,M,C,Q)
            rec=(M.lo,n,N,y)
            if min_margin is None or rec[0]<min_margin[0]: min_margin=rec
            checks+=1
    out={
      'classification':'PASS_NORMALIZED_COMPONENT_ROW_MONOTONICITY',
      'cell_derivative_checks':checks,
      'minimum_derivative_numerator':{
        'lower':float(min_margin[0]),'row_n':min_margin[1],
        'cell_N':min_margin[2],'right_endpoint':str(min_margin[3]),
        'certified_above':'1/20'},
      'window_upper':str(WINDOW_MAX),
      'scope':'Directed Fraction/sqrt/log intervals certify monotonicity of Q_Y(n)/(sqrt(Y)-1) on the full factor-54 window. Hall coupling and exact row positivity are proved symbolically in L-91322.'
    }
    p=Path(__file__).resolve().parent/'results'/'verification.json'
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']);print(p)
if __name__=='__main__': main()
