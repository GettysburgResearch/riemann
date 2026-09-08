#!/usr/bin/env python3
"""Independent MW full-horizon check by cell integration, not signed work.

No author module is imported. Euler's linear sieve supplies Mobius values;
polynomial-square integration supplies past energy and the entire stable future.
Only the fixed 65536-event source is covered, not later arithmetic events.
"""
from fractions import Fraction as F
from math import factorial, isqrt
import hashlib
import json
from pathlib import Path

BITS=160
S=1<<BITS
NMAX=65536
CHECKPOINTS=(1,2,3,4,8,16,32,64,128,256,512,1024,4096,16384,65536)
C=(F(1),F(-5,2),F(7,4),F(-3,8))

def need(ok,msg):
    if not ok:raise ValueError(msg)

class R:
    __slots__=('l','u')
    def __init__(self,l,u):
        need(type(l) is int and type(u) is int and l<=u,'interval endpoints')
        self.l,self.u=l,u
    @staticmethod
    def val(x):
        if isinstance(x,R):return x
        a=F(x);return R(a.numerator*S//a.denominator,-((-a.numerator*S)//a.denominator))
    def __add__(self,o):
        o=R.val(o);return R(self.l+o.l,self.u+o.u)
    __radd__=__add__
    def __neg__(self):return R(-self.u,-self.l)
    def __sub__(self,o):return self+-R.val(o)
    def __mul__(self,o):
        o=R.val(o);v=(self.l*o.l,self.l*o.u,self.u*o.l,self.u*o.u)
        return R(min(v)//S,-((-max(v))//S))
    __rmul__=__mul__
    def rec(self):return {'lo':str(self.l),'hi':str(self.u),'denominator':str(S)}
    def pos(self):
        need(self.u>=0,'negative upper bound for a nonnegative integral')
        return R(max(0,self.l),self.u)

def log_ratio(n,d):
    need(d>0 and d<=n<=2*d,'log domain')
    z=F(n-d,n+d)
    if not z:return R.val(0)
    # Sum exact rational terms, round once, and retain the full positive tail.
    total=F(0);power=z;j=0
    while True:
        total+=2*power/(2*j+1)
        j+=1;power*=z*z
        tail=2*power/((2*j+1)*(1-z*z))
        if tail < F(1,1<<180):break
    lo=R.val(total);hi=R.val(total+tail)
    return R(lo.l,hi.u)

def invsqrt(n):
    a=isqrt(S*S//n)
    return R(a,a+(a*a*n!=S*S))

def sieve(N):
    least=[0]*(N+1);mu=[0]*(N+1);mu[1]=1;primes=[]
    for n in range(2,N+1):
        if least[n]==0:least[n]=n;primes.append(n);mu[n]=-1
        for p in primes:
            m=n*p
            if m>N:break
            least[m]=p
            if n%p==0:mu[m]=0;break
            mu[m]=-mu[n]
    return mu,primes

def polynomial(x):
    return [sum((C[i]*x[i-j]*F(1,factorial(j)) for i in range(j,4)),R.val(0)) for j in range(4)]

def square_poly(p):
    out=[R.val(0) for _ in range(7)]
    for i in range(4):
        for j in range(4):out[i+j]=out[i+j]+p[i]*p[j]
    return out

def infinite_norm(x):
    p2=square_poly(polynomial(x))
    return sum((v*F(factorial(k),2**(k+1)) for k,v in enumerate(p2)),R.val(0)).pos()

def run():
    mu,primes=sieve(NMAX)
    own_mu_sha=hashlib.sha256(bytes(v+1 for v in mu[1:])).hexdigest()
    root=Path(__file__).resolve().parent
    raw=(root/'evidence/mw-normal.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest()=='ddaa01ec89167f7604939711c548ce80e856eb8197bf34b566e69439883dc9d6','comparison receipt identity')
    source=json.loads(raw);by={r['N']:r for r in source['results']}
    need(own_mu_sha==source['mu_sha256'],'linear-sieve Mobius mismatch')
    x=[R.val(1),R.val(0),R.val(0),R.val(0)];H=R.val(0);rows=[]
    for n in range(1,NMAX+1):
        if n>1:
            delta=log_ratio(n,n-1);ratio=F(n-1,n);powers=[R.val(1)]
            for k in range(1,7):powers.append(powers[-1]*delta)
            moments=[R.val((1-ratio*ratio)/2)]
            for k in range(1,7):
                moments.append((F(k,2)*moments[-1]-F(ratio*ratio,2)*powers[k]).pos())
            p2=square_poly(polynomial(x))
            H=H+sum((a*b for a,b in zip(p2,moments)),R.val(0)).pos()
            x=[ratio*sum((x[j]*powers[i-j]*F(1,factorial(i-j)) for j in range(i+1)),R.val(0)) for i in range(4)]
            x[0]=x[0]+mu[n]*invsqrt(n)
        if n in CHECKPOINTS:
            future=infinite_norm(x);J=H+future
            for field,value in [('J',J),('H_logN',H),('future',future)]:
                old=by[n][field]
                need(value.l<=int(old['hi']) and int(old['lo'])<=value.u,'disjoint independent '+field+' at '+str(n))
            rows.append({'N':n,'J':J.rec(),'H_logN':H.rec(),'future':future.rec()})
    for name,lo,hi in [('J',721,723),('H_logN',718,720),('future',2,3)]:
        v=rows[-1][name]
        need(int(v['lo'])*1000>lo*S and int(v['hi'])*1000<hi*S,'independent final rational bound')
    return {'schema':'riemann-final-review-independent-mw-v1','arithmetic':'160-bit outward dyadics; rational logarithm sums; exact polynomial moments',
            'mobius_algorithm':'Euler linear sieve, independent of original multiple-marking sieve',
            'mu_sha256':own_mu_sha,'integer_events':NMAX,'integrated_interevent_cells':NMAX-1,
            'complete_stable_future_per_checkpoint':True,'checkpoint_count':len(rows),
            'method':'Direct integration of the output polynomial on every time cell plus its entire future. No Lyapunov/work summation is used to compute energy.',
            'author_modules_imported':False,'rh_proved':False,'rows':rows}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2)+'\n',end='')
