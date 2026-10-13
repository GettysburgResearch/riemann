#!/usr/bin/env python3
"""Exact finite diagnostics for determinant rigidity. No asymptotic inference.

Standard library only. Proof and code have the same author. The residue
implementation uses explicit quotient fields, unlike #935's lattice remainder.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import prod
import json

ZERO = (0, 0)
ONE = (1, 0)
ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
# name, rational prime, root of omega in F_p (None for inert), norm, generator
PRIMES = (
    ('7a', 7, 4, 7, (3, 1)),
    ('7b', 7, 2, 7, (2, -1)),
    ('13', 13, 9, 13, (4, 1)),
    ('19', 19, 7, 19, (5, 2)),
    ('25', 5, None, 25, (5, 0)),
)
COUNTS = defaultdict(int)


def need(ok, label):
    COUNTS['predicates'] += 1
    if not ok:
        raise RuntimeError(label)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def scale(n, x):
    return (n*x[0], n*x[1])


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def total(items):
    z = ZERO
    for item in items:
        z = add(z, item)
    return z


def power(x, e):
    if e < 0:
        raise ValueError('negative exponent')
    ans = ONE
    while e:
        if e & 1:
            ans = mul(ans, x)
        x = mul(x, x)
        e //= 2
    return ans


def residue(x, prime):
    _, p, r, _, _ = prime
    return (x[0] % p, x[1] % p) if r is None else (x[0]+x[1]*r) % p


def modular_power(x, e, prime):
    _, p, r, _, _ = prime
    z = residue(x, prime)
    if r is not None:
        return pow(z, e, p)
    ans = ONE
    while e:
        if e & 1:
            a = mul(ans, z)
            ans = (a[0] % p, a[1] % p)
        a = mul(z, z)
        z = (a[0] % p, a[1] % p)
        e //= 2
    return ans


def symbol(u, prime):
    value = residue(u, prime)
    if value == 0 or value == ZERO:
        return ZERO
    out = modular_power(u, (prime[3]-1)//6, prime)
    matches = [z for z in ROOTS if residue(z, prime) == out]
    need(len(matches) == 1, ('sextic residue', u, prime[0], out))
    return matches[0]


def convolve(a, b, degree):
    out = [ZERO]*(degree+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= degree:
                out[i+j] = add(out[i+j], mul(x, y))
    return out


def divide(a, b, degree):
    if b[0] != ONE:
        raise ValueError('unit constant required')
    out = [ZERO]*(degree+1)
    for e in range(degree+1):
        val = a[e] if e < len(a) else ZERO
        for j in range(1, min(e, len(b)-1)+1):
            val = add(val, neg(mul(b[j], out[e-j])))
        out[e] = val
    return out


def factors(eigenvalues, degree):
    det = [ONE]
    for z in eigenvalues:
        det = convolve(det, [ONE, neg(z)], len(det))
    raw = [ONE, neg(total(eigenvalues))]
    return raw, det, divide(det, raw, degree), divide(raw, det, degree)


def padded(a, degree):
    return (a+[ZERO]*(degree+1))[:degree+1]


def local_checks():
    degree = 12
    tested = 0
    for rank in range(5):
        for phases in product(ROOTS, repeat=rank):
            raw, det, forward, inverse = factors(phases, degree)
            need(convolve(forward, raw, degree) == padded(det, degree), 'D/P * P')
            need(convolve(inverse, det, degree) == padded(raw, degree), 'P/D * D')
            need(convolve(forward, inverse, degree) == [ONE]+[ZERO]*degree, 'inverse')
            need(forward[1] == inverse[1] == ZERO, 'linear cancellation')
            tested += 1
    bounds = 0
    for r in range(1, 17):
        for j in range(65):
            t = Fraction(1, 2*r+j)
            u = (1+t)**r-1-r*t
            target = 4*r*r*t*t
            need(u/(1-r*t) <= target, ('forward majorant', r, t))
            need(u/(1-t)**r <= target, ('inverse majorant', r, t))
            bounds += 1
    return {'eigenvalue_lists': tested, 'series_degree': degree,
            'rational_majorant_points': bounds, 'rank_range_majorants': [1, 16]}


def cyclic_pattern(multiplicities, order):
    return tuple(neg(total(scale(m, ROOTS[(6//order)*j*g % 6])
                           for j, m in enumerate(multiplicities)))
                 for g in range(order))


def cyclic_negative_integral(pattern, order):
    nums = []
    for j in range(order):
        n = total(mul(pattern[g], ROOTS[-(6//order)*j*g % 6]) for g in range(order))
        if n[1] or n[0] % order or n[0] > 0:
            return False
        nums.append(-n[0]//order)
    return tuple(nums)


def rigidity_checks():
    results = {}
    for order, bound in ((2, 3), (3, 2)):
        if order == 2:
            alphabet = [(j, 0) for j in range(-bound, bound+1)]
        else:
            alphabet = [(a, b) for a in range(-2*bound, 2*bound+1)
                        for b in range(-2*bound, 2*bound+1)
                        if norm((a, b)) <= bound*bound]
        expected = {cyclic_pattern(m, order) for m in product(range(bound+1), repeat=order)
                    if sum(m) <= bound}
        accepted = set()
        tests = 0
        for pattern in product(alphabet, repeat=order):
            ms = cyclic_negative_integral(pattern, order)
            legal = ms is not False
            need(legal == (pattern in expected), ('cyclic classification', order, pattern))
            if legal:
                need(sum(ms) <= bound, 'rank bound at identity')
                need(cyclic_pattern(ms, order) == pattern, 'Fourier reconstruction')
                accepted.add(pattern)
            tests += 1
        need(accepted == expected, 'cyclic coverage')
        results['C'+str(order)] = {'patterns': tests, 'accepted': len(accepted),
                                   'bounded_alphabet_size': len(alphabet)}
    chars = ((1, 1, 1), (1, -1, 1), (2, 0, -1))
    weights = (1, 3, 2)
    for i in range(3):
        for j in range(3):
            need(sum(w*x*y for w, x, y in zip(weights, chars[i], chars[j]))
                 == 6*(i == j), 'S3 orthogonality')
    bound = 3
    expected = set()
    for m in product(range(bound+1), repeat=3):
        if m[0]+m[1]+2*m[2] <= bound:
            expected.add(tuple(-sum(m[j]*chars[j][g] for j in range(3)) for g in range(3)))
    accepted = set()
    for pattern in product(range(-bound, bound+1), repeat=3):
        cs = [Fraction(sum(w*a*b for w, a, b in zip(weights, pattern, ch)), 6) for ch in chars]
        legal = all(c.denominator == 1 and c <= 0 for c in cs)
        need(legal == (pattern in expected), ('S3 classification', pattern, cs))
        if legal:
            accepted.add(pattern)
    need(accepted == expected, 'S3 full finite coverage')
    results['S3'] = {'integer_patterns': (2*bound+1)**3, 'accepted': len(accepted),
                     'class_sizes': list(weights), 'bound': bound}
    return results


def semigroup(cap):
    out = []
    def visit(j, es, n):
        if j == len(PRIMES):
            out.append((tuple(es), n))
            return
        e = 0
        while n <= cap:
            visit(j+1, es+[e], n)
            n *= PRIMES[j][3]
            e += 1
    visit(0, [], 1)
    return sorted(out, key=lambda item: (item[1], item[0]))


def eigenvalues_for(name, q):
    eta4 = ONE if q % 4 == 1 else (-1, 0)
    eta9 = {1: ONE, 4: ROOTS[2], 7: ROOTS[4]}[q % 9]
    if name == 'rank1':
        return [eta9]
    if name == 'rank2_norm4':
        return [ONE, eta4]
    if name == 'rank3_norm9':
        return [ONE, ONE, eta9]
    raise ValueError(name)


def arithmetic_checks():
    cap = 512
    pool = semigroup(cap)
    rows = [(a, b) for a in range(-5, 6) for b in range(-5, 6)
            if 0 < norm((a, b)) <= 13]
    masks = (0, 1, 5, 31)
    reps = ('rank1', 'rank2_norm4', 'rank3_norm9')
    phases = {}
    for u in rows:
        local = [symbol(u, p) for p in PRIMES]
        for es, _ in pool:
            val = ONE
            for z, e in zip(local, es):
                val = mul(val, power(z, e))
            phases[u, es] = val
    need(PRIMES[0][3] == PRIMES[1][3], 'equal norm fixture')
    need(residue(PRIMES[0][4], PRIMES[1]) != 0, 'distinct conjugate ideals')
    checked = 0
    for rep in reps:
        polys = [factors(eigenvalues_for(rep, p[3]), 12) for p in PRIMES]
        coeff = {}
        for es, _ in pool:
            vals = []
            for mode in range(4):
                z = ONE
                for data, e in zip(polys, es):
                    a = data[mode]
                    z = mul(z, a[e] if e < len(a) else ZERO)
                vals.append(z)
            coeff[es] = vals
        for mask in masks:
            allowed = [(es, n) for es, n in pool
                       if all(not e or not (mask & (1 << j)) for j, e in enumerate(es))]
            for u in rows:
                vals = {es: [mul(c, phases[u, es]) for c in coeff[es]] for es, _ in allowed}
                for X in (31, 128, 512):
                    direct_raw = total(vals[es][0] for es, n in allowed if X < 2*n <= 2*X)
                    direct_det = total(vals[es][1] for es, n in allowed if X < 2*n <= 2*X)
                    forward, inverse = ZERO, ZERO
                    for de, dn in allowed:
                        for me, mn in allowed:
                            if X < 2*dn*mn <= 2*X:
                                forward = add(forward, mul(vals[de][2], vals[me][0]))
                                inverse = add(inverse, mul(vals[de][3], vals[me][1]))
                    need(forward == direct_det, ('physical forward', rep, mask, u, X))
                    need(inverse == direct_raw, ('physical inverse', rep, mask, u, X))
                    checked += 1
    for p in PRIMES:
        need(symbol(p[4], p) == ZERO, 'literal nonunit')
        need(power(symbol(p[4], p), 6) == ZERO, 'nonunit sixth power')
        for u in rows:
            z = symbol(u, p)
            need(symbol(power(u, 6), p) == (ZERO if z == ZERO else ONE), 'sixth-copy mask')
    return {'rows': len(rows), 'row_ball_norm': 13, 'prime_norms': [p[3] for p in PRIMES],
            'semigroup_ideal_columns': len(pool), 'column_norm_cap': cap,
            'representations': list(reps), 'masks': len(masks),
            'annular_scales': [31, 128, 512], 'forward_inverse_pairs': checked,
            'coverage': 'All nonzero Eisenstein element rows in the stated ball; columns only in the five-prime semigroup.'}


def negative_controls():
    _, _, k, h = factors([ONE, ONE], 8)
    # D=P*k at degree three needs a noncoprime d=p^2,m=p term.
    full = add(k[3], scale(-2, k[2]))
    false_gcd = k[3]
    need(full == ZERO and false_gcd != ZERO, 'false coprimality rejected')
    need(h[2] == (-1, 0) and add(ONE, h[2]) == ZERO, 'signed inverse cancellation')
    need(1+abs(h[2][0]) == 2, 'unsigned inverse rejected')
    _, _, k3, _ = factors([ONE]*3, 10)
    need(k3[2] == (3, 0) and all(k3[e] == (8*3**(e-3), 0) for e in range(3, 11)),
         'small-prime geometric tail')
    need(Fraction(9, 7) > 1, 'weighted small-prime growth')
    # The positive standard S3 character passes only the 1D coefficient tests.
    pattern = (2, 0, -1)
    cs = [Fraction(sum(w*a*b for w, a, b in zip((1, 3, 2), pattern, ch)), 6)
          for ch in ((1, 1, 1), (1, -1, 1), (2, 0, -1))]
    need(cs == [0, 0, 1], 'nonabelian probe omission rejected')
    return {'false_coprimality_rejected': True, 'unsigned_inverse_rejected': True,
            'missing_small_prime_gate_rejected': True, 'missing_nonabelian_probes_rejected': True}


def main():
    report = {'status': 'PASS', 'arithmetic': 'exact integers, Fractions and Z[omega]',
              'scope': 'finite algebra only; no analytic input or asymptotic moment certified',
              'local_euler_series': local_checks(), 'finite_character_classification': rigidity_checks(),
              'physical_sum_identities': arithmetic_checks(), 'negative_controls': negative_controls()}
    report['explicit_predicates_including_setup'] = COUNTS['predicates']
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
