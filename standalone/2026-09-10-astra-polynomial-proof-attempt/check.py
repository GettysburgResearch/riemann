#!/usr/bin/env python3
"""Exact/interval controls for a failed proof step, not a proof of Q-AC28.

Standard-library only. The interval pattern and Machin/Bernoulli primitives
are adapted from the pinned AC28 checker and are not an independent audit of
that code. Polynomial integration and divisor-recursion/trial-factorization
provide different finite constructions. No asymptotic conclusion is inferred
from this replay.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial, isqrt
from pathlib import Path
import json

BITS=256
S=1<<BITS
PARENT='b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e'

def require(ok, message):
    if not ok: raise ValueError(message)
def down(x):
    x=F(x); return F(x.numerator*S//x.denominator,S)
def up(x):return -down(-F(x))
class I:
    def __init__(self,lo,hi=None):
        hi=lo if hi is None else hi
        require(F(lo)<=F(hi),'inverted interval')
        self.lo,self.hi=down(lo),up(hi)
    def __add__(self,b):
        b=iv(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-iv(b)
    def __rsub__(self,b):return iv(b)+-self
    def __mul__(self,b):
        b=iv(b);q=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(q),max(q))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=iv(b);require(b.lo*b.hi>0,'division through zero')
        return self*I(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return iv(b)/self
    def __pow__(self,k):
        require(type(k)is int and k>=0,'invalid power')
        out=I(1);base=self
        while k:
            if k&1:out=out*base
            base=base*base;k//=2
        return out
    def pair(self):return [int(self.lo*S),int(self.hi*S)]
def iv(x):return x if isinstance(x,I) else I(x)
def rat(x):x=F(x);return [x.numerator,x.denominator]
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(x):return sha256(enc(x)).hexdigest()
def same(a,b):
    if type(a)is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def bernoulli(n):
    out=[F(1)]
    for j in range(1,n+1):
        out.append(-sum((F(comb(j+1,k))*out[k] for k in range(j)),F(0))/F(j+1))
    return out

def atan(q,terms):
    a=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),F(0))
    b=a+F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return I(min(a,b),max(a,b))
def odd_zeta(k,pi,B):
    s=2*k
    c=(1-F(1,2**s))*((-1)**(k+1))*B[s]*F(2**(s-1),factorial(s))
    return c*pi**s

def mu_trial(n):
    if n==1:return 1
    out=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;out=-out
            if n%p==0:return 0
        p+=1
    return -out if n>1 else out

def mu_inverse(K):
    a=[0]*(K+1);a[1]=1
    for n in range(2,K+1):a[n]=-sum(a[d] for d in range(1,n) if n%d==0)
    return a

def a_rec(N):
    a=F(1)
    for j in range(N):a*=F(2*j+2,2*j+3)
    return a

def integrate_square(c,lo,hi):
    v=I(0)
    for i,a in c.items():
        for j,b in c.items():v+=a*b*F(hi**(i+j+1)-lo**(i+j+1),i+j+1)
    return v

def evaluate(c,t):return sum((x*t**j for j,x in c.items()),I(0))
def qeval(N,t):return sum((F((-1)**j*comb(N,j),2*j+1)*t**(2*j+1) for j in range(N+1)),F(0))

def payload():
    beta=[]
    for N in range(65):
        c=[(-1)**j*comb(N,j) for j in range(N+1)]
        sq=[0]*(2*N+1)
        for j,u in enumerate(c):
            for k,v in enumerate(c):sq[j+k]+=u*v
        require(sq==[(-1)**j*comb(2*N,j) for j in range(2*N+1)],'product coefficients')
        A=sum((F(c[j],2*j+1) for j in range(N+1)),F(0))
        un=sum((F(x,2*j+1) for j,x in enumerate(sq)),F(0))
        wt=sum((F(x,2*j+3) for j,x in enumerate(sq)),F(0))
        require(A==a_rec(N)==F(2**(2*N)*factorial(N)**2,factorial(2*N+1)),'a_N reconstruction')
        require(un==a_rec(2*N) and un==(4*N+3)*wt,'critical weight identity')
        require((2*N+1)*A*A>=1 and (N+1)*A*A<=1,'a_N bounds')
        beta.append({'N':N,'a_N':rat(A),'unweighted':rat(un),'weighted':rat(wt),
                     'norm_ratio':4*N+3,'endpoint_ratio':rat(A*A/wt)})
    mu=mu_inverse(512)
    require(mu[1:]==[mu_trial(n) for n in range(1,513)],'independent Mobius construction')
    harmon=[];cur=F(0);odd=F(0)
    for n in range(1,513):
        cur+=F(mu[n],n)
        if n%2:odd+=F(mu[n],n)
        require(abs(cur)<=1 and abs(odd)<=2,'finite harmonic bound')
        if n in [1,2,3,16,64,128,256,512]:harmon.append([n,rat(cur),rat(odd)])
    pi=16*atan(5,100)-4*atan(239,50)
    B=bernoulli(66);Z=[odd_zeta(k,pi,B) for k in range(1,34)]
    require(all(z.lo>1 for z in Z),'positive native even-zeta data')
    native=[]
    for N in [0,1,2,4,8,16,32]:
        q={2*j+1:F((-1)**j*comb(N,j),2*j+1) for j in range(N+1)}
        p={2*j+1:q[2*j+1]/Z[j] for j in range(N+1)}
        e={0:I(a_rec(N))}
        for j in range(N+1):e[2*j+1]=q[2*j+1]*(1/Z[j]-1)
        pnorm=integrate_square(p,0,1);enorm=integrate_square(e,1,3)
        require(pnorm.lo>0 and pnorm.hi<=4*a_rec(N)**2,'native input bound')
        require(enorm.lo>0 and enorm.hi<=8*a_rec(N)**2,'native output bound')
        points=[]
        for t in [F(1,4),F(1,2),F(1)]:
            partial=sum((F(mu[n],n)*qeval(N,t/n) for n in range(1,257,2)),F(0))
            target=evaluate(p,t);error=t/F(256)
            require(target.lo<=partial+error and target.hi>=partial-error,'native inverse partial sum/tail')
            points.append({'type':'p','t':rat(t),'interval':target.pair(),'partial_interval':I(partial).pair(),'tail':rat(error)})
        for t in [F(1),F(3,2),F(2),F(3)]:
            partial=a_rec(N)+sum((F(mu[n],n)*qeval(N,t/n) for n in range(3,257,2)),F(0))
            target=evaluate(e,t);error=t/F(256)
            require(target.lo<=partial+error and target.hi>=partial-error,'compensated output partial sum/tail')
            points.append({'type':'E','t':rat(t),'interval':target.pair(),'partial_interval':I(partial).pair(),'tail':rat(error)})
        force=a_rec(2*N)/F(4*N+3)
        finite_ratio=(enorm-F(1,100)*pnorm)/(4*force)
        native.append({'N':N,'p_norm_squared':pnorm.pair(),'E_norm_squared':enorm.pair(),
                       'forcing_squared':rat(force),'finite_eta_001_ratio':finite_ratio.pair(),'points':points})
    return {'schema':'polynomial-direct-attempt/v1','parent':PARENT,
            'target_proved':False,'rh_proved':False,
            'claim':'auxiliary unweighted graph estimate refuted; target remains open',
            'bits':BITS,'beta_rows':beta,'harmonic_samples':harmon,
            'native_cases':native,'mobius_values_checked':512,
            'scope':'Finite primitive replays; all-N identities rely on the written algebra.'}

def seal(p):return {'payload':p,'sha256':sha(p)}
def accept(r,expected):
    require(type(r)is dict and set(r)=={'payload','sha256'},'envelope')
    require(r['sha256']==sha(r['payload']),'checksum')
    require(same(r['payload'],expected),'primitive reconstruction mismatch')
def selftest(p):
    accept(seal(p),p)
    changes=[lambda x:x.update(target_proved=True),lambda x:x.update(rh_proved=True),
             lambda x:x['beta_rows'][1].update(norm_ratio=3),lambda x:x['beta_rows'].pop(),
             lambda x:x['native_cases'][0].update(forcing_squared=[0,1]),
             lambda x:x.update(parent='0'*40),lambda x:x.update(bits=128),
             lambda x:x.update(claim='all-degree inequality proved')]
    for mutate in changes:
        y=deepcopy(p);mutate(y);require(not same(y,p),'ineffective mutation')
        try:accept(seal(y),p)
        except ValueError:pass
        else:raise ValueError('resealed corruption accepted')
    return len(changes)
def atom(_):raise ValueError('float/nonfinite JSON prohibited')
def pairs(rows):
    out={}
    for k,v in rows:require(k not in out,'duplicate key');out[k]=v
    return out

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path);g.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true');a=ap.parse_args();p=payload()
    if a.write:a.write.write_bytes(enc(seal(p))+b'\n')
    else:accept(json.loads(a.check.read_text(),parse_float=atom,parse_constant=atom,object_pairs_hook=pairs),p)
    n=selftest(p) if a.self_test else 0
    print('PASS_POLYNOMIAL_ATTEMPT',sha(p),'resealed_rejections='+str(n),'TARGET_NOT_PROVED')
if __name__=='__main__':main()
