#!/usr/bin/env python3
"""Exact/directed replay for L-32311 outer-255/256 SHARP theorem."""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
import hashlib, json
from pathlib import Path

DIGITS=16
SCALE=10**DIGITS
T_MAX=262143
K_MAX=255


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


def floor_div(x,d): return x//d

def ceil_div(x,d): return -((-x)//d)


def mul_scaled(a,b,c,d):
    vals=(a*c,a*d,b*c,b*d)
    return floor_div(min(vals),SCALE),ceil_div(max(vals),SCALE)


def scale_int(k,x):
    return (k*x[0],k*x[1]) if k>=0 else (k*x[1],k*x[0])


def sub(x,y): return x[0]-y[1],x[1]-y[0]


MU=mobius_sieve(T_MAX)
INV_LO=[0]*(T_MAX+1); INV_HI=[0]*(T_MAX+1)
PRE_LO=[0]*(T_MAX+1); PRE_HI=[0]*(T_MAX+1)
for n in range(1,T_MAX+1):
    INV_LO[n],INV_HI[n]=invsqrt_scaled(n)
    PRE_LO[n]=PRE_LO[n-1]+INV_LO[n]
    PRE_HI[n]=PRE_HI[n-1]+INV_HI[n]

A_LO=[0]*(K_MAX+1); A_HI=[0]*(K_MAX+1); M=[0]*(K_MAX+1)
lo=hi=m=0
for k in range(1,K_MAX+1):
    il,ih=INV_LO[k],INV_HI[k]
    if MU[k]>0: lo+=il; hi+=ih
    elif MU[k]<0: lo-=ih; hi-=il
    m+=MU[k]; A_LO[k]=lo; A_HI[k]=hi; M[k]=m


def fixed_gates():
    # 21/250 + sum I_K > 3/40.
    clo=floor_div(21*SCALE,250)
    for K in range(2,256):
        d=(INV_LO[K]-INV_HI[K+1],INV_HI[K]-INV_LO[K+1])
        p=scale_int(2,mul_scaled(A_LO[K],A_HI[K],d[0],d[1]))
        rat=Fraction(M[K],K*(K+1))
        r=(floor_div(rat.numerator*SCALE,rat.denominator),
           ceil_div(rat.numerator*SCALE,rat.denominator))
        clo+=sub(p,r)[0]
    continuum_gt=clo*40>3*SCALE

    # Sum E_K < 3162.
    ehi=0
    for K in range(2,256):
        abs_a=max(abs(A_LO[K]),abs(A_HI[K]))
        _,sh=sqrt_scaled(3 if K==2 else 2*(K+1))
        _,ph=mul_scaled(abs_a,abs_a,0,sh)
        ehi+=ph+abs(M[K])*SCALE
    error_lt=ehi<3162*SCALE
    assert continuum_gt and error_lt
    assert Fraction(3,40)-Fraction(3162,262144)>Fraction(1,16)

    negative={}; same={}; adverse={}
    same_min=None; adverse_min=None
    for K in range(128,256):
        assert A_HI[K]<0
        sl,_=sqrt_scaled(K)
        upper=ceil_div(A_HI[K]*sl,SCALE)-M[K]*SCALE
        negative[str(K)]=upper<0

        # twice the local lower bound L_K:
        # 2 L_K = 5 A_K sqrt(K+1) - 4 M_K.
        _,sh=sqrt_scaled(K+1)
        twice_lower=floor_div(5*A_LO[K]*sh,SCALE)-4*M[K]*SCALE

        # 8*(L_K+K/8) = 4*(2L_K)+K.
        eight_same=4*twice_lower+K*SCALE
        same[str(K)]=eight_same>0
        margin_floor=floor_div(eight_same,8)
        if same_min is None or margin_floor<same_min[0]:
            same_min=(margin_floor,K)

        if MU[K]==1:
            # Subtract the universal transition loss 1/2.
            eight_adverse=eight_same-4*SCALE
            adverse[str(K)]=eight_adverse>0
            adverse_floor=floor_div(eight_adverse,8)
            if adverse_min is None or adverse_floor<adverse_min[0]:
                adverse_min=(adverse_floor,K)

    assert all(negative.values()) and all(same.values()) and all(adverse.values())
    return continuum_gt,error_lt,negative,same,adverse,same_min,adverse_min


def tail256(T):
    J=T//256+1
    total_lo=0
    tlo,thi=INV_LO[T],INV_HI[T]
    for K in range(1,256):
        a=max(J,T//(K+1)+1); b=T//K
        if a>b: continue
        sums=(PRE_LO[b]-PRE_LO[a-1],PRE_HI[b]-PRE_HI[a-1])
        pl,ph=mul_scaled(A_LO[K],A_HI[K],sums[0],sums[1])
        count=b-a+1
        if M[K]>=0:
            pl-=M[K]*count*thi
        else:
            pl-=M[K]*count*tlo
        total_lo+=pl
    return total_lo


def main():
    continuum,error,negative,same,adverse,same_min,adverse_min=fixed_gates()

    target=Fraction(1,16)
    target_scaled=ceil_div(target.numerator*SCALE*SCALE,target.denominator)
    minimum=None
    for T in range(256,T_MAX+1):
        s_lo=tail256(T)
        # S_T(J_256)/sqrt(T) > 1/16.
        margin=s_lo*INV_LO[T]-target_scaled
        assert margin>0,(T,margin)
        if minimum is None or margin<minimum[0]: minimum=(margin,T)

    data={
      "schema":"X-32307-outer-two-hundred-fifty-five-two-hundred-fifty-sixths-v1",
      "classification":"DIRECTED_OUTER_TWO_HUNDRED_FIFTY_FIVE_TWO_HUNDRED_FIFTY_SIXTHS_SHARP_VERIFIED",
      "digits":DIGITS,
      "finite_tail_endpoint_min":256,
      "finite_tail_endpoint_max":T_MAX,
      "finite_tail_endpoints_checked":T_MAX-255,
      "finite_tail_min_margin_endpoint":minimum[1],
      "finite_tail_min_margin_scaled":str(minimum[0]),
      "finite_tail_margin_scale":str(SCALE*SCALE),
      "continuum_tail_lower_gt_3_over_40":continuum,
      "tail_error_upper_lt_3162":error,
      "tail_at_T262144_gt_1_over_16":True,
      "new_cells_strictly_negative":all(negative.values()),
      "same_cell_gates_positive":all(same.values()),
      "adverse_transition_gates_positive":all(adverse.values()),
      "same_cell_min_margin":{
          "K":same_min[1],
          "lower_margin_scaled":str(same_min[0]),
          "scale":str(SCALE),
          "orientation_decimal":format(same_min[0]/SCALE,".15g"),
      },
      "adverse_transition_min_margin":{
          "K":adverse_min[1],
          "lower_margin_scaled":str(adverse_min[0]),
          "scale":str(SCALE),
          "orientation_decimal":format(adverse_min[0]/SCALE,".15g"),
      },
      "proof_boundary":"imports L-32310 for j>T/128; finite tail gate T=256..262143; T>=262144 analytic; fixed quotient gates K=128..255; RH not certified",
    }
    raw=json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    data["sha256_without_digest"]=hashlib.sha256(raw).hexdigest()
    out=json.dumps(data,indent=2,sort_keys=True)+"\n"
    p=Path(__file__).with_name("results")/"verification.json"
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(out)
    print(out,end="")


if __name__=="__main__": main()
