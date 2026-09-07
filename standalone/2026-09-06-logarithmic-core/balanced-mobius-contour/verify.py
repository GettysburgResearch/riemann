#!/usr/bin/env python3
"""Bounded exact algebra checks, not a numerical contour or an RH proof."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'README.md', 'PROOF.md', 'SOURCES.json', 'VALIDATION.md',
         'verify.py', 'result.json', 'test_rejections.py', 'SHA256SUMS'}
PARENT_SHA = '036e9d3d7b429e9ac8d850e81910c53addfa1d9654050732cfc3dc8bcc4e47c7'
PARENT_BLOB = '046a12cd9233aa7d8a9a3a5d4d4c64a67d4207be'
HEAD = '47b8a507aea0ad6e1dd0ab23dfd2035a0eb03abb'
# A formal polynomial is {sorted tuple of variable names: rational coefficient}.
P = dict[tuple[str, ...], Q]

def const(x: int | Q) -> P:
    return {(): Q(x)} if x else {}

def var(x: str) -> P:
    return {(x,): Q(1)}

def add(a: P, b: P) -> P:
    c = a.copy()
    for k, v in b.items():
        c[k] = c.get(k, Q(0)) + v
        if not c[k]:
            del c[k]
    return c

def scale(a: P, q: int | Q) -> P:
    return {k: v*q for k, v in a.items() if v*q}

def mul(a: P, b: P) -> P:
    c: P = {}
    for k, v in a.items():
        for l, w in b.items():
            key = tuple(sorted(k+l))
            c[key] = c.get(key, Q(0)) + v*w
    return {k: v for k, v in c.items() if v}

def summ(items) -> P:
    out: P = {}
    for item in items:
        out = add(out, item)
    return out

@lru_cache(None)
def factors(n: int) -> tuple[tuple[int, int], ...]:
    if n < 1:
        raise ValueError('positive integer required')
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p; e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)

@lru_cache(None)
def logp(n: int) -> P:
    return {('log:'+str(p),): Q(e) for p, e in factors(n)}

@lru_cache(None)
def mangoldt(n: int) -> P:
    f = factors(n)
    return var('log:'+str(f[0][0])) if len(f) == 1 else {}

def mu_sieve(n: int) -> list[int]:
    out = [1]*(n+1); out[0] = 0
    composite = [False]*(n+1)
    for p in range(2, n+1):
        if not composite[p]:
            for k in range(p, n+1, p):
                composite[k] = True; out[k] *= -1
            for k in range(p*p, n+1, p*p):
                out[k] = 0
    return out

def conv(a: dict[int, P], b: dict[int, P], bound: int) -> dict[int, P]:
    out: dict[int, P] = {}
    for n, v in a.items():
        if not v:
            continue
        for k, w in b.items():
            if n*k <= bound and w:
                out[n*k] = add(out.get(n*k, {}), mul(v, w))
    return {n: v for n, v in out.items() if v}

def scaled_completion(y: int) -> tuple[dict[int, P], P, P]:
    """Return coefficients log(2)*p_Y, and log(2)*a_Y, log(2)*b_Y."""
    mu = mu_sieve(y)
    mass = sum((Q(mu[n], n) for n in range(1, y)), Q(0))
    ell = scale(summ(logp(n) for n in range(y, 2*y)), Q(1, y))
    moment = summ(scale(logp(n), Q(mu[n], n)) for n in range(1, y))
    b = add(add(scale(ell, mass), scale(moment, -1)), const(-1))
    a = add(scale(logp(2), -mass), scale(b, -1))
    p = {n: scale(logp(2), mu[n]) for n in range(1, y) if mu[n]}
    for n in range(y, 2*y):
        p[n] = scale(a, Q(n, y))
        p[2*n] = scale(b, Q(2*n, y))
    return p, a, b

def perturbation(y: int) -> dict[int, P]:
    out: dict[int, P] = {}
    for n in range(y, 2*y):
        for d, c in ((1, 1), (2, -4), (4, 4)):
            out[d*n] = const(Q(c*n, y))
    return out

def proxy(p: dict[int, P], bound: int) -> dict[int, P]:
    """log(2)^2 times coefficients of mathscr L_{p/log2}."""
    logarithm = {n: logp(n) for n in range(2, bound+1)}
    one = {n: const(1) for n in range(1, bound+1)}
    linear = conv(p, logarithm, bound)
    quadratic = conv(conv(p, p, bound), conv(one, logarithm, bound), bound)
    return {n: add(scale(mul(logp(2), linear.get(n, {})), 2),
                   scale(quadratic.get(n, {}), -1)) for n in range(1, bound+1)}

def weight(u: Q) -> Q:
    if Q(1, 4) < u <= 1:
        return u/3-Q(1, 192)/u**2
    if 1 < u < 4:
        return Q(1, 3)/u**2-u/192
    return Q(0)

# Independent accepting elementary logarithm enclosures. No floats.
BITS = 144
DEN = 1 << BITS

def atanh_log(u: Q) -> tuple[Q, Q]:
    z = (u-1)/(u+1)
    if not 0 <= z <= Q(1, 3):
        raise ValueError('log range')
    total = Q(0); power = z
    terms = 100
    for j in range(terms):
        total += 2*power/(2*j+1); power *= z*z
    error = 2*power/((2*terms+1)*(1-z*z))
    return total, total+error

@lru_cache(None)
def log_interval(n: int) -> tuple[Q, Q]:
    if n < 1:
        raise ValueError('positive log input')
    r = n.bit_length()-1
    a, b = atanh_log(Q(n, 1 << r))
    c, d = atanh_log(Q(2))
    a += r*c; b += r*d
    lo = (a.numerator*DEN)//a.denominator
    hi = -((-b.numerator*DEN)//b.denominator)
    return Q(lo, DEN), Q(hi, DEN)

def iadd(a, b):
    return a[0]+b[0], a[1]+b[1]

def imul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)

def idiv(a, b):
    if b[0] <= 0 <= b[1]:
        raise ValueError('interval division through zero')
    return imul(a, (1/b[1], 1/b[0]))

def evaluate(p: P) -> tuple[Q, Q]:
    out = (Q(0), Q(0))
    for mon, coeff in p.items():
        term = (coeff, coeff)
        for v in mon:
            if not v.startswith('log:'):
                raise ValueError('non-log symbol')
            term = imul(term, log_interval(int(v[4:])))
        out = iadd(out, term)
    return out

def rational(x: Q) -> str:
    return str(x.numerator)+'/'+str(x.denominator)

def poly_json(p: P):
    return [[list(k), rational(v)] for k, v in sorted(p.items())]

def reconstruct() -> dict:
    checks: Counter = Counter(); digest = hashlib.sha256()
    def check(ok: bool, group: str):
        if not ok:
            raise ValueError('mathematical control: '+group)
        checks[group] += 1
    mu = mu_sieve(512)
    for n in range(1, 513):
        f = factors(n)
        expected = 0 if any(e >= 2 for _, e in f) else (-1)**len(f)
        check(mu[n] == expected, 'independent_mobius_sieve')
    for n in range(1, 65):
        check(sum(Q(mu[d], d)*sum((Q(1,k) for k in range(1,n//d+1)),Q(0))
                  for d in range(1,n+1)) == 1, 'harmonic_divisor_identity')
    for y in range(2, 25):
        p,a,b = scaled_completion(y)
        check(summ(scale(v,Q(1,n)) for n,v in p.items()) == {}, 'two_exact_jets')
        deriv = summ(scale(mul(v,logp(n)),Q(-1,n)) for n,v in p.items())
        check(deriv == logp(2), 'two_exact_jets')
        exact = summ(scale(mul(v,v),Q(1,n)) for n,v in p.items())
        expected = add(scale(mul(logp(2),logp(2)),
                             sum((Q(mu[n]**2,n) for n in range(1,y)),Q(0))),
                       scale(add(mul(a,a),scale(mul(b,b),2)),Q(3*y-1,2*y)))
        check(exact == expected, 'diagonal_norm_identity')
        ai=idiv(evaluate(a),log_interval(2)); bi=idiv(evaluate(b),log_interval(2))
        check(-6<ai[0]<=ai[1]<6 and -5<bi[0]<=bi[1]<5,
              'bounded_actual_completion_constants')
        digest.update(json.dumps([y,poly_json(a),poly_json(b)],separators=(',',':')).encode())
        e=perturbation(y)
        check(summ(scale(v,Q(1,n)) for n,v in e.items()) == {}, 'homogeneous_jets_norm')
        check(summ(scale(mul(v,logp(n)),Q(1,n)) for n,v in e.items()) == {},
              'homogeneous_jets_norm')
        en=summ(scale(mul(v,v),Q(1,n)) for n,v in e.items())
        check(en == const(Q(13*(3*y-1),2*y)), 'homogeneous_jets_norm')
    l2sq=mul(logp(2),logp(2))
    for y in (2,3,4,5,8):
        p,_,_=scaled_completion(y); bound=2*y*y
        out=proxy(p,bound)
        for n in range(1,bound):
            check(out[n] == mul(mangoldt(n),l2sq), 'exact_prefix_reconstruction')
        residual=add(scale(logp(2),mu[y]),scale(p[y],-1))
        defect=add(mul(mangoldt(bound),l2sq),scale(out[bound],-1))
        check(defect == mul(logp(2),mul(residual,residual)), 'first_omitted_coefficient')
        digest.update(json.dumps([y,poly_json(defect)],separators=(',',':')).encode())
    native=[]
    for y in (4,6,8,10):
        m=Q(y,2); bound=y*y
        p,_,_=scaled_completion(y); out=proxy(p,bound)
        native_sum=summ(scale(mangoldt(n),weight(Q(n)/m**2)/m)
                        for n in range(1,bound+1))
        reconstructed=summ(scale(out[n],weight(Q(n)/m**2)/m)
                          for n in range(1,bound+1))
        check(reconstructed == mul(native_sum,l2sq), 'full_annular_scalar_identity')
        scalar=add(native_sum,const(-Q(45,128)*m+Q(1,4)))
        value=evaluate(scalar)
        native.append({'m':rational(m),'D_interval':[rational(x) for x in value]})
    for y in (4,6,8):
        p,_,_=scaled_completion(y); e=perturbation(y); bound=y*y
        base=proxy(p,bound)
        for sign in (-1,1):
            moved=p.copy()
            for n,v in e.items():
                moved[n]=add(moved.get(n,{}),scale(mul(logp(2),v),sign))
            image=proxy(moved,bound)
            check(image == base, 'source_preserving_null_directions')
    # Laurent expansion: -2 p zeta' + p^2 zeta zeta'.
    d,e,g0,g1,g2=(var('v:'+x) for x in ('d','e','g0','g1','g2'))
    def laurent(a,b):
        c={}
        for i,x in a.items():
            for j,y in b.items():
                c[i+j]=add(c.get(i+j,{}),mul(x,y))
        return c
    p={1:d,2:e}; z={-1:const(1),0:g0,1:g1,2:g2}
    zp={-2:const(-1),0:g1,1:scale(g2,2)}
    first=laurent(p,zp); second=laurent(laurent(p,p),laurent(z,zp))
    residue=add(scale(first.get(-1,{}),-2),second.get(-1,{}))
    check(residue == add(scale(d,2),scale(mul(d,d),-1)), 'principal_part')
    check(not any(second.get(k) or first.get(k) for k in (-3,-2)), 'principal_part')
    check(weight(Q(1,4))==weight(Q(4))==0 and weight(Q(1))==Q(21,64),
          'kernel_and_tail_constants')
    check(Q(3,2)*(6**2+2*5**2)==129, 'kernel_and_tail_constants')
    check(Q(13*3,2)==Q(39,2), 'kernel_and_tail_constants')
    for n in range(2,13):
        for k in range(1,n):
            diff=(log_interval(n)[0]-log_interval(k)[1])
            check(diff >= Q(n-k,n), 'mean_value_spacing_bound')
    eps=Q(1,8)
    check(-Q(1,2)+eps<0 and -Q(3,4)+eps/2<-Q(1,2)+eps,
          'kernel_and_tail_constants')
    return {'schema':'bmc-v1','parent_head':HEAD,
            'status':'PROPOSED_COMPONENT_PROOFS_END_TO_END_BOUND_OPEN',
            'rh_proved':False,'native_count_power_saving_proved':False,
            'contour_integral_numerically_evaluated':False,
            'groups':dict(sorted(checks.items())), 'bounded_checks':sum(checks.values()),
            'symbolic_completion_digest':digest.hexdigest(),
            'small_native_scalar_fixtures':native,
            'scope':{'mobius_sieve_max':512,'completion_Y_max':24,
                     'proxy_Y_cases':[2,3,4,5,8], 'annular_Y_cases':[4,6,8,10],
                     'accepting_arithmetic':'Fraction formal polynomials and 144-bit outward logs',
                     'analytic_proof_status':'paper arguments; no formal or independent acceptance'}}

def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key')
        d[k]=v
    return d

def read_json(path:Path):
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates,
                      parse_float=lambda _:(_ for _ in ()).throw(ValueError('float forbidden')))

def strict_equal(a,b):
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b

def authenticate():
    found=set()
    for p in ROOT.rglob('*'):
        if p.is_symlink():
            raise ValueError('symlink forbidden')
        if p.is_file():
            found.add(p.relative_to(ROOT).as_posix())
    if found!=FILES:
        raise ValueError('packet inventory')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,name=line.split('  ')
        if name in entries or name not in FILES-{'SHA256SUMS'}:
            raise ValueError('manifest inventory')
        entries[name]=h
    if entries.keys()!=FILES-{'SHA256SUMS'}:
        raise ValueError('manifest coverage')
    for name,h in entries.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=h:
            raise ValueError('digest mismatch: '+name)
    parent=ROOT.parent/'sparse-sign-bootstrap'/'PROOF.md'
    b=parent.read_bytes()
    if parent.is_symlink() or hashlib.sha256(b).hexdigest()!=PARENT_SHA:
        raise ValueError('parent source mismatch')
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if blob!=PARENT_BLOB:
        raise ValueError('parent Git identity')
    src=read_json(ROOT/'SOURCES.json')
    if src.get('parent_head')!=HEAD or src.get('parent_proof_blob')!=PARENT_BLOB:
        raise ValueError('source lock mismatch')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    if args.write and args.check:
        raise ValueError('choose write or check')
    if args.check:
        authenticate()
    result=reconstruct()
    if args.write:
        args.write.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    if args.check and not strict_equal(result,read_json(args.check)):
        raise ValueError('reconstruction mismatch')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REFUSED: '+str(exc),file=sys.stderr)
        sys.exit(1)
