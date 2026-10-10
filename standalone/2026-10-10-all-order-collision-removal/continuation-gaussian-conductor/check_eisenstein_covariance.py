#!/usr/bin/env python3
"""Exact finite arithmetic replay; not a checker of the infinite analytic bound.

Standard library only. Eisenstein integers and sixth roots are pairs a+b*omega.
All enumerations below are complete in their declared finite ranges. The test
window is 1_[1,2], not the smooth single window of the analytic implication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import isqrt, prod
from pathlib import Path

E = tuple[int, int]
ZERO: E = (0, 0)
ONE: E = (1, 0)
ROOTS: tuple[E, ...] = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
COUNTS: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise ValueError(label)
    COUNTS[label.split(':',1)[0]] += 1


def add(x: E, y: E) -> E:
    return x[0]+y[0], x[1]+y[1]


def mul(x: E, y: E) -> E:
    a,b=x; c,d=y
    return a*c-b*d, a*d+b*c-b*d


def conj(x: E) -> E:
    return x[0]-x[1], -x[1]


def norm(x: E) -> int:
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


def scale(a: int, x: E) -> E:
    return a*x[0], a*x[1]


def quotient(x: E, y: E) -> E | None:
    q=norm(y)
    if not q:
        raise ZeroDivisionError('zero Eisenstein divisor')
    z=mul(x,conj(y))
    return (z[0]//q,z[1]//q) if z[0]%q == z[1]%q == 0 else None


def primary(x: E) -> E:
    values=[mul(x,u) for u in ROOTS]
    values=[v for v in values if v[0]%3==1 and v[1]%3==0]
    require(len(values)==1, 'primary:unique')
    return values[0]


@lru_cache(None)
def rows(bound: int) -> tuple[E,...]:
    if bound < 1:
        return ()
    r=2*isqrt(bound)+3
    return tuple((a,b) for a in range(-r,r+1) for b in range(-r,r+1)
                 if 0 < a*a-a*b+b*b <= bound)


def rational_primes(bound: int) -> list[int]:
    return [p for p in range(2,bound+1)
            if all(p%d for d in range(2,isqrt(p)+1))]


def fp_mul(x: E,y: E,p: int) -> E:
    z=mul(x,y)
    return z[0]%p,z[1]%p


def fp_pow(x: E,n: int,p: int) -> E:
    y=ONE
    while n:
        if n&1:
            y=fp_mul(y,x,p)
        x=fp_mul(x,x,p); n//=2
    return y


@dataclass(frozen=True)
class PrimeIdeal:
    p: int
    w: int | None
    generator: E
    q: int

    def char(self, x: E) -> int:
        """Return sixth-root exponent, or -1 for the exact character zero."""
        if self.w is None:
            a=(x[0]%self.p,x[1]%self.p)
            if a==ZERO:
                return -1
            v=fp_pow(a,(self.q-1)//6,self.p)
            roots=[(z[0]%self.p,z[1]%self.p) for z in ROOTS]
        else:
            a=(x[0]+x[1]*self.w)%self.p
            if not a:
                return -1
            v=pow(a,(self.q-1)//6,self.p)
            roots=[(z[0]+z[1]*self.w)%self.p for z in ROOTS]
        if v not in roots:
            raise ValueError('residue value is not a sixth root')
        return roots.index(v)

    def field(self) -> tuple[E,...]:
        if self.w is None:
            return tuple(product(range(self.p),repeat=2))
        return tuple((a,0) for a in range(self.p))


def make_prime_ideals(bound: int) -> tuple[PrimeIdeal,...]:
    out=[]
    for p in rational_primes(bound):
        if p in (2,3):
            continue
        if p%3==2:
            if p*p<=bound:
                out.append(PrimeIdeal(p,None,primary((p,0)),p*p))
        else:
            roots=[w for w in range(p) if (w*w+w+1)%p==0]
            require(len(roots)==2,'split:two_roots')
            candidates=[z for z in rows(p) if norm(z)==p]
            for w in roots:
                gens={primary(z) for z in candidates if (z[0]+z[1]*w)%p==0}
                require(len(gens)==1,'prime_generator:unique')
                out.append(PrimeIdeal(p,w,gens.pop(),p))
    return tuple(sorted(out,key=lambda t:(t.q,t.p,-1 if t.w is None else t.w)))


def root_value(e: int) -> E:
    return ZERO if e<0 else ROOTS[e%6]


def character(mask: int, x: E, primes: tuple[PrimeIdeal,...]) -> int:
    ans=0
    for j,p in enumerate(primes):
        if mask>>j&1:
            e=p.char(x)
            if e<0:
                return -1
            ans+=e
    return ans%6


def psi(a: int,b: int,x: E,primes: tuple[PrimeIdeal,...]) -> E:
    ea=character(a,x,primes); eb=character(b,x,primes)
    return ZERO if min(ea,eb)<0 else ROOTS[(ea-eb)%6]


def mask_generator(mask: int, primes: tuple[PrimeIdeal,...]) -> E:
    z=ONE
    for j,p in enumerate(primes):
        if mask>>j&1:
            z=mul(z,p.generator)
    return z


def mask_norm(mask: int,primes: tuple[PrimeIdeal,...]) -> int:
    return prod(p.q for j,p in enumerate(primes) if mask>>j&1)


def submasks(mask: int):
    d=mask
    while True:
        yield d
        if not d:
            return
        d=(d-1)&mask


def squarefree_ideals(bound: int, primes: tuple[PrimeIdeal,...]) -> dict[int,E]:
    """Independently enumerate all primary lattice points, then factor them."""
    result={}
    for z in rows(bound):
        if z[0]%3!=1 or z[1]%3 or norm(z)%2==0 or norm(z)%3==0:
            continue
        rest=z; mask=0; sqf=True
        for j,p in enumerate(primes):
            e=0
            while True:
                t=quotient(rest,p.generator)
                if t is None:
                    break
                rest=t; e+=1
            if e>1:
                sqf=False
            if e:
                mask|=1<<j
        require(rest==ONE,'factorization:complete_primary')
        if sqf:
            require(mask not in result,'factorization:no_duplicate_ideal')
            result[mask]=z
            require(mask_generator(mask,primes)==z,'factorization:reconstruct')
    # Independent squarefree mask enumeration constrained by norm.
    alternative={0:ONE}
    for j,p in enumerate(primes):
        for m,z in list(alternative.items()):
            if norm(z)*p.q<=bound:
                alternative[m|(1<<j)]=mul(z,p.generator)
    require(result==alternative,'ideal_enumeration:two_methods')
    return result


def local_tests() -> dict:
    selected=[p for p in make_prime_ideals(121)
              if (p.p in (7,13,19) and p.w is not None) or
                 (p.p in (5,11) and p.w is None)]
    totals=[]
    for p in selected:
        field=p.field()
        vals={x:root_value(p.char(x)) for x in field}
        for x in field:
            require((vals[x]==ZERO)==(p.char(x)<0),'local:zero_extension')
            for y in field:
                xy=fp_mul(x,y,p.p) if p.w is None else ((x[0]*y[0])%p.p,0)
                require(vals[xy]==mul(vals[x],vals[y]),'local:multiplicative')
        for h in field:
            acc=ZERO
            for x in field:
                z=((x[0]+h[0])%p.p,(x[1]+h[1])%p.p)
                acc=add(acc,mul(vals[z],conj(vals[x])))
            require(acc==((p.q-1,0) if h==ZERO else (-1,0)),
                    'local:Gauss_autocorrelation')
        require(p.char(ROOTS[1]) == ((p.q-1)//6)%6,'local:unit_signature')
        totals.append({'q':p.q,'omega_root':p.w,'generator':p.generator})
    return {'fields':totals}


def kernel_tests() -> dict:
    primes=make_prime_ideals(26)
    # Complete prime set up to norm 26, all its squarefree product columns.
    masks=list(range(1<<len(primes)))
    bound=19
    vv=rows(bound)
    table={m:[root_value(character(m,u,primes)) for u in vv] for m in masks}
    ngen={m:mask_norm(m,primes) for m in masks}
    gen={m:mask_generator(m,primes) for m in masks}
    cache={}
    def primitive(a,b,L):
        key=(a,b,L)
        if key not in cache:
            value=ZERO
            for u in rows(L):
                value=add(value,psi(a,b,u,primes))
            cache[key]=value
        return cache[key]
    differing=0; masked_nonzero=0; lost_mask_example=None; phase_example=None
    for r in masks:
        for s in masks:
            direct=ZERO
            for x,y in zip(table[r],table[s]):
                direct=add(direct,mul(x,conj(y)))
            g=r&s; a=r^g; b=s^g
            rhs=ZERO; rhs_without_phase=ZERO
            for d in submasks(g):
                sign=(-1)**d.bit_count()
                inner=primitive(a,b,bound//ngen[d])
                rhs=add(rhs,scale(sign,mul(psi(a,b,gen[d],primes),inner)))
                rhs_without_phase=add(rhs_without_phase,scale(sign,inner))
            require(direct==rhs,'row_kernel:exact_mask_identity')
            er=character(r,ROOTS[1],primes); es=character(s,ROOTS[1],primes)
            if er!=es:
                differing+=1
                require(direct==ZERO,'row_kernel:unit_block_zero')
            if r!=s and g and direct!=ZERO:
                masked_nonzero+=1
            if r!=s and g and direct!=primitive(a,b,bound) and lost_mask_example is None:
                lost_mask_example={'r':r,'s':s,'g':g,'direct':direct,
                                   'without_mask':primitive(a,b,bound)}
            if direct!=rhs_without_phase and phase_example is None:
                phase_example={'r':r,'s':s,'g':g,'direct':direct,
                               'without_phase':rhs_without_phase}
    require(lost_mask_example is not None,'negative_control:mask_is_required')
    require(phase_example is not None,'negative_control:phase_is_required')
    return {'row_norm_bound':bound,'row_count':len(vv),'prime_ideal_count':len(primes),
            'product_columns':len(masks),'unit_mismatch_pairs':differing,
            'nonzero_shared_prime_offdiagonals':masked_nonzero,
            'missing_mask_counterexample':lost_mask_example,
            'missing_phase_counterexample':phase_example}


def integrated_panel(k: int,D: int,power: int,H: int) -> dict:
    primes=make_prime_ideals(2*D)
    ideals=squarefree_ideals(2*D,primes)
    nn={m:norm(z) for m,z in ideals.items()}
    # Each allocation of disjoint ideals contributes exactly an interval in X.
    events=defaultdict(Counter)
    tuples=0
    for factors in product(ideals,repeat=k):
        union=0
        good=True
        for m in factors:
            if union&m:
                good=False; break
            union|=m
        if not good:
            continue
        lo=F(max(nn[m] for m in factors),2)
        hi=min(F(min(nn[m] for m in factors)),F(D))
        if lo>=hi:
            continue
        events[lo][union]+=1; events[hi][union]-=1; tuples+=1
    cuts=sorted(events)
    vv=rows(H)
    cols=sorted({r for ev in events.values() for r in ev})
    values={r:[root_value(character(r,u,primes)) for u in vv] for r in cols}
    kernels={}
    conductor={}
    for r in cols:
        for s in cols:
            z=ZERO
            for x,y in zip(values[r],values[s]):
                z=add(z,mul(x,conj(y)))
            kernels[r,s]=z
            conductor[r,s]=mask_norm(r^s,primes)
    acc=Counter(); energy=F(0); diag=F(0); off=F(0); low=F(0); high=F(0)
    sectors=defaultdict(F)
    for j,x in enumerate(cuts[:-1]):
        acc.update(events[x]); active={r:w for r,w in acc.items() if w}
        y=cuts[j+1]
        mass=(x**(-power)-y**(-power))/power
        direct=0
        for index,u in enumerate(vv):
            z=ZERO
            for r,w in active.items():
                z=add(z,scale((-1)**r.bit_count()*w,values[r][index]))
            direct+=norm(z)
        diagonal=0; remainder=ZERO; lowpart=ZERO; highpart=ZERO
        for r,w in active.items():
            diagonal+=w*w*kernels[r,r][0]
            require(kernels[r,r][1]==0,'integral:diagonal_real')
            for s,v in active.items():
                if r==s:
                    continue
                contribution=scale((-1)**(r.bit_count()+s.bit_count())*w*v,kernels[r,s])
                remainder=add(remainder,contribution)
                if conductor[r,s]<=H:
                    lowpart=add(lowpart,contribution)
                else:
                    highpart=add(highpart,contribution)
                sectors[conductor[r,s]] += mass*contribution[0]
        require(remainder[1]==lowpart[1]==highpart[1]==0,'integral:Hermitian_real')
        require(direct==diagonal+remainder[0],'integral:literal_signed_identity')
        require(remainder==add(lowpart,highpart),'integral:conductor_partition')
        energy+=mass*direct; diag+=mass*diagonal; off+=mass*remainder[0]
        low+=mass*lowpart[0]; high+=mass*highpart[0]
    require(energy==diag+low+high,'integral:integrated_identity')
    require(energy>=0 and diag>=0 and off>=-diag,'integral:positivity_boundary')
    def fstr(a):
        return str(a)
    return {'k':k,'horizon_D':D,'row_bound_H':H,'weight_exponent_2k_sigma':power,
            'complete_squarefree_factors':len(ideals),'ordered_allocations':tuples,
            'product_columns':len(cols),'scale_intervals':len(cuts)-1,
            'energy':fstr(energy),'diagonal':fstr(diag),'offdiagonal':fstr(off),
            'low_Q_le_H':fstr(low),'high_Q_gt_H':fstr(high),
            'sector_sha256':hashlib.sha256(json.dumps({str(q):str(v) for q,v in sorted(sectors.items())},
                sort_keys=True).encode()).hexdigest()}


def exponent_tests() -> dict:
    examples=[]
    for k in range(2,21):
        for denom in (8,12,24,48):
            delta=F(1,denom)
            for h in (F(1),F(21,20),F(11,10)):
                qstar=h/(1-delta)
                require(qstar*(1-delta)==h,'exponent:cutoff_cost')
                require(-2*delta*h+(1+delta)*h==h*(1-delta),'exponent:low_saving')
                alpha=F(1,2)+delta+5*h/(12*k)
                require(alpha==F(1,2)+delta+(5*h/6)/(2*k),'exponent:zero_free_adapter')
                if k==2 and h==1:
                    examples.append({'delta':str(delta),'Q_cutoff_exponent':str(qstar),
                                     'conditional_boundary':str(alpha)})
            hcomplete=2*k*(1-delta)
            require(F(1,2)+delta+5*hcomplete/(12*k)==F(4,3)+delta/6,
                    'exponent:no_free_global_completion')
    for k,expected in ((2,F(17,24)),(3,F(23,36)),(4,F(29,48))):
        require(F(1,2)+F(5,12*k)==expected,'exponent:parent_limit')
    return {'fourth_order_examples':examples}


def replay() -> dict:
    COUNTS.clear()
    local=local_tests()
    kernel=kernel_tests()
    panels=[integrated_panel(2,25,3,100),integrated_panel(3,13,4,100),
            integrated_panel(4,13,5,100)]
    exponents=exponent_tests()
    return {'status':'PASS','scope':'exact finite arithmetic; no infinite moment or asymptotic certification',
            'local_fields':local,'row_kernels':kernel,'integrated_panels':panels,
            'exponents':exponents,'predicate_counts':dict(sorted(COUNTS.items())),
            'total_predicates':sum(COUNTS.values())}


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',type=Path)
    ap.add_argument('--check',type=Path)
    ns=ap.parse_args()
    if ns.write and ns.check:
        ap.error('choose --write or --check, not both')
    result=json.loads(json.dumps(replay(), sort_keys=True))
    if ns.check:
        saved=json.loads(ns.check.read_text(encoding='utf-8'))
        if saved!=result:
            raise SystemExit('REJECT: recorded result differs from full exact replay')
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if ns.write:
        ns.write.write_text(text,encoding='utf-8')
    print(text,end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
