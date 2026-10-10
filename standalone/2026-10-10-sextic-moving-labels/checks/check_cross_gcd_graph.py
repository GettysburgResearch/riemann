#!/usr/bin/env python3
"""Exact finite algebra diagnostics for cross-gcd graph identities.

These finite models test identities and exponent bookkeeping only. They do
not verify the native analytic moment input, pointwise estimates, or any
infinite mean-square theorem. Integer arithmetic represents Z[zeta_6].
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import math


ZERO = (0, 0)
ONE = (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c + b * d


def scale(c, z):
    return c * z[0], c * z[1]


def conjugate(z):
    return z[0] + z[1], -z[1]


def norm2(z):
    value = mul(z, conjugate(z))
    require(value[1] == 0 and value[0] >= 0, ("invalid norm", z, value))
    return value[0]


def phase_values(phases):
    result = []
    for mask in range(1 << len(phases)):
        value = ONE
        for bit, phase in enumerate(phases):
            if mask & (1 << bit):
                value = mul(value, phase)
        result.append(value)
    return result


def ideal_norms(primes):
    return [math.prod(p for bit, p in enumerate(primes) if mask >> bit & 1)
            for mask in range(1 << len(primes))]


def theta(values, cutoff, signed, norms):
    shared = 0
    for i in range(len(values)):
        for j in range(i):
            common = values[i] & values[j]
            if norms[common] >= cutoff:
                return 0
            shared |= common
    return (-1) ** shared.bit_count() if signed else 1


def check_native_gcd_identity():
    primes = (7, 13)
    masks = tuple(range(4))
    norms = ideal_norms(primes)
    mu = [(-1) ** mask.bit_count() for mask in masks]
    weight_x = (2, -1, 3, 5)
    weight_y = (-1, 4, 2, -3)
    selectors = ((1, 1, 1, 1), (1, 0, -1, 1),
                 (0, 1, 1, 1), (1, -1, 1, -1))
    checks = 0
    for phases in product((ZERO,) + ROOTS, repeat=2):
        eta = phase_values(phases)
        for fixed in masks:
            for selector in selectors:
                left = ZERO
                for n, m in product(masks, repeat=2):
                    if (n | m) & fixed:
                        continue
                    coefficient = (mu[n] * mu[m] * weight_x[n] * weight_y[m]
                                   * selector[n & m])
                    left = add(left, scale(coefficient, mul(eta[n], conjugate(eta[m]))))
                right = ZERO
                for c, e in product(masks, repeat=2):
                    if c & e or (c | e) & fixed:
                        continue
                    q = c | e
                    if eta[q] == ZERO:
                        continue
                    ax = ay = ZERO
                    for r in masks:
                        if r & (fixed | q):
                            continue
                        ax = add(ax, scale(mu[r] * weight_x[q | r], eta[r]))
                        ay = add(ay, scale(mu[r] * weight_y[q | r], eta[r]))
                    right = add(right, scale(selector[c] * mu[e], mul(ax, conjugate(ay))))
                require(left == right, ("gcd selector identity", phases, fixed, selector, left, right))
                checks += 1
    return {"prime_norms": primes, "phase_and_zero_assignments": 49,
            "bounded_gcd_selector_identities": checks}


def check_matching_identities():
    primes = (7, 13)
    masks = tuple(range(4))
    norms = ideal_norms(primes)
    mu = [(-1) ** mask.bit_count() for mask in masks]
    weights = ((2, -1, 3, 5), (-1, 4, 2, -3), (3, 1, -2, 4))
    cutoffs = (2, 8, 14, 92)
    thresholds = (1, 7, 13, 14, 92)
    checks = {2: 0, 3: 0}

    # Exact c,e inversion collapsed onto q=c*e; this has not assumed q labels
    # from different edges are coprime. Every q tuple is retained below.
    lambda_by_threshold = {}
    for threshold in thresholds:
        lambdas = []
        for q in masks:
            lambdas.append(sum(mu[q ^ c] for c in masks
                               if c & q == c and norms[c] >= threshold))
        lambda_by_threshold[threshold] = lambdas

    for k in (2, 3):
        tuples = tuple(product(masks, repeat=k))
        for phases in product((ZERO,) + ROOTS, repeat=2):
            eta = phase_values(phases)
            for cutoff, signed in product(cutoffs, (False, True)):
                theta_values = {ns: theta(ns, cutoff, signed, norms) for ns in tuples}
                original = {}
                for ns in tuples:
                    scalar = theta_values[ns]
                    value = ONE
                    for i, n in enumerate(ns):
                        scalar *= mu[n] * weights[i][n]
                        value = mul(value, eta[n])
                    original[ns] = scale(scalar, value)

                fixed_divisibility = {}
                for qs in tuples:
                    value = ZERO
                    for residuals in tuples:
                        if any(q & r for q, r in zip(qs, residuals)):
                            continue
                        ns = tuple(q | r for q, r in zip(qs, residuals))
                        scalar = theta_values[ns]
                        term = ONE
                        for i, r in enumerate(residuals):
                            scalar *= mu[r] * weights[i][ns[i]]
                            term = mul(term, eta[r])
                        value = add(value, scale(scalar, term))
                    fixed_divisibility[qs] = value

                left_values = {(m, t): ZERO for m in range(1, k + 1) for t in thresholds}
                for ns, ms in product(tuples, repeat=2):
                    if original[ns] == ZERO or original[ms] == ZERO:
                        continue
                    term = mul(original[ns], conjugate(original[ms]))
                    smallest = math.inf
                    for m in range(1, k + 1):
                        smallest = min(smallest, norms[ns[m - 1] & ms[m - 1]])
                        for threshold in thresholds:
                            if smallest >= threshold:
                                left_values[m, threshold] = add(left_values[m, threshold], term)

                for m in range(1, k + 1):
                    for threshold in thresholds:
                        right = 0
                        lambdas = lambda_by_threshold[threshold]
                        for matched_qs in product(masks, repeat=m):
                            if any(eta[q] == ZERO for q in matched_qs):
                                continue
                            qs = matched_qs + (0,) * (k - m)
                            coefficient = math.prod(lambdas[q] for q in matched_qs)
                            right += coefficient * norm2(fixed_divisibility[qs])
                        require(left_values[m, threshold] == (right, 0),
                                ("matching identity", k, phases, cutoff, signed,
                                 m, threshold, left_values[m, threshold], right))
                        checks[k] += 1
    return {"prime_norms": primes, "phase_and_zero_assignments": 49,
            "one_sided_selector_types": ["gcd thresholds", "gcd thresholds with shared-prime signs"],
            "fourth_moment_matching_identities": checks[2],
            "sixth_moment_matching_identities": checks[3]}


def check_endpoint_and_graph_decomposition():
    primes = (7, 13, 19, 31)
    masks = range(16)
    norms = ideal_norms(primes)
    cutoffs = (2, 8, 92, 100000)
    thresholds = (1, 7, 13, 19, 91)
    checks = 0
    nontrivial_residual_cycle_cases = 0
    for n1, n2, m1, m2 in product(masks, repeat=4):
        fixed = n2 | m1
        d, e = n1 & fixed, m2 & fixed
        x, y = n1 ^ d, m2 ^ e
        require(not ((x | y) & fixed), ("fixed-prime residual", n1, n2, m1, m2))
        require((n1 & m2) == ((d & e) | (x & y)), ("endpoint gcd factorization", n1, n2, m1, m2))
        require(not ((d & e) & (x & y)), ("endpoint gcd coprimality", n1, n2, m1, m2))
        for cutoff, threshold in product(cutoffs, thresholds):
            original_path = (norms[n1 & n2] < cutoff and norms[m1 & m2] < cutoff
                             and norms[n1 & m1] >= threshold and norms[n2 & m1] >= threshold
                             and norms[n2 & m2] >= threshold)
            grouped_path = (norms[n2 & m1] >= threshold
                            and norms[d & m1] >= threshold and norms[e & n2] >= threshold
                            and norms[d & n2] < cutoff and norms[e & m1] < cutoff)
            require(original_path == grouped_path, ("path endpoint selector", n1, n2, m1, m2, cutoff, threshold))
            original_cycle = original_path and norms[n1 & m2] >= threshold
            grouped_cycle = grouped_path and norms[d & e] * norms[x & y] >= threshold
            require(original_cycle == grouped_cycle, ("cycle endpoint selector", n1, n2, m1, m2, cutoff, threshold))
            if original_cycle and norms[d & e] < threshold and (x & y):
                nontrivial_residual_cycle_cases += 1
            checks += 2
    require(nontrivial_residual_cycle_cases > 0, "model failed to exercise the nontrivial cycle residual")

    graph_counts = {"single": 0, "matching": 0, "star": 0, "path": 0, "cycle": 0}
    edges = ((0, 2), (0, 3), (1, 2), (1, 3))
    for mask in range(1, 16):
        degrees = [0] * 4
        count = mask.bit_count()
        for bit, (i, j) in enumerate(edges):
            if mask >> bit & 1:
                degrees[i] += 1
                degrees[j] += 1
        if count == 1:
            name = "single"
        elif count == 2:
            name = "matching" if max(degrees) == 1 else "star"
        elif count == 3:
            require(sorted(degrees) == [1, 1, 2, 2], "invalid three-edge shape")
            name = "path"
        else:
            require(degrees == [2, 2, 2, 2], "invalid four-edge shape")
            name = "cycle"
        graph_counts[name] += 1
    require(graph_counts == {"single": 4, "matching": 2, "star": 4, "path": 4, "cycle": 1},
            ("edge intersection classification", graph_counts))
    return {"prime_norms": primes, "endpoint_selector_checks": checks,
            "nontrivial_residual_cycle_cases": nontrivial_residual_cycle_cases,
            "nonempty_graph_intersections": graph_counts}


def check_exponents():
    results = []
    for b in (Fraction(3, 4), Fraction(7, 8), Fraction(139999, 160000), Fraction(1)):
        a = 2 * b - 1
        endpoint = 1 / (3 - 2 * b)
        for r in (Fraction(0), endpoint):
            single = 2 + a * r
            star = Fraction(3, 2) + (b + Fraction(1, 2)) * r
            path = 1 + 2 * r
            require(single >= star and single >= path, ("union range", b, r))
            require(2 * (star - single) == path - single, ("star/path exact relation", b, r))
        results.append({"b": str(b), "largest_r_with_single_edge_cost": str(endpoint),
                        "loss_at_endpoint": str(a * endpoint)})
    require(1 / (3 - 2 * Fraction(7, 8)) == Fraction(4, 5), "7/8 endpoint")
    require(Fraction(3, 4) * Fraction(1, 4) == Fraction(3, 16), "quarter-scale loss")
    for k in range(2, 9):
        for m in range(k):
            b = Fraction(7, 8)
            a = 2 * b - 1
            require(1 + 2 * b * (k - 1) - a * m == k + a * (k - 1 - m),
                    ("all-order matching exponent", k, m))
    return {"union_ranges": results, "matching_orders_checked": list(range(2, 9)),
            "interpretation": "finite rational arithmetic only; infinite parameter formulas are proved in the note"}


def main():
    report = {
        "scope": "Exact finite identities and exponent bookkeeping; no infinite analytic theorem is tested.",
        "native_gcd_selector": check_native_gcd_identity(),
        "matching_inversion": check_matching_identities(),
        "endpoint_and_graph": check_endpoint_and_graph_decomposition(),
        "exponents": check_exponents(),
    }
    path = Path(__file__).with_name("cross_gcd_graph_checks.json")
    payload = json.dumps(report, indent=2) + "\n"
    path.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
