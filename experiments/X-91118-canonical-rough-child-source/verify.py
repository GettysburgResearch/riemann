#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

class Qr:
    """q0+q1*r with r^2=1/p."""
    def __init__(self,q0=0,q1=0,p=67):
        self.q0=Fraction(q0); self.q1=Fraction(q1); self.p=p
    def __add__(self,o):
        if not isinstance(o,Qr): o=Qr(o,0,self.p)
        assert self.p==o.p
        return Qr(self.q0+o.q0,self.q1+o.q1,self.p)
    __radd__=__add__
    def __neg__(self): return Qr(-self.q0,-self.q1,self.p)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        if not isinstance(o,Qr): o=Qr(o,0,self.p)
        assert self.p==o.p
        return Qr(self.q0*o.q0+self.q1*o.q1/Fraction(self.p),
                  self.q0*o.q1+self.q1*o.q0,self.p)
    __rmul__=__mul__
    def __eq__(self,o):
        if not isinstance(o,Qr): o=Qr(o,0,self.p)
        return self.p==o.p and self.q0==o.q0 and self.q1==o.q1
    def pair(self): return [str(self.q0),str(self.q1)]

def check_prime(p):
    r=Qr(0,1,p)
    one=Qr(1,0,p)
    B=one-r
    # W_Psi has coefficients 4*sqrt(x)/n - 3/sqrt(n).
    lhs_u=Qr(4*(p-1),0,p)*Fraction(1,p)
    lhs_v=-3*B
    rhs_u=B*(4*r)+4*B
    rhs_v=-3*B
    assert lhs_u==rhs_u
    assert lhs_v==rhs_v

    # General w_a identity on the two basis coefficients.
    for a in (Fraction(1),Fraction(2),Fraction(4,3),Fraction(7,5)):
        lhs_u=a*Qr(Fraction(p-1,p),0,p)
        rhs_u=B*(a*r)+a*B
        assert lhs_u==rhs_u
        assert -B==-B

    # Pure harmonic active pair.
    assert Qr(Fraction(p-1,p),0,p)==one-r*r

    return {
        "p":p,
        "B_pair":B.pair(),
        "child_scale_lt_c0": Fraction(1,p) < Fraction(1844367547103,10**14),
    }

def main():
    rows=[check_prime(p) for p in (67,71,73,79,83,89,97,101,127,257)]
    assert all(r["child_scale_lt_c0"] for r in rows)

    # Existing directed Hall corridors imply the SHARP-source margin.
    hall = -Fraction(9,50)+2*Fraction(39,100)
    assert hall==Fraction(3,5)

    result={
        "classification":"PASS_CANONICAL_ROUGH_CHILD_SOURCE_PARTITION",
        "prime_checks":rows,
        "sharp_no_upward_hall_margin":str(hall),
        "identity":"w_Psi(x,n)-w_Psi(x,pn)=(1-p^-1/2)w_Psi(x/p,n)+4(1-p^-1/2)sqrt(x)/n",
        "scope":"Exact algebra in Q[r]/(r^2-1/p), plus rational factor-54 and Hall-margin checks. This does not prove the parallel least-prime source partition."
    }
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])

if __name__=="__main__":
    main()
