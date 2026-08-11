#!/usr/bin/env python3
from fractions import Fraction
import json
import sys

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=toQ(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-toQ(o))
    def __rsub__(self,o): return toQ(o)-self
    def __mul__(self,o):
        o=toQ(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=toQ(o); den=o.a*o.a-2*o.b*o.b
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=toQ(o); return self.a==o.a and self.b==o.b

def toQ(x): return x if isinstance(x,Q2) else Q2(x,0)

def mul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return out

def evalp(p,x):
    x=Fraction(x); s=Fraction(0); pw=Fraction(1)
    for a in p: s+=a*pw; pw*=x
    return s

Q=[Fraction(2),Fraction(-15),Fraction(35),Fraction(-30),Fraction(8)]
assert Q==mul(mul([1,-1],[1,-2]),mul([2,-1],[1,-4]))
for root in [Fraction(1),Fraction(2),Fraction(1,2),Fraction(1,4)]:
    assert evalp(Q,root)==0

band=[]
for R in range(4):
    A=sum(Q[r]*2**(r+1) for r in range(R+1))
    B=-sum(Q[r] for r in range(R+1))
    band.append((A,B))
assert band==[(4,-2),(-56,13),(224,-22),(-256,8)]
assert sum(Q)==0 and sum(Q[r]*2**r for r in range(5))==0

K=64
coef=[Fraction(1)]+[Fraction(0)]*K
for c,mult in [(Fraction(1),2),(Fraction(2),1),(Fraction(1,2),1),(Fraction(4),1)]:
    for _ in range(mult):
        geom=[c**k for k in range(K+1)]
        nxt=[Fraction(0)]*(K+1)
        for i,a in enumerate(coef):
            if a:
                for j in range(K+1-i): nxt[i+j]+=a*geom[j]
        coef=nxt
assert all(x>0 for x in coef)

for k in range(1,K+1):
    assert Fraction(2)+2**k+Fraction(1,2**k)+4**k>0

Qprime=[-r*Q[r] for r in range(5)]
assert Qprime==[0,15,-70,90,-32]

def invsqrt2pow(r):
    if r%2==0: return Q2(Fraction(1,2**(r//2)),0)
    return Q2(0,Fraction(1,2**((r+1)//2)))

A=[toQ(Q[r])*invsqrt2pow(r) for r in range(5)]
assert A[0]==2 and A[2]==Fraction(35,2) and A[4]==2
assert A[1]==Q2(0,Fraction(-15,2)) and A[3]==Q2(0,Fraction(-15,2))

p=[Q2(1),Q2(0,Fraction(-3,4)),Q2(Fraction(1,4))]
corr={lag:Q2(0) for lag in range(-2,3)}
for i,ai in enumerate(p):
    for j,aj in enumerate(p): corr[i-j]=corr[i-j]+8*ai*aj
for r,a in enumerate(A): assert corr[r-2]==a

assert 43*43 > 8*15*15

result={
    "classification":"PASS_X_90423_PHASE_LOCKED_FACTOR16",
    "polynomial_factorizations":1,
    "root_checks":4,
    "annular_band_checks":5,
    "positive_inverse_coefficients":K+1,
    "positive_generalized_prime_coefficients":K,
    "current_gauge_coefficients":len(Qprime),
    "fejer_riesz_laurent_coefficients":5,
    "coercivity_checks":2,
    "deterministic_rh_proved":False,
    "scope":"exact polynomial/source/phase-lock/scale-frame algebra only"
}
path=None
if "--json" in sys.argv:
    path=sys.argv[sys.argv.index("--json")+1]
text=json.dumps(result,indent=2,sort_keys=True)+"\n"
if path:
    open(path,"w").write(text)
else:
    print(text,end="")