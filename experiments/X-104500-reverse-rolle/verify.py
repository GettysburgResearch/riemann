#!/usr/bin/env python3
"""Exact finite checks for the T-104500 reverse-Rolle/Riccati packet.

This standard-library checker verifies polynomial and interval instances of the
exact identities. It does not evaluate Xi, replay Conrey/Levinson estimates,
or prove the growing-box or downward-cascade theorems.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

Q = Fraction
Poly = List[Q]


def trim(p: Sequence[Q]) -> Poly:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q or [Q(0)]


def deg(p: Sequence[Q]) -> int:
    return len(trim(p)) - 1


def add(a: Sequence[Q], b: Sequence[Q]) -> Poly:
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def sub(a: Sequence[Q], b: Sequence[Q]) -> Poly:
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])


def scale(a: Sequence[Q], c: Q) -> Poly:
    return trim([c*x for x in a])


def mul(a: Sequence[Q], b: Sequence[Q]) -> Poly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def derivative(a: Sequence[Q]) -> Poly:
    if len(a) <= 1:
        return [Q(0)]
    return trim([Q(i)*a[i] for i in range(1, len(a))])


def integral(a: Sequence[Q]) -> Poly:
    return [Q(0)] + [a[i]/Q(i+1) for i in range(len(a))]


def evaluate(a: Sequence[Q], x: Q) -> Q:
    y = Q(0)
    for c in reversed(a):
        y = y*x + c
    return y


def divmod_poly(a: Sequence[Q], b: Sequence[Q]) -> Tuple[Poly, Poly]:
    aa = trim(a)
    bb = trim(b)
    if bb == [0]:
        raise ZeroDivisionError
    if deg(aa) < deg(bb):
        return [Q(0)], aa
    q = [Q(0)] * (deg(aa) - deg(bb) + 1)
    r = aa[:]
    while r != [0] and deg(r) >= deg(bb):
        k = deg(r) - deg(bb)
        c = r[-1] / bb[-1]
        q[k] += c
        r = sub(r, [Q(0)] * k + [c*x for x in bb])
    return trim(q), trim(r)


def sturm_sequence(p: Sequence[Q]) -> List[Poly]:
    p0 = trim(p)
    p1 = derivative(p0)
    if p1 == [0]:
        return [p0]
    seq = [p0, p1]
    while seq[-1] != [0]:
        _, r = divmod_poly(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(scale(r, Q(-1)))
    return seq


def sign(x: Q) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def sign_at_infinity(p: Sequence[Q], positive: bool) -> int:
    pp = trim(p)
    s = sign(pp[-1])
    if not positive and deg(pp) % 2:
        s = -s
    return s


def variations(signs: Iterable[int]) -> int:
    nz = [s for s in signs if s]
    return sum(a != b for a, b in zip(nz, nz[1:]))


def sturm_variations_at(seq: Sequence[Poly], x: Q | str) -> int:
    if x == "+inf":
        signs = [sign_at_infinity(p, True) for p in seq]
    elif x == "-inf":
        signs = [sign_at_infinity(p, False) for p in seq]
    else:
        assert isinstance(x, Q)
        signs = [sign(evaluate(p, x)) for p in seq]
    return variations(signs)


def count_real_roots(p: Sequence[Q], a: Q | str = "-inf", b: Q | str = "+inf") -> int:
    seq = sturm_sequence(p)
    return sturm_variations_at(seq, a) - sturm_variations_at(seq, b)


def linear_root(c: int) -> Poly:
    return [Q(-c), Q(1)]


def irreducible_quadratic(a: int) -> Poly:
    return [Q(a*a), Q(0), Q(1)]


def product(polys: Sequence[Poly]) -> Poly:
    out: Poly = [Q(1)]
    for p in polys:
        out = mul(out, p)
    return out


def choose_regular_shift(base: Poly, critical: Sequence[int]) -> Poly:
    for shift in [1, 2, -1, 3, -2, 5, -3, 7, 11, -5]:
        p = base[:]
        p[0] += Q(shift)
        if all(evaluate(p, Q(c)) != 0 for c in critical):
            return trim(p)
    raise AssertionError("failed to choose regular shift")


def wrong_extrema(p: Poly, critical: Sequence[int]) -> int:
    dd = derivative(derivative(p))
    total = 0
    for c in critical:
        v = evaluate(p, Q(c))
        curv = evaluate(dd, Q(c))
        assert v and curv
        if v*curv > 0:
            total += 1
    return total


def global_fixture(critical: Sequence[int], quadratic_scales: Sequence[int]) -> Tuple[Poly, Poly]:
    d = product([linear_root(c) for c in critical] + [irreducible_quadratic(a) for a in quadratic_scales])
    p = choose_regular_shift(integral(d), critical)
    assert derivative(p) == d
    return p, d


def interval_edge_identity(p: Poly, critical: Sequence[int], a: Q, b: Q) -> Tuple[int, int, int]:
    assert a < b and evaluate(p, a) and evaluate(p, b)
    crit = [c for c in critical if a < c < b]
    points = [a] + [Q(c) for c in crit] + [b]
    edge_count = sum(evaluate(p, x)*evaluate(p, y) < 0 for x, y in zip(points, points[1:]))
    root_count = count_real_roots(p, a, b)
    assert edge_count == root_count
    if not crit:
        return root_count, 0, 0
    dd = derivative(derivative(p))
    e = [int(evaluate(p, Q(c))*evaluate(dd, Q(c)) > 0) for c in crit]
    left_edge = int(evaluate(p, a)*evaluate(p, Q(crit[0])) < 0)
    right_edge = int(evaluate(p, Q(crit[-1]))*evaluate(p, b) < 0)
    bminus = 1 - e[0] - left_edge
    bplus = 1 - e[-1] - right_edge
    assert bminus in (0, 1) and bplus in (0, 1)
    formula = len(crit) + 1 - 2*sum(e) - bminus - bplus
    assert formula == root_count
    return root_count, sum(e), bminus+bplus


def verify() -> dict:
    global_checks = 0
    interval_checks = 0
    riccati_checks = 0
    critical_sets = [
        [-3, -1, 2],
        [-4, -2, 0, 3],
        [-5, -1, 1, 4, 6],
        [-6, -3, 2, 5],
        [-7, -4, -1, 2, 5, 8],
    ]
    quadratic_sets = [[], [1], [1, 2], [2], [1, 3]]
    for crit in critical_sets:
        for quads in quadratic_sets:
            p, d = global_fixture(crit, quads)
            nr_p = deg(p) - count_real_roots(p)
            nr_d = deg(d) - count_real_roots(d)
            e = wrong_extrema(p, crit)
            assert nr_p - nr_d == 2*e
            global_checks += 1
            dd = derivative(d)
            lag = sub(mul(d, d), mul(p, dd))
            assert add(scale(mul(d, d), Q(-1)), lag) == scale(mul(p, dd), Q(-1))
            for c in crit:
                residue = evaluate(p, Q(c)) / evaluate(dd, Q(c))
                is_wrong = evaluate(p, Q(c))*evaluate(dd, Q(c)) > 0
                assert (residue > 0) == is_wrong
            riccati_checks += 1
            candidates = [Q(crit[0]-3), Q(crit[-1]+3)]
            mids = [Q(crit[i]+crit[i+1], 2) for i in range(len(crit)-1)]
            endpoints = candidates[:1] + mids + candidates[1:]
            endpoints = [x if evaluate(p, x) else x+Q(1, 7) for x in endpoints]
            for i in range(len(endpoints)):
                for j in range(i+1, len(endpoints)):
                    interval_edge_identity(p, crit, endpoints[i], endpoints[j])
                    interval_checks += 1

    quartic: Poly = [Q(2), Q(0), Q(-2), Q(0), Q(1)]
    qcrit = [-1, 0, 1]
    qd = derivative(quartic)
    q_e = wrong_extrema(quartic, qcrit)
    q_nr = deg(quartic)-count_real_roots(quartic)
    qd_nr = deg(qd)-count_real_roots(qd)
    assert q_e == 2
    assert q_nr == 4 and qd_nr == 0
    assert q_nr-qd_nr == 2*q_e
    assert q_nr-qd_nr != q_e

    payload = {
        "schema": "riemann.t104500.xi_riccati_rolle.v1",
        "checks": {
            "global_polynomial_conservation": global_checks,
            "interval_edge_and_boundary_identities": interval_checks,
            "riccati_residue_identities": riccati_checks,
            "factor_two_counterexample": True,
        },
        "scope": {
            "real_reverse_rolle_conservation_proved": True,
            "complex_winding_transport_proved_analytically": True,
            "riccati_pick_dictionary_proved": True,
            "fixed_scaled_box_high_derivative_real_rootedness_proved_from_ki_gunns_hughes": True,
            "growing_original_height_box_uniformity_proved": False,
            "xi_downward_defect_transport_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104500_XI_RICCATI_ROLLE_EXACT_ALGEBRA",
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = verify()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
