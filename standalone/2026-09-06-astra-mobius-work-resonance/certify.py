#!/usr/bin/env python3
"""Directed finite Mobius work certificates; not an RH verifier.

Each new arithmetic event costs a fixed four-state update. All real endpoints
are dyadic enclosures made by integer operations. The full future of the
FINITE input is included by its exact rational observability Gramian.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

BITS = 160
S = 1 << BITS
N_MAX = 65536
CHECKPOINTS = (1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 16384, 65536)
QNUM = ((385,-639,324,-54),(-639,3518,-2882,660),(324,-2882,2536,-600),(-54,660,-600,144))

class VerificationError(ValueError):
    pass

def require(ok: bool, text: str) -> None:
    if not ok:
        raise VerificationError(text)

def ceildiv(n: int, d: int) -> int:
    require(d > 0, 'nonpositive divisor')
    return -((-n)//d)

@dataclass(frozen=True)
class IV:
    lo: int
    hi: int
    def __post_init__(self) -> None:
        require(self.lo <= self.hi, 'reversed interval')
    @staticmethod
    def rat(n: int | F, d: int = 1) -> 'IV':
        q = F(n,d)
        return IV(q.numerator*S//q.denominator, ceildiv(q.numerator*S,q.denominator))
    def __add__(self, other: 'IV') -> 'IV':
        return IV(self.lo+other.lo, self.hi+other.hi)
    def __neg__(self) -> 'IV':
        return IV(-self.hi,-self.lo)
    def __sub__(self, other: 'IV') -> 'IV':
        return self + (-other)
    def __mul__(self, other: 'IV') -> 'IV':
        a = (self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return IV(min(a)//S,ceildiv(max(a),S))
    def scale(self, n: int, d: int = 1) -> 'IV':
        require(d>0,'nonpositive scale denominator')
        a,b=self.lo*n,self.hi*n
        return IV(min(a,b)//d,ceildiv(max(a,b),d))
    def sq(self) -> 'IV':
        m = 0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        M = max(self.lo*self.lo,self.hi*self.hi)
        return IV(m//S,ceildiv(M,S))
    def obj(self) -> dict[str,str]:
        return {'lo':str(self.lo),'hi':str(self.hi),'denominator':str(S)}

ZERO=IV.rat(0)

def add(values) -> IV:
    r=ZERO
    for v in values:r=r+v
    return r

def log_step(n: int) -> IV:
    """log(n/(n-1))=2 atanh(1/(2n-1)), n>=2."""
    require(n>=2,'log-step domain')
    v=2*n-1
    lo=hi=0
    p=v
    j=0
    while True:
        denom=(2*j+1)*p
        lo += (2*S)//denom
        hi += ceildiv(2*S,denom)
        j += 1
        p *= v*v
        # First omitted exponent is 2j+1. All later denominators >=2j+1.
        rem_num=2*v*v
        rem_den=(2*j+1)*p*(v*v-1)
        if rem_num*S < rem_den:
            hi += ceildiv(rem_num*S,rem_den)
            break
        require(j<=BITS,'log-series safety cap')
    return IV(lo,hi)

def reciprocal_sqrt(n: int) -> IV:
    require(n>=1,'square-root domain')
    k=isqrt((S*S)//n)
    return IV(k,k if k*k*n==S*S else k+1)

def mobius(N: int) -> list[int]:
    require(1<=N<=N_MAX,'fixed resource cap')
    mu=[1]*(N+1);mu[0]=0
    prime=bytearray(b'\1')*(N+1)
    for p in range(2,N+1):
        if prime[p]:
            for n in range(p,N+1,p):prime[n]=0;mu[n]=-mu[n]
            for n in range(p*p,N+1,p*p):mu[n]=0
    return mu

def shift(x: list[IV], n: int) -> list[IV]:
    if n==1:return x.copy()
    t=log_step(n);t2=t.sq();t3=t2*t
    ans=[x[0],x[1]+t*x[0],x[2]+t*x[1]+(t2*x[0]).scale(1,2),
         x[3]+t*x[2]+(t2*x[1]).scale(1,2)+(t3*x[0]).scale(1,6)]
    return [z.scale(n-1,n) for z in ans]

def quadratic(x: list[IV]) -> IV:
    return add([x[i].sq().scale(QNUM[i][i],2048) for i in range(4)] +
               [(x[i]*x[j]).scale(QNUM[i][j],1024) for i in range(4) for j in range(i+1,4)])

def digest(data: object) -> str:
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def compute() -> dict[str,object]:
    mu=mobius(N_MAX);x=[ZERO]*4;work=ZERO;diag=ZERO;rows=[]
    lastH=None
    for n in range(1,N_MAX+1):
        x=shift(x,n)
        a=reciprocal_sqrt(n).scale(mu[n]) if mu[n] else ZERO
        output=add(x[j].scale(QNUM[0][j],2048) for j in range(4))
        work=work+(a*output).scale(2)
        diag=diag+IV.rat(385*mu[n]*mu[n],2048*n)
        x[0]=x[0]+a
        if n in CHECKPOINTS:
            J=diag+work;store=quadratic(x);H=J-store
            require(J.lo>0,f'finite full norm n={n}')
            require(store.lo>0,f'future storage n={n}')
            if n>1:require(H.lo>0,f'past energy n={n}')
            else:require(H.lo<=0<=H.hi,'initial past energy')
            if lastH is not None:require(H.lo>lastH.hi,f'checkpoint monotonicity n={n}')
            lastH=H
            require(max(v.hi-v.lo for v in (J,store,H,diag,work)) < 1 << 70,'interval width')
            rows.append({'N':n,'D':diag.obj(),'W':work.obj(),'J':J.obj(),
                         'H_logN':H.obj(),'future':store.obj()})
    byN={row['N']:row for row in rows}
    require(int(byN[3]['W']['lo'])*20>S,'actual W3>1/20')
    require(int(byN[64]['H_logN']['lo'])*2>S,'cross-check H(log64)>1/2')
    require(int(byN[64]['H_logN']['hi'])*25<13*S,'cross-check H(log64)<13/25')
    for field,lo,hi in [('J',721,723),('H_logN',718,720),('future',2,3)]:
        item=byN[N_MAX][field]
        require(int(item['lo'])*1000>lo*S and int(item['hi'])*1000<hi*S,'last checkpoint rational bound '+field)
    ans={'schema':'MWR26.directed-finite-work.v1','arithmetic':'DIRECTED_INTEGER_INTERVAL',
         'bits':BITS,'integer_events':N_MAX,'checkpoints':list(CHECKPOINTS),'results':rows,
         'mu_sha256':hashlib.sha256(bytes(v+1 for v in mu[1:])).hexdigest(),
         'scope':'All 65536 prescribed events; complete future tail of EACH checkpoint finite input. Not the tail of the untruncated infinite Mobius source. No asymptotic extrapolation.'}
    ans['payload_sha256']=digest(ans)
    return ans

def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--expect',type=Path)
    ns=ap.parse_args()
    try:
        result=compute()
        if ns.expect:require(json.loads(ns.expect.read_text())==result,'retained certificate differs from full replay')
        text=json.dumps(result,sort_keys=True,indent=2)+'\n'
        if ns.output:ns.output.write_text(text)
        else:print(text,end='')
        return 0
    except (VerificationError,OSError,json.JSONDecodeError) as exc:
        print(str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
