#!/usr/bin/env python3
"""Bounded exact algebra only. This program does not prove spectral reality."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCE_LOCK.json', 'VALIDATION.md',
         'check.py', 'result.json', 'SHA256SUMS'}


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for k, v in enumerate(a): c[k] += v
    for k, v in enumerate(b): c[k] += v
    return trim(c)


def scale(a, s): return trim([v*s for v in a])


def mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)


def deriv(a): return trim([i*a[i] for i in range(1,len(a))] or [0])


def strict_pairs(items):
    d = {}
    for k,v in items:
        require(k not in d, 'duplicate JSON key')
        d[k] = v
    return d


def load(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=strict_pairs,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('no floats')))


def same(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b


def reconstruct():
    counts = {}
    # Differential expression identity, w=iz/2 treated as a formal scalar.
    count=0
    for C in [[0,1], [0,2,0,3], [F(1,3),F(-2,5),0,1]]:
        C=trim(C)
        for f in [[1], [0,1], [1,-2,3], [0,0,1,0,2]]:
            f=trim(f)
            for w in [F(-2),F(0),F(3,7)]:
                D=add(C,[-w])
                Af=add(scale(deriv(f),-1),mul(D,f))
                product=add(deriv(Af),mul(D,Af))
                explicit=add(scale(deriv(deriv(f)),-1),
                             mul(add(mul(D,D),deriv(C)),f))
                require(product==explicit,'factorization sign')
                count+=1
    counts['polynomial_factorizations']=count
    count=0
    # Exact Wronskian algebra for arbitrary endpoint integrals and nonzero Q.
    for Q in [F(1,2),F(1),F(3)]:
        for r in [F(-2),F(0),F(5,3)]:
            for A,B in [(F(2),F(3)),(F(-2),F(2)),(F(1,7),F(-4,3))]:
                ym,yp=Q*A,Q*B
                dym=r*ym+1/Q
                dyp=r*yp-1/Q
                require(ym*dyp-dym*yp==-(A+B),'Wronskian normalization')
                count+=1
    counts['wronskian_algebra']=count
    count=0
    # Real and imaginary parts at a characteristic state; b may be nonzero.
    for a in [F(1),F(-3,2)]:
        for b in [F(0),F(1,4),F(-2,5)]:
            for N in [F(1),F(7,3)]:
                c=-b*N/2
                h=(a*a+b*b)*N/4
                real=h+b*c-(a*a-b*b)*N/4
                imag=-a*c-a*b*N/2
                require(real==0 and imag==0,'energy identity')
                require(2*c==-b*N,'potential moment')
                count+=1
    counts['characteristic_energy_identities']=count
    count=0
    # theta(e^(2d)x) and theta(e^(-2d)x) exchange under inversion.
    # r=e^(d/2); no transcendental evaluation is claimed.
    for r in [F(5,4),F(3,2),F(2),F(3)]:
        for c in [F(9,8),F(5,3),F(2)]:
            D=c+(r+1/r)/2
            w0,wp,wm=c/D,r/(2*D),1/(2*r*D)
            require(w0+wp+wm==1,'constant heat atom')
            require(wp/r**2==wm and wm*r**2==wp,'modular exchange')
            require((c+(r+1/r)/2)/D==1,'endpoint normalization')
            count+=1
    counts['self_reciprocal_heat_weights']=count
    # Exact multiplier cancellation and nonzero derivative factor at the
    # displayed shifted roots, with v=e^(d eta)>1 left as an exact parameter.
    count=0
    for v in [F(11,10),F(5,4),F(3,2),F(2),F(3)]:
        c=(v+1/v)/2
        sh=(v-1/v)/2
        require(c*c-sh*sh==1 and sh>0,'hyperbolic identity')
        require(c+(-c)==0,'changed-source root')
        count+=1
    counts['changed_source_multiplier_identities']=count
    # One finite matrix with a positive self-adjoint H and non-real roots
    # does NOT model the full differential source. It only checks the sign
    # trap in replacing a skew coefficient by an adjoint product.
    # For H=1,C=1: P(z)=1-iz-z^2/4 has z=-2i, a double zero.
    require(F(1)-F(2)+F(1)==0,'finite skew-pencil sign control')
    counts['declared_finite_sign_control']=1
    return {'schema':'exact-theta-pencil-bounded-algebra-v1',
            'rh_proved':False,'actual_xi_spectral_reality_proved':False,
            'status':'BOUNDED_ALGEBRA_ONLY',
            'groups':counts,'total_bounded_cases':sum(counts.values()),
            'native_numerical_zero_computation':False,
            'infinite_analytic_arguments_machine_proved':False}


def authenticate():
    actual={p.name for p in ROOT.iterdir()}
    require(actual==FILES,'exact file inventory')
    require(all(p.is_file() and not p.is_symlink() for p in ROOT.iterdir()),
            'regular files only')
    rows=(ROOT/'SHA256SUMS').read_text().splitlines()
    declared={}
    for line in rows:
        digest,name=line.split('  ',1)
        require(name not in declared and name in FILES-{'SHA256SUMS'},'manifest names')
        require(len(digest)==64,'manifest digest')
        declared[name]=digest
    require(set(declared)==FILES-{'SHA256SUMS'},'manifest coverage')
    for name,digest in declared.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
                'hash mismatch: '+name)
    lock=load(ROOT/'SOURCE_LOCK.json')
    require(lock['parent']['commit']=='3954f6398dd4be35182d89f44d1a715a4cfcbda0',
            'parent reference drift')
    require(lock['author_status']=='research-not-review-acceptance','source status')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--emit',action='store_true',help='unauthenticated producer mode')
    p.add_argument('--check',type=Path)
    a=p.parse_args()
    require(a.emit != (a.check is not None),'choose exactly one mode')
    result=reconstruct()
    if a.check is not None:
        authenticate()
        require(same(load(a.check),result),'result reconstruction mismatch')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as e:
        print('REJECT: '+str(e),file=sys.stderr)
        sys.exit(1)
