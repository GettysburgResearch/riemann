#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
DEN=10**90

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
        o=as_i(o); v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        v=(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        return I(min(v),max(v))
    def __rtruediv__(self,o): return as_i(o)/self

def as_i(x):
    if isinstance(x,I): return x
    x=Fraction(x); return I(x,x)

def sqrt_i(x):
    x=Fraction(x); z=(x.numerator*DEN*DEN)//x.denominator; m=isqrt(z)
    while (m+1)*(m+1)*x.denominator<=x.numerator*DEN*DEN: m+=1
    while m*m*x.denominator>x.numerator*DEN*DEN: m-=1
    return I(Fraction(m,DEN),Fraction(m+1,DEN))

def invsqrt_i(n): return 1/sqrt_i(n)

def bounded_divisors(primes,limit):
    out=[(1,1)]
    for p in primes:
        out += [(d*p,-mu) for d,mu in list(out) if d*p<=limit]
    return sorted(out)

DIVS_4104=bounded_divisors(PRIMES,4104)
DIVS_82=[z for z in DIVS_4104 if z[0]<=82]
ODD=[d for d,mu in DIVS_4104 if mu==-1 and d<4096]

def prefix(t,y=None):
    A=Fraction(0); B=I(Fraction(0),Fraction(0))
    source=DIVS_4104 if y is None else DIVS_82
    for d,mu in source:
        if y is not None and Fraction(d)>y: break
        if (mu==1 and d<=t+8) or (mu==-1 and d<=t):
            A += Fraction(mu,d); B += mu*invsqrt_i(d)
    return A,B

def fixed(a,A,B,Ay,By,y):
    s=sqrt_i(y); u=sqrt_i(83)
    return a*s*(u*A-Ay/u)-3*B+3*By/u

def active(a,A,B,Ay,By,y,t):
    s=sqrt_i(y); rt=sqrt_i(t)
    return a*A*rt-3*B-a*Ay*y/rt+3*By*s/rt

def convex_global(a,A,B,Ay,By,t):
    rt=sqrt_i(t)
    return a*A*rt-3*B+Fraction(9,4*a)*(By*By)/(Ay*rt)

def child_margin(a,Ay,By,y): return a*sqrt_i(y)*Ay-3*By

def certify():
    minima={4:(None,None),5:(None,None)}; childmins={4:(None,None),5:(None,None)}
    checks=0
    base=sorted({Fraction(1),Fraction(83)}|{Fraction(d) for d,_ in DIVS_82})
    for t in ODD:
        A,B=prefix(t); split=Fraction(t,83)
        points=sorted(q for q in (set(base)|{split}) if 1<=q<=83)
        for left,right in zip(points[:-1],points[1:]):
            if left>=right: continue
            Ay,By=prefix(t,left)
            for a in (4,5):
                for cm in (child_margin(a,Ay,By,left),child_margin(a,Ay,By,right)):
                    checks+=1
                    if cm.lo<=0: raise AssertionError(('child',a,t,left,right,cm))
                    if childmins[a][0] is None or cm.lo<childmins[a][0]:
                        childmins[a]=(cm.lo,{'threshold':t,'left':str(left),'right':str(right)})
                if left>=split:
                    candidates=[fixed(a,A,B,Ay,By,left),fixed(a,A,B,Ay,By,right)]
                elif right<=split:
                    candidates=[active(a,A,B,Ay,By,left,t),active(a,A,B,Ay,By,right,t)]
                    if Ay<0: candidates.append(convex_global(a,A,B,Ay,By,t))
                else: raise AssertionError('split not inserted')
                for k,val in enumerate(candidates):
                    checks+=1
                    if val.lo<=1: raise AssertionError(('Hall',a,t,left,right,k,val))
                    if minima[a][0] is None or val.lo<minima[a][0]:
                        minima[a]=(val.lo,{'threshold':t,'left':str(left),'right':str(right),'candidate':k})
    return {
      'classification':'PASS_P79_FINITE_LOW_PREFIX_TARGET_AND_SCORE_HALL',
      'odd_thresholds':len(ODD),
      'directed_checks':checks,
      'target_margin_certified_above':'1',
      'score_margin_certified_above':'1',
      'minimum_target_lower':str(minima[4][0]),
      'minimum_target_location':minima[4][1],
      'minimum_score_lower':str(minima[5][0]),
      'minimum_score_location':minima[5][1],
      'minimum_child_target_lower':str(childmins[4][0]),
      'minimum_child_score_lower':str(childmins[5][0]),
      'scope':('Exact Fraction interval certificate over every P79 odd threshold t<4096, '
               'every child activation cell 1<=y<83, and all real p>=max(83,t/y). '
               'Separate target and score Hall feasibility is certified; a common '
               'two-ledger transport and RH are not certified here.')
    }

def main():
    result=certify(); out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification']); print(out)

if __name__=='__main__': main()
