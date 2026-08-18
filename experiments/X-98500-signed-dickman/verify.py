#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

PRIMES_61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def dickman(max_u=6.0, h=2e-4):
    n=int(max_u/h)+1
    rho=[1.0]*n
    one=int(round(1/h))
    for i in range(one+1,n):
        u=i*h
        f0=-rho[i-1-one]/((i-1)*h)
        f1=-rho[i-one]/u
        rho[i]=rho[i-1]+0.5*h*(f0+f1)
    return h,rho

def at(u,h,rho):
    return rho[min(int(round(u/h)),len(rho)-1)]

def kappa_ratio(B):
    s=sum(math.log(p)/(p-1) for p in PRIMES_61 if p<=B)
    return s+0.5772156649015328606+math.log(4)-35/8

def continuum_transfer(u,L,a,c,h,rho):
    # beta(w)=a+c exp(-w/2), so eta=c exp(-w/2).
    # Numerically replay the exact signed-boundary formula.
    N=200000
    W=min(L*u,40.0)
    dw=W/N
    integ=0.0
    for j in range(N):
        w=(j+0.5)*dw
        v=u-w/L
        if v<=1:
            deriv=0.0
        else:
            deriv=-at(v-1,h,rho)/v
        integ += c*math.exp(-w/2)*deriv*dw/L
    return a*at(u,h,rho)+c*math.exp(-L*u/2)+integ

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    args=ap.parse_args()

    h,rho=dickman()
    vals={str(u):at(u,h,rho) for u in (1,2,3,4,5,6)}
    assert all(v>0 for v in vals.values())
    assert abs(vals["2"]-(1-math.log(2)))<8e-4

    kr11=kappa_ratio(11)
    kr13=kappa_ratio(13)
    kr61=kappa_ratio(61)
    assert kr11<0<kr13<kr61
    assert -0.21<kr11<-0.19
    assert 0.0<kr13<0.03
    assert 1.2<kr61<1.5

    # Signed boundary is relative to rho, unlike the unsigned 1/L payment.
    u=4.0; L=100.0; a=1.0; c=0.3
    transfer=continuum_transfer(u,L,a,c,h,rho)
    mainterm=a*at(u,h,rho)
    rel=(transfer-mainterm)/mainterm
    assert abs(rel)<0.05

    # Exponent algebra behind L ~ T^(5/8)(log T)^(3/4).
    # LHS u log u and VK exponent have the same T^(3/8)(log T)^(1/4) scale.
    T=10.0**12
    C0=100.0
    L=C0*T**(5/8)*math.log(T)**(3/4)
    uT=T/L
    lhs=uT*math.log(2*uT+2)
    rhs=L**(3/5)*math.log(L)**(-1/5)
    assert rhs/lhs>10

    result={
      "classification":"PASS_T98500_SIGNED_DICKMAN_VK_TRANSFER",
      "dickman_values":vals,
      "kappa_over_a":{
        "B11":kr11,
        "B13":kr13,
        "B61":kr61
      },
      "signed_boundary_fixture":{
        "u":u,"L":L,"main":mainterm,"transfer":transfer,
        "relative_correction":rel
      },
      "five_eighths_exponent_fixture":{
        "T":T,"C0":C0,"u":uT,"lhs":lhs,"vk_scale":rhs,
        "ratio":rhs/lhs
      },
      "vk_pnt_proved_by_replay":False,
      "multidimensional_stieltjes_theorem_proved_by_replay":False,
      "critical_core_proved":False,
      "RH_established":False
    }
    canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
    out=Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__=="__main__":
    main()
