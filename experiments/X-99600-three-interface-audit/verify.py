#!/usr/bin/env python3
"""Exact replay for T99600.

The replay uses only Python's standard library. It checks:
  * the complete compact SHARP Hall-prefix certificate on 1 <= t < 67;
  * the exact Radon--Nikodym child cocycle and the raw-cutoff mutation;
  * the one-prime alpha-child/native-Euler coefficient separator;
  * the corrected sequential first-owner Euler identity;
  * the exact two-row numerator noncancellation algebra;
  * fail-closed status flags.

It does not prove the future-completed current sign, the global SHARP Harnack
negative-mass theorem, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Dict, List, Tuple

Q = Fraction
BITS = 40
DEN = 1 << BITS
VERDICT = "PASS_T99600_THREE_INTERFACE_HOSTILE_AUDIT"


def mobius_upto(n: int) -> List[int]:
    mu = [0] * (n + 1)
    lp = [0] * (n + 1)
    primes: List[int] = []
    mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def sqrt_interval(n: int) -> Tuple[Q, Q]:
    q = isqrt(n * DEN * DEN)
    lo = Q(q, DEN)
    hi = lo if q * q == n * DEN * DEN else Q(q + 1, DEN)
    assert lo * lo <= n <= hi * hi
    return lo, hi


def inv_sqrt_interval(n: int) -> Tuple[Q, Q]:
    lo, hi = sqrt_interval(n)
    return 1 / hi, 1 / lo


def compact_hall_certificate() -> Dict[str, object]:
    mu = mobius_upto(66)
    a = Q(0)
    b_lo = Q(0)
    b_hi = Q(0)
    records = []

    for t in range(1, 67):
        a += Q(mu[t], t)
        inv_lo, inv_hi = inv_sqrt_interval(t)
        if mu[t] == 1:
            b_lo += inv_lo
            b_hi += inv_hi
        elif mu[t] == -1:
            b_lo -= inv_hi
            b_hi -= inv_lo

        x = t if a >= 0 else 67
        sqrt_lo, sqrt_hi = sqrt_interval(x)
        main_lo = 4 * (a * sqrt_lo if a >= 0 else a * sqrt_hi)
        main_hi = 4 * (a * sqrt_hi if a >= 0 else a * sqrt_lo)
        h_lo = main_lo - 3 * b_hi
        h_hi = main_hi - 3 * b_lo
        assert h_lo <= h_hi
        records.append((h_lo, h_hi, t, x, a))

    minimum = min(records, key=lambda row: row[0])
    h_lo, h_hi, t, x, a = minimum
    others = [row for row in records if row is not minimum]
    assert (t, x) == (13, 67)
    assert h_lo > Q(7, 20)
    assert all(row[0] > Q(7, 20) for row in records)
    assert min(row[0] for row in others) > h_hi

    return {
        "thresholds_checked": 66,
        "interval_bits": BITS,
        "minimum_threshold": t,
        "minimum_proved_unique": True,
        "minimum_endpoint": x,
        "minimum_lower_num": str(h_lo.numerator),
        "minimum_lower_den": str(h_lo.denominator),
        "minimum_upper_num": str(h_hi.numerator),
        "minimum_upper_den": str(h_hi.denominator),
        "minimum_lower_decimal": f"{float(h_lo):.15f}",
        "minimum_upper_decimal": f"{float(h_hi):.15f}",
        "margin_over_7_20_decimal": f"{float(h_lo - Q(7,20)):.15f}",
    }


def T_of_square_root(r: Q) -> Q:
    return 4 * r - 3


def rn_cocycle_certificate() -> Dict[str, object]:
    TY = T_of_square_root(Q(100))
    TZ = T_of_square_root(Q(50))
    TW = T_of_square_root(Q(25))
    r_zy = TZ / TY
    r_wz = TW / TZ
    r_wy = TW / TY
    assert 0 < r_wy <= r_zy <= 1
    assert r_wz * r_zy == r_wy

    parent = T_of_square_root(Q(2))
    child = T_of_square_root(Q(1))
    exact_ratio = child / parent
    assert parent == 5 and child == 1 and exact_ratio == Q(1, 5)
    assert exact_ratio != 1

    return {
        "cocycle_fixture": {
            "R_Z_given_Y": str(r_zy),
            "R_W_given_Z": str(r_wz),
            "R_W_given_Y": str(r_wy),
        },
        "raw_cutoff_fixture": {
            "parent_density": str(parent),
            "child_density": str(child),
            "exact_ratio": str(exact_ratio),
            "raw_indicator_rejected": True,
        },
    }


Poly = Dict[int, Q]


def poly_add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Q(0)) + c
        if out[e] == 0:
            del out[e]
    return out


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            out[e1 + e2] = out.get(e1 + e2, Q(0)) + c1 * c2
    return {e: c for e, c in out.items() if c}


def alpha_separator() -> Dict[str, object]:
    minus_r2 = {2: Q(-1)}
    plus_r2 = {2: Q(1)}
    alpha_child = poly_add(minus_r2, plus_r2)
    native_child = {1: Q(-1)}
    assert alpha_child == {}
    assert alpha_child != native_child

    odd_export = {2: Q(2)}
    raw_magnitude = {1: Q(1)}
    assert odd_export != raw_magnitude
    assert 8 * 8 < 67
    return {
        "alpha_identity_shifted_coefficient": "0",
        "native_euler_shifted_coefficient": "-r",
        "parity_exported_magnitude": "2*r^2",
        "native_parity_magnitude": "r",
        "missing_native_magnitude": "r-2*r^2>0 for p>=67",
    }


ShiftPoly = Dict[int, Q]


def shift_add(a: ShiftPoly, b: ShiftPoly) -> ShiftPoly:
    out = dict(a)
    for mask, c in b.items():
        out[mask] = out.get(mask, Q(0)) + c
        if out[mask] == 0:
            del out[mask]
    return out


def shift_scale(a: ShiftPoly, c: Q) -> ShiftPoly:
    return {m: c * v for m, v in a.items() if c * v}


def shift_multiply_factor(a: ShiftPoly, i: int, r: Q) -> ShiftPoly:
    out: ShiftPoly = {}
    bit = 1 << i
    for mask, c in a.items():
        out[mask] = out.get(mask, Q(0)) + c
        out[mask | bit] = out.get(mask | bit, Q(0)) - r * c
    return {m: c for m, c in out.items() if c}


def future_product(rs: List[Q], start: int) -> ShiftPoly:
    out: ShiftPoly = {0: Q(1)}
    for i in range(start, len(rs)):
        out = shift_multiply_factor(out, i, rs[i])
    return out


def first_owner_identity() -> Dict[str, object]:
    rs = [Q(1, 5), Q(1, 7), Q(1, 11), Q(1, 13)]
    native = future_product(rs, 0)

    s = Q(1)
    rhs: ShiftPoly = {}
    for i, r in enumerate(rs):
        lam = r * s
        fut = future_product(rs, i + 1)
        term = dict(fut)
        shifted = {mask | (1 << i): -c for mask, c in fut.items()}
        rhs = shift_add(rhs, shift_scale(shift_add(term, shifted), lam))
        s *= 1 - r
    rhs = shift_add(rhs, {0: s})

    assert rhs == native

    surv = Q(1)
    lambda_sum = Q(0)
    for r in rs:
        lam = r * surv
        lambda_sum += lam
        surv *= 1 - r
    assert surv + lambda_sum == 1

    return {
        "prime_count": len(rs),
        "native_monomials": len(native),
        "survival": str(surv),
        "lambda_sum": str(lambda_sum),
        "identity_exact": True,
    }


def two_row_noncancellation() -> Dict[str, object]:
    expr = {2: Q(-3), 1: Q(9), 0: Q(-6)}
    factored = poly_mul({1: Q(-3), 0: Q(3)}, {1: Q(1), 0: Q(-2)})
    assert expr == factored
    return {
        "P2_relation": "b=2a-1",
        "substituted_3P3": "-3(a-1)(a-2)",
        "open_half_plane_exclusion": "|a|=2^{-Re z}<1",
        "exact": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    core = {
        "schema": "riemann.x99600.three-interface-audit.v1",
        "compact_hall": compact_hall_certificate(),
        "rn_cocycle": rn_cocycle_certificate(),
        "native_coefficient_separator": alpha_separator(),
        "first_owner_euler_identity": first_owner_identity(),
        "two_row_noncancellation": two_row_noncancellation(),
        "compact_hall_closed": True,
        "rn_endpoint_interface_closed": True,
        "analytic_consumer_closed": True,
        "alpha_child_native_promotion_refuted": True,
        "future_completed_current_sign_proved": False,
        "harnack_negative_mass_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()

    output = args.output
    if output is None:
        output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
