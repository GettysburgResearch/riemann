#!/usr/bin/env python3
"""Complete finite Eisenstein census. Integer arithmetic; NumPy speeds row sums.
The hard window is D/2 < N(n) <= D. No asymptotic inference is made.
"""
import argparse
from collections import Counter, defaultdict
import json
import math
from pathlib import Path

ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (0, 0))

def require(ok, message):
    if not ok:
        raise ValueError(message)

def norm(u):
    a, b = u
    return a*a-a*b+b*b

def field_mul(x, y, p):
    a, b = x
    c, d = y
    return ((a*c-b*d) % p, (a*d+b*c-b*d) % p)

def field_pow(x, e, p):
    z = (1, 0)
    while e:
        if e & 1:
            z = field_mul(z, x, p)
        x = field_mul(x, x, p)
        e //= 2
    return z

def primes_through(D):
    flags = bytearray(b'\x01')*(D+1)
    flags[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(D)+1):
        if flags[p]:
            flags[p*p:D+1:p] = b'\x00'*((D-p*p)//p+1)
    return [p for p in range(5, D+1) if flags[p]]

def prime_ideals(D):
    """All prime ideals outside 2 and 3, not one ideal per rational norm."""
    out = []
    for p in primes_through(D):
        if p % 3 == 1:
            roots = [r for r in range(p) if (r*r+r+1) % p == 0]
            require(len(roots) == 2, 'split prime needs two distinct ideals')
            for r in roots:
                sixth = {pow(1+r, e, p): e for e in range(6)}
                require(len(sixth) == 6, 'sixth-root order')
                table = [6 if x == 0 else sixth[pow(x, (p-1)//6, p)]
                         for x in range(p)]
                out.append((p, p, r, table))
        elif p*p <= D:
            sixth = {(a % p, b % p): e for e, (a, b) in enumerate(ROOTS[:6])}
            table = [6 if a == b == 0 else
                     sixth[field_pow((a, b), (p*p-1)//6, p)]
                     for a in range(p) for b in range(p)]
            out.append((p*p, p, None, table))
    return sorted(out, key=lambda v: (v[0], -1 if v[2] is None else v[2]))

def element_rows(H):
    bound = math.isqrt(4*H//3)+1
    return [(a, b) for a in range(-bound, bound+1)
            for b in range(-bound, bound+1) if 0 < norm((a, b)) <= H]

def ideals_through(D, primes):
    ideals = [(1, (), 1)]
    for j, (q, _, _, _) in enumerate(primes):
        new = []
        for n, fac, sign in ideals:
            power, e = q, 1
            while n*power <= D:
                new.append((n*power, fac+((j, e),), sign*(-1)**e))
                power *= q
                e += 1
        ideals.extend(new)
    return sorted(ideals, key=lambda v: (v[0], v[1]))

def local_phase(u, prime):
    _, p, r, table = prime
    a, b = u
    idx = (a+r*b) % p if r is not None else (a % p)*p+b % p
    return table[idx]

def phase(u, fac, primes):
    e = 0
    for j, power in fac:
        local = local_phase(u, primes[j])
        if local == 6:
            return 6
        e += power*local
    return e % 6

def merge(f, g):
    """Product IDEAL, with repeated exponents retained."""
    h = dict(f)
    for j, e in g:
        h[j] = h.get(j, 0)+e
    return tuple(sorted(h.items()))

def product_counts(columns, k):
    """Unsigned ordered factorization profile. Native signs are parity of total degree."""
    if k == 2:
        out = Counter()
        for i, f in enumerate(columns):
            for j in range(i, len(columns)):
                out[merge(f, columns[j])] += 1 if i == j else 2
        return out
    out = Counter({(): 1})
    for _ in range(k):
        nxt = Counter()
        for f, v in out.items():
            for g in columns:
                nxt[merge(f, g)] += v
        out = nxt
    return out

def row_count_prefix(rows, H):
    out = [0]*(H+1)
    for u in rows:
        out[norm(u)] += 1
    for t in range(1, H+1):
        out[t] += out[t-1]
    return out

def coprime_count(support, H, R, primes):
    divs = [(1, 1)]
    for j in support:
        q = primes[j][0]
        divs += [(d*q, -sgn) for d, sgn in divs if d*q <= H]
    return sum(sgn*R[H//d] for d, sgn in divs)

def principal_reference(products, H, R, primes):
    """All sixth-power aliases AND their union nonunit masks. No row loop."""
    grouped = defaultdict(list)
    cache = {}
    def count(s):
        if s not in cache:
            cache[s] = coprime_count(s, H, R, primes)
        return cache[s]
    equal = 0
    for fac, multiplicity in products.items():
        support = tuple(j for j, e in fac)
        charge = tuple((j, e % 6) for j, e in fac if e % 6)
        equal += multiplicity*multiplicity*count(support)
        grouped[charge].append((support, multiplicity))
    aliases = 0
    unmasked = 0
    alias_pairs = 0
    for block in grouped.values():
        unmasked += sum(v for s, v in block)**2
        for i, (s, v) in enumerate(block):
            for t, w in block[i+1:]:
                aliases += 2*v*w*count(tuple(sorted(set(s) | set(t))))
                alias_pairs += 1
    return {'equal_product': equal, 'sixth_alias_addition': aliases,
            'principal_total': equal+aliases,
            'unmasked_total': R[H]*unmasked,
            'distinct_products': len(products), 'charge_classes': len(grouped),
            'unequal_product_alias_pairs': alias_pairs}


def principal_fourth(columns, H, R, primes):
    """Memory-bounded pair-product engine, with injective symbolic integer labels.
    The label primes are NOT ideal norms. They only encode unique factorization.
    A representative pair reconstructs all physical prime ideals and their masks.
    """
    cap = max(32, 2*len(primes))
    labels = primes_through(cap)
    while len(labels) < len(primes):
        cap *= 2
        labels = primes_through(cap)
    codes = [math.prod(labels[j]**e for j, e in f) for f in columns]
    products = {}
    for i, a in enumerate(codes):
        for j in range(i, len(codes)):
            key = a*codes[j]
            v = 1 if i == j else 2
            if key in products:
                products[key][0] += v
            else:
                products[key] = [v, i, j]
    cache = {}
    def count(s):
        if s in cache:
            return cache[s]
        v = coprime_count(s, H, R, primes)
        if len(cache) < 4096:
            cache[s] = v
        return v
    equal = 0
    unmasked = 0
    exceptional = defaultdict(list)
    for code, (v, i, j) in products.items():
        fac = merge(columns[i], columns[j])
        support = tuple(a for a, e in fac)
        equal += v*v*count(support)
        unmasked += v*v
        if any(e >= 6 for a, e in fac):
            charge = code//math.prod(labels[a]**(6*(e//6)) for a, e in fac)
            exceptional[charge].append((support, v))
    aliases = 0
    pairs = 0
    classes = len(products)
    for charge, block in exceptional.items():
        if charge in products:
            v, i, j = products[charge]
            fac = merge(columns[i], columns[j])
            require(all(e < 6 for a, e in fac), 'canonical charge')
            block.append((tuple(a for a, e in fac), v))
        classes -= len(block)-1
        for i, (s, v) in enumerate(block):
            for t, w in block[i+1:]:
                aliases += 2*v*w*count(tuple(sorted(set(s) | set(t))))
                unmasked += 2*v*w
                pairs += 1
    return {'equal_product': equal, 'sixth_alias_addition': aliases,
            'principal_total': equal+aliases, 'unmasked_total': R[H]*unmasked,
            'distinct_products': len(products), 'charge_classes': classes,
            'unequal_product_alias_pairs': pairs}

def native_arrays(D, rows, ideals, primes):
    import numpy as np
    require(3*len(ideals)**2 < 2**63, 'int64 norm guard')
    require(4*max(1, D) < 2**63, 'row arithmetic guard')
    rr = np.array(rows, dtype=np.int64)
    require(rr.size == 0 or int(np.max(np.abs(rr)))**2*4 < 2**63,
            'row residue multiplication guard')
    vals = np.array(ROOTS, dtype=np.int64)
    chars = []
    row_bound = max(max(abs(a), abs(b)) for a, b in rows)
    for q, p, r, table in primes:
        require((D+2)*max(1, row_bound) < 2**63,
                'residue arithmetic guard')
        idx = (rr[:, 0]+r*rr[:, 1]) % p if r is not None else (rr[:, 0] % p)*p+rr[:, 1] % p
        chars.append(np.asarray(table, dtype=np.int8)[idx])
    sums = {s: np.zeros((len(rows), 2), dtype=np.int64)
            for s in ('mobius', 'liouville', 'squarefree_unsigned')}
    columns = {s: [] for s in ('mobius', 'liouville')}
    for n, fac, sgn in ideals:
        if not D < 2*n <= 2*D:
            continue
        exponent = np.zeros(len(rows), dtype=np.int32)
        zero = np.zeros(len(rows), dtype=bool)
        require(6*sum(e for j, e in fac) < 2**31, 'exponent guard')
        for j, e in fac:
            exponent += (chars[j].astype(np.int32) % 6)*e
            zero |= chars[j] == 6
        exponent %= 6
        exponent[zero] = 6
        v = vals[exponent]
        sums['liouville'] += sgn*v
        columns['liouville'].append(fac)
        if all(e == 1 for j, e in fac):
            sums['mobius'] += sgn*v
            sums['squarefree_unsigned'] += v
            columns['mobius'].append(fac)
    return sums, columns

def run(D, H):
    require(type(D) is int and type(H) is int and D >= 4 and H >= 1, 'positive integer sizes')
    primes = prime_ideals(D)
    rows = element_rows(H)
    ideals = ideals_through(D, primes)
    R = row_count_prefix(rows, H)
    arrays, columns = native_arrays(D, rows, ideals, primes)
    out = {'D': D, 'H': H, 'row_count': len(rows),
           'prime_ideal_count': len(primes), 'good_ideal_count_through_D': len(ideals),
           'column_counts': {s: len(c) for s, c in columns.items()},
           'moments': {}, 'row_one': {}, 'maximum_squared_modulus': {},
           'fourth_references': {}}
    for source, vector in arrays.items():
        # Convert BEFORE exponentiation: high moments use unbounded Python integers.
        energies = [int(a)*int(a)-int(a)*int(b)+int(b)*int(b) for a, b in vector]
        out['moments'][source] = {str(2*k): sum(v**k for v in energies) for k in range(1, 5)}
        out['maximum_squared_modulus'][source] = max(energies)
        out['row_one'][source] = [int(v) for v in vector[rows.index((1, 0))]]
    for source, cols in columns.items():
        ref = principal_fourth(cols, H, R, primes)
        ref['signed_remainder'] = out['moments'][source]['4']-ref['principal_total']
        out['fourth_references'][source] = ref
    return out

def ceil_power_21_20(D):
    lo, hi = 0, D
    target = D**21
    while hi**20 < target:
        hi *= 2
    while hi-lo > 1:
        mid = (hi+lo)//2
        if mid**20 >= target:
            hi = mid
        else:
            lo = mid
    return hi

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--D', type=int, default=256)
    parser.add_argument('--H', type=int)
    parser.add_argument('--near-linear', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    require(not (args.H is not None and args.near_linear), 'choose H or near-linear')
    H = args.H if args.H is not None else (ceil_power_21_20(args.D) if args.near_linear else args.D)
    text = json.dumps(run(args.D, H), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')

if __name__ == '__main__':
    main()
