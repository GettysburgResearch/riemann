#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA="riemann.t99030.survival-resolvent-bellman.v1"

class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError
    @staticmethod
    def coerce(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o): o=self.coerce(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-self.coerce(o))
    def __rsub__(self,o): return self.coerce(o)-self
    def __mul__(self,o):
        o=self.coerce(o); v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        return I(min(1/self.lo,1/self.hi),max(1/self.lo,1/self.hi))
    def __truediv__(self,o): return self*self.coerce(o).reciprocal()
    def __rtruediv__(self,o): return self.coerce(o)/self

def decimal(q,digits=100):
    sign="-" if q<0 else ""; q=abs(q); whole,rem=divmod(q.numerator,q.denominator); out=[]
    for _ in range(digits):
        rem*=10; digit,rem=divmod(rem,q.denominator); out.append(str(digit))
    return f"{sign}{whole}."+''.join(out)

def interval_json(x): return {"lower":decimal(x.lo),"upper":decimal(x.hi)}

def sqrt_i(n,digits=90):
    scale=10**digits; q=math.isqrt(n*scale*scale); lo=Fraction(q,scale)
    return I(lo) if q*q==n*scale*scale else I(lo,Fraction(q+1,scale))

def invsqrt_i(n): return sqrt_i(n).reciprocal()

def log_unit_i(y,terms=160):
    y=Fraction(y)
    if not Fraction(1)<=y<=Fraction(2): raise ValueError
    z=(y-1)/(y+1); z2=z*z; power=z; partial=Fraction(0)
    for k in range(terms):
        partial+=power/(2*k+1); power*=z2
    lo=2*partial; tail=2*power/((2*terms+1)*(1-z2))
    return I(lo,lo+tail)

def mobius_upto(n):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=[False]*(n+1)
    for x in range(2,n+1):
        if not comp[x]: primes.append(x); mu[x]=-1
        for p in primes:
            if x*p>n: break
            comp[x*p]=True
            if x%p==0: mu[x*p]=0; break
            mu[x*p]=-mu[x]
    return mu

def root_mass_interval():
    mu=mobius_upto(66); a=Fraction(0); b=I(0); total=I(0)
    for N in range(1,67):
        a+=Fraction(mu[N],N); b+=mu[N]*invsqrt_i(N)
        ds=sqrt_i(N+1)-sqrt_i(N); lg=log_unit_i(Fraction(N+1,N))
        total+=16*a*a-40*a*b*ds+6*b*b*lg
    assert total.lo>15 and total.hi<16
    return total

def causal_coefficients(rs):
    s=Fraction(1); lambdas=[]; alphas=[]
    for r in rs:
        lam=r*s; lambdas.append(lam); alphas.append(r*lam); s*=1-r
    return s,lambdas,alphas

def fixture(rs,children,current):
    s,lams,alphas=causal_coefficients(rs); den=1-s
    pis=[x/den for x in lams]; assert sum(pis,Fraction(0))==1
    parent=(sum(l*c for l,c in zip(lams,current))+sum(a*d for a,d in zip(alphas,children)))/den
    rhs=sum(pi*r*d for pi,r,d in zip(pis,rs,children))
    correction=sum(pi*c for pi,c in zip(pis,current))
    assert parent==rhs+correction and correction<=0 and parent<=rhs
    assert max(parent,0)<=max(r*max(d,0) for r,d in zip(rs,children))
    return {"parent":str(parent),"discounted":str(rhs),"current":str(correction),"pis":[str(x) for x in pis]}

def verify():
    mass=root_mass_interval()
    fixtures=[
        fixture([Fraction(1,9),Fraction(1,10),Fraction(1,11)],[Fraction(2),Fraction(3,2),Fraction(-1,3)],[Fraction(-1,4),0,Fraction(-2,5)]),
        fixture([Fraction(3,25),Fraction(2,19)],[Fraction(7,5),Fraction(9,7)],[Fraction(-3,8),Fraction(-1,11)]),
        fixture([Fraction(1,12)],[Fraction(2)],[0]),
    ]
    assert 67>64  # 1/sqrt(67)<1/8
    debt=2*mass.hi; assert debt<32
    # Mutations
    rs=[Fraction(1,9),Fraction(1,10)]; s,lams,alphas=causal_coefficients(rs); den=1-s
    children=[Fraction(2),Fraction(3)]
    raw=sum(a*d for a,d in zip(alphas,children)); assert raw/den>raw
    positive_current=[Fraction(1,20),0]
    bad=(sum(l*c for l,c in zip(lams,positive_current))+raw)/den
    discounted=sum((l/den)*r*d for l,r,d in zip(lams,rs,children))
    assert bad>discounted
    core={
      "frozen_parent":{"pr":620,"head":"493e12fcba3f9b98dda7c3595bff73b256e00ca4"},
      "root_mass":{"interval":interval_json(mass),"strict_upper":16,"score_debt_upper":decimal(debt),"strict_debt_upper":32},
      "bellman_fixtures":fixtures,
      "mutations":{"survival_resolvent_required":True,"current_score_superordination_required":True,"hall_bonus_export_forbidden":True},
      "scientific_boundary":{"arbitrary_rough_prime_paths_supported":True,"fixed_67_level_telescope_required":False,"rh_established_by_replay":False},
    }
    digest=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {"schema":SCHEMA,"classification":"PASS_T99030_SURVIVAL_RESOLVENT_BELLMAN_HARDENING","proof_object_sha256":digest,"core":core}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path); args=ap.parse_args()
    result=verify(); text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(result["classification"]); print(result["proof_object_sha256"])
if __name__=="__main__": main()
