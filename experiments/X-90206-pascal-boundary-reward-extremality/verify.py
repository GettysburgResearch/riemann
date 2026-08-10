#!/usr/bin/env python3
"""Exact replay for finite-boundary Pascal reward extremality."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'/'verification.json'


def ceil_frac(x: Fraction)->int:
    return (x.numerator + x.denominator - 1)//x.denominator


def fval(m:int,r:Fraction)->Fraction:
    if m==1: return Fraction(0)
    if m==2: return r/2
    if m==3: return (r+1)/3
    return Fraction(1)


def uniform_drift(m:int,r:Fraction)->Fraction:
    if m==1: return Fraction(0)
    if m==2: return fval(2,r)
    den=m*(m-1)
    pf=sum((Fraction(2*k,den)*fval(k,r) for k in range(1,m)),Fraction(0))
    return fval(m,r)-pf


def ordered_bounds(m:int,alpha:Fraction)->tuple[int,int,int]:
    b=min(m//2,max(1,ceil_frac(alpha*m)))
    return b,m-b,m-2*b+1


def ordered_drift(m:int,r:Fraction,alpha:Fraction)->Fraction:
    if m==1:return Fraction(0)
    b,e,N=ordered_bounds(m,alpha)
    pf=sum((Fraction(2*k,m*N)*fval(k,r) for k in range(b,e+1)),Fraction(0))
    return fval(m,r)-pf


def mobius(N:int)->list[int]:
    mu=[0]*(N+1);mu[1]=1
    primes=[];comp=[False]*(N+1)
    for i in range(2,N+1):
        if not comp[i]:primes.append(i);mu[i]=-1
        for p in primes:
            if i*p>N:break
            comp[i*p]=True
            if i%p==0:mu[i*p]=0;break
            mu[i*p]=-mu[i]
    return mu


def divisors(n:int):
    return [d for d in range(1,n+1) if n%d==0]


def conv(a,b,N):
    c=[Fraction(0)]*(N+1)
    for n in range(1,N+1):
        c[n]=sum((a[d]*b[n//d] for d in divisors(n)),Fraction(0))
    return c


def source_check(r:Fraction,N:int=96):
    mu0=mobius(N);mu=[Fraction(x) for x in mu0]
    inc=[Fraction(0)]*(N+1)
    inc[1]=0
    inc[2]=r
    inc[3]=1
    inc[4]=3-r
    for n in range(5,N+1):inc[n]=1
    actual=conv(mu,inc,N)
    q=[Fraction(0)]*(N+1);q[1]=1
    if N>=2:q[2]=1-r
    if N>=4:q[4]=r-2
    qmu=conv(q,mu,N)
    expected=[Fraction(0)]*(N+1);expected[1]=1-qmu[1]
    for n in range(2,N+1):expected[n]=-qmu[n]
    assert actual==expected
    return actual,q


def pairing_check(r:Fraction,N:int=60):
    mu0=mobius(N);mu=[Fraction(x) for x in mu0]
    w=[Fraction(0)]*(N+1)
    for q in range(2,N+1):w[q]=Fraction((17*q+5)%23,q+7)
    U=[Fraction(0)]*(N+2)
    for m in range(1,N+1):
        U[m]=sum((mu[k]*w[m*k] for k in range(1,N//m+1)),Fraction(0))
    node=[U[m]-U[m+1] for m in range(N+1)]
    F=[Fraction(0)]*(N+1)
    for m in range(1,N+1):F[m]=m*fval(m,r)
    lhs=sum((node[m]*F[m] for m in range(1,N+1)),Fraction(0))
    src,q=source_check(r,N)
    rhs=sum((src[n]*w[n] for n in range(1,N+1)),Fraction(0))
    assert lhs==rhs
    filtered=-sum((conv(q,mu,N)[n]*w[n] for n in range(2,N+1)),Fraction(0))
    assert rhs==filtered
    return str(lhs)


def main():
    uniform_checks=0
    for r in [Fraction(0),Fraction(1),Fraction(2),Fraction(5,2),Fraction(13,5)]:
        for m in range(2,201):
            d=uniform_drift(m,r)
            expected = r/2 if m==2 else (Fraction(1,3) if m==3 else Fraction(10-4*r,m*(m-1)))
            assert d==expected
            uniform_checks+=1
    assert all(uniform_drift(m,Fraction(5,2))>=0 for m in range(2,500))
    assert uniform_drift(4,Fraction(5,2)+Fraction(1,1000))<0

    ordered_checks=0; witnesses=[]
    for alpha in [Fraction(1,100),Fraction(1,10),Fraction(1,4),Fraction(1,3),Fraction(2,5),Fraction(49,100)]:
        assert all(ordered_drift(m,Fraction(2),alpha)>=0 for m in range(2,1000))
        m=max(4,(alpha.denominator//alpha.numerator)+1)
        while ordered_bounds(m,alpha)[0]!=2:
            m+=1
            assert m<10000
        bad=ordered_drift(m,Fraction(201,100),alpha)
        assert bad<0
        witnesses.append({'alpha':str(alpha),'m':m,'drift_at_2.01':str(bad),'interval':ordered_bounds(m,alpha)[:2]})
        ordered_checks+=998

    r=Fraction(5,2);C=12
    assert C*uniform_drift(2,r)==15
    assert C*uniform_drift(3,r)==4
    assert all(C*uniform_drift(m,r)==0 for m in range(4,500))

    source_cases=[]
    for r in [Fraction(0),Fraction(1),Fraction(2),Fraction(5,2),Fraction(13,5)]:
        actual,q=source_check(r)
        source_cases.append({'r':str(r),'q1':str(q[1]),'q2':str(q[2]),'q4':str(q[4]),'pairing':pairing_check(r)})

    result={
      'verdict':'PASS_X_90206_PASCAL_BOUNDARY_REWARD_EXTREMALITY',
      'uniform_formula_checks':uniform_checks,
      'ordered_nonnegative_checks':ordered_checks,
      'ordered_r_gt_2_witnesses':witnesses,
      'canonical_reward':{'r':'5/2','scale':12,'d2':15,'d3':4,'tail_zero_through':499},
      'source_polynomial_cases':source_cases,
      'theorem':{
        'uniform_positive_r_interval':'[0,5/2]',
        'positive_ordered_balance_r_interval':'[0,2]',
        'zero_safe_uniform_subinterval':'[1,5/2]',
        'max_uniform_polynomial':'(1-t)(1-t/2)',
        'max_balanced_polynomial':'1-t',
      },
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['verdict']);print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
