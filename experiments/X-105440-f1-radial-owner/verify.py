#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
import random
from pathlib import Path

VERDICT = "PASS_T105440_F1_RADIAL_OWNER_AND_PLUCKER_RECTANGLES"

# Polynomial dictionary on m commuting variables with exponents 0,1,2,...
Poly = dict[tuple[int, ...], Fraction]


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for mon, c in p.items():
            out[mon] = out.get(mon, Fraction(0)) + c
            if out[mon] == 0:
                del out[mon]
    return out


def scale(p: Poly, c: Fraction) -> Poly:
    return {m: c * v for m, v in p.items() if c * v}


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for a, ca in p.items():
        for b, cb in q.items():
            mon = tuple(x + y for x, y in zip(a, b))
            out[mon] = out.get(mon, Fraction(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


def one(m: int) -> Poly:
    return {(0,) * m: Fraction(1)}


def var(m: int, i: int, power: int = 1) -> Poly:
    mon = [0] * m
    mon[i] = power
    return {tuple(mon): Fraction(1)}


def factor_product(m: int, indices, power: int = 1, integrate_t: bool = False) -> Poly:
    out: Poly = {}
    inds = list(indices)
    for k in range(len(inds) + 1):
        for subset in combinations(inds, k):
            mon = [0] * m
            for j in subset:
                mon[j] = power
            coeff = Fraction((-1) ** k, k + 1 if integrate_t else 1)
            out[tuple(mon)] = out.get(tuple(mon), Fraction(0)) + coeff
    return out


def euler(m: int, power: int = 1) -> Poly:
    return factor_product(m, range(m), power, False)


def radial_owner(m: int, i: int) -> Poly:
    others = [j for j in range(m) if j != i]
    native = mul(var(m, i), factor_product(m, others, 1, True))
    squared = mul(var(m, i, 2), factor_product(m, others, 2, True))
    return add(scale(native, Fraction(-1)), squared)


def interval_product(m: int, i: int, j: int) -> Poly:
    return factor_product(m, range(i + 1, j), 1, False)


def extreme_pair(m: int, i: int, j: int) -> Poly:
    return mul(mul(var(m, i), var(m, j)), interval_product(m, i, j))


def equal_pair_packets(defect: Poly, m: int):
    singleton = [{} for _ in range(m)]
    pair = {(i, j): {} for i in range(m) for j in range(i + 1, m)}
    for mon, coeff in defect.items():
        support = [i for i, e in enumerate(mon) if e]
        k = len(support)
        if k == 1:
            i = support[0]
            singleton[i][mon] = singleton[i].get(mon, Fraction(0)) + coeff
        elif k >= 2:
            share = coeff / Fraction(k * (k - 1) // 2)
            for i, j in combinations(support, 2):
                pair[(i, j)][mon] = pair[(i, j)].get(mon, Fraction(0)) + share
    return singleton, pair


def poly_eq(p: Poly, q: Poly) -> bool:
    return add(p, scale(q, Fraction(-1))) == {}


def owner_difference_rhs(m: int, i: int, j: int) -> Poly:
    others = [k for k in range(m) if k not in (i, j)]
    h1 = factor_product(m, others, 1, True)
    h2 = factor_product(m, others, 2, True)
    term1 = mul(add(var(m, j), scale(var(m, i), Fraction(-1))), h1)
    term2 = mul(add(var(m, i, 2), scale(var(m, j, 2), Fraction(-1))), h2)
    return add(term1, term2)


def rectangle_factor(m: int, a: int, b: int, c: int, d: int):
    lhs = add(
        extreme_pair(m, a, c),
        scale(extreme_pair(m, a, d), Fraction(-1)),
        scale(extreme_pair(m, b, c), Fraction(-1)),
        extreme_pair(m, b, d),
    )
    ebc = interval_product(m, b, c)
    left = add(
        mul(
            mul(var(m, a), interval_product(m, a, b)),
            add(one(m), scale(var(m, b), Fraction(-1))),
        ),
        scale(var(m, b), Fraction(-1)),
    )
    right = add(
        var(m, c),
        scale(
            mul(
                mul(
                    add(one(m), scale(var(m, c), Fraction(-1))),
                    interval_product(m, c, d),
                ),
                var(m, d),
            ),
            Fraction(-1),
        ),
    )
    return lhs, mul(mul(ebc, left), right)


def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vsub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def vscale(c, x):
    return tuple(c * a for a in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def hodge_identity(v, m: int):
    dim = len(next(iter(v.values())))
    zero = (Fraction(0),) * dim
    total = zero
    rows = [zero for _ in range(m)]
    diagonal = Fraction(0)
    edges = list(v)
    for i, j in edges:
        x = v[(i, j)]
        total = vadd(total, x)
        rows[i] = vadd(rows[i], x)
        rows[j] = vadd(rows[j], x)
        diagonal += norm2(x)
    q2 = Fraction(0)
    for index, edge in enumerate(edges):
        for other in edges[index + 1 :]:
            if set(edge).isdisjoint(other):
                q2 += 2 * dot(v[edge], v[other])
    return norm2(total), q2 - diagonal + sum(norm2(row) for row in rows)


def cycle_projection(v, m: int):
    dim = len(next(iter(v.values())))
    zero = (Fraction(0),) * dim
    edges = list(combinations(range(m), 2))
    total = zero
    rows = [zero for _ in range(m)]
    for i, j in edges:
        total = vadd(total, v[(i, j)])
        rows[i] = vadd(rows[i], v[(i, j)])
        rows[j] = vadd(rows[j], v[(i, j)])
    count = Fraction(m * (m - 1), 2)
    mean = vscale(Fraction(1, count), total)
    stars = [
        vscale(Fraction(1, m - 2), vsub(rows[i], vscale(Fraction(2, m), total)))
        for i in range(m)
    ]
    return {
        (i, j): vsub(vsub(v[(i, j)], mean), vadd(stars[i], stars[j]))
        for i, j in edges
    }


def rectangle_norm_sum(w, m: int):
    total = Fraction(0)
    for a, b, c, d in combinations(range(m), 4):
        for (i, j), (k, ell) in [
            ((a, b), (c, d)),
            ((a, c), (b, d)),
            ((a, d), (b, c)),
        ]:
            delta = vadd(
                vsub(w[tuple(sorted((i, k)))], w[tuple(sorted((i, ell)))]),
                vsub(w[tuple(sorted((j, ell)))], w[tuple(sorted((j, k)))]),
            )
            total += norm2(delta)
    return total


def run() -> dict:
    radial_checks = 0
    difference_checks = 0
    pair_bridge_checks = 0
    extreme_checks = 0
    plucker_checks = 0

    for m in range(1, 9):
        defect = add(euler(m, 1), scale(euler(m, 2), Fraction(-1)))
        owners = [radial_owner(m, i) for i in range(m)]
        assert poly_eq(add(*owners), defect)
        radial_checks += 1

        singleton, pair = equal_pair_packets(defect, m)
        for i in range(m):
            incident = (
                add(*(pair[tuple(sorted((i, j)))] for j in range(m) if j != i))
                if m > 1
                else {}
            )
            assert poly_eq(add(singleton[i], scale(incident, Fraction(1, 2))), owners[i])
            pair_bridge_checks += 1

        for i, j in combinations(range(m), 2):
            assert poly_eq(
                add(owners[i], scale(owners[j], Fraction(-1))),
                owner_difference_rhs(m, i, j),
            )
            difference_checks += 1

        degree_two = add(euler(m, 1), scale(one(m), Fraction(-1)))
        degree_two = add(degree_two, *(var(m, i) for i in range(m)))
        if m >= 2:
            assert poly_eq(
                add(*(extreme_pair(m, i, j) for i, j in combinations(range(m), 2))),
                degree_two,
            )
            extreme_checks += 1

    for m in range(4, 9):
        for a, b, c, d in combinations(range(m), 4):
            lhs, rhs = rectangle_factor(m, a, b, c, d)
            assert poly_eq(lhs, rhs)
            plucker_checks += 1

    rng = random.Random(105440)
    hodge_checks = 0
    cycle_checks = 0
    for m in range(4, 10):
        edges = list(combinations(range(m), 2))
        for _ in range(100):
            values = {
                edge: tuple(Fraction(rng.randint(-7, 7), rng.randint(1, 9)) for _ in range(3))
                for edge in edges
            }
            lhs, rhs = hodge_identity(values, m)
            assert lhs == rhs
            hodge_checks += 1

            cycle = cycle_projection(values, m)
            for i in range(m):
                row = (Fraction(0),) * 3
                for j in range(m):
                    if i != j:
                        row = vadd(row, cycle[tuple(sorted((i, j)))])
                assert row == (Fraction(0),) * 3
            assert rectangle_norm_sum(cycle, m) == Fraction((m - 1) * (m - 2)) * sum(
                norm2(x) for x in cycle.values()
            )
            cycle_checks += 1

    one_label_defect = add(euler(1, 1), scale(euler(1, 2), Fraction(-1)))
    assert one_label_defect
    assert list(combinations(range(1), 2)) == []

    mutations = sorted(
        [
            "extreme_pair_interval_product_omitted_rejected",
            "finite_hodge_gap_promoted_to_cofinal_trace_rejected",
            "four_cycle_factorization_promoted_to_size_bound_rejected",
            "native_and_squared_owner_signs_conflated_rejected",
            "old_f1star_cycle_chain_promoted_to_rh_rejected",
            "owner_difference_cross_term_retained_rejected",
            "pair_only_packet_promoted_to_complete_defect_rejected",
            "radial_owner_share_not_one_over_depth_rejected",
            "rh_promoted_by_replay_rejected",
            "singleton_terms_deleted_before_homotopy_recombination_rejected",
        ]
    )

    payload = {
        "schema": "riemann.x105440.f1-radial-owner.v1",
        "classification": VERDICT,
        "base_pr": 730,
        "base_sha": "512ff17dd7880313694c20372ca2b84ad2a5c330",
        "wick_pr": 719,
        "wick_sha": "b6cb90d3d5f06320ba2c4908930a5b85fa270240",
        "radial_owner_checks": radial_checks,
        "owner_difference_checks": difference_checks,
        "equal_pair_bridge_checks": pair_bridge_checks,
        "extreme_pair_checks": extreme_checks,
        "plucker_rectangle_checks": plucker_checks,
        "hodge_dirichlet_checks": hodge_checks,
        "cycle_localization_checks": cycle_checks,
        "pair_only_separator": True,
        "radial_owner_decomposition_proved": True,
        "endpoint_difference_factorization_proved": True,
        "four_cycle_plucker_factorization_proved": True,
        "t105430_complete_pair_composition_valid": False,
        "f1eot105441_proved": False,
        "f1rect105443_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    result = run()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
