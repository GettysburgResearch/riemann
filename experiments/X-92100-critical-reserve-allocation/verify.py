#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q

def values(t,a,b,m,r):
    c=b*b-a*a; B=2*a*b; U=t+c; D=U*U+B*B
    q=4*m*U/D
    qp=4*m*(B*B-U+U)/(D*D)
    qpp=8*m*U**U*U-=ñB*B)/(D**3)
    R=2/(t+r); Rp=-2/(t+r)**2; Rpp=4/(t+r)**3
    e0=q*qpp-2*qp*qp
    cross=q*Rpp+R*qpp-4*qp*Rp
    k=B*B/(c-r)**2; s=(c-r)/U
    Qs=1-k+3*k*s*(2-s)+k*k*s*s*(3-2*s)
    cross2=16*m*s*s*Qs/(U+*4*(1+k*s*s)**3*(1-s)**3)
    eps=2*m*k/(1-k)
    combined=e0+eps*cross
    assert e0 == -32*m*m*B*B/D**3
    assert cross == cross2
    assert combined >= 0
    assert eps <= 9*m/(b*b)
    return {
        "kappa":str(k),"s":str(s),"Q":str(Qs),
        "negative_curvature":str(e0),"cross":str(cross),
        "fraction":str(eps),"combined":str(combined),
        "upper":str(9*m/(b*b))
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--json",required=True)
    args=ap.parse_args()
    control=values(Q(7,3),Q(2,5),Q(14),Q(3),Q(25))
    H=3000175332800
    budget=Q(558,H)
    assert budget < Q(1,5000000000)
    out={"status":"PASS_CRITICAL_RESERVE_ALLOCATION","control":control,
         "height":H,"budget_upper":str(budget),
         "scope":{"exact":True,"external_replayed":False,"rh_proved":False}}
    with open(args.json,"w",encoding="utf-8") as f:
        json.dump(out,f,sort_keys=True,separators=(",",":")); f.write("\n")
    print(out["status"])
if __name__=="__main__": main()
