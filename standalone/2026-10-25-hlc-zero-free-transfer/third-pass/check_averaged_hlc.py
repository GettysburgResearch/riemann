#!/usr/bin/env python3
"""Exact finite identities for AVERAGED_HLC.md; no asymptotic claims."""
from fractions import Fraction as F
from math import isqrt
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def arithmetic(nmax):
    factors = [{} for _ in range(nmax + 1)]
    for p in range(2, nmax + 1):
        if factors[p]:
            continue
        for n in range(p, nmax + 1, p):
            k, v = n, 0
            while k % p == 0:
                k //= p
                v += 1
            factors[n][p] = v
    mu = [0] * (nmax + 1)
    mu[1] = 1
    lam = [{} for _ in range(nmax + 1)]
    logs = [{} for _ in range(nmax + 1)]
    for n in range(2, nmax + 1):
        mu[n] = 0 if any(v > 1 for v in factors[n].values()) else (-1)**len(factors[n])
        logs[n] = {p: F(v) for p, v in factors[n].items()}
        if len(factors[n]) == 1:
            lam[n] = {next(iter(factors[n])): F(1)}
    return mu, factors, lam, logs


def bump(t, power):
    return ((t-1)*(2-t))**power if 1 < t < 2 else F(0)


def summation_check(m_scale, n_scale, h_scale):
    x_scale = m_scale*n_scale
    m_max, v_max = 2*m_scale + 2, 2*x_scale + 2
    mu, _, _, _ = arithmetic(v_max + m_max + 4)
    prefixes = [0]
    for value in mu[1:]:
        prefixes.append(prefixes[-1] + value)
    direct, parts = F(0), F(0)
    for n in range(n_scale + 1, 2*n_scale + 1):
        coefficient = F((-1)**n * (n+2), n+3)
        def kernel(m, v):
            return (bump(F(m,m_scale),2)*bump(F(v,x_scale),2)
                    *bump(F(v-m*n,h_scale),3))
        for m in range(1, m_max + 1):
            for v in range(1, v_max + 1):
                direct += coefficient*mu[m]*mu[v]*kernel(m,v)
                mixed = kernel(m+1,v+1)-kernel(m+1,v)-kernel(m,v+1)+kernel(m,v)
                parts += coefficient*prefixes[m]*prefixes[v]*mixed
    require(direct == parts, 'exact mixed summation by parts')
    require(direct != 0, 'control has nonzero signed sum')
    require(-parts != direct, 'negative control: wrong integration sign')
    return {'M':m_scale,'N':n_scale,'H':h_scale,'exact_T':str(direct)}


def cutoff(t):
    if t <= 1:
        return F(1)
    if t >= 2:
        return F(0)
    z=t-1
    return 1-3*z*z+2*z*z*z


def formal_add(target, source, weight=F(1)):
    for p,value in source.items():
        target[p] = target.get(p,F(0))+weight*value
        if target[p] == 0:
            del target[p]


def scalar_log_convolution(scalars, logs):
    nmax=len(scalars)-1
    out=[{} for _ in range(nmax+1)]
    for d in range(1,nmax+1):
        if scalars[d] == 0:
            continue
        for k in range(1,nmax//d+1):
            formal_add(out[d*k],logs[k],scalars[d])
    return out


def log_times_one(logs):
    nmax=len(logs)-1
    out=[{} for _ in range(nmax+1)]
    for d in range(1,nmax+1):
        for k in range(1,nmax//d+1):
            formal_add(out[d*k],logs[d])
    return out


def vaughan_check(nmax,u,v):
    mu,_,lam,logs=arithmetic(nmax)
    mu1=[F(mu[n])*cutoff(F(n,u)) for n in range(nmax+1)]
    mu2=[F(mu[n])-mu1[n] for n in range(nmax+1)]
    lam1=[{p:c*cutoff(F(n,v)) for p,c in lam[n].items()
           if c*cutoff(F(n,v)) != 0} for n in range(nmax+1)]
    lam2=[]
    for n in range(nmax+1):
        term=dict(lam[n]); formal_add(term,lam1[n],F(-1)); lam2.append(term)
    one=scalar_log_convolution(mu1,logs)
    two=scalar_log_convolution(mu1,log_times_one(lam1))
    three=scalar_log_convolution(mu2,log_times_one(lam2))
    for n in range(1,nmax+1):
        rhs=dict(lam1[n])
        formal_add(rhs,one[n]); formal_add(rhs,two[n],F(-1)); formal_add(rhs,three[n])
        require(rhs == lam[n], 'smooth Vaughan identity at n='+str(n))
    return {'nmax':nmax,'U':u,'V':v,'arithmetic':'formal prime logarithms'}


def cadd(a,b):
    return (a[0]+b[0],a[1]+b[1])


def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def cconj(a):
    return (a[0],-a[1])


def cnorm(a):
    return a[0]*a[0]+a[1]*a[1]


def cmean(values):
    n=len(values)
    return (sum(a[0] for a in values)/n,sum(a[1] for a in values)/n)


def affine_check(p):
    f=[(F(x*x-3*x+1),F(x-2)) for x in range(p)]
    g=[(F(x**3+2*x-1),F((-1)**x)) for x in range(p)]
    mf,mg=cmean(f),cmean(g)
    vf=sum(cnorm(z) for z in f)/p-cnorm(mf)
    vg=sum(cnorm(z) for z in g)/p-cnorm(mg)
    energy=F(0)
    for q in range(1,p):
        for h in range(p):
            correlation=cmean([cmul(f[x],cconj(g[(q*x+h)%p])) for x in range(p)])
            energy+=cnorm(correlation)
    energy/=p*(p-1)
    expected=cnorm(mf)*cnorm(mg)+vf*vg/(p-1)
    require(energy==expected,'complete affine second moment')
    require(energy != vf*vg/(p-1),'negative control: missing mean mode')
    return {'prime':p,'exact_energy':str(energy),'nonconstant_energy':str(vf*vg/(p-1))}


def ramare_check(nmax,y):
    mu,factors,_,_=arithmetic(nmax)
    for n in range(1,nmax+1):
        rhs=F(0)
        for p in factors[n]:
            if p<=y:
                continue
            a=n//p
            if a%p==0:
                continue
            count=sum(q>y for q in factors[a])
            rhs-=F(mu[a],1+count)
        lhs=mu[n] if any(p>y for p in factors[n]) else 0
        require(rhs==lhs,'exact broad selector at n='+str(n))
    return {'nmax':nmax,'y':y}


if __name__=='__main__':
    result={
      'status':'PASS',
      'scope':'exact finite identities; no summatory or zero-free assertion',
      'mixed_summation':[summation_check(4,6,6),summation_check(5,8,10)],
      'smooth_vaughan':[vaughan_check(400,7,11),vaughan_check(512,13,5)],
      'affine_group':[affine_check(p) for p in (3,5,7,11)],
      'broad_selector':[ramare_check(2000,y) for y in (3,7,13)]
    }
    print(json.dumps(result,indent=2))
