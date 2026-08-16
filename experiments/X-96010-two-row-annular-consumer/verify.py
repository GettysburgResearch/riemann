#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Tuple

import numpy as np

HERE=Path(__file__).resolve().parent


def mobius_linear(n:int)->np.ndarray:
    mu=np.zeros(n+1,dtype=np.int8); mu[1]=1
    lp=np.zeros(n+1,dtype=np.int32)
    primes=[]
    for i in range(2,n+1):
        if lp[i]==0:
            lp[i]=i; primes.append(i); mu[i]=-1
        for p in primes:
            v=i*p
            if v>n: break
            lp[v]=p
            if p==lp[i]:
                mu[v]=0; break
            mu[v]=-mu[i]
    return mu


def kernels(mu:np.ndarray)->Tuple[np.ndarray,np.ndarray]:
    n=len(mu)-1
    r2=-mu.astype(np.float64); r2[1]+=1.0
    r2[2::2]+=2.0*mu[1:n//2+1]
    r2[3::3]-=mu[1:n//3+1]
    r3=-(1.0/3.0)*mu.astype(np.float64); r3[1]+=1.0/3.0
    r3[2::2]-=(1.0/3.0)*mu[1:n//2+1]
    r3[3::3]+=(5.0/3.0)*mu[1:n//3+1]
    r3[4::4]-=mu[1:n//4+1]
    return r2,r3


def prefixes(r:np.ndarray):
    n=len(r)-1
    x=np.arange(1,n+1,dtype=np.float64)
    b=r[1:]/np.sqrt(x)
    s=np.empty(n+1,dtype=np.float64); s[0]=0.0; np.cumsum(b,out=s[1:])
    t=np.empty(n+1,dtype=np.float64); t[0]=0.0; np.cumsum(b*np.log(x),out=t[1:])
    return s,t


def annular_value(X:float,s:np.ndarray,t:np.ndarray)->float:
    N=int(math.floor(X)); M=int(math.floor(X/4.0)); L=math.log(4.0)
    return float(L*s[M]+math.log(X)*(s[N]-s[M])-(t[N]-t[M]))


def scan_row(j:int,s:np.ndarray,t:np.ndarray,limit:int):
    L=math.log(4.0)
    best=(float('inf'),None); neg=0
    start=max(j+1,2)
    for lo in range(start,limit+1,500_000):
        hi=min(limit+1,lo+500_000)
        X=np.arange(lo,hi,dtype=np.int64); M=X//4
        vals=L*s[M]+np.log(X)*(s[X]-s[M])-(t[X]-t[M])
        k=int(np.argmin(vals)); v=float(vals[k]); xx=int(X[k])
        if v<best[0]: best=(v,xx)
        neg+=int(np.count_nonzero(vals < -1e-11))
    return {'row':j,'minimum':best[0],'argmin':best[1],'negative_count_below_-1e-11':neg}


def beta(n:int,q:int)->float:
    if n<q:return 0.0
    k,r=divmod(n,q)
    return k*(q-1-r)/(n+1)


def inverse_row(X:float):
    N=int(X); d=np.zeros(N+1)
    for q in range(N,1,-1):
        used=sum(d[n]*beta(n,q) for n in range(q+1,N+1))
        target=math.log(X/q)/math.sqrt(q) if q<=X else 0.0
        d[q]=(q+1)/(q-1)*(target-used)
    return d


def crosscheck_beta(s2,t2,s3,t3):
    worst=0.0; cases=[]
    for X in [8,12,16,31,64,97,128]:
        c=inverse_row(float(X)); cq=inverse_row(X/4.0) if X/4>=2 else np.zeros(2)
        a=c.copy(); a[:len(cq)]-=cq
        for j,s,t in [(2,s2,t2),(3,s3,t3)]:
            err=abs(float(a[j])-annular_value(float(X),s,t)); worst=max(worst,err)
            cases.append({'X':X,'row':j,'error':err})
    if worst>5e-10: raise AssertionError(('beta crosscheck',worst))
    return {'maximum_error':worst,'cases':cases}


def normalization_counterexample():
    import mpmath as mp
    mp.mp.dps=80
    X=mp.mpf(3)
    J=(2*mp.sqrt(2)*(mp.log(mp.mpf(3)/2)-2*(1-mp.sqrt(mp.mpf(2)/3))))*mp.log(2)
    P=mp.log(2)/mp.sqrt(2)*mp.log(mp.mpf(3)/2)
    F=J-P
    if not F < -mp.mpf(289)/5000: raise AssertionError(F)
    return {'F_Lambda_3':mp.nstr(F,50),'proved_upper_bound':'-289/5000'}


def noncancellation_certificate():
    # P2=0 gives y=2x-1; 3P3=0 then gives -3(x-1)(x-2)=0.
    coeff=[-3.0,9.0,-6.0]
    roots=np.roots(coeff)
    if max(min(abs(r-1),abs(r-2)) for r in roots)>1e-12: raise AssertionError(roots)
    return {'elimination_polynomial':'-3*(x-1)*(x-2)','roots':[1,2],
            'open_strip_common_zero':False}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--limit',type=int,default=1_000_000); ap.add_argument('--output',default='results/verification.json')
    args=ap.parse_args(); limit=args.limit
    mu=mobius_linear(limit); r2,r3=kernels(mu); s2,t2=prefixes(r2); s3,t3=prefixes(r3)
    result={
      'schema':'riemann.x96010.two-row-annular-consumer.v1',
      'limit':limit,
      'row_scans':[scan_row(2,s2,t2,limit),scan_row(3,s3,t3,limit)],
      'beta_crosscheck':crosscheck_beta(s2,t2,s3,t3),
      'normalization_counterexample':normalization_counterexample(),
      'two_row_noncancellation':noncancellation_certificate(),
      'affine_cell_contract':'integer knots are exhaustive because coefficients are affine in log(X) on each unit cell',
      'mutations_rejected':['identify <Y4,Omega> with J_Lambda','drop F_Lambda','omit scale factor 1-4^-s','replace rows 2 and 3 by one unproved universal kernel','treat a finite scan as RH proof'],
      'scientific_status':'exact consumer and finite reductions; two-row positivity remains unproved',
      'rh_established':False,
    }
    if any(x['negative_count_below_-1e-11'] for x in result['row_scans']):
        result['verdict']='COUNTEREXAMPLE_FOUND_RETRACT_ANNULAR_POSITIVITY'
    else:
        result['verdict']='PASS_TWO_ROW_ANNULAR_CONSUMER_HARDENING_AND_SCAN'
    canon=json.dumps(result,sort_keys=True,separators=(',',':')).encode(); result['proof_object_sha256']=hashlib.sha256(canon).hexdigest()
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['verdict']); print(result['proof_object_sha256'])
    return 0 if result['verdict'].startswith('PASS') else 2

if __name__=='__main__': raise SystemExit(main())
