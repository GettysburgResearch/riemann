#!/usr/bin/env python3
"""Exact finite checks for THREE_EDGE_INTEGER_BRIDGE.md; stdlib only.

This checks algebra, finite interval unions and constants. It does not
verify a summed HLC operator, any root/history comparison, or a native
inverse moment. All requirements remain active under python -O.
"""

from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd, isqrt
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def det(z, w):
    return z[0] * w[1] - z[1] * w[0]


@lru_cache(None)
def signed_divisors(n):
    require(n != 0, "divisors of zero are not a finite family")
    n = abs(n)
    pos = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            pos.add(d)
            pos.add(n // d)
    return tuple(sorted(pos | {-d for d in pos}))


def integer_candidates(A, B, j0, j1, j2):
    N = B * j1 + j0 * j2
    require(B != 0 and N != 0, "nonresonant enumerator received a resonance")
    out = set()
    for delta in signed_divisors(N):
        if (delta + A * j0) % B:
            continue
        h = (delta + A * j0) // B
        numerator = A * j1 + h * j2
        if numerator % delta:
            continue
        x, y = numerator // delta, N // delta
        if gcd(h, j0) == gcd(x, y) == 1:
            out.add((h, x, y))
    return out


def window_interval(a, b, low, high, domain):
    """Exact closed domain where low <= a+b*t <= high; endpoints have measure 0."""
    lo, hi = domain
    if b == 0:
        return domain if low <= a <= high else None
    left, right = F(low - a, b), F(high - a, b)
    if left > right:
        left, right = right, left
    lo, hi = max(lo, left), min(hi, right)
    return None if lo > hi else (lo, hi)


def intersect_windows(vertices, domain=(F(-2), F(2))):
    interval = domain
    for a, b in vertices:
        interval = window_interval(a, b, F(1, 16), F(16), interval)
        if interval is None:
            return None
    return interval


def union_length(intervals):
    ordered = sorted(interval for interval in intervals if interval is not None)
    total = F(0)
    if not ordered:
        return total
    left, right = ordered[0]
    for lo, hi in ordered[1:]:
        if lo <= right:
            right = max(right, hi)
        else:
            total += right - left
            left, right = lo, hi
    return total + right - left


counts = defaultdict(int)
J = tuple(j for j in range(-3, 4) if j)
Jset = set(J)
endpoints = [(A, B) for A, B in product(range(-3, 4), repeat=2)
             if B and gcd(A, B) == 1]
small_vectors = [(x, y) for x, y in product(range(-6, 7), repeat=2)
                 if gcd(x, y) == 1]
brute = defaultdict(set)
for A, B in endpoints:
    for j0 in J:
        for h in range(-6, 7):
            if gcd(h, j0) != 1:
                continue
            for x, y in small_vectors:
                j1, j2 = det((h, j0), (x, y)), det((x, y), (A, B))
                if j1 in Jset and j2 in Jset:
                    brute[A, B, j0, j1, j2].add((h, x, y))
                    counts["independent_integer_bridges"] += 1

for A, B in endpoints:
    for j0, j1, j2 in product(J, repeat=3):
        key = (A, B, j0, j1, j2)
        N = B * j1 + j0 * j2
        if N:
            candidates = integer_candidates(*key)
            bounded = {(h, x, y) for h, x, y in candidates
                       if max(abs(h), abs(x), abs(y)) <= 6}
            require(bounded == brute[key], f"integer bridge mismatch {key}")
            require(len(candidates) <= len(signed_divisors(N)), "integer divisor count")
            for h, x, y in candidates:
                require(det((h, j0), (x, y)) == j1, "first Cramer equation")
                require(det((x, y), (A, B)) == j2, "second Cramer equation")
            intervals = [window_interval(h, j0, F(1, 16), F(16), (F(-2), F(2)))
                         for h, _, _ in candidates]
            bound = F(len(signed_divisors(N)) * 255, 16 * abs(j0))
            require(union_length(intervals) <= min(F(4), bound), "phase interval union")
            counts["integer_nonresonant_data"] += 1
            counts["rational_phase_union_checks"] += 1
        else:
            for h, x, y in brute[key]:
                if intersect_windows([(A, B), (h, j0), (x, y)]) is None:
                    continue
                delta = B * h - A * j0
                if delta:
                    require((x, y) == (1, 0) and j1 == -j0 and j2 == B,
                            "positive first backtrack classification")
                    counts["positive_first_backtracks"] += 1
                else:
                    require((h, j0) == (A, B) and j2 == -j1,
                            "positive last backtrack classification")
                    counts["positive_last_backtracks"] += 1

for j0, j1, j2 in product(J, repeat=3):
    g = gcd(abs(j0), abs(j2))
    residues = [h for h in range(abs(j0)) if (h * j2 + j1) % j0 == 0]
    require(bool(residues) == (j1 % g == 0), "closed congruence solvability")
    if residues:
        step = abs(j0) // g
        require(len(residues) == g, "closed congruence multiplicity")
        require(all((h - residues[0]) % step == 0 for h in residues),
                "closed congruence residue class")
    for h in range(-12, 13):
        if (j1 + h * j2) % j0 == 0:
            x, y = -(j1 + h * j2) // j0, -j2
            require(det((h, j0), (x, y)) == j1 and det((x, y), (1, 0)) == j2,
                    "closed triangle determinant equations")
            counts["closed_triangle_congruence_instances"] += 1
    counts["closed_triangle_congruence_classes"] += 1

for q in (3, 5, 7, 11, 13, 17, 19, 31):
    intervals = []
    for n in range(q):
        if n in (1, q - 1):
            continue
        h = 1 - n
        z1, z2 = (h, q), (2 - h, -q)
        interval = (F(4 * n + 1, 4 * q), F(4 * n + 3, 4 * q))
        require(gcd(*z1) == gcd(*z2) == 1, "closed example primitivity")
        require(det((1, 0), z1) == q and det(z1, z2) == -2 * q
                and det(z2, (1, 0)) == q, "closed example determinants")
        for R in interval:
            require(F(1, 4) <= z1[0] + z1[1] * R <= F(7, 4), "first closed window")
            require(F(1, 4) <= z2[0] + z2[1] * R <= F(7, 4), "second closed window")
        intervals.append(interval)
    require(union_length(intervals) == F(q - 2, 2 * q), "closed positive-measure family")
    counts["closed_triangle_no_decay_examples"] += 1

for absolute_j0, sign, j1, j2 in product((17, 31, 64, 101, 211, 997),
                                        (-1, 1), (1, 2, 3, 7, 11, 31, 100),
                                        (1, 2, 3, 4, 7, 14, 31, 101, 211)):
    j0 = sign * absolute_j0
    g = gcd(abs(j0), abs(j2))
    lower_h = F(1, 16) - max(0, -2 * j0)
    upper_h = F(16) - min(0, -2 * j0)
    start = -((-lower_h.numerator) // lower_h.denominator)
    stop = upper_h.numerator // upper_h.denominator
    intervals = [window_interval(h, -2 * j0, F(1, 16), F(16), (F(0), F(1)))
                 for h in range(start, stop + 1) if (h * j2 + j1) % j0 == 0]
    expected = F(0) if j1 % g else min(F(1), F(255 * g, 16 * abs(j0)))
    require(union_length(intervals) == expected, "closed triangle exact gcd root density")
    count_integral = sum((interval[1] - interval[0] for interval in intervals if interval is not None), F(0))
    expected_count = F(0) if j1 % g else F(255 * g, 16 * abs(j0))
    require(count_integral == expected_count, "closed triangle exact multiplicity integral")
    counts["closed_triangle_exact_gcd_root_densities"] += 1
    counts["closed_triangle_exact_multiplicity_integrals"] += 1
    if F(0) < expected < 1:
        counts["closed_triangle_nontrivial_gcd_savings"] += 1

for H in range(1, 65):
    harmonic = sum((F(1, h) for h in range(1, H + 1)), F(0))
    divisor_harmonic = F(0)
    for h in range(1, H + 1):
        tau_h = len(signed_divisors(h)) // 2
        require(sum(gcd(h, d) for d in range(1, H + 1)) <= H * tau_h,
                "one difference gcd sum")
        divisor_harmonic += F(tau_h, h)
        counts["gcd_inner_sum_inequalities"] += 1
    require(divisor_harmonic <= harmonic * harmonic, "harmonic divisor square bound")
    counts["harmonic_divisor_sum_inequalities"] += 1

for Y in range(1, 10):
    labels = range(Y, 4 * Y + 1)
    weighted = F(0)
    for a, b, c in product(labels, repeat=3):
        if len({a, b, c}) < 3:
            continue
        weighted += F(gcd(abs(b - a), abs(c - b)), abs(b - a) * a * b * c)
        counts["weighted_distinct_product_triples"] += 1
    H = 3 * Y
    harmonic = sum((F(1, h) for h in range(1, H + 1)), F(0))
    exact_upper = F(4 * (3 * Y + 1) * H, Y ** 3) * harmonic * harmonic
    coarse_upper = F(48, Y) * harmonic * harmonic
    require(weighted <= exact_upper <= coarse_upper, "weighted triangle label sum")
    counts["weighted_triangle_sum_scales"] += 1


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


for z0 in small_vectors:
    g, bez_a, bez_b = egcd(*z0)
    require(g == 1, "primitive complement existence")
    w0 = (-bez_b, bez_a)
    require(det(z0, w0) == 1, "unimodular complement")
    for root in (F(0), F(1, 7), F(1, 3), F(1, 2), F(6, 7), F(1)):
        tz, tw = z0[0] - 2 * root * z0[1], w0[0] - 2 * root * w0[1]
        numerator = -2 * w0[1] * tz + 2 * z0[1] * tw
        require(numerator == -2, "source root Jacobian numerator")
        if F(1, 16) <= tz <= 16:
            require(F(2, 1) / (tz * tz) >= F(1, 128), "source Jacobian lower bound")
        counts["exact_root_jacobians"] += 1
require(F(128) * 2 * F(255, 16) == 4080, "general source constant")
require(F(1, 2) * 2 * F(255, 16) == F(255, 16), "global root constant")

for q in (1009, 10007):
    # B=1 leaves a wide endpoint window: the new saving is not merely
    # a large endpoint determinant restricting its own phase window.
    A, B, j0, j1, j2 = 1, 1, 2 * q, 6 * q, 1 - 2 * q
    candidates = integer_candidates(A, B, j0, j1, j2)
    require((q + 2, 2 * q + 1, 4 * q) in candidates, "large actual bridge retained")
    intervals = []
    for h, x, y in candidates:
        interval = intersect_windows([(A, -2 * B), (h, -2 * j0), (x, -2 * y)],
                                     (F(0), F(1)))
        intervals.append(interval)
    measure = union_length(intervals)
    tauN = len(signed_divisors(B * j1 + j0 * j2)) // 2
    bound = F(255 * tauN, 16 * j0)
    require(F(0) < measure <= bound < 1, "nontrivial exact source-root saving")
    counts["large_nontrivial_root_measure_examples"] += 1

# Eisenstein arithmetic is implemented independently on pairs a+b*omega.
EZ, EO = (0, 0), (1, 0)


def eadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def eneg(u):
    return (-u[0], -u[1])


def esub(u, v):
    return eadd(u, eneg(v))


def emul(u, v):
    a, b = u
    c, d = v
    return (a * c - b * d, a * d + b * c - b * d)


def econj(u):
    return (u[0] - u[1], -u[1])


def enorm(u):
    a, b = u
    return a * a - a * b + b * b


def ediv_exact(u, v):
    require(v != EZ, "division by zero in Eisenstein ring")
    num, den = emul(u, econj(v)), enorm(v)
    if num[0] % den or num[1] % den:
        return None
    return (num[0] // den, num[1] // den)


@lru_cache(None)
def eprimitive(u, v):
    while v != EZ:
        numerator, den = emul(u, econj(v)), enorm(v)
        q = tuple((2 * a + den) // (2 * den) for a in numerator)
        remainder = esub(u, emul(q, v))
        require(enorm(remainder) < enorm(v), "Eisenstein Euclidean descent")
        u, v = v, remainder
    return enorm(u) == 1


def edet(z, w):
    return esub(emul(z[0], w[1]), emul(z[1], w[0]))


units = tuple(u for u in product(range(-2, 3), repeat=2) if enorm(u) == 1)
require(len(units) == 6, "six Eisenstein units")


@lru_cache(None)
def edivisors(N):
    require(N != EZ, "Eisenstein divisors of zero")
    limit = 2 * (isqrt(enorm(N)) + 1)
    divisors = tuple(delta for delta in product(range(-limit, limit + 1), repeat=2)
                     if delta != EZ and enorm(delta) <= enorm(N)
                     and ediv_exact(N, delta) is not None)
    associate_classes = defaultdict(set)
    for delta in divisors:
        key = min(emul(unit, delta) for unit in units)
        associate_classes[key].add(delta)
    require(all(len(orbit) == 6 for orbit in associate_classes.values()),
            "six associates per divisor ideal")
    require(len(divisors) == 6 * len(associate_classes), "ideal divisor multiplicity")
    counts["eisenstein_divisor_ideals_checked"] += len(associate_classes)
    return divisors


def eisenstein_candidates(A, B, j0, j1, j2):
    N = eadd(emul(B, j1), emul(j0, j2))
    require(B != EZ and N != EZ, "Eisenstein nonresonance")
    out = set()
    for delta in edivisors(N):
        h = ediv_exact(eadd(delta, emul(A, j0)), B)
        if h is None:
            continue
        x = ediv_exact(eadd(emul(A, j1), emul(h, j2)), delta)
        if x is None:
            continue
        y = ediv_exact(N, delta)
        require(y is not None, "divisor enumeration integrity")
        if eprimitive(h, j0) and eprimitive(x, y):
            out.add((h, x, y))
    return out


elements = tuple(product(range(-1, 2), repeat=2))
element_set = set(elements)
unit_set = set(units)
eendpoints = [(A, B) for A, B in product(elements, repeat=2)
              if B != EZ and eprimitive(A, B)]
evectors = [(x, y) for x, y in product(elements, repeat=2) if eprimitive(x, y)]
ebrute = defaultdict(set)
for A, B in eendpoints:
    for j0 in units:
        for h in elements:
            for x, y in evectors:
                j1, j2 = edet((h, j0), (x, y)), edet((x, y), (A, B))
                if j1 in unit_set and j2 in unit_set:
                    ebrute[A, B, j0, j1, j2].add((h, x, y))
                    counts["independent_eisenstein_bridges"] += 1

for A, B in eendpoints:
    for j0, j1, j2 in product(units, repeat=3):
        key = (A, B, j0, j1, j2)
        N = eadd(emul(B, j1), emul(j0, j2))
        if N != EZ:
            candidates = eisenstein_candidates(*key)
            bounded = {(h, x, y) for h, x, y in candidates
                       if h in element_set and x in element_set and y in element_set}
            require(bounded == ebrute[key], f"Eisenstein bridge mismatch {key}")
            require(len(candidates) <= len(edivisors(N)), "Eisenstein bridge count")
            for h, x, y in candidates:
                require(edet((h, j0), (x, y)) == j1, "Eisenstein first equation")
                require(edet((x, y), (A, B)) == j2, "Eisenstein second equation")
            counts["eisenstein_nonresonant_data"] += 1
        else:
            for h, x, y in ebrute[key]:
                delta = esub(emul(B, h), emul(A, j0))
                if delta != EZ:
                    require(y == EZ and x in unit_set, "Eisenstein first unit return")
                    require(j1 == eneg(emul(x, j0)) and j2 == emul(x, B),
                            "first unit-return labels")
                else:
                    epsilon = ediv_exact(j0, B)
                    require(epsilon in unit_set and h == emul(epsilon, A),
                            "Eisenstein last unit return")
                    require(j1 == eneg(emul(epsilon, j2)), "last unit-return label")
                counts["eisenstein_unit_return_cases"] += 1

for a, b in product(range(-8, 9), repeat=2):
    if (a, b) == EZ:
        continue
    multiplication_matrix_det = a * (a - b) + b * b
    require(multiplication_matrix_det == enorm((a, b)), "complex area dilation")
    counts["eisenstein_area_dilations"] += 1

require(counts["positive_first_backtracks"] > 0 and counts["positive_last_backtracks"] > 0,
        "both integer resonances exercised")
require(counts["eisenstein_unit_return_cases"] > 0, "unit resonances exercised")
print(json.dumps({"status": "passed", "counts": dict(sorted(counts.items())),
                  "constants": {"source_general": "4080", "source_global_root": "255/16",
                                "integer_associates": 2, "eisenstein_associates": 6},
                  "scope": "finite algebra, root measures and weighted triangle sums; no full HLC/native moment theorem"},
                 indent=2, sort_keys=True))
