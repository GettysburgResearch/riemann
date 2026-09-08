#!/usr/bin/env python3
"""Finite algebra only. No evaluation of xi, W, or an infinite prime sum.

Logarithms of primes are formal labels. Coefficients are exact Fractions.
Taking v_j=r_j/sqrt(j) removes every square root from the tested identities.
A successful run is not a machine proof of the all-N analytic statements.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Callable

HERE = Path(__file__).resolve().parent
C = tuple[F, F]
Poly = list[C]
ZERO: C = (F(0), F(0))

def add(x: C, y: C) -> C:
    return x[0]+y[0], x[1]+y[1]

def sub(x: C, y: C) -> C:
    return x[0]-y[0], x[1]-y[1]

def real_inner(x: C, y: C) -> F:
    return x[0]*y[0]+x[1]*y[1]

def poly_inner(x: Poly, y: Poly) -> F:
    return sum((real_inner(a,b)/F(i+j+1)
                for i,a in enumerate(x) for j,b in enumerate(y)), F(0))

def poly_sub(x: Poly, y: Poly) -> Poly:
    return [sub(x[i] if i<len(x) else ZERO,
                y[i] if i<len(y) else ZERO) for i in range(max(len(x),len(y)))]

def factor(n: int) -> dict[int,int]:
    if n<1:
        raise ValueError('positive integer required')
    out: dict[int,int] = {}
    p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out

def mangoldt_label(n: int) -> int | None:
    fs=factor(n)
    return next(iter(fs)) if len(fs)==1 else None

def clean(x: dict[int,F]) -> dict[int,F]:
    return {p:q for p,q in x.items() if q}

def check_identity(N: int, rs: list[Poly]) -> None:
    # Independently assembled divisor diagonal, cross form, and edge squares.
    lhs: dict[int,F]=defaultdict(F)
    rhs: dict[int,F]=defaultdict(F)
    for j in range(1,N+1):
        norm=poly_inner(rs[j],rs[j])
        for p,e in factor(j).items():
            lhs[p]+=F(e,j)*norm
        for n in range(2,N//j+1):
            p=mangoldt_label(n)
            if p is not None:
                lhs[p]+=norm/F(n*j)
    for i in range(2,N+1):
        for j in range(1,i):
            if i%j==0:
                p=mangoldt_label(i//j)
                if p is not None:
                    lhs[p]-=F(2,i)*poly_inner(rs[i],rs[j])
    for n in range(2,N+1):
        p=mangoldt_label(n)
        if p is not None:
            for j in range(1,N//n+1):
                diff=poly_sub(rs[n*j],rs[j])
                rhs[p]+=poly_inner(diff,diff)/F(n*j)
    if clean(lhs)!=clean(rhs):
        raise AssertionError(f'divisor quadratic identity failed at N={N}')
    if any(q<0 for q in rhs.values()):
        raise AssertionError('negative square coefficient')

def fixtures() -> dict:
    groups: Counter[str]=Counter()
    def check(group: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(group)
        groups[group]+=1
    for N in (1,2,3,4,6,8,12,16,25,32,50):
        complex_rs=[[]]+[[(F(j%7-3,j+1),F(j%5-2,j+2))] for j in range(1,N+1)]
        check_identity(N,complex_rs)
        groups['complex_vector_identity']+=1
        # Each primitive polynomial has both endpoint values zero.
        ps: list[Poly]=[[]]
        for j in range(1,N+1):
            a=(F(j%7-3,j+1),F(j%5-2,j+2))
            b=(F(j%3-1,j+3),F(j%4-2,j+4))
            ps.append([ZERO,a,sub(b,a),(-b[0],-b[1])])
        check_identity(N,ps)
        groups['primitive_polynomial_identity']+=1
        check('primitive_endpoints',all(p[0]==ZERO and
              sum((z[0] for z in p),F(0))==0 and
              sum((z[1] for z in p),F(0))==0 for p in ps[1:]))
        check_identity(N,[[]]+[[(F(1),F(0))] for _ in range(N)])
        groups['ground_state_square_identity']+=1
        reachable={1}
        for k in range(2,N+1):
            if any(k%p==0 and k//p in reachable for p in factor(k)):
                reachable.add(k)
        check('prime_edge_connectivity',len(reachable)==N)
        # Logarithm labels for the exact Rayleigh numerator.
        direct: dict[int,F]=defaultdict(F)
        target: dict[int,F]=defaultdict(F)
        for n in range(2,N+1):
            p=mangoldt_label(n)
            if p:
                for j in range(1,N//n+1):
                    direct[p]+=F(2,n*j)
        for k in range(1,N+1):
            for p,e in factor(k).items():
                target[p]+=F(2*e,k)
        check('rayleigh_numerator',clean(direct)==clean(target))
        ell=F(1,2**20*N*N)
        check('integer_knot_budget',2*N*ell<1 and ell<F(1,2*N))
    # Each fixture covers a whole finite divisor or factorial identity.
    for k in (1,2,4,6,12,30,60,100,128,210,256):
        lhs: dict[int,F]=defaultdict(F)
        for d in range(2,k+1):
            p=mangoldt_label(d)
            if k%d==0 and p:
                lhs[p]+=1
        check('divisor_log_identity',clean(lhs)=={p:F(e) for p,e in factor(k).items()})
    for N in (1,2,5,10,25,50):
        lhs: dict[int,F]=defaultdict(F)
        rhs: dict[int,F]=defaultdict(F)
        for n in range(2,N+1):
            p=mangoldt_label(n)
            if p:
                lhs[p]+=N//n
        for j in range(1,N+1):
            for p,e in factor(j).items(): rhs[p]+=e
        check('factorial_floor_identity',clean(lhs)==clean(rhs))
    z=F(1,3)
    log2lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(4)),F(0))
    log2hi=log2lo+2*z**9/(9*(1-z*z))
    check('logarithm_constants',F(1,2)<log2lo<log2hi<F(3,4))
    check('gamma_derivative_budget',F(1,2)+1+F(11,16)<3)
    check('small_curvature_budget',16-11>0)
    check('cross_exponential_budget',F(128,127)<F(12,11))
    check('regular_cross_budget',F(8,2**20)<F(1,2))
    check('positivity_margin',20*F(1,2)-6-3-F(8,2**20)>F(1,2))
    check('two_vertex_adjacency_is_not_psd',-F(1,2)<0)
    check('operator_normalization',F(3,2)*F(1,2)==F(3,4))
    return {'status':'PASS_FINITE_ALGEBRA',
            'finite_fixtures':sum(groups.values()),'groups':dict(sorted(groups.items())),
            'arithmetic':'Gaussian rationals and formal prime-log coefficients',
            'analytic_theorems_machine_proved':False,
            'unrestricted_source_sign_proved':False,'rh_proved':False,
            'regular_cross_ceiling':str(F(8,2**20)),
            'log2_interval':[str(log2lo),str(log2hi)],
            'base_commit':'8cc6fc78db37f42290c7372bc994b3bfa94898ef',
            'proof_sha256':hashlib.sha256((HERE/'PROOF.md').read_bytes()).hexdigest(),
            'source_lock_sha256':hashlib.sha256((HERE/'SOURCE_LOCK.json').read_bytes()).hexdigest()}

def no_duplicates(pairs: list[tuple[str,object]]) -> dict:
    out={}
    for key,value in pairs:
        if key in out: raise ValueError('duplicate JSON key')
        out[key]=value
    return out

def canonical(x: object) -> str:
    return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)

def manifest() -> None:
    lines=(HERE/'SHA256SUMS').read_text().splitlines()
    named=set()
    for line in lines:
        sha,name=line.split('  ',1)
        if name in named or Path(name).name!=name: raise ValueError('manifest path')
        named.add(name)
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=sha:
            raise ValueError('manifest mismatch: '+name)
    expected={p.name for p in HERE.iterdir() if p.is_file() and p.name!='SHA256SUMS'}
    if named!=expected: raise ValueError('manifest coverage')

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    ap.add_argument('--manifest',action='store_true')
    args=ap.parse_args()
    got=fixtures()
    if args.check:
        expected=json.loads(args.check.read_text(),object_pairs_hook=no_duplicates)
        if canonical(expected)!=canonical(got): raise ValueError('saved result mismatch')
    if args.manifest: manifest()
    print(json.dumps(got,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
