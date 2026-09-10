#!/usr/bin/env python3
"""Exact finite controls; the external finite-height theorem is NOT rerun."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha1, sha256
import importlib.util
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent / 'annular-scalar-route'
LOCKED = {
    'PROOF.md': '0f1b21227d064e61f4f532d9025c78106baa688e',
    'verify.py': 'a347fb454f3f1116b521cedb8dace3c23612657a',
}

def need(condition, message):
    if not condition:
        raise ValueError(message)


def primitive_module():
    for name, expected in LOCKED.items():
        data = (PARENT / name).read_bytes()
        actual = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        need(actual == expected, 'parent source mismatch: ' + name)
    spec = importlib.util.spec_from_file_location('authenticated_annular_primitives', PARENT / 'verify.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def w(u):
    u = F(u)
    if not F(1, 4) < u <= 4:
        return F(0)
    return u/3 - 1/(192*u*u) if u <= 1 else 1/(3*u*u) - u/192


def gaussian(a, b=0): return F(a), F(b)
def add(a, b): return a[0]+b[0], a[1]+b[1]
def neg(a): return -a[0], -a[1]
def sub(a, b): return add(a, neg(b))
def mul(a, b): return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def norm2(a): return a[0]*a[0]+a[1]*a[1]
def inv(a):
    d = norm2(a)
    need(d != 0, 'Gaussian zero denominator')
    return a[0]/d, -a[1]/d

def div(a, b): return mul(a, inv(b))
def scale(c, a): return F(c)*a[0], F(c)*a[1]


def reconstruct():
    expected_lock = {
        'schema': 'riemann.annular.height-transfer.v1',
        'repository': 'GettysburgResearch/riemann',
        'parent': '8d8750e5be8e0f2920db371bf31ea93c2d0a0caf',
        'parent_objects': {'annular-scalar-route/'+k: v for k, v in LOCKED.items()},
        'external_height': {'arxiv': '2004.09765v1', 'doi': '10.1112/blms.12460',
                            'theorem': '1', 'published_height': 3000175332800,
                            'used_height': 3000000000000, 'replayed': False},
    }
    need(canonical(strict_json(ROOT/'SOURCE_LOCK.json')) == canonical(expected_lock),
         'source-lock contract mismatch')
    p = primitive_module()
    I, Q = p.I, p.Q
    counts = Counter()
    def check(group, condition):
        need(condition, 'control failed: ' + group)
        counts[group] += 1

    # Primitive re-evaluation, not stored source constants.
    H = 3 * 10**12
    pi = p.pi_interval()
    C0 = p.source_constant()
    R = ((p.log_interval(I.of(H)/(2*pi))+1)/(2*pi*H)
         +(40*p.log_exact(F(H+2))+10)/(H*H))
    cmax, R0 = F(237, 5000), F(37, 25*10**12)
    check('primitive_source_bounds', F(C0.lo, Q) > 0)
    check('primitive_source_bounds', F(C0.hi, Q) < cmax)
    check('primitive_source_bounds', F(R.lo, Q) > 0)
    check('primitive_source_bounds', F(R.hi, Q) < R0)
    check('primitive_source_bounds', H < 3000175332800)

    tail = lambda m: F(85, 64)*R0*(m+2+F(1, m))
    gamma = lambda m: F(205, 128*m**5)
    budgets = [
        ('small_strong', 2, 4, F(1, 10)),
        ('large_strong', 4, 5*10**10, F(1, 10)),
        ('small_wide', 2, 16, F(1, 200)),
        ('large_wide', 16, 10**11, F(1, 200)),
    ]
    records = []
    for name, left, right, threshold in budgets:
        bound = F(1, 4)-cmax-gamma(left)-tail(right)
        check('continuum_endpoint_budgets', bound > threshold)
        records.append({'name': name, 'left': left, 'right': right,
                        'lower': str(bound), 'required': str(threshold),
                        'decimal_enclosure': I.of(bound).decimals(12)})
    check('range_coverage', budgets[0][2] == budgets[1][1])
    check('range_coverage', budgets[2][2] == budgets[3][1])
    eps = F(1887, 5*10**12)
    check('unbounded_weaker_bound', 255*R0 == eps)
    check('unbounded_weaker_bound', 192*(cmax+gamma(2))+F(1275, 2)*R0 < 19)
    check('not_an_unbounded_sharp_bound', eps*10**12 > 29)
    check('gamma_remainder_coefficient', F(1, 8)*F(2, 5)*(32+F(1, 32)) == F(205, 128))

    # The paired resolvent identity uses two copies, not four.
    b = gaussian(F(3, 2))
    b2 = mul(b, b)
    for alpha in (F(-1, 3), F(0), F(1, 4)):
        for ordinate in (F(2), F(13, 2), F(100)):
            z = gaussian(alpha, ordinate)
            z2 = mul(z, z)
            check('strip_denominator', norm2(sub(b2, z2)) >= (ordinate**2+2)**2)
            for im in (F(0), F(1, 3)):
                r = gaussian(2, im)
                r2 = mul(r, r)
                difference = sub(div(scale(2, r), sub(r2, z2)),
                                 div(scale(2, r), sub(b2, z2)))
                lhs = div(difference, sub(b2, r2))
                rhs = div(scale(2, r), mul(sub(b2, z2), sub(r2, z2)))
                check('paired_laplace_identity', lhs == rhs)

    c = F(1, 8)
    for radius in (F(1, 2), F(2, 3), F(1), F(3, 2), F(2)):
        for t in (F(-2), F(-1, 2), F(0), F(1, 2), F(2)):
            phase = gaussian((1-t*t)/(1+t*t), 2*t/(1+t*t))
            A = mul(sub(gaussian(1), scale(c*radius, phase)),
                    sub(gaussian(1), scale(c/radius, (phase[0], -phase[1]))))
            check('filter_modulus_envelope', norm2(A) <= F(85, 64)**2)

    # A zero at the lower endpoint is excluded from the tail, not counted twice.
    atoms = [(F(50), 2), (F(100), 3), (F(101), 5), (F(200), 1)]
    for cut in (F(99), F(100), F(101), F(150)):
        ncut = sum(mult for height, mult in atoms if height <= cut)
        rhs = -F(ncut)/cut**2 + sum((F(mult)/max(cut, height)**2
                                            for height, mult in atoms), F(0))
        lhs = sum((F(mult)/height**2 for height, mult in atoms if height > cut), F(0))
        check('stieltjes_endpoint', lhs == rhs)

    for u in [F(j, 16) for j in range(1, 81)]:
        check('compact_weight', 0 <= w(u) <= F(21, 64))
        check('self_reciprocity', w(1/u) == u*w(u))
    integral_lower = (F(1, 9)*(1-F(1, 8)) + F(1, 576)*(1-8))
    integral_upper = (F(1, 9)*(1-F(1, 8)) - F(1, 576)*(8-1))
    check('square_drift', integral_lower == F(49, 576))
    check('square_drift', integral_upper == F(49, 576))
    check('square_drift', integral_lower+integral_upper == F(49, 288))
    check('square_drift', F(1, 4)+F(49, 288) == F(121, 288))
    check('square_drift', 2*w(1) == F(21, 32))

    # Finite prime-factor data are only controls of the exact decomposition.
    # They are NOT an enumeration of the large continuum range.
    pp = p.prime_powers(4*24**2)
    for m in range(2, 25):
        full = defaultdict(F)
        parts = [defaultdict(F) for _ in range(3)]
        for n, prime in pp.items():
            coefficient = p.annular_coeff(m, n)
            check_equal = coefficient == w(F(n, m*m))/m
            need(check_equal, 'native weight normalization')
            exponent, remaining = 0, n
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            need(remaining == 1 and exponent >= 1, 'not a prime power')
            full[prime] += coefficient
            parts[min(exponent, 3)-1][prime] += coefficient
        check('exact_prime_power_partition', all(
            full[prime] == sum(part[prime] for part in parts) for prime in full))
    primes = [prime for n, prime in pp.items() if n == prime]
    for j in range(1, 9):
        n = 2**j
        product = 1
        for prime in primes:
            if n//2 < prime <= n:
                product *= prime
        check('dyadic_chebyshev_divisibility', comb(n, n//2) % product == 0)
        check('dyadic_chebyshev_divisibility', comb(n, n//2) < 2**n)

    payload = {
        'status': 'PASS_BOUNDED_HEIGHT_TRANSFER_CONTROLS',
        'rh_proved': False,
        'unbounded_sharp_bound_proved': False,
        'new_full_window_psd_proved': False,
        'external_verification_rerun': False,
        'large_range_enumerated': False,
        'bits': p.BITS,
        'external_height_used': H,
        'finite_scalar_range': {'real_m_min': 2, 'real_m_max': 10**11,
                                'strict_margin': '1/200'},
        'stronger_scalar_range': {'real_m_min': 2, 'real_m_max': 5*10**10,
                                  'strict_margin': '1/10'},
        'C0_enclosure': C0.bounds(), 'C0_decimal': C0.decimals(12),
        'Rbar_enclosure': R.bounds(), 'Rbar_decimal': R.decimals(26),
        'Rbar_rational_upper': str(R0),
        'unbounded_leading_coefficient_loss': str(eps),
        'continuum_budgets': records,
        'prime_square_limit': '49/288',
        'prime_only_offset': '121/288',
        'prime_partition_fixture_range': [2, 24],
        'groups': dict(sorted(counts.items())),
        'total_bounded_controls': sum(counts.values()),
        'scope': 'Finite exact arithmetic and source bindings only; analytic proofs and the external theorem require mathematical review.',
    }
    return payload


def strict_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, 'duplicate JSON key')
            result[key] = value
        return result
    def invalid(value):
        raise ValueError('non-finite JSON number: ' + value)
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=invalid)


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':'), allow_nan=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path)
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    result = reconstruct()
    if args.check:
        need(canonical(strict_json(args.check)) == canonical(result), 'stored result mismatch')
    text = json.dumps(result, sort_keys=True, indent=2, allow_nan=False)+'\n'
    if args.out:
        args.out.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
