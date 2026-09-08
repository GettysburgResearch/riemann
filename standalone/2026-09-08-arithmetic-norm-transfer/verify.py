#!/usr/bin/env python3
"""Bounded exact controls for ANT1--ANT5, not an RH or analytic proof checker."""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md','README.md','SYNTHESIS.md','SOURCES.json','VALIDATION.md',
         'verify.py','test_rejections.py','result.json','SHA256SUMS'}
PARENT = '31a35a90b0b924dc98a2c89c463fb59577f45a4e'
D = (1, -5, 8, -4)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def strict_json(path: Path):
    def unique(items):
        out = {}
        for k,v in items:
            require(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    def bad(s):
        raise ValueError('noninteger JSON numeric: ' + s)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique,
                      parse_float=bad, parse_constant=bad)


def exact_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(exact_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a)==len(b) and all(exact_equal(x,y) for x,y in zip(a,b))
    return a == b


def authenticate():
    require({p.name for p in ROOT.iterdir()} == FILES, 'file inventory')
    for p in ROOT.iterdir():
        require(p.is_file() and not p.is_symlink(), 'nonregular file')
    records = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name = line.split('  ',1)
        require(name not in records and name in FILES-{'SHA256SUMS'}, 'manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest), 'digest')
        records[name]=digest
    require(set(records)==FILES-{'SHA256SUMS'}, 'manifest coverage')
    for name,digest in records.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
                'checksum: '+name)
    sources = strict_json(ROOT/'SOURCES.json')
    require(sources['publication_parent']==PARENT, 'parent lock')
    require(sources['claim_of_exhaustive_review'] is False, 'review scope')
    require(sources['external_computations_replayed'] is False, 'external replay scope')


def factor(n):
    require(type(n) is int and n>=1, 'factor input')
    f = {}
    p=2
    while p*p<=n:
        while n%p==0:
            f[p]=f.get(p,0)+1
            n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f


def mobius(n):
    f=factor(n)
    return 0 if any(e>1 for e in f.values()) else (-1)**len(f)


def mu_sieve(N):
    mu=[1]*(N+1);mu[0]=0
    prime=[True]*(N+1)
    for p in range(2,N+1):
        if prime[p]:
            for n in range(p,N+1,p):
                mu[n]*=-1
                prime[n]=False
            for n in range(p*p,N+1,p*p):mu[n]=0
    return mu


def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def poly_power(a,k):
    out=[F(1)]
    for _ in range(k):out=poly_mul(out,a)
    return out


def poly_derivative(a):
    return [i*a[i] for i in range(1,len(a))]


def poly_at(a,x):
    val=F(0)
    for c in reversed(a):val=val*x+c
    return val


def variation(Y,d=D):
    out={}
    for j,c in enumerate(d):
        for n in range(Y,2*Y):
            require((2**j)*n not in out, 'overlapping dyadic blocks')
            out[(2**j)*n]=F(c*n,Y)
    return out


def S(a):return sum((v*v/F(n) for n,v in a.items()),F(0))


