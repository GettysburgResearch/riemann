#!/usr/bin/env python3
"""Exact/directed replay for L-32309 outer-sixty-three-sixty-fourths SHARP theorem."""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
import hashlib, json
from pathlib import Path

DIGITS=24
SCALE=10**DIGITS
T_MAX=16383


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
    a,b=x
    return (k*a,k*b) if k>=0 else (k*b,k*a)


def add(x,y): return x[0]+y[0],x[1]+y[1]

def sub(x,y): return x[0]-y[1],x[1]-y[0]


MU=mobius_sieve(T_MAX)
INV_LO=[0]*(T_MAX+1); INV_HI=[0]*(T_MAX+1)
PRE_LO=[0]*(T_MAX+1); PRE_HI=[0]*(T_MAX+1)
for n in range(1,T_MAX+1):
    INV_LO[n],INV_HI[n]=invsqrt_scaled(n)
    PRE_LO[n]=PRE_LO[n-1]+INV_LO[n]
    PRE_HI[n]=PRE_HI[n-1]+INV_HI[n]

MU64=mobius_sieve(64)
A_LO=[0]*65; A_HI=[0]*65; M=[0]*65
lo=hi=m=0
for k in range(1,65):
    il,ih=INV_LO[k],INV_HI[k]
    if MU64[k]>0: lo+=il; hi+=ih
    elif MU64[k]<0: lo-=ih; hi-=il
    m+=MU64[k]; A_LO[k]=lo; A_HI[k]=hi; M[k]=m

LOCAL={
32:Fraction(-7,1),33:Fraction(-67,10),34:Fraction(-63,10),35:Fraction(-59,10),
36:Fraction(-6,1),37:Fraction(-67,10),38:Fraction(-63,10),39:Fraction(-29,5),
40:Fraction(-59,10),41:Fraction(-13,2),42:Fraction(-36,5),43:Fraction(-39,5),
44:Fraction(-8,1),45:Fraction(-81,10),46:Fraction(-77,10),47:Fraction(-42,5),
48:Fraction(-17,2),49:Fraction(-87,10),50:Fraction(-44,5),51:Fraction(-17,2),
52:Fraction(-43,5),53:Fraction(-46,5),54:Fraction(-47,5),55:Fraction(-9,1),
56:Fraction(-91,10),57:Fraction(-87,10),58:Fraction(-41,5),59:Fraction(-44,5),
60:Fraction(-89,10),61:Fraction(-19,2),62:Fraction(-91,10),63:Fraction(-46,5),
}


def fixed_tail_and_local_gates():
    # C_* = 21/250 + sum I_K, with I_K the continuum cell contribution.
    clo=floor_div(21*SCALE,250); chi=ceil_div(21*SCALE,250)
    for K in range(2,64):
        d=(INV_LO[K]-INV_HI[K+1],INV_HI[K]-INV_LO[K+1])
        p=scale_int(2,mul_scaled(A_LO[K],A_HI[K],d[0],d[1]))
        rat=Fraction(M[K],K*(K+1))
        r=(floor_div(rat.numerator*SCALE,rat.denominator),
           ceil_div(rat.numerator*SCALE,rat.denominator))
        term=sub(p,r); clo+=term[0]; chi+=term[1]
    continuum_gt=clo*500>69*SCALE

    ehi=0
    for K in range(2,64):
        abs_a=max(abs(A_LO[K]),abs(A_HI[K]))
        _,sh=sqrt_scaled(3 if K==2 else 2*(K+1))
        _,ph=mul_scaled(abs_a,abs_a,0,sh)
        ehi+=ph+abs(M[K])*SCALE
    error_lt=ehi<438*SCALE
    assert continuum_gt and error_lt
    assert Fraction(69,500)-Fraction(438,16384)>Fraction(11,100)

    negative={}; local={}
    for K in range(32,64):
        assert A_HI[K]<0
        sl,_=sqrt_scaled(K)
        upper=ceil_div(A_HI[K]*sl,SCALE)-M[K]*SCALE
        negative[str(K)]=upper<0
        _,sh=sqrt_scaled(K+1)
        twice_lower=floor_div(5*A_LO[K]*sh,SCALE)-4*M[K]*SCALE
        c=LOCAL[K]
        local[str(K)]=twice_lower*c.denominator>2*c.numerator*SCALE
    assert all(negative.values()) and all(local.values())

    same={K:LOCAL[K]+Fraction(11*K,50) for K in range(32,64)}
    adverse={K:same[K]-Fraction(1,2) for K in range(32,64) if MU64[K]==1}
    assert all(v>0 for v in same.values()) and all(v>0 for v in adverse.values())
    return continuum_gt,error_lt,negative,local,same,adverse


