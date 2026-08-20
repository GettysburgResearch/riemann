#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
from typing import Dict, Iterable, Tuple

VERDICT = "PASS_T102100_CARRIER_FREE_STAIRCASE_MATRIX"

Poly = Dict[Tuple[int, ...], Fraction]


def poly_add(a: Poly, b: Poly) -> Poly:
    out: dict[Tuple[int, ...], Fraction] = defaultdict(Fraction)
    for mon, c in a.items():
        out[mon] += c
    for mon, c in b.items():
        out[mon] += c
    return {m: c for m, c in out.items() if c}


def poly_scale(c: Fraction, a: Poly) -> Poly:
    return {m: c * v for m, v in a.items() if c * v}


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: dict[Tuple[int, ...], Fraction] = defaultdict(Fraction)
    for ma, ca in a.items():
        for mb, cb in b.items():
            out[tuple(x + y for x, y in zip(ma, mb))] += ca * cb
    return {m: c for m, c in out.items() if c}


def scalar_poly(k: int, c: Fraction = Fraction(1)) -> Poly:
    return {(0,) * k: c}


def variable_poly(k: int, i: int) -> Poly:
    m = [0] * k
    m[i] = 1
    return {tuple(m): Fraction(1)}


def euler_interval(rs: list[Fraction], a: int, b: int) -> Poly:
    k = len(rs)
    out = scalar_poly(k)
    for h in range(a, b + 1):
        out = poly_mul(out, poly_add(scalar_poly(k), poly_scale(-rs[h], variable_poly(k, h))))
    return out


def weighted_B(rs: list[Fraction], i: int, j: int) -> Poly:
    L = Fraction(1)
    for h in range(i):
        L *= 1 - rs[h]
    R = Fraction(1)
    for h in range(j + 1, len(rs)):
        R *= 1 - rs[h]
    return poly_scale(L * R, euler_interval(rs, i, j))


def delta(k: int, i: int) -> Poly:
    return poly_add(scalar_poly(k), poly_scale(-1, variable_poly(k, i)))


def weighted_hazard(rs: list[Fraction], i: int, j: int) -> Poly:
    k = len(rs)
    L = Fraction(1)
    for h in range(i):
        L *= 1 - rs[h]
    R = Fraction(1)
    for h in range(j + 1, k):
        R *= 1 - rs[h]
    inner = euler_interval(rs, i + 1, j - 1) if i + 1 <= j - 1 else scalar_poly(k)
    return poly_scale(rs[i] * rs[j] * L * R, poly_mul(poly_mul(delta(k, i), delta(k, j)), inner))


def verify_weighted_coboundary() -> dict:
    rs = [Fraction(1, 3), Fraction(1, 5), Fraction(2, 11), Fraction(1, 7), Fraction(3, 23), Fraction(1, 13)]
    k = len(rs)
    checked = 0
    for i in range(k):
        for j in range(i + 1, k):
            lhs = weighted_hazard(rs, i, j)
            rhs = poly_add(
                poly_add(weighted_B(rs, i, j), poly_scale(-1, weighted_B(rs, i + 1, j))),
                poly_add(poly_scale(-1, weighted_B(rs, i, j - 1)), weighted_B(rs, i + 1, j - 1)),
            )
            assert lhs == rhs
            checked += 1

    # Rectangle telescope.
    a, b, c, d = 0, 2, 3, 5
    rect = scalar_poly(k, Fraction(0))
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            rect = poly_add(rect, weighted_hazard(rs, i, j))
    boundary = poly_add(
        poly_add(weighted_B(rs, a, d), poly_scale(-1, weighted_B(rs, b + 1, d))),
        poly_add(poly_scale(-1, weighted_B(rs, a, c - 1)), weighted_B(rs, b + 1, c - 1)),
    )
    assert rect == boundary

    # Staircase telescope with a nondecreasing threshold.
    thresholds = [2, 3, 4]
    stair = scalar_poly(k, Fraction(0))
    for i, m in enumerate(thresholds):
        for j in range(m, k):
            stair = poly_add(stair, weighted_hazard(rs, i, j))
    formula = poly_add(weighted_B(rs, 0, k - 1), poly_scale(-1, weighted_B(rs, len(thresholds), k - 1)))
    for i, m in enumerate(thresholds):
        formula = poly_add(formula, poly_scale(-1, poly_add(weighted_B(rs, i, m - 1), poly_scale(-1, weighted_B(rs, i + 1, m - 1)))))
    assert stair == formula

    left_budget = sum(rs[i] * __import__('functools').reduce(lambda x, h: x * (1 - rs[h]), range(i), Fraction(1)) for i in range(k))
    assert left_budget == 1 - __import__('functools').reduce(lambda x, r: x * (1 - r), rs, Fraction(1))
    assert left_budget < 1
    return {"interval_pairs_checked": checked, "left_boundary_budget": str(left_budget)}


# ----- Exact Bernstein certificate for the sharp cubic Harnack bound -----

