#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
import hashlib, json
from pathlib import Path

VERDICT="PASS_T99280_COMPACT_HALL_SUBPOWER_LANDAU_HARDENING"
BITS=96
TERMS=96

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    @staticmethod
    def exact(x):
        return I(x if isinstance(x,F) else F(x), x if isinstance(x,F) else F(x))
    def __add__(self,o):
        o=o if isinstance(o,I) else I.exact(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-(o if isinstance(o,I) else I.exact(o)))
    def __rsub__(self,o): return I.exact(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I.exact(o)
        v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        assert not (self.lo<=0<=self.hi)
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I.exact(o)
        return self*o.inv()

@lru_cache(None)
def sqrt_i(n:int)->I:
    scale=1<<BITS
    q=isqrt(n*scale*scale)
    lo=F(q,scale)
    hi=lo if q*q==n*scale*scale else F(q+1,scale)
    return I(lo,hi)

@lru_cache(None)
def invsqrt_i(n:int)->I:
    return sqrt_i(n).inv()

def log_unit(num:int,den:int)->I:
    assert den<=num<=2*den
    if num==den:return I.exact(0)
    z=F(num-den,num+den)
    assert 0<=z<=F(1,3)
    s=F(0); p=z
    for r in range(TERMS):
        s+=p/F(2*r+1)
        p*=z*z
    lo=2*s
    tail=2*p/F(2*TERMS+1)/(1-z*z)
    return I(lo,lo+tail)

@lru_cache(None)
def log_i(num:int,den:int=1)->I:
    assert num>=den>0
    if num==den:return I.exact(0)
    k=0; d=den
    while num>=2*d:
        d*=2;k+=1
    return k*log_unit(2,1)+log_unit(num,d)

def mobius(n:int)->int:
    x=n;p=2;par=0
    while p*p<=x:
        if x%p==0:
            x//=p;par^=1
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    if x>1:par^=1
    return -1 if par else 1

def compact_hall():
    A=F(0);B=I.exact(0)
    best=None
    for t in range(1,67):
        m=mobius(t)
        A+=F(m,t)
        B+=m*invsqrt_i(t)
        x=t if A>=0 else 67
        H=4*sqrt_i(x)*A-3*B
        if best is None or H.lo<best[0]:
            best=(H.lo,H.hi,t,x)
    assert best is not None
    assert best[0]>F(7,20)
    return best

def cell_coeffs(j:int,N:int):
    A=F(j+1,j-1)
    B=F((j+1)*(j-2),j*(j-1))
    C=F(2,j*(j-1))
    a=A*invsqrt_i(j)
    b=A*invsqrt_i(j)*log_i(j)
    if N>=j+1:
        a-=B*invsqrt_i(j+1)
        b-=B*invsqrt_i(j+1)*log_i(j+1)
    for m in range(j+2,N+1):
        a+=C*invsqrt_i(m)
        b+=C*invsqrt_i(m)*log_i(m)
    return a,b

def compact_profile():
    best=None
    for j in range(2,67):
        for N in range(j,67):
            a,b=cell_coeffs(j,N)
            u=sqrt_i(N+1)
            Q=a*log_i(N+1)-b
            margin=a*(4*u-3)-2*u*Q
            if best is None or margin.lo<best[0]:
                best=(margin.lo,margin.hi,j,N)
            assert margin.lo>0
    assert best is not None
    assert best[0]>F(1,10)
    return best

@lru_cache(None)
def build():
    hall=compact_hall()
    prof=compact_profile()
    z=F(2,3)
    lead=-z*(z+1)/(1-z)
    assert lead==F(-10,3)
    # One exact geometric fixture for the typed alpha-only resolvent.
    root_mass=F(16); kappa=F(1,8)
    assert root_mass/(1-kappa)==F(128,7)
    core={
      "schema":"riemann.x99280.triad-hardening.v1",
      "verdict":VERDICT,
      "compact_hall_witness_t":hall[2],
      "compact_hall_lower_gt":"7/20",
      "profile_witness_j":prof[2],
      "profile_witness_cell":prof[3],
      "profile_derivative_margin_gt":"1/10",
      "all_compact_profile_cells_checked":sum(67-j for j in range(2,67)),
      "subpower_resolvent_mass_fixture":"128/7",
      "noncancellation_leading_fixture":"-10/3",
      "local_common_source_ledger_reconstructed":False,
      "rh_established":False,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    return core

def main():
    out=build()
    p=Path(__file__).resolve().parent/"results"/"verification.json"
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["verdict"]);print(out["proof_object_sha256"])

if __name__=="__main__":main()