def u_interval(T,m):
    K=T//m
    p=mul_scaled(A_LO[K],A_HI[K],INV_LO[m],INV_HI[m])
    return sub(p,scale_int(M[K],(INV_LO[T],INV_HI[T])))


def tail64(T):
    J=T//64+1; total=(0,0)
    for K in range(1,64):
        a=max(J,T//(K+1)+1); b=T//K
        if a>b: continue
        sums=(PRE_LO[b]-PRE_LO[a-1],PRE_HI[b]-PRE_HI[a-1])
        p=mul_scaled(A_LO[K],A_HI[K],sums[0],sums[1])
        total=add(total,sub(p,scale_int(M[K]*(b-a+1),(INV_LO[T],INV_HI[T]))))
    return total


def finite_new_strip(T):
    s_lo,_=tail64(T); checked=0; minimum=None
    for j in range(max(2,T//64+1),T):
        if 64*j<=T: continue
        if 32*j>T: break
        uj=u_interval(T,j); uj1=u_interval(T,j+1)
        local_lo=(j+2)*uj[0]-j*uj1[1]
        cert=(j-1)*local_lo+2*s_lo
        assert cert>0,(T,j,cert)
        checked+=1
        if minimum is None or cert*minimum[3]<minimum[2]*(j-1):
            minimum=(T,j,cert,j-1)
    return checked,minimum


def main():
    continuum,error,negative,local,same,adverse=fixed_tail_and_local_gates()
    total=0; globalmin=None
    for T in range(3,T_MAX+1):
        checked,mi=finite_new_strip(T); total+=checked
        if mi and (globalmin is None or mi[2]*globalmin[3]<globalmin[2]*mi[3]): globalmin=mi
    data={
      "schema":"X-32305-outer-sixty-three-sixty-fourths-v1",
      "classification":"DIRECTED_OUTER_SIXTY_THREE_SIXTY_FOURTHS_SHARP_VERIFIED",
      "digits":DIGITS,
      "finite_endpoint_max":T_MAX,
      "finite_new_strip_rows_checked":total,
      "continuum_tail_lower_gt_69_over_500":continuum,
      "tail_error_upper_lt_438":error,
      "tail_at_T16384_gt_11_over_100":True,
      "new_cells_strictly_negative_gates":negative,
      "new_local_lower_gates":local,
      "same_cell_margins":{str(k):f"{v.numerator}/{v.denominator}" for k,v in same.items()},
      "adverse_transition_margins":{str(k):f"{v.numerator}/{v.denominator}" for k,v in adverse.items()},
      "minimum_finite_certificate":{"T":globalmin[0],"j":globalmin[1],"lower_numerator_scaled":str(globalmin[2]),"denominator":globalmin[3]},
      "proof_boundary":"finite new strip through T=16383; T>=16384 analytic via integral cell tail; RH not certified",
    }
    raw=json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    data["sha256_without_digest"]=hashlib.sha256(raw).hexdigest()
    out=json.dumps(data,indent=2,sort_keys=True)+"\n"
    p=Path(__file__).with_name("results")/"verification.json"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(out)
    print(out,end="")

if __name__=="__main__": main()
