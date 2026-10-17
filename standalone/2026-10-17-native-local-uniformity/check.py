#!/usr/bin/env python3
"""Exact finite diagnostics, not a verifier of the imported analytic theorem."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt, prod
import json

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--mutate', choices=['split', 'power', 'exclusion', 'owner', 'progression', 'jacobian'])
ARGS = PARSER.parse_args()
COUNTS: Counter[str] = Counter()

def check(ok: bool, name: str) -> None:
    COUNTS[name] += 1
    if not ok:
        raise RuntimeError('REJECT: ' + name)

def sieve(N: int):
    spf = list(range(N+1))
    for p in range(2, isqrt(N)+1):
        if spf[p] == p:
            for n in range(p*p, N+1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf, [p for p in range(2,N+1) if spf[p] == p]

def ideal_primes(N, ps):
    out=[]
    for p in ps:
        if p == 3:
            out.append((3,p,1,0))
        elif p % 3 == 1:
            out.extend([(p,p,1,0),(p,p,1,1)])
        elif p*p <= N:
            out.append((p*p,p,2,0))
    return sorted(out)

def phase(q, label, profile):
    return 1 if profile == 0 else (-1 if (q+label)%3 else 0)

def excluded(p,label,profile):
    return p in (2,3) or (profile == 1 and p == 7 and label == 0)

def local_scaled(q,label,p,m,family,N,profile,alter=False):
    """q**e * c(p**e), integer fixtures. Odd m uses b=q**(-1/2)*phase."""
    z=phase(q,label,profile)
    if excluded(p,label,profile):
        return {0:1} if not (alter and ARGS.mutate=='exclusion') else {0:1,1:-q}
    a=(m//2-1) if m%2==0 else ((m-3)//2)
    if alter and ARGS.mutate=='power':
        a += 1
    out={0:1}
    if family=='native':
        out[1]=-q
    elif family=='coupled':
        out[1]=-(q-1)
        if q**m<=N: out[m]=-z*q**(m+a)
    elif family=='two':
        out[1]=-q
        if q**m<=N: out[m]=-z*q**(m+a)
        if q**(m+1)<=N: out[m+1]=z*q**(m+1+a)
    else:
        j=0
        while q**(1+j*m)<=N:
            out[1+j*m]=-(q-1)*z**j*q**(j*(m+a))
            j+=1
    return {e:v for e,v in out.items() if q**e<=N}

def euler_census(N,m,family,profile,spf,ps):
    tables={}
    for q,p,f,label in ideal_primes(N,ps):
        if ARGS.mutate=='split' and f==1 and p!=3 and label==1:
            continue
        old=tables.get(p,{0:1})
        loc=local_scaled(q,label,p,m,family,N,profile,True)
        new=defaultdict(int)
        for e,v in old.items():
            for j,w in loc.items():
                if p**(e+f*j)<=N: new[e+f*j]+=v*w
        tables[p]=dict(new)
    ans=[0]*(N+1); ans[1]=1
    for n in range(2,N+1):
        p=spf[n]; r=n; e=0
        while r%p==0: r//=p; e+=1
        ans[n]=ans[r]*tables.get(p,{0:1}).get(e,0)
    return ans

def ideal_dfs_census(N,m,family,profile,ps):
    """Separate enumeration of every supported ideal, not one representative per norm."""
    ip=ideal_primes(N,ps); ans=[0]*(N+1); nodes=0
    tables=[]
    for q,p,f,label in ip:
        if excluded(p,label,profile): tables.append([]); continue
        z=phase(q,label,profile)
        a=(m-2)//2 if m%2==0 else (m-3)//2
        options=[]
        # Direct coefficient definition, distinct from the norm-Euler recurrence.
        for e in range(1, (N.bit_length()+1)):
            ne=q**e
            if ne>N: break
            v=0
            if family=='native': v=-1 if e==1 else 0
            elif family=='coupled':
                v=Q(-(q-1),q) if e==1 else (-z*q**a if e==m else 0)
            elif family=='two':
                v=-1 if e==1 else (-z*q**a if e==m else (z*q**a if e==m+1 else 0))
            elif (e-1)%m==0:
                j=(e-1)//m; v=Q(-(q-1),q)*(z*q**a)**j
            if v:
                scaled=v*ne
                check(scaled.denominator==1 if isinstance(scaled,Q) else True,'integer_fixture')
                options.append((ne,int(scaled)))
        tables.append(options)
    def walk(start,n,v):
        nonlocal nodes
        ans[n]+=v; nodes+=1
        for j in range(start,len(ip)):
            if ip[j][0]>N//n: break
            for ne,c in tables[j]:
                if ne>N//n: break
                walk(j+1,n*ne,v*c)
    walk(0,1,1)
    return ans,nodes

def mu_table(N,spf):
    mu=[0]*(N+1); mu[1]=1
    for n in range(2,N+1):
        p=spf[n]; r=n//p; mu[n]=0 if r%p==0 else -mu[r]
    return mu

NMAX=131072
SPF,PRIMES=sieve(NMAX)
CENSUS=[]
for family,m,profile in product(['native','coupled','two','geometric'],[2,3,6],[0,1]):
    N=4096
    e=euler_census(N,m,family,profile,SPF,PRIMES)
    d,nodes=ideal_dfs_census(N,m,family,profile,PRIMES)
    check(e==d,'complete_ideal_norm_census')
    CENSUS.append({'family':family,'m':m,'profile':profile,'cap':N,'ideals':nodes})
for family in ['native','coupled']:
    e=euler_census(NMAX,6,family,0,SPF,PRIMES)
    d,nodes=ideal_dfs_census(NMAX,6,family,0,PRIMES)
    check(e==d,'complete_ideal_norm_census')
    CENSUS.append({'family':family,'m':6,'profile':0,'cap':NMAX,'ideals':nodes})
    if family=='coupled':
        check(e[7**6]==-2*7**8,'first_sixth_power_both_conjugates')

# Full unmasked native norm identity, including the primes above 2 and 3.
N=20000; mu=mu_table(N,SPF); cv=[0]*(N+1)
chi=lambda n: 0 if n%3==0 else (1 if n%3==1 else -1)
for a in range(1,N+1):
    if mu[a]:
        for b in range(1,N//a+1): cv[a*b]+=mu[a]*mu[b]*chi(b)
truth=[0]*(N+1); truth[1]=1
for n in range(2,N+1):
    p=SPF[n]; r=n; e=0
    while r%p==0: r//=p; e+=1
    tab={0:1,1:-1} if p==3 else ({0:1,1:-2,2:1} if p%3==1 else {0:1,2:-1})
    truth[n]=truth[r]*tab.get(e,0)
check(truth==cv,'unmasked_mu_convolution_all_norms')

# Exact formal completion factors through degree 36.
def multiply(a,b,M):
    out=[Q(0)]*(M+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=M: out[i+j]+=x*y
    return out
M=36
for q,m,z,family in product([2,3,7,25],[2,4,6],[-1,Q(1,2),1],['coupled','two','geometric']):
    inv=[Q(1)]*(M+1); x=[Q(0),Q(1)]+[Q(0)]*(M-1)
    D=[Q(0)]*(M+1); D[m]=z*q**(m//2-1)
    one=[Q(1)]+[Q(0)]*M
    invD=one[:]
    for j in range(1,M//m+1): invD[j*m]=D[m]**j
    if family=='coupled':
        F=one[:]; F[1]=-1+Q(1,q); F[m]=-D[m]
        numer=[Q(0)]*(M+1); numer[1]=Q(1,q); numer[m]=-D[m]
        J=[a+b for a,b in zip(one,multiply(numer,inv,M))]
    elif family=='two':
        F=multiply([Q(1),Q(-1)],[a-b for a,b in zip(one,D)],M)
        J=[a-b for a,b in zip(one,D)]
    else:
        F=[a-(1-Q(1,q))*b for a,b in zip(one,multiply(x,invD,M))]
        inside=[a-b for a,b in zip([Q(1,q)]+[Q(0)]*M,D)]
        rest=multiply(multiply(x,inside,M),multiply(inv,invD,M),M)
        J=[a+b for a,b in zip(one,rest)]
    check(multiply([Q(1),Q(-1)],J,M)==F,'formal_completion_full_shared_factors')
for q in [4,9,25,49,121]:
    t=Q(1,isqrt(q)); rr=Q(1,q)
    masses=[(rr*t+rr)/(1-t),rr,2*rr*t/((1-t)*(1-rr))]
    check(all(v<=12*rr for v in masses),'critical_local_mass')
for q,m in product([16,81,625],[2,3,4,6,10,100]):
    rt=isqrt(isqrt(q)); t=Q(1,rt**3); rr=Q(1,q)
    coeff=Q(isqrt(q)**(m-2)); D=coeff*t**m
    masses=[(rr*t+D)/(1-t),D,t*(rr+D)/((1-t)*(1-D))]
    check(all(v<=10*Q(1,isqrt(q)**3) for v in masses),'three_quarter_local_mass')
check(2*Q(5,7)/((1-Q(5,7))*(1-Q(1,2)))<12,'small_norm_rational_gate')

# Congruence preimages retain gcds; no coprimality assumption on the dilation.
for a,mod in product(range(1,14),range(1,12)):
    for res in range(mod):
        direct=[b for b in range(31) if (a*b-res)%mod==0]
        g=gcd(a,mod)
        if res%g: got=[]
        else:
            step=mod//g
            root=(res//g*pow(a//g,-1,step))%step if step>1 else 0
            if ARGS.mutate=='progression': step=mod
            got=[b for b in range(31) if (b-root)%step==0]
        check(direct==got,'progression_preimage')

# Largest factor partition keeps caps, ties, repeated factors and phases.
smallmu=mu_table(6,SPF)
for r in range(1,5):
    for caps in [(0,40),(3,25),(7,18)]:
        direct=Counter(); split=Counter()
        for ds in product(range(1,7),repeat=r):
            n=prod(ds)
            groups=[prod(ds[j:j+2]) for j in range(0,r,2)]
            if not all(caps[0]<g<=caps[1] for g in groups): continue
            if not (10<n<=90) or n%3!=1: continue
            wt=prod(smallmu[d] for d in ds)
            direct[(n,(n*n+2*n)%5)]+=wt
            for j in range(r):
                own=all(ds[j]>=ds[i] for i in range(r))
                if ARGS.mutate!='owner': own=own and all(ds[j]>ds[i] for i in range(j))
                if own: split[(n,(n*n+2*n)%5)]+=wt
        check(direct==split,'unique_largest_owner_capped_tensor')

# Parameter margins for the entire permitted dilation range, in exact algebra.
for r in range(1,65):
    eps=Q(1,100*r); delta=eps/2; theta=1-Q(2,3*r)
    margin=theta+eps-Q(1,3)-delta-(1-Q(1,r))*(Q(2,3)-delta)
    check(margin==eps-delta/r and margin>0,'hyperbola_lower_margin')
    check(delta-eps<0,'hyperbola_upper_margin')

# Integral overlap identities, including the dilation Jacobian.
for L,d in product([Q(1,2),Q(3,2),Q(5),Q(8)],range(1,9)):
    for i,j in product(range(1,6),repeat=2):
        left=max(Q(0),L-d*abs(i-j))
        factor=d*d if ARGS.mutate=='jacobian' else d
        right=factor*max(Q(0),L/d-abs(i-j))
        check(left==right,'critical_dilation_jacobian')

REPORT={'status':'PASS_FINITE_DIAGNOSTICS_NOT_ANALYTIC_CERTIFICATION',
        'counts':dict(sorted(COUNTS.items())), 'census':CENSUS,
        'scope':{'native_norm_identity_cap':20000,'large_census_cap':NMAX,
                 'odd_m_profiles':'b_p is attenuated by q^(-1/2) to give exact rational fixtures',
                 'local_mass_q':'square/fourth-power algebra fixtures; not a list of prime ideals',
                 'independent_mathematical_review':False,'RH_proved':False,
                 'imported_MRSTT_reproved':False}}
print(json.dumps(REPORT,sort_keys=True,indent=2))
