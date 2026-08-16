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
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asI(o))
    def __rsub__(self,o): return asI(o)-self
    def __mul__(self,o):
        o=asI(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o); assert not (o.lo<=0<=o.hi)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return asI(o)/self

def asI(x):
    if isinstance(x,I): return x
    if not isinstance(x,Fraction): x=Fraction(x)
    return I(x,x)

DEN=10**80

def sqrtQ(x:Fraction)->I:
    z=(x.numerator*DEN*DEN)//x.denominator
    m=isqrt(z)
    return I(Fraction(m,DEN),Fraction(m+1,DEN))

def logQ(x:Fraction,terms:int=220)->I:
    assert x>0
    k=0; y=x
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    z=(y-1)/(y+1); zz=z*z; p=z; s=Fraction(0)
    for j in range(terms):
        s += p/Fraction(2*j+1); p*=zz
    tail=2*p/(Fraction(2*terms+1)*(1-zz))
    ly=I(2*s,2*s+tail)
    z2=Fraction(1,3); zz2=z2*z2; p2=z2; s2=Fraction(0)
    for j in range(terms):
        s2 += p2/Fraction(2*j+1); p2*=zz2
    tail2=2*p2/(Fraction(2*terms+1)*(1-zz2))
    l2=I(2*s2,2*s2+tail2)
    return ly+k*l2

def mu_sieve(N:int):
    mu=[0]*(N+1); mu[1]=1; primes=[]; lp=[0]*(N+1)
    for i in range(2,N+1):
        if lp[i]==0:
            lp[i]=i; primes.append(i); mu[i]=-1
        for p in primes:
            if p>lp[i] or i*p>N: break
            lp[i*p]=p
            if i%p==0:
                mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu

def main():
    mu=mu_sieve(55)
    C=I(Fraction(0),Fraction(0))
    for k in range(1,56):
        if not mu[k]: continue
        invsqrt=1/sqrtQ(Fraction(k))
        term=1+Fraction(1,2)*logQ(Fraction(55,k))
        C += abs(mu[k])*invsqrt*term
    assert C.hi < 17

    log4=2*logQ(Fraction(2))
    assert log4.lo > Fraction(4,3)
    rel=Fraction(232)/log4
    assert rel.hi < 174

    c0lo=Fraction(1844367547103,10**14)
    assert c0lo > Fraction(1,55)
    assert Fraction(1,55) > Fraction(4,225)
    term=Fraction(800)/sqrtQ(c0lo)
    assert term.hi < 6000

    out={
      "classification":"PASS_FINITE_CONTINUUM_ADJACENT_MISMATCH",
      "C55_upper":float(C.hi),
      "C55_lt_17":True,
      "log4_lower":float(log4.lo),
      "interior_relative_constant_upper":float(rel.hi),
      "interior_relative_constant_lt_174":True,
      "terminal_collar_coefficient_800_over_sqrt_c0_upper":float(term.hi),
      "scope":"Exact Fraction arithmetic with directed rational square-root and atanh-log enclosures. Analytic zeta(3/2)<3 and the carry/detail telescopes are proved in L-91114."
    }
    path=Path(__file__).resolve().parent/"results"/"verification.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["classification"])

if __name__=="__main__":
    main()
