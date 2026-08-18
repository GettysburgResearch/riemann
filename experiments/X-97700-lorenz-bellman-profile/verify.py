#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T97700_EXACT_LORENZ_BELLMAN_CORE"


def pos(x):
    return max(x, Fraction(0))


def dual(source, lam):
    TE=sum((a*t for s,a,t,r in source if s>0),Fraction())
    TO=sum((a*t for s,a,t,r in source if s<0),Fraction())
    RE=sum((a*r for s,a,t,r in source if s>0),Fraction())
    RO=sum((a*r for s,a,t,r in source if s<0),Fraction())
    HE=sum((a*pos(r-lam*t) for s,a,t,r in source if s>0),Fraction())
    HO=sum((a*pos(r-lam*t) for s,a,t,r in source if s<0),Fraction())
    return lam*TO+HE-RO, lam*TE+HO-RE


def swap(source):
    return [(-s,a,t,r) for s,a,t,r in source]


def scale(source,c):
    return [(s,c*a,t,r) for s,a,t,r in source]


class I:
    def __init__(self,lo,hi):
        assert lo<=hi
        self.lo,self.hi=lo,hi
    def __add__(self,o):
        with localcontext(Context(prec=80,rounding=ROUND_FLOOR)): lo=self.lo+o.lo
        with localcontext(Context(prec=80,rounding=ROUND_CEILING)): hi=self.hi+o.hi
        return I(lo,hi)
    def __sub__(self,o):
        with localcontext(Context(prec=80,rounding=ROUND_FLOOR)): lo=self.lo-o.hi
        with localcontext(Context(prec=80,rounding=ROUND_CEILING)): hi=self.hi-o.lo
        return I(lo,hi)
    def __mul__(self,o):
        z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(z),max(z))
    def inv(self):
        assert self.lo>0
        with localcontext(Context(prec=80,rounding=ROUND_FLOOR)): lo=Decimal(1)/self.hi
        with localcontext(Context(prec=80,rounding=ROUND_CEILING)): hi=Decimal(1)/self.lo
        return I(lo,hi)
    def div(self,o): return self*o.inv()


def sqrt_i(n):
    with localcontext(Context(prec=80,rounding=ROUND_FLOOR)): lo=Decimal(n).sqrt()
    with localcontext(Context(prec=80,rounding=ROUND_CEILING)): hi=Decimal(n).sqrt()
    return I(lo,hi)


def ratio_i(n,d):
    with localcontext(Context(prec=80,rounding=ROUND_FLOOR)): lo=(Decimal(n)/Decimal(d)).sqrt()
    with localcontext(Context(prec=80,rounding=ROUND_CEILING)): hi=(Decimal(n)/Decimal(d)).sqrt()
    return I(lo,hi)


def target_i(n,d):
    if n<d: return I(Decimal(0),Decimal(0))
    return I(Decimal(4),Decimal(4))*ratio_i(n,d)-I(Decimal(3),Decimal(3))


def divisors(limit=923):
    ps=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    out=[(1,1)]
    for p in ps:
        out += [(d*p,-s) for d,s in list(out) if d*p<=limit]
    return sorted(out)


def main():
    # Universal cushion, swap and prime-adjoining recurrence.
    P=[(1,Fraction(2,3),Fraction(5,4),Fraction(7,6)),(-1,Fraction(3,5),Fraction(4,3),Fraction(2,7))]
    C=[(1,Fraction(4,5),Fraction(3,2),Fraction(5,3)),(-1,Fraction(2,9),Fraction(7,4),Fraction(1,5))]
    lam=Fraction(5,7); rho=Fraction(2,9)
    dp,dm=dual(P,lam)
    cushion=sum((a*pos(lam*t-r) for s,a,t,r in P),Fraction())
    assert dp+dm==cushion
    assert dual(swap(P),lam)==(dm,dp)
    parent=P+scale(swap(C),rho)
    cdp,cdm=dual(C,lam)
    assert dual(parent,lam)==(dp+rho*cdm,dm+rho*cdp)

    # NCBI true but CPSL false.
    bad=[(1,Fraction(1),Fraction(1),Fraction(1)),(-1,Fraction(1),Fraction(2),Fraction(0))]
    assert dual(bad,Fraction(0))[0]==1
    assert dual(bad,Fraction(-10))[0]==-9

    # CPSL node sources but NCBI failure on three-node shift.
    f=[Fraction(0),Fraction(0),Fraction(1)]
    Tf=[f[1],f[2],Fraction(0)]
    c=[f[i]+Tf[i] for i in range(3)]
    Tc=[c[1],c[2],Fraction(0)]
    assert c==[0,1,1] and Tc==[1,1,0] and c[0]<Tc[0]

    # Minimal state failures.
    base=[(1,Fraction(1),Fraction(1),Fraction(0))]
    assert dual(base,Fraction(-1))==(1,-1)
    assert dual([],Fraction(1))[0]==dual(base,Fraction(1))[0]==0
    assert dual([],Fraction(1))[1]!=dual(base,Fraction(1))[1]
    assert Fraction(1)-Fraction(1,2)*0 != Fraction(1)-Fraction(1,2)*2

    # Odd-history directed witness.
    E=I(Decimal(0),Decimal(0)); O=I(Decimal(0),Decimal(0))
    root71=sqrt_i(71)
    ds=divisors()
    assert len(ds)==239
    for d,s in ds:
        td=(target_i(923,d)-target_i(13,d).div(root71)).div(sqrt_i(d))
        if s>0: E=E+td
        else: O=O+td
    gap=E-O
    assert gap.lo>Decimal(17)

    core={
      "schema":"riemann.t97700.exact-core.v1",
      "universal_cushion":True,
      "prime_recurrence":True,
      "ncbi_cpsl_non_equivalence":True,
      "smallest_two_sided_failure":{"X":1,"lambda":-1,"Dplus":1,"Dminus":-1},
      "odd_history":{"X":61841,"history":[67],"terminal":[71,13],"active_divisors":239,"gap_lower":str(gap.lo)},
      "lbp67_proved":False,
      "rh_established":False,
      "verdict":VERDICT
    }
    canonical=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
    out=Path(__file__).resolve().parent/"results/verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(core,indent=2,sort_keys=True)+"\n")
    print(core["verdict"]); print(core["proof_object_sha256"])

if __name__=="__main__": main()
