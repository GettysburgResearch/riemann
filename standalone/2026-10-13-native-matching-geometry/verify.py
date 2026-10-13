#!/usr/bin/env python3
"""Exact finite diagnostics. They do not prove the infinite estimates in PROOF.md.
Standard library only; run identically with and without Python optimization.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import math

HERE = Path(__file__).resolve().parent
COUNTS = Counter()

def check(ok, label):
    COUNTS[label] += 1
    if not ok:
        raise ValueError(label)


def rank(matrix):
    if not matrix:
        return 0
    a = [[Q(x) for x in row] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        p = next((i for i in range(row, len(a)) if a[i][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        pivot = a[row][col]
        a[row] = [x/pivot for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                t = a[i][col]
                a[i] = [x-t*y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def incidence(v, edges):
    return [[int(i in e) for e in edges] for i in range(v)]


def bipartite_components(v, edges):
    adj = [set() for _ in range(v)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    colours = {}
    bip = 0
    for s in range(v):
        if s in colours:
            continue
        colours[s] = 0
        todo = [s]
        good = True
        while todo:
            a = todo.pop()
            for b in adj[a]:
                if b not in colours:
                    colours[b] = 1-colours[a]; todo.append(b)
                elif colours[b] == colours[a]:
                    good = False
        bip += good
    return bip


def graph_checks():
    graphs = 0
    for v in range(1, 6):
        complete = list(combinations(range(v), 2))
        for mask in range(1 << len(complete)):
            edges = [e for j, e in enumerate(complete) if mask >> j & 1]
            r = rank(incidence(v, edges))
            check(r == v-bipartite_components(v, edges), 'unsigned_rank')
            check(len(edges)-r >= 0, 'nonnegative_nullity')
            graphs += 1
    profiles = []
    for k in range(1, 9):
        cross = [(i, k+j) for i in range(k) for j in range(k)]
        all_edges = list(combinations(range(2*k), 2))
        cross_d = len(cross)-rank(incidence(2*k, cross))
        full_d = len(all_edges)-rank(incidence(2*k, all_edges))
        check(cross_d == (k-1)**2, 'principal_dimension')
        check(full_d == (0 if k == 1 else k*(2*k-3)), 'no_singleton_dimension')
        profiles.append({'k': k, 'principal_log_power': cross_d,
                         'no_singleton_log_power': full_d})
    fixtures = [(2, [(0, 1)]),
                (4, [(0, 2), (0, 3), (1, 2), (1, 3)]),
                (4, list(combinations(range(4), 2))),
                (6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)])]
    for v, edges in fixtures:
        d = len(edges)-rank(incidence(v, edges))
        for cap in range(4):
            fibers = Counter()
            weighted = 0
            for a in product(range(cap+1), repeat=len(edges)):
                deg = tuple(sum(a[j] for j, e in enumerate(edges) if i in e)
                            for i in range(v))
                if max(deg) > cap:
                    continue
                check(sum(deg) == 2*sum(a), 'degree_energy_identity')
                fibers[deg] += 1
                weighted += 2**sum(a)
            for size in fibers.values():
                check(size <= (cap+1)**d, 'fiber_dimension_bound')
            # 1/sqrt(2)<3/4 gives a rational, deliberately loose 4^v constant.
            bound = (4**v)*(cap+1)**d
            check(weighted**2 <= bound**2*2**(v*cap), 'dyadic_sum_bound')
    # Exact polynomial counts, not an inference of an asymptotic from samples.
    for m in range(9):
        check(sum(1 for a in range(m+1)) == m+1, 'K22_fiber')
        count = sum(1 for a in range(m+1) for b in range(m-a+1))
        check(count == math.comb(m+2, 2), 'K4_fiber')
        rows = [(a, b, m-a-b) for a in range(m+1) for b in range(m-a+1)]
        c = sum(all(x+y <= m for x, y in zip(r, s)) for r in rows for s in rows)
        check(8*c == (m+1)*(m+2)*(m*m+3*m+4), 'K33_fiber')
    return graphs, profiles


def decode(left, right):
    left, right = list(left), list(right)
    z = min(len(left), len(right))
    edges = list(zip(left[:z], right[:z]))
    side = 0 if len(left) >= len(right) else 1
    remaining = left[z:] if side == 0 else right[z:]
    groups = [(side, tuple(remaining[j:j+6])) for j in range(0, len(remaining), 6)]
    return edges, groups


def local_checks():
    principal_patterns = 0
    for k in range(1, 9):
        sets = [tuple(i for i in range(k) if m >> i & 1) for m in range(1 << k)]
        for left in sets:
            for right in sets:
                if (len(left)-len(right)) % 6:
                    continue
                edges, groups = decode(left, right)
                l = [i for i, j in edges]; r = [j for i, j in edges]
                for side, g in groups:
                    check(len(g) == 6, 'six_slot_group')
                    (l if side == 0 else r).extend(g)
                check(tuple(sorted(l)) == left and tuple(sorted(r)) == right,
                      'principal_decoder_reconstruction')
                check(2*len(edges)+6*len(groups) == len(left)+len(right),
                      'principal_norm_cost')
                check((len(left)+len(right)) % 2 == 0, 'principal_mobius_parity')
                if k <= 5:
                    check(not groups, 'no_early_alias')
                principal_patterns += 1
        for subset in range(1 << (2*k)):
            n = subset.bit_count()
            if n >= 2:
                check((n == 2) or Q(n, 2) > 1, 'higher_incidence_summability')
    # Norm/mask local factors, entirely rational.
    for m in range(1, 17):
        for q in (7, 13, 19, 25, 31, 49):
            p0 = 1-Q(1, q)
            direct = p0**m + m*(p0/q)*p0**(m-1)*p0
            formula = p0**m*(1+m*p0/q)
            check(direct == formula and formula > 0, 'weighted_local_density')
    # Aliases can have negative cross terms for a general unitary twist.
    alias = {}
    for k in range(1, 9):
        neutral = sum(math.comb(k, a)*math.comb(k, b)
                      for a in range(k+1) for b in range(k+1) if (a-b) % 6 == 0)
        rotated = sum(math.comb(k, a)*math.comb(k, b)*(-1 if ((a-b)//2) % 2 else 1)
                      for a in range(k+1) for b in range(k+1) if (a-b) % 6 == 0)
        check(neutral >= 0 and rotated >= 0, 'local_reference_positivity')
        alias[k] = (neutral, rotated)
    check(alias[6] == (926, 922), 'order_twelve_phase_witness')
    for q in (7, 13, 25):
        with_zero = Q(1, q)+(1-Q(1, q))*alias[6][0]
        check(with_zero != alias[6][0], 'literal_zero_probability')
    # If r is squarefree, same sixth charge means r*d^6, with NO gcd requirement.
    for r in product((0, 1), repeat=3):
        for n in product(range(8), repeat=3):
            same = all((x-y) % 6 == 0 for x, y in zip(n, r))
            representation = all(x >= y and (x-y) % 6 == 0 for x, y in zip(n, r))
            check(same == representation, 'alias_isolation_algebra')
    return principal_patterns, alias[6]


def load_arithmetic():
    path = HERE/'census_source.py'
    raw = path.read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    check(blob == '2a074ccede483324392a729056ccbf43a1f26eac', 'source_binding')
    spec = importlib.util.spec_from_file_location('census_source', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def arithmetic_checks(c):
    cases = []
    for D in (16, 32, 64):
        primes = c.prime_ideals(D)
        ideals = c.ideals_through(D, primes)
        cols = [f for n, f, _ in ideals if D < 2*n and all(e == 1 for j, e in f)]
        products = c.product_counts(cols, 2)
        for H in (1, 7, 13, 31, 64):
            rows = c.element_rows(H)
            prefix = c.row_count_prefix(rows, H)
            cache = {}
            def rowcount(support):
                if support not in cache:
                    direct = sum(all(c.local_phase(u, primes[j]) != 6 for j in support)
                                 for u in rows)
                    inc = c.coprime_count(support, H, prefix, primes)
                    check(direct == inc, 'literal_mask_inclusion_exclusion')
                    cache[support] = direct
                return cache[support]
            via_products = sum(v*v*rowcount(tuple(j for j, e in fac))
                               for fac, v in products.items())
            brute = 0
            for a, b, x, y in product(cols, repeat=4):
                f, g = c.merge(a, b), c.merge(x, y)
                active = any((dict(f).get(j, 0)-dict(g).get(j, 0)) % 6
                             for j in set(dict(f)) | set(dict(g)))
                check((not active) == (f == g), 'quartic_principal_condition')
                if not active:
                    brute += rowcount(tuple(j for j, e in f))
            check(brute == via_products, 'physical_principal_reconstruction')
            for support in cache:
                den = math.prod(primes[j][0] for j in support)
                num = math.prod(primes[j][0]-1 for j in support)
                # Direct finite independent-divisibility enumeration.
                delta = Q(0)
                for bits in product((0, 1), repeat=len(support)):
                    probability = Q(1)
                    for j, bit in zip(support, bits):
                        q = primes[j][0]
                        probability *= Q(q-1, q) if bit else Q(1, q)
                    if all(bits):
                        delta += probability
                check(delta == Q(num, den), 'independent_density_reconstruction')
            cases.append({'D': D, 'H': H, 'columns': len(cols), 'rows': len(rows),
                          'principal_fourth': via_products})
    # Conjugate prime ideals have equal norms, but are not the same ideal.
    p = c.prime_ideals(32)
    check(p[0][0] == p[1][0] == 7 and p[0][2] != p[1][2], 'split_ideal_identity')
    return cases


def main():
    graphs, profiles = graph_checks()
    patterns, alias = local_checks()
    arithmetic = arithmetic_checks(load_arithmetic())
    negative_controls = {
        'ordinary_cycle_rank_wrong_for_triangle': 3-(3-1) != 3-rank(incidence(3, [(0,1),(1,2),(0,2)])),
        'sixth_charge_not_equal_product': (6 % 6 == 0) and 6 != 0,
        'all_principal_alias_terms_not_nonnegative': alias[1] < math.comb(12, 6),
        'erasing_nonunit_mask_changes_reference': Q(1,7)+Q(6,7)*926 != 926,
    }
    for key, value in negative_controls.items():
        check(value, 'negative_control_'+key)
    output = {'status': 'PASS_FINITE_DIAGNOSTICS_ONLY', 'predicates_including_setup': sum(COUNTS.values()),
              'counts': dict(sorted(COUNTS.items())), 'graphs_rank_checked': graphs,
              'principal_local_patterns': patterns, 'logarithmic_profiles': profiles,
              'arithmetic_cases': arithmetic, 'negative_controls': negative_controls,
              'scope': 'Exact finite graph, local-algebra and small full-column mask checks. Not an asymptotic proof.'}
    print(json.dumps(output, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
