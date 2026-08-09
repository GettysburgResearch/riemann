#!/usr/bin/env python3
"""Exact/directed replay for L-32307 outer-fifteen-sixteenths SHARP theorem."""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
import hashlib, json
from pathlib import Path

DIGITS = 40
SCALE = 10 ** DIGITS
T_MAX = 255


def mobius_sieve(n):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]:
            primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0:
                mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu


def invsqrt_scaled(n):
    a=isqrt((SCALE*SCALE)//n)
    while (a+1)*(a+1)*n <= SCALE*SCALE: a+=1
    while a*a*n > SCALE*SCALE: a-=1
    return a,a+1


def sqrt_scaled(n):
    a=isqrt(n*SCALE*SCALE)
    while (a+1)*(a+1) <= n*SCALE*SCALE: a+=1
    while a*a > n*SCALE*SCALE: a-=1
    return a,a+1


def fixed_cell_gates():
    mu=mobius_sieve(15)
    alo=[0]*16; ahi=[0]*16; M=[0]*16
    lo=hi=0; m=0
    for k in range(1,16):
        il,ih=invsqrt_scaled(k)
        if mu[k]>0:
            lo+=il; hi+=ih
        elif mu[k]<0:
            lo-=ih; hi-=il
        m+=mu[k]
        alo[k]=lo; ahi[k]=hi; M[k]=m

    positive={2:Fraction(2,5),3:Fraction(2,5),4:Fraction(1,3),
              5:Fraction(1,5),6:Fraction(1,8)}
    pos={}
    for K,c in positive.items():
        if ahi[K] < 0:
            sl,sh=sqrt_scaled(K+1); lower=alo[K]*sh-M[K]*SCALE*SCALE
        else:
            sl,sh=sqrt_scaled(K); lower=alo[K]*sl-M[K]*SCALE*SCALE
        pos[str(K)] = lower*c.denominator > c.numerator*SCALE*SCALE

    uinner={}
    for K in range(8,16):
        sl,sh=sqrt_scaled(K+1)
        lower=alo[K]*sh-M[K]*SCALE*SCALE
        uinner[str(K)] = 5*lower > -4*SCALE*SCALE

    local_bounds={8:Fraction(-13,10),9:Fraction(-8,5),10:Fraction(-6,5),
                  11:Fraction(-2,1),12:Fraction(-9,4),13:Fraction(-31,10),
                  14:Fraction(-14,5),15:Fraction(-12,5)}
    local={}
    for K,c in local_bounds.items():
        sl,sh=sqrt_scaled(K+1)
        # 2*SCALE^2 times the certified local lower bound.
        lhs=5*alo[K]*sh-4*M[K]*SCALE*SCALE
        local[str(K)] = lhs*c.denominator > 2*c.numerator*SCALE*SCALE

    assert all(pos.values()) and all(uinner.values()) and all(local.values())
    return pos,uinner,local


def finite_endpoint(T):
    mu=mobius_sieve(T)
    lo=[0]*(T+1); hi=[0]*(T+1)
    for n in range(1,T+1):
        lo[n],hi[n]=invsqrt_scaled(n)
    hlo=[0]*(T+1); hhi=[0]*(T+1)
    for n in range(1,T+1):
        hlo[n]=lo[n]-hi[T]
        hhi[n]=hi[n]-lo[T]

    ulo=[0]*(T+2); uhi=[0]*(T+2)
    for k in range(1,T+1):
        muk=mu[k]
        if not muk: continue
        for m in range(1,T//k+1):
            n=m*k
            if muk>0:
                ulo[m]+=hlo[n]; uhi[m]+=hhi[n]
            else:
                ulo[m]-=hhi[n]; uhi[m]-=hlo[n]

    tail=[0]*(T+3)
    for m in range(T,0,-1):
        tail[m]=tail[m+1]+ulo[m]

    checked=0
    min_item=None
    for j in range(2,T):
        if 16*j <= T: continue
        a_lo=j*ulo[j]-(j-2)*uhi[j+1]
        num_lo=(j+1)*a_lo+2*tail[j+2]
        assert num_lo>0,(T,j,num_lo)
        checked+=1
        den=j*(j-1)
        if min_item is None or num_lo*min_item[3] < min_item[2]*den:
            min_item=(T,j,num_lo,den)
    return checked,min_item


def main():
    pos,uinner,local=fixed_cell_gates()
    total=0; globalmin=None
    for T in range(3,T_MAX+1):
        checked,mi=finite_endpoint(T)
        total+=checked
        if mi and (globalmin is None or mi[2]*globalmin[3] < globalmin[2]*mi[3]):
            globalmin=mi

    tail_gate=Fraction(1271,8400)-Fraction(271,60*256)>Fraction(13,100)
    same_margins={
        8:Fraction(39,50), 9:Fraction(37,50), 10:Fraction(7,5),
        11:Fraction(43,50), 12:Fraction(87,100), 13:Fraction(7,25),
        14:Fraction(21,25), 15:Fraction(3,2),
    }
    adverse={10:same_margins[10]-Fraction(1,2),
             14:same_margins[14]-Fraction(1,2),
             15:same_margins[15]-Fraction(1,2)}
    assert tail_gate and all(x>0 for x in same_margins.values()) and all(x>0 for x in adverse.values())

    data={
        "schema":"X-32303-outer-fifteen-sixteenths-v1",
        "classification":"DIRECTED_OUTER_FIFTEEN_SIXTEENTHS_SHARP_VERIFIED",
        "finite_endpoint_max":T_MAX,
        "finite_coefficient_rows_checked":total,
        "fixed_positive_cell_gates":pos,
        "fixed_inner_state_lower_gates":uinner,
        "fixed_inner_local_lower_gates":local,
        "tail_reserve_at_T256_gt_13_over_100":tail_gate,
        "same_cell_margin_lower_bounds":{str(k):f"{v.numerator}/{v.denominator}" for k,v in same_margins.items()},
        "adverse_transition_margins":{str(k):f"{v.numerator}/{v.denominator}" for k,v in adverse.items()},
        "minimum_finite_certificate":{
            "T":globalmin[0],"j":globalmin[1],
            "lower_numerator_scaled":str(globalmin[2]),
            "denominator":globalmin[3],
            "digits":DIGITS,
        },
        "proof_boundary":"finite base through T=255 plus fixed radical gates only; T>=256 is analytic in L-32307; RH is not certified",
    }
    raw=json.dumps(data,indent=2,sort_keys=True)+"\n"
    data["sha256_without_digest"]=hashlib.sha256(raw.encode()).hexdigest()
    out=json.dumps(data,indent=2,sort_keys=True)+"\n"
    result=Path(__file__).with_name("results")/"verification.json"
    result.parent.mkdir(parents=True,exist_ok=True)
    result.write_text(out,encoding="utf-8")
    print(out,end="")


if __name__=="__main__":
    main()
