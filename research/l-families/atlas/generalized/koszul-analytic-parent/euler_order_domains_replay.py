"""Euler degree order, exact source domains, and square-field pole cancellation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE = "5104c38614461a3e080c93631b855094d0e5961a"
PINS = (
    (
        "coherent_place_euler_replay.py",
        "c802d60a3aa6da49fae47ac462c587e6f9b98c74",
        "965b3329e8f33a53fa4979286addd091c44b59b26a2623a4038040c20d32a7f7",
    ),
    (
        "COHERENT_QUADRATIC_PLACE_EULER.md",
        "2b5b7ef94b0c4c6326a0e06221d01d23475ec58e",
        "08e8bf391afb9d4d5a63d23206a5755cabfec755790e7709c3ceedb67b26d99d",
    ),
)
OWNED = (
    "EULER_ORDER_AND_FOUR_DOMAINS.md",
    "S3_WEIGHT_CIRCLE_POLE_DIVISOR.md",
    "EULER_ORDER_DOMAINS_REPLAY.md",
    "euler_order_domains_replay.py",
    "tests/test_euler_order_domains.py",
)
FIXTURE = HERE / "euler_order_domains.verification.json"


def need(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def digest(data: bytes):
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen():
    for name, blob, expected in PINS:
        actual = subprocess.check_output(
            ["git", "rev-parse", FREEZE + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(actual == blob, "Euler-order dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "Euler-order dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working Euler-order source changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_coherent_euler_domains", HERE / "coherent_place_euler_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "authenticated coherent source import failed",
)
A = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(A)
E, M, C, R = A.E, A.M, A.C, A.R


def prime_character(p: int, value: int):
    R.integer(p, 5, 7)
    need(p in (5, 7), "bounded source prime required")
    R.integer(value, -(10**8), 10**8)
    if value % p == 0:
        return 0
    residue = pow(value % p, (p - 1) // 2, p)
    need(residue in (1, p - 1), "prime quadratic character failed")
    return 1 if residue == 1 else -1


def branch_inventory(index: int):
    source = A.native_source(index)
    p, a, b = source["parameters"]
    counts = []
    for row in source["primitive_rows"]:
        pair = {-1: 0, 1: 0}
        for item in row["finite_fibre_histogram"]:
            if A.fibre_kind(item) == "C2":
                need(item["chi_u"] in (-1, 1), "old branch met new zero ramification")
                pair[item["chi_u"]] += item["number"]
        counts.append(pair)
    first, second = counts
    total_first = sum(first.values())
    need(
        (second[1] - total_first) % 2 == 0 and second[-1] % 2 == 0,
        "degree-two branch signs forgot Frobenius squaring",
    )
    pairs = [(1, chi, first[chi]) for chi in (-1, 1)]
    pairs.extend(((2, 1, (second[1] - total_first) // 2), (2, -1, second[-1] // 2)))
    old_inventory = dict(E.closed_place_data(index)["finite_branch_orbits"])
    degree_four = old_inventory[4]
    norm = (4 * a**3 + 27 * b * b) * pow(27, -1, p) % p
    need(norm != 0, "smooth source has zero branch-root norm")
    norm_sign = prime_character(p, norm)
    pairs.append((4, norm_sign, degree_four))
    need(
        all(count >= 0 for _, _, count in pairs)
        and sum(degree * count for degree, _, count in pairs) == 4,
        "signed branch inventory does not have full degree four",
    )
    for degree in (1, 2, 4):
        need(
            sum(count for d, _, count in pairs if d == degree) == old_inventory[degree],
            "signed and unsigned old branch inventories disagree",
        )
    return {
        "parameters": source["parameters"],
        "closed_branch_rows": [
            {"degree": degree, "chi": chi, "count": count}
            for degree, chi, count in pairs
            if count
        ],
        "quartic_root_norm_in_base_field": norm,
        "quartic_orbit_chi": norm_sign,
        "degree_four_field_enumerated": False,
        "rational_branch_chi_counts": [first[-1], first[1]],
        "extension_two_branch_chi_counts": [second[-1], second[1]],
    }


def local_sums_from_polynomial(poly, cut: int):
    R.integer(cut, 1, 32)
    need(
        type(poly) is list and 1 <= len(poly) <= 33 and poly[0] == 1,
        "bounded normalized polynomial required",
    )
    for coefficient in poly:
        need(
            type(coefficient) is int and coefficient.bit_length() <= 1024,
            "bounded exact polynomial coefficient required",
        )
    traces = [0]
    for n in range(1, cut + 1):
        value = -n * (poly[n] if n < len(poly) else 0)
        value -= sum(poly[j] * traces[n - j] for j in range(1, min(n, len(poly))))
        traces.append(value)
    return [-value for value in traces[1:]]


def compact_first_source(index: int, cut: int = 24):
    R.integer(cut, 2, 32)
    source = A.native_source(index)
    inventory = branch_inventory(index)
    anti = A.first_four_factor_control(index)["anti_regular_degree_twelve_polynomial"]
    boundary = [1] + [0] * 12
    for row in inventory["closed_branch_rows"]:
        factor = [1] + [0] * (row["degree"] - 1) + [-row["chi"]]
        boundary = M.multiply(
            boundary, E.integer_power(factor, 3 * row["count"], 12), 12
        )
    compact = M.multiply(anti, boundary, 24)
    need(
        len(compact) == 25 and compact[-1] != 0,
        "actual compact first-grade rank is not 24",
    )
    sums = local_sums_from_polynomial(compact, cut)
    primitive = []
    rational_second = 0
    for j, row in enumerate(source["primitive_rows"]):
        total = 0
        for item in row["finite_fibre_histogram"]:
            kind = A.fibre_kind(item)
            if kind == "C2" or item["chi_u"] == 0:
                continue
            if kind == "e":
                total += 6 * item["chi_u"] * item["number"]
            if j == 0 and kind in ("e", "s"):
                rational_second += 6 * item["number"]
        primitive.append(total)
    need(
        sums[:2] == primitive,
        "complete compact source polynomial disagrees with actual good-fibre traces",
    )
    need(
        (primitive[1] - rational_second) % 2 == 0,
        "closed degree-two regular trace is not integral",
    )
    degrees = [primitive[0], (primitive[1] - rational_second) // 2]
    q = source["parameters"][0]
    need(
        all(
            max(0, abs(value) - 12) ** 2 <= 144 * q**n
            for n, value in enumerate(sums, 1)
        ),
        "compact trace exceeded actual twelve Weil and twelve boundary eigenvalue bound",
    )
    need(
        all(
            (n * abs(value)) ** 2 <= 32**2 * q**n for n, value in enumerate(degrees, 1)
        ),
        "small source degree traces violate proved degree bound",
    )
    zeros = M.multiply(anti, [1, 0, -q], 14)
    need(
        len(zeros) == 15 and zeros[-1] == -(q**7),
        "first good-zero polynomial must retain fourteen roots with multiplicity",
    )
    return {
        "parameters": source["parameters"],
        "signed_branch_inventory": inventory,
        "actual_boundary_polynomial": boundary,
        "compact_first_grade_polynomial": compact,
        "compact_h0_h1_h2": [0, 24, 0],
        "weight_one_and_boundary_ranks": [12, 12],
        "compact_trace_sums": sums,
        "new_primitive_good_traces": primitive,
        "rational_good_second_power_trace": rational_second,
        "closed_degree_one_two_linear_traces": degrees,
        "first_good_zero_polynomial": zeros,
        "first_good_zero_polynomial_is_not_a_new_curve_numerator": True,
        "maximum_new_primitive_field_order": max(
            row["field_order"] for row in source["primitive_rows"]
        ),
    }


def local_log_coefficient(kind: str, epsilon: int, n: int):
    need(
        kind in ("e", "s", "c") and type(epsilon) is int and epsilon in (-1, 1),
        "actual good joint source required",
    )
    R.integer(n, 1, 64)
    if kind == "e":
        return Fraction(((-1) ** (n + 1) * 2**n + 4) * epsilon**n, n)
    if kind == "s":
        return Fraction(4, n) if n % 2 == 0 else Fraction(0)
    return Fraction(3 * epsilon**n, n) if n % 3 == 0 else Fraction(0)


def degree_tail_control(
    q: int,
    r: Fraction = Fraction(1, 4),
    growth_upper: Fraction = Fraction(3, 4),
    cut: int = 24,
):
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded source prime required")
    r, growth_upper = C.exact(r), C.exact(growth_upper)
    R.integer(cut, 2, 32)
    need(0 < r < Fraction(1, 2) and q * r * r < 1, "strict good-log disk required")
    need(
        0 < growth_upper < 1 and growth_upper**2 >= q * r * r,
        "rational growth bound must dominate sqrt(Q)r",
    )
    constant = 2 / (1 - 2 * r) + 2 / (1 - r)
    linear = 32 * growth_upper ** (cut + 1) / ((cut + 1) * (1 - growth_upper))
    nonlinear = constant * (q * r * r) ** (cut + 1) / ((cut + 1) * (1 - q * r * r))
    controls = []
    tail = ((2 * r) ** (cut + 1) / (1 - 2 * r) + 4 * r ** (cut + 1) / (1 - r)) / (
        cut + 1
    )
    for kind in ("e", "s", "c"):
        for epsilon in (-1, 1):
            finite = sum(
                (
                    abs(local_log_coefficient(kind, epsilon, n)) * r**n
                    for n in range(2, cut + 1)
                ),
                Fraction(0),
            )
            need(
                finite + tail <= constant * r * r,
                "source local logarithms violate proved nonlinear bound",
            )
            controls.append(
                {
                    "class": kind,
                    "chi": epsilon,
                    "finite_absolute_nonlinear_sum": C.qjson(finite),
                    "proved_local_omitted_tail": C.qjson(tail),
                }
            )
    return {
        "Q": q,
        "radius": C.qjson(r),
        "sqrt_Q_times_radius_upper": C.qjson(growth_upper),
        "degree_cut": cut,
        "outside_absolute_Euler_disk": q * r > 1,
        "nonlinear_constant": C.qjson(constant),
        "linear_degree_tail_bound": C.qjson(linear),
        "nonlinear_degree_tail_bound": C.qjson(nonlinear),
        "complete_degree_tail_bound": C.qjson(linear + nonlinear),
        "actual_local_log_controls": controls,
    }


def local_root_and_split_controls():
    small = Fraction(1, 32)
    fe = (1 + 2 * small) / (1 - small) ** 4
    remainder = fe - 1 - 6 * small
    need(
        0 < remainder < 3 * small, "split-source absolute-divergence lower bound failed"
    )
    lo, hi = Fraction(1, 16), Fraction(1, 9)
    value = lambda x: 1 - 14 * x + 9 * x * x
    need(value(lo) > 0 and value(hi) < 0, "exact bad even-root enclosure failed")
    return {
        "split_small_argument_cap": C.qjson(small),
        "split_linear_term": C.qjson(6 * small),
        "split_absolute_higher_coefficient_bound": C.qjson(remainder),
        "split_factor_difference_lower_multiplier": 3,
        "bad_even_root_absolute_square_interval": [C.qjson(lo), C.qjson(hi)],
        "bad_even_zero_modulus_interval": [[1, 4], [1, 3]],
        "new_parameter_or_field_for_bad_root_control": False,
        "finite_bad_factor_not_in_good_log": True,
    }


def even_arithmetic_order(n: int, m_D: int, m_E: int, resonant: bool):
    R.integer(n, 2, 16)
    need(n % 2 == 0, "even arithmetic H1 grade required")
    R.integer(m_D, 0, 2)
    R.integer(m_E, 0, 2)
    need(
        type(resonant) is bool and m_D + m_E > 0,
        "exact resonance flag and an actual eigenvalue required",
    )
    rows = M.lie_rows(2 * n)
    a2 = rows[2 * n - 1]["multiplicities"][0]
    _, b, std = rows[n - 1]["multiplicities"]
    denominator = b * m_D + std * m_E
    correction = a2 if resonant else 0
    signed = correction - denominator
    return {
        "grade": n,
        "elliptic_denominator_order": denominator,
        "double_grade_trivial_multiplicity": a2,
        "resonance_zero_correction": correction,
        "signed_order": signed,
        "pole_order": max(0, -signed),
        "zero_order": max(0, signed),
    }


def reciprocal_norm_table():
    rows = [
        ("good_plus", [2, 1]),
        ("good_minus", [-2, 1]),
        ("old_C2", [1, 3, 1, 1]),
        ("old_C3", [3, -1, 1]),
        ("new_zero_even", [9, 14, 1]),
        ("new_infinity_even", [3, 7, 10, 3, 1]),
    ]
    out = []
    for kind, poly in rows:
        value = abs(poly[0])
        for prime in (2, 3):
            while value % prime == 0:
                value //= prime
        need(
            poly[-1] == 1 and value == 1,
            "reciprocal norm table has an unexpected constant prime divisor",
        )
        out.append({"source": kind, "monic_reciprocal_polynomial": poly})
    return out


def square_field_source_control():
    p = 7
    need((-4) % p != 0, "the seven-point source is not generic smooth S3")
    elliptic = [1 + prime_character(p, x**3 + x) for x in range(p)]
    discriminant = [1 + prime_character(p, u**4 + 3) for u in range(p)]
    e_count = sum(elliptic) + 1
    d_count = sum(discriminant) + 2
    need(
        (e_count, d_count) == (8, 8),
        "actual seven-point elliptic source counts changed",
    )
    trace = p + 1 - e_count
    trace_d = p + 1 - d_count
    pe2 = [1, -(trace * trace - 2 * p), p * p]
    pd2 = [1, -(trace_d * trace_d - 2 * p), p * p]
    need(pe2 == pd2 == [1, 14, 49], "source Frobenius square is not (1+7T)^2")
    grade2 = even_arithmetic_order(2, 2, 2, True)
    grade4 = even_arithmetic_order(4, 2, 2, True)
    need(
        grade2["pole_order"] == 2 and grade4["signed_order"] == 0,
        "actual square-field cancellation did not distinguish grades two and four",
    )
    multiplicities = [M.lie_rows(n)[-1]["multiplicities"] for n in (4, 8)]
    need(
        multiplicities == [[0, 1, 1], [4, 6, 10]],
        "actual grade-eight trivial source was replaced by a scalar estimate",
    )
    numerator = E.integer_power([1, 0, -49], 4, 8)
    denominator = E.integer_power([1, 7], 4, 8)
    remaining = E.integer_power([1, -7], 4, 8)
    need(
        numerator == M.multiply(denominator, remaining, 8),
        "exact resonant finite factors did not cancel",
    )
    return {
        "primitive_field_order": 7,
        "source_parameters_p_A_B": [7, 1, 0],
        "elliptic_finite_fibre_counts": elliptic,
        "discriminant_finite_fibre_counts": discriminant,
        "infinity_counts_E_D": [1, 2],
        "proper_point_counts_E_D": [e_count, d_count],
        "base_field_polynomials_E_D": [[1, 0, 7], [1, 0, 7]],
        "Frobenius_square_polynomials_E_D": [pe2, pd2],
        "field_49_enumerated": False,
        "source_multiplicities_grades_four_eight": multiplicities,
        "grade_two_order": grade2,
        "grade_four_order": grade4,
        "nonsquare_trace_zero_is_not_resonance": even_arithmetic_order(4, 1, 1, False),
        "cancelled_factor_in_w_equals_z_four": denominator,
        "remaining_factor_in_w_equals_z_four": remaining,
    }


def build_payload():
    authenticate_frozen()
    return {
        "schema": "source-Euler-order-domains-and-pole-divisor-v1",
        "provenance": {
            "source_freeze": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "actual_compact_first_sources": [
            compact_first_source(index) for index in range(3)
        ],
        "certified_grouped_degree_tails": [degree_tail_control(q) for q in (5, 7)],
        "heldout_interior_radius_control": degree_tail_control(
            7, Fraction(1, 3), Fraction(9, 10), 24
        ),
        "split_and_bad_root_controls": local_root_and_split_controls(),
        "reciprocal_norm_table": reciprocal_norm_table(),
        "actual_square_field_resonance": square_field_source_control(),
        "maximum_existing_panel_primitive_field_order": 49,
        "new_resonance_primitive_field_order": 7,
        "not_claimed": [
            "individual absolute Euler factors converge on the good grouped-log disk",
            "full bad-attached source is zero-free on the good-log disk",
            "the good-log series diverges at every exterior point",
            "a denominator-only list gives the full pole divisor over square fields",
            "the fourteen good zeros form a new genus-seven curve numerator",
            "new RH theorem",
        ],
    }


def check_payload(candidate: object):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "Euler-order fixture differs from exact authenticated source replay",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(
            json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")), sort_keys=True)
            == json.dumps(payload, sort_keys=True),
            "Euler-order fixture mismatch",
        )
    print(
        "PASS actual Euler degree order, four domains and square-field pole correction"
    )


if __name__ == "__main__":
    main()
