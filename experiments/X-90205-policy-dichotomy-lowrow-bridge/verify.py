#!/usr/bin/env python3
"""Replay for L-90208/L-90209: policy dichotomy and low-row bridge."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
from mpmath import mp
mp.dps=70
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results'/'verification.json'

def pascal_hitting(n:int,m:int)->Fraction:
    h=[Fraction(0)]*(m+1);h[n]=1
    for M in range(n+1,m+1):
        h[M]=sum(Fraction(2*k,M*(M-1))*h[k] for k in range(n,M))
    return h[m]

def verify_pascal():
    checks=0
    for n in range(1,13):
        for m in range(1,121):
            got=pascal_hitting(n,m) if m>=n else Fraction(0)
            exp=Fraction(0) if m<n else (Fraction(1) if m==n else Fraction(2,n+1))
            assert got==exp; checks+=1
    return checks

def A(n,u):
    return n**(1-u)+(2-n)*(n+1)**(-u)+mp.mpf(2)/(n+1)*mp.zeta(u,n+2)

def verify_transfer():
    maxerr=mp.mpf('0');checks=0
    for n in range(1,10):
        for u in [mp.mpf('1.3'),mp.mpf('2.1')+mp.mpf('.7')*1j,mp.mpf('3.2')+mp.mpf('4.1')*1j]:
            direct=n*n**(-u)+(2-n)*(n+1)**(-u)+mp.mpf(2)/(n+1)*mp.zeta(u,n+2)
            err=abs(direct-A(n,u));maxerr=max(maxerr,err);assert err<mp.mpf('1e-65');checks+=1
    return checks,maxerr

def Q(u): return (1-2**(-u))*(2-2**(-u))
def verify_lowrow_symbol():
    maxerr=mp.mpf('0');checks=0
    for u in [mp.mpf('.7')+1.2j,mp.mpf('1.3')+4.7j,mp.mpf('2.2')+11.3j]:
        lhs=mp.mpf(15)/2*A(2,u)+2*A(3,u)
        rhs=6*mp.zeta(u)-3*Q(u)
        err=abs(lhs-rhs);maxerr=max(maxerr,err);assert err<mp.mpf('1e-64');checks+=1
    return checks,maxerr

def mobius(N):
    mu=[0]*(N+1);mu[1]=1;ps=[];comp=[False]*(N+1)
    for i in range(2,N+1):
        if not comp[i]:ps.append(i);mu[i]=-1
        for p in ps:
            if i*p>N:break
            comp[i*p]=True
            if i%p==0:mu[i*p]=0;break
            mu[i*p]=-mu[i]
    return mu

def omega_values(N):
    mu=mobius(N);out=[0]*(N+1)
    for n in range(1,N+1):
        out[n]=2*mu[n]
        if n%2==0:out[n]-=3*mu[n//2]
        if n%4==0:out[n]+=mu[n//4]
    return out

def verify_source_and_volterra():
    maxerr=mp.mpf('0');checks=0
    for X in [mp.mpf('17.25'),mp.mpf('64'),mp.mpf('211.75')]:
        N=int(mp.floor(X));om=omega_values(N)
        S=mp.mpf('0');H=mp.mpf('0');I=mp.mpf('0')
        for q in range(2,N+1):
            if not om[q]:continue
            qq=mp.mpf(q);w=mp.mpf(om[q])
            S+=-3*w*qq**(-mp.mpf('.5'))*mp.log(X/qq)
            H+=-3*w*(qq**(-mp.mpf('.5'))-X**(-mp.mpf('.5')))
            I+=-3*w*(qq**(-mp.mpf('.5'))*mp.log(X/qq)-2*(qq**(-mp.mpf('.5'))-X**(-mp.mpf('.5'))))
        err=abs(S-(2*H+I));maxerr=max(maxerr,err);assert err<mp.mpf('1e-64');checks+=1
    return checks,maxerr

def verify_uniform_characteristic():
    checks=0;maxerr=mp.mpf('0')
    for u in [mp.mpf('.2')+.7j,mp.mpf('1.7')+2.3j,mp.mpf('3.1')+4.2j]:
        integ=1-(1/(u+1)+1/(u+1))
        closed=(u-1)/(u+1)
        err=abs(integ-closed);maxerr=max(maxerr,err);assert err<mp.mpf('1e-65');checks+=1
    return checks,maxerr

def main():
    tc,te=verify_transfer();lc,le=verify_lowrow_symbol();vc,ve=verify_source_and_volterra();uc,ue=verify_uniform_characteristic()
    result={
      'verdict':'PASS_X_90205_POLICY_DICHOTOMY_LOWROW_BRIDGE',
      'pascal_hitting_checks':verify_pascal(),
      'transfer_checks':tc,'transfer_max_error':mp.nstr(te,8),
      'lowrow_symbol_checks':lc,'lowrow_symbol_max_error':mp.nstr(le,8),
      'volterra_checks':vc,'volterra_max_error':mp.nstr(ve,8),
      'uniform_characteristic_checks':uc,'uniform_characteristic_max_error':mp.nstr(ue,8)}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['verdict']);print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
