#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction
    def __add__(self, other):
        other=as_i(other); return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+(-as_i(other))
    def __mul__(self,other):
        other=as_i(other)
        vals=[self.lo*other.lo,self.lo*other.hi,
              self.hi*other.lo,self.hi*other.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=as_i(other)
        if other.lo<=0<=other.hi: raise ZeroDivisionError
        vals=[self.lo/other.lo,self.lo/other.hi,
              self.hi/other.lo,self.hi/other.hi]
        return I(min(vals),max(vals))
    def __rtruediv__(self,other): return as_i(other)/self


def as_i(x):
    return x if isinstance(x,I) else I(Fraction(x),Fraction(x))


DEN=10**80


def sqrt_i(x:Fraction|int)->I:
    x=Fraction(x)
    z=(x.numerator*DEN*DEN)//x.denominator
    m=isqrt(z)
    return I(Fraction(m,DEN),Fraction(m+1,DEN))


def mobius(N:int):
    mu=[0]*(N+1); mu[1]=1; lp=[0]*(N+1); primes=[]
    for n in range(2,N+1):
        if lp[n]==0:
            lp[n]=n; primes.append(n); mu[n]=-1
        for p in primes:
            if p>lp[n] or p*n>N: break
            lp[p*n]=p
            if n%p==0:
                mu[p*n]=0; break
            mu[p*n]=-mu[n]
    return mu


MU=mobius(54)
ROOT_LO=Fraction(1844367547103,10**14)
X=1/ROOT_LO


def atom(a:Fraction,n:int)->I:
    return a*sqrt_i(X)/n - 1/sqrt_i(n)


def main():
    threshold=31
    margin=I(Fraction(0),Fraction(0))
    even=[]; odd=[]
    for n in range(1,threshold+1):
        if MU[n]==1:
            margin += atom(Fraction(4,3),n); even.append(n)
        elif MU[n]==-1:
            margin -= atom(Fraction(3,2),n); odd.append(n)
    assert margin.hi < Fraction(-3,2), margin
    out={
      'classification':'PASS_HETEROGENEOUS_CORRIDOR_HALL_COUNTEREXAMPLE',
      'x':str(X),
      'threshold':threshold,
      'capacity_parameter':'4/3',
      'demand_parameter':'3/2',
      'directed_upper':str(margin.hi),
      'upper_decimal':float(margin.hi),
      'certified_below':'-3/2',
      'even_states':even,
      'odd_states':odd,
      'scope':(
        'Exact Fraction arithmetic with directed rational square-root '
        'enclosures. This refutes only heterogeneous parameter aggregation; '
        'the common-parameter Hall corridor of L-91331 is retained.'
      )
    }
    path=Path(__file__).resolve().parent/'results'/'verification.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification'])


if __name__=='__main__': main()
