#!/usr/bin/env python3
"""Reviewer-written exact/directed controls for pass 3. No research-code imports.

Finite reconstructions are not proofs of the infinite analytic statements.
All accepting arithmetic uses integers/Fraction; decimal strings round outward.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path

BITS = 176
SCALE = 1 << BITS
COUNTS = {}


def need(ok, message, group='contracts'):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    if not ok:
        raise ValueError(message)


def ceildiv(a, b):
    if b <= 0:
        raise ValueError('positive divisor required')
    return -((-a)//b)


class I:
    """Closed interval [lo,hi]/2**BITS; every nonexact operation rounds out."""
    __slots__ = ('lo', 'hi')
    def __init__(self, lo, hi=None):
        if type(lo) is not int or (hi is not None and type(hi) is not int):
            raise TypeError('integer endpoints')
        self.lo, self.hi = lo, lo if hi is None else hi
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    @staticmethod
    def q(x):
        x = F(x)
        return I(x.numerator*SCALE//x.denominator,
                 ceildiv(x.numerator*SCALE, x.denominator))
    def __add__(self, other):
        other = other if isinstance(other, I) else I.q(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I.q(other))
    def __rsub__(self, other):
        return I.q(other) + -self
    def __mul__(self, other):
        other = other if isinstance(other, I) else I.q(other)
        products = [self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi]
        return I(min(products)//SCALE, ceildiv(max(products), SCALE))
    __rmul__ = __mul__
    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError('division through zero')
        if self.hi < 0:
            return -(-self).reciprocal()
        return I(SCALE*SCALE//self.hi, ceildiv(SCALE*SCALE, self.lo))
    def __truediv__(self, other):
        return self * (other if isinstance(other, I) else I.q(other)).reciprocal()
    def __rtruediv__(self, other):
        return I.q(other)*self.reciprocal()
    def sq(self):
        high=max(self.lo*self.lo, self.hi*self.hi)
        low=0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return I(low//SCALE, ceildiv(high,SCALE))
    def __pow__(self, n):
        if type(n) is not int or n < 0:
            raise ValueError('nonnegative integer power')
        a, b = I.q(1), self
        while n:
            if n & 1: a = a*b
            n //= 2
            if n: b=b.sq()
        return a
    def sqrt(self):
        if self.lo < 0:
            raise ValueError('negative square root')
        lo=math.isqrt(self.lo*SCALE); hi=math.isqrt(self.hi*SCALE)
        if hi*hi < self.hi*SCALE: hi += 1
        return I(lo,hi)
    def contains(self, x):
        x=F(x)
        return F(self.lo,SCALE) <= x <= F(self.hi,SCALE)
    def within(self, a, b):
        return F(a) < F(self.lo,SCALE) <= F(self.hi,SCALE) < F(b)
    def mid(self):
        return F(self.lo+self.hi,2*SCALE)
    def data(self, places=18):
        return {'lo':str(self.lo),'hi':str(self.hi),'bits':BITS,
                'decimal_lower':decimal(F(self.lo,SCALE),places,False),
                'decimal_upper':decimal(F(self.hi,SCALE),places,True)}


def decimal(q, places=18, upper=False):
    q=F(q); scale=10**places
    n=ceildiv(q.numerator*scale,q.denominator) if upper else q.numerator*scale//q.denominator
    return ('-' if n<0 else '')+str(abs(n)//scale)+'.'+str(abs(n)%scale).zfill(places)


@lru_cache(None)
def logq(q):
    """Positive rational log: power-of-two reduction, positive atanh with explicit tail."""
    q=F(q)
    if q <= 0: raise ValueError('positive log argument')
    if q < 1: return -logq(1/q)
    k=0
    while q >= 2:
        q /= 2; k += 1
    def unit(y):
        z=(F(y)-1)/(F(y)+1); z2=z*z; term=z; total=F(0)
        n=72
        for j in range(n):
            total += 2*term/(2*j+1); term *= z2
        rem=2*term/((2*n+1)*(1-z2))
        return I(total.numerator*SCALE//total.denominator,
                 ceildiv((total+rem).numerator*SCALE,(total+rem).denominator))
    return unit(q)+k*unit(F(2))


@lru_cache(None)
def pi_interval():
    def atan_inv(n):
        x=F(1,n); total=F(0); t=x
        for j in range(96):
            total += (-1)**j*t/(2*j+1); t *= x*x
        other=total+t/193
        return I(min(total,other).numerator*SCALE//min(total,other).denominator,
                 ceildiv(max(total,other).numerator*SCALE,max(total,other).denominator))
    return 16*atan_inv(5)-4*atan_inv(239)


@lru_cache(None)
def factors(n):
    if type(n) is not int or n<1: raise ValueError('positive integer')
    out=[]; p=2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e+=1
        if e: out.append((p,e))
        p+=1
    if n>1: out.append((n,1))
    return tuple(out)


def mu(n):
    fs=factors(n)
    return 0 if any(e>1 for p,e in fs) else (-1)**len(fs)


def phi(n):
    v=n
    for p,e in factors(n): v=v//p*(p-1)
    return v


def j2(n):
    v=n*n
    for p,e in factors(n): v=v//(p*p)*(p*p-1)
    return v


def solve(A, b):
    """Rational elimination; proposals produced without floating point."""
    n=len(b); M=[[F(v) for v in row]+[F(rhs)] for row,rhs in zip(A,b)]
    need(len(M)==n and all(len(r)==n+1 for r in M),'solve dimension')
    for j in range(n):
        pivot=next((i for i in range(j,n) if M[i][j]),None)
        need(pivot is not None,'singular rational solve')
        M[j],M[pivot]=M[pivot],M[j]
        for i in range(j+1,n):
            if M[i][j]:
                q=M[i][j]/M[j][j]; M[i][j]=F(0)
                for k in range(j+1,n+1): M[i][k]-=q*M[j][k]
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(M[j][-1]-sum((M[j][k]*x[k] for k in range(j+1,n)),F(0)))/M[j][j]
    need(all(sum((F(v)*w for v,w in zip(row,x)),F(0))==rhs for row,rhs in zip(A,b)), 'rational solve residual')
    return x


def ldl_pivots(A):
    n=len(A); M=[[F(v) for v in row] for row in A]; out=[]
    need(all(M[i][j]==M[j][i] for i in range(n) for j in range(n)),'symmetric LDL')
    for j in range(n):
        d=M[j][j]; need(d>0,'positive LDL pivot');out.append(d)
        for i in range(j+1,n):
            for k in range(i,n):
                M[i][k]=M[k][i]=M[i][k]-M[i][j]*M[k][j]/d
    return out


def interval_contracts():
    n=0
    for a in (F(-7,3),F(-1,7),F(0),F(2,9),F(13,2)):
        for b in (F(-11,4),F(-1,11),F(0),F(3,8),F(9,2)):
            x,y=I.q(a),I.q(b)
            need((x+y).contains(a+b),'addition containment','interval');n+=1
            need((x*y).contains(a*b),'multiplication containment','interval');n+=1
            if b:
                need((x/y).contains(a/b),'division containment','interval');n+=1
            need(x.sq().contains(a*a),'square containment','interval');n+=1
    for x in (I(-3,4),I(0),I(-1,1)):
        try: x.reciprocal()
        except ValueError: pass
        else: raise ValueError('zero division accepted')
        need(True,'zero rejection','interval')
    need(logq(2).within('0.6931471805599453094','0.6931471805599453095'),'log2','interval')
    need(pi_interval().within('3.1415926535897932384','3.1415926535897932385'),'pi','interval')
    need(I.q(2).sqrt().sq().contains(2),'sqrt square','interval')
    return {'exact_containment_comparisons':n,'bits':BITS}


def ant_limit():
    """Complete ANT5 constant: all 4095 cells, no midpoint-only acceptance."""
    T=4096; H=[I.q(0)]
    for n in range(1,T+1): H.append(H[-1]+I.q(F(1,n*n)))
    d=(1,-5,8,-4); total=I.q(0)
    for r in range(1,T):
        A=I.q(0); B=F(0)
        for j,c in enumerate(d):
            u=r//(1<<j); l=r//(1<<(j+1))
            A+= (H[u]-H[l])*F(c,2*(4**j))
            B+=c*(2*l-F(u,2))
        cell=A.sq()*F(3*r*r+3*r+1,3)+2*A*B+I.q(B*B/F(r*(r+1)))
        # Cancellation in the expression can produce a tiny negative interval lower endpoint;
        # its exact integral is nonnegative, so intersect with [0,infinity).
        need(cell.hi>=0,'cell integral sign','ant_cells')
        total+=I(max(0,cell.lo),cell.hi)
    tail=I.q(F(10000,3*T**3)); result=I(total.lo,total.hi+tail.hi)
    need(result.within('1.704219450036','1.704219498544'),'ANT complete enclosure','ant')
    # Exact null-direction coefficients, all-power graph and full physical lower interval.
    for Y in range(2,33):
        c={ (1<<j)*n:F(d[j]*n,Y) for j in range(4) for n in range(Y,2*Y)}
        need(sum(c.values(),F(0))==0,'ANT centering','ant')
        need(sum((a/n for n,a in c.items()),F(0))==0,'ANT balance','ant')
        # Formal prime-log coordinates establish the second jet, not a decimal near zero.
        jets={p:F(0) for n in c for p,e in factors(n)}
        for n,a in c.items():
            for p,e in factors(n): jets[p]+=a*e/n
        need(not any(jets.values()),'ANT derivative jet','ant')
        S=sum((a*a/n for n,a in c.items()),F(0))
        need(S==F(63,2)*F(3*Y-1,2*Y),'ANT diagonal','ant')
        lower=F(0)
        for r in range((3*Y+1)//2,2*Y):
            val=sum((a*(r//n) for n,a in c.items()),F(0))
            lower+=val*val/F(r*(r+1))
        # The manuscript proof handles the half-integer endpoint continuously;
        # the complete cells form a slightly shorter independent lower check.
        need(lower>0,'nonzero actual residual interval','ant')
    return {'cells':T-1,'tail_upper':tail.data(),'constant':result.data(),
            'acceptance':'published open decimal interval strictly contains this closed enclosure',
            'null_directions_checked':31}


def capacity():
    primes=(2,3,5,7,11,13); panels={}
    for mode in ('squarefree','geometric'):
        subsets=[]
        for mask in range(1,1<<len(primes)):
            weight=F(1); rate=I.q(0)
            for i,p in enumerate(primes):
                if mask>>i&1:
                    weight*=F(1,p if mode=='squarefree' else p-1)
                    rate+=logq(p)*(F(p+1,p) if mode=='squarefree' else F(p,p-1))
            subsets.append((weight,rate))
        G=sum((I.q(w)/a for w,a in subsets),I.q(0))
        expected={'squarefree':('1.185322859710','1.185322859712','1.915941534725','1.915941534729'),
                  'geometric':('1.822501191776','1.822501191780','2.372217088315','2.372217088320')}[mode]
        need(G.within(*expected[:2]),'capacity root contrast','capacity')
        # Monotone directed secular signs enclose root independently.
        lo=F(expected[2]);hi=F(expected[3])
        def sec(c):return sum((I.q(w)/(a*c-1) for w,a in subsets),I.q(-1))
        need(sec(lo).lo>0 and sec(hi).hi<0,'secular bracket','capacity')
        for step in range(72):
            m=(lo+hi)/2; s=sec(m)
            if s.lo>0:lo=m
            elif s.hi<0:hi=m
            else:break
        need(sec(lo).lo>0 and sec(hi).hi<0,'refined secular signs','capacity')
        A=I(I.q(lo).lo,I.q(hi).hi)
        V=sum((I.q(w)/(a*A-1).sq() for w,a in subsets),I.q(0))
        panels[mode]={'modes':len(subsets),'root_contrast':G.data(),
                      'anchored_constant':A.data(),'slow_weight':(1/(1+V)).data()}
    # Rational-rate product chain: independently solve killed generator Poisson equation.
    ps=(2,3,5); states=list(itertools.product((0,1),repeat=3)); n=len(states)
    Z=math.prod((F(p+1,p) for p in ps),start=F(1))
    prob=[math.prod((F(1,p) if x else F(1) for p,x in zip(ps,s)),start=F(1))/Z for s in states]
    L=[[F(0)]*n for _ in states]
    for i,s in enumerate(states):
        for j,t in enumerate(states):
            changed=[k for k in range(3) if s[k]!=t[k]]
            if len(changed)==1:
                k=changed[0];rate=F(1) if s[k] else F(1,ps[k])
                L[i][j]=-rate;L[i][i]+=rate
    u=solve([row[1:] for row in L[1:]],[F(1)]*(n-1))
    mean=sum((prob[i+1]*u[i] for i in range(n-1)),F(0))
    g=F(0)
    for mask in range(1,8):
        w=math.prod((F(1,p) for i,p in enumerate(ps) if mask>>i&1),start=F(1))
        a=sum((F(p+1,p) for i,p in enumerate(ps) if mask>>i&1),F(0))
        g+=w/a
    need(mean==g,'root lifetime equals root contrast','capacity')
    return {'six_prime_panels':panels,'rational_killed_chain_states':n,
            'stationary_mean_lifetime':str(mean),'independent_root_contrast':str(g)}


def work():
    A=[[-1,0,0,0],[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]]
    C=[F(1),F(-5,2),F(7,4),F(-3,8)]
    Q=[[F(v,2048) for v in row] for row in
       [[385,-639,324,-54],[-639,3518,-2882,660],[324,-2882,2536,-600],[-54,660,-600,144]]]
    for i in range(4):
        for j in range(4):
            need(sum((A[k][i]*Q[k][j]+Q[i][k]*A[k][j] for k in range(4)),F(0))==-C[i]*C[j],
                 'Lyapunov identity','work')
    piv=ldl_pivots(Q)
    need(piv==list(map(F,['385/2048','946109/788480','6400405/484407808','6561/3277007360'])), 'work pivots','work')
    def R(r):
        v=logq(r)
        return (385-639*v+162*v.sq()-9*v**3)/(2048*I.q(r))
    W3= -I.q(2).sqrt()*R(2)-2/I.q(3).sqrt()*R(3)+2/I.q(6).sqrt()*R(F(3,2))
    need(W3.lo>SCALE//20,'actual W3 positive work','work')
    # Coherent source energy: entirely independent finite integral/floor identity.
    for N in range(1,65):
        m=[0];
        for k in range(1,N+1):m.append(m[-1]+mu(k))
        J=sum((F(m[k]**2,k*(k+1)) for k in range(1,N)),F(0))+F(m[N]**2,N)
        pair=sum((F(mu(i)*mu(j),max(i,j)) for i in range(1,N+1) for j in range(1,N+1)),F(0))
        inc=sum((F(2*mu(k)*m[k-1]+mu(k)**2,k) for k in range(1,N+1)),F(0))
        need(J==pair==inc,'coherent norm and signed work','work')
    return {'pivots':[str(x) for x in piv],'actual_W3':W3.data(),
            'coherent_full_tail_cutoffs':64}


def arithmetic():
    # Solve the balanced-detail optimizer in direct rational coordinates independently.
    opts={}
    for M in (3,4,8,16,32):
        odds=list(range(1,M+1,2)); n=len(odds)
        R=[[F(math.gcd(i,j)**2,i*i*j*j) for j in odds] for i in odds]
        u=[F(1,k) for k in odds]; e=[F(int(k==1)) for k in odds]
        K=[row+[e[i],u[i]] for i,row in enumerate(R)]+[e+[F(0),F(0)],u+[F(0),F(0)]]
        sol=solve(K,[F(0)]*n+[F(1),F(0)])[:n]
        S=sum((F(mu(d)**2,j2(d)) for d in odds),F(0))
        a=sum((F(mu(d)*phi(d),j2(d)) for d in odds),F(0))
        D=sum((F(phi(d)**2,j2(d)) for d in odds),F(0)); det=S*D-a*a
        for k,x in zip(odds,sol):
            v=k*k*sum((F(mu(d//k)*mu(d),j2(d)) for d in odds if d%k==0),F(0))
            w=k*k*sum((F(mu(d//k)*phi(d),j2(d)) for d in odds if d%k==0),F(0))
            need(x==(D*v-a*w)/det,'balanced KKT coefficient','arithmetic')
        opts[str(M)]={'coefficients':{str(k):str(x) for k,x in zip(odds,sol)}}
    need(opts['16']['coefficients']['9']=='-20880/57769','nonsquarefree constrained coefficient','arithmetic')
    # Vasyunin support obstruction, including overlapping prime-2 exception.
    for q in range(2,33):
        f={}
        for d in range(1,q+1):
            if q%d:continue
            a=mu(q//d)
            if d>1:f[d-1]=f.get(d-1,0)+a*d*(d-1)
            f[d]=f.get(d,0)-a*d*(d+1)
        for k in range(2,33):
            val=sum((F(v*(j%k),j*(j+1)*k) for j,v in f.items()),F(0))
            need(val==int(k==q),'finite dual identity','arithmetic')
        need(sum((F(v,j*(j+1)) for j,v in f.items()),F(0))==-mu(q),'target dual','arithmetic')
        norm=sum((F(v*v,j*(j+1)) for j,v in f.items()),F(0))
        if q==2:need(norm==14,'prime 2 overlap','arithmetic')
        if q==5:need(norm==52,'missing 5 gap','arithmetic')
    # Terminal source, full continuation and short-source balanced hyperbola identity.
    def Q(x):
        x=F(x)
        return sum((F(mu(k))*(1-x/k) for k in range(1,int(x)+1,2)),F(0))
    def W(z):
        z=F(z)
        return sum((z/k-1 for k in range(1,int(z)+1,2)),F(0))
    for Y in range(3,32,2):
        odds=list(range(1,Y+1,2)); mo=sum((F(mu(k),k) for k in odds),F(0))
        lam={k:F(mu(k))-(Y*mo if k==Y else 0) for k in odds}
        need(sum((x/k for k,x in lam.items()),F(0))==0,'terminal balance','arithmetic')
        B=sum((a*b*W(F(Y*Y,k*l)) for k,a in lam.items() for l,b in lam.items()),F(0))
        need(B==Q(Y*Y)-2*Q(Y),'balanced hyperbola','arithmetic')
        for n in range(1,4*Y):
            direct=sum((a*(n//k-n//(2*k)) for k,a in lam.items()),F(0))
            continuation=1+(n//Y-n//(2*Y))*Q(Y)-sum((sum(mu(k) for k in range(1,n//j+1,2)) for j in range(1,n//Y+1,2)))
            need(direct==continuation,'terminal complete continuation','arithmetic')
            if n<Y:need(direct==1,'terminal native horizon','arithmetic')
    for L in (1,2,3,7):
        Y=200*L+1
        for sign in (1,-1):
            bands=(110,130) if sign==1 else (150,180)
            c={k:F(s*k,Y) for h,s in zip(bands,(1,-1)) for k in (h*L+2*r+1 for r in range(L))}
            need(sum((a/k for k,a in c.items()),F(0))==0,'hostile balanced source','arithmetic')
            B=sum((a*b*W(F(Y*Y,k*l)) for k,a in c.items() for l,b in c.items()),F(0))
            target=F(L*L,3)-F(12721*L**4,Y*Y) if sign==1 else -F(900*L**4,Y*Y)
            need(B==target and sign*B>0,'hostile exact quadratic sign','arithmetic')
    return {'balanced_optimizers':opts,'dual_indices':31,'terminal_cutoffs':15,
            'hostile_source_panels':8,'norm_wording':'BL26 equation (6.3) is squared norm Omega(sqrt(M)), norm Omega(M**(1/4))'}


def annular():
    # Elementary Euler-constant interval; no stored transcendental value.
    N=4096
    harmonic=sum((I.q(F(1,k)) for k in range(1,N+1)),I.q(0))
    hlog=harmonic-logq(N)
    gamma=I((hlog-I.q(F(1,2*N))).lo,
            (hlog-I.q(F(1,2*(N+1)))).hi)
    pi=pi_interval()
    # log(pi) via rational endpoint enclosure, then monotonicity.
    lp=I(logq(F(pi.lo,SCALE)).lo,logq(F(pi.hi,SCALE)).hi)
    C0=F(47,64)-F(21,64)*(gamma+lp)+F(115,96)*logq(2)-F(641,1728)*logq(3)-F(65,192)*logq(5)
    need(C0.within('0.04','0.0474'),'annular C0 bound','annular')
    H=3*10**12
    logHpi=logq(H)-logq(2)-lp
    R=(logHpi+1)/(2*pi*H)+(40*logq(H+2)+10)/(H*H)
    need(R.hi<I.q(F(37,25*10**12)).lo,'height-to-tail bound','annular')
    # Concavity in m of the elementary lower comparison lets endpoints suffice.
    def lower(m):
        return F(1,4)-F(237,5000)-F(205,128*m**5)-F(85,64)*F(37,25*10**12)*(m+2+F(1,m))
    for bound,threshold in ((5*10**10,F(1,10)),(10**11,F(1,200))):
        need(min(lower(2),lower(bound))>threshold,'continuum comparison endpoints','annular')
    ds=[]
    for m in range(2,33):
        B=I.q(0)
        for n in range(m*m//4+1,4*m*m+1):
            fs=factors(n)
            if len(fs)!=1:continue
            a=64*n-F(m**6,n*n) if n<=m*m else F(64*m**6,n*n)-n
            need(a>=0,'annular rational weights','annular')
            B+=a*logq(fs[0][0])
        D=B/(192*m**3)-F(45*m,128)+F(1,4)
        need(D.lo>I.q(F(1,10)).hi,'actual finite annular values','annular')
        ds.append(D.data())
    # EF convex budget constants, and CR triple-jet Laurent coefficient check.
    a=2+I.q(2).sqrt()
    need(((a+a.sq())/2).hi<8*SCALE,'complete nonlinear jump budget','annular')
    # Formal truncated products: zeta=1/t+g+u*t; p=a+b*t+c*t^2/2.
    def mul(x,y):
        out={}
        for i,v in x.items():
            for j,w in y.items():out[i+j]=out.get(i+j,F(0))+v*w
        return out
    for a0,b,c,g,u in ((F(2,3),F(-1,2),F(5,7),F(3,5),F(4,9)),
                       (F(0),F(1),F(2),F(0),F(-3)),(F(0),F(4,3),F(7),F(1),F(2))):
        z={-1:F(1),0:g,1:u};zp={-2:F(-1),0:u};p={0:a0,1:b,2:c/2}
        L=mul(mul(z,zp),mul(p,p))
        for e,v in mul(zp,p).items():L[e]=L.get(e,F(0))-2*v
        need(L.get(-3,0)==-a0*a0,'triple residue cubic coefficient','annular')
        need(L.get(-2,0)==2*a0-2*a0*b-g*a0*a0,'triple residue quadratic coefficient','annular')
        need(L.get(-1,0)==2*b-b*b-a0*c-2*g*a0*b,'triple residue linear coefficient','annular')
    return {'C0':C0.data(),'external_height_assumed':H,'zero_tail_bound':R.data(),
            'actual_finite_m_range':[2,32],'D_values':ds,
            'continuum_scope':'elementary scalar budget only; external zero census not replayed'}


def strict_json(text):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    def bad(x):raise ValueError('nonfinite JSON')
    return json.loads(text,object_pairs_hook=pairs,parse_constant=bad)


def verify_receipt(result, text):
    # Canonical serialization, rather than Python ==, keeps bool/int/float distinct.
    actual=json.dumps(strict_json(text),sort_keys=True,separators=(',',':'))
    expected=json.dumps(result,sort_keys=True,separators=(',',':'))
    if actual != expected:
        raise ValueError('receipt differs from complete reconstruction')


GROUPS={'interval':interval_contracts,'ant':ant_limit,'capacity':capacity,'work':work,'arithmetic':arithmetic,'annular':annular}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group',choices=tuple(GROUPS)+('all',),default='all')
    parser.add_argument('--verify-receipt',type=Path)
    args=parser.parse_args()
    names=tuple(GROUPS) if args.group=='all' else (args.group,)
    data={name:GROUPS[name]() for name in names}
    result={'schema':'riemann.review.pass3.controls.v1','marker':'PASS_BOUNDED_REVIEWER_RECONSTRUCTION',
            'groups':data,'assertions':COUNTS,'bits':BITS,'author_research_code_executed':False,
            'whole_repository_checked':False,'fresh_lean_build':False,'rh_proved':False}
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.verify_receipt:
        verify_receipt(result,args.verify_receipt.read_text(encoding='utf-8'))
    print(text,end='')


if __name__=='__main__':main()
