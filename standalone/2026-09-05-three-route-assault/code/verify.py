#!/usr/bin/env python3
"""Recompute finite controls. This does not machine-prove the analytic theorems."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, isqrt
from pathlib import Path
import json
from exact import (add, apply, columns, det, dot, eye, hs2, inverse, matrix, mul,
                   outer, positive_definite, projection, scale, sub, tr, transpose, zeros)
ROOT=Path(__file__).resolve().parents[1]

class Checks:
    def __init__(self): self.counts: dict[str,int]={}
    def require(self, group: str, condition: bool, message: str):
        if not condition: raise ArithmeticError(f'{group}: {message}')
        self.counts[group]=self.counts.get(group,0)+1

def weight(n: int) -> F:
    if n<0: raise ValueError('negative index')
    r=isqrt(n+1)
    if r*r<n+1: r+=1
    return F(1,(n+1)*r)

def companion(a: list[F]):
    if not a or a[0]!=1: raise ValueError('constant coefficient must equal one')
    n=len(a)-1; out=zeros(n); b=F(1)
    for j in range(n):
        out[0][j]=(-1)**j*a[j+1]/b
        if j<n-1: out[j+1][j]=weight(j)
        b*=weight(j)
    return out

def elementary(xs: list[F]) -> list[F]:
    a=[F(1)]+[F(0)]*len(xs)
    for x in xs:
        for k in range(len(xs),0,-1): a[k]+=x*a[k-1]
    return a

def route1(c: Checks) -> dict:
    for n in range(1,8):
        for family in range(3):
            a=[F(1)]+[F(((-1)**(j*family))*(j+family),factorial(j+1)) for j in range(1,n+1)]
            k=companion(a)
            for u in range(-n,1):
                lhs=det(add(eye(n),scale(k,u)))
                rhs=sum((x*F(u)**j for j,x in enumerate(a)),F(0))
                c.require('companion_polynomial',lhs==rhs,'determinant/Taylor identity')
            if n>=3:
                v=[F(0)]*n; v[1]=1; v[2]=-1
                c.require('companion_nonpositive',dot(v,apply(k,v))==-weight(1),'negative tail Rayleigh vector')
    k=companion([F(1),F(1),F(2)])
    c.require('counterfeit',tr(k)==1 and det(k)==2,'complex-root counterfeit retained')
    c.require('counterfeit',F(1)-4*F(2)<0,'quadratic has nonreal roots')
    # Actual-theta marked obstruction uses exactly this vacuum/forced-bit algebra.
    for vacuum in [F(1,4),F(1,2),F(3,4)]:
        for conditional in [F(1,5),F(1,2),F(4,5)]:
            a=1-vacuum; b=a*conditional; joint=b; cov=joint-a*b
            c.require('marked_covariance',cov==vacuum*b and cov>0,'forced-bit covariance')
            # A real symmetric/Hermitian determinant instead subtracts |offdiag|^2.
            for offdiag in [F(0),F(1,7),F(2,7)]:
                c.require('marked_covariance',a*b-offdiag**2<joint,'determinantal exclusion')
    probs=[F(1,2),F(1,3),F(1,6)]
    fibers=[[F(1,3),F(1,7),F(1,11)], [F(1,2),F(1,5),F(1,9)], [F(2,3),F(2,7),F(1,7)]]
    mean=lambda xs:sum((p*x for p,x in zip(probs,xs)),F(0))
    e=[elementary(xs) for xs in fibers]
    aa=[mean([row[j] for row in e]) for j in range(4)]
    t=[[sum((x**j for x in xs),F(0)) for xs in fibers] for j in (1,2,3)]
    s2=aa[1]**2-2*aa[2]; s3=aa[1]**3-3*aa[1]*aa[2]+3*aa[3]
    var=mean([x*x for x in t[0]])-mean(t[0])**2
    cov=mean([x*y for x,y in zip(t[0],t[1])])-mean(t[0])*mean(t[1])
    kap3=mean([(x-mean(t[0]))**3 for x in t[0]])
    c.require('cycle_cumulants',s2==mean(t[1])-var,'second cycle variance debt')
    c.require('cycle_cumulants',s3==mean(t[2])-F(3,2)*cov+kap3/2,'third cycle cumulant debt')
    forced_a,forced_b,forced_joint=F(1,2),F(1,4),F(1,4)
    eps=F(1,100)
    c.require('marked_approximation',forced_joint-eps>(forced_a+eps)*(forced_b+eps),'small approximation cannot repair covariance')
    return {'synthetic_second_cycle':str(s2),'synthetic_third_cycle':str(s3),
            'actual_theta_marked_sign':'proved in manuscript; no numerical theta premise',
            'companion_positive':False}

def discrete_abel(bs: list[F], ws: list[F]):
    if len(bs)!=len(ws): raise ValueError('length mismatch')
    acc=F(0); prefixes=[]
    for b in bs: acc+=b; prefixes.append(acc)
    return prefixes[-1]*ws[-1]+sum((prefixes[i]*(ws[i]-ws[i+1]) for i in range(len(bs)-1)),F(0))

def route2(c: Checks) -> dict:
    for n in range(1,7):
        for seed in range(4):
            bs=[F((j+seed)%5-2,j+1) for j in range(n)]
            ws=[F((-1)**(j+seed)) for j in range(n)]
            value=sum((b*w for b,w in zip(bs,ws)),F(0))
            c.require('abel',discrete_abel(bs,ws)==value,'forward summation by parts')
            twisted=[b*w for b,w in zip(bs,ws)]
            c.require('abel',discrete_abel(twisted,[1/w for w in ws])==sum(bs,F(0)),'inverse summation by parts')
    for sigma,t,omega in product([F(1,2),F(1),F(2)],[F(-3),F(0),F(3,2)],[F(j,2) for j in range(-8,9)]):
        a=sigma**2+omega**2; b=sigma**2+(omega-t)**2
        residual=sigma**2*(a-b)**2-t**2*a*b
        factored=-t**2*(sigma**2+t*omega-omega**2)**2
        c.require('sharp_resolvent',residual==factored and residual<=0,'exact sharp multiplier inequality')
    for sigma,k in product([F(1),F(2),F(3)],[F(3,2),F(2),F(3)]):
        t=sigma*(k-1/k); omega=sigma*k
        ratio=(sigma**2+omega**2)/(sigma**2+(omega-t)**2)
        c.require('sharp_equality',ratio==k*k,'sharp multiplier equality point')
    return {'finite_frequency_theorem':'proved in manuscript; no Möbius exponent improvement',
            'new_power_saving':False}

def hilbert_packet(alphas: list[F], ms: dict[F,int], radius: int, c: Checks):
    n=2*radius+1; ts=list(range(-radius,radius+1))
    if any(a==0 or 1/a not in ms or ms[a]!=ms[1/a] for a in alphas):
        raise ValueError('fixture must be invariant under reciprocal conjugation')
    if len(set(alphas))!=len(alphas) or len(alphas)>n: raise ValueError('invalid fixture support')
    vs={a:[a**t for t in ts] for a in alphas}
    real=[a for a in alphas if abs(a)==1]; pairs=[a for a in alphas if abs(a)>1]
    rr={a:[(x+y)/2 for x,y in zip(vs[a],vs[1/a])] for a in pairs}
    oo={a:[(x-y)/2 for x,y in zip(vs[a],vs[1/a])] for a in pairs}
    uu=[vs[a] for a in real if ms[a]>1]+list(rr.values())
    vv=[vs[a] for a in real]+list(rr.values())
    pu=projection(uu,n); pv=projection(vv,n); pw=projection(list(vs.values()),n)
    pe=sub(pv,pu); pn=sub(pw,pv); ps=[pu,pe,pn]
    aa=zeros(n)
    for a in alphas: aa=add(aa,scale(outer(vs[a],vs[1/a]),F(ms[a],n)))
    mass=sum(ms.values()); simple=sum(ms[a]==1 for a in real); u=len(uu); q=len(pairs)
    leak=sum((dot(vs[a],apply(pu,vs[a]))/n for a in real if ms[a]==1),F(0))
    he=sum((ms[a]*dot(oo[a],apply(pe,oo[a]))/n for a in pairs),F(0))
    hn=sum((ms[a]*dot(oo[a],apply(pn,oo[a]))/n for a in pairs),F(0))
    d=mass-simple-2*u
    blocks=[[mul(mul(p,aa),r) for r in ps] for p in ps]
    rem=hs2(sub(blocks[0][0],scale(pu,2)))+hs2(sub(blocks[1][1],pe))+hs2(blocks[2][2])
    rem+=2*sum((hs2(blocks[i][j]) for i in range(3) for j in range(i+1,3)),F(0))
    energy=tr(mul(aa,aa)); lhs=energy-(2*mass-simple)
    rhs=2*d+2*leak+4*he+8*hn+rem
    c.require('hilbert_flag',aa==transpose(aa),'selfadjoint source')
    c.require('hilbert_flag',tr(aa)==mass,'trace is total multiplicity')
    c.require('hilbert_surplus',lhs==rhs,'full surplus identity')
    c.require('hilbert_surplus',min(F(d),leak,he,hn,rem)>=0,'nonnegative surplus terms')
    # Independent energy reconstruction from the pair kernel on the time grid.
    kernel=lambda a,b:sum(((a/b)**t for t in ts),F(0))/n
    pairenergy=sum((ms[a]*ms[b]*kernel(a,b)**2 for a in alphas for b in alphas),F(0))
    c.require('pair_energy',energy==pairenergy,'ordered pair kernel energy')
    if q:
        b=columns(vv,n); o=columns([oo[a] for a in pairs],n)
        gbb=scale(mul(transpose(b),b),F(1,n))
        gbo=scale(mul(transpose(b),o),F(1,n))
        goo=scale(mul(transpose(o),o),F(1,n))
        schur=sub(goo,mul(mul(transpose(gbo),inverse(gbb)),gbo))
        c.require('horizontal_schur',positive_definite(schur),'strict horizontal Gram floor')
        dd=zeros(q)
        for j,a in enumerate(pairs): dd[j][j]=F(ms[a])
        dh=mul(dd,schur); htrace=tr(dh); hsq=tr(mul(dh,dh))
        c.require('horizontal_schur',htrace==hn,'Schur trace is horizontal mass')
        c.require('horizontal_schur',hs2(blocks[2][2])==4*hsq,'negative block square')
        c.require('horizontal_surplus',lhs>=8*hn+4*hsq,'horizontal-only lower bound')
        if all(m==1 for m in ms.values()):
            c.require('horizontal_surplus',lhs>=8*hn+8*hn*hn/q,'sharp simple-packet bound')
        if len(alphas)==2 and all(m==1 for m in ms.values()):
            c.require('horizontal_sharp',lhs==8*hn+8*hn*hn,'one-pair equality')
    else: c.require('horizontal_zero',hn==0,'all-real supports have no horizontal defect')
    return {'support':[str(a) for a in alphas], 'multiplicities':[ms[a] for a in alphas],
            'grid_radius':radius,'M':mass,'simple_real':simple,'pairs':q,
            'energy':str(energy),'surplus':str(lhs),'horizontal_trace':str(hn)}

def route3(c: Checks) -> dict:
    specs=[([F(1)], [1],1),([F(1),F(-1)],[2,1],2),
           ([F(2),F(1,2)],[1,1],2),([F(2),F(1,2)],[3,3],2),
           ([F(1),F(2),F(1,2)],[1,1,1],3),
           ([F(1),F(-1),F(2),F(1,2)],[2,1,1,1],3),
           ([F(2),F(1,2),F(3),F(1,3)],[1,1,1,1],3),
           ([F(1),F(-1),F(2),F(1,2),F(3),F(1,3)],[3,1,2,2,1,1],4)]
    rows=[hilbert_packet(xs,dict(zip(xs,ms)),r,c) for xs,ms,r in specs]
    leading=[]
    for m in range(1,5):
        k=2*m+1; powers=list(range(1,k,2))
        gram=[[F(1,i+j+1) for j in powers] for i in powers]
        target=[F(1,k+j+1) for j in powers]
        residual=F(1,2*k+1)-dot(target,apply(inverse(gram),target))
        legendre_lead=F(comb(2*k,k),2**k)
        formula=1/(F(2*k+1)*legendre_lead**2)
        c.require('screening_legendre',residual==formula and residual>0,'exact monic Legendre residual')
        leading.append({'real_pairs':m,'power':2*k,'coefficient':str(residual/F(factorial(k)**2))})
    c.require('screening_legendre',leading[0]['coefficient']=='1/1575','sixth-order screening constant')
    # Exact Taylor expansion after projection on the limiting real linear span.
    raw={2*j:F(2**(2*j),2*factorial(2*j+1)) for j in range(1,5)}
    cc={2*j-1:F(2*j,factorial(2*j+1)) for j in range(1,5)}
    sq={k:F(0) for k in range(0,9)}
    for i,x in cc.items():
        for j,y in cc.items():
            if i+j<=8: sq[i+j]+=3*x*y
    coeffs={k:raw.get(k,F(0))-sq.get(k,F(0)) for k in (2,4,6,8)}
    c.require('screening_series',coeffs=={2:F(0),4:F(0),6:F(1,1575),8:F(1,14175)},'projected odd Taylor series')
    return {'packets':rows,'screening_leading_terms':leading,
            'new_zero_proportion':False,'arithmetic_horizontal_bound':False}

def run_all() -> dict:
    c=Checks(); r1=route1(c); r2=route2(c); r3=route3(c)
    return {'schema':'three-routes-exact-v1','arithmetic':'EXACT_RATIONAL / SYNTHETIC_CONTROL',
            'route1':r1,'route2':r2,'route3':r3,'checks':c.counts,'total_checks':sum(c.counts.values()),
            'analytic_proofs_machine_verified':False,'independent_review_completed':False,'rh_proved':False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true'); mode.add_argument('--check',action='store_true')
    args=p.parse_args(); data=run_all(); payload=json.dumps(data,indent=2,sort_keys=True)+'\n'
    dest=ROOT/'results'/'exact.json'
    if args.write: dest.write_text(payload,encoding='utf-8')
    elif not dest.is_file() or dest.read_text(encoding='utf-8')!=payload:
        raise SystemExit('FAIL: retained exact result differs from fresh reconstruction')
    print('PASS_THREE_ROUTE_FINITE_CONTROLS')
    print('exact_checks='+str(data['total_checks']))
    print('ANALYTIC_PROOFS_REQUIRE_REVIEW; RH_UNPROVED')
if __name__=='__main__': main()
