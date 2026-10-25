#!/usr/bin/env python3
"""Finite checks for HLC_PATH_CANCELLATION.md. No asymptotic claim is tested."""

from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
import json
from math import gcd


COUNTS = Counter()


def require(test, label):
    if not test:
        raise RuntimeError(label)


def det(z, w, p):
    return (z[0] * w[1] - z[1] * w[0]) % p


def points(p):
    return [(x, y) for x in range(p) for y in range(p) if x or y]


def scale(z, a, p):
    return ((a * z[0]) % p, (a * z[1]) % p)


def neighbours(vs, p, c):
    return {z: [w for w in vs if det(z, w, p) == c] for z in vs}


def walk(start, cs, tables, filters=None):
    counts = {start: 1}
    for j, c in enumerate(cs, 1):
        nxt = Counter()
        for z, count in counts.items():
            for w in tables[c][z]:
                if filters and j in filters and not filters[j](w):
                    continue
                nxt[w] += count
        counts = nxt
    return counts


def qreturn(p, k):
    if k == 0:
        return Q(1)
    return (Q(1) + (-1) ** k * Q(1, p ** (k - 1))) / (p + 1)


def two_step_product():
    for p in (3, 5, 7, 11):
        vs = points(p)
        ts = {c: neighbours(vs, p, c) for c in range(p)}
        for c, d in product(range(1, p), repeat=2):
            lam = (-d * pow(c, -1, p)) % p
            for z in vs:
                counts = walk(z, (c, d), ts)
                for w in vs:
                    expected = p if w == scale(z, lam, p) else int(det(z, w, p) != 0)
                    require(counts.get(w, 0) == expected, "two-step product")
                    COUNTS["two_step_matrix_entries"] += 1


