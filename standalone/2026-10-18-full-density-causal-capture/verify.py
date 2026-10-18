"""Exact finite Euler-mask tests; not an analytic proof or Gaussian evaluation."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json

# Q(omega), omega^2+omega+1=0; no floating-point arithmetic is used.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1],-x[1])
def scale(x,a): return (x[0]*a,x[1]*a)
def power(x,n):
    y=(F(1),F(0))
    for _ in range(n): y=mul(y,x)
    return y
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); ROOT=(F(1),F(1))

def primes(N):
    flag=[True]*(N+1)
    for d in range(2,isqrt(N)+1):
        if flag[d]:
            for j in range(d*d,N+1,d): flag[j]=False
    return [d for d in range(2,N+1) if flag[d]]

def census(N,exterior=False,mutate=''):
    # Each coordinate is ONE prime ideal; split conjugates are not collapsed.
    ps=[]
    for p in primes(N):
        if exterior and p in (2,3): continue
        if p==3: ps.append((p,0,3))
        elif p%3==1: ps.extend([(p,0,p),(p,1,p)])
        elif p*p<=N: ps.append((p,0,p if mutate=='inert_norm' and p==2 else p*p))
    out=[((),1)]
    for idx,(_,_,q) in enumerate(ps):
        prev=list(out)
        for fac,n in prev:
            e=1
            while n*q**e<=N:
                out.append((fac+((idx,e),),n*q**e));e+=1
    return sorted(out,key=lambda z:(z[1],z[0])),ps

def hnf_counts(N):
    # omega-stable HNF lattice: a=c*t, b=c*u, u^2-u+1=0 mod t.
    cts=Counter()
    for c in range(1,isqrt(N)+1):
        for t in range(1,N//(c*c)+1):
            for u in range(t):
                if (u*u-u+1)%t==0: cts[c*c*t]+=1
    return cts

def subfac(n,d):
    nn=dict(n)
    for i,e in d:
        if nn.get(i,0)<e: return None
        nn[i]-=e
    return tuple((i,e) for i,e in sorted(nn.items()) if e)

def divides(d,n): return subfac(n,d) is not None

def divisors(n):
    opts=[[(i,j) for j in range(e+1)] for i,e in n]
    return [tuple((i,j) for i,j in z if j) for z in product(*opts)] if opts else [()]

def mu(n): return 0 if any(e>1 for _,e in n) else (-1)**len(n)
def support(n):return {i for i,e in n}
def norm(n,ps):
    q=1
    for i,e in n:q*=ps[i][2]**e
    return q

def radnorm(n,ps):
    q=1
    for i,e in n:q*=ps[i][2]
    return q

def chi(n,profile):
    out=ONE
    for i,e in n:out=mul(out,power(profile[i],e))
    return out

def convolution(f,g,rows):
    return {n:sum_field(mul(f.get(d,ZERO),g.get(subfac(n,d),ZERO)) for d in divisors(n)) for n,_ in rows}

def sum_field(xs):
    out=ZERO
    for x in xs:out=add(out,x)
    return out

def norm2(f,rows):
    z=sum_field(scale(mul(v,conj(v)),F(1,q)) for n,q in rows for v in [f[n]])
    if z[1]!=0 or z[0]<0:raise ValueError('nonreal_squared_norm')
    return z[0]

def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('--mutate',default='',choices=['','inert_norm','shared_radical','erase_mask','wrong_inverse','drop_powers','wrong_population','drop_horizon'])
    m=pa.parse_args().mutate
    counts=Counter()
    def check(name,ok):
        if not ok:raise ValueError(name)
        counts[name]+=1
    full,ps0=census(512,False,m)
    hc=hnf_counts(512);pc=Counter(q for _,q in full)
    for n in range(1,513):check('all_ideal_HNF_norm_fibers',hc[n]==pc[n])
    rows,ps=census(512,True)
    ext=Counter(q for _,q in rows)
    pref=[0]*513
    for n in range(1,513):pref[n]=pref[n-1]+hc[n]
    for B in range(1,513):
        expected=pref[B]-pref[B//4]-pref[B//3]+pref[B//12]
        check('exterior_count_inclusion_exclusion',sum(v for q,v in ext.items() if q<=B)==expected)
    check('complete_exterior_count',len(rows)==157)
    profiles=[[ONE]*len(ps),[power(ROOT,i%6) for i in range(len(ps))],
              [ZERO if i%5==0 else power(ROOT,(2*i+1)%6) for i in range(len(ps))]]
    # Exact full prefix identities, at every ideal through norm 512.
    for pr in profiles:
        native={n:scale(chi(n,pr),mu(n)) for n,q in rows}
        k={n:scale(chi(n,pr),F(1,radnorm(n,ps))) for n,q in rows}
        if m=='wrong_population':
            for n,q in rows:
                if n:
                    prob=F(1)
                    for i,e in n:
                        Q=ps[i][2];prob*=F(1,Q)/(1-F(1,Q**6))
                    k[n]=scale(chi(n,pr),prob)
        inv={}
        for n,q in rows:
            c=F(1)
            for i,e in n:
                Q=ps[i][2];c*=(-1 if m!='wrong_inverse' else 1)*F(1,Q)*(1-F(1,Q))**(e-1)
            inv[n]=scale(chi(n,pr),c)
        vk=convolution(k,inv,rows)
        va=convolution(k,native,rows)
        for n,q in rows:
            check('complete_limit_inverse',vk[n]==(ONE if not n else ZERO))
            phi=F(1)
            for i,e in n:phi*=1-F(1,ps[i][2])
            check('native_totient_source',va[n]==scale(native[n],phi))
        for B in [1,7,13,32,64,128]:
            masks=[b for b,q in rows if q<=B]; nb=len(masks)
            tmean={n:ZERO for n,q in rows}
            maskedmean={n:ZERO for n,q in rows}
            for b in masks:
                sb=support(b)
                t={n:chi(n,pr) if support(n)<=sb and not(m=='drop_powers' and any(e>1 for i,e in n)) else ZERO for n,q in rows}
                out=convolution(t,native,rows)
                for n,q in rows:
                    target=native[n] if (not(support(n)&sb) or m=='erase_mask') else ZERO
                    check('complete_native_mask_convolution',out[n]==target)
                    tmean[n]=add(tmean[n],t[n]);maskedmean[n]=add(maskedmean[n],out[n])
            for n,q in rows:
                nr=radnorm(n,ps)
                num=sum(1 for b,qn in rows if qn<=B//nr)
                check('finite_mask_kernel_count',scale(tmean[n],F(1,nb))==scale(chi(n,pr),F(num,nb)))
                cop=sum(1 for b in masks if not(support(b)&support(n)))
                check('finite_signed_native_mean',scale(maskedmean[n],F(1,nb))==scale(native[n],F(cop,nb)))
    # Complete finite critical weighted l2 assembly, retaining every cross term.
    small=[z for z in rows if z[1]<=64]
    keys=[n for n,q in small]
    rad={n:radnorm(n,ps) for n in keys}
    for pr in profiles:
        for kind in [0,1]:
            f={n:scale(chi(n,pr),F(mu(n) if kind==0 else (j%7-3),j+1)) for j,(n,q) in enumerate(small)}
            for B in [13,32,64,128]:
                masks=[b for b,q in rows if q<=B];nb=len(masks)
                lhs=F(0)
                for b in masks:
                    t={d:chi(d,pr) if support(d)<=support(b) else ZERO for d in keys}
                    lhs+=norm2(convolution(t,f,small),small)
                rhs=ZERO
                for d in keys:
                    for e in keys:
                        r=rad[d]*rad[e] if m=='shared_radical' else norm(tuple((i,1) for i in sorted(support(d)|support(e))),ps)
                        cnt=sum(1 for b,q in rows if q<=B//r)
                        if not cnt:continue
                        inner=ZERO
                        for n,q in small:
                            nd,ne=subfac(n,d),subfac(n,e)
                            if nd is not None and ne is not None:
                                inner=add(inner,scale(mul(f[nd],conj(f[ne])),F(1,q)))
                        rhs=add(rhs,scale(mul(mul(chi(d,pr),conj(chi(e,pr))),inner),cnt))
                check('complete_critical_weighted_Gram',rhs==(lhs,F(0)))
    # A finite upper horizon is NOT a full-line multiplier norm.
    top=keys[-1];pideal=((0,1),)
    f={n:ONE if n==top else ZERO for n in keys}
    shifted={n:f.get(subfac(n,pideal),ZERO) if subfac(n,pideal) is not None else ZERO for n in keys}
    actual=norm2(shifted,small)
    full_norm=norm2(f,small)/ps[0][2]
    if m=='drop_horizon':actual=full_norm
    check('finite_horizon_tail_retained',actual < full_norm)
    # All inverse local coefficients, including high prime powers, are necessary.
    for q in [7,13,19,25,31]:
        beta=1-F(1,q)
        kl=[F(1)]+[F(1,q)]*12
        il=[F(1)]+[-F(1,q)*beta**(j-1) for j in range(1,13)]
        for j in range(13):check('local_inverse_all_powers',sum(kl[i]*il[j-i] for i in range(j+1))==(1 if j==0 else 0))
    print(json.dumps({'status':'PASS','finite_predicates':sum(counts.values()),'groups':dict(sorted(counts.items())),
      'full_ideals_through_512':len(full),'exterior_ideals_through_512':len(rows),
      'profiles':'principal, abstract sixth-root phases, and literal zero phases; not a full Kummer census',
      'arithmetic':'integers and Fractions in Q(omega); exact finite critical-weight coefficient space',
      'scope':'finite source/convolution/count/Gram identities, not Gaussian evaluation, analytic proof, or RH',
      'rh_proved':False},sort_keys=True,indent=2))
if __name__=='__main__':main()
