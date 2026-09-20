"""Classical integer arithmetic and strict report utilities; no numerical decisions."""
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

def require(ok, message):
    if not ok: raise ValueError(message)

def sieve(N):
    spf=list(range(N+1))
    for p in range(2,isqrt(N)+1):
        if spf[p]==p:
            for n in range(p*p,N+1,p):
                if spf[n]==n: spf[n]=p
    mu=[0]*(N+1); rad=[1]*(N+1); core=[1]*(N+1)
    mu[1]=1
    for n in range(2,N+1):
        p=spf[n]; q=n//p
        mu[n]=0 if q%p==0 else -mu[q]
        rad[n]=rad[q] if q%p==0 else rad[q]*p
        core[n]=core[q]//p if core[q]%p==0 else core[q]*p
    return spf,mu,rad,core,[p for p in range(2,N+1) if spf[p]==p]

def divisors(N):
    out=[[] for _ in range(N+1)]
    for d in range(1,N+1):
        for n in range(d,N+1,d): out[n].append(d)
    return out

def residue(s,d):
    r=s%d
    return r if 2*r<=d else r-d

def near_candidates(s,H,divs):
    # Every pair gets one canonical signed nearest-multiple remainder.
    for r in range(-H,H+1):
        n=s-r
        if n<1 or n>=len(divs): continue
        for d in divs[n]:
            if d<s and residue(s,d)==r: yield d,abs(r)

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)

def strict_read(path):
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out,'duplicate key');out[k]=v
        return out
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite')))

def completed_source(Y,mu):
    c={n:Fraction(mu[n]) for n in range(1,Y+1) if mu[n]}
    residual=sum((v/n for n,v in c.items()),Fraction())
    n=Y
    while residual:
        n+=1
        v=-min(Fraction(3),abs(residual)*n)*(1 if residual>0 else -1)
        c[n]=v;residual+=v/n
    require(max(abs(v) for v in c.values())<=3,'coefficient cap')
    require(sum((v/n for n,v in c.items()),Fraction())==0,'reciprocal balance')
    return c

def convolution(c):
    z={}
    for d,a in c.items():
        for e,b in c.items(): z[d*e]=z.get(d*e,Fraction())+a*b
    return {d:v for d,v in z.items() if v}
