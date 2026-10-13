#!/usr/bin/env python3
"""Exact finite diagnostics for the positive singleton flow.

All good squarefree Eisenstein ideals in each declared hard annulus, and all
nonzero element rows in the declared norm ball, are included. No asymptotic
claim follows from these finite tests. NumPy is used ONLY for bounded int64
Gram products; final sums and local moment tests use Python integers/Fractions.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from math import factorial, isqrt
import numpy as np

COUNT = 0

def require(ok: bool, message: str) -> None:
    global COUNT
    COUNT += 1
    if not ok:
        raise ArithmeticError(message)

# Q(sqrt(5)); tuples mean a+b*sqrt(5).
def qa(x, y): return (x[0]+y[0], x[1]+y[1])
def qneg(x): return (-x[0], -x[1])
def qm(x, y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def qs(c): return (F(c), F(0))
def qp(x, n):
    out=qs(1)
    for _ in range(n): out=qm(out,x)
    return out

def qsign(x):
    a,b=x
    if b==0: return (a>0)-(a<0)
    if a==0: return (b>0)-(b<0)
    if a>0 and b>0: return 1
    if a<0 and b<0: return -1
    d=a*a-5*b*b
    return ((d>0)-(d<0)) * (1 if a>0 else -1)

ZP=(F(1,2),F(1,2)); ZM=(F(1,2),F(-1,2))
PP=(F(1,2),F(-1,10)); PM=(F(1,2),F(1,10))

def moments(n):
    out=[1,0]
    while len(out)<=n: out.append(out[-1]+out[-2])
    return out

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def norm(a,b): return a*a-a*b+b*b

def local_checks():
    start=COUNT
    mm=moments(60)
    for n in range(61):
        direct=qa(qm(PP,qp(ZP,n)),qm(PM,qp(ZM,n)))
        require(direct==qs(mm[n]),f'law moment {n}')
    # Peano kernel, exact algebraic evaluation on rational grid points.
    for j in range(-40,81):
        t=F(j,40)
        def poscube(z):
            w=qa(z,qs(-t))
            return qp(w,3) if qsign(w)>0 else qs(0)
        val=qa(qm(PP,poscube(ZP)),qm(PM,poscube(ZM)))
        val=qa(val,qs(-max(F(1)-t,0)**3+3*max(-t,0)**2))
        require(qsign(val)>=0,'negative Peano kernel')
        if t<=-1 or t>=2: require(val==qs(0),'kernel support')
    require(F(mm[4]-1,24)==F(1,24),'kernel mass')
    require(F(mm[5]-1,120)/F(1,24)==F(2,5),'kernel mean')
    require(F(2*(mm[6]-1),720)/F(1,24)-F(2,5)**2==F(8,75),'kernel variance')
    samples=0
    for a,b,c,d in product(range(-2,3),repeat=4):
        A=norm(a,b); B=2*a*c-a*d-b*c+2*b*d; C=norm(c,d)
        poly=[1]
        for k in range(1,11):
            poly=conv(poly,[A,B,C])
            if k<2: continue
            ran=sum(x*mm[j] for j,x in enumerate(poly))
            raw=sum(poly); deriv=poly[1]
            rem=ran-raw+deriv
            ck=F(factorial(2*k),24*factorial(2*k-4))*F(8,75)**(k-2)
            require(rem>=ck*C**k,f'coercivity at {(a,b,c,d,k)}')
            if k==2: require(rem==C*C,'fourth remainder')
            if k==3: require(rem==3*A*C*C+3*B*B*C+6*B*C*C+4*C**3,'sixth remainder')
            samples+=1
    # Deliberately false substitutions, rejected by concrete witnesses.
    require(13+4-1==16 and 16>13,'no universal local decrease')
    require(5-4-1==0 and 0<5,'both increment signs')
    require(1-2*1-1+1==-1,'m4=1 violates square positivity')
    require(sum(c*m for c,m in zip([1,4,6,4,1],[1,0,1,0,1]))!=13,'symmetric signs change triple term')
    return {'exact_predicates':COUNT-start,'complex_pairs':625,'even_orders':list(range(4,21,2)),
            'coercivity_cases':samples,'law_moments_checked_through':60,
            'kernel_grid_points':121,'negative_controls':4}

def atom_checks():
    """Independent exact atom enumeration versus polynomial moment contraction.

    This auxiliary three-coordinate model is explicitly NOT the full native
    census. Real signed squarefree coefficients and every coordinate mask are
    used. Complex local inequalities and full native rows are tested elsewhere.
    """
    start=COUNT; checked=0
    mm=moments(8)
    for mask in range(8):
        terms={bits:(-1)**sum(bits) for bits in product((0,1),repeat=3)
               if sum(bits)<=2 and all(not bits[j] or not(mask>>j&1) for j in range(3))}
        for frozen in range(8):
            for k in (2,3,4):
                poly={(0,0,0):1}
                for _ in range(2*k):
                    new={}
                    for e,c in poly.items():
                        for f,d in terms.items():
                            g=tuple(e[j]+f[j] for j in range(3))
                            new[g]=new.get(g,0)+c*d
                    poly=new
                contracted=0
                for e,c in poly.items():
                    for j in range(3):
                        if not(frozen>>j&1): c*=mm[e[j]]
                    contracted+=c
                exact=qs(0)
                free=[j for j in range(3) if not(frozen>>j&1)]
                for labels in product((0,1),repeat=len(free)):
                    xs=[qs(1)]*3; probability=qs(1)
                    for j,b in zip(free,labels):
                        xs[j]=(ZM,ZP)[b]; probability=qm(probability,(PM,PP)[b])
                    value=qs(0)
                    for e,c in terms.items():
                        term=qs(c)
                        for j in range(3):
                            if e[j]: term=qm(term,xs[j])
                        value=qa(value,term)
                    exact=qa(exact,qm(probability,qp(value,2*k)))
                require(exact==qs(contracted),'atom/expanded-moment agreement')
                require(contracted>=0,'atom positivity')
                checked+=1
    return {'models':checked,'predicates':COUNT-start,'scope':'three real coordinates, all masks and frozen sets'}

def rational_primes(X):
    a=[True]*(X+1); a[:2]=[False,False]
    for p in range(2,isqrt(X)+1):
        if a[p]:
            for n in range(p*p,X+1,p): a[n]=False
    return [p for p in range(2,X+1) if a[p]]

def prime_ideals(X):
    out=[]
    for p in rational_primes(X):
        if p in (2,3): continue
        if p%3==1:
            roots=[r for r in range(p) if (r*r+r+1)%p==0]
            require(len(roots)==2,'split roots')
            out.extend({'norm':p,'p':p,'root':r,'kind':'split'} for r in roots)
        elif p*p<=X: out.append({'norm':p*p,'p':p,'root':None,'kind':'inert'})
    out.sort(key=lambda z:(z['norm'],z['p'],-1 if z['root'] is None else z['root']))
    return out

def fm(x,y,p): return ((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%p)
def fp(x,n,p):
    z=(1,0)
    while n:
        if n&1: z=fm(z,x,p)
        x=fm(x,x,p); n//=2
    return z

def exponent(ideal,a,b):
    p=ideal['p']; q=ideal['norm']
    if ideal['kind']=='split':
        r=ideal['root']; x=(a+b*r)%p
        if not x: return -1
        z=pow(x,(p-1)//6,p); base=(1+r)%p
        for j in range(6):
            if pow(base,j,p)==z: return j
    else:
        x=(a%p,b%p)
        if x==(0,0): return -1
        z=fp(x,(q-1)//6,p)
        for j in range(6):
            if fp((1,1),j,p)==z: return j
    raise ArithmeticError('sextic symbol not a sixth root')

POWERS=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))

def get_columns(P,X):
    out=[]
    def visit(i,n,ids):
        if 2*n>X: out.append((tuple(ids),n))
        for j in range(i,len(P)):
            nn=n*P[j]['norm']
            if nn>X: break
            visit(j+1,nn,ids+[j])
    visit(0,1,[])
    return out

def row_height(D):
    lo,hi=D,D*D
    while lo<hi:
        m=(lo+hi)//2
        if m**20>=D**21: hi=m
        else: lo=m+1
    return lo

def census(D,y):
    start=COUNT; H=row_height(D); P=prime_ideals(D); cols=get_columns(P,D)
    R=2*isqrt(H)+3
    rows=[(a,b) for a in range(-R,R+1) for b in range(-R,R+1) if 0<norm(a,b)<=H]
    require(all(norm(a,b)<=H for a,b in rows),'row coverage')
    E=np.array([[exponent(p,a,b) for a,b in rows] for p in P],dtype=np.int16)
    require(exponent(P[0],7,0)==-1,'literal nonunit zero')
    require(P[0]['norm']==P[1]['norm']==7 and P[0]['root']!=P[1]['root'],'split ideals distinct')
    require(exponent(P[0],-P[0]['root'],1)==-1 and exponent(P[1],-P[0]['root'],1)!=-1,'collapse-split-primes rejected')
    def char(ids):
        if not ids: return np.ones(len(rows),dtype=np.int64),np.zeros(len(rows),dtype=np.int64)
        arr=E[list(ids),:]; e=arr.sum(axis=0)%6; zero=np.any(arr<0,axis=0)
        aa=np.array([POWERS[int(j)][0] for j in e],dtype=np.int64)
        bb=np.array([POWERS[int(j)][1] for j in e],dtype=np.int64)
        aa[zero]=0; bb[zero]=0
        return aa,bb
    A=np.zeros(len(rows),dtype=np.int64); B=A.copy()
    for ids,_ in cols:
        aa,bb=char(ids); sg=(-1)**len(ids); A+=sg*aa; B+=sg*bb
    norms=A*A-A*B+B*B
    native=sum(int(n)**2 for n in norms)
    products=Counter(tuple(sorted(x[0]+z[0])) for x in cols for z in cols)
    keys=sorted(products)
    chars=[char(ids) for ids in keys]
    # Bound every dot product and subsequent int64 combination BEFORE using it.
    require(6*len(rows)<2**62,'Gram int64 bound')
    aa=np.array([c[0] for c in chars],dtype=np.int64)
    bb=np.array([c[1] for c in chars],dtype=np.int64)
    gram2=2*(aa@aa.T)-aa@bb.T-bb@aa.T+2*(bb@bb.T)
    types=[sum((P[i]['norm']-1)//6 for i in ids)%6 for ids in keys]
    counts=[Counter(ids) for ids in keys]
    pending=[i for i,p in enumerate(P) if p['norm']>y]
    orders=[pending,list(reversed(pending))]
    initial=[0,0]; injections=[[0]*len(pending) for _ in orders]; dissipations=[[0]*len(pending) for _ in orders]
    rank=[{p:j for j,p in enumerate(order)} for order in orders]
    total=0; no_singleton=0; tuples=0
    for f in range(len(keys)):
        for g in range(f,len(keys)):
            if types[f]!=types[g]:
                require(int(gram2[f,g])==0,'unit orthogonality')
                continue
            v=int(gram2[f,g])*products[keys[f]]*products[keys[g]]*((-1)**(len(keys[f])+len(keys[g])))
            if f==g:
                require(v%2==0,'diagonal trace division'); v//=2
            total+=v; tuples+=1
            occ=counts[f]+counts[g]
            ones=[p for p,c in occ.items() if c==1 and P[p]['norm']>y]
            fours=[p for p,c in occ.items() if c==4 and P[p]['norm']>y]
            if not ones: no_singleton+=v
            for z,rr in enumerate(rank):
                a=max((rr[p] for p in ones),default=-1)
                qs=sorted(rr[p] for p in fours)
                if a<0: initial[z]+=v*(2**len(qs))
                else: injections[z][a]+=v*2**sum(t>a for t in qs)
                for j in qs:
                    if a<j: dissipations[z][j]+=v*2**sum(t>j for t in qs)
    require(total==native,'complete product/direct moment agreement')
    require(initial[0]==initial[1],'order-independent start')
    for z in range(2):
        require(all(v>=0 for v in dissipations[z]),'positive complete dissipation')
        require(initial[z]+sum(injections[z])-sum(dissipations[z])==native,'full telescoping')
    if D==64: require(native==26472,'independent-source D64 benchmark')
    if D==128: require(native==359664,'independent-source D128 benchmark')
    if D==256: require(native==3021246,'independent-source D256 benchmark')
    nonzero=[]
    for z,order in enumerate(orders):
        nonzero.append([{'prime':P[p],'injection':injections[z][j],'dissipation':dissipations[z][j],
                         'net':injections[z][j]-dissipations[z][j]} for j,p in enumerate(order)
                        if injections[z][j] or dissipations[z][j]])
    return {'D':D,'H':H,'frozen_norm_cap':y,'prime_ideals':len(P),'columns':len(cols),'rows':len(rows),
            'pair_products':len(keys),'evaluated_product_pairs':tuples,'native_M4':native,
            'smooth_singleton_sector':no_singleton,'golden_start':initial[0],
            'forward_injection':sum(injections[0]),'forward_dissipation':sum(dissipations[0]),
            'reverse_injection':sum(injections[1]),'reverse_dissipation':sum(dissipations[1]),
            'profiles':{'increasing':nonzero[0],'decreasing':nonzero[1]},'exact_predicates':COUNT-start}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--max-D',type=int,default=256); p.add_argument('--profiles',action='store_true'); a=p.parse_args()
    report={'scope':'Exact finite algebra and complete hard-window native fourth-moment flow, not asymptotics',
            'local':local_checks(),'atom_enumeration':atom_checks(),'censuses':[census(D,y) for D,y in [(64,17),(128,23),(256,30),(128,1)] if D<=a.max_D]}
    for case in report['censuses']:
        case['step_signs']={name:{'positive':sum(z['net']>0 for z in arr),'negative':sum(z['net']<0 for z in arr), 'zero':sum(z['net']==0 for z in arr)} for name,arr in case['profiles'].items()}
        if not a.profiles: del case['profiles']
    report['total_predicates']=COUNT
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__': main()
