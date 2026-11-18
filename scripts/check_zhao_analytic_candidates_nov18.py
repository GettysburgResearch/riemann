"""Necessary conductor test for 2 xi'_K(1)/xi_K(1) <= 2, unconditionally."""
import argparse
from functools import cache
import json
from math import isqrt
from pathlib import Path
from flint import arb, arb_series, ctx, fmpz_poly, nmod_poly
from check_zhao_field_weight_nov18 import primes_through

SCALES=(145,160,180,210)
UNIT=10**8


@cache
def base_upper(n,r2):
    bounds=[]
    for ss in SCALES:
        s=arb(ss)/100
        z=arb_series([s,1],prec=2).zeta()
        b=(4*(s-arb(1)/2)-2/s-2/(s-1)+n*arb.pi().log()
           -(n-r2)*(s/2).digamma()-r2*((s+1)/2).digamma()-2*n*z[1]/z[0])
        bounds.append(int((b*UNIT).upper().ceil().unique_fmpz()))
    return bounds


@cache
def gain(p,n,fs):
    g=[]
    for ss in SCALES:
        s=arb(ss)/100
        logp=arb(p).log()
        v=n/((s*logp).exp()-1)
        v-=sum(f/((f*s*logp).exp()-1) for f in fs)
        g.append(int((2*logp*v*UNIT).lower().floor().unique_fmpz()))
    return g


def select(rows,limit):
    primes=primes_through(limit)
    keep=[]
    for item in rows:
        n,r1,d,_=map(int,item["label"].split("/")[-1].split('.'))
        dlow=int((arb(d).log()*UNIT).lower().floor().unique_fmpz())
        a=[x-dlow for x in base_upper(n,(n-r1)//2)]
        coeff=item["coeffs"]
        disc=int(fmpz_poly(coeff).discriminant())
        index=isqrt(abs(disc)//d)
        if abs(disc)!=index**2*d:
            raise ArithmeticError("Bad order index")
        for p in primes:
            if index%p==0:
                continue
            fs=tuple(sorted(f.degree() for f,_ in nmod_poly(coeff,p).factor()[1]))
            for i,v in enumerate(gain(p,n,fs)):
                a[i]-=v
            if min(a)<0:
                break
        else:
            keep.append(item)
    return keep


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    ap.add_argument("output",type=Path)
    ap.add_argument("--limit",type=int,default=127)
    opt=ap.parse_args()
    ctx.prec=96
    rows=json.loads(opt.input.read_text())
    left=select(rows,opt.limit)
    opt.output.write_text(json.dumps(left,separators=(',',':')))
    print(len(rows),len(left))
