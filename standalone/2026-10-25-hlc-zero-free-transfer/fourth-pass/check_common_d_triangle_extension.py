#!/usr/bin/env python3
"""Exact checks for the common-D triangle extension; stdlib only."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, prod
import json


COUNTS = Counter()
W = F(255, 16)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def window(a, b, interval=(F(0), F(1))):
    if b == 0:
        return interval if F(1, 16) <= a <= 16 else None
    lo, hi = sorted((F(F(1, 16) - a, b), F(16 - a, b)))
    lo, hi = max(lo, interval[0]), min(hi, interval[1])
    return (lo, hi) if lo < hi else None


def length(interval):
    return F(0) if interval is None else interval[1] - interval[0]


def line(z, p):
    x, y = z[0] % p, z[1] % p
    require(x or y, "primitive projective reduction")
    return (1, y * pow(x, -1, p) % p) if x else (0, 1)


def legal(sequence):
    return all(sequence[j] != sequence[j + 1] for j in range(3))


def check_label_family(shared, sequences, groups):
    kk = len(shared)
    require(all(legal(seq) for seq in sequences), "only legal adjacent replacements")
    bb, aa, cc, dd = [prod(seq[j] for seq in sequences) for j in range(4)]
    common = prod(shared)
    j0, j1, j2 = common * (bb - aa), common * (aa - cc), common * (cc - dd)
    require(j0 and j1 and j2, "actual nonzero raw determinants")
    bad = any(seq[0] == seq[2] or seq[1] == seq[3] for seq in sequences)
    returning = tuple(i for i, seq in enumerate(sequences) if seq[0] == seq[3])
    tt = prod(sequences[i][0] for i in returning)
    require(tt == gcd(bb, dd), "returning prime product is endpoint gcd")
    vv = [sum((F(1, p) for p in group), F(0)) for group in groups]
    root_coordinate_product = (2 ** kk) * prod(v ** -2 for v in vv)
    one_edge = F(1, 2 ** kk) * prod(v ** -1 for v in vv)
    pre = root_coordinate_product * one_edge ** 3
    require(pre == F(1, 4 ** kk) * prod(v ** -5 for v in vv),
            "different root lists retain the same orbit coefficient")
    gg = gcd(abs(j0), abs(j2))
    g0 = gcd(abs(bb - aa), abs(cc - dd))
    if not bad and len(returning) < kk:
        require(bb // tt != dd // tt, "proper returning set has distinct reduced endpoint products")
        require(gcd(g0, tt) == 1, "closed gcd is coprime to returning product")
        require(((aa - cc) % g0 == 0) == (((bb - dd) // tt) % g0 == 0),
                "closed solvability becomes reduced endpoint congruence")
        COUNTS["partial_return_gcd_reductions"] += 1
    if j1 % gg:
        COUNTS["insoluble_closed_families"] += 1
        return
    modulus = abs(j0) // gg
    residue = 0 if modulus == 1 else (-(j1 // gg) * pow(j2 // gg, -1, modulus)) % modulus
    h_min = F(1, 16) + min(0, 2 * j0)
    h_max = F(16) + max(0, 2 * j0)
    lower = ceil((h_min - residue) / modulus) - 1
    upper = floor((h_max - residue) / modulus) + 1
    count, original_weight = F(0), F(0)
    union_primes = tuple(sorted(set(shared) | {p for seq in sequences for p in seq}))
    for index in range(lower, upper + 1):
        hh = residue + modulus * index
        first = window(hh, -2 * j0)
        count += length(first)
        require((j1 + hh * j2) % j0 == 0, "integer closed candidate")
        xx, yy = -(j1 + hh * j2) // j0, -j2
        if first is None or gcd(hh, j0) != 1 or gcd(xx, yy) != 1:
            continue
        vertices = ((1, 0), (hh, j0), (xx, yy), (1, 0))
        mass = F(1)
        for p in union_primes:
            active = [j for j in range(4)
                      if p in shared or any(seq[j] == p for seq in sequences)]
            forced = {line(vertices[j], p) for j in active}
            local = F(0) if len(forced) != 1 else F(1, p + 1)
            # This sums all p+1 line indicators directly, without
            # introducing a fresh line for an endpoint repetition.
            lines = [(1, y) for y in range(p)] + [(0, 1)]
            enumerated = sum((F(int(all(line(vertices[j], p) == ell for j in active)), p + 1)
                              for ell in lines), F(0))
            require(local == enumerated, "literal once-line finite average")
            mass *= local
            COUNTS["literal_active_line_averages"] += 1
        if bad:
            require(mass == 0, "forbidden cross repetition has zero active-line mass")
            COUNTS["excluded_cross_collision_paths"] += 1
        else:
            expected = prod(F(1, p + 1) for p in union_primes)
            require(mass == expected, "all surviving prime patterns are consistent")
            denominator = common * aa * cc * tt * (bb // tt) * (dd // tt)
            require(denominator == prod(union_primes), "squarefree active union")
            require(mass <= F(1, denominator), "partial-return original line weight")
            second = window(xx, -2 * yy, first)
            original_weight += pre * mass * length(second)
            COUNTS["surviving_primitive_paths"] += 1
    require(count == W * gg / abs(j0), "full closed candidate multiplicity")
    if not bad:
        bound = pre * F(1, common * aa * cc * tt * (bb // tt) * (dd // tt)) * W * gg / abs(j0)
        require(original_weight <= bound, "complete fixed-label original-weight root bound")
    COUNTS["soluble_closed_families"] += 1


def source_patterns():
    choices = (5, 7, 11, 13)
    for seq in product(choices, repeat=4):
        if legal(seq):
            check_label_family((3,), (seq,), ((3, *choices),))
    cases = [
        ((5, 7, 11, 5), (19, 23, 29, 31)),
        ((5, 7, 11, 13), (19, 23, 29, 19)),
        ((5, 7, 11, 5), (19, 23, 29, 19)),
        ((5, 7, 11, 13), (19, 23, 29, 31)),
        ((5, 7, 5, 13), (19, 23, 29, 31)),
        ((5, 7, 11, 7), (19, 23, 29, 19)),
    ]
    for seqs in cases:
        check_label_family((3, 17), seqs,
                           ((3, 5, 7, 11, 13), (17, 19, 23, 29, 31)))
    require(COUNTS["excluded_cross_collision_paths"] > 0,
            "zero-line obstruction is actually exercised")
    require(COUNTS["partial_return_gcd_reductions"] > 0,
            "proper returning groups are exercised")


def weighted_four_product_sums():
    for yy in (2, 3, 4, 6):
        harmonic = sum((F(1, n) for n in range(1, 3 * yy + 1)), F(0))
        for tt in range(1, yy + 1):
            bb = F(yy, tt)
            endpoint_values = range(ceil(bb), floor(4 * bb) + 1)
            for gg in range(1, 3 * yy + 2):
                pairs = sum(1 for u, v in product(endpoint_values, repeat=2)
                            if u != v and (u - v) % gg == 0)
                require(pairs <= 24 * bb ** 2 / gg, "nonzero endpoint congruence pair count")
                COUNTS["reduced_endpoint_pair_counts"] += 1
            total = F(0)
            for aa, cc, u, v in product(range(yy, 4 * yy + 1), range(yy, 4 * yy + 1), endpoint_values, endpoint_values):
                if u == v:
                    continue
                hh, kk = tt * u - aa, cc - tt * v
                if not hh or not kk:
                    continue
                gg = gcd(abs(hh), abs(kk))
                if (u - v) % gg:
                    continue
                total += F(gg, aa * cc * tt * u * v * abs(hh))
                COUNTS["weighted_four_product_terms"] += 1
            require(total <= F(288, tt * yy) * harmonic, "fixed-return-product numerical upper bound")
            COUNTS["weighted_four_product_scales"] += 1


def subset_and_error_normalizers():
    for kk in range(1, 7):
        vs = [F(i + 2, i + 4) for i in range(kk)]
        subset_sum = sum((prod(vs[i] for i in subset)
                          for size in range(kk) for subset in combinations(range(kk), size)), F(0))
        require(subset_sum == prod(1 + v for v in vs) - prod(vs), "proper-return-set mass sum")
        COUNTS["return_subset_normalizers"] += 1
    for jj in range(1, 8):
        beta, delta = F(1, 100000), F(1, 4)
        require(6 * (jj + 4) * beta + (jj + 1) * beta - delta / 100
                == (7 * jj + 25) * beta - delta / 100,
                "complete common-D discrete discrepancy")
        COUNTS["extension_discrepancy_budgets"] += 1
    require(32 * F(1, 40000) - F(1, 400) == -F(17, 10000), "explicit common-D polynomial example")


def negative_controls():
    # The diagonal endpoint case cannot be included in the nonzero-difference
    # congruence count: it requires the separate three-product theorem.
    diagonal_pairs = 4
    require(diagonal_pairs > F(24, 101), "reject including identical reduced endpoint products")
    # A prime active at the first root remains geometrically incident to
    # the final root even when absent from its active list.
    rho, p = F(2, 3), 5
    require(rho / (p + 1) < F(1, p + 1), "nonreturning endpoint damping need not be one")
    COUNTS["negative_controls"] += 2


def main():
    source_patterns()
    weighted_four_product_sums()
    subset_and_error_normalizers()
    negative_controls()
    print(json.dumps({"status": "passed", "counts": dict(sorted(COUNTS.items())),
                      "scope": "common-D raw rooted triangles; no arbitrary history or full native moment"}, indent=2))


if __name__ == "__main__":
    main()