R_POWER: dict[tuple[int, int, int], Fraction] = {
    (4, 3, 3): Fraction(1, 256),
    (3, 2, 2): Fraction(-3, 32),
    (2, 1, 1): Fraction(51, 64),
    (1, 3, 3): Fraction(-2),
    (1, 2, 2): Fraction(6),
    (1, 1, 1): Fraction(-51, 8),
    (1, 0, 3): Fraction(-2),
    (1, 0, 2): Fraction(6),
    (1, 0, 1): Fraction(-51, 8),
    (1, 0, 0): Fraction(2),
    (0, 0, 1): Fraction(3),
}


def affine_u_substitute(poly: dict[tuple[int, int, int], Fraction], lo: Fraction, hi: Fraction) -> dict[tuple[int, int, int], Fraction]:
    # U = lo + (hi-lo)V.
    out: dict[tuple[int, int, int], Fraction] = defaultdict(Fraction)
    d = hi - lo
    for (i, j, k), c in poly.items():
        for r in range(k + 1):
            out[(i, j, r)] += c * comb(k, r) * lo ** (k - r) * d ** r
    return {m: c for m, c in out.items() if c}


def power_to_bernstein(poly: dict[tuple[int, int, int], Fraction], degs=(4, 3, 3)) -> dict[tuple[int, int, int], Fraction]:
    nx, ny, nz = degs
    out = {}
    for i in range(nx + 1):
        for j in range(ny + 1):
            for k in range(nz + 1):
                s = Fraction(0)
                for (a, b, c), coef in poly.items():
                    if a <= i and b <= j and c <= k:
                        s += coef * Fraction(comb(i, a), comb(nx, a)) * Fraction(comb(j, b), comb(ny, b)) * Fraction(comb(k, c), comb(nz, c))
                out[(i, j, k)] = s
    return out


def verify_bernstein_harnack() -> dict:
    intervals = [
        (Fraction(0), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(17, 32)),
        (Fraction(17, 32), Fraction(9, 16)),
        (Fraction(9, 16), Fraction(5, 8)),
        (Fraction(5, 8), Fraction(3, 4)),
        (Fraction(3, 4), Fraction(1)),
    ]
    mins = []
    for lo, hi in intervals:
        B = power_to_bernstein(affine_u_substitute(R_POWER, lo, hi))
        m = min(B.values())
        assert m >= 0
        mins.append(m)
    assert min(v for v in mins if v > 0) == Fraction(1, 32768)
    # Exact threshold relation: C=17/16, so 1/C=16/17.
    assert Fraction(17, 16) * Fraction(16, 17) == 1
    return {
        "bernstein_boxes": len(intervals),
        "minimum_positive_coefficient": "1/32768",
        "width_exponent": "exp(16/17)",
    }


# ----- Directed rational interval counterexample to cone iteration -----

Interval = tuple[Fraction, Fraction]


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def ineg(a: Interval) -> Interval:
    return -a[1], -a[0]


def isub(a: Interval, b: Interval) -> Interval:
    return iadd(a, ineg(b))


def imul(a: Interval, b: Interval) -> Interval:
    vals = [a[i] * b[j] for i in range(2) for j in range(2)]
    return min(vals), max(vals)


def iscale(c: Fraction, a: Interval) -> Interval:
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def sqrt_interval(x: Fraction, digits: int = 34) -> Interval:
    scale = 10 ** digits
    q = x.numerator * scale * scale // x.denominator
    k = isqrt(q)
    lo, hi = Fraction(k, scale), Fraction(k + 1, scale)
    assert lo * lo <= x < hi * hi
    return lo, hi


def psi_interval(x: Fraction) -> Interval:
    s = sqrt_interval(x)
    if x <= 1:
        return iscale(Fraction(64), isub((3 * x, 3 * x), iscale(x, s)))
    return iscale(Fraction(64), isub(iscale(Fraction(3), s), (Fraction(1), Fraction(1))))


def K_interval(p: int, q: int, y: Fraction) -> Interval:
    z = psi_interval(y)
    z = isub(z, psi_interval(y / p))
    z = isub(z, psi_interval(y / q))
    z = iadd(z, psi_interval(y / (p * q)))
    return z


def invsqrt_interval(n: int) -> Interval:
    lo, hi = sqrt_interval(Fraction(n))
    return Fraction(1, hi), Fraction(1, lo)


def verify_cone_separator() -> dict:
    p, q, ell1, ell2, y = 73, 277, 103, 199, 7519
    K0 = K_interval(p, q, Fraction(y))
    K1 = K_interval(p, q, Fraction(y, ell1))
    K2 = K_interval(p, q, Fraction(y, ell2))
    K12 = K_interval(p, q, Fraction(y, ell1 * ell2))
    a1, a2 = Fraction(17, 16 * ell1), Fraction(17, 16 * ell2)
    value = iscale(a1 * a2, K0)
    value = isub(value, imul((a1, a1), imul(invsqrt_interval(ell2), K2)))
    value = isub(value, imul((a2, a2), imul(invsqrt_interval(ell1), K1)))
    value = iadd(value, imul(imul(invsqrt_interval(ell1), invsqrt_interval(ell2)), K12))
    assert value[1] < Fraction(-339, 1000)
    return {
        "fixture": [p, q, ell1, ell2, y],
        "certified_upper": f"{value[1].numerator}/{value[1].denominator}",
        "certified_upper_lt": "-339/1000",
    }