def floor_sum(a,x):
    return sum((v*(x//n) for n,v in a.items()),F(0))


def cell_energy(a,left,right):
    """Exact homogeneous norm on an arbitrary positive rational finite interval."""
    left=F(left);right=F(right)
    require(0<left<=right,'cell range')
    total=F(0);x=left
    while x<right:
        end=min(right,F(x.numerator//x.denominator+1))
        val=floor_sum(a,x)
        total+=val*val*(1/x-1/end)
        x=end
    return total


def graph_edges(a,N):
    out=defaultdict(F)
    for p in range(2,N+1):
        if factor(p)!={p:1}:continue
        k=p
        while k<=N:
            for j in range(1,N//k+1):
                diff=a.get(k*j,F(0))-a.get(j,F(0))
                out[p]+=diff*diff/F(k*j)
            k*=p
    return dict(out)


def graph_matrix(a,N):
    out=defaultdict(F)
    # Diagonal is log(n) + M(N/n), in a_n/sqrt(n) coordinates.
    for n,an in a.items():
        for p,k in factor(n).items():out[p]+=k*an*an/F(n)
        for r in range(2,N//n+1):
            fs=factor(r)
            if len(fs)==1:
                p=next(iter(fs));out[p]+=an*an/F(n*r)
    # Full off diagonal: enumerate index pairs, not a prime-power edge list.
    items=sorted(a.items())
    for j,aj in items:
        for n,an in items:
            if n<=j or n%j:continue
            r=n//j;fs=factor(r)
            if len(fs)==1:
                p=next(iter(fs));out[p]-=2*aj*an/F(n)
    return dict(out)


def clean(d):return {k:v for k,v in d.items() if v}


def H_direct(t):
    t=F(t)
    cuts={F(1),F(2)}
    for k in range(1,int(t)+1):
        x=t/k
        if 1<x<2:cuts.add(x)
    cuts=sorted(cuts);ans=F(0)
    for x,y in zip(cuts,cuts[1:]):
        mid=(x+y)/2
        ans+=(t//mid)*(y*y-x*x)/2
    return ans


def H_formula(t):
    t=F(t);U=int(t);L=int(t/2)
    return F(2*L)-F(U,2)+t*t*sum((F(1,k*k) for k in range(L+1,U+1)),F(0))/2


def profile_certificate(T=4096):
    h2=[F(0)]
    for k in range(1,T+1):h2.append(h2[-1]+F(1,k*k))
    low=F(0)
    for r in range(1,T):
        A=B=F(0)
        for j,d in enumerate(D):
            U=r//(2**j);L=r//(2**(j+1))
            A+=d*(h2[U]-h2[L])/F(2*4**j)
            B+=d*(F(2*L)-F(U,2))
        value=A*A*F(3*r*r+3*r+1,3)+2*A*B+B*B/F(r*(r+1))
        require(value>=0,'negative exact square integral')
        low+=value
    high=low+F(10000,3*T**3)
    scale=10**12
    a=(low.numerator*scale)//low.denominator
    b=-((-high.numerator*scale)//high.denominator)
    require(F(1704219450036,scale)<low<high<F(1704219498544,scale),
            'profile enclosure')
    # Fingerprints avoid converting enormous exact integers to decimal strings.
    encoded=(hex(low.numerator)+'/'+hex(low.denominator)).encode()
    return {'cutoff':T,'integrated_cells':T-1,
            'decimal_denominator':scale,'outward_numerators':[a,b],
            'exact_partial_sum_sha256':hashlib.sha256(encoded).hexdigest(),
            'tail_bound':[10000,3*T**3]}


def reconstruct():
    groups={}
    mus=mu_sieve(512)
    for n in range(1,513):require(mus[n]==mobius(n),'Mobius source')
    groups['independent_mobius_values']=512

    count=0
    for m in [F(-1),F(-1,3),F(0),F(1)]:
        for t in [F(-4),F(-1,2),F(0),F(4)]:
            for u in [F(-1),F(0),F(3,2)]:
                A=u-2*t;B=3*t-2*u-2*m;C=u+m-t
                require(A+B+C==-m and B+2*C==t and A+2*B+4*C==u,
                        'three-jet algebra')
                count+=1
    groups['three_constraint_algebra']=count

    count=0
    for r in range(2,5):
        for t in range(1,4):
            d=poly_mul(poly_power([F(1),F(-2)],r),poly_power([F(1),F(-1)],t))
            z=d
            for k in range(r):
                require(poly_at(z,F(1,2))==0,'safe derivative zero');z=poly_derivative(z)
            z=d
            for k in range(t):
                require(poly_at(z,F(1))==0,'centering derivative zero');z=poly_derivative(z)
            for Y in [2,3,7]:
                a=variation(Y,d)
                require(sum((c/F(n) for n,c in a.items()),F(0))==0,'balance')
                require(sum(a.values(),F(0))==0,'centering')
                expected=F(3*Y-1,2*Y)*sum((c*c/F(2**j) for j,c in enumerate(d)),F(0))
                require(S(a)==expected,'diagonal exact formula')
                count+=1
    groups['finite_jet_variations']=count
    require(poly_mul(poly_power([F(1),F(-2)],2),[F(1),F(-1)])==list(D),
            'explicit multiplier')

    count=0;maxN=0
    for Y in [2,3,4,5,8,12,16]:
        a=variation(Y);N=16*Y
        require(clean(graph_edges(a,N))==clean(graph_matrix(a,N)), 'prime-power graph identity')
        require(S(a)==F(63,2)*F(3*Y-1,2*Y),'explicit S')
        require(S(a)<F(189,4),'norm cap')
        require(max(abs(x) for x in a.values())<16,'coefficient cap')
        count+=1;maxN=max(maxN,N)
    groups['complete_formal_prime_log_graphs']=count

    count=0
    for Y in range(2,33):
        a=variation(Y)
        require(cell_energy(a,F(3*Y,2),2*Y)>=F(Y,24),'full low-interval lower bound')
        # An independent prefix: neither correction nor its three jets alters it.
        prefix={n:F(mobius(n)) for n in range(1,Y)}
        for j in range(1,Y):
            require(floor_sum(prefix,j)==1 and floor_sum(a,j)==0,'literal prefix')
        count+=1
    groups['physical_interval_lower_bounds']=count

    count=0
    for r in range(0,33):
        for frac in [F(0),F(1,4),F(3,4)]:
            x=r+frac
            require(H_direct(x)==H_formula(x),'continuum floor integral')
            count+=1
    require(sum(D)==0 and sum((F(d,2**j) for j,d in enumerate(D)),F(0))==0,
            'complete profile cancellations')
    require(sum(abs(d)*2**j for j,d in enumerate(D))==75,'profile tail constant')
    require(F(1,4)*(F(7,3)-2+F(1,2))==F(5,24),'profile positive range')
    groups['rational_continuum_profiles']=count

    # Exponents in the COMPLETE convexity-based low/high split.
    a=F(5,8)
    require(2-(a+1)==1-a==F(3,8),'frequency split exponent')
    require(F(2)*16**2==512 and F(24)*F(189,2)==2268,'norm transfer constants')
    require(F(3,2)*(12**2+2*21**2+4*8**2)==1923,'completion diagonal constant')
    groups['exact_budget_identities']=4

    certificate=profile_certificate()
    return {
        'status':'PROPOSED_COMPONENT_PROOFS_INDEPENDENT_REVIEW_REQUIRED',
        'rh_proved':False,
        'fixed_power_saving_proved':False,
        'new_native_minimum_computed':False,
        'analytic_theorems_machine_verified':False,
        'native_bound':'E(p_Y^c) << Y exp(-c (log Y)^(3/5) (log log Y)^(-1/5))',
        'sharp_variation_transfer':'Gamma(Y) is of order Y/log Y',
        'parent':PARENT,
        'groups':groups,
        'bounded_panels':sum(groups.values()),
        'maximum_graph_source_integer':maxN,
        'profile_certificate':certificate,
        'imports_not_replayed':['Lee--Leong Theorem 1.2','classical zeta convexity'],
        'scope':'No numerical zeta or zero data, no numerical contour, no parent code executed.'
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',type=Path)
    parser.add_argument('--emit',action='store_true')
    args=parser.parse_args()
    if args.check:
        authenticate()
    data=reconstruct()
    if args.check:
        require(exact_equal(data,strict_json(args.check.resolve())),'reconstruction mismatch')
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=='__main__':
    try: main()
    except Exception as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
