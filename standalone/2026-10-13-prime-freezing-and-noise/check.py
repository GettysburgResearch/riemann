#!/usr/bin/env python3
"""Exact finite diagnostics; not a proof of any asymptotic estimate.
Uses only the standard library. Run with Python or python -O.
Native character checks restrict columns to the five stated prime ideals;
they do not enumerate the full native family below the norm cap.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, prod
from collections import Counter
import json

# a+b*w, where w^2+w+1=0. All arithmetic is exact.
def z(a=0,b=0): return (F(a),F(b))
ZERO,ONE,ROOT=z(),z(1),z(1,1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def scale(x,t): return (x[0]*t,x[1]*t)
def power(x,n):
    r=ONE
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def conj(x): return (x[0]-x[1],-x[1])
def norm(x):
    a,b=x;return a*a-a*b+b*b
def real(x): return x[0]-x[1]/2
def total(xs):
    r=ZERO
    for x in xs:r=add(r,x)
    return r
ROOTS=[power(ROOT,j) for j in range(6)]
COUNTS=Counter()
def check(ok,label):
    COUNTS[label]+=1
    if not ok:raise RuntimeError('failed: '+label)

def conv(a,b,J):
    return [total(mul(a[i],b[n-i]) for i in range(n+1)) for n in range(J+1)]

def local_checks():
    J=6
    for a,ph in product([F(0),F(1,3),F(1,2),F(1)],ROOTS+[ZERO]):
        means_h=[ZERO]*(J+1); means_g=[ZERO]*(J+1)
        for eps in [-1,1]:
            prob=(1-a*eps)/2
            zz=F(eps)+a
            h=[ONE]+[scale(power(ph,j),zz*a**(j-1)) for j in range(1,J+1)]
            hm=[ONE]+[scale(power(ph,j),-zz*(-a)**(j-1)) for j in range(1,J+1)]
            g=[ONE]+[scale(power(ph,j),-zz*(-eps)**(j-1)) for j in range(1,J+1)]
            m=[ONE,scale(ph,-a)]+[ZERO]*(J-1)
            f=[ONE,scale(ph,eps)]+[ZERO]*(J-1)
            sq=[ONE]+[scale(power(ph,j),1-a*a) if j%2==0 else ZERO for j in range(1,J+1)]
            check(conv(m,h,J)==f,'local_mean_times_noise')
            check(conv(h,g,J)==[ONE]+[ZERO]*J,'local_noise_inverse')
            check(conv(sq,hm,J)==g,'local_inverse_square_factor')
            check(conv(f,g,J)==m,'local_coupled_deconvolution')
            for j in range(J+1):
                means_h[j]=add(means_h[j],scale(h[j],prob))
                means_g[j]=add(means_g[j],scale(g[j],prob))
        check(means_h==[ONE]+[ZERO]*J,'centered_noise_mean')
        sq=[ONE]+[scale(power(ph,j),1-a*a) if j%2==0 else ZERO for j in range(1,J+1)]
        check(means_g==sq,'inverse_noise_mean')
        # Independence of f and its inverse-noise factor destroys p^2 cancellation.
        if a<1 and ph!=ZERO:
            check(means_g[2]!=ZERO,'independence_false_substitution_detected')

# Actual prime ideals of Z[w]: roots mod 7,13 and the inert prime over 5.
PRIMES=[(7,2,7),(7,4,7),(13,3,13),(13,9,13),(5,None,25)]
NORMS=[p[2] for p in PRIMES]
def ffmul(x,y,p):
    a,b=x;c,d=y
    return ((a*c-b*d)%p,(a*d+b*c-b*d)%p)
def ffpow(x,n,p):
    out=(1,0)
    while n:
        if n&1:out=ffmul(out,x,p)
        x=ffmul(x,x,p);n//=2
    return out
def character(row,prime):
    p,r,q=prime;a,b=row
    if r is not None:
        x=(a+b*r)%p
        if x==0:return ZERO
        val=pow(x,(q-1)//6,p)
        for j in range(6):
            if pow((1+r)%p,j,p)==val:return ROOTS[j]
    else:
        x=(a%p,b%p)
        if x==(0,0):return ZERO
        val=ffpow(x,(q-1)//6,p)
        for j in range(6):
            if ffpow((1,1),j,p)==val:return ROOTS[j]
    raise RuntimeError('invalid sextic character')

def native_checks():
    rows=[(a,b) for a in range(-6,7) for b in range(-6,7) if 0<a*a-a*b+b*b<=13]
    check(len(rows)==54,'all_rows_norm13')
    for pr in PRIMES:
        p,r,q=pr
        residues=[(a,0) for a in range(p)] if r is not None else list(product(range(p),repeat=2))
        counts=Counter(character(x,pr) for x in residues)
        check(counts[ZERO]==1,'literal_zero_local')
        for rt in ROOTS:check(counts[rt]==(q-1)//6,'sextic_residue_coverage')
    signs=list(product([-1,1],repeat=5))
    masks=[None,0,4]
    ks=[1,2,3,4]
    flux_signs=Counter(); trajectory=None
    columns=[]
    for es in product([0,1],repeat=5):
        n=prod(q**e for q,e in zip(NORMS,es))
        if 1<n<=196:columns.append((es,n))
    for mask in masks:
        totals={k:[F(0) for _ in range(6)] for k in ks}
        for row in rows:
            chars=[character(row,pr) for pr in PRIMES]
            coeff=[]
            for es,n in columns:
                cc=ONE
                if mask is not None and es[mask]:cc=ZERO
                else:
                    for ch,e in zip(chars,es):
                        if e:cc=mul(cc,ch)
                coeff.append((es,cc))
            vals={s:total(scale(cc,prod(v**e for v,e in zip(s,es))) for es,cc in coeff) for s in signs}
            for k in ks:
                moments=[]
                for j in range(6):
                    legal=[s for s in signs if s[:j]==(-1,)*j]
                    mj=sum((norm(vals[s])**k for s in legal),F(0))/len(legal)
                    moments.append(mj);totals[k][j]+=mj
                check(moments[-1]==norm(vals[(-1,)*5])**k,'frozen_endpoint_native')
                direct_mu=total(scale(cc,(-1)**sum(es)) for es,cc in coeff)
                check(direct_mu==vals[(-1,)*5],'literal_mobius_endpoint')
                for j in range(5):
                    flux=F(0)
                    for tail in product([-1,1],repeat=4-j):
                        plus=(-1,)*j+(1,)+tail
                        minus=(-1,)*j+(-1,)+tail
                        U=scale(add(vals[plus],vals[minus]),F(1,2))
                        V=scale(sub(vals[plus],vals[minus]),F(1,2))
                        A=norm(U)+norm(V); B=2*real(mul(U,conj(V)))
                        diff=-sum((F(comb(k,l))*A**(k-l)*B**l for l in range(1,k+1,2)),F(0))
                        check(diff==(norm(vals[minus])**k-norm(vals[plus])**k)/2,'odd_binomial_flux')
                        if k==2:
                            check(diff==-4*A*real(mul(U,conj(V))),'fourth_flux_formula')
                        flux+=diff
                    flux/=2**(4-j)
                    check(flux==moments[j+1]-moments[j],'one_prime_freeze_increment')
                    flux_signs['positive' if flux>0 else 'negative' if flux<0 else 'zero']+=1
                check(sum((moments[j+1]-moments[j] for j in range(5)),F(0))==moments[-1]-moments[0],'full_signed_telescoping')
        if mask is None:trajectory={str(k):[str(x) for x in totals[k]] for k in ks}
    return {'prime_ideals':[{'rational_prime':p,'omega_root':r,'norm':q} for p,r,q in PRIMES],
            'row_count':len(rows),'squarefree_columns':len(columns),'column_norm_cap':196,
            'mask_cases':masks,'moment_orders':[2*k for k in ks],
            'flux_signs':dict(sorted(flux_signs.items())),
            'summed_native_freezing_trajectories':trajectory}

def centered_norm_checks():
    # Finite arbitrary coefficient sample, including repeated-prime radical groups.
    alpha=[F(1,3),F(1,2),F(0)]
    J=3; primes=[2,3,5]; X=120
    ns=[]
    for es in product(range(7),repeat=3):
        n=prod(p**e for p,e in zip(primes,es))
        if n<=X:ns.append((es,n))
    for noise in ['plus','minus']:
        B={}
        for es,n in ns:
            rad=tuple(int(e>0) for e in es)
            c=power(ROOT,n%6)
            for a,e in zip(alpha,es):
                if e:c=scale(c,a**(e-1) if noise=='plus' else -(-a)**(e-1))
            B[rad]=add(B.get(rad,ZERO),c)
        for k in [1,2,3]:
            lhs=F(0)
            for sig in product([-1,1],repeat=3):
                prob=prod((1-a*s)/2 for a,s in zip(alpha,sig))
                zz=[a+s for a,s in zip(alpha,sig)]
                val=total(scale(c,prod(v**e for v,e in zip(zz,rad))) for rad,c in B.items())
                lhs+=prob*norm(val)**k
            rhs=sum((F((4*(2*k-1))**sum(rad))*norm(c) for rad,c in B.items()),F(0))**k
            check(lhs<=rhs,'centered_hypercontractivity_sample')
    return len(ns)

def main():
    local_checks(); native=native_checks(); count=centered_norm_checks()
    result={'status':'PASS','arithmetic':'exact fractions in Q(omega), omega^2+omega+1=0',
            'scope':'finite algebra only; no asymptotic, pole, or RH certification',
            'checks':dict(sorted(COUNTS.items())),'total_checks':sum(COUNTS.values()),
            'radical_group_sample_ideals':count,'native':native}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
