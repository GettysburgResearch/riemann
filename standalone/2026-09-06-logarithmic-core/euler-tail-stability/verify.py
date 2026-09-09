#!/usr/bin/env python3
"""Bounded exact controls, not a proof of the infinite analytic theorems."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import math
import sys

HERE = Path(__file__).resolve().parent
FILES = {
    'PROOF.md', 'README.md', 'SOURCES.md', 'SOURCE_LOCK.json',
    'VALIDATION.md', 'ATTEMPT_LEDGER.md', 'verify.py',
    'test_rejections.py', 'result.json', 'SHA256SUMS',
}
PARENT = '93e5d45b63f6a9a60f981e81df589feff1ba1cfb'
PARENTS = {
    'annular-scalar-route/PROOF.md': '0f1b21227d064e61f4f532d9025c78106baa688e',
    'height-transfer-and-prime-squares/PROOF.md': '2ee61d78b5bcf8e06de973f7e29634112c37e1a9',
}
SCOPE = {
    'rh_proved': False,
    'native_unbounded_sign_proved': False,
    'new_full_window_certificate': False,
    'global_model_parameters_numerically_certified': False,
    'analytic_theorems_machine_proved': False,
    'external_zero_verification_replayed': False,
    'bounded_exact_checks_only': True,
}
COUNTS: Counter[str] = Counter()

def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def check(group: str, condition: bool) -> None:
    need(condition, 'ARITHMETIC:' + group)
    COUNTS[group] += 1

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()

def unique_object(pairs):
    out = {}
    for key, val in pairs:
        need(key not in out, 'DUPLICATE_JSON_KEY')
        out[key] = val
    return out

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)

def exact_equal(left, right) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(exact_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(exact_equal(x, y) for x, y in zip(left, right))
    return left == right

def authenticate_parents(parent_root: Path) -> None:
    lock = load_json(HERE / 'SOURCE_LOCK.json')
    need(set(lock) == {'schema','repository','parent_head','files'}, 'SOURCE_TOP_FIELDS')
    need(lock.get('repository') == 'GettysburgResearch/riemann', 'SOURCE_REPOSITORY')
    need(lock.get('parent_head') == PARENT, 'SOURCE_HEAD')
    need(lock.get('schema') == 'riemann.euler-tail-stability.sources.v1', 'SOURCE_SCHEMA')
    entries = lock.get('files')
    need(type(entries) is list and len(entries) == len(PARENTS), 'SOURCE_COVERAGE')
    by_path = {}
    for entry in entries:
        need(type(entry) is dict and set(entry) == {'relative_path', 'git_blob', 'sha256'}, 'SOURCE_FIELDS')
        path = entry['relative_path']
        need(path not in by_path, 'SOURCE_DUPLICATE')
        by_path[path] = entry
    need(set(by_path) == set(PARENTS), 'SOURCE_COVERAGE')
    for rel, expected in PARENTS.items():
        data = (parent_root / rel).read_bytes()
        need(git_blob(data) == expected == by_path[rel]['git_blob'], 'PARENT_BLOB:' + rel)
        need(hashlib.sha256(data).hexdigest() == by_path[rel]['sha256'], 'PARENT_SHA256:' + rel)

def authenticate_delivery() -> None:
    need(not any(p.is_symlink() for p in HERE.rglob('*')), 'DELIVERY_SYMLINK')
    actual = {str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file()}
    need(actual == FILES, 'DELIVERY_COVERAGE')
    rows = {}
    for line in (HERE / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        need(name not in rows and name in FILES - {'SHA256SUMS'}, 'MANIFEST_PATH')
        rows[name] = digest
    need(set(rows) == FILES - {'SHA256SUMS'}, 'MANIFEST_COVERAGE')
    for name, digest in rows.items():
        need(hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest, 'MANIFEST_HASH:' + name)

# Exact rational complex arithmetic. No float, optimizer, or special-function package.
def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def cpow(x, k):
    y = (Q(1), Q(0))
    for _ in range(k): y = cmul(y, x)
    return y

def w(u):
    if Q(1, 4) < u <= 1: return u/3 - 1/(192*u*u)
    if 1 < u <= 4: return 1/(3*u*u) - u/192
    return Q(0)

def v(u):
    if Q(1, 4) < u < 1: return -u - 1/(64*u*u)
    if 1 < u < 4: return 1/(u*u) + u/64
    return Q(0)

def rational_integral(terms, a, b):
    total = Q(0)
    for power, coeff in terms.items():
        need(power != -1, 'LOG_IN_RATIONAL_INTEGRAL')
        total += coeff*(b**(power+1) - a**(power+1))/(power+1)
    return total

def factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1: out[n] = out.get(n, 0) + 1
    return out

def power4(t):
    # Used only for half-integer t, so 4^t=2^(2t) is rational.
    e = 2*t
    need(e.denominator == 1, 'POWER_DOMAIN')
    return Q(2)**e.numerator

@lru_cache(None)
def log_interval(n: int):
    """ln(n) using positive atanh series, then outward dyadic rounding."""
    need(n >= 1, 'LOG_DOMAIN')
    bits, N = 160, 64
    k = n.bit_length()-1
    y = Q(n, 2**k)
    def series(z):
        ans = Q(0)
        zp = z
        for j in range(N):
            ans += 2*zp/(2*j+1)
            zp *= z*z
        err = 2*zp/((2*N+1)*(1-z*z))
        return ans, ans+err
    lo2, hi2 = series(Q(1, 3))
    lo, hi = series((y-1)/(y+1))
    lo, hi = lo+k*lo2, hi+k*hi2
    den = 1 << bits
    low_num = (lo.numerator*den)//lo.denominator
    high_num = -((-hi.numerator*den)//hi.denominator)
    return Q(low_num, den), Q(high_num, den)

def interval_sum_log(coefficients):
    lo = hi = Q(0)
    for p, c in coefficients.items():
        l, h = log_interval(p)
        if c >= 0: lo += c*l; hi += c*h
        else: lo += c*h; hi += c*l
    return lo, hi

def build_result(parent_root: Path):
    COUNTS.clear()
    authenticate_parents(parent_root)
    a = Q(45, 128)
    # Primitive identities and bounds of the native weight.
    for i in range(1, 81):
        t = Q(i, 16)
        check('weight_geometry', 0 <= w(t) <= Q(21, 64) and w(1/t) == t*w(t))
    check('exact_integrals', rational_integral({1: Q(1,3), -2: -Q(1,192)}, Q(1,4), Q(1))
          + rational_integral({-2: Q(1,3), 1: -Q(1,192)}, Q(1), Q(4)) == a)
    check('exact_integrals', rational_integral({1: -Q(1), -2: -Q(1,64)}, Q(1,4), Q(1))
          + rational_integral({-2: Q(1), 1: Q(1,64)}, Q(1), Q(4)) == a)
    # u=t^2 makes the critical Mellin moment rational to integrate.
    check('exact_integrals', rational_integral({2: Q(2,3), -4: -Q(1,96)}, Q(1,2), Q(1))
          + rational_integral({-4: Q(2,3), 2: -Q(1,96)}, Q(1), Q(2)) == Q(49,144))
    check('exact_integrals', rational_integral({-2: Q(1), 1: Q(1,64)}, Q(1), Q(4)) == Q(111,128))
    # Direct integral versus closed Mellin symbol at real half-integers.
    for j in range(-6, 9):
        z = Q(j, 2)
        if z in (-1, 2): continue
        q = power4(z)
        direct = (1-1/(4*q))/(3*(z+1)) - (1-16/q)/(192*(z-2))
        direct += (q/16-1)/(3*(z-2)) - (4*q-1)/(192*(z+1))
        A = Q(65,64)-q/16-1/(4*q)
        check('mellin_symbol', direct == A/(Q(9,4)-(z-Q(1,2))**2) and direct > 0)
    check('slope_constants', -3*Q(65,64)-a == -Q(435,128))
    check('slope_constants', 3*(Q(65,64)+Q(111,128))-a == Q(339,64))
    check('slope_constants', Q(9,2)*Q(241,128)-a == Q(2079,256) < 9)
    check('slope_constants', Q(5,16)**3 < Q(1,32))
    check('slope_constants', Q(81,16)-3*Q(5,16) == Q(33,8))
    check('slope_constants', Q(49,144)*Q(72,245) == Q(1,10))
    check('slope_constants', sum(Q(3,4)**k/math.factorial(k) for k in range(4)) > 2)
    for i in range(4, 17):
        t = Q(i,16)
        check('slope_envelope', Q(65,64)-t-1/(64*t*t)
              == (1-t)*(64*t*t-t-1)/(64*t*t) >= 0)
    # Independently reconstruct the binomial factorization controlling every prime power.
    for n in range(1, 33):
        valuations = factors(math.comb(2*n,n))
        reconstructed = {}
        for p in range(2, 2*n+1):
            if len(factors(p)) != 1 or factors(p).get(p) != 1: continue
            pk, value = p, 0
            while pk <= 2*n:
                digit = (2*n)//pk - 2*(n//pk)
                need(digit in (0,1), 'BINOMIAL_DIGIT')
                if n < pk: need(digit == 1, 'PRIME_POWER_OMITTED')
                value += digit
                pk *= p
            if value: reconstructed[p] = value
        check('binomial_prime_powers', reconstructed == valuations and math.comb(2*n,n) <= 2**(2*n))
    units = [(Q(1),Q(0)),(-Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),(-Q(5,13),Q(12,13))]
    for r in [Q(0),Q(1,16),Q(1,8),Q(1,4)]:
        for unit in units:
            check('euler_units', unit[0]**2+unit[1]**2 == 1)
            order = 12
            lam = [Q(0)] + [1-2*r**k*cpow(unit,k)[0] for k in range(1,order+1)]
            ordinary = [Q(1), 1-2*r*unit[0]] + [1-2*r*unit[0]+r*r]*(order-1)
            for k in range(1,order+1):
                check('euler_positive_coefficients', Q(1,2) <= lam[k] <= Q(3,2) and ordinary[k] > 0)
                check('euler_log_identity', k*ordinary[k] == sum(lam[j]*ordinary[k-j] for j in range(1,k+1)))
            ck = [Q(1)] + [Q(0)]*order
            for degree in range(1,7):
                ck = [k*ck[k]+sum(lam[j]*ck[k-j] for j in range(1,k+1)) for k in range(order+1)]
                check('selberg_recurrence', all(c >= 0 for c in ck))
            check('local_factor_numerator', ordinary[2]-ordinary[1] == r*r)
    # The native unweighted divisor identity is additional information, not preserved automatically.
    check('native_identity_separation', 1-2*Q(1,4)*Q(3,5) == Q(7,10) != 1)
    # Full geometric prime-power contribution at phase pi, with exact residual.
    for r in [Q(1,4),Q(1,8),Q(1,16),Q(1,32)]:
        for n in range(1,10):
            finite = sum((-r)**k for k in range(1,n+1))
            remainder = (-r)**(n+1)/(1+r)
            check('prime_phase_tail', finite+remainder == -r/(1+r) < 0)
    # Native slopes at rational points, including all prime powers in their annuli.
    slope_receipts = []
    for j in range(2,10):
        m = Q(j)+Q(1,3)
        X = m*m
        N = (4*X).numerator//(4*X).denominator
        coeff = {}
        for n in range(2,N+1):
            fac = factors(n)
            if len(fac) == 1:
                p = next(iter(fac))
                coeff[p] = coeff.get(p,Q(0))+v(Q(n)/X)/X
        lo, hi = interval_sum_log(coeff)
        lo -= a; hi -= a
        check('native_slope_intervals', -Q(435,128) <= lo <= hi <= Q(339,64))
        receipt_den = 1 << 64
        receipt_lo = Q((lo.numerator*receipt_den)//lo.denominator, receipt_den)
        receipt_hi = Q(-((-hi.numerator*receipt_den)//hi.denominator), receipt_den)
        need(receipt_lo <= lo <= hi <= receipt_hi, 'RECEIPT_ROUNDING')
        slope_receipts.append({'m':str(m),'lower':str(receipt_lo),'upper':str(receipt_hi),'largest_integer':N})
    # Exact divided-difference replacement of the sharp positive mass transfer.
    check('comparison_constants', Q(21,64)*12 == Q(63,16))
    check('comparison_constants', Q(339,64) > Q(435,128))
    return {
        'schema':'riemann.euler-tail-stability.checks.v1',
        'status':'PASS_BOUNDED_EXACT_CONTROLS',
        'scope':SCOPE,
        'parent_head':PARENT,
        'parent_proof_blobs':PARENTS,
        'groups':dict(sorted(COUNTS.items())),
        'total_controls':sum(COUNTS.values()),
        'native_slope_receipts':slope_receipts,
        'claimed_new_native_positive_range':None,
        'global_parameter_certificate':None,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-root', type=Path, default=HERE.parent)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--validate', action='store_true')
    args = parser.parse_args()
    if args.check or args.validate: authenticate_delivery()
    result = build_result(args.parent_root)
    if args.check:
        supplied = load_json(args.check)
        need(exact_equal(supplied, result), 'RESULT_MISMATCH')
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('REJECT:' + str(exc), file=sys.stderr)
        raise SystemExit(2)
