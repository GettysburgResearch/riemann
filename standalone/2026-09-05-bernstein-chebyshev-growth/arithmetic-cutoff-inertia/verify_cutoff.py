#!/usr/bin/env python3
"""Exact finite algebra controls for AC-1--AC-3, not an RH proof checker.

Only fractions and integers enter acceptance. No assert statements are used.
Run from any directory: python verify_cutoff.py --check result.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sys
from typing import Any

HERE = Path(__file__).resolve().parent
PARENT_BLOB = '81d7d5db7a25f5875a08c10235fdb514d67cc744'
PARENT_COMMIT = '39c13367f4b3956631ea1e00fac6c3005fc32057'
COUNTS: dict[str, int] = {}
Poly = list[F]


def need(ok: bool, message: str, group: str = 'algebra') -> None:
    if not ok:
        raise ValueError(message)
    COUNTS[group] = COUNTS.get(group, 0) + 1


def trim(p: Poly) -> Poly:
    q = list(p)
    while len(q) > 1 and not q[-1]:
        q.pop()
    return q or [F(0)]


def add(p: Poly, q: Poly) -> Poly:
    return trim([(p[i] if i < len(p) else F(0)) +
                 (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q)))])


def scale(p: Poly, k: F) -> Poly:
    return trim([k*x for x in p])


def mul(p: Poly, q: Poly) -> Poly:
    r = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def deriv(p: Poly) -> Poly:
    return trim([i*p[i] for i in range(1, len(p))])


def value(p: Poly, x: F) -> F:
    r = F(0)
    for c in reversed(p):
        r = r*x+c
    return r


def integral(p: Poly, end: F = F(1)) -> F:
    return sum((c*end**(j+1)/F(j+1) for j, c in enumerate(p)), F(0))


def norm2(p: Poly, end: F = F(1)) -> F:
    return integral(mul(p, p), end)


def fs(x: F) -> str:
    return f'{x.numerator}/{x.denominator}'


def harmonic(n: int) -> F:
    return sum((F(1, j) for j in range(1, n+1)), F(0))


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    d: dict[str, Any] = {}
    for k, v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key: '+k)
        d[k] = v
    return d


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=no_duplicates,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def strict_equal(a: Any, b: Any) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x, y in zip(a, b))
    return a == b


def verify() -> dict[str, Any]:
    COUNTS.clear()
    lock = load(HERE/'SOURCE_LOCK.json')
    need(type(lock) is dict and lock.get('parent_commit') == PARENT_COMMIT,
         'parent commit lock mismatch', 'source_integrity')
    need(lock.get('parent_blob') == PARENT_BLOB,
         'parent blob lock mismatch', 'source_integrity')
    parent = HERE.parent/'cross-route-hardy-laguerre'/'BRIDGE.md'
    need(parent.is_file() and git_blob(parent.read_bytes()) == PARENT_BLOB,
         'parent proof blob mismatch', 'source_integrity')

    b, c = F(3,2), F(1,2)
    chi = [F(x) for x in [0,0,0,1,-3,3,-1]]
    ds = [chi]
    for _ in range(3):
        ds.append(deriv(ds[-1]))
    for k in range(3):
        need(value(ds[k], F(0)) == 0, 'left endpoint', 'bump')
        need(value(ds[k], F(1)) == 0, 'right endpoint', 'bump')
    I = [norm2(p) for p in ds]
    expected = [F(1,12012), F(1,770), F(2,35), F(36,7)]
    for x, y in zip(I, expected):
        need(x == y, 'polynomial moment mismatch', 'bump')
    # Independent beta integral for I0.
    need(I[0] == F(factorial(6)**2, factorial(13)), 'beta integral', 'bump')
    for k, ratio in enumerate([F(78,5), F(44), F(90)]):
        need(I[k+1]/I[k] == ratio, 'derivative ratio', 'bump')
        need(90*I[k]-I[k+1] >= 0, 'all-L coefficient certificate', 'bump')

    norm_fixtures = []
    for length in [F(1), F(2), F(15), F(30), F(60), F(90)]:
        phi = [coef/length**i for i, coef in enumerate(chi)]
        hp = add(deriv(deriv(phi)), scale(phi, -c*c))
        hprime = deriv(hp)
        hn, dn = norm2(hp, length), norm2(hprime, length)
        rhs_h = length*(I[2]/length**4+2*c*c*I[1]/length**2+c**4*I[0])
        rhs_d = length*(I[3]/length**6+2*c*c*I[2]/length**4+c**4*I[1]/length**2)
        need(hn == rhs_h and hn > 0, 'h norm formula', 'norms')
        need(dn == rhs_d, 'h derivative norm formula', 'norms')
        need(dn/hn <= F(90)/length**2, 'Rayleigh derivative bound', 'norms')
        for sign in [-1, 1]:
            d = sign*c
            antiderivative = add(deriv(phi), scale(phi, -d))
            need(add(deriv(antiderivative), scale(antiderivative, d)) == hp,
                 'exponential-moment identity', 'annihilation')
            need(value(antiderivative, F(0)) == 0 and
                 value(antiderivative, length) == 0,
                 'exponential-moment boundary terms', 'annihilation')
        norm_fixtures.append({'L':fs(length), 'h_norm_squared':fs(hn),
                              'derivative_norm_squared':fs(dn), 'ratio':fs(dn/hn)})

    # Certificate valid for every ell>=0, not a list of sampled ell values.
    ell = [F(0), F(1)]
    oneplus = [F(1), F(1)]
    difference = add(scale(mul(oneplus, oneplus), F(1,2)),
                     scale([F(5), F(0), F(1,2)], -F(1,10)))
    need(difference == [F(0),F(1),F(9,20)], 'uniform length polynomial', 'majorant')
    need(all(x >= 0 for x in difference), 'uniform length sign', 'majorant')
    need(1/(b*b)+F(9,2) < 5, 'majorant slack', 'majorant')
    for q in [F(0), F(1,3), F(10), F(100)]:
        for t in [F(0), F(1,2), F(1), F(5)]:
            alpha, beta = 4+2*q, 18+q*t*t
            need(beta/alpha <= max(F(9,2), t*t/2),
                 'convex ratio identity', 'majorant')
            length = 30*(1+t)
            need(F(90)/length**2*(1/(b*b)+beta/alpha) <= F(1,2),
                 'finite support margin', 'majorant')

    for j in [1,2,7,31]:
        cj = 2*j+c
        need(2*cj/(cj*cj-b*b) == F(1,2*j-1)+F(1,2*j+2),
             'gamma splitting', 'multipliers')
        for w in [F(0), F(1,3), F(2)]:
            lhs=2*cj*(w*w+b*b)/((cj*cj-b*b)*(w*w+cj*cj))
            rhs=2*cj/(cj*cj-b*b)-2*cj/(w*w+cj*cj)
            need(lhs == rhs, 'gamma rational multiplier', 'multipliers')
    for n in [1,2,4,16,64]:
        lhs=sum((F(1,2*j-1)-F(1,2*j+2) for j in range(1,n+1)),F(0))
        rhs=harmonic(2*n)-harmonic(n)/2-harmonic(n+1)/2+F(1,2)
        need(lhs == rhs, 'harmonic finite regrouping', 'multipliers')
    need(4*b/3 == 2, 'two-orientation prime multiplier', 'multipliers')
    need(b*b-c*c == 2, 'growing pole constant', 'multipliers')
    need(F(1,4)**(-3)+F(1,2)*F(1,4)**(-2) == 72,
         'digamma cubic envelope', 'constants')
    need(F(72,4) == 18, 'digamma frequency scaling', 'constants')

    # Elementary strict signs used only for the X=2 continuum-repair obstruction.
    exp_lower=sum((F(39,20)**k/F(factorial(k)) for k in range(7)),F(0))
    need(exp_lower > 7, 'log7 enclosure', 'constants')
    need(harmonic(6)-F(39,20) == F(1,2), 'Euler constant lower bound', 'constants')
    need(F(3,2)**2 > 2, 'sqrt2 upper endpoint', 'constants')
    need(F(3,2)*(4-F(2,3)) == 5, 'compensated X2 endpoint', 'constants')
    need(F(1,2)+F(3,2)+3*F(2,3)+1 == 5,
         'Omega0 negative endpoint', 'constants')

    # Independent piecewise-Laplace verification of the continuum tail.
    repair_fixtures=[]
    for X in [F(1),F(2),F(4),F(10)]:
        for k in [2,3,4]:
            r=c+k
            low= -F(1,3)/X*((1-X**(-(k-1)))/(r-b)+(1-X**(-(k+2)))/(r+b))
            high= -F(1,2)*X**(-k)/(r-c)+(X*X/6-F(1,3)/X)*X**(-(k+2))/(r+b)
            germ=(-X**(-k)/(r-c)+(r/b)/X)/(b*b-r*r)
            need(low+high == germ, 'continuum piecewise Laplace transform', 'continuum')
            repair_fixtures.append({'X':fs(X),'r':fs(r),'laplace':fs(germ)})

    # The normalized Rayleigh exponent 2aL=45(1+log X).
    need(2*F(3,4)*30 == 45, 'Rayleigh exponent', 'constants')
    need(F(4)/(2*b) == F(4,3), 'Rayleigh prefactor', 'constants')
    hashes={name:sha(HERE/name) for name in ['PROOF.md','verify_cutoff.py','SOURCE_LOCK.json']}
    return {
        'scope':'EXACT_FINITE_ALGEBRA_AND_SOURCE_INTEGRITY; analytic proofs require review; RH_UNPROVED',
        'parent_commit':PARENT_COMMIT,
        'parent_blob':PARENT_BLOB,
        'source_sha256':hashes,
        'checks':sum(COUNTS.values()),
        'check_groups':dict(sorted(COUNTS.items())),
        'bump_integrals':[fs(x) for x in I],
        'uniform_length_certificate':[fs(x) for x in difference],
        'exp_39_20_lower':fs(exp_lower),
        'norm_fixtures':norm_fixtures,
        'continuum_laplace_fixtures':repair_fixtures,
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    action=parser.add_mutually_exclusive_group()
    action.add_argument('--write',type=Path)
    action.add_argument('--check',type=Path)
    args=parser.parse_args()
    try:
        result=verify()
        encoded=json.dumps(result,sort_keys=True,indent=2)+'\n'
        if args.check is not None:
            saved=load(args.check)
            if not strict_equal(saved,result):
                raise ValueError('saved result or source digest mismatch')
        if args.write is not None:
            args.write.write_text(encoded,encoding='utf-8')
        sys.stdout.write(encoded)
    except (ValueError,OSError,TypeError,KeyError) as exc:
        print('REFUSED: '+str(exc),file=sys.stderr)
        return 1
    return 0


if __name__=='__main__':
    raise SystemExit(main())
