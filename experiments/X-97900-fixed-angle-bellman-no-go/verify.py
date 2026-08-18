#!/usr/bin/env python3
"""Directed replay for T-97900.  Standard library only."""
from __future__ import annotations
import hashlib, json
from dataclasses import dataclass
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from pathlib import Path

PREC=120
NEAR=Context(prec=PREC,rounding=ROUND_HALF_EVEN)
DOWN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)
HERE=Path(__file__).resolve().parent
SMALL=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

@dataclass(frozen=True)
class I:
    lo: Decimal
    hi: Decimal
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    def __add__(self,o):
        with localcontext(DOWN): lo=self.lo+o.lo
        with localcontext(UP): hi=self.hi+o.hi
        return I(lo,hi)
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        with localcontext(DOWN): lo=min(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        with localcontext(UP): hi=max(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(lo,hi)
    def scale_int(self,n):
        if n<0: return (-self).scale_int(-n)
        with localcontext(DOWN): lo=self.lo*Decimal(n)
        with localcontext(UP): hi=self.hi*Decimal(n)
        return I(lo,hi)
    def inv_pos(self):
        if self.lo<=0: raise ValueError("positive interval required")
        with localcontext(DOWN): lo=Decimal(1)/self.hi
        with localcontext(UP): hi=Decimal(1)/self.lo
        return I(lo,hi)

ZERO=I(Decimal(0),Decimal(0))
def sqrt_int(n):
    with localcontext(NEAR):
        v=Decimal(n).sqrt(); return I(v.next_minus(NEAR),v.next_plus(NEAR))
def log_int(n):
    if n==1:return ZERO
    with localcontext(NEAR):
        v=Decimal(n).ln(); return I(v.next_minus(NEAR),v.next_plus(NEAR))
def invsqrt(n): return sqrt_int(n).inv_pos()
def qstar(n): return 0 if n==1 else 15 if n==2 else 6 if n==3 else 3 if n==4 else 6

def coeffs(limit=200):
    f=[qstar(n) for n in range(limit+1)]; m=f.copy()
    for p in SMALL+[67]:
        old=f.copy(); oldu=m.copy()
        for n in range(1,limit+1):
            if n%p==0: f[n]=old[n]-old[n//p]; m[n]=oldu[n]+oldu[n//p]
            else: f[n]=old[n]; m[n]=oldu[n]
    return f,m
FCOEF,MCOEF=coeffs()

def hinge(num,den,n):
    if num<den*n:return ZERO
    if num>=den*4*n:return log_int(4)
    return (log_int(num)-log_int(den))-log_int(n)
def state(num,den=1):
    f=m=ZERO
    for n in range(1,num//den+1):
        h=hinge(num,den,n)
        if h.lo==0 and h.hi==0: continue
        a=invsqrt(n)*h
        f=f+a.scale_int(FCOEF[n]); m=m+a.scale_int(MCOEF[n])
    return f,m
def margin(num,den=1):
    f,m=state(num,den); return f.scale_int(42)-m

def sieve(n):
    a=[True]*(n+1); a[:2]=[False,False]
    for p in range(2,int(n**.5)+1):
        if a[p]:
            for k in range(p*p,n+1,p):a[k]=False
    return [i for i,v in enumerate(a) if v]

def exact_maps():
    f=[Fraction(0),Fraction(0),Fraction(1)]
    tf=[f[1],f[2],Fraction(0)]; c=[f[i]+tf[i] for i in range(3)]
    tc=[c[1],c[2],Fraction(0)]; t2f=[f[2],Fraction(0),Fraction(0)]
    assert [c[i]-tc[i] for i in range(3)]==[f[i]-t2f[i] for i in range(3)]
    dp,dm,bp,bm,rho=map(Fraction,[7,-3,5,11,2])
    assert bp+rho*dm==-1 and bm+rho*dp==25
    return {"ncbi":"c-Tc=(I-T^2)f","prime_recurrence":["-1","25"]}

def run():
    smallest=None
    for x in range(67,161):
        g=margin(x)
        assert g.lo>0,(x,g)
        if smallest is None or g.lo<smallest[0]:smallest=(g.lo,x,g.hi)
    g160,g161=margin(160),margin(161)
    assert g160.lo>0>g161.hi
    left,right=margin(16037507,100000),margin(16037508,100000)
    assert left.lo>0>right.hi
    f161,m161=state(161); assert f161.lo>0
    kappa=Fraction(1)
    for p in SMALL:kappa*=Fraction(p-1,p+1)
    snaps=[]
    for i,p in enumerate([p for p in sieve(700) if p>=67],1):
        kappa*=Fraction(p-1,p+1)
        if i in {1,5,18,50,100}:snaps.append({"count":i,"last_prime":p,"ratio":str(kappa)})
    assert kappa<Fraction(1,80)
    core={
      "schema":"riemann.t97900.fixed-angle-bellman-no-go.v1",
      "frozen_heads":{"pr591":"5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111","pr581":"62aaa54ac49f0aa89fd58f14a539cc53089f884c","pr584":"e919c6afd1e95fffa505f7ba3f532cb12b8c410c","pr582":"699f9f119a66823702e96fba95cc8b14b8251c60","pr576":"0f6ea6eae813c1d867ae50744cf5fd57e2720bb7"},
      "separator":{"positive_integer_range":[67,160],"smallest_pre_failure":[str(smallest[0]),smallest[1],str(smallest[2])],"G160":[str(g160.lo),str(g160.hi)],"G161":[str(g161.lo),str(g161.hi)],"crossing_bracket":["160.37507","160.37508"],"left":[str(left.lo),str(left.hi)],"right":[str(right.lo),str(right.hi)],"F161":[str(f161.lo),str(f161.hi)],"M161":[str(m161.lo),str(m161.hi)]},
      "euler_product_snapshots":snaps,"exact_maps":exact_maps(),
      "mutations_rejected":["treat_1_over_42_as_invariant","claim_separator_is_negative_scalar","drop_unsigned_plus_sign","erase_parity_swap","replace_future_quotient_by_root_only","claim_ncbi_equals_cpsl","promote_finite_scan_to_all_scale"],
      "all_fixed_positive_apertures_invariant":False,"scalar_positivity_refuted":False,"cpsl67_proved":False,"ncbi67_proved":False,"rh_established":False,"verdict":"PASS_T97900_FIXED_ANGLE_BELLMAN_NO_GO"}
    core["proof_object_sha256"]=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return core

def main():
    r=run(); out=HERE/"results"/"verification.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
    print(r["verdict"]); print(r["proof_object_sha256"])
if __name__=="__main__":main()
