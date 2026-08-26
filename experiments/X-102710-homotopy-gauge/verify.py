#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path

def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def conv(a,b,N):
    out=[Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:
                out[i+j]+=x*y
    return out

def sqrt1minus(N):
    c=[Fraction(0) for _ in range(N+1)]
    c[0]=Fraction(1)
    c[1]=Fraction(-1,2)
    for k in range(2,N+1):
        c[k]=c[k-1]*Fraction(2*k-3,2*k)
    return c

def sqrt1plus(N):
    c=[Fraction(0) for _ in range(N+1)]
    c[0]=Fraction(1)
    for k in range(1,N+1):
        c[k]=c[k-1]*Fraction(3-2*k,2*k)
    return c

def poly_add(a,b):
    N=max(len(a),len(b))
    out=[Fraction(0) for _ in range(N)]
    for i in range(N):
        if i<len(a): out[i]+=a[i]
        if i<len(b): out[i]+=b[i]
    return out

def poly_scale(a,c):
    return [c*x for x in a]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    N=18
    sm=sqrt1minus(N)
    sp=sqrt1plus(N)

    endpoint_checks=0
    ratio_checks=0
    tangent_checks=0
    for tau in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
        sx2=[Fraction(0) for _ in range(N+1)]
        for k,c in enumerate(sm):
            if 2*k<=N: sx2[2*k]=c
        ell=poly_add(poly_scale(sm,tau),poly_scale(sx2,1-tau))
        h=conv(ell,ell,N)
        e=[Fraction(0) for _ in range(N+1)]
        e[0]=1
        e[1]=-tau
        e[2]=-(1-tau)
        assert h[0]==e[0] and h[1]==e[1]
        if tau in (0,1):
            assert h==e
            endpoint_checks+=1
        else:
            assert h[0]-e[0]==0 and h[1]-e[1]==0
            ratio_checks+=1

        tangent=poly_add(sm,poly_scale(sx2,-1))
        assert tangent[0]==0
        assert tangent[1]==Fraction(-1,2)
        tangent_checks+=1

    transfer_checks=0
    for tau in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
        numbase=poly_add([tau],poly_scale(sp,1-tau))
        num=conv(numbase,numbase,N)
        inv=[Fraction(0) for _ in range(N+1)]
        inv[0]=1
        for k in range(1,N+1):
            inv[k]=-(1-tau)*inv[k-1]
        g=conv(num,inv,N)
        assert g[0]==1 and g[1]==0
        e=[Fraction(0) for _ in range(N+1)]
        e[0]=1
        e[1]=-tau
        e[2]=-(1-tau)
        h_from_ratio=conv(e,g,N)
        sx2=[Fraction(0) for _ in range(N+1)]
        for k,c in enumerate(sm):
            if 2*k<=N: sx2[2*k]=c
        ell=poly_add(poly_scale(sm,tau),poly_scale(sx2,1-tau))
        h=conv(ell,ell,N)
        assert h_from_ratio==h
        transfer_checks+=1

    cA=2*math.log(2)*(1-2**-0.5)
    assert cA>0
    payload={
        "schema":"riemann.t102710.homotopy-gauge-exchange.v1",
        "series_order":N,
        "endpoint_checks":endpoint_checks,
        "ratio_checks":ratio_checks,
        "tangent_checks":tangent_checks,
        "transfer_checks":transfer_checks,
        "A_half_order_constant":cA,
        "gauge_transfer_has_no_linear_term":True,
        "separate_field_energy_subpower":False,
        "phdc102710_proved":False,
        "rh_established":False,
        "verdict":"PASS_T102710_HOMOTOPY_GAUGE_EXCHANGE",
    }
    payload["proof_object_sha256"]=digest(payload)
    text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])
if __name__=="__main__":
    main()
