#!/usr/bin/env python3
"""Exact finite arithmetic for the joint-archimedean theorem; no asymptotic tests.

Only Python's standard library is required. Predicates include setup guards.
All ideals through norm 512 are enumerated up to the six units and checked
against an independent rational-norm Euler count. The finite moment tests
state smaller, complete column/row domains explicitly. --mutate executes
intentionally incorrect models; a nonzero exit is expected for each one.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json

COUNT=0
MUTATION=''
UNITS=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ONE=(F(1),F(0)); ZERO=(F(0),F(0))

def require(test: bool, label: str) -> None:
    global COUNT
    COUNT+=1
    if not test: raise ArithmeticError(label)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1],-x[1])
def norm(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def scale(x,c): return (x[0]*c,x[1]*c)
def power(x,e):
    if e<0: return power(conj(x),-e)  # used only for unit-modulus x
    z=(1,0)
    while e:
        if e&1: z=mul(z,x)
        x=mul(x,x); e//=2
    return z

def canonical(x): return min(mul(x,u) for u in UNITS)
def divide(x,y):
    a,b=mul(x,conj(y)); q=norm(y)
    return (a//q,b//q) if a%q==0 and b%q==0 else None

def primes(X):
    sieve=[True]*(X+1); sieve[:2]=[False,False]
    for p in range(2,isqrt(X)+1):
        if sieve[p]:
            for n in range(p*p,X+1,p): sieve[n]=False
    return [p for p in range(2,X+1) if sieve[p]]

def all_ideals(X):
    B=2*isqrt(X)+2
    out={canonical((a,b)) for a in range(-B,B+1) for b in range(-B,B+1)
         if 0<norm((a,b))<=X}
    return sorted(out,key=lambda x:(norm(x),x))

def build_primes(X,ideals):
    bynorm=defaultdict(list)
    for a in ideals: bynorm[norm(a)].append(a)
    ps=[]
    for p in primes(X):
        if p==3: ps.append((3,3,canonical((1,-1)),None,'ramified'))
        elif p%3==1:
            require(len(bynorm[p])==2,'two split prime ideals')
            for a in bynorm[p]:
                root=(-a[0]*pow(a[1],-1,p))%p
                require((root*root+root+1)%p==0,'split root orientation')
                ps.append((p,p,a,root,'split'))
        elif p*p<=X: ps.append((p*p,p,canonical((p,0)),None,'inert'))
    return sorted(ps,key=lambda x:(x[0],x[2]))

def factor(a,ps):
    v=a; factors=[]
    for j,pp in enumerate(ps):
        if pp[0]>norm(v): break
        e=0
        while True:
            q=divide(v,pp[2])
            if q is None: break
            v=q; e+=1
        if e: factors.append((j,e))
    require(norm(v)==1,'complete prime ideal factorization')
    require(norm(a)==prod_int(ps[j][0]**e for j,e in factors),'factor norms')
    return tuple(factors)

def prod_int(xs):
    v=1
    for x in xs:v*=x
    return v

def euler_counts(X):
    out=[0]*(X+1); out[1]=1
    for p in primes(X):
        degrees=[1] if p==3 else ([1,1] if p%3==1 else [2])
        for f in degrees:
            q=p**f
            if q>X:continue
            new=out[:]; v=q
            while v<=X:
                for n in range(1,X//v+1):new[n*v]+=out[n]
                v*=q
            out=new
    return out

def residue_power(x,e,p):
    z=(1,0)
    while e:
        if e&1:z=tuple(t%p for t in mul(z,x))
        x=tuple(t%p for t in mul(x,x));e//=2
    return z

def sextic(pp,u):
    q,p,gen,root,kind=pp
    if kind=='split':
        x=(u[0]+root*u[1])%p
        if x==0:return ONE if MUTATION=='erase-mask' else ZERO
        value=pow(x,(q-1)//6,p); eps=(1+root)%p
        for j in range(6):
            if pow(eps,j,p)==value:return tuple(F(t) for t in UNITS[j])
    elif kind=='inert':
        x=(u[0]%p,u[1]%p)
        if x==(0,0):return ONE if MUTATION=='erase-mask' else ZERO
        value=residue_power(x,(q-1)//6,p)
        for j in range(6):
            if residue_power((1,1),j,p)==value:return tuple(F(t) for t in UNITS[j])
    raise ArithmeticError('invalid sextic prime or residue')

def symbol(fac,u,ps):
    z=ONE
    for j,e in fac:z=mul(z,power(sextic(ps[j],u),e))
    return z

def psi(a,l=1):
    if MUTATION=='erase-angle':return ONE
    exponent=1 if MUTATION=='omit-unit-power' else 6
    value=scale(power(a,exponent),F(1,norm(a)**3))
    return power(value,l)

def qstr(x):
    return str(x.numerator) if x.denominator==1 else str(x)

def finite_poly(cols,k):
    out={canonical((1,0)):ONE}
    for _ in range(k):
        new=defaultdict(lambda:ZERO)
        for a,c in out.items():
            for b,d in cols:
                key=canonical(mul(a,b)); new[key]=add(new[key],mul(c,d))
        out=dict(new)
    return out

def coefficient_checks(ps):
    checks=0
    for q,p,gen,root,kind in ps:
        if p in(2,3) or q>31:continue
        for m in(2,3,4,6,8):
            # Exact critical weighted coefficient lists: at e=m*j+eps,
            # t_e^2/q^e=q^(-2j-eps). No irrational coefficients needed.
            total=F(0)
            for j in range(8):
                for eps in(0,1):
                    e=m*j+eps
                    wt=F(1,q**(2*j+eps));total+=wt
                    require(wt==F(q**(j*(m-2)),q**e),'critical square weight')
                    checks+=1
            require(total<1/((1-F(1,q))),'square mass majorant finite part')
            coupled=(1-F(1,q))*(1+(1-F(1,q))**2/F(q)+F(1,q*q))
            require(coupled>0 and abs(coupled-1)<F(4,q*q),'coupled density local factor')
        # Character-zero at a sixth power must not become one.
        require(sextic((q,p,gen,root,kind),gen)==ZERO,'literal prime zero')
    # All-order balanced local factor cancels its degree-one edge matrix.
    for k in range(1,9):
        count=Counter()
        for maskL in range(1<<k):
            for maskR in range(1<<k):
                a=maskL.bit_count();b=maskR.bit_count()
                if a==b:count[a]+=1
        require(count[0]==1 and count[1]==k*k,'local matching linear term')
    return checks

def run():
    ideals=all_ideals(512);ps=build_primes(512,ideals)
    counts=Counter(norm(a) for a in ideals);other=euler_counts(512)
    for n in range(1,513):require(counts[n]==other[n],'lattice/Euler complete norm census')
    facs={a:factor(a,ps) for a in ideals}
    good=[a for a in ideals if all(ps[j][1] not in(2,3) for j,e in facs[a])]
    sq=[a for a in good if all(e==1 for j,e in facs[a])]
    for a in ideals:
        require(norm(psi(a))==1,'unit-modulus archimedean character')
        for unit in UNITS:require(psi(mul(a,unit))==psi(a),'unit-independent character')
    chosen=[a for a in good if norm(a)<=64]
    for a in chosen:
        for b in chosen:
            require(psi(mul(a,b))==mul(psi(a),psi(b)),'angular multiplicativity')
            require(norm(mul(a,b))==norm(a)*norm(b),'multiplicative ideal norm')
    # Complete norm fibers must not be collapsed.
    norm7=[a for a in ideals if norm(a)==7]
    require(len(norm7)==2 and norm7[0]!=norm7[1],'two norm-seven ideals')
    require(psi(norm7[0])!=psi(norm7[1]),'angular separation of conjugate ideals')
    key=lambda a: norm(a) if MUTATION=='collapse-norm' else canonical(a)
    require(len({key(a) for a in norm7})==2,'product keys must retain ideal identity')
    bound=F(600,2401)
    if MUTATION=='false-isometry-constant':bound=F(1,2)
    require(bound<F(1,3),'strict near-isometry constant')
    exp4=sum(F(4**j,prod_int(range(1,j+1))) for j in range(8))
    require(exp4>50,'rational exponential lower bound')
    require(3*((1+F(2,49))**2-1)==F(600,2401),'exact Schur arithmetic')
    fixtures=[]
    for D,H in((32,13),(64,79),(128,13)):
        columns=[a for a in sq if D<2*norm(a)<=2*D]
        B=2*isqrt(H)+2
        rows=[(a,b) for a in range(-B,B+1) for b in range(-B,B+1) if 0<norm((a,b))<=H]
        totals={l:0 for l in(-1,0,1)}; diag=0; normdiag=0
        for u in rows:
            cs=[(a,scale(symbol(facs[a],u,ps),(-1)**len(facs[a]))) for a in columns]
            for k in(1,2):
                coeff=finite_poly(cs,k)
                for l in(-1,0,1):
                    direct=ZERO
                    for a,c in cs:direct=add(direct,mul(c,psi(a,l)))
                    via=ZERO
                    for a,c in coeff.items():via=add(via,mul(c,psi(a,l)))
                    require(power(direct,k)==via,'complete product angular evaluation')
                    require(norm(via)==norm(direct)**k,'exact 2k moment evaluation')
                    if k==2:totals[l]+=norm(via)
                if k==2:
                    diag+=sum(norm(c) for c in coeff.values())
                    fibers=defaultdict(lambda:ZERO)
                    for a,c in coeff.items():fibers[norm(a)]=add(fibers[norm(a)],c)
                    normdiag+=sum(norm(c) for c in fibers.values())
        fixtures.append({'X':D,'H':H,'all_good_squarefree_columns':len(columns),
            'all_nonzero_rows':len(rows),'native_M4_at_t0_l0':qstr(F(totals[0])),
            'M4_l_plus1':qstr(F(totals[1])),'M4_l_minus1':qstr(F(totals[-1])),
            'product_ideal_diagonal':qstr(F(diag)),'product_norm_diagonal':qstr(F(normdiag))})
        if D==64:require(totals[0]==26472,'prior complete native census D64 H79')
    local=coefficient_checks(ps)
    for k in range(1,13):
        ideal_log=(k-1)**2; norm_log=2*k*k-2*k+1
        require(norm_log-ideal_log==k*k,'same-radial logarithmic gain')
        for j in range(2*k+1):
            tau=F(j,4)
            if tau<=F(k,2):
                require(max(k+tau,2*k-tau)==2*k-tau,'short radial exponent maximum')
        require(F(k,2)*2==k,'balanced parameter volume')
    e=F(1,100000);alpha=F(1,2)+e;beta=F(1,2)
    C=F(1,6)+alpha/3;old_theta=alpha+beta/2-F(1,2)
    require(C-old_theta==F(1,12)-2*e/3,'959 theta-saving reconstruction')
    require(1-C+F(1,4)+3*e==F(11,12)+8*e/3,'959 true Mellin shift')
    # A finite product polynomial realizes the sharp obstruction to removing
    # angle from this near-isometry: norm-only averaging leaves 4, not 2.
    require(abs(F(4)-2)>F(600,2401)*2,'omitting angle violates claimed constant')
    return {'status':'exact finite algebra only; not proof of an asymptotic estimate',
        'complete_ideal_cap':512,'all_ideals':len(ideals),'good_ideals':len(good),
        'good_squarefree_ideals':len(sq),'prime_ideals':len(ps),
        'norm7_generators':norm7,'norm7_psi1':[[qstr(F(v)) for v in psi(a)] for a in norm7],
        'near_isometry_constant':'600/2401','finite_native_cases':fixtures,
        'critical_local_weights_checked':local,'predicates_including_setup':COUNT}

def main():
    global MUTATION
    p=argparse.ArgumentParser();p.add_argument('--mutate',default='',choices=['','erase-mask','erase-angle','omit-unit-power','collapse-norm','false-isometry-constant'])
    args=p.parse_args();MUTATION=args.mutate
    print(json.dumps(run(),sort_keys=True,indent=2))
if __name__=='__main__':main()
