#!/usr/bin/env python3
"""Bounded exact reconstruction for CGG26. Finite checks are not an RH proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAMES = {'PROOF.md','README.md','REVIEW_AND_SOURCES.md','SOURCE_LOCK.json',
         'VALIDATION.md','check.py','test_check.py','verification.json','SHA256SUMS'}
BASE = 'f99d9e3908dde4865377c75d9ca051c1f545bf4f'
PARENT = 'f782788933dc21a0fe6a844950f5ca532eba7d86'
LOCK_HASH = '8434e3497cd7d84237776d15a150d34d3ea074e4c0f3443edd7bf0b3a959380a'
Q = 1 << 160


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)


def canonical(x: object) -> str:
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def reject_number(s: str):
    raise ValueError('noninteger JSON number: '+s)


def pairs(items):
    d = {}
    for k,v in items:
        require(k not in d, 'duplicate key')
        d[k] = v
    return d


def read_json(path: Path):
    require(path.is_file() and not path.is_symlink(), 'not a regular receipt')
    require(path.stat().st_size < 200000, 'oversized receipt')
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=reject_number, parse_constant=reject_number)


def rational_tag(x: F):
    require(type(x) is F, 'nonrational derived value')
    s = format(x.numerator, 'x')+'/'+format(x.denominator, 'x')
    return {'sha256':hashlib.sha256(s.encode()).hexdigest(),
            'numerator_bits':abs(x.numerator).bit_length(),
            'denominator_bits':x.denominator.bit_length()}


@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __post_init__(self):
        require(type(self.lo) is int and type(self.hi) is int and self.lo<=self.hi,
                'bad interval')
    @staticmethod
    def of(x):
        if isinstance(x, I): return x
        require(type(x) in (int,F), 'nonexact interval input')
        x = F(x)
        return I((x.numerator*Q)//x.denominator,
                 -((-x.numerator*Q)//x.denominator))
    def __add__(self, other):
        o=I.of(other); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self, other): return self+-I.of(other)
    def __rsub__(self, other): return I.of(other)+-self
    def __mul__(self, other):
        o=I.of(other); a=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(a)//Q,-((-max(a))//Q))
    __rmul__=__mul__
    def inv(self):
        require(not self.lo<=0<=self.hi,'inverse through zero')
        return I((Q*Q)//self.hi,-((-Q*Q)//self.lo))
    def __truediv__(self, other): return self*I.of(other).inv()
    def __rtruediv__(self, other): return I.of(other)*self.inv()
    def record(self):
        return {'lo_hex':format(self.lo,'x'),'hi_hex':format(self.hi,'x'),'bits':160}
    def decimal(self, digits=12):
        scale=10**digits
        lo=(self.lo*scale)//Q; hi=-((-self.hi*scale)//Q)
        def text(n):
            sign='-' if n<0 else ''; a=abs(n)
            return sign+str(a//scale)+'.'+str(a%scale).zfill(digits)
        return [text(lo),text(hi)]


@lru_cache(None)
def log_bounds(n: int) -> I:
    require(type(n) is int and n>=1,'log domain')
    def atanh(z):
        s=F(0); power=z; zz=z*z
        for j in range(80):
            s+=power/(2*j+1); power*=zz
        return 2*s, 2*power/(161*(1-zz))
    k=n.bit_length()-1; m=1<<k
    l2,r2=atanh(F(1,3)); lr,rr=atanh(F(n-m,n+m))
    lo=k*l2+lr; hi=lo+k*r2+rr
    return I(I.of(lo).lo,I.of(hi).hi)


def primes_sieve(n: int):
    a=[True]*(n+1);a[0:2]=[False,False]
    for p in range(2,isqrt(n)+1):
        if a[p]:
            for j in range(p*p,n+1,p):a[j]=False
    return [j for j in range(2,n+1) if a[j]]


def prime_trial(n: int):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def box(ps):
    out=[1]
    for p in ps: out += [p*n for n in out]
    return sorted(out)


def mass(ps):
    z=F(1)
    for p in ps:z*=F(p+1,p)
    return z


def modes(ps, rates):
    out=[((),F(1),F(0))]
    for p in ps:
        out += [(D+(p,),b/p,a+F(p+1,p)*rates[p]) for D,b,a in out]
    return out[1:]


def inner(x,y,S):return sum((x[n]*y[n]/n for n in S), F(0))
def mean(x,S):return sum((x[n]/n for n in S),F(0))/sum((F(1,n) for n in S),F(0))
def variance(x,S):
    m=mean(x,S);return sum(((x[n]-m)**2/n for n in S),F(0))


def energies(x,es,rates):
    return sum((rates[p]/n*(x[n]-x[j])**2 for j,n,p in es),F(0))


def root_profile(ps,rates):
    ms=modes(ps,rates);G=sum((b/a for D,b,a in ms),F(0));H=sum((b/a**2 for D,b,a in ms),F(0))
    vals={}
    for n in box(ps):
        K=F(0)
        for D,b,a in ms:
            c=F(1)
            for p in D:c*= -1 if n%p==0 else F(1,p)
            K+=c/a
        vals[n]=1-K/G
    return vals,G,H


def psd_ldl(M):
    a=[row[:] for row in M];piv=[]
    for i in range(len(a)):
        d=a[i][i];require(d>=0,'negative exact LDL pivot');piv.append(d)
        if d==0:
            require(all(a[j][i]==0 for j in range(i+1,len(a))), 'zero-pivot offdiagonal')
            continue
        for j in range(i+1,len(a)):
            for k in range(j,len(a)):
                a[k][j]-=a[j][i]*a[k][i]/d
                a[j][k]=a[k][j]
    return {'dimension':len(a),'positive':sum(d>0 for d in piv),'zero':sum(d==0 for d in piv),
            'pivots_sha256':hashlib.sha256(canonical([rational_tag(d) for d in piv]).encode()).hexdigest()}


def small_graph(A,B):
    SA,SB=box(A),box(B);S=sorted(set(SA)|set(SB));za,zb=mass(A),mass(B);z=za+zb-1
    rates={p:F(p+2,p+1) for p in A+B}  # FORMAL positive rational log rates only.
    coord=sorted([(n,p*n,p) for ps,ss in [(A,SA),(B,SB)] for p in ps for n in ss if n%p])
    # Independent pair-ratio graph; avoids trusting the product-edge generator.
    pair=[]
    for j,n in combinations(S,2):
        if n%j==0 and prime_trial(n//j):pair.append((j,n,n//j))
    require(coord==sorted(pair),'edge inventory mismatch')
    require(set(SA)&set(SB)=={1} and sum((F(1,n) for n in S),F(0))==z,'root mass')
    g=min(F(p+1,p)*rates[p] for p in A+B)
    fa,ga,ha=root_profile(A,rates);fb,gb,hb=root_profile(B,rates)
    f={n:fa.get(n,F(0)) for n in S}
    E=energies(f,pair,rates);v=variance(f,S)
    target=ha/ga+ga*(zb-1)/z
    require(f[1]==0 and mean(f,SA)==1 and all(f[n]==0 for n in SB),'trial root/mean')
    require(v/E==target,'exact Rayleigh mismatch')
    upper=1/g+(zb*ga+za*gb)/(za+zb)
    require(target<=upper,'trial exceeds gluing upper')
    identities=0
    for seed in range(1,5):
        f={n:F(((n*seed+3)%11)-5,seed+1) for n in S};f={n:x-f[1] for n,x in f.items()}
        a,b=mean(f,SA),mean(f,SB)
        rhs=variance(f,SA)+variance(f,SB)+za*zb/(za+zb)*(a-b)**2-(za*a+zb*b)**2/(z*(za+zb))
        require(variance(f,S)==rhs,'variance root correction')
        require(variance(f,S)<=energies(f,pair,rates)/g+za*zb/(za+zb)*(a-b)**2,'contrast bound')
        identities+=1
    # Exact compression to the simultaneous global-mean/branch-contrast kernel.
    qa=A[0]; qb=B[0]
    rest=[n for n in S if n not in (qa,qb)]
    w={n:F(1,n) for n in S}
    ell={n:(F(1,za) if n in SA else 0)-(F(1,zb) if n in SB else 0) for n in S}
    det=w[qa]*w[qb]*(ell[qb]-ell[qa]);require(det!=0,'dependent constraints')
    basis=[]
    for n in rest:
        vec={k:F(0) for k in S};vec[n]=F(1)
        rhs0=-w[n];rhs1=-w[n]*ell[n]
        vec[qa]=(rhs0*w[qb]*ell[qb]-w[qb]*rhs1)/det
        vec[qb]=(w[qa]*rhs1-rhs0*w[qa]*ell[qa])/det
        require(sum(vec[k]*w[k] for k in S)==0 and sum(vec[k]*w[k]*ell[k] for k in S)==0,'constraint solve')
        basis.append(vec)
    def bilin(x,y):
        return sum((rates[p]/n*(x[n]-x[j])*(y[n]-y[j]) for j,n,p in pair),F(0))-g*inner(x,y,S)
    M=[[bilin(x,y) for y in basis] for x in basis]
    return {'A':A,'B':B,'vertices':len(S),'edges':len(pair),'variance_identities':identities,
            'formal_rates':{str(p):[rates[p].numerator,rates[p].denominator] for p in A+B},
            'rayleigh':rational_tag(target),'upper':rational_tag(upper),'complement_ldl':psd_ldl(M)}


def actual_case(y,ps):
    A=[p for p in ps if p<=y];za=mass(A);zb=F(1);B=[];previous=zb
    for p in ps:
        if p<=y:continue
        previous=zb;zb*=F(p+1,p);B.append(p)
        if zb>=za:break
    require(zb>=za and previous<za,'first crossing not covered')
    require(zb<za*F(B[-1]+1,B[-1]),'overshoot')
    # Fixed rational trial, source primes unchanged.
    rates={p:F(log_bounds(p).lo*(1<<32)//Q,1<<32) for p in A}
    ms=modes(A,rates);G0=sum((b/a for D,b,a in ms),F(0));H0=sum((b/a**2 for D,b,a in ms),F(0))
    numerator=H0/G0**2+(zb-1)/(za+zb-1)
    E0=I.of(0);GA=I.of(0)
    for D,b,a0 in ms:
        a=sum((F(p+1,p)*log_bounds(p) for p in D),I.of(0))
        E0+=I.of(b/(G0*a0)**2)*a
        GA+=I.of(b)/a
    witness=I.of(numerator)/E0
    g0=F(3,2)*log_bounds(2)
    upper=1/g0+(I.of(zb)*GA+I.of(za*(zb-1))/log_bounds(B[0]))/(za+zb)
    require(witness.lo>Q and witness.hi<upper.lo,'actual bracket/gap bound')
    if y==2:
        exact=I.of(F(16,21))/log_bounds(2)
        require(max(witness.lo,exact.lo)<=min(witness.hi,exact.hi),'five-vertex exact quotient')
    return {'y':y,'P':B[-1],'A':A,'B_prime_count':len(B),
            'B_primes_sha256':hashlib.sha256(canonical(B).encode()).hexdigest(),
            'full_vertex_count_formula':f'2^{len(A)}+2^{len(B)}-1',
            'enumerated_A_nonconstant_modes':len(ms),'enumerated_B_vertices':False,
            'Z_A':[za.numerator,za.denominator],'Z_B':rational_tag(zb),
            'trial_log_rates':{str(p):[rates[p].numerator,rates[p].denominator] for p in A},
            'rayleigh_lower_witness':witness.record(),'witness_decimal':witness.decimal(),
            'theorem_upper_enclosure':upper.record(),'upper_decimal':upper.decimal(),
            'actual_A_capacity':GA.record()}


def reconstruct():
    ps=primes_sieve(16384)
    other=[n for n in range(2,16385) if prime_trial(n)]
    require(ps==other,'primitive prime disagreement')
    for n in [2,3,5,7,11,13,17,31]:
        a=log_bounds(n);require(a.lo>0 and a.lo<=a.hi,'log certificate')
        # Log values are positive and do not rely on a float oracle.
    panels=[([2],[3]),([2],[3,5]),([2,3],[5,7]),([2,5],[3,7]),
            ([2,3,5],[7,11]),([2,3,5],[7,11,13]),([2,3,5,7],[11,13,17,19])]
    graphs=[small_graph(A,B) for A,B in panels]
    cases=[actual_case(y,ps) for y in [2,3,5,7,11,13]]
    return {'schema':'CGG26-1','rh_proved':False,'asymptotic_verified_by_finite_checks':False,
            'source':{'base':BASE,'box_capacity_parent':PARENT},
            'primitive':{'range_end':16384,'prime_count':len(ps),'methods':['eratosthenes','trial_division']},
            'formal_graph_panels':graphs,'actual_log_prime_rayleigh_certificates':cases,
            'interpretation':'Rayleigh lower witnesses plus analytic upper bounds; not computed true eigenvalues or an RH bound.'}


def authenticate():
    names={p.name for p in ROOT.iterdir()}
    require(names==NAMES,'packet inventory')
    require(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in NAMES),'packet regular files')
    lines=(ROOT/'SHA256SUMS').read_text().splitlines(); entries={}
    for line in lines:
        parts=line.split('  ');require(len(parts)==2,'manifest syntax');h,n=parts
        require(n not in entries and len(h)==64 and all(c in '0123456789abcdef' for c in h),'manifest entry')
        entries[n]=h
    require(set(entries)==NAMES-{'SHA256SUMS'},'manifest exact coverage')
    for n,h in entries.items():require(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'hash '+n)
    require(hashlib.sha256((ROOT/'SOURCE_LOCK.json').read_bytes()).hexdigest()==LOCK_HASH,'complete source-lock bytes')
    lock=read_json(ROOT/'SOURCE_LOCK.json')
    require(lock['base_main']==BASE and lock['sources'][0]['commit']==PARENT,'source lock')


def main():
    ap=argparse.ArgumentParser();group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true',help='untrusted producer output; no acceptance')
    group.add_argument('--check',type=Path)
    ns=ap.parse_args()
    if ns.emit:
        print(json.dumps(reconstruct(),sort_keys=True,indent=2));return
    authenticate();expected=read_json(ns.check);actual=reconstruct()
    require(canonical(expected)==canonical(actual),'primitive reconstruction mismatch')
    print('PASS_CGG26_BOUNDED '+hashlib.sha256(canonical(actual).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,TypeError,OSError,ZeroDivisionError) as exc:
        raise SystemExit('REJECT_CGG26: '+str(exc))
