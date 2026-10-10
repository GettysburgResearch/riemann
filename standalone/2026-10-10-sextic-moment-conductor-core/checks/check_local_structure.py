"""Exact finite controls for the conductor/interaction packet.

The finite columns use a sharp norm band and nu=1. The row set is an entire
small Eisenstein norm ball. These are algebraic controls, not smooth-weight
asymptotics or evidence establishing an infinite moment estimate.

Only Python's standard library is used. A failed predicate raises explicitly;
the acceptance checks remain enabled with python -O.
"""

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
UNITS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
COUNT = defaultdict(int)


def require(ok, kind):
    COUNT[kind] += 1
    if not ok:
        raise RuntimeError("Failed exact predicate: " + kind)


def ring_mul(x, y, p=None):
    a, b = x
    c, d = y
    z = (a * c - b * d, a * d + b * c - b * d)
    return z if p is None else (z[0] % p, z[1] % p)


def ring_pow(x, e, p):
    out = (1, 0)
    while e:
        if e & 1:
            out = ring_mul(out, x, p)
        x = ring_mul(x, x, p)
        e //= 2
    return out


def root_mul(x, y):
    """Multiply integer coordinates in Z[zeta_6], zeta_6^2=zeta_6-1."""
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def root_pow(z, e):
    out = (1, 0)
    for _ in range(e):
        out = root_mul(out, z)
    return out


def prime_ideals(limit):
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            for n in range(p * p, limit + 1, p):
                sieve[n] = False
    ideals = []
    for p in range(5, limit + 1):
        if not sieve[p]:
            continue
        if p % 3 == 1:
            roots = [r for r in range(p) if (r * r + r + 1) % p == 0]
            require(len(roots) == 2, "split_prime_roots")
            ideals.extend((p, p, r) for r in roots)
        elif p * p <= limit:
            ideals.append((p * p, p, None))
    return sorted(ideals, key=lambda q: (q[0], q[2] or 0))


