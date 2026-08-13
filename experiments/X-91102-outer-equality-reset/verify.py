#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import json
import sys
sys.set_int_max_str_digits(100000)
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
        o=asI(o); vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o)
        assert not (o.lo<=0<=o.hi)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return asI(o)/self

def asI(x):
    if isinstance(x,I): return x
    if not isinstance(x,Fraction): x=Fraction(x)
    return I(x,x)

DEN=10**90

def sqrtQ(x: Fraction)->I:
    assert x>=0
    z=(x.numerator*DEN*DEN)//x.denominator
    m=isqrt(z)
    return I(Fraction(m,DEN),Fraction(m+1,DEN))

def logQ(x: Fraction, terms:int=220)->I:
    assert x>0
    k=0; y=x
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    z=(y-1)/(y+1)
    zz=z*z
    p=z
    s=Fraction(0)
    for j in range(terms):
        s += p/Fraction(2*j+1)
        p *= zz
    s*=2
    tail=2*p/(Fraction(2*terms+1)*(1-zz))
    ly=I(s,s+tail)
    if y==1: ly=I(Fraction(0),Fraction(0))
    z2=Fraction(1,3); zz2=z2*z2; p2=z2; s2=Fraction(0)
    for j in range(terms):
        s2 += p2/Fraction(2*j+1); p2*=zz2
    s2*=2; tail2=2*p2/(Fraction(2*terms+1)*(1-zz2))
    l2=I(s2,s2+tail2)
    return ly + k*l2

def logI(x:I)->I:
    return I(logQ(x.lo).lo,logQ(x.hi).hi)

def mu_sieve(N):
    mu=[0]*(N+1); mu[1]=1; primes=[]; lp=[0]*(N+1)
    for i in range(2,N+1):
        if lp[i]==0: lp[i]=i; primes.append(i); mu[i]=-1
        for p in primes:
            if p>lp[i] or i*p>N: break
            lp[i*p]=p
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu

MU=mu_sieve(55)

def sums(N):
    A=Fraction(0); B=I(Fraction(0),Fraction(0)); C=I(Fraction(0),Fraction(0))
    for k in range(1,N+1):
        m=MU[k]
        if not m: continue
        A += Fraction(m,k)
        invsqrt=sqrtQ(Fraction(k))/k
        B += m*invsqrt
        C += m*(logQ(Fraction(k))*invsqrt)
    return A,B,C

def Ftheta(theta:Fraction,N:int)->I:
    A,B,C=sums(N)
    rt=sqrtQ(theta); lt=logQ(theta)
    return 4*(A-theta)+rt*(4*(1-B)+2*C+2*(B+1)*lt)

def Dx_at_knot(M:int,N:int)->I:
    # x=1/sqrt(M), evaluated with cell sums N
    A,B,C=sums(N)
    x=1/sqrtQ(Fraction(M))
    lx=Fraction(-1,2)*logQ(Fraction(M))
    return -8*x+8+2*C+4*(B+1)*lx

def main():
    # knot signs F(1/N)>0, N=2..54
    min_knot=None
    for N in range(2,55):
        v=Ftheta(Fraction(1,N),N)
        assert v.lo>0,(N,v)
        if min_knot is None or v.lo<min_knot[1]: min_knot=(N,v.lo)
    left55=Ftheta(Fraction(1,55),54)
    assert left55.hi<0,left55

    # endpoint derivatives positive for cells 6..54
    min_der=None
    for N in range(6,55):
        for M in (N+1,N):
            d=Dx_at_knot(M,N)
            assert d.lo>0,(N,M,d)
            if min_der is None or d.lo<min_der[2]: min_der=(N,M,d.lo)

    # cells 3,4,5 have F''<0: (B_N+1)/2 < 1/sqrt(N+1)
    for N in (3,4,5):
        _,B,_=sums(N)
        crit=(B+1)/2
        left=1/sqrtQ(Fraction(N+1))
        assert crit.hi<left.lo,(N,crit,left)
    # left derivative cells 3,4 negative; cell 5 endpoints positive already and derivative shape gives a max
    for N in (3,4):
        d=Dx_at_knot(N+1,N)
        assert d.hi<0,(N,d)

    # cell 2: F' has its maximum at x=(B+1)/2 and that maximum is negative
    _,B2,C2=sums(2)
    xcrit=(B2+1)/2
    dcrit=-8*xcrit+8+2*C2+4*(B2+1)*logI(xcrit)
    assert dcrit.hi<0,dcrit

    # Continuum endpoint equality weight lambda_N(x)=2 sqrt(x) a_N-m_N.
    # It is monotone on each cell, so endpoint checks suffice.
    min_weight=None
    for N in range(1,55):
        A_N,B_N,_=sums(N)
        endpoints=[Fraction(N)]
        if N<54:
            endpoints.append(Fraction(N+1))
        else:
            # theta >= c0 and c0 > lo imply x=1/theta < 1/lo.
            endpoints.append(Fraction(10**14,1844367547103))
        for xx in endpoints:
            weight=2*sqrtQ(xx)*A_N-B_N
            assert weight.lo > Fraction(31,100),(N,xx,weight)
            if min_weight is None or weight.lo<min_weight[2]:
                min_weight=(N,xx,weight.lo)

    # Uniform finite sum-integral error constant on theta >= 1/55.
    cerr=I(Fraction(0),Fraction(0))
    for k in range(1,56):
        if MU[k] == 0:
            continue
        cerr += (logQ(Fraction(55,k)) / sqrtQ(Fraction(k)))
    cout=sqrtQ(Fraction(55))*cerr
    assert cout.hi < 113, cout

    # root bracket
    lo=Fraction(1844367547103,10**14)
    hi=Fraction(1844367547105,10**14)
    flo=Ftheta(lo,54); fhi=Ftheta(hi,54)
    assert flo.hi<0,(flo,)
    assert fhi.lo>0,(fhi,)

    out={
      'classification':'PASS_OUTER_EQUALITY_CORRECTION_ONE_CROSSING',
      'root_bracket':[str(lo),str(hi)],
      'root_decimal_bracket':[float(lo),float(hi)],
      'F_at_root_bracket':[float(flo.hi),float(fhi.lo)],
      'F_at_1_over_55_upper':float(left55.hi),
      'minimum_positive_knot':{'N':min_knot[0],'lower':float(min_knot[1])},
      'minimum_positive_endpoint_derivative':{'cell_N':min_der[0],'knot_M':min_der[1],'lower':float(min_der[2])},
      'uniform_finite_sum_integral_error_constant_upper':float(cout.hi),
      'minimum_outer_continuum_equality_weight':{'cell_N':min_weight[0],'x':float(min_weight[1]),'lower':float(min_weight[2])},
      'scope':'Assertions use exact Fraction arithmetic with directed rational square-root and atanh-log enclosures. Decimal fields are readable summaries only.'
    }
    path=Path(__file__).resolve().parent / 'results' / 'verification.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification'])
    print(path)
if __name__=='__main__': main()
