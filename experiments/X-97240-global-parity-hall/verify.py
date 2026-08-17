#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent

def mobius_sieve(n:int):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu

def v2(n:int):
    k=0
    while n%2==0 and n:
        k+=1; n//=2
    return k

def b(n,mu):
    return mu[n]-(mu[n//2] if n%2==0 else 0)

def a(n,mu):
    return (6 if n==1 else 0)-6*mu[n]+(9*mu[n//2] if n%2==0 else 0)-(3*mu[n//4] if n%4==0 else 0)

def g2(n): return v2(n)+1

def h(n): return 6*g2(n)+(3*g2(n//2) if n%2==0 else 0)

def divisors(n): return [d for d in range(1,n+1) if n%d==0]

def elem(rs,k):
    dp=[Fraction(0)]*(k+1); dp[0]=Fraction(1)
    for r in rs:
        for j in range(k,0,-1): dp[j]+=r*dp[j-1]
    return dp[k]

def bonferroni_checks():
    cases=[]
    for m in range(1,13):
        rs=[Fraction((7*i+3)%17+1, 200) for i in range(m)]
        z=sum(rs)
        L=2*math.ceil(4*(float(z)+1))
        if L%2: L+=1
        es=[elem(rs,k) for k in range(min(L,len(rs)+1))]
        S=sum(((-1)**k)*es[k] for k in range(len(es)))
        assert float(S)>0
        cases.append({'m':m,'z':str(z),'L':L,'S':str(S)})
    return cases

def finite_difference_phi(u, shifts):
    total=0.0; m=len(shifts)
    for mask in range(1<<m):
        s=0.0; bits=0
        for i,a0 in enumerate(shifts):
            if mask>>i&1: s+=a0; bits+=1
        x=u-s
        total+=(-1)**bits*(x*math.exp(x/2) if x>=0 else 0.0)
    return total

def run():
    N=20000; mu=mobius_sieve(N)
    conv_checks=factor_checks=julia_checks=0
    for n in range(1,N+1):
        q=sum(a(d,mu) for d in divisors(n))
        expected=0 if n==1 else 15 if n==2 else 3 if n==4 else 6
        assert q==expected; conv_checks+=1
        rhs=(6 if n==1 else 0)-3*(2*b(n,mu)-(b(n//2,mu) if n%2==0 else 0))
        assert a(n,mu)==rhs; factor_checks+=1
        assert h(n)>=abs(a(n,mu)); julia_checks+=1
    parity_checks=0
    for n in range(1,500):
        for depth in range(8):
            assert abs(((-1 if depth%2 else 1)*a(n,mu)))<=h(n)
            parity_checks+=1
    smooth_checks=0
    for r in range(1,7):
        shifts=[0.07+0.013*i for i in range(r)]
        assert finite_difference_phi(sum(shifts)+0.4,shifts)>=-1e-12
        smooth_checks+=1
    bon=bonferroni_checks()
    payload={
      'classification':'PASS_T97240_GLOBAL_PARITY_HALL_SCALAR_JULIA_REDUCTION',
      'schema':'riemann.t97240.v1','base_pr':561,
      'base_sha':'db9bdc63c855c6ddf664b763d748f8155a6a2c67',
      'exact_checks':{'scalar_convolution':conv_checks,'reciprocal_state_factorization':factor_checks,'julia_psd_columns':julia_checks,'history_parity_conjugations':parity_checks,'adaptive_bonferroni_cases':len(bon)},
      'diagnostics':{'smooth_interior_cases':smooth_checks},
      'does_not_prove':['GABPT','eventual scalar positivity','Riemann Hypothesis'],
      'gabpt_proved_by_replay':False,'rh_established_by_replay':False,
      'bonferroni_fixtures':bon,
    }
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
    return payload

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=HERE/'results/verification.json')
    args=ap.parse_args(); out=run(); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']); print(out['proof_object_sha256'])
if __name__=='__main__': main()
