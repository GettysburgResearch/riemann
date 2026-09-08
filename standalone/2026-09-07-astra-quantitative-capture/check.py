#!/usr/bin/env python3
"""Bounded rational checks for HC26. Does not verify the analytic theorems."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from fractions import Fraction as F
from pathlib import Path
from typing import Any

FILES = (
    'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.md', 'SOURCE_LOCK.json',
    'VALIDATION.md', 'check.py', 'test_check.py', 'verification.json',
)
SOURCE_LOCK = {
    'repository': 'GettysburgResearch/riemann',
    'read_pr_812_head': '2d683186cb3dd4f304159d8176215ceae8ac59fb',
    'read_pr_814_head': 'dc7babb830cb696810fb68bd74f6a33459f5f921',
    'parent_path': 'standalone/2026-09-07-astra-source-stability/PROOF.md',
    'parent_git_blob': 'd407fcc6b2ecf7d92f9393c3fc474f445095ca31',
    'parent_sha256': '63dda3d0ff38e28829ca7d80a491201a12a32b7282c8b301f2aef54d062e58b8',
    'parent_bytes': 17698,
    'parent_execution_this_pass': False,
    'runtime_parent_dependency': False,
    'mathematical_status': 'author-proposed component proofs; RH and (10) unproved',
}

class CheckError(ValueError):
    pass

def need(ok: bool, message: str) -> None:
    if not ok:
        raise CheckError(message)

def canon(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=True) + '\n').encode()

def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    d: dict[str, Any] = {}
    for k, v in items:
        need(k not in d, 'duplicate JSON key')
        d[k] = v
    return d

def forbidden(_: str) -> Any:
    raise CheckError('floating or nonfinite JSON number')

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_float=forbidden, parse_constant=forbidden)

def fs(x: F) -> str:
    return f'{x.numerator}/{x.denominator}'

def poly_dot(a: list[F], b: list[F]) -> F:
    return sum((x*y for x, y in zip(a,b)), F(0))

def evaluate(a: list[F], x: F) -> F:
    v=F(0)
    for c in reversed(a):
        v=v*x+c
    return v

def solve(a: list[list[F]], b: list[F]) -> list[F]:
    n=len(a)
    need(n>0 and len(b)==n and all(len(r)==n for r in a), 'matrix dimensions')
    m=[row[:] + [v] for row,v in zip(a,b)]
    for i in range(n):
        p=next((j for j in range(i,n) if m[j][i]), None)
        need(p is not None, 'singular matrix')
        m[i],m[p]=m[p],m[i]
        z=m[i][i]
        m[i]=[x/z for x in m[i]]
        for j in range(n):
            if j!=i:
                z=m[j][i]
                m[j]=[x-z*y for x,y in zip(m[j],m[i])]
    return [row[-1] for row in m]

def projection(n: int, target: list[F]) -> tuple[F,list[F],list[F]]:
    # Independent polynomial-column construction for A_*(w)=1-2w.
    size=max(n+1,len(target))
    cols=[]
    for j in range(n):
        col=[F(0)]*size
        col[j]=F(1); col[j+1]=F(-2)
        cols.append(col)
    q=target+[F(0)]*(size-len(target))
    gram=[[poly_dot(c,d) for d in cols] for c in cols]
    rhs=[poly_dot(c,q) for c in cols]
    c=solve(gram,rhs)
    err=[q[j]-sum((c[i]*cols[i][j] for i in range(n)),F(0)) for j in range(size)]
    return poly_dot(err,err),c,err

def reconstruct() -> dict[str,Any]:
    counts: dict[str,int]={}
    def test(group: str, ok: bool, msg: str) -> None:
        need(ok, group+': '+msg)
        counts[group]=counts.get(group,0)+1

    s=F(1,16)
    test('exponents',2*s<F(1,5),'source Sobolev range')
    test('exponents',2*s<F(1,2),'Blaschke summability range')
    test('exponents',s/F(3)-(s/F(8))*F(4,3)==s/F(6),'Holder loss')
    test('exponents',F(1,3)+F(1,6)==F(1,2),'Holder indices')
    test('exponents',F(2,3)+F(1,3)==1,'interpolation weights')
    test('exponents',s<F(1,2),'target truncation loss')

    # No logarithm is numerically evaluated. ell is its exact integer ceiling.
    for n in list(range(1,65))+[127,128,129,1023,1024,10**6]:
        ell=n.bit_length(); L=23+6*ell; a=16+4*ell
        test('small_value_constants',2**(ell-1)<n+1<=2**ell,'ceiling')
        test('small_value_constants',L<=2**(ell+4),'L bound')
        test('small_value_constants',F(96*n*(n+1)*L,2**a)<=F(3,256),'exceptional mass')
        test('small_value_constants',1+L*(4*a+15)==1818+842*ell+96*ell*ell,'polynomial expansion')
    for N in range(1,17):
        for j in range(0,4*(N+1)+1):
            x=F(j,N+1); w=min(x,F(1))
            # w^2 <= x^(1/8), raised to the eighth power.
            test('fejer_factors',w**16<=x,'coefficient error bound')
        test('degree_split',(N+1)**3>=2*N+3,'logarithmic rank conversion')

    # Exact radial norm of one Blaschke factor; finite part plus geometric tail.
    for a in [F(0),F(1,4),F(1,2),F(2,3),F(3,4)]:
        for r in [F(1,4),F(1,2),F(3,4),F(7,8)]:
            total=a*a+(1-a*a)**2*r*r/(1-a*a*r*r)
            finite=a*a+sum(((1-a*a)**2*a**(2*j-2)*r**(2*j) for j in range(1,9)),F(0))
            tail=(1-a*a)**2*a**16*r**18/(1-a*a*r*r)
            test('blaschke_radial',total==finite+tail,'geometric tail')
            test('blaschke_radial',1-total==(1-a*a)*(1-r*r)/(1-a*a*r*r),'radial defect')
    for z in [F(-3,4),F(-1,3),F(0),F(2,5),F(4,5)]:
        vals=[((a-z)/(1-a*z))**2 for a in [F(1,4),F(1,2),F(3,4)]]
        prod=F(1)
        for v in vals: prod*=v
        test('blaschke_product',all(0<=v<=1 for v in vals),'factor contractivity')
        test('blaschke_product',0<=1-prod<=sum((1-v for v in vals),F(0)),'defect subadditivity')
    for a in [F(1,4),F(1,2),F(3,4),F(1)]:
        for b in [F(0),(1-a)/2,1-a]:
            norm=(1-a)**2+b*b
            test('schur_deficit',norm<=2*(1-a),'finite Schur norm identity')

    targets=[[F(1)],[F(0),F(1)],[F(1),F(1)],[F(1),F(-2)],
             [F(1),F(0),F(-1)]]
    panels=[]
    for ti,q in enumerate(targets):
        floor=F(3,4)*evaluate(q,F(1,2))**2
        previous=None
        for n in range(1,13):
            value,c,err=projection(n,q)
            test('synthetic_projection',value>=floor,'Hardy intrinsic lower bound')
            test('synthetic_projection',all(err[j]-2*err[j+1]==0 for j in range(n)), 'normal equations from residual')
            if previous is not None:
                test('synthetic_projection',value<=previous,'nested projection')
            if ti==0:
                exact=F(3*4**n,4**(n+1)-1)
                test('synthetic_projection',value==exact,'continuant formula')
                test('synthetic_projection',value-F(3,4)==F(3,4*(4**(n+1)-1)),'exact excess')
            if ti==3:
                test('synthetic_projection',value==0,'source target reproduced')
            previous=value
            if n in [1,2,4,8,12]:
                panels.append({'target':ti,'rank':n,'error':fs(value),'intrinsic':fs(floor),'excess':fs(value-floor)})

    horizons=[]
    for j in range(1,13):
        n=j*j+1
        floor=F(3,4)*4**j
        err=4**j*F(3*4**n,4**(n+1)-1)
        excess=err-floor
        test('growing_synthetic',excess==F(3*4**j,4*(4**(n+1)-1)),'scaled excess')
        test('growing_synthetic',excess<=F(1,2**j),'small removable term')
        test('growing_synthetic',floor>=2**j,'large intrinsic term')
        horizons.append({'j':j,'rank':n,'floor':fs(floor),'excess':fs(excess)})

    return {
        'schema':'HC26-bounded-reconstruction-v1',
        'rh_proved':False,'full_bound_10_proved':False,
        'paper_capture_theorem':'proposed; not machine verified',
        'actual_source_energy_computation':False,
        'arithmetic':'integer and Fraction only; no floating-point acceptance',
        'scope':{'gram_ranks':list(range(1,13)), 'targets':5,
                 'growing_synthetic_j':list(range(1,13)), 'fejer_N':list(range(1,17))},
        'groups':counts,'bounded_controls':sum(counts.values()),
        'synthetic_projection_panels':panels,'growing_synthetic_panels':horizons,
        'rate_exponents':{'sobolev_s':fs(s),'weighted_inverse_power':fs(s/6)},
    }

def validate_files(root: Path) -> None:
    for p in [root,*root.parents]:
        need(not p.is_symlink(),'symlink in package path')
    need(root.is_dir(),'package root missing')
    actual={p.name for p in root.iterdir()}
    need(actual==set(FILES)|{'SHA256SUMS'},'exact package inventory')
    for name in actual:
        p=root/name
        need(p.is_file() and not p.is_symlink(),'nonregular package entry')
    lines=(root/'SHA256SUMS').read_text(encoding='ascii').splitlines()
    need(len(lines)==len(FILES),'manifest count')
    seen=set()
    for line in lines:
        parts=line.split('  ')
        need(len(parts)==2,'manifest syntax')
        digest,name=parts
        need(name in FILES and name not in seen,'manifest path')
        need(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'manifest digest')
        seen.add(name)
        need(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'manifest content mismatch')
    need(seen==set(FILES),'manifest coverage')
    need(canon(read_json(root/'SOURCE_LOCK.json'))==canon(SOURCE_LOCK),'source metadata drift')

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__,allow_abbrev=False)
    ap.add_argument('--root',type=Path,default=Path(__file__).parent)
    args=ap.parse_args()
    try:
        root=Path(os.path.abspath(args.root))
        validate_files(root)
        result=reconstruct()
        need(canon(read_json(root/'verification.json'))==canon(result),'primitive reconstruction mismatch')
        print(json.dumps({'status':'PASS_BOUNDED_HC26','bounded_controls':result['bounded_controls'],
                          'groups':result['groups'],'rh_proved':False,'full_bound_10_proved':False,
                          'verification_sha256':hashlib.sha256(canon(result)).hexdigest()},sort_keys=True))
        return 0
    except (CheckError,OSError,ValueError,TypeError) as e:
        print('REJECT_HC26: '+str(e))
        return 1

if __name__=='__main__':
    raise SystemExit(main())