def line_return_formulas():
    for p in (3, 5, 7, 11):
        vs = points(p)
        yline = [(a, 0) for a in range(1, p)]
        ts = {c: neighbours(vs, p, c) for c in range(p)}
        sequences = set()
        for k in range(1, 7):
            sequences.add(tuple(1 for _ in range(k)))
            sequences.add(tuple((j % (p - 1)) + 1 for j in range(k)))
            sequences.add(tuple(1 if j % 2 == 0 else p - 1 for j in range(k)))
        for cs in sorted(sequences):
            k = len(cs)
            lam = 1
            if k % 2 == 0:
                for j in range(0, k, 2):
                    lam = lam * (-cs[j + 1] * pow(cs[j], -1, p)) % p
            for z in yline:
                counts = walk(z, cs, ts)
                return_mass = sum(counts.get(w, 0) for w in yline)
                require(Q(return_mass, p ** k) == qreturn(p, k), "return mass")
                for w in yline:
                    expected = qreturn(p, k) / (p - 1)
                    if k % 2 == 0:
                        expected += Q(1, p ** (k // 2)) * (
                            int(w == scale(z, lam, p)) - Q(1, p - 1)
                        )
                    require(Q(counts.get(w, 0), p ** k) == expected, "line-return kernel")
                    COUNTS["line_return_matrix_entries"] += 1
        # A zero determinant step has p-1 targets and annihilates radial variation.
        for cs in ((0,), (0, 1), (1, 0), (1, 0, 1), (1, 2 % p, 0, 1), (0, 0, 1, 1)):
            normalizer = 1
            for c in cs:
                normalizer *= p if c else p - 1
            n_nonzero = sum(c != 0 for c in cs)
            for z in yline:
                counts = walk(z, cs, ts)
                for w in yline:
                    expected = qreturn(p, n_nonzero) / (p - 1)
                    require(Q(counts.get(w, 0), normalizer) == expected, "zero-step kernel")
                    COUNTS["zero_step_entries"] += 1


def bridge_projectors():
    for p in (3, 5, 7):
        vs = points(p)
        yline = [(a, 0) for a in range(1, p)]
        outside = [z for z in vs if z[1] != 0]
        ts = {c: neighbours(vs, p, c) for c in range(1, p)}
        for cs in ((1, 1, 1), (1, 2, p - 1), (p - 1, p - 1, 2)):
            c1, c2, c3 = cs
            all_bridges = {}
            marginal1, marginal2 = Counter(), Counter()
            for z, w in product(yline, repeat=2):
                pairs = [
                    (a, b)
                    for a in ts[c1][z]
                    for b in ts[c2][a]
                    if det(b, w, p) == c3
                ]
                require(len(pairs) == p, "three-step bridge count")
                all_bridges[z, w] = pairs
                for a, b in pairs:
                    marginal1[a] += 1
                    marginal2[b] += 1
            require(set(marginal1) == set(outside), "first intermediate support")
            require(set(marginal2) == set(outside), "second intermediate support")
            for a in outside:
                require(marginal1[a] == p - 1, "first marginal uniformity")
                require(marginal2[a] == p - 1, "second marginal uniformity")
                COUNTS["bridge_marginal_counts"] += 2
            for seed1, seed2 in product(range(4), repeat=2):
                bad1 = {a for a in outside if (a[0] + 2 * a[1] + seed1) % (seed1 + 2) == 0}
                bad2 = {a for a in outside if (2 * a[0] + a[1] + seed2) % (seed2 + 2) == 0}
                delta = Q(len(bad1) + len(bad2), len(outside))
                dvals = []
                for z, w in product(yline, repeat=2):
                    retained = sum(a not in bad1 and b not in bad2 for a, b in all_bridges[z, w])
                    dvals.append(Q(p - retained, p))
                mean_d = sum(dvals, Q(0)) / len(dvals)
                mean_d2 = sum((d * d for d in dvals), Q(0)) / len(dvals)
                require(mean_d <= delta, "projection L1 error")
                require(mean_d2 <= min(Q(1), delta), "projection Hilbert-Schmidt error")
                # Arbitrary endpoint projectors only delete nonnegative kernel mass.
                for endpoint_seed in range(3):
                    compressed = []
                    for (z, w), d in zip(product(yline, repeat=2), dvals):
                        compressed.append(d if (z[0] + endpoint_seed) % 2 and (w[0] + endpoint_seed) % 3 else Q(0))
                    require(sum((d * d for d in compressed), Q(0)) / len(compressed) <= min(Q(1), delta), "endpoint projection bound")
                    COUNTS["projector_error_checks"] += 1
                COUNTS["projector_error_checks"] += 2


def two_step_masks_and_short_returns():
    for p in (3, 5, 7, 11):
        vs = points(p)
        yline = [(a, 0) for a in range(1, p)]
        outside = [z for z in vs if z[1] != 0]
        ts = {c: neighbours(vs, p, c) for c in range(1, p)}
        for c in range(1, p):
            for seed in range(5):
                bad = {w for w in outside if (w[0] + seed * w[1]) % (seed + 2) == 0}
                delta = Q(len(bad), len(outside))
                av = []
                for z in yline:
                    a = Q(sum(w not in bad for w in ts[c][z]), p)
                    av.append(a)
                    counts = walk(z, (c, p - c), ts, {1: lambda w: w not in bad})
                    require(counts.get(z, 0) == a * p, "masked two-step diagonal")
                    require(all(counts.get(w, 0) == 0 for w in yline if w != z), "masked two-step off diagonal")
                require(sum(av, Q(0)) / (p - 1) == 1 - delta, "two-step retained mean")
                require(sum((a * a for a in av), Q(0)) / (p - 1) >= (1 - delta) ** 2, "two-step retained lower bound")
                COUNTS["two_step_mask_cases"] += 1
        for m in range(1, 5):
            cs = tuple(p - 1 if j % 2 == 0 else 1 for j in range(2 * m))
            filters = {j: lambda z: z[1] == 0 for j in range(2, 2 * m + 1, 2)}
            for z in yline:
                counts = walk(z, cs, ts, filters)
                require(counts.get(z, 0) == p ** m, "repeated short-return diagonal")
                require(all(counts.get(w, 0) == 0 for w in yline if w != z), "repeated short-return off diagonal")
                COUNTS["short_return_schedules"] += 1
            # Explicit determinant telescoping with alternating complete products.
            gs = [0 if j % 2 == 0 else 1 for j in range(2 * m + 1)]
            require(cs == tuple((gs[j] - gs[j + 1]) % p for j in range(2 * m)), "actual telescoping determinant pattern")
            COUNTS["telescoping_product_cases"] += 1


def local_damping_and_fock_schedule():
    # A local line is paid once, regardless of the number of active intervals.
    for p in (3, 5, 7, 11):
        for r in range(1, 6):
            active = set(range(0, 2 * r + 1, 2))
            line_at = [0 if j % 2 == 0 else 1 for j in range(2 * r + 1)]
            eta = [Q(j + 1, 4 * r + 4) for j in range(2 * r + 1)]
            avg = Q(0)
            for ell in range(p + 1):
                term = Q(1)
                for j in range(2 * r + 1):
                    if j in active:
                        term *= int(ell == line_at[j])
                    else:
                        term *= 1 - eta[j] * int(ell == line_at[j])
                avg += term / (p + 1)
            require(avg == Q(1, p + 1), "one line factor for alternating active set")
            # Two distinct primes, each introduced once; later uses are transfers.
            active_prime = "b"
            memory = set()
            selected = {"b"}
            for edge in range(2 * r):
                incoming = "a" if active_prime == "b" else "b"
                departing = active_prime
                if edge == 0:
                    require(incoming not in selected, "fresh first incoming prime")
                    selected.add(incoming)
                else:
                    require(incoming in memory, "return from existing memory")
                    memory.remove(incoming)
                if edge != 2 * r - 1:
                    memory.add(departing)
                active_prime = incoming
            require(active_prime == "b" and not memory and selected == {"a", "b"}, "empty endpoint memory schedule")
            COUNTS["fock_schedule_cases"] += 1


def unordered_list_factor():
    for j in range(0, 5):
        source = tuple(range(j + 1))
        target = tuple(range(j)) + (j + 1,)
        source_perms = list(permutations(source))
        target_perms = set(permutations(target))
        compatible = 0
        for s in source_perms:
            if s[-1] != j:
                continue
            t = s[:-1] + (j + 1,)
            compatible += int(t in target_perms)
        require(Q(compatible, len(source_perms)) == Q(1, j + 1), "one-group unordered list factor")
        for k in range(1, 6):
            require(Q(compatible ** k, len(source_perms) ** k) == Q(1, (j + 1) ** k), "K-group unordered list factor")
            COUNTS["list_symmetrization_cases"] += 1


def circle_distance(x):
    r = x - (x.numerator // x.denominator)
    return min(r, 1 - r)


def largest_group_backtracks():
    # Full-I separation tests all incoming lower groups, even if an
    # individual edge had labelled some of those choices "fresh".
    p = 1000000007
    shared_top, new_top = 1000000009, 1000000033
    old_shared_lower = 5
    old_departing_lower = 7
    new_lower = 11
    middle_lower = (old_shared_lower, new_lower)
    middle_top = (shared_top, new_top)
    candidates = [(a * b, z) for a, b, z in product(middle_lower, middle_top, (7, 13, 17, 19))]
    products = [d * z for d, z in candidates]
    require(len(products) == len(set(products)), "separation products distinct")
    old_pair = (old_shared_lower * shared_top, old_departing_lower)
    old_product = old_pair[0] * old_pair[1]
    full_middle = old_shared_lower * new_lower * shared_top * new_top
    threshold = Q(100, 1000000000)
    for numerator in (137, 211, 919, 1013, 2003):
        r = Q(numerator, 100003)
        min_gap = min(circle_distance((x - y) * r) for x, y in product(products, repeat=2) if x != y)
        require(min_gap >= threshold, "full-I separation hypothesis")
        h_target = (p * old_product - full_middle) * r
        hstar = (h_target.numerator // h_target.denominator) % p
        center = (full_middle * r + hstar) / p
        retained = [(d, z) for d, z in candidates if circle_distance(d * z * r - center) <= Q(16, p)]
        require(retained == [old_pair], "full-I forces entire previous product")
        require(Q(32, p) < threshold, "phase separation margin")
        for d, z in candidates:
            if d * z == old_product:
                require(d == old_pair[0] and z == old_pair[1], "current-list and outside-prime factor split")
        COUNTS["largest_group_phase_cases"] += 1
    # Integer geometry: det(z0,z1)=j, det(z1,z2)=-j implies z2-z0=k z1.
    # tau(x,y)=x and all x-coordinates lie in [1,16].
    p = 257
    zs = [(x, y) for x in range(1, 17) for y in range(-5, 6) if gcd(x, y) == 1]
    for z0, z1 in product(zs, repeat=2):
        j = z0[0] * z1[1] - z0[1] * z1[0]
        if j == 0 or j % p == 0:
            continue
        for k in range(-15, 16):
            z2 = (z0[0] + k * z1[0], z0[1] + k * z1[1])
            if not 1 <= z2[0] <= 16 or gcd(*z2) != 1:
                continue
            require(z1[0] * z2[1] - z1[1] * z2[0] == -j, "opposite integer determinants")
            if det(z0, z2, p) == 0:
                require(k == 0 and z2 == z0, "recorded line forces exact integer backtrack")
            COUNTS["integer_backtrack_cases"] += 1


def separation_measure():
    def intervals(n, delta):
        out = []
        for j in range(n):
            lo, hi = Q(j, n) - delta / n, Q(j, n) + delta / n
            if lo < 0:
                out.extend([(Q(0), hi), (lo + 1, Q(1))])
            elif hi > 1:
                out.extend([(lo, Q(1)), (Q(0), hi - 1)])
            else:
                out.append((lo, hi))
        return out

    def union_length(segs):
        merged = []
        for lo, hi in sorted(segs):
            if merged and lo <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
            else:
                merged.append((lo, hi))
        return sum((hi - lo for lo, hi in merged), Q(0))

    for xs in ((1, 2), (1, 3, 8), (2, 5, 9, 14), (1, 4, 7, 12, 19)):
        for delta in (Q(1, 100), Q(1, 31), Q(1, 10)):
            segs = []
            for j, x in enumerate(xs):
                for y in xs[j + 1:]:
                    local = intervals(abs(x - y), delta)
                    require(union_length(local) == 2 * delta, "integer circle map preserves bad-set measure")
                    segs.extend(local)
            require(union_length(segs) <= min(Q(1), delta * len(xs) * (len(xs) - 1)), "full-I separation union bound")
            COUNTS["separation_measure_cases"] += 1
    e1 = Q(1, 1000000)
    for k in range(1, 9):
        eps = [3 ** j * e1 for j in range(k)]
        require(eps[-1] - 2 * sum(eps[:-1], Q(0)) == e1, "polynomial hierarchy exponent")
        COUNTS["polynomial_band_hierarchies"] += 1


def negative_controls():
    p = 5
    vs = points(p)
    line = [(a, 0) for a in range(1, p)]
    ts = {c: neighbours(vs, p, c) for c in range(1, p)}
    z = (1, 0)
    two = walk(z, (p - 1, 1), ts)
    require(two[z] == p and two.get((2, 0), 0) == 0, "two-step mutation witness")
    require(Q(two[z], p) != Q(1, p - 1), "reject false uniform two-step bridge")
    full_four = walk(z, (p - 1, 1, p - 1, 1), ts)
    forced_four = walk(z, (p - 1, 1, p - 1, 1), ts, {2: lambda w: w[1] == 0})
    require(full_four.get((2, 0), 0) > 0 and forced_four.get((2, 0), 0) == 0, "reject ignoring middle line condition")
    require(Q(1, p + 1) != Q(1, (p + 1) ** 3), "reject repeated line charge")
    n, s, eta = Q(1, 4), Q(1, 10000), Q(1, 1000)
    require(n / 100 - 5 * s - eta == Q(1, 1000), "root-count single-error budget")
    COUNTS["negative_controls"] += 3
    COUNTS["exact_exponent_comparisons"] += 1


def main():
    two_step_product()
    line_return_formulas()
    bridge_projectors()
    two_step_masks_and_short_returns()
    local_damping_and_fock_schedule()
    unordered_list_factor()
    largest_group_backtracks()
    separation_measure()
    negative_controls()
    print(json.dumps({"status": "passed", "arithmetic": "integer and exact rational", "counts": dict(sorted(COUNTS.items())), "scope": "finite identities only; no integer completion or new zero-free region"}, indent=2))


if __name__ == "__main__":
    main()
