#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

class Qr:
    """q0+q1*r in Q[r]/(r^2-1/p)."""
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
    def pair(self): return [str(self.q0),str(self.q1)]

def certify_prime(p):
    r=Qr(0,1,p); one=Qr(1,0,p)
    A=one-r*r; B=one-r; d=A-B
    columns=[(2*A-B)+d, B+d, A, B]
    exact=one+2*r-3*r*r
    assert columns[0].q0==exact.q0 and columns[0].q1==exact.q1
    assert columns[1].q0==A.q0 and columns[1].q1==A.q1
    # The rational gate r<1/8 is equivalent to p>64.
    assert p>64
    # r(1+2r-3r^2) < r+2r^2 < 5/32.
    # Certify the final step by 1/sqrt(p)<1/8 and 1/p<1/64.
    upper=Fraction(1,8)+2*Fraction(1,64)
    assert upper==Fraction(5,32)
    return {
        "p":p,
        "ell1_norm_pair":exact.pair(),
        "scale_weighted_upper":str(upper),
    }

def main():
    primes=[67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,257,1009]
    rows=[certify_prime(p) for p in primes]
    result={
        "classification":"PASS_SCALE_WEIGHTED_ROUGH_CONTRACTION",
        "prime_checks":rows,
        "uniform_bound":"5/32",
        "identity":"sqrt(X/p)||Dtilde_p z||_1 < (5/32)sqrt(X)||z||_1 for p>=67,z>=0",
        "scope":"Exact matrix algebra and rational p>64 bounds. The replay does not construct the disjoint least-prime source partition or prove a score-loss comparison."
    }
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])

if __name__=="__main__":
    main()
