#!/usr/bin/env python3
from __future__ import annotations
import json, math
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
RESULT=ROOT/'results'/'verification.json'


def mobius_sieve(n:int)->np.ndarray:
    mu=np.zeros(n+1,dtype=np.int8); mu[1]=1
    primes=[]; comp=np.zeros(n+1,dtype=bool)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            ip=i*p
            if ip>n: break
            comp[ip]=True
            if i%p==0: mu[ip]=0; break
            mu[ip]=-mu[i]
    return mu


def divergence(w:np.ndarray,X:int,mu:np.ndarray)->np.ndarray:
    U=np.zeros(X+2)
    for k in range(1,X+1):
        mk=int(mu[k])
        if mk:
            top=X//k; m=np.arange(1,top+1)
            U[1:top+1]+=mk*w[m*k]
    r=np.zeros(X+2); r[1:X+1]=U[1:X+1]-U[2:X+2]
    return r


def occupation_range(r:np.ndarray,X:int)->np.ndarray:
    s=np.arange(X+2,dtype=float)*r
    events=np.zeros(X+2); active=0.0; M=np.zeros(X+2)
    for n in range(X,1,-1):
        active += events[n]
        M[n]=s[n]+n*active
        b=(n+3)//4; rr=n-b; N=rr-b+1
        C=2*M[n]/(n*N)
        events[rr]+=C; events[b-1]-=C
    return M


def occupation_direct(r:np.ndarray,X:int)->np.ndarray:
    M=np.zeros(X+2)
    for n in range(X,1,-1):
        inc=0.0
        for m in range(n+1,X+1):
            b=(m+3)//4; N=m-2*b+1
            if b<=n<=m-b:
                inc += M[m]*(2*n)/(m*N)
        M[n]=n*r[n]+inc
    return M


def hinge_w(T:int)->np.ndarray:
    w=np.zeros(T+2); q=np.arange(2,T+1,dtype=float)
    w[2:T+1]=1/np.sqrt(q)-1/math.sqrt(T)
    return w


def critical_w(X:int)->np.ndarray:
    w=np.zeros(X+2); q=np.arange(2,X+1,dtype=float)
    w[2:X+1]=np.log(X/q)/np.sqrt(q)
    return w


def exact_step_mutation():
    X=9
    mu=[0,1,-1,-1,0,-1,1,-1,0,0]
    w=[Fraction(0) for _ in range(X+2)]
    for q in range(2,9): w[q]=1
    U=[Fraction(0) for _ in range(X+2)]
    for m in range(1,X+1):
        U[m]=sum((mu[k]*w[m*k] for k in range(1,X//m+1)),Fraction(0))
    r=[Fraction(0) for _ in range(X+2)]
    for m in range(1,X+1): r[m]=U[m]-U[m+1]
    M=[Fraction(0) for _ in range(X+2)]
    for n in range(X,1,-1):
        inc=Fraction(0)
        for m in range(n+1,X+1):
            b=(m+3)//4; N=m-2*b+1
            if b<=n<=m-b:
                inc += M[m]*Fraction(2*n,m*N)
        M[n]=n*r[n]+inc
    assert M[4]==Fraction(-4,3)
    return {'X':9,'target':'1_(2<=q<=8)','M4':'-4/3'}


def policy_exact_checks():
    rows=0
    for m in range(2,101):
        b=(m+3)//4; N=m-2*b+1
        probs=[Fraction(2*k,m*N) for k in range(b,m-b+1)]
        assert sum(probs,Fraction(0))==1
        rows+=1
    # independent direct-vs-range Green propagation
    maxerr=0.0
    for X in (20,50,100):
        mu=mobius_sieve(X); r=divergence(critical_w(X),X,mu)
        a=occupation_range(r,X); b=occupation_direct(r,X)
        maxerr=max(maxerr,float(np.max(np.abs(a-b))))
        assert maxerr<2e-12
    return {'probability_rows':rows,'max_direct_vs_range_error':maxerr}


def exhaustive_hinges(limit=2000):
    negative=0; min_positive=float('inf'); meta=None
    for T in range(3,limit+1):
        mu=mobius_sieve(T); r=divergence(hinge_w(T),T,mu); M=occupation_range(r,T)
        vals=M[2:T+1]
        negative += int(np.sum(vals < -1e-10))
        if T>2:
            nonterminal=M[2:T]
            if len(nonterminal):
                i=int(np.argmin(nonterminal)); v=float(nonterminal[i])
                if v<min_positive: min_positive=v; meta=(T,i+2)
    assert negative==0
    return {'T_min':3,'T_max':limit,'negative_coordinates':negative,
            'smallest_nonterminal':min_positive,
            'smallest_at':{'T':meta[0],'n':meta[1]}}


def spots(target='hinge'):
    out=[]
    for X in (1000,10000,100000,1000000):
        mu=mobius_sieve(X)
        w=hinge_w(X) if target=='hinge' else critical_w(X)
        r=divergence(w,X,mu); M=occupation_range(r,X); vals=M[2:X+1]
        neg=int(np.sum(vals < -1e-9)); assert neg==0
        out.append({'X':X,'negative_coordinates':neg,'M2':float(M[2])})
    return out


def main():
    result={
      'verdict':'PASS_X_90205_ORDERED_BALANCED_HINGE_RECONNAISSANCE',
      'exact_policy':policy_exact_checks(),
      'step_mutation':exact_step_mutation(),
      'hinge_exhaustive':exhaustive_hinges(),
      'hinge_spots':spots('hinge'),
      'critical_spots':spots('critical'),
      'note':'finite scans are reconnaissance only; OBH is not certified cofinally',
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(result,indent=2)+'\n')
    print(result['verdict']); print(json.dumps(result,indent=2))

if __name__=='__main__': main()
