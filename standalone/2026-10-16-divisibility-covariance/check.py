#!/usr/bin/env python3
"""Exact finite diagnostics. These tests do not certify analytic asymptotics."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import subprocess
import sys

ZERO=(F(0),F(0)); ONE=(F(1),F(0))
EPS=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
COUNTS=Counter()
MUTATION=""

def require(ok: bool, category: str, detail: object="") -> None:
    COUNTS[category]+=1
    if not ok:
        raise ValueError(f"FAIL {category}: {detail}")

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1],-x[1])
def scale(x,t): return (x[0]*t,x[1]*t)
def norm(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def power(x,k):
    out=ONE
    while k:
        if k&1: out=mul(out,x)
        x=mul(x,x); k//=2
    return out

def mulmod(x,y,p):
    a,b=mul(x,y); return int(a)%p,int(b)%p

def powmod(x,k,p):
    out=(1,0)
    while k:
        if k&1: out=mulmod(out,x,p)
        x=mulmod(x,x,p); k//=2
    return out

# Prime IDEAL labels: the two split ideals over 7 remain distinct.
PRIMES=(("7a",7,7,2),("7b",7,7,4),("25",25,5,None))

def chi(u, prime):
    name,q,p,r=prime
    if r is None:
        z=(u[0]%p,u[1]%p)
        if z==(0,0): return ZERO
        z=powmod(z,(q-1)//6,p)
        for e in EPS:
            if z==(e[0]%p,e[1]%p): return tuple(map(F,e))
    else:
        z=(u[0]+r*u[1])%p
        if not z: return ZERO
        z=pow(z,(q-1)//6,p)
        for e in EPS:
            if z==(e[0]+r*e[1])%p: return tuple(map(F,e))
    raise ValueError("residue does not identify a sixth root")

def local(e,m,q,a,b):
    if e==0: return ONE
    if MUTATION=="erase-mask":
        if a==ZERO: a=ONE
        if b==ZERO: b=ONE
    if e==1:
        return scale(a,F(q-1,q)*(1 if MUTATION=="wrong-prime-sign" else -1))
    if e==m:
        require(m%2==0,"even_fixture_degree")
        return scale(b,-q**(m//2-1+(MUTATION=="wrong-power-weight")))
    return ZERO

def coeff(es,m,phases):
    z=ONE
    for e,pr,(a,b) in zip(es,PRIMES,phases): z=mul(z,local(e,m,pr[1],a,b))
    return z

def predicted_pair(es,fs,m,phases):
    """Independent gcd/core construction, including the forced p at gap m-1."""
    gamma=ONE; d=F(1)
    for e,f,pr,(a,b) in zip(es,fs,PRIMES,phases):
        q=pr[1]
        if e==f:
            if e==0: value=F(1)
            elif e==1: value=F((q-1)**2,q*q)*norm(a)
            elif e==m: value=F(q**(m-2))*norm(b)
            else: return ZERO
            d*=value
            continue
        gap=abs(e-f); g=min(e,f)
        if gap==1 and g==0: z=scale(a,-F(q-1,q))
        elif gap==m and g==0: z=scale(b,-q**(m//2-1))
        elif gap==m-1 and g==1:
            if MUTATION=="drop-middle-channel": return ZERO
            z=scale(mul(b,conj(a)),F(q-1,q)*q**(m//2-1))
        else: return ZERO
        gamma=mul(gamma,z if e>f else conj(z))
    return scale(gamma,d)

def spf_table(n):
    s=list(range(n+1))
    if n>=1:s[1]=1
    for p in range(2,math.isqrt(n)+1):
        if s[p]==p:
            for j in range(p*p,n+1,p):
                if s[j]==j:s[j]=p
    return s

def convolution(a,b):
    z={}
    for i,x in a.items():
        for j,y in b.items():z[i+j]=z.get(i+j,0)+x*y
    return z

def norm_series(n,m,*,squarefree=False,excluded=()):
    """n^2 times the sum of |c_m(I)|^2 over ALL good K-ideals of norm n."""
    spf=spf_table(n); out=[0]*(n+1);out[1]=1; polys={}
    excluded=set(excluded)
    for p in range(2,n+1):
        if spf[p]!=p:continue
        if p in (2,3):polys[p]={0:1};continue
        if p%3==1:
            count=2-sum((p,j) in excluded for j in (0,1));q=p;f=1
        else:
            count=1-int((p,0) in excluded);q=p*p;f=2
        base={0:1,f:(q-1)**2}
        if not squarefree:base[m*f]=q**(3*m-2)
        poly={0:1}
        for _ in range(count):poly=convolution(poly,base)
        polys[p]=poly
    for x in range(2,n+1):
        p=spf[x];r=x;e=0
        while r%p==0:r//=p;e+=1
        out[x]=out[r]*polys[p].get(e,0)
    return out

def sqfree_ideals(limit):
    """Complete good squarefree ideals through limit, as labeled prime supports."""
    spf=spf_table(limit);pr=[]
    for p in range(5,limit+1):
        if spf[p]!=p:continue
        if p%3==1:pr.extend([((p,0),p),((p,1),p)])
        elif p*p<=limit:pr.append(((p,0),p*p))
    pr.sort(key=lambda x:(x[1],x[0])); ideals=[(1,())]
    for label,q in pr:
        ideals.extend((v*q,s+(label,)) for v,s in tuple(ideals) if v*q<=limit)
    return ideals

def introot(n,m):
    lo=0;hi=n+1
    while hi-lo>1:
        md=(hi+lo)//2
        if md**m<=n:lo=md
        else:hi=md
    return lo

def poly3_mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(t+u for t,u in zip(i,j));c[k]=c.get(k,0)+x*y
    return {k:v for k,v in c.items() if v}

def run(cap):
    # Independent exact root basis: epsilon=1+omega, not omega.
    for j,e in enumerate(EPS):
        require(power((F(1),F(1)),j)==tuple(map(F,e)),"sixth_root_basis",j)
        require(norm(e)==1,"unit_norm",j)
    rows=[(a,b) for a in range(-5,6) for b in range(-5,6) if 0<a*a-a*b+b*b<=13]
    require(len(rows)==54,"complete_small_row_count",len(rows))
    for u in rows:
        for pr in PRIMES:
            z=chi(u,pr)
            require(norm(z) in (0,1),"literal_local_mask",(u,pr[0]))
            if z!=ZERO:require(power(z,6)==ONE,"literal_character_order",(u,pr[0]))
    require(any(chi(u,PRIMES[0])!=chi(u,PRIMES[1]) for u in rows),"conjugate_ideals_distinct")
    explicit_prime_signs=[]
    for m in (4,6,8):
        exps=list(product((0,1,m),repeat=3))
        use_rows=rows if m==6 else rows[:7]+[(1,0)]
        for u in use_rows:
            phases=[]
            for j,pr in enumerate(PRIMES):
                a=chi(u,pr);b=mul(EPS[(j+1)%6],power(a,m));phases.append((a,b))
                if a==ZERO:require(local(1,m,pr[1],a,b)==ZERO and local(m,m,pr[1],a,b)==ZERO,"masked_channels",(m,u,j))
            cs=[coeff(e,m,phases) for e in exps]
            for i,e in enumerate(exps):
                for j,f in enumerate(exps):
                    require(mul(cs[i],conj(cs[j]))==predicted_pair(e,f,m,phases),"complete_finite_gcd_pairs",(m,u,e,f))
            for j,pr in enumerate(PRIMES):
                for hs in product((0,1,m),repeat=2):
                    h=list(hs);h.insert(j,0);n=h.copy();n[j]=1
                    got=mul(coeff(n,m,phases),conj(coeff(h,m,phases)))
                    want=scale(phases[j][0],-F(pr[1]-1,pr[1])*norm(coeff(h,m,phases)))
                    require(got==want,"prime_quotient_pairs",(m,u,j,h))
                    if u==(1,0) and all(x==0 for x in h):
                        require(got[1]==0 and got[0]<0,"principal_negative_sign",(m,j))
                        explicit_prime_signs.append([m,pr[0],str(got[0])])
    # Full local difference classification, including zero coefficients.
    for m in range(3,13):
        allowed={0,1,m}
        for e in range(m+2):
            for f in range(m+2):
                predicted=(e==f and e in allowed) or (abs(e-f)==1 and min(e,f)==0) or (abs(e-f)==m and min(e,f)==0) or (abs(e-f)==m-1 and min(e,f)==1)
                require(predicted==(e in allowed and f in allowed),"full_local_support",(m,e,f))
        for q in (7,13,25,49):
            # Squared normalized constants avoid irrational critical weights.
            require(F((q-1)**2,q**3)<=1 and F(1,q*q)<=1 and F((q-1)**2,q**5)<=1,"uniform_normalized_core",(m,q))
            require(F(q**(m-2),q**m)==F(1,q*q),"density_independent_degree",(m,q))
            alpha=F(m-1,m);sigma=1-F(3,2*m)
            require(alpha-sigma==F(1,2*m),"pole_contour_gap",m)
            require(m*alpha-m+2==1,"secondary_pole_location",m)
            for delta in (F(1,1000),F(1,100)):
                require(m*(alpha+delta)-m+2-1==m*delta,"residue_derivative_factor",(m,delta))
    # Exact multivariate Euler-polynomial cancellation.
    one={(0,0,0):1};one_minus_a={**one,(1,0,0):-1};one_minus_b={**one,(0,1,0):-1}
    qpoly={**one,(1,0,1):1,(0,1,0):1}
    expanded=poly3_mul(poly3_mul(one_minus_a,one_minus_b),qpoly);expanded.pop((0,0,0))
    expected={(1,0,1):1,(1,0,0):-1,(2,0,1):-1,(1,1,1):-1,(0,2,0):-1,(2,1,1):1,(1,2,0):1}
    require(expanded==expected,"two_pole_euler_polynomial")
    # Rational proof that four literal split prime ideals overpay the diagonal.
    require(F(8,3)**2>7 and F(11,3)**2>13,"four_prime_square_root_bounds")
    for x,lower in ((F(2),7),(F(8,3),13)):
        require(sum(x**j/F(math.factorial(j)) for j in range(6))>lower,"four_prime_log_bounds",x)
    for x,upper in ((F(1,2),F(5,3)),(F(8,9),F(5,2))):
        bound=sum(x**j/F(math.factorial(j)) for j in range(4))+(x**4/F(24))/(1-x/F(5))
        require(bound<upper,"four_prime_exponential_bounds",x)
    four_lower=4*(F(1323,7720)+F(6084,64735))
    require(four_lower==F(26522577,24987710) and four_lower>F(21,20),"forced_positive_remainder_margin")
    # Complete norm fibers, independently reconstructed via r*d^m with (r,d)=1.
    census=[]
    for m in (3,4,6,8):
        direct=norm_series(cap,m); rebuilt=[0]*(cap+1)
        ds=sqfree_ideals(introot(cap,m))
        for nd,support in ds:
            dscale=nd**m
            sf=norm_series(cap//dscale,m,squarefree=True,excluded=support)
            factor=nd**(3*m-2)
            for nr in range(1,len(sf)):rebuilt[nr*dscale]+=sf[nr]*factor
        mismatch=next((i for i in range(1,cap+1) if direct[i]!=rebuilt[i]),None)
        require(mismatch is None,"complete_norm_fiber_reconstruction",(m,mismatch))
        if m==6 and cap>=7**6:
            require(direct[7**6]==2*7**(3*m-2),"first_powerful_conjugate_fiber")
        digest=hashlib.sha256("\n".join(map(str,direct[1:])).encode()).hexdigest()
        census.append({"m":m,"all_norms_through":cap,"squarefree_power_factors":len(ds),"nonzero_norm_fibers":sum(x!=0 for x in direct[1:]),"scaled_integer_sha256":digest})
    return {"status":"PASS","scope":"Finite exact algebra and full stated norm-fiber reconstructions, not analytic certification", "prime_ideal_norms":[7,7,25],"physical_rows":54,"m6_pair_column_set":"all 27 exponent-0/1/6 ideals in the three-prime semigroup; not all K-ideals below a common cap", "m4_m8_rows":"first seven enumerated rows plus (1,0)", "predicate_counts":dict(sorted(COUNTS.items())),"principal_prime_sign_samples":explicit_prime_signs,"complete_norm_census":census}

def main():
    p=argparse.ArgumentParser();p.add_argument("--cap",type=int,default=200000)
    p.add_argument("--mutate",choices=("wrong-prime-sign","drop-middle-channel","erase-mask","wrong-power-weight"),default="")
    p.add_argument("--write",type=Path);args=p.parse_args()
    if args.cap<1:raise ValueError("cap must be positive")
    global MUTATION;MUTATION=args.mutate
    report=run(args.cap);text=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.write:args.write.write_text(text)
    else:sys.stdout.write(text)

if __name__=="__main__": main()
