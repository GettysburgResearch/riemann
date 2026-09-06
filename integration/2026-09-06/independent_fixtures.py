#!/usr/bin/env python3
"""Bounded independent integration fixtures; not a proof of analytic inputs or RH."""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def require(ok, label):
    if not ok:
        raise ValueError(label)


def determinant(a):
    a=[list(map(Q,row)) for row in a]
    n=len(a);ans=Q(1)
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        if pivot is None:return Q(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];ans=-ans
        x=a[k][k];ans*=x
        for j in range(k,n):a[k][j]/=x
        for i in range(k+1,n):
            x=a[i][k]
            for j in range(k,n):a[i][j]-=x*a[k][j]
    return ans


def dd2(t,y):
    return sum((y[i]/((t[i]-t[(i+1)%3])*(t[i]-t[(i+2)%3])) for i in range(3)),Q(0))


def jet_q(t,c,b2,m):
    u=t+c;den=u*u+b2
    return (4*m*u/den,4*m*(b2-u*u)/den**2,8*m*u*(u*u-3*b2)/den**3)


def jet_r(t,r):
    u=t+r
    return (2/u,-2/u**2,4/u**3)


def energy(j):return j[0]*j[2]-2*j[1]**2

def cross(f,g):return f[0]*g[2]+g[0]*f[2]-4*f[1]*g[1]


