#!/usr/bin/env python3
"""Exact checks for CLOSED_TRIANGLE_WEIGHT.md; no full operator claim."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial, gcd, prod
import json


COUNTS = Counter()
W = F(255, 16)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def det(z, w):
    return z[0] * w[1] - z[1] * w[0]


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def window_interval(a, b, interval=(F(0), F(1))):
    """Root interval where 1/16 <= a+b*r <= 16."""
    left, right = interval
    if b == 0:
        return interval if F(1, 16) <= a <= 16 else None
    lo, hi = sorted((F(F(1, 16) - a, b), F(16 - a, b)))
    left, right = max(left, lo), min(right, hi)
    return (left, right) if left < right else None


def interval_length(interval):
    return F(0) if interval is None else interval[1] - interval[0]


def ordered_state_normalization():
    # Start and end are the source vector 1 on an unordered root orbit.
    # Endpoint S projections act as the identity. The two interior S's
    # have probabilities 1/(J+1)! before the next departing prime is fixed.
    primes = (3, 5, 7, 11, 13, 17, 19)
    for jj in range(1, 5):
        shared = primes[:jj]
        aa, bb, cc = primes[jj:jj + 3]
        orbit_b = tuple(permutations((*shared, bb)))
        orbit_a = tuple(permutations((*shared, aa)))
        orbit_c = tuple(permutations((*shared, cc)))
        nn = len(orbit_b)
        require(nn == factorial(jj + 1), "root ordered orbit size")
        legal_b = [s for s in orbit_b if s[-1] == bb]
        legal_a = [s for s in orbit_a if s[-1] == aa]
        legal_c = [s for s in orbit_c if s[-1] == cc]
        paths = 0
        for s0, s1, s2 in product(legal_b, legal_a, legal_c):
            t1, t2, t3 = (*s0[:-1], aa), (*s1[:-1], cc), (*s2[:-1], bb)
            require(t1 in orbit_a and t2 in orbit_c and t3 in orbit_b,
                    "literal T followed by orbit symmetrization")
            paths += 1
        for vv in (F(2, 3), F(7, 11), sum((F(1, p) for p in primes), F(0))):
            sigma = vv ** (-(jj + 1))
            direct = sigma * vv ** -3 * F(paths, nn ** 2)
            root_orbit = nn * sigma
            normalized_edge = F(1, jj + 1) / vv
            quotient = root_orbit * normalized_edge ** 3
            claimed = F(factorial(jj + 1), (jj + 1) ** 3) * vv ** (-(jj + 4))
            require(direct == quotient == claimed, "original root and three-edge normalization")
            require(direct != sigma * normalized_edge ** 3, "reject lost root orbit factor")
            COUNTS["ordered_quotient_normalizations"] += 1
        COUNTS["literal_ordered_triangle_paths"] += paths

    for jj, kk in product(range(1, 6), range(1, 4)):
        vv = [F(2 * i + 3, 3 * i + 5) for i in range(kk)]
        pre = F(factorial(jj + 1) ** kk, (jj + 1) ** (3 * kk)) * prod(v ** (-(jj + 4)) for v in vv)
        shared_mass = prod(v ** jj / factorial(jj) for v in vv)
        post = F(1, (jj + 1) ** (2 * kk)) * prod(v ** -4 for v in vv)
        require(pre * shared_mass == post, "exact shared-list cancellation")
        COUNTS["factorial_cancellations"] += 1


def shared_list_mass():
    for primes in ((3, 5, 7, 11, 13), (17, 19, 23, 29, 31, 37)):
        vv = sum((F(1, p) for p in primes), F(0))
        for jj in range(1, min(4, len(primes)) + 1):
            full = sum((F(1, prod(ds)) for ds in combinations(primes, jj)), F(0))
            upper = vv ** jj / factorial(jj)
            require(full <= upper, "unordered elementary symmetric mass")
            for abc in permutations(primes, 3):
                available = [p for p in primes if p not in abc]
                retained = sum((F(1, prod(ds)) for ds in combinations(available, jj)), F(0))
                require(retained <= full <= upper, "drop shared-list prime exclusions only after weighting")
                COUNTS["excluded_shared_list_sums"] += 1


def line(z, p):
    x, y = z[0] % p, z[1] % p
    require(x or y, "primitive vertex has a projective reduction")
    return (1, y * pow(x, -1, p) % p) if x else (0, 1)


def active_prime_mass(vertices, shared, aa, bb, cc):
    result = F(1)
    for p in (*shared, aa, bb, cc):
        active = range(4) if p in shared else (1,) if p == aa else (2,) if p == cc else (0, 3)
        active = tuple(active)
        labels = [line(z, p) for z in vertices]
        lines = [(1, y) for y in range(p)] + [(0, 1)]
        local = F(0)
        for ell in lines:
            if not all(labels[j] == ell for j in active):
                continue
            # Any positive damping exponent can be used: all inactive
            # vertices avoid the forced active line in this family.
            inactive_matches = sum(labels[j] == ell for j in range(4) if j not in active)
            require(inactive_matches == 0, "unshared active prime has no inactive-vertex incidence")
            local += F(2, 3) ** inactive_matches / (p + 1)
        require(local == F(1, p + 1), "prime line is drawn exactly once")
        result *= local
        COUNTS["actual_prime_line_averages"] += 1
    return result


def actual_triangle_labels():
    families = [((3,), (5, 7, 11)), ((5,), (3, 7, 11)),
                ((3, 5), (7, 11, 13)), ((3, 5, 7), (11, 13, 17))]
    for shared, choices in families:
        dd = prod(shared)
        jj = len(shared)
        vv = sum((F(1, p) for p in (*shared, *choices)), F(0))
        pre = F(factorial(jj + 1), (jj + 1) ** 3) * vv ** (-(jj + 4))
        for aa, bb, cc in permutations(choices):
            j0, j1, j2 = dd * (bb - aa), dd * (aa - cc), dd * (cc - bb)
            require(all((j0, j1, j2)) and j0 + j1 + j2 == 0, "actual old-minus-new determinants")
            gg, qq = gcd(abs(j0), abs(j2)), abs(j0) // gcd(abs(j0), abs(j2))
            h_lo = floor(F(1, 16) + min(0, 2 * j0)) - 1
            h_hi = ceil(F(16) + max(0, 2 * j0)) + 1
            candidate_count, actual_weight = F(0), F(0)
            for hh in range(h_lo, h_hi + 1):
                if (hh - 1) % qq:
                    continue
                first = window_interval(hh, -2 * j0)
                candidate_count += interval_length(first)
                require((j1 + hh * j2) % j0 == 0, "common-D closed congruence")
                xx, yy = -(j1 + hh * j2) // j0, -j2
                z0, z1, z2 = (1, 0), (hh, j0), (xx, yy)
                if gcd(*z1) != 1 or gcd(*z2) != 1 or first is None:
                    continue
                require(det(z0, z1) == j0 and det(z1, z2) == j1 and det(z2, z0) == j2,
                        "literal closed raw geometry")
                require(hh % 2 and xx % 2, "source odd-first parity from primitive even determinant")
                all_positions = window_interval(xx, -2 * yy, first)
                if all_positions is None:
                    continue
                local = active_prime_mass((z0, z1, z2, z0), shared, aa, bb, cc)
                expected = prod(F(1, p + 1) for p in (*shared, aa, bb, cc))
                require(local == expected <= F(1, dd * aa * bb * cc), "actual squarefree union line weight")
                actual_weight += pre * local * interval_length(all_positions)
                COUNTS["primitive_retained_triangle_paths"] += 1
            require(candidate_count == W * gg / abs(j0), "root integral retains every candidate multiplicity")
            bound = pre * F(1, dd * aa * bb * cc) * W * gg / abs(j0)
            require(actual_weight <= bound, "original-weight root-averaged triangle bound")
            require(F(gg, abs(j0)) == F(gcd(abs(bb - aa), abs(cc - bb)), abs(bb - aa)),
                    "shared D cancels from gcd ratio")
            COUNTS["complete_label_weight_checks"] += 1
            COUNTS["exact_multiplicity_integrals"] += 1


def discrepancy_budget():
    for jj, delta in product(range(1, 8), (F(1, 4), F(1, 3), F(1, 2))):
        beta = delta / (200 * (7 * jj + 19))
        used_modulus = (jj + 3) * beta
        labels = (jj + 3) * beta
        candidates = (jj + 1) * beta
        total = labels + candidates + 5 * used_modulus - delta / 100
        require(total == (7 * jj + 19) * beta - delta / 100 == -delta / 200,
                "complete source discrepancy budget")
        COUNTS["discrete_root_budgets"] += 1
    require(26 * F(1, 40000) - F(1, 400) == -F(37, 20000), "explicit polynomial-band example")
    require(F(1, 80000) < F(37, 20000), "main count is the limiting power in example")
    COUNTS["explicit_polynomial_examples"] += 1


def negative_controls():
    require(W / 2 > 1, "candidate count cannot be replaced by a union probability")
    # Distinct numerical products are insufficient for the 1/(Dabc) bound.
    dd, aa, bb, cc = 7, 6, 10, 15
    wrong_extension = prod(F(1, p + 1) for p in (2, 3, 5, 7))
    require(wrong_extension > F(1, dd * aa * bb * cc), "reject line-weight extension before prime-level distinctness")
    for p in (3, 5, 7, 11):
        require(F(1, p + 1) != F(1, (p + 1) ** 3), "reject independent line draws at three active vertices")
    COUNTS["negative_controls"] += 6


def main():
    ordered_state_normalization()
    shared_list_mass()
    actual_triangle_labels()
    discrepancy_budget()
    negative_controls()
    print(json.dumps({"status": "passed", "counts": dict(sorted(COUNTS.items())),
                      "arithmetic": "exact rational weights, root interval lengths and integer identities",
                      "scope": "restricted raw common-D rooted triangle; imported finite-residue estimate not proved here"}, indent=2))


if __name__ == "__main__":
    main()
