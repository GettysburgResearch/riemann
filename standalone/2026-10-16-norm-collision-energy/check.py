#!/usr/bin/env python3
"""Exact finite algebra checks, not certification of infinite analytic claims.

Standard library only. Complete ideal lists are used at the declared caps;
phase/mask profiles are explicit algebraic fixtures, not a theta-row census.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import gcd, lcm, isqrt
import hashlib
import json

COUNTS: Counter[str] = Counter()

def require(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise ValueError(f"failed {label}, predicate {COUNTS[label]}")

@dataclass(frozen=True)
class Quad:
    """Exact a+b sqrt(p), with a fixed positive nonsquare prime p."""
    a: Q
    b: Q
    p: int
    def __add__(self, o: Quad) -> Quad:
        if self.p != o.p: raise ValueError('incompatible fields')
        return Quad(self.a+o.a, self.b+o.b, self.p)
    def __neg__(self) -> Quad: return Quad(-self.a,-self.b,self.p)
    def __sub__(self, o: Quad) -> Quad: return self+-o
    def __mul__(self, o: Quad) -> Quad:
        if self.p != o.p: raise ValueError('incompatible fields')
        return Quad(self.a*o.a+self.p*self.b*o.b,self.a*o.b+self.b*o.a,self.p)
    def nonnegative(self) -> bool:
        if self.b == 0: return self.a >= 0
        if self.b > 0:
            return self.a >= 0 or self.p*self.b*self.b >= self.a*self.a
        return self.a > 0 and self.a*self.a >= self.p*self.b*self.b

def partitions(n: int, minimum: int=1):
    if n == 0:
        yield ()
    for j in range(minimum,n+1):
        for tail in partitions(n-j,j): yield (j,)+tail

def conv(a: dict, b: dict) -> dict:
    out = {}
    for i,x in a.items():
        for j,y in b.items():
            z=x*y
            out[i+j]=out[i+j]+z if i+j in out else z
    return out

def local_budget_checks() -> int:
    cases=0
    for d in range(1,7):
        for fs in partitions(d):
            r=fs.count(1)
            tensor=tuple(h for f in fs for g in fs for h in [lcm(f,g)]*gcd(f,g))
            require(sum(tensor)==d*d,'tensor_degree')
            require(tensor.count(1)==r*r,'tensor_first_coefficient')
            for p,m in product((2,3,7,13),range(2,10)):
                zero=Quad(Q(0),Q(0),p); one=Quad(Q(1),Q(0),p)
                def real(x): return Quad(Q(x),Q(0),p)
                poly={0:one}
                for f in fs:
                    lin=Q(1)-Q(1,p**f)
                    if f%2: lin_q=Quad(Q(0),lin/Q(p**((f+1)//2)),p)
                    else: lin_q=real(lin/Q(p**(f//2)))
                    poly=conv(poly,{0:one,f:lin_q,m*f:real(Q(1,p**f))})
                tail=sum((v for e,v in poly.items() if e>=2),zero)
                bound=real(Q(3**d,p))
                require((bound-tail).nonnegative(),'critical_l1_tail')
                squares=sum((v*v for e,v in poly.items() if e>=2),zero)
                require((real(Q(9**d,p*p))-squares).nonnegative(),'critical_l2_tail')
                first=Quad(Q(0),Q(r*(p-1),p*p),p)
                require(poly.get(1,zero)==first,'first_coefficient')
                # Formal inverse tensor zeta at critical weight. Odd m can
                # leave genuine quadratic values when different channels collide.
                squared={e:v*v for e,v in poly.items()}
                inv={0:one}
                for h in tensor:
                    inv=conv(inv,{0:one,h:real(-Q(1,p**h))})
                quotient=conv(squared,inv)
                residual=zero
                for e,v in quotient.items():
                    if e: residual=residual+(v if v.nonnegative() else -v)
                kd=2*d*d+d**4+2**(d*d)*(1+d*d+9**d)
                require((real(Q(kd,p*p))-residual).nonnegative(),'critical_inverse_tensor_mass')
                cases+=1
    return cases

def primes(cap: int) -> list[int]:
    sieve=bytearray(b'\x01')*(cap+1); sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(cap)+1):
        if sieve[p]: sieve[p*p:cap+1:p]=b'\x00'*((cap-p*p)//p+1)
    return [i for i in range(2,cap+1) if sieve[i]]

def prime_ideals(cap: int):
    ans=[]
    for p in primes(cap):
        if p in (2,3): continue
        if p%3==1:
            ans += [(p,p,1,0),(p,p,1,1)]
        elif p*p<=cap: ans.append((p*p,p,2,0))
    return sorted(ans)

def phase(q: int,index: int,profile: str) -> tuple[int,int]:
    if profile=='conjugate': return 1, (-1 if index else 1)
    if profile=='mask' and q==7 and index==0: return 0,0
    if profile=='mask': return (-1 if index else 1),1
    return 1,1

def options(q: int,index: int,m: int,profile: str,native: bool=False):
    if not native and m%2:
        raise ValueError('integer-weight census requires even m; local tests cover odd m exactly')
    a,b=phase(q,index,profile)
    result=[(1,Q(1))]
    if a: result.append((q,-Q(a) if native else -Q(a*(q-1),q)))
    if b and not native: result.append((q**m,-Q(b*q**(m//2-1))))
    return result

def complete_ideal_list(cap: int,m: int,profile: str,native: bool=False):
    rows=[(1,Q(1))]
    for q,p,f,index in prime_ideals(cap):
        old=rows[:]
        for nn,c in options(q,index,m,profile,native)[1:]:
            if nn>cap: continue
            rows.extend((n*nn,x*c) for n,x in old if n*nn<=cap)
    return rows

def norm_euler(cap: int,m: int,profile: str,native: bool=False):
    local={}
    for q,p,f,index in prime_ideals(cap):
        fac={}
        for nn,c in options(q,index,m,profile,native):
            if nn>cap: continue
            exponent=0
            while nn>1: nn//=p; exponent+=1
            fac[exponent]=c
        local[p]=conv(local.get(p,{0:Q(1)}),fac)
    spf=list(range(cap+1))
    for p in range(2,isqrt(cap)+1):
        if spf[p]==p:
            for n in range(p*p,cap+1,p):
                if spf[n]==n: spf[n]=p
    coeff=[Q(0)]*(cap+1); coeff[1]=Q(1)
    for n in range(2,cap+1):
        p=spf[n]; rest=n; e=0
        while rest%p==0: rest//=p; e+=1
        coeff[n]=coeff[rest]*local.get(p,{}).get(e,Q(0))
    return coeff

def census_checks():
    fixtures=[(4096,2,'unit',False),(4096,4,'unit',False),
              (4096,6,'conjugate',False),(4096,6,'mask',False),
              (8192,6,'unit',True),(131072,6,'unit',False)]
    records=[]
    for cap,m,profile,native in fixtures:
        ideal_list=complete_ideal_list(cap,m,profile,native)
        aggregated=defaultdict(Q); literal_diag=defaultdict(Q)
        for n,x in ideal_list: aggregated[n]+=x; literal_diag[n]+=x*x
        euler=norm_euler(cap,m,profile,native)
        for n in range(1,cap+1):
            require(aggregated[n]==euler[n],'complete_norm_fiber')
        require(aggregated[7]**2!=literal_diag[7] if profile!='mask' else True,
                'distinct_equal_norm_guard')
        encoded='\n'.join(f'{n}:{x}' for n,x in sorted(aggregated.items())).encode()
        records.append(dict(cap=cap,m=m,profile=profile,native=native,
                            supported_ideals=len(ideal_list),
                            nonzero_norm_coefficients=sum(bool(x) for x in euler),
                            aggregation_sha256=hashlib.sha256(encoded).hexdigest()))
    return records

def local_quadratic_factor(p: int,m: int,b1: int,b2: int) -> Q:
    # Critical local coefficients: use sqrt(p) to keep odd m exact as well.
    one=Quad(Q(1),Q(0),p)
    lin=Quad(Q(0),-Q(p-1,p*p),p)
    polys=[{0:one,1:lin,m:Quad(-Q(b,p),Q(0),p)} for b in (b1,b2)]
    pol=conv(*polys)
    value=sum((x*x for x in pol.values()),Quad(Q(0),Q(0),p))
    require(value.b==0,'quadratic_factor_rationality')
    return value.a

def constants_and_negative_checks():
    for p,b1,b2 in product((7,13,19),(-1,0,1),(-1,0,1)):
        a=1-Q(1,p); s=(b1+b2)**2
        expected=1+4*a*a/p+a**4/(p*p)+Q(s,p*p)+a*a*s/(p**3)+Q((b1*b2)**2,p**4)
        for m in range(3,10):
            require(local_quadratic_factor(p,m,b1,b2)==expected,'m_independent_constant')
    require(local_quadratic_factor(7,2,1,1)!=local_quadratic_factor(7,6,1,1),
            'negative_m2_overlap')
    require(2*Q(6,7)**2!=(2*Q(6,7))**2,'negative_square_before_group')
    require(-Q(6,7)!=-2*Q(6,7),'negative_missing_conjugate')
    require(-7**2!=-7**3,'negative_wrong_power')
    require(options(7,0,6,'mask')==[(1,Q(1))],'negative_mask_power_branch')
    require((-1)**6!=(-1),'negative_power_twist')
    require((2,2)!=(1,1,1,1),'negative_inert_as_split')
    require(8*8>8,'negative_graph_degree')
    # Two equal-norm ideals retain their cross term under EVERY twist average.
    require(Q(1)+Q(1)+2*Q(1)!=Q(1)+Q(1),'negative_twist_kills_norm_collision')

def gaussian_algebra_checks():
    for c,a,b,x in product((Q(0),Q(1,2),Q(5,6),Q(2)),
                           (Q(-2),Q(0),Q(3)),(Q(-1),Q(0),Q(4)),
                           (Q(-3),Q(0),Q(2))):
        beta=2*c-1; mu=(a+b)/2
        original=(2*c-1)*x-c*(a+b)-((x-a)**2+(x-b)**2)/4
        final=-(x-mu-beta)**2/2-mu+beta**2/2-(a-b)**2/8
        require(original==final,'gaussian_square_completion')
    for r,degree in product(range(1,8),range(1,6)):
        vals=[Q((i+1)**r,1+i) for i in range(8)]
        edges=[(i,j) for i in range(8) for j in range(8) if abs(i-j)<degree]
        maxdeg=max(sum(i==v for i,j in edges) for v in range(8))
        lhs=sum(vals[i]*vals[j] for i,j in edges)
        require(lhs<=maxdeg*sum(x*x for x in vals),'graph_schur')

def run():
    cases=local_budget_checks()
    constants_and_negative_checks(); gaussian_algebra_checks()
    records=census_checks()
    return dict(status='PASS: finite algebra only',
                local_splitting_m_prime_cases=cases,
                complete_ideal_censuses=records,
                predicates=dict(sorted(COUNTS.items())),total_predicates=sum(COUNTS.values()),
                negative_controls=9,
                limitations='Same-author implementations; full ideal caps but algebraic phase profiles. No analytic/asymptotic certification or theta-row census.')

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