def run():
    counts={}
    def ck(lane,ok):
        require(ok,lane+' fixture failed')
        counts[lane]=counts.get(lane,0)+1
    # Total-value endpoint issue and function-level algebra, independent of zero data.
    for s in (Q(1,3),Q(1,2),Q(2),Q(-1)):
        for l0 in (Q(0),Q(2,7),Q(-5)):
            lam=l0-1/s-1/(1-s)
            ck('entire_normalization',s*(s-1)*lam/2==Q(1,2)+s*(s-1)*l0/2)
    for s in (Q(0),Q(1)):
        ck('entire_endpoint',Q(1,2)+s*(s-1)*Q(3)==Q(1,2))
        ck('old_total_endpoint',s*(s-1)*Q(7)==0)
    H=Q(1024);r0=Q(1)
    ck('reserve_budget',18/Q(32)+18/H==Q(297,512))
    ck('reserve_budget',1-Q(297,512)==Q(215,512))
    # Source-specific local payment jets, not a fitted final-shape PSD assumption.
    for a,b,m in ((Q(1,4),Q(1025),Q(1)),(Q(1,3),Q(2050),Q(2))):
        c=b*b-a*a;B2=4*a*a*b*b;d=c-r0;k=B2/d**2;eps=2*m*k/(1-k)
        ck('local_geometry',d>=Q(2,3)*b*b and k<Q(1,2) and eps<=9*m/b**2)
        for t in (Q(0),Q(1,16),Q(1,4),Q(1),Q(9),Q(10**6)):
            u=t+c;s=d/u;f=jet_q(t,c,B2,m);g=jet_r(t,r0)
            qpoly=1-k+3*k*s*(2-s)+k*k*s*s*(3-2*s)
            expected=16*m*s*s*qpoly/(u**4*(1+k*s*s)**3*(1-s)**3)
            ck('paid_orbit',energy(f)==-32*m*m*B2/(u*u+B2)**3)
            ck('paid_orbit',cross(f,g)==expected and qpoly>=1-k)
            paid=tuple(f[j]+eps*g[j] for j in range(3))
            ck('paid_orbit',paid[0]>0 and energy(paid)>=0)
            ck('source_monotonicity',f[1]<0 and f[0]+t*f[1]>0 and 2*f[1]+t*f[2]<0)
    # Algebraic three-node determinant factorization on unrelated exact data.
    xs=(Q(1,4),Q(1,2),Q(3,2));ts=tuple(x*x for x in xs)
    for ps in ((Q(2),Q(5),Q(7)),(Q(7,3),Q(2,5),Q(11)),(Q(1),Q(1),Q(1))):
        K=[[(xs[i]*ps[i]+xs[j]*ps[j])/(xs[i]+xs[j]) for j in range(3)] for i in range(3)]
        delta=(ts[1]-ts[0])*(ts[2]-ts[0])*(ts[2]-ts[1])
        denom=(xs[0]+xs[1])**2*(xs[0]+xs[2])**2*(xs[1]+xs[2])**2
        rhs=ps[0]*ps[1]*ps[2]*delta**2/denom*dd2(ts,[1/p for p in ps])*dd2(ts,[ts[i]*ps[i] for i in range(3)])
        ck('pick_factorization',determinant(K)==rhs)
    # Empty and finite off-line sources, including the repaired half-node.
    for off in (False,True):
        def p(t):
            return jet_r(t,r0)[0]+(jet_q(t,Q(1025)**2-Q(1,16),Q(1025)**2/Q(4),Q(1))[0] if off else 0)
        for x in ((Q(1,4),Q(1,2),Q(3,2)),(Q(1,2),Q(1,2),Q(2)),(Q(1),Q(1),Q(1))):
            K=[[(x[i]*p(x[i]**2)+x[j]*p(x[j]**2))/(x[i]+x[j]) for j in range(3)] for i in range(3)]
            for mask in range(1,8):
                idx=[i for i in range(3) if mask>>i&1]
                ck('finite_source_psd',determinant([[K[i][j] for j in idx] for i in idx])>=0)
    # D's finite counterexamples and corrected identities.
    ck('farkas_sign',Q(-1)+Q(1)>=0 and Q(-1)<0 and not Q(-1)-Q(1)>=0)
    bad=[[Q(0),Q(0)],[Q(0),Q(-1)]]
    ck('principal_minors',bad[0][0]==0 and determinant(bad)==0 and bad[1][1]<0)
    h=[(0 if n%3==0 else (-2)**(n//3)*(1 if n%3==1 else 2)) for n in range(48)]
    f=[];previous=0;difference=0
    for hn in h:difference+=hn;previous+=difference;f.append(previous)
    def delta(n,k):
        if k==0:return f[n] if n>=0 else 0
        return delta(n,k-1)-delta(n-1,k-1)
    for n in range(2,48):ck('varying_order',delta(n,2 if n%3==0 else 4)==0)
    ds={2:Q(3,2),3:Q(-2),5:Q(1,3)};a=Q(2);G=sum(ds.values())
    pair=sum((v*w*min(i,j)**2 for i,v in ds.items() for j,w in ds.items()),Q(0))
    integral=Q(0)
    knots=sorted(ds)
    for lo,hi in zip(knots,knots[1:]):
        suffix=sum(v for n,v in ds.items() if n>=hi)
        integral+=suffix*suffix*(hi*hi-lo*lo)
    ck('poisson_energy',pair==a*a*G*G+integral)
    ck('poisson_energy',pair-(G*G+integral)==(a*a-1)*G*G)
    for M in range(1,12):
        upper=Q(1,4)-sum((Q(1,4)**j for j in range(1,M+1)),Q(0))
        ck('schur_upper_direction',upper-(Q(1,4)-Q(1,3))==Q(1,3)*Q(1,4)**M)
    ck('schur_upper_direction',Q(1,4)-Q(1,4)==0 and Q(1,4)-Q(1,3)<0)
    ck('prime_atom_sign',-Q(1,128)-Q(1,2)/4==-Q(17,128)<0)
    # Independent finite P61 coefficient reconstruction, not the global bias campaign.
    primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)
    def mu_P(n):
        ans=1
        for p0 in primes:
            if n%p0==0:
                n//=p0;ans=-ans
                if n%p0==0:return 0
        return ans if n==1 else 0
    def div_P(n):return abs(mu_P(n))
    def q(n):return 6-6*(n==1)+9*(n==2)-3*(n==4)
    for n in range(1,201):
        divs=[d for d in range(1,n+1) if n%d==0 and div_P(d)]
        fc=sum(mu_P(d)*q(n//d) for d in divs)
        mc=sum(q(n//d) for d in divs)
        omega=sum(n%p0==0 for p0 in primes)
        ff=6*(omega==0)-6*mu_P(n)+9*(mu_P(n//2) if n%2==0 else 0)-3*(mu_P(n//4) if n%4==0 else 0)
        mm=6*2**omega-6*div_P(n)+9*(div_P(n//2) if n%2==0 else 0)-3*(div_P(n//4) if n%4==0 else 0)
        ck('p61_finite_coefficients',fc==ff)
        ck('p61_finite_coefficients',mc==mm)
    return {'marker':'PASS_INDEPENDENT_INTEGRATION_FIXTURES','counts':counts,'total':sum(counts.values()),
            'arithmetic':'EXACT_RATIONAL_INTEGER','infinite_analysis_machine_proved':False,
            'original_heavy_campaigns_rerun':False,'lean_compiled':False,'rh_proved':False}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
