#!/usr/bin/env python3
"""Exact/directed replay for L-32308 outer-thirty-one-thirty-seconds SHARP theorem."""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
import hashlib, json
from pathlib import Path

DIGITS=32
SCALE=10**DIGITS
T_MAX=2047


def mobius_sieve(n):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu


def invsqrt_scaled(n):
    a=isqrt((SCALE*SCALE)//n)
    while (a+1)*(a+1)*n<=SCALE*SCALE: a+=1
    while a*a*n>SCALE*SCALE: a-=1
    return a,a+1


def sqrt_scaled(n):
    a=isqrt(n*SCALE*SCALE)
    while (a+1)*(a+1)<=n*SCALE*SCALE: a+=1
    while a*a>n*SCALE*SCALE: a-=1
    return a,a+1


MU=mobius_sieve(T_MAX)
INV=[(0,0)]*(T_MAX+1)
for n in range(1,T_MAX+1): INV[n]=invsqrt_scaled(n)

CELL={
2:Fraction(41,100),3:Fraction(43,100),4:Fraction(36,100),5:Fraction(20,100),
6:Fraction(14,100),7:Fraction(1,100),8:Fraction(-11,100),9:Fraction(-22,100),
10:Fraction(-28,100),11:Fraction(-38,100),12:Fraction(-48,100),13:Fraction(-61,100),
14:Fraction(-70,100),15:Fraction(-76,100),16:Fraction(-81,100),17:Fraction(-89,100),
18:Fraction(-97,100),19:Fraction(-108,100),20:Fraction(-118,100),21:Fraction(-125,100),
22:Fraction(-130,100),23:Fraction(-137,100),24:Fraction(-144,100),25:Fraction(-151,100),
26:Fraction(-156,100),27:Fraction(-161,100),28:Fraction(-165,100),29:Fraction(-171,100),
30:Fraction(-179,100),31:Fraction(-188,100),
}
LOCAL={
16:Fraction(-26,10),17:Fraction(-33,10),18:Fraction(-35,10),19:Fraction(-42,10),
20:Fraction(-45,10),21:Fraction(-42,10),22:Fraction(-38,10),23:Fraction(-45,10),
24:Fraction(-46,10),25:Fraction(-48,10),26:Fraction(-44,10),27:Fraction(-46,10),
28:Fraction(-47,10),29:Fraction(-53,10),30:Fraction(-60,10),31:Fraction(-67,10),
}


def fixed_gates():
    mu=mobius_sieve(31)
    alo=[0]*32; ahi=[0]*32; M=[0]*32
    lo=hi=m=0
    lower={}; negative={}; local={}
    for k in range(1,32):
        il,ih=invsqrt_scaled(k)
        if mu[k]>0: lo+=il; hi+=ih
        elif mu[k]<0: lo-=ih; hi-=il
        m+=mu[k]; alo[k]=lo; ahi[k]=hi; M[k]=m
    for K in range(2,32):
        if ahi[K]<0:
            _,sh=sqrt_scaled(K+1); v=alo[K]*sh-M[K]*SCALE*SCALE
        else:
            sl,_=sqrt_scaled(K); v=alo[K]*sl-M[K]*SCALE*SCALE
        c=CELL[K]
        lower[str(K)]=v*c.denominator>c.numerator*SCALE*SCALE
    for K in range(16,32):
        assert ahi[K]<0
        sl,_=sqrt_scaled(K)
        negative[str(K)]=ahi[K]*sl-M[K]*SCALE*SCALE<0
        _,sh=sqrt_scaled(K+1)
        # twice the local lower bound: 5 A_K sqrt(K+1)-4 M_K.
        v=5*alo[K]*sh-4*M[K]*SCALE*SCALE
        c=LOCAL[K]
        local[str(K)]=v*c.denominator>2*c.numerator*SCALE*SCALE
    assert all(lower.values()) and all(negative.values()) and all(local.values())
    return lower,negative,local


def finite_endpoint(T):
    tlo,thi=INV[T]
    hlo=[0]*(T+1); hhi=[0]*(T+1)
    for n in range(1,T+1):
        il,ih=INV[n]; hlo[n]=il-thi; hhi[n]=ih-tlo
    ulo=[0]*(T+2); uhi=[0]*(T+2)
    for m in range(1,T+1):
        sl=sh=0
        for k in range(1,T//m+1):
            muk=MU[k]
            if muk>0: sl+=hlo[m*k]; sh+=hhi[m*k]
            elif muk<0: sl-=hhi[m*k]; sh-=hlo[m*k]
        ulo[m]=sl; uhi[m]=sh
    tail=[0]*(T+3)
    for m in range(T,0,-1): tail[m]=tail[m+1]+ulo[m]
    checked=0; minimum=None
    for j in range(2,T):
        if 32*j<=T: continue
        local_lo=j*ulo[j]-(j-2)*uhi[j+1]
        num_lo=(j+1)*local_lo+2*tail[j+2]
        assert num_lo>0,(T,j,num_lo)
        checked+=1; den=j*(j-1)
        if minimum is None or num_lo*minimum[3]<minimum[2]*den:
            minimum=(T,j,num_lo,den)
    return checked,minimum


def main():
    lower,negative,local=fixed_gates()
    C=Fraction(3,40)+sum(CELL[K]*Fraction(1,K*(K+1)) for K in range(2,32))
    err=sum(abs(CELL[K]) for K in range(2,32))
    tail2048=C-err/Fraction(2048)
    assert C>Fraction(29,200) and tail2048>Fraction(1,8)
    same={K:LOCAL[K]+Fraction(K,4) for K in range(16,32)}
    adverse={K:same[K]-Fraction(1,2) for K in (21,22,26)}
    assert all(v>0 for v in same.values()) and all(v>0 for v in adverse.values())

    total=0; globalmin=None
    for T in range(3,T_MAX+1):
        checked,mi=finite_endpoint(T); total+=checked
        if mi and (globalmin is None or mi[2]*globalmin[3]<globalmin[2]*mi[3]): globalmin=mi

    data={
      "schema":"X-32304-outer-thirty-one-thirty-seconds-v1",
      "classification":"DIRECTED_OUTER_THIRTY_ONE_THIRTY_SECONDS_SHARP_VERIFIED",
      "digits":DIGITS,
      "finite_endpoint_max":T_MAX,
      "finite_coefficient_rows_checked":total,
      "tail_asymptotic_constant":f"{C.numerator}/{C.denominator}",
      "tail_floor_error_constant":f"{err.numerator}/{err.denominator}",
      "tail_at_T2048_gt_one_eighth":tail2048>Fraction(1,8),
      "cell_state_lower_gates":lower,
      "new_cells_strictly_negative_gates":negative,
      "new_local_lower_gates":local,
      "same_cell_margins":{str(k):f"{v.numerator}/{v.denominator}" for k,v in same.items()},
      "adverse_transition_margins":{str(k):f"{v.numerator}/{v.denominator}" for k,v in adverse.items()},
      "minimum_finite_certificate":{"T":globalmin[0],"j":globalmin[1],"lower_numerator_scaled":str(globalmin[2]),"denominator":globalmin[3]},
      "proof_boundary":"finite base through T=2047 plus fixed radical gates through quotient 31; T>=2048 analytic; RH not certified",
    }
    raw=json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    data["sha256_without_digest"]=hashlib.sha256(raw).hexdigest()
    out=json.dumps(data,indent=2,sort_keys=True)+"\n"
    p=Path(__file__).with_name("results")/"verification.json"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(out)
    print(out,end="")

if __name__=="__main__": main()