def symbol(q, row):
    norm, p, root = q
    a, b = row
    if root is not None:
        z = (a + root * b) % p
        if z == 0:
            return -1
        v = pow(z, (norm - 1) // 6, p)
        for j, (x, y) in enumerate(UNITS):
            if v == (x + root * y) % p:
                return j
    else:
        z = (a % p, b % p)
        if z == (0, 0):
            return -1
        v = ring_pow(z, (norm - 1) // 6, p)
        for j, (x, y) in enumerate(UNITS):
            if v == (x % p, y % p):
                return j
    raise RuntimeError("Sextic Euler exponent missed the six roots")


def local_controls(kmax=7):
    for k in range(1, kmax + 1):
        for left in range(1 << k):
            l = left.bit_count()
            for right in range(1 << k):
                r = right.bit_count()
                m = l + r
                residue = (l - r) % 6
                require((m - residue) % 2 == 0, "mobius_parity")
                require(m >= min(residue, 6 - residue), "minimum_load")
                require(residue == 0 or m >= 1, "nonprincipal_nonempty")
                if m == 1:
                    require(residue in (1, 5), "singleton_sextic")
                if m == 2 and residue != 0:
                    require(residue in (2, 4), "double_cubic")
                for value in range(-1, 6):
                    # Compute the unexpanded product in the integer ring first.
                    z = (0, 0) if value == -1 else ROOTS[value]
                    conjugate = (z[0] + z[1], -z[1])
                    literal = root_mul(root_pow(z, l), root_pow(conjugate, r))
                    if m == 0:
                        expected = (1, 0)
                    elif value == -1:
                        expected = (0, 0)
                    else:
                        expected = ROOTS[(residue * value) % 6]
                    require(literal == expected, "local_product_with_exact_zero_mask")


def field_controls():
    for q in ((7, 7, 2), (7, 7, 4), (13, 13, 3), (13, 13, 9), (25, 5, None)):
        norm, p, root = q
        elements = [(a, 0) for a in range(p)] if root is not None else list(
            itertools.product(range(p), repeat=2))
        values = [symbol(q, z) for z in elements]
        require([values.count(j) for j in range(-1, 6)] == [1] + [(norm - 1) // 6] * 6,
                "full_residue_field_orthogonality")
        for x, sx in zip(elements, values):
            for y, sy in zip(elements, values):
                actual = symbol(q, ring_mul(x, y, p))
                expected = -1 if min(sx, sy) < 0 else (sx + sy) % 6
                require(actual == expected, "full_residue_field_multiplicativity")


def matrix_mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def graph_controls():
    for k in range(1, 10):
        c = [[2 if i == j else -1 for j in range(k)] for i in range(k)]
        require([sum(row) for row in c] == [3 - k] * k, "graph_common_eigenvector")
        for j in range(1, k):
            v = [int(i == 0) - int(i == j) for i in range(k)]
            cv = [sum(x * y for x, y in zip(row, v)) for row in c]
            require(cv == [3 * x for x in v], "graph_transverse_eigenvector")
        for i in range(k):
            s = identity(k)
            s[i] = [-1 if j == i else 1 for j in range(k)]
            require(matrix_mul(s, s) == identity(k), "reflection_involution")
            st = list(map(list, zip(*s)))
            require(matrix_mul(matrix_mul(st, c), s) == c, "reflection_form")
    reflections = []
    for i in range(3):
        s = identity(3)
        s[i] = [-1 if j == i else 1 for j in range(3)]
        reflections.append(s)
    p = matrix_mul(matrix_mul(reflections[0], reflections[1]), reflections[2])
    p2 = matrix_mul(p, p)
    nilpotent = [[p2[i][j] - int(i == j) for j in range(3)] for i in range(3)]
    require(nilpotent == [[3, 0, -3]] * 3, "affine_nonzero_translation")
    require(matrix_mul(nilpotent, nilpotent) == [[0] * 3 for _ in range(3)],
            "affine_nilpotence")
    power = identity(3)
    for m in range(16):
        expected = [[int(i == j) + m * nilpotent[i][j] for j in range(3)]
                    for i in range(3)]
        require(power == expected, "affine_power_formula")
        power = matrix_mul(power, p2)
    q7, q13 = (7, 7, 4), (13, 13, 9)
    s713 = symbol(q13, (-2, -3))
    s137 = symbol(q7, (1, -3))
    require((2 * s713) % 6 == (2 * s137) % 6 == 4, "actual_cubic_reciprocity")
    require((4 * s713) % 6 == 2, "missing_edge_nontrivial")
    return {"coxeter_matrix": p, "square_minus_identity": nilpotent,
            "missing_edge_as_sixth_root_exponent": 2}


def columns_in_band(ideals, d):
    cols = []

    def visit(start, norm, factors):
        if d // 2 < norm <= d:
            cols.append((norm, -1 if len(factors) % 2 else 1, factors))
        for j in range(start, len(ideals)):
            nn = norm * ideals[j][0]
            if nn > d:
                break
            visit(j + 1, nn, factors + (j,))

    visit(0, 1, ())
    return cols


def norm_ball(h):
    bound = math.isqrt((4 * h) // 3) + 2
    return [(a, b) for a in range(-bound, bound + 1)
            for b in range(-bound, bound + 1) if 0 < a * a - a * b + b * b <= h]


def moment_panel(d, h, k):
    ideals = prime_ideals(d)
    cols = columns_in_band(ideals, d)
    active = sorted(set(itertools.chain.from_iterable(c[2] for c in cols)))
    renumber = {old: new for new, old in enumerate(active)}
    ideals = [ideals[j] for j in active]
    cols = [(norm, mu, tuple(renumber[j] for j in fac)) for norm, mu, fac in cols]
    rows = norm_ball(h)
    symbols = [[symbol(q, row) for q in ideals] for row in rows]
    direct = 0
    for sr in symbols:
        a = b = 0
        for _, mu, fac in cols:
            if any(sr[j] < 0 for j in fac):
                continue
            x, y = ROOTS[sum(sr[j] for j in fac) % 6]
            a += mu * x
            b += mu * y
        direct += (a * a + a * b + b * b) ** k

    zero = (0,) * len(ideals)
    left = {zero: 1}
    for _ in range(k):
        out = defaultdict(int)
        for counts, coeff in left.items():
            for _, mu, fac in cols:
                c = list(counts)
                for j in fac:
                    c[j] += 1
                out[tuple(c)] += coeff * mu
        left = dict(out)

    kernels = {}
    regions = {name: [0, 0] for name in
               ("no_singletons", "low_complexity_with_singletons", "remaining")}
    pair_count = 0
    for l, lc in left.items():
        for r, rc in left.items():
            m = tuple(a + b for a, b in zip(l, r))
            residues = tuple((a - b) % 6 for a, b in zip(l, r))
            key = tuple(-1 if load == 0 else residue for load, residue in zip(m, residues))
            if key not in kernels:
                ka = kb = 0
                used = [j for j, value in enumerate(key) if value >= 0]
                for sr in symbols:
                    if any(sr[j] < 0 for j in used):
                        continue
                    a, b = ROOTS[sum(key[j] * sr[j] for j in used) % 6]
                    ka += a
                    kb += b
                kernels[key] = ka, kb
            u = math.prod(q[0] for q, load in zip(ideals, m) if load == 1)
            v = math.prod(q[0] for q, load, residue in zip(ideals, m, residues)
                          if load == 2 and residue != 0)
            if u == 1:
                region = "no_singletons"
            elif u * u * v <= h * h:
                region = "low_complexity_with_singletons"
            else:
                region = "remaining"
            ka, kb = kernels[key]
            regions[region][0] += lc * rc * ka
            regions[region][1] += lc * rc * kb
            require(sum(m) % 2 == sum(residues) % 2, "global_mobius_parity")
            pair_count += 1
    total = [sum(v[j] for v in regions.values()) for j in range(2)]
    require(total == [direct, 0], "literal_moment_reconstruction")
    for value in regions.values():
        require(value[1] == 0, "region_conjugation_closure")
    return {"D": d, "H": h, "k": k, "rows": len(rows), "columns": len(cols),
            "left_product_groups": len(left), "product_group_pairs": pair_count,
            "distinct_row_kernels": len(kernels), "direct_exact_moment": direct,
            "regions_exact": {name: value[0] for name, value in regions.items()},
            "weight_scope": "nu=1, sharp half-open column band and sharp full row norm ball"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    local_controls()
    field_controls()
    graph = graph_controls()
    panels = [moment_panel(d, h, k) for d, h, k in
              ((16, 23, 2), (32, 47, 2), (64, 97, 2), (16, 23, 3), (32, 47, 3))]
    result = {"status": "PASS", "arithmetic": "EXACT_INTEGER_AND_SIXTH_ROOT_ALGEBRA",
              "infinite_moment_proved_by_computation": False,
              "checks": dict(sorted(COUNT.items())), "total_predicates": sum(COUNT.values()),
              "interaction_graph": graph, "panels": panels}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