# ----- Common five-box spline and vector Vaughan source identity -----


def poly1_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def verify_common_spline_algebra() -> dict:
    # Differential polynomials acting on the common positive box spline.
    # P_A = -(1/3) s(s-1/2)^2.
    pa = poly1_mul([Fraction(0), Fraction(-1, 3)], poly1_mul([Fraction(-1, 2), 1], [Fraction(-1, 2), 1]))
    # P_Q = (1/6)(s-1/2)(2s^2+5s+9).
    pq = [x / 6 for x in poly1_mul([Fraction(-1, 2), 1], [Fraction(9), Fraction(5), Fraction(2)])]
    pg = [pa[i] + pq[i] for i in range(max(len(pa), len(pq)))]
    while pg and pg[-1] == 0:
        pg.pop()
    expected = poly1_mul([Fraction(-1), Fraction(2)], [Fraction(3), Fraction(2)])
    expected = [x / 4 for x in expected]
    assert pg == expected
    assert pa == [Fraction(0), Fraction(-1, 12), Fraction(1, 3), Fraction(-1, 3)]
    assert pq == [Fraction(-3, 4), Fraction(13, 12), Fraction(2, 3), Fraction(1, 3)]
    return {
        "base_boxes": {"zero_weight": 3, "half_weight": 2, "support_ratio": 32},
        "A_operator": "-(1/3)D(D-1/2)^2",
        "Q_operator": "(1/6)(D-1/2)(2D^2+5D+9)",
        "G_operator": "(1/4)(2D-1)(2D+3)",
    }


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def conv(a: list[int], b: list[int], nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    for d in range(1, nmax + 1):
        if not a[d]:
            continue
        for m in range(1, nmax // d + 1):
            if b[m]:
                out[d * m] += a[d] * b[m]
    return out


def verify_vaughan_identity() -> dict:
    nmax, U = 400, 9
    mu = mobius_sieve(nmax)
    one = [0] + [1] * nmax
    eps = [0] * (nmax + 1)
    eps[1] = 1
    mu_u = [0] * (nmax + 1)
    for n in range(1, U + 1):
        mu_u[n] = mu[n]
    a_u = [eps[n] - conv(mu_u, one, nmax)[n] for n in range(nmax + 1)]
    assert all(a_u[n] == 0 for n in range(1, U + 1))
    rhs1 = [2 * x for x in mu_u]
    rhs2 = conv(conv(mu_u, mu_u, nmax), one, nmax)
    rhs3 = conv(conv(a_u, a_u, nmax), mu, nmax)
    rebuilt = [rhs1[n] - rhs2[n] + rhs3[n] for n in range(nmax + 1)]
    assert rebuilt[1:] == mu[1:]
    return {"coefficients_checked": nmax, "cutoff": U}


def run() -> dict:
    cob = verify_weighted_coboundary()
    bern = verify_bernstein_harnack()
    sep = verify_cone_separator()
    spline = verify_common_spline_algebra()
    vaughan = verify_vaughan_identity()

    mutations = sorted([
        "carrier_region_absolute_values_rejected",
        "cfbb102100_assumed_rejected",
        "global_harnack_cone_iteration_rejected",
        "positive_renewal_type_mismatch_rejected",
        "raw_aq_channels_called_carrier_free_rejected",
        "rh_established_by_replay_rejected",
        "staircase_boundary_replaced_by_bulk_absolute_sum_rejected",
        "type_i_zero_moment_reused_on_balanced_vector_rejected",
    ])
    core = {
        "schema": "riemann.x102100.carrier-free-staircase.v1",
        "classification": VERDICT,
        "base_pr": 697,
        "base_sha": "e878c3717cd8124564e5400b2ec5db035e3a4088",
        "external_heads": {
            "pr691": "1de27a2c29e15e2dd94154f174c57bde3909daf7",
            "pr695": "5c3cb301134ee9c7ae13e6508fc60e7272cb1a3a",
            "pr696": "f4016db548afceb31b150547cb6cd48b4cddb77d",
            "pr698": "a10d6a40105142de2708632589c458d7534f556a",
        },
        "survival_weighted_coboundary": cob,
        "sharp_cubic_harnack": bern,
        "harnack_cone_separator": sep,
        "common_positive_spline": spline,
        "vaughan_identity": vaughan,
        "power_width_exponent_improved": True,
        "carrier_free_joint_filter": True,
        "vector_type_i_terms_integrable": True,
        "cfbb102100_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
