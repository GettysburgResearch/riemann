#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
DEN=10**30

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
        o=as_i(o)
        vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        vals=(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        return I(min(vals),max(vals))
    def __rtruediv__(self,o): return as_i(o)/self

def as_i(x):
    if isinstance(x,I): return x
    x=Fraction(x); return I(x,x)

@lru_cache(None)
def sqrt_i(x:Fraction):
    z=(x.numerator*DEN*DEN)//x.denominator
    m=isqrt(z)
    while (m+1)*(m+1)*x.denominator<=x.numerator*DEN*DEN: m+=1
    while m*m*x.denominator>x.numerator*DEN*DEN: m-=1
    return I(Fraction(m,DEN),Fraction(m+1,DEN))

@lru_cache(None)
def invsqrt_i(n:int): return 1/sqrt_i(Fraction(n))

def bounded_divisors(limit:int):
    out=[(1,1)]
    for p in PRIMES:
        out += [(d*p,-mu) for d,mu in list(out) if d*p<=limit]
    return sorted(out)

DIVS=bounded_divisors(4104)
DIVS_82=[z for z in DIVS if z[0]<=82]
ODD=[d for d,mu in DIVS if mu==-1 and d<4096]

def prefix(t:int,y:Fraction|None=None):
    A=Fraction(0); B=I(Fraction(0),Fraction(0))
    source=DIVS if y is None else DIVS_82
    for d,mu in source:
        if y is not None and Fraction(d)>y: break
        if (mu==1 and d<=t+8) or (mu==-1 and d<=t):
            A += Fraction(mu,d); B += mu*invsqrt_i(d)
    return A,B

def fixed(a,A,B,Ay,By,y):
    s=sqrt_i(y); u=sqrt_i(Fraction(83))
    return a*s*(u*A-Ay/u)-3*B+3*By/u

def active(a,A,B,Ay,By,y,t):
    s=sqrt_i(y); rt=sqrt_i(Fraction(t))
    return a*A*rt-3*B-a*Ay*y/rt+3*By*s/rt

def child_margin(a,Ay,By,y): return a*sqrt_i(y)*Ay-3*By

def certify():
    checks=0
    minimum={4:(None,None),5:(None,None)}
    child_minimum={4:(None,None),5:(None,None)}
    base=sorted({Fraction(1),Fraction(83)}|{Fraction(d) for d,_ in DIVS_82})

    for t in ODD:
        A,B=prefix(t); split=Fraction(t,83)
        points=sorted(q for q in (set(base)|{split}) if 1<=q<=83)
        for left,right in zip(points[:-1],points[1:]):
            Ay,By=prefix(t,left)
            for a in (4,5):
                for cm in (child_margin(a,Ay,By,left),child_margin(a,Ay,By,right)):
                    checks+=1
                    assert cm.lo>0,("child",a,t,left,right,cm)
                    if child_minimum[a][0] is None or cm.lo<child_minimum[a][0]:
                        child_minimum[a]=(cm.lo,(t,left,right))

                if left>=split:
                    candidates=[fixed(a,A,B,Ay,By,left),fixed(a,A,B,Ay,By,right)]
                else:
                    assert right<=split
                    candidates=[active(a,A,B,Ay,By,left,t),active(a,A,B,Ay,By,right,t)]
                    if Ay<0:
                        dl=-2*a*Ay*sqrt_i(left)+3*By
                        dr=-2*a*Ay*sqrt_i(right)+3*By
                        checks+=1
                        assert dl.lo>=0 or dr.hi<=0,("interior vertex",a,t,left,right,dl,dr)

                for index,value in enumerate(candidates):
                    checks+=1
                    assert value.lo>1,("Hall",a,t,left,right,index,value)
                    if minimum[a][0] is None or value.lo<minimum[a][0]:
                        minimum[a]=(value.lo,(t,left,right,index))

    return {
      "classification":"PASS_P79_LOW_PREFIX_CORRECTED_CELL_DERIVATIVE",
      "odd_thresholds":len(ODD),
      "directed_checks":checks,
      "target_margin_certified_above":"1",
      "score_margin_certified_above":"1",
      "minimum_target_lower":str(minimum[4][0]),
      "minimum_target_location":[str(x) for x in minimum[4][1]],
      "minimum_score_lower":str(minimum[5][0]),
      "minimum_score_location":[str(x) for x in minimum[5][1]],
      "minimum_child_target_lower":str(child_minimum[4][0]),
      "minimum_child_score_lower":str(child_minimum[5][0]),
      "scope":("Exact Fraction interval proof over every P79 odd threshold t<4096, "
               "every child activation cell 1<=y<83 and every real "
               "p>=max(83,t/y). Separate target and score Hall feasibility only.")
    }

def main():
    result=certify()
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(out)

if __name__=="__main__": main()
