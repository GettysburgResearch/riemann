#!/usr/bin/env python3
"""Reconstruct the literal source, a six-moment model, and independent-spin barrier.
Standard library only. Finite interval checks do not prove the all-order Ising target.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import core as c
I=c.I; SCALE=c.SCALE; require=c.require
ROOT=Path(__file__).resolve().parent
COUNTS=(256,10,1,1,1,1)
CENTERS=tuple(map(F,(
 '0.000784100483934504800021164523067768053084801521311093425055476',
 '0.0261028464767228925702550599632506400078323685567327434446549',
 '0.0651834120102568568686597721894087581412131502974407889759052',
 '0.0852279920789717575679293799226624764155747893511433191156653',
 '0.120571177056070609724805507537325348644144706077350482344551',
 '0.267259230200238621330636622812748395131034479251098058303145')))


def invmat(A):
    n=len(A);a=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        require(k is not None,'singular rational matrix');a[k],a[j]=a[j],a[k]
        q=a[j][j];a[j]=[u/q for u in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j];a[i]=[u-q*v for u,v in zip(a[i],a[j])]
    return [r[n:] for r in a]


def absup(v):return F(max(abs(v.lo),abs(v.hi)),SCALE)
def rec(x):return [x.numerator,x.denominator]
def interval(lo,hi):return I(I.coerce(F(lo)).lo,I.coerce(F(hi)).hi)
def inside(x,lo,hi,label):
    require(x.lo>I.coerce(F(lo)).hi and x.hi<I.coerce(F(hi)).lo,label)


def cumulants(mu):
    std={j:mu[j]/mu[2]**(j//2) for j in mu}
    kap={};unit={};s={}
    for j in range(2,15,2):
        kap[j]=std[j]-sum((comb(j-1,k-1)*kap[k]*std[j-k] for k in range(2,j,2)),I.coerce(0))
        unit[j]=1-sum(comb(j-1,k-1)*unit[k] for k in range(2,j,2))
        s[j//2]=kap[j]/unit[j]
    require([unit[j] for j in range(2,15,2)]==[1,-2,16,-272,7936,-353792,22368256], 'unit cumulants')
    return unit,s


def certify_model(mu,unit,s):
    n=6;rad=F(1,10**16);nu=COUNTS;x=CENTERS
    box=[interval(a-rad,a+rad) for a in x]
    require(all(z.lo>I.rat(1,2000).hi and z.hi<SCALE for z in box),'positive box')
    require(all(box[i].hi<box[i+1].lo for i in range(5)),'distinct box')
    J0=[[F(k*nu[j])*x[j]**(k-1) for j in range(n)] for k in range(1,n+1)]
    R=invmat(J0)
    for i in range(n):
        for j in range(n):
            require(sum(R[i][k]*J0[k][j] for k in range(n))==int(i==j),'exact inverse identity')
    rn=max(sum(abs(t) for t in row) for row in R)
    require(rn<10**10,'preconditioner norm')
    res=[sum((nu[j]*I.coerce(x[j])**k for j in range(n)),I.coerce(0))-s[k] for k in range(1,n+1)]
    beta=max(absup(sum((R[i][k]*res[k] for k in range(n)),I.coerce(0))) for i in range(n))
    J=[[k*nu[j]*box[j]**(k-1) for j in range(n)] for k in range(1,n+1)]
    defect=[[I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(n)),I.coerce(0)) for j in range(n)] for i in range(n)]
    lip=max(sum(absup(t) for t in row) for row in defect)
    require(beta<F(1,10**20) and lip<F(1,10**9),'Banach bounds')
    require(beta+lip*rad<rad,'independent self map')
    # Paper's bound for the fixed 270-spin Gibbs law at EVERY real coupling J.
    crude=factorial(12)*2**11*2*12**2*40000*10000*270**12
    require(crude<10**55,'complete Gibbs derivative ceiling')
    maxJ=F(1,10**100)
    gbeta=beta+rn*10**55*maxJ
    glip=lip+6*rn*10**55*maxJ
    require(gbeta+glip*rad<rad and glip<F(1,10**8),'strict ferromagnetic self map')
    diff=unit[14]*(sum((nu[j]*box[j]**7 for j in range(n)),I.coerce(0))-s[7])
    inside(diff,'0.0409','0.0410','unmatched independent fourteenth moment')
    return {'spin_count':sum(nu),'multiplicities':list(nu),'centers':[str(a) for a in x],
        'radius':rec(rad),'squared_weights':[b.record() for b in box],
        'physical_weights':[(mu[2]*b).sqrt().record() for b in box],
        'preconditioner_norm':I.coerce(rn).record(),'residual_bound':I.coerce(beta).record(),'jacobian_defect_bound':I.coerce(lip).record(),
        'positive_coupling_interval':[rec(F(0)),rec(maxJ)],
        'coupled_selfmap_ratio':I.coerce(gbeta/rad+glip).record(),
        'standardized_fourteenth_difference':diff.record()}


def old_tangent(mu,unit):
    old=c.fit_seed(mu);x=[I(*old[k]) for k in ('a','b','c','d')]
    e=[I.coerce(1)]+[I.coerce(0) for _ in range(4)]
    for y in x:
        for k in range(4,0,-1):e[k]=e[k]+y*e[k-1]
    lam=[5*unit[10]*((-1)**(4-k))*e[5-k]/(k*unit[2*k]) for k in range(1,5)]
    out=[]
    for i,j in ((0,0),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)):
        a=x[i].sqrt();b=x[j].sqrt();der=[]
        for r in range(1,6):
            d=I.coerce(0)
            for l in range(r):
                tc=F(unit[2*l+2],factorial(2*l+1))
                td=F(unit[2*(r-1-l)+2],factorial(2*(r-1-l)+1))
                d=d+factorial(2*r)*tc*td*a**(2*l+1)*b**(2*(r-1-l)+1)
            der.append(d)
        ans=der[4]-sum((lam[k]*der[k] for k in range(4)),I.coerce(0))
        inside(ans,'-0.030','-0.009','compensated positive-edge derivative')
        out.append({'edge_class':[i,j],'derivative':ans.record()})
    return {'old_squared_weights':[y.record() for y in x],'per_edge_derivatives':out}


def zero_and_barrier(raw,mu,four):
    inside(four[0],'5e-18','6e-18','positive endpoint')
    inside(four[1],'-9e-18','-8e-18','negative endpoint')
    inside(four[2],'-3.0e-12','-2.9e-12','nonzero triple')
    require(mu[2].hi<I.rat(1,20).lo,'variance ceiling')
    # IVT zero in [a,b]; triple interval radius 3(b-a)/2; |Xi'|<1/8.
    halfwidth=F(3,2)*F(1,10**14)
    triple=I(four[2].lo-I.coerce(halfwidth/8).hi,four[2].hi+I.coerce(halfwidth/8).hi)
    require((triple/raw[0]).hi<I.rat(-4,10**12).lo,'complete triple neighborhood')
    require(2*F(1,20)*F(142,10)**2<21,'amplification ceiling')
    require((1+3**21)*F(1,10**22)<F(4,10**12),'tripling separation')
    n=256
    low=F(3**43,2**n)
    model=F(47**257,factorial(257))/(1-F(47,258))
    target=F(10**100,2**514)
    require(F(800000,49)*(1+factorial(43))<10**100,'safe real MGF ceiling')
    require(low+model+target<F(1,10**50),'all 512-moment remainder')
    require(F(1,10**50)+F(3,10**24)<F(1,10**22),'small total coupling exclusion')
    return {'fourier_values':[q.record() for q in four],
        'triple_interval_Xi':triple.record(),'separation_tolerance':rec(F(1,10**22)),
        'independent_IR_order_excluded':256,
        'taylor_error_bound':I.coerce(low+model+target).record(),
        'total_coupling_strict_lower_bound':rec(F(1,10**24))}


def algebra_controls():
    # Cumulants from exact convolution independently check first seven unit values.
    from itertools import product
    cases=0
    for weights in ((F(1),),(F(1,3),F(2,5)),(F(1,4),F(1,3),F(1,2))):
        vals=[sum(a*t for a,t in zip(weights,sig)) for sig in product((-1,1),repeat=len(weights))]
        mm={j:sum(v**j for v in vals)/len(vals) for j in range(0,15,2)};kk={};uc={}
        for j in range(2,15,2):
            kk[j]=mm[j]-sum(comb(j-1,k-1)*kk[k]*mm[j-k] for k in range(2,j,2))
            uc[j]=1-sum(comb(j-1,k-1)*uc[k] for k in range(2,j,2))
            require(kk[j]==uc[j]*sum(a**j for a in weights),'independent cumulant addition');cases+=1
    for r in range(1,9):
        nodes=[F(i+1,r+2) for i in range(r)];nu=[i+1 for i in range(r)]
        J=[[F(k*nu[i])*nodes[i]**(k-1) for i in range(r)] for k in range(1,r+1)]
        R=invmat(J);xd=[-row[0] for row in R]
        lhs=sum(nu[i]*nodes[i]**r*xd[i] for i in range(r));rhs=F((-1)**r)
        for a in nodes:rhs*=a
        require(lhs==rhs,'Gaussian lift sign identity');cases+=1
    # Rational Chebyshev tripling identity, no selected trigonometric samples.
    for j in range(-20,21):
        q=F(j,20);require(4*q**3-3*q==q*(4*q*q-3),'tripling polynomial');cases+=1
    for j in range(1,10):
        r=F(j,10);ct=-r
        val=(4*ct**3-3*ct+r)/(1+r)
        require(val==4*r*(1-r)>0,'interacting tripling witness');cases+=1
    return {'rational_algebra_cases':cases}


def produce():
    raw,mu,four,cover=c.full_theta();unit,s=cumulants(mu)
    return {'schema':'IME26-1','rh_proved':False,'all_order_realization_proved':False,
        'exact_even_moment_orders':[2,4,6,8,10,12],
        'coverage':cover,'raw_moments':{str(j):t.record() for j,t in raw.items()},
        'normalized_moments':{str(j):t.record() for j,t in mu.items()},
        'power_sum_targets':{str(j):t.record() for j,t in s.items()},
        'model':certify_model(mu,unit,s),'old_seed_tangent':old_tangent(mu,unit),
        'barrier':zero_and_barrier(raw,mu,four),'controls':algebra_controls()}


def unique_pairs(pairs):
    d={}
    for k,v in pairs:
        require(k not in d,'duplicate key');d[k]=v
    return d

def no_float(x):raise ValueError('noninteger JSON number')

def strict_load(path):
    return json.loads(Path(path).read_text(),object_pairs_hook=unique_pairs,
                      parse_float=no_float,parse_constant=no_float)

def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def authenticate():
    manifest=ROOT/'SHA256SUMS';require(manifest.is_file() and not manifest.is_symlink(),'manifest')
    lines=manifest.read_text().splitlines();names=[]
    for line in lines:
        dig,name=line.split('  ');require(len(dig)==64 and '/' not in name,'manifest row')
        p=ROOT/name;require(p.is_file() and not p.is_symlink(),'regular payload')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==dig,'hash '+name);names.append(name)
    require(len(names)==len(set(names)) and len(names)>0,'manifest unique')
    actual={p.name for p in ROOT.iterdir()}
    require(actual==set(names)|{'SHA256SUMS'},'inventory')


def main():
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    require(bool(a.emit)^bool(a.check),'choose emit or check')
    if a.check:
        authenticate(); expected=strict_load(a.check)
    obj=produce()
    txt=json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    else:require(same(expected,obj),'reconstruction mismatch')
    print(txt,end='')
if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,ArithmeticError,KeyError,StopIteration) as e:
        print('REFUSED:',str(e),file=sys.stderr);sys.exit(2)
