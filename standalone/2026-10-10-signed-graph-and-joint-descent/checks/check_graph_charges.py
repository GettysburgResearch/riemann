#!/usr/bin/env python3
"""Exact diagnostics for the signed graph and dense graph manuscripts.

This checks finite algebra, zero/sixth-root phases, signed incidence
identities, graph partitions, and rational exponents. It does not evaluate
L-functions or verify NM2, PW, infinite convergence, or analytic bounds.
All acceptance gates are explicit RuntimeError checks; Python -O does not
remove them. The two-prime phase model is formal, not an enumeration of
genuine global Hecke characters.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb, lcm, prod
from pathlib import Path
import json


COUNTS: Counter[str] = Counter()
ZERO = (0, 0)
ONE = (1, 0)
# zeta^2 = zeta - 1; coefficients in the integral basis (1, zeta).
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
PHASES = (ZERO,) + ROOTS
NORMS = (1, 7, 13, 91)
MOBIUS = (1, -1, -1, 1)
FOREST_B = (Q(3, 5), Q(3, 4), Q(7, 8), Q(1))


def gate(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError("Exact diagnostic failed: " + label)
    COUNTS[label] += 1


def za(x, y):
    return x[0] + y[0], x[1] + y[1]


def zm(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def zs(x, n):
    return x[0] * n, x[1] * n


def zc(x):
    return x[0] + x[1], -x[1]


def zp(x, n):
    result = ONE
    for _ in range(n):
        result = zm(result, x)
    return result


def formal_correction_checks():
    for x in ROOTS:
        gate(zp(x, 6) == ONE, "sixth_root_relations")
        gate(zm(x, zc(x)) == ONE, "unit_conjugation_relations")
    gate(zp(ZERO, 0) == ONE and zp(ZERO, 1) == ZERO,
         "literal_zero_power_convention")
    for count in (4, 6):
        k = count // 2
        for exponents in product(range(3), repeat=count):
            support = [v for v, exponent in enumerate(exponents) if exponent]
            for masked in (False, True):
                coefficient = 0
                for subset in range(1 << len(support)):
                    remainder = list(exponents)
                    sign = (-1) ** subset.bit_count()
                    for j, v in enumerate(support):
                        if subset & (1 << j):
                            remainder[v] -= 1
                    e = 1 if masked else 1 - sum(x > 0 for x in remainder)
                    coefficient += sign * e
                expected = int(not support)
                if not masked and sum(exponents) == 1:
                    expected = -1
                gate(coefficient == expected, "formal_forward_coefficients")
                for phase in PHASES:
                    monomial = ONE
                    for v, exponent in enumerate(exponents):
                        x = phase if v < k else zc(phase)
                        monomial = zm(monomial, zp(x, exponent))
                    gate(zs(monomial, coefficient) == zs(monomial, expected),
                         "formal_forward_all_zero_sixth_phases")


@lru_cache(None)
def cross_edges(k):
    return tuple((i, k + j) for i in range(k) for j in range(k))


def graph_from_tuple(values, k, threshold):
    result = 0
    for j, (v, w) in enumerate(cross_edges(k)):
        if NORMS[values[v] & values[w]] >= threshold:
            result |= 1 << j
    return result


@lru_cache(None)
def graph_data(k, graph):
    count = 2 * k
    parent = list(range(count))
    degrees = [0] * count
    forest = []

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for j, (v, w) in enumerate(cross_edges(k)):
        if not graph & (1 << j):
            continue
        degrees[v] += 1
        degrees[w] += 1
        rv, rw = root(v), root(w)
        if rv != rw:
            parent[rv] = rw
            forest.append((v, w))

    @lru_cache(None)
    def matching(left, used_right):
        if left == k:
            return 0
        value = matching(left + 1, used_right)
        for right in range(k):
            edge = left * k + right
            if graph & (1 << edge) and not used_right & (1 << right):
                value = max(value, 1 + matching(left + 1,
                                               used_right | (1 << right)))
        return value

    four_cycle = any(
        all(graph & (1 << (i * k + j)) for i in left for j in right)
        for left in combinations(range(k), 2)
        for right in combinations(range(k), 2)
    )
    return (tuple(forest), sum(d == 0 for d in degrees),
            matching(0, 0), four_cycle)


def exact_charges(count, b, axes, edges, label):
    """Check every induced subset, using an exact common denominator."""
    alpha = [Q(1, 2) if v in axes else b for v in range(count)]
    denominator = lcm(*(x.denominator for x in alpha),
                      *(w.denominator for _, _, w in edges))
    av = [int(x * denominator) for x in alpha]
    ev = [((1 << u) | (1 << v), int(w * denominator))
          for u, v, w in edges]
    gate(all(w >= 0 for _, _, w in edges), label + "_nonnegative")
    sums = [0] * (1 << count)
    for subset in range(1, 1 << count):
        bit = subset & -subset
        sums[subset] = sums[subset ^ bit] + av[bit.bit_length() - 1]
        if subset.bit_count() >= 2:
            used = sum(w for mask, w in ev if subset & mask == mask)
            gate(sums[subset] - used >= denominator, label + "_subsets")
    return sum(w for _, _, w in edges)


def forest_graph_checks():
    for k in (2, 3):
        count = 2 * k
        for graph in range(1 << (k * k)):
            forest, isolated, matching, _ = graph_data(k, graph)
            rank = len(forest)
            degree = [0] * count
            for v, w in forest:
                degree[v] += 1
                degree[w] += 1
            axes = tuple(sorted(range(count), key=lambda v: (degree[v], v))[:2])
            tau = Q(rank) - Q(degree[axes[0]] + degree[axes[1]], 2)
            target_tau = Q(rank - 1) + min(Q(1), Q(isolated, 2))
            gate(tau == target_tau, "rank_isolates_statistic")
            gate(matching <= rank, "matching_is_bounded_by_forest_rank")
            if rank <= k - 1:
                gate(isolated >= 2 * k - 2 * rank,
                     "low_rank_forces_unused_vertices")
            for b in FOREST_B:
                a = 2 * b - 1
                alpha = [Q(1, 2) if v in axes else b for v in range(count)]
                edges = [(v, w, alpha[v] + alpha[w] - 1) for v, w in forest]
                total = exact_charges(count, b, axes, edges, "forest")
                gate(total == a * tau, "forest_total_charge")
                for m in range(min(rank, k - 1) + 1):
                    chosen = forest[:m]
                    touched = {v for edge in chosen for v in edge}
                    unused = [v for v in range(count) if v not in touched]
                    gate(len(unused) >= 2, "rank_union_two_unused_axes")
                    union_axes = tuple(unused[:2])
                    weighted = [(v, w, a) for v, w in chosen]
                    total_m = exact_charges(count, b, union_axes, weighted,
                                            "rank_union")
                    gate(total_m == a * m, "rank_union_total_charge")
                    gate(tau >= m, "rank_union_statistic_dominates_m")
                if matching == k:
                    gate(tau >= k - 1, "full_matching_union_charge")
                if rank == 2 * k - 1:
                    gate(tau == 2 * k - 2, "connected_graph_charge")
    # A native endpoint cannot be charged as if it still had weight b.
    b = Q(7, 8)
    gate(Q(1, 2) + b - (2 * b - 1) < 1,
         "negative_control_missing_native_discount")


def cycle_checks():
    for k in range(3, 7):
        for half_length in range(2, k):
            length = 2 * half_length
            unweighted = []
            for j in range(half_length):
                unweighted.extend(((j, k + j),
                                   ((j + 1) % half_length, k + j)))
            axes = (k - 1, 2 * k - 1)
            gate(len(set(unweighted)) == length, "cycle_edge_count")
            for b in FOREST_B:
                a = 2 * b - 1
                w = min(a, b - Q(1, length))
                edges = [(u, v, w) for u, v in unweighted]
                total = exact_charges(2 * k, b, axes, edges, "cycle")
                gate(total == min(a * length, b * length - 1),
                     "cycle_total_charge")
                gate(total - a * (length - 1)
                     == min(a, (1 - b) * (length - 2)),
                     "cycle_improvement_identity")
        for b in (Q(3, 4), Q(7, 8), Q(1)):
            a = 2 * b - 1
            axes = (k - 1, 2 * k - 1)
            edges = [(u, v, b - Q(1, 4))
                     for u in (0, 1) for v in (k, k + 1)]
            edges += [(i, k + i, a) for i in range(2, k - 1)]
            total = exact_charges(2 * k, b, axes, edges, "cycle_matching")
            gate(total == a * (k - 1) + 1, "cycle_matching_total_charge")
            gate(1 + 2 * b * (k - 1) - total == k - 1,
                 "cycle_matching_D_exponent")
    for k in range(2, 41):
        for b in FOREST_B:
            a = 2 * b - 1
            gate(1 + 2 * b * (k - 1) == k + a * (k - 1),
                 "base_exponent_identity")
            gate(k - a * (k - 1) + Q(1, 2) * 2 * a * (k - 1) == k,
                 "connected_half_cutoff_identity")
            if k >= 3:
                charge = a * (k - 1) + 1
                gate(Q(k - 1) + charge / charge == k,
                     "cycle_matching_diagonal_cutoff")
    gate(Q(1, 1) / (Q(3, 4) * 2 + 1) == Q(2, 5),
         "sixth_cycle_cutoff_two_fifths")


def dense_checks():
    represented = 0
    for k in range(3, 25):
        b0 = Q(k, 2 * (k - 1))
        bs = sorted({b0, (b0 + 1) / 2, Q(7, 8), Q(1)})
        for b in bs:
            gate(b0 <= b <= 1, "dense_b_domain")
            A = Q(k - 2 * b, k * (k - 2))
            B = b - Q(1, 2)

            def slack(r, n, t):
                return b * (n + t) + Q(r, 2) - 1 - t * (n * A + r * B)

            corners = (
                (0, 1, 1, Q((k - 1) * (2 * b * (k - 1) - k),
                            k * (k - 2))),
                (0, 1, k, Q((k - 1) * (b * k - 2), k - 2)),
                (0, k - 2, 1, b * (k - 1 + Q(2, k)) - 2),
                (0, k - 2, k, k * (2 * b - 1) - 1),
                (1, 0, 1, Q(0)),
                (1, 0, k, Q(k - 1, 2)),
                (1, k - 2, 1, b * (k - 2 + Q(2, k)) - 1),
                (1, k - 2, k, (k * (2 * b - 1) - 1) / 2),
                (2, 0, 1, 1 - b),
                (2, 0, k, k * (1 - b)),
                (2, k - 2, 1, b * (k - 3 + Q(2, k))),
                (2, k - 2, k, Q(0)),
            )
            for r, n, t, expected in corners:
                gate(slack(r, n, t) == expected, "dense_corner_identities")
                gate(expected >= 0, "dense_corner_nonnegative")
            for r in range(3):
                for n in range(k - 1):
                    for t in range(k + 1):
                        if r + n + t < 2:
                            continue
                        gate(slack(r, n, t) >= 0, "dense_all_subset_classes")
                        represented += comb(2, r) * comb(k - 2, n) * comb(k, t)
            charge = 2 * k * B + k * (k - 2) * A
            gate(charge == 2 * b * (k - 1), "dense_total_charge")
            gate(1 + 2 * b * (k - 1) - charge == 1,
                 "dense_D_exponent")
            gate(1 + charge / (2 * b) == k, "dense_diagonal_cutoff")
            gate(A >= 0 and B >= 0, "dense_nonnegative_charges")
        gate(b0 * k - 2 == Q((k - 2) ** 2, 2 * (k - 1)),
             "dense_lower_endpoint_identities")
        gate(b0 * (k - 1 + Q(2, k)) - 2
             == Q((k - 2) * (k - 3), 2 * (k - 1)),
             "dense_lower_endpoint_identities")
        gate(k * (2 * b0 - 1) - 1 == Q(1, k - 1),
             "dense_lower_endpoint_identities")
        gate(b0 * (k - 2 + Q(2, k)) - 1
             == Q((k - 2) ** 2, 2 * (k - 1)),
             "dense_lower_endpoint_identities")
        bad_b = (b0 + Q(1, 2)) / 2
        bad_A = Q(k - 2 * bad_b, k * (k - 2))
        gate(2 * bad_b - 1 - bad_A < 0,
             "negative_control_dense_below_witness_domain")
    gate(1 / (2 * Q(7, 8)) == Q(4, 7), "dense_four_sevenths_cutoff")
    gate(Q(4, 7) - Q(1, 2) == Q(1, 14), "dense_cutoff_gain")
    return represented


def shared_signature(values, count):
    patterns = []
    for prime in range(2):
        pattern = sum(1 << v for v in range(count)
                      if values[v] & (1 << prime))
        patterns.append(pattern if pattern.bit_count() >= 2 else 0)
    return tuple(patterns)


def base_from_signature(signature, count):
    return tuple(sum(1 << prime for prime in range(2)
                     if signature[prime] & (1 << v))
                 for v in range(count))


def shared_sign(signature):
    return (-1) ** sum((prime + 1) * (pattern + pattern.bit_count())
                      for prime, pattern in enumerate(signature) if pattern)


def selector_values(values, signature, k):
    sign = shared_sign(signature)
    answer = [sign]
    cut = all(NORMS[values[v] & values[w]] < 13
              for side in (range(k), range(k, 2 * k))
              for v, w in combinations(side, 2))
    for threshold in (1, 7, 13, 91):
        graph = graph_from_tuple(values, k, threshold)
        forest, _, matching, cycle4 = graph_data(k, graph)
        rank = len(forest)
        predicates = (rank >= k - 1, matching >= k - 1, matching == k,
                      rank == 2 * k - 1, cycle4,
                      cut and rank >= k - 1)
        answer.extend(sign * int(p) for p in predicates)
    return tuple(answer)


def test_weight(v, ideal):
    # Arbitrary fixed finite test values; no analytic estimate is inferred.
    return (v + 2) * (ideal + 1) + (-1) ** ideal * (1 + v % 2)


def incidence_signed_checks():
    for k in (2, 3):
        count = 2 * k
        records = []
        direct_index = {}
        for values in product(range(4), repeat=count):
            signature = shared_signature(values, count)
            base = base_from_signature(signature, count)
            for v, w in combinations(range(count), 2):
                gate(values[v] & values[w] == base[v] & base[w],
                     "all_pair_gcd_from_shared_incidence")
            selectors = selector_values(values, signature, k)
            gate(selectors == selector_values(base, signature, k),
                 "selectors_independent_of_singletons")
            gate(graph_from_tuple(values, k, 1) == (1 << (k * k)) - 1,
                 "threshold_one_is_complete_graph")
            test = prod(test_weight(v, value) for v, value in enumerate(values))
            direct_index[values] = len(records)
            records.append((values, signature, selectors, test))

        # Independently enumerate shared ideals first, then allowed
        # pairwise-coprime singleton owners for every remaining prime.
        shared_options = [0] + [mask for mask in range(1, 1 << count)
                                if mask.bit_count() >= 2]
        groups = []
        seen = set()
        for signature in product(shared_options, repeat=2):
            base = base_from_signature(signature, count)
            free = [prime for prime in range(2) if signature[prime] == 0]
            children = []
            for owners in product(range(-1, count), repeat=len(free)):
                singletons = [0] * count
                for prime, owner in zip(free, owners):
                    if owner >= 0:
                        singletons[owner] |= 1 << prime
                values = tuple(base[v] | singletons[v] for v in range(count))
                gate(values not in seen, "incidence_reconstruction_unique")
                seen.add(values)
                gate(shared_signature(values, count) == signature,
                     "incidence_reconstruction_signature")
                idx = direct_index[values]
                children.append((tuple(singletons), idx, records[idx][3]))
            groups.append((signature, selector_values(base, signature, k),
                           children))
        gate(len(seen) == 4 ** count, "incidence_reconstruction_complete")

        for phase_pair in product(PHASES, repeat=2):
            eta = (ONE, phase_pair[0], phase_pair[1],
                   zm(phase_pair[0], phase_pair[1]))
            direct = []
            direct_sectors = [ZERO] * 25
            for values, _, selectors, test in records:
                value = ONE
                for v, ideal in enumerate(values):
                    x = eta[ideal] if v < k else zc(eta[ideal])
                    value = zm(value, zs(x, MOBIUS[ideal]))
                value = zs(value, test)
                direct.append(value)
                for j, multiplier in enumerate(selectors):
                    if multiplier:
                        direct_sectors[j] = za(direct_sectors[j],
                                               zs(value, multiplier))

            reconstructed = [ZERO] * 25
            for signature, selectors, children in groups:
                exterior = ONE
                for prime, pattern in enumerate(signature):
                    if not pattern:
                        continue
                    r = (pattern & ((1 << k) - 1)).bit_count()
                    s = (pattern >> k).bit_count()
                    x = phase_pair[prime]
                    local = zm(zp(x, r), zp(zc(x), s))
                    exterior = zm(exterior, zs(local, (-1) ** (r + s)))
                core = ZERO
                for singletons, idx, test in children:
                    value = ONE
                    for v, ideal in enumerate(singletons):
                        x = eta[ideal] if v < k else zc(eta[ideal])
                        value = zm(value, zs(x, MOBIUS[ideal]))
                    value = zs(value, test)
                    gate(zm(exterior, value) == direct[idx],
                         "signed_incidence_all_zero_sixth_phase_identity")
                    core = za(core, value)
                complete_core = zm(exterior, core)
                for j, multiplier in enumerate(selectors):
                    if multiplier:
                        reconstructed[j] = za(reconstructed[j],
                                               zs(complete_core, multiplier))
            for left, right in zip(direct_sectors, reconstructed):
                gate(left == right, "signed_selector_complete_covariances")

        # A balanced shared prime must retain its principal zero mask.
        exact_mask = zm(ZERO, zc(ZERO))
        naive_reduced_zeroth_power = zp(ZERO, 0)
        gate(exact_mask == ZERO and naive_reduced_zeroth_power == ONE,
             "negative_control_dropped_principal_zero")
        left_singleton = (1,) + (0,) * (count - 1)
        right_singleton = (0, 1) + (0,) * (count - 2)
        gate(shared_signature(left_singleton, count)
             == shared_signature(right_singleton, count)
             and bool(left_singleton[0] & 1) != bool(right_singleton[0] & 1),
             "negative_control_singleton_selector_not_eligible")


def locate(name, candidates):
    for directory in candidates:
        candidate = directory / name
        if candidate.is_file():
            return candidate
    raise RuntimeError("Cannot locate required manuscript " + name)


def binding(path):
    raw = path.read_bytes()
    return {"sha256": sha256(raw).hexdigest(), "bytes": len(raw)}


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph-note", type=Path)
    parser.add_argument("--dense-note", type=Path)
    parser.add_argument("--output", type=Path,
                        default=here / "graph_charge_checks.json")
    args = parser.parse_args()
    graph_note = args.graph_note or locate(
        "ARBITRARY_GRAPH_SECTORS.md", (here, here.parent))
    dense_note = args.dense_note or locate(
        "DENSE_CROSS_GCD_SECTORS.md", (here, here.parent,
                                      here.parent / "root"))
    formal_correction_checks()
    forest_graph_checks()
    cycle_checks()
    represented = dense_checks()
    incidence_signed_checks()
    gate(COUNTS["negative_control_missing_native_discount"] == 1,
         "negative_controls_present")
    gate(COUNTS["negative_control_dropped_principal_zero"] == 2,
         "negative_controls_present")
    report = {
        "format": "signed_graph_exact_diagnostics_v1",
        "outcome": "PASS",
        "arithmetic": "integers, rational Fractions, and integral Z[zeta_6]",
        "source_bindings": {
            "ARBITRARY_GRAPH_SECTORS.md": binding(graph_note),
            "DENSE_CROSS_GCD_SECTORS.md": binding(dense_note),
            "check_graph_charges.py": binding(Path(__file__).resolve()),
        },
        "coverage": {
            "formal_forward_axes": [4, 6],
            "formal_forward_prime_exponents": [0, 1, 2],
            "formal_forward_masks": [False, True],
            "formal_phase_values_per_prime": 7,
            "two_prime_norms": [7, 13],
            "two_prime_phase_assignments": 49,
            "signed_moment_orders": [4, 6],
            "signed_tuple_counts_per_phase": {"4": 256, "6": 4096},
            "signed_selectors_per_moment": 25,
            "gcd_thresholds": [1, 7, 13, 91],
            "graph_orders_all_labeled_graphs": [2, 3],
            "graph_counts": {"2": 16, "3": 512},
            "forest_b_values": [str(b) for b in FOREST_B],
            "cycle_k_range": [3, 6],
            "cycle_lengths": "every even length from 4 through 2k-2",
            "dense_k_range": [3, 24],
            "dense_b_values":
                "unique b0, (b0+1)/2, 7/8, 1, with b0=k/(2(k-1))",
            "dense_subset_coverage":
                "all (r,n,t) symmetry classes of all labeled subsets",
            "dense_labeled_subsets_represented": represented,
            "general_exponent_k_range": [2, 40],
        },
        "passed_predicates": dict(sorted(COUNTS.items())),
        "total_passed_predicates": sum(COUNTS.values()),
        "not_verified": [
            "NM2 and PW_b analytic premises or their source proofs",
            "infinite Euler convergence or infinite moment inequalities",
            "genuine global Hecke characters or L-function values",
            "full moments, cofinal hierarchy, zero-free regions, or RH",
            "all-order graph inequalities by finite extrapolation",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS:", report["total_passed_predicates"],
          "exact finite predicates; no analytic bounds certified.")
    print("Report:", args.output)


if __name__ == "__main__":
    main()
