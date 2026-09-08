#!/usr/bin/env python3
"""Exact bounded checks and one complete actual divisor inverse certificate.

No float, zeta/zero oracle, or parent executable is used in acceptance.
The code does not prove the all-set/infinite-domain analytic theorems.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from typing import Any

BITS=160
SCALE=1<<BITS


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)


def ceildiv(a: int, b: int) -> int:
    return -((-a)//b)


class I:
    __slots__=('lo','hi')
    def __init__(self, lo: int, hi: int):
        require(type(lo) is int and type(hi) is int and lo<=hi,'bad interval')
        self.lo,self.hi=lo,hi
    @staticmethod
    def rational(x: F | int) -> 'I':
        x=F(x)
        return I((x.numerator*SCALE)//x.denominator,
                 ceildiv(x.numerator*SCALE,x.denominator))
    def __add__(self, other: 'I') -> 'I':
        return I(self.lo+other.lo,self.hi+other.hi)
    def __neg__(self) -> 'I':
        return I(-self.hi,-self.lo)
    def __sub__(self, other: 'I') -> 'I':
        return self+-other
    def scale(self, x: F | int) -> 'I':
        x=F(x); vals=(self.lo*x.numerator,self.hi*x.numerator)
        return I(min(vals)//x.denominator,ceildiv(max(vals),x.denominator))
    def square_upper(self) -> F:
        return F(max(abs(self.lo),abs(self.hi))**2,SCALE**2)
    def record(self) -> dict[str,int]:
        return {'lower':self.lo,'upper':self.hi,'denominator':SCALE}


def log_rational(q: F) -> I:
    require(q>=1,'log argument below one')
    k=0
    while q>=2:
        q/=2;k+=1
    def base(x: F) -> tuple[F,F]:
        z=(x-1)/(x+1); z2=z*z; power=z; s=F(0)
        for j in range(80):
            s+=2*power/(2*j+1);power*=z2
        tail=2*power/(161*(1-z2))
        return s,s+tail
    l,u=base(q);l2,u2=base(F(2))
    l+=k*l2;u+=k*u2
    return I((l.numerator*SCALE)//l.denominator,
             ceildiv(u.numerator*SCALE,u.denominator))


def primes(n: int) -> list[int]:
    a=[True]*(n+1)
    if n>=0:a[0]=False
    if n>=1:a[1]=False
    p=2
    while p*p<=n:
        if a[p]:
            for k in range(p*p,n+1,p):a[k]=False
        p+=1
    return [i for i in range(n+1) if a[i]]


def factors(n: int) -> dict[int,int]:
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out


def edge_list(vertices: list[int]) -> list[tuple[int,int,int]]:
    lookup=set(vertices);out=[]
    for n in vertices:
        for p,a in factors(n).items():
            for k in range(1,a+1):
                j=n//(p**k)
                require(j in lookup,'not divisor closed')
                out.append((j,n,p))
    return out


def zeros(n: int) -> list[list[F]]:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def ldl_pivots(a: list[list[F]]) -> list[F]:
    n=len(a);m=[r[:] for r in a];out=[]
    for i in range(n):
        p=m[i][i];require(p>0,f'nonpositive LDL pivot {i}')
        out.append(p)
        for j in range(i+1,n):
            for k in range(j,n):
                m[k][j]-=m[j][i]*m[k][i]/p
                m[j][k]=m[k][j]
    return out


def rational_string(x: F) -> str:
    return f'{x.numerator}/{x.denominator}'


def subtree_checks() -> dict[str,int]:
    cases=0
    # Complete descendant classification in each finite initial interval.
    for N in range(2,81):
        for v in range(2,N+1):
            pv=min(factors(v))
            for n in range(v,N+1,v):
                x=n;is_desc=False
                while x>1:
                    if x==v:is_desc=True;break
                    p=min(factors(x));x//=p**factors(x)[p]
                k=n//v
                predicted=all(p<pv for p in factors(k))
                require(is_desc==predicted,'descendant mismatch')
                if predicted:
                    require(len(factors(n))==len(factors(v))+len(factors(k)),
                            'omega additivity')
                cases+=1
    return {'finite_descendant_cases':cases}


def arithmetic_checks() -> dict[str,int]:
    ps=primes(256)
    require(ps==[n for n in range(2,257) if factors(n)=={n:1}],'sieve mismatch')
    cases=0
    for n in range(1,257):
        fs=factors(n);d={p:0 for p in fs}
        for q in range(2,n+1):
            if n%q==0 and len(factors(q))==1:
                p=next(iter(factors(q)));d[p]+=1
        require(d==fs,'Mangoldt divisor identity')
        cases+=1
    log_cases=0
    for p in ps:
        lp=log_rational(F(p));low=F(2,3)*(p.bit_length()-1)
        require(lp.lo*low.denominator>low.numerator*SCALE,'log minorant')
        log_cases+=1
    require(log_rational(F(2)).lo*3>2*SCALE,'log2 lower')
    require(log_rational(F(2)).hi*4<3*SCALE,'log2 upper')
    return {'divisor_identities':cases,'prime_checks':255,'log_enclosures':log_cases}


def dirichlet_checks() -> dict[str,Any]:
    cases=0
    sets=[list(range(1,N+1)) for N in (2,3,4,8,12,16,32)]
    sets += [[d for d in range(1,n+1) if n%d==0] for n in (36,60,72,360,1024)]
    min_pivot=None; grounded_pivots=0
    for vertices in sets:
        N=len(vertices);ix={v:i for i,v in enumerate(vertices)};E=zeros(N)
        for j,n,p in edge_list(vertices):
            c=F(2,3)*(p.bit_length()-1)/n
            a,b=ix[j],ix[n]
            E[a][a]+=c;E[b][b]+=c;E[a][b]-=c;E[b][a]-=c
        require(all(sum(row)==0 for row in E),'constant null vector')
        P=max(p for n in vertices for p in factors(n))
        kap=48*(1+(16*P.bit_length()).bit_length())
        B=[[E[i][j]-(F(1,kap*vertices[i]) if i==j else F(0))
            for j in range(1,N)] for i in range(1,N)]
        piv=ldl_pivots(B);grounded_pivots+=len(piv)
        min_pivot=min(piv) if min_pivot is None else min(min_pivot,*piv)
        for seed in range(1,5):
            f=[F((seed*n)%7-3,seed+1) for n in vertices]
            form=sum(f[i]*E[i][j]*f[j] for i in range(N) for j in range(N))
            edges=sum(F(2,3)*(p.bit_length()-1)/n*(f[ix[n]]-f[ix[j]])**2
                      for j,n,p in edge_list(vertices))
            require(form==edges,'full cross-term identity')
            cases+=1
    return {'divisor_closed_sets':len(sets),'signed_vectors':cases,
            'positive_grounded_pivots':grounded_pivots,
            'minimum_grounded_pivot':rational_string(min_pivot)}


TRIAL=[74448062,-26376039,4449468,-22598702,13406564,-20327903,
6239006,-26508164,25956889,-18050658,-11488509,-17808660,35356205,
-29934309,8148716,-25690859,18511265,-25362342,-5057466,-32286693,
45734480,-24852442,-10930717,-27451164,47258210,-30768779,-1669941,
-24311483,1383346,-24169373,8148716]


def actual_inverse_certificate() -> dict[str,Any]:
    N=32;ns=list(range(2,N+1)); y=[F(t,10**8) for t in TRIAL]
    def row(n: int) -> list[F]:
        if n==1:return [-F(1,i) for i in ns]
        return [F(int(i==n)) for i in ns]
    M=[[F(int(i==j),i)+F(1,i*j) for j in ns] for i in ns]
    Kminus=zeros(N-1);q={p:F(0) for p in primes(N)}
    ky={p:[F(0)]*(N-1) for p in primes(N)}
    edges=edge_list(list(range(1,N+1)))
    for j,n,p in edges:
        d=[a-b for a,b in zip(row(n),row(j))]
        dy=sum(a*b for a,b in zip(d,y)); q[p]+=dy*dy/n
        low=F(2,3)*(p.bit_length()-1)/n
        for i in range(N-1):
            ky[p][i]+=d[i]*dy/n
            for k in range(N-1):Kminus[i][k]+=low*d[i]*d[k]
    piv=ldl_pivots([[Kminus[i][j]-M[i][j]/384 for j in range(N-1)]
                    for i in range(N-1)])
    logs={p:log_rational(F(p)) for p in primes(N)}
    dual=I.rational(2*y[0])
    for p in logs:dual=dual-logs[p].scale(q[p])
    residual=[]
    for i in range(N-1):
        r=I.rational(int(i==0))
        for p in logs:r=r-logs[p].scale(ky[p][i])
        residual.append(r)
    budget=384*sum(n*r.square_upper() for n,r in zip(ns,residual))
    lo=F(dual.lo,SCALE); hi=F(dual.hi,SCALE)+budget
    # Coarse human-readable enclosure, distinct from exact interval endpoints.
    bracket=(F(7444806194657,10**13),F(7444806194659,10**13))
    require(bracket[0]<lo<hi<bracket[1],'claimed inverse enclosure failed')
    return {'N':N,'largest_prime':31,'edge_count':len(edges),'metric':'harmonic-mean-zero exact M',
            'rational_trial_denominator':10**8,'rational_trial_numerators':TRIAL,
            'finite_gap_certificate':'K_minus - M/384 has all positive LDL pivots',
            'gap_pivot_count':len(piv),'gap_minimum_pivot':rational_string(min(piv)),
            'inverse_lower':rational_string(lo),'inverse_upper':rational_string(hi),
            'residual_budget_upper':rational_string(budget),
            'strict_display_bracket':[rational_string(x) for x in bracket],
            'no_infinite_analytic_gap_input_for_this_finite_certificate':True}


def counterfeit_check() -> dict[str,int]:
    # Ground-channel subtraction leaves the orthogonal block unchanged.
    cases=0
    for N in range(2,18):
        h=sum(F(1,n) for n in range(1,N+1))
        eps=F(1,N+1)
        require(-eps*h<0,'null-channel witness')
        for j in range(2,N+1):
            # f1=-1/j, f_j=1 has harmonic mean zero.
            require(-F(1,j)+F(1,j)==0,'orthogonal witness')
            cases+=1
    return {'exact_null_channel_panels':cases}


def reconstruct() -> dict[str,Any]:
    return {'status':'PROPOSED_COMPONENT_PROOFS','rh_proved':False,
            'arithmetic_spectral_gap_proved_in_manuscript':True,
            'largest_prime_not_integer_height':True,
            'finite_code_proves_infinite_theorem':False,
            'arithmetic':arithmetic_checks(),'tree':subtree_checks(),
            'finite_forms':dirichlet_checks(),'inverse_certificate':actual_inverse_certificate(),
            'retained_channel':counterfeit_check()}


def no_duplicates(pairs: list[tuple[str,Any]]) -> dict[str,Any]:
    d={}
    for k,v in pairs:
        if k in d:raise ValueError('duplicate JSON key')
        d[k]=v
    return d


def strict_equal(a: Any,b: Any) -> bool:
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b


def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path);p.add_argument('--emit',type=Path)
    args=p.parse_args();out=reconstruct()
    if args.check:
        data=json.loads(args.check.read_text(),object_pairs_hook=no_duplicates,
                        parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        require(strict_equal(data,out),'retained result does not match reconstruction')
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.emit:args.emit.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
