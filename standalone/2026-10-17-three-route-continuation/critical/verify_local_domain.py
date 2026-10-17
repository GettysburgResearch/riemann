#!/usr/bin/env python3
"""Exact algebra audit of all local branch types and their common period.

Variables: (q,D,P,V,Phi,alpha,tau1,tau2,tau3,tau4), q=sqrt(Q).
The Laurent ring imposes alpha^6=1, gamma*Phi*tau1=-q and
 tau1*tau5=q^2. It retains every other phase symbol literally.
The written proof supplies the complete infinite support enumeration.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

COUNT=0

def require(condition, message):
    global COUNT
    COUNT+=1
    if not condition:
        raise ValueError(message)

class Poly:
    def __init__(self, terms=None):
        if isinstance(terms,(int,F)):
            terms={(0,)*10:F(terms)}
        out={}
        for e,c in (terms or {}).items():
            e=list(e);e[5]%=6;e=tuple(e)
            out[e]=out.get(e,F(0))+F(c)
        self.t={e:c for e,c in out.items() if c}
    @staticmethod
    def cast(x): return x if isinstance(x,Poly) else Poly(x)
    def __add__(self,other):
        other=self.cast(other); out=self.t.copy()
        for e,c in other.t.items():out[e]=out.get(e,F(0))+c
        return Poly(out)
    __radd__=__add__
    def __neg__(self): return Poly({e:-c for e,c in self.t.items()})
    def __sub__(self,o): return self+-self.cast(o)
    def __rsub__(self,o): return self.cast(o)+-self
    def __mul__(self,o):
        o=self.cast(o);out={}
        for e,c in self.t.items():
            for f,d in o.t.items():
                g=tuple(x+y for x,y in zip(e,f))
                out[g]=out.get(g,F(0))+c*d
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:
            if len(self.t)!=1:raise ValueError('negative power of non-monomial')
            e,c=next(iter(self.t.items()))
            return Poly({tuple(n*x for x in e):c**n})
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,o):return self.t==self.cast(o).t

def variable(i):
    e=[0]*10;e[i]=1
    return Poly({tuple(e):F(1)})
q,D,P,V,Phi,alpha,t1,t2,t3,t4=(variable(i) for i in range(10))
Q=q**2;r=q**-2
gamma=-q*Phi**-1*t1**-1
tau=[Poly(-1),t1,t2,t3,t4,Q*t1**-1]
A=Phi**6*Q**4*D**6;E=A*V
W=alpha*P;D1=alpha**-1*D
require(alpha**6==1,'sixth-order unit phase')
require(gamma*Phi*t1==-q,'principal target normalization')
require(t1*tau[5]==Q,'Gauss complementary product')
require(D1*W==D*P,'row-independent leading mixed term')

def C(t,k,J):
    if t==0:
        return Poly(1 if k==0 or J==0 else 0)
    if k==0:
        if J<t-1:return Poly(0)
        T=tau[t%6] if J==t-1 else (Q-1 if t%6==0 else Poly(0))
        return Q**(t-1)*T
    if k==1:
        if J<t:return Poly(0)
        T=tau[(t-1)%6] if J==t else (Q-1 if (t-1)%6==0 else Poly(0))
        return t1*Q**(t-1)*T
    return Poly(0)

def coefficient(e,l,k,m,j):
    t=e+3*l;J=j+6*m
    return gamma**e*Phi**t*alpha**(k-t)*C(t,k,J)*q**(-e)*D**e*Q**(-l)*D**(3*l)*P**k*V**m

B2=Phi**3*alpha**3*t3*Q*D**3
B30=gamma*Phi**4*alpha**2*t4*q**3*D**4
B31=Phi**3*alpha**4*t1*t2*Q*D**3*P
B4=gamma*Phi**4*alpha**3*t1*t3*q**3*D**4*P
T={1:D*P,2:B2,3:B30+B31,4:B4,5:-r*A}
branches=[
 ('k0-boundary-j0',1,0,0,0,0,-D1),
 ('k0-boundary-j2',0,1,0,0,2,B2),
 ('k0-boundary-j3',1,1,0,0,3,B30),
 ('k0-boundary-j5',0,2,0,0,5,-r*A),
 ('k1-boundary-j0',0,2,1,1,0,E*W),
 ('k1-boundary-j1',1,0,1,0,1,D*P),
 ('k1-boundary-j3',0,1,1,0,3,B31),
 ('k1-boundary-j4',1,1,1,0,4,B4),
]
for j in range(6):
    branches.append((f'k0-interior-j{j}',0,2,0,1,j,(1-r)*E))
    delta=1 if j<=1 else 0
    branches.append((f'k1-interior-j{j}',1,0,1,delta,j,-(Q-1)*D*P*V**delta))
for name,e,l,k,m,j,expected in branches:
    first=coefficient(e,l,k,m,j)
    require(first==expected,name+' exact first term')
    require(coefficient(e,l+2,k,m+1,j)==E*first,name+' common period')
# The exponent increment is independent of the starting t and J:
# C contributes Q^6, the l weight contributes Q^-2 D^6,
# angular and row phases contribute Phi^6 alpha^-6, and m contributes V.
require(Q**6*Q**-2*D**6*Phi**6*alpha**-6*V==E,'universal period exponent identity')

for j in range(6):
    require(coefficient(0,0,0,0,j)==1,f'baseline j{j}')
    require(coefficient(0,0,0,1,j)==V,f'baseline geometric ratio j{j}')
    require(coefficient(0,0,1,0,j)==(W if j==0 else 0),f't0 positive k j{j}')
    require(coefficient(0,0,2,0,j)==(W**2 if j==0 else 0),f't0 k-tail j{j}')

# Every possible residue type and representative valuation comparison is checked.
# The written source formulas make the same zero/nonzero rule periodic in t,J.
for e in (0,1):
    for l in range(5):
        t=e+3*l
        if t==0:continue
        for j in range(6):
            for m in range(5):
                J=j+6*m
                for k in range(4):
                    allowed=(k==0 and ((J==t-1) or (J>=t and t%6==0))) or (k==1 and ((J==t) or (J>t and (t-1)%6==0)))
                    require((C(t,k,J)!=0)==allowed,f'support e{e} l{l} j{j} m{m} k{k}')

# Assemble the exact infinite branch sums after clearing their geometric denominators.
for j in range(1,6):
    delta=1 if j==1 else 0
    assembled=(1-E)+(1-r)*E-(Q-1)*D*P*V**delta+(1-V)*T[j]
    proposed=1-r*E-(Q-1)*D*P*V**delta+(1-V)*T[j]
    require(assembled==proposed,f'bad H numerator j{j}')
    if j==1:
        require(proposed==1-r*E+(1-Q*V)*D*P,'j1 simplification')
# Good factor, common denominator (1-E)(1-V)(1-W) for F_0.
assembled=(1-E)*(1-W)+W*(1-E)*(1-V)+(1-r)*E*(1-W)+E*W*(1-V)*(1-W)-D1*(1-V)*(1-W)-(Q-1)*D*P*V*(1-W)
source=(1-V*W)*(1-E)+E*(1-W)*((1-r)+W*(1-V))-D1*(1-W)*((1-V)+(Q-1)*W*V)
require(assembled==source,'good local factor from all branches')
require((1-D1*W)*(1-D1+D1*W)-(1-D1)==D1**2*W*(1-W),'extracted leading Euler cancellation')
# Negative controls: dropping the unit mask would erase these boundary terms;
# dropping the common bad-prime term would erase the stated transverse cost.
require(coefficient(1,0,1,0,1)!=0,'masked tau0 boundary survives at j1')
require(coefficient(0,2,0,0,5)!=0,'masked tau0 boundary survives at j5')
require(coefficient(1,0,1,0,2)==-(Q-1)*D*P,'common bad-prime term survives at j2')
require(coefficient(1,0,1,0,2)!=0,'common bad-prime term cannot be dropped')

print(json.dumps({'status':'PASS','exact_checks':COUNT,
    'proof_sha256':sha256(Path(__file__).with_name('LOCAL_DOMAIN.md').read_bytes()).hexdigest(),
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'coverage':['all 20 surviving boundary/interior branch first terms','their common period and universal exponent identity','all j=0,...,5 assembled numerators','finite support representatives','three native negative controls'],
    'not_verified':['metaplectic foundation','global Poisson identity','future contour comparison']},indent=2))
