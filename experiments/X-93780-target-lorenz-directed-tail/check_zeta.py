#!/usr/bin/env python3
"""Directed decimal enclosure of zeta(1/2) and zeta'(1/2).

Uses the Hurwitz Euler--Maclaurin formula through B2 at integer a, with the
periodic Bernoulli bound |B2({t})| <= 1/6. Decimal sqrt/ln primitives are
computed at 100 digits and widened by EPS after every interval operation.
"""
from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
import argparse, hashlib, json
from pathlib import Path

PREC=100
EPS=Decimal('1e-82')

class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(lo)
        self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(hi))
        assert self.lo<=self.hi
    def __add__(self,o):
        o=asiv(o); return IV(self.lo+o.lo-EPS,self.hi+o.hi+EPS)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __rsub__(self,o): return asiv(o)-self
    def __mul__(self,o):
        o=asiv(o); v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(v)-EPS,max(v)+EPS)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asiv(o); assert not(o.lo<=0<=o.hi)
        v=(self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi)
        return IV(min(v)-EPS,max(v)+EPS)
    def __rtruediv__(self,o): return asiv(o)/self

def asiv(x): return x if isinstance(x,IV) else IV(x)

def primitive_sqrt(n:int)->IV:
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_HALF_EVEN
        v=Decimal(n).sqrt()
    return IV(v-EPS,v+EPS)

def primitive_ln(n:int)->IV:
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_HALF_EVEN
        v=Decimal(n).ln()
    return IV(v-EPS,v+EPS)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,default=20000);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();a=args.a; assert a>=2
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_HALF_EVEN
        z=IV(0); zp=IV(0)
        for n in range(1,a):
            sq=primitive_sqrt(n); inv=IV(1)/sq; ln=primitive_ln(n)
            z += inv
            zp -= ln*inv
        sqa=primitive_sqrt(a); lna=primitive_ln(a); ainv=IV(1)/sqa; a32=IV(a)*sqa
        # Hurwitz EM through B2, at s=1/2.
        z += -IV(2)*sqa + IV(1)/(IV(2)*sqa) + IV(1)/(IV(24)*a32)
        zp += sqa*(IV(2)*lna-IV(4)) - lna/(IV(2)*sqa) + (IV(1)-lna/IV(2))/(IV(12)*a32)
        # Exact B2-periodic remainder bounds.
        rem = IV(1)/(IV(24)*a32)
        remp = (IV(5)/IV(36)+lna/IV(24))/a32
        z=IV(z.lo-rem.hi,z.hi+rem.hi)
        zp=IV(zp.lo-remp.hi,zp.hi+remp.hi)
        claimed_z=IV('-1.460355','-1.460354')
        claimed_zp=IV('-3.922647','-3.922646')
        assert claimed_z.lo <= z.lo and z.hi <= claimed_z.hi,(z.lo,z.hi)
        assert claimed_zp.lo <= zp.lo and zp.hi <= claimed_zp.hi,(zp.lo,zp.hi)
        payload={
            'classification':'PASS_DIRECTED_ZETA_HALF_PRIMITIVES',
            'arithmetic_class':'DECIMAL_100_DIGIT_OUTWARD_INTERVAL_PLUS_EXACT_B2_REMAINDER',
            'a':a,
            'zeta_half_interval':[str(z.lo),str(z.hi)],
            'zeta_prime_half_interval':[str(zp.lo),str(zp.hi)],
            'published_zeta_interval':[str(claimed_z.lo),str(claimed_z.hi)],
            'published_zeta_prime_interval':[str(claimed_zp.lo),str(claimed_zp.hi)],
            'zeta_remainder_radius':str(rem.hi),
            'zeta_prime_remainder_radius':str(remp.hi),
            'primitive_padding':str(EPS),
            'primitive_count':2*(a-1)+2,
            'rh_established_by_replay':False,
        }
        raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
        print(payload['classification']);print(payload['proof_object_sha256'])
if __name__=='__main__':main()
