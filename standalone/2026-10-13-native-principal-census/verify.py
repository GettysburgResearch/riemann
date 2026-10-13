#!/usr/bin/env python3
"""Bounded exact reconstructions. Not a proof of an asymptotic moment bound."""
from collections import Counter, defaultdict
from itertools import combinations, product
import json
import math
import census as c

CHECKS = Counter()

def need(ok, label):
    if not ok:
        raise RuntimeError(label)
    CHECKS[label] += 1

def add(x, y):
    return x[0]+y[0], x[1]+y[1]

def mul(x, y):
    a, b = x
    d, e = y
    return a*d-b*e, a*e+b*d-b*e

def scale(a, x):
    return a*x[0], a*x[1]

def rem(x, p):
    a, b = p
    N = c.norm(p)
    num = mul(x, (a-b, -b))
    i, j = num[0]//N, num[1]//N
    poss = [add(x, scale(-1, mul((s, t), p)))
            for s in range(i-1, i+3) for t in range(j-1, j+3)]
    return min(poss, key=lambda v: (c.norm(v), v))

def modpower(x, e, p):
    out, x = rem((1, 0), p), rem(x, p)
    while e:
        if e & 1:
            out = rem(mul(out, x), p)
        x = rem(mul(x, x), p)
        e //= 2
    return out

def geometric_ideals(D):
    bnd = math.isqrt(4*D//3)+1
    # The half-open sector 0 <= b < a has exactly one generator per ideal.
    return [(a, b) for a in range(1, bnd+1) for b in range(a)
            if c.norm((a, b)) <= D and not (a % 2 == b % 2 == 0)
            and (a+b) % 3 != 0]

def generator(prime):
    q, p, r, _ = prime
    if r is None:
        return (p, 0)
    return next(v for v in geometric_ideals(q)
                if c.norm(v) == q and (v[0]+r*v[1]) % p == 0)

def coverage():
    D = 256
    primes = c.prime_ideals(D)
    ideals = c.ideals_through(D, primes)
    geom = geometric_ideals(D)
    by_norm = Counter(n for n, fac, sgn in ideals)
    geo_norm = Counter(map(c.norm, geom))
    for n in range(1, D+1):
        need(by_norm[n] == geo_norm[n], 'all_ideal_norm_coverage')
    squares = [mul(generator(p), generator(p)) for p in primes if p[0]**2 <= D]
    geo_sf = Counter(c.norm(v) for v in geom if all(rem(v, p2) != (0, 0) for p2 in squares))
    alg_sf = Counter(n for n, f, s in ideals if all(e == 1 for j, e in f))
    for n in range(1, D+1):
        need(geo_sf[n] == alg_sf[n], 'squarefree_norm_coverage')
    need(sum(p[0] == 7 for p in primes) == 2, 'conjugate_ideals_retained')
    # Independent norm-count formula r_K(n)=6 sum_{d|n} chi_{-3}(d).
    H = 1024
    R = c.row_count_prefix(c.element_rows(H), H)
    for n in range(1, H+1):
        s = sum(0 if d % 3 == 0 else (1 if d % 3 == 1 else -1)
                for d in range(1, n+1) if n % d == 0)
        need(R[n]-R[n-1] == 6*s, 'complete_row_count')

def residues_and_masks():
    primes = c.prime_ideals(96)
    rows = c.element_rows(13)
    need(len(rows) == 54, 'small_row_count')
    for prime in primes:
        g = generator(prime)
        for u in rows:
            e = c.local_phase(u, prime)
            if rem(u, g) == (0, 0):
                need(e == 6, 'literal_zero')
            else:
                value = modpower(u, (prime[0]-1)//6, g)
                need(rem(c.ROOTS[e], g) == value, 'independent_residue_symbol')
    H = 64
    rows = c.element_rows(H)
    R = c.row_count_prefix(rows, H)
    for bits in product((0, 1), repeat=4):
        support = tuple(j for j, b in enumerate(bits) if b)
        literal = sum(all(c.local_phase(u, primes[j]) != 6 for j in support) for u in rows)
        need(literal == c.coprime_count(support, H, R, primes), 'mask_inclusion_exclusion')

def direct_principal(products, rows, primes):
    out = 0
    for u in rows:
        groups = defaultdict(lambda: (0, 0))
        for fac, v in products.items():
            charge = tuple((j, e % 6) for j, e in fac if e % 6)
            sgn = (-1)**sum(e for j, e in fac)
            groups[charge] = add(groups[charge], scale(sgn*v, c.ROOTS[c.phase(u, fac, primes)]))
        out += sum(c.norm(z) for z in groups.values())
    return out

def exact_references_and_moments():
    for D, H in ((16, 13), (32, 32), (64, 64), (96, 13)):
        primes = c.prime_ideals(D)
        ideals = c.ideals_through(D, primes)
        rows = c.element_rows(H)
        R = c.row_count_prefix(rows, H)
        arrays, columns = c.native_arrays(D, rows, ideals, primes)
        for source in ('mobius', 'liouville'):
            for i, u in enumerate(rows):
                z = (0, 0)
                for n, fac, sgn in ideals:
                    if D < 2*n <= 2*D and (source == 'liouville' or all(e == 1 for j, e in fac)):
                        z = add(z, scale(sgn, c.ROOTS[c.phase(u, fac, primes)]))
                need(z == tuple(int(v) for v in arrays[source][i]), 'scalar_vector_source_match')
            for k in (1, 2, 3):
                products = c.product_counts(columns[source], k)
                reference = c.principal_reference(products, H, R, primes)['principal_total']
                if k == 2:
                    need(c.principal_fourth(columns[source], H, R, primes) == c.principal_reference(products, H, R, primes), 'two_product_engines_match')
                need(reference == direct_principal(products, rows, primes), 'principal_direct_row_match')


def negative_controls():
    primes = c.prime_ideals(13)
    rows = c.element_rows(13)
    R = c.row_count_prefix(rows, 13)
    # A sixth exponent keeps the zero at p; principal charge alone is insufficient.
    products = c.product_counts([(), ((0, 3),)], 2)
    ref = c.principal_reference(products, 13, R, primes)
    need(ref['sixth_alias_addition'] > 0, 'reject_equal_product_only')
    need(ref['principal_total'] != ref['unmasked_total'], 'reject_unmasked_reference')
    g = generator(primes[0])
    need(c.phase(g, ((0, 6),), primes) == 6, 'reject_zero_to_one_at_sixth_power')
    need(c.local_phase(g, primes[1]) != 6, 'reject_equal_norm_ideal_collapse')
    # Squarefree columns first need extra sixth aliases at order 12.
    products = c.product_counts([(), ((0, 1),)], 6)
    ref = c.principal_reference(products, 13, R, primes)
    need(ref['sixth_alias_addition'] == 2*c.coprime_count((0,), 13, R, primes),
         'squarefree_order_twelve_alias')
    # The finite remainder has both signs, even for the literal native source.
    for D, expected_sign in ((16, 1), (128, -1)):
        result = c.run(D, D)
        remainder = result['fourth_references']['mobius']['signed_remainder']
        need(expected_sign*remainder > 0, 'reject_universal_remainder_sign')

def main():
    coverage()
    residues_and_masks()
    exact_references_and_moments()
    negative_controls()
    print(json.dumps({'status': 'PASS', 'checks': dict(sorted(CHECKS.items())),
                      'total_predicates': sum(CHECKS.values()),
                      'scope': 'finite exact arithmetic only; no infinite moment certification'},
                     sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
