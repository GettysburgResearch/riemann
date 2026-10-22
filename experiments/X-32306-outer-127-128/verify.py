#!/usr/bin/env python3
"""Exact/directed replay for L-32310 outer-127/128 SHARP theorem."""
from fractions import Fraction
from math import isqrt
import hashlib, json
from pathlib import Path

DIGITS=14
SCALE=10**DIGITS
T_MAX=65535
K_MAX=127
M_MAX=T_MAX//64+2


def mobius_sieve(n):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=bytearray(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            v=i*p
            if v>n: break
            comp[v]=1
            if i%p==0: mu[v]=0; break
            mu[v]=-mu[i]
    return mu


def invsqrt_scaled(n):
    a=isqrt((SCALE*SCALE)//n)
    while (a+1)*(a+1)*n<=SCALE*SCALE: a+=1
    while a*a*n>SCALE*SCALE: a-=1
    return a,a+1


def sqrt_scaled(n):
    a=isqrt(n*SCALE*SCALE)
    return a, a if a*a==n*SCALE*SCALE else a+1


def mul_scaled(a,b,c,d):
    vals=(a*c,a*d,b*c,b*d)
    return min(vals)//SCALE, -((-max(vals))//SCALE)


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
    if MU[k]>0: lo+=INV_LO[k]; hi+=INV_HI[k]
    elif MU[k]<0: lo-=INV_HI[k]; hi-=INV_LO[k]
    m+=MU[k]; A_LO[k]=lo; A_HI[k]=hi; M[k]=m

# Precompute A_K/sqrt(m) for every m used by the new finite strip.
P_LO=[[0]*(M_MAX+1) for _ in range(K_MAX+1)]
P_HI=[[0]*(M_MAX+1) for _ in range(K_MAX+1)]
for K in range(1,K_MAX+1):
    for m in range(1,M_MAX+1):
        P_LO[K][m],P_HI[K][m]=mul_scaled(A_LO[K],A_HI[K],INV_LO[m],INV_HI[m])


def fixed_gates():
    # Continuum tail lower bound: 21/250 + sum I_K.
    cont_lo=(21*SCALE)//250
    for K in range(2,K_MAX+1):
        dlo=INV_LO[K]-INV_HI[K+1]
        dhi=INV_HI[K]-INV_LO[K+1]
        p_lo,_=mul_scaled(A_LO[K],A_HI[K],dlo,dhi)
        p_lo*=2
        q=Fraction(M[K],K*(K+1))
        q_hi=-((-q.numerator*SCALE)//q.denominator)
        cont_lo+=p_lo-q_hi
    continuum=1000*cont_lo>103*SCALE

    err_hi=0
    for K in range(2,K_MAX+1):
        abs_a=max(abs(A_LO[K]),abs(A_HI[K]))
        _,sh=sqrt_scaled(3 if K==2 else 2*(K+1))
        _,p_hi=mul_scaled(abs_a,abs_a,0,sh)
        err_hi+=p_hi+abs(M[K])*SCALE
    error=err_hi<1218*SCALE

    negative={}; local={}
    for K in range(64,128):
        sl,sh=sqrt_scaled(K)
        _,p_hi=mul_scaled(A_LO[K],A_HI[K],sl,sh)
        negative[str(K)]=p_hi-M[K]*SCALE<0

        sl,sh=sqrt_scaled(K+1)
        p_lo,_=mul_scaled(A_LO[K],A_HI[K],sl,sh)
        twice_local=5*p_lo-4*M[K]*SCALE
        # local > -4K/25; twice_local is twice the scaled local lower bound.
        local[str(K)]=25*twice_local>-8*K*SCALE

    tail=Fraction(103,1000)-Fraction(1218,65536)
    assert continuum and error and all(negative.values()) and all(local.values())
    assert tail>Fraction(21,250)
    assert Fraction(64,125)-Fraction(1,2)==Fraction(3,250)>0
    return continuum,error,negative,local


def u_interval(T,m):
    K=T//m
    lo=P_LO[K][m]; hi=P_HI[K][m]; mk=M[K]
    if mk>=0:
        return lo-mk*INV_HI[T], hi-mk*INV_LO[T]
    return lo-mk*INV_LO[T], hi-mk*INV_HI[T]


def tail_start(T,J):
    lo=hi=0
    for K in range(1,min(K_MAX,T//J)+1):
        a=max(J,T//(K+1)+1); b=T//K
        if a>b: continue
        s_lo=PRE_LO[b]-PRE_LO[a-1]
        s_hi=PRE_HI[b]-PRE_HI[a-1]
        p_lo,p_hi=mul_scaled(A_LO[K],A_HI[K],s_lo,s_hi)
        cnt=b-a+1; mk=M[K]
        if mk>=0:
            lo+=p_lo-mk*cnt*INV_HI[T]; hi+=p_hi-mk*cnt*INV_LO[T]
        else:
            lo+=p_lo-mk*cnt*INV_LO[T]; hi+=p_hi-mk*cnt*INV_HI[T]
    return lo,hi


def finite_base():
    total=0; minimum=None
    for T in range(3,T_MAX+1):
        j0=max(2,T//128+1); j1=T//64
        if j0>j1: continue
        s_lo,_=tail_start(T,j0)
        for j in range(j0,j1+1):
            uj=u_interval(T,j); uj1=u_interval(T,j+1)
            local_lo=(j+2)*uj[0]-j*uj1[1]
            cert=(j-1)*local_lo+2*s_lo
            assert cert>0,(T,j,cert)
            total+=1
            if minimum is None or cert*minimum[3]<minimum[2]*(j-1):
                minimum=(T,j,cert,j-1)
            # S(j+1)=S(j)-u(j): lower bound subtracts the upper endpoint.
            s_lo-=uj[1]
    return total,minimum


def main():
    continuum,error,negative,local=fixed_gates()
    total,minimum=finite_base()
    core={
      "schema":"X-32306-outer-one-hundred-twenty-seven-one-hundred-twenty-eighths-v1",
      "classification":"DIRECTED_OUTER_127_128_SHARP_VERIFIED",
      "digits":DIGITS,
      "finite_endpoint_max":T_MAX,
      "finite_new_strip_rows_checked":total,
      "continuum_tail_lower_gt_103_over_1000":continuum,
      "tail_error_upper_lt_1218":error,
      "tail_at_T65536_gt_21_over_250":True,
      "new_cells_strictly_negative_gates":negative,
      "new_local_lower_gt_minus_4K_over_25_gates":local,
      "uniform_same_cell_margin":"K/125",
      "uniform_adverse_transition_margin_at_K64":"3/250",
      "minimum_finite_certificate":{
        "T":minimum[0],"j":minimum[1],
        "lower_numerator_scaled":str(minimum[2]),"denominator":minimum[3]},
      "proof_boundary":"finite new strip through T=65535; T>=65536 analytic via integral cell tail; RH not certified",
    }
    raw=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["sha256_without_digest"]=hashlib.sha256(raw).hexdigest()
    out=json.dumps(core,indent=2,sort_keys=True)+"\n"
    p=Path(__file__).with_name("results")/"verification.json"
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(out)
    print(out,end="")

if __name__=="__main__": main()
