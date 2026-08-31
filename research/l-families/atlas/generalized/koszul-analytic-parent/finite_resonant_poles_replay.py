"""Uniform source cancellation threshold and the exact fully resonant pole list."""

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
FREEZE = "f977b2e9e962b4ad560ce0edfac6dd97fb395d6b"
PINS = (
    (
        "euler_order_domains_replay.py",
        "48fae9ed9cf8c44d08a7b750a992919351af3a2a",
        "d5de562ccd1c852ae50b087e451749567612cb6d0f8646b5a7520712b5e52493",
    ),
    (
        "S3_WEIGHT_CIRCLE_POLE_DIVISOR.md",
        "381ee262cbd59f671a23f29fa19a9dd6f856463b",
        "0f5f303150da5e1d5dc181617b481ce6ab87003a30613693b8e59692cc04336f",
    ),
)
OWNED = (
    "FINITE_RESONANT_COHERENT_POLES.md",
    "RESONANT_POLES_REPLAY.md",
    "finite_resonant_poles_replay.py",
    "tests/test_finite_resonant_poles.py",
)
FIXTURE = HERE / "finite_resonant_poles.verification.json"


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
        need(actual == blob, "finite resonance dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "finite resonance dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working resonance source changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_exact_pole_divisor", HERE / "euler_order_domains_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None, "authenticated divisor import failed"
)
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)
M, C, R, E = D.M, D.C, D.R, D.E


def mobius(n: int):
    R.integer(n, 1, 128)
    remaining = n
    parity = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            parity += 1
            if remaining % divisor == 0:
                return 0
        divisor += 1
    if remaining > 1:
        parity += 1
    return (-1) ** parity


def source_log_numerator(kind: str, n: int):
    R.integer(n, 1, 128)
    need(kind in ("e", "s", "c"), "actual S3 class required")
    if kind == "e":
        return 4 - (-2) ** n
    if kind == "s":
        return 4 if n % 2 == 0 else 0
    return 3 if n % 3 == 0 else 0


def powered_class(kind: str, k: int):
    need(kind in ("e", "s", "c"), "actual S3 class required")
    R.integer(k, 1, 128)
    if kind == "e" or (kind == "s" and k % 2 == 0) or (kind == "c" and k % 3 == 0):
        return "e"
    return kind


def adams_source_row(n: int):
    R.integer(n, 1, 64)
    characters = []
    for kind in ("e", "s", "c"):
        numerator = sum(
            mobius(k) * source_log_numerator(powered_class(kind, k), n // k)
            for k in range(1, n + 1)
            if n % k == 0
        )
        numerator *= (-1) ** (n + 1)
        need(numerator % n == 0, "actual Adams character is not integral")
        characters.append(numerator // n)
    frozen = M.lie_rows(n)[-1]
    need(
        characters == frozen["class_traces"],
        "direct source Adams formula differs from frozen Lie characters",
    )
    dimension, s, c = characters
    numerators = [
        dimension + 3 * s + 2 * c,
        dimension - 3 * s + 2 * c,
        2 * (dimension - c),
    ]
    need(
        all(value >= 0 and value % 6 == 0 for value in numerators),
        "actual irreducible source multiplicity invalid",
    )
    mult = [value // 6 for value in numerators]
    need(
        mult == frozen["multiplicities"] and 2 * (mult[1] + mult[2]) == dimension - s,
        "source character projection lost the exact elliptic total",
    )
    return {
        "grade": n,
        "actual_characters": characters,
        "multiplicities": mult,
        "exact_twice_B_plus_C": dimension - s,
    }


def uniform_bound_control(n: int):
    R.integer(n, 6, 32)
    need(n % 2 == 0, "even cancellation grade required")
    lower = Fraction(4**n - 12 * 2**n - 40 * n + 12, 12 * n)
    upper = Fraction(2 * (2**n + 2 ** (n // 2 + 1) - 2), n)
    margin = 4**n - 36 * 2**n - 48 * 2 ** (n // 2) - 40 * n + 60
    normalized = (
        Fraction(36) + Fraction(48, 2 ** (n // 2)) + Fraction(40 * n - 60, 2**n)
    )
    next_normalized = (
        Fraction(36)
        + Fraction(48, 2 ** (n // 2 + 1))
        + Fraction(40 * (n + 2) - 60, 2 ** (n + 2))
    )
    need(
        margin > 0 and lower > upper and next_normalized < normalized < 2**n,
        "uniform geometric bound failed its explicit monotonicity control",
    )
    original = adams_source_row(n)
    doubled = adams_source_row(2 * n)
    need(
        doubled["multiplicities"][0] >= lower
        and original["exact_twice_B_plus_C"] <= upper,
        "bounded actual source escaped the proved lower/upper inequalities",
    )
    gap = doubled["multiplicities"][0] - original["exact_twice_B_plus_C"]
    need(gap > 0, "actual doubled-grade source failed strict cancellation")
    return {
        "grade": n,
        "A_double_grade_lower": C.qjson(lower),
        "twice_B_plus_C_upper": C.qjson(upper),
        "sufficient_integer_margin": margin,
        "normalized_sufficient_RHS": C.qjson(normalized),
        "next_even_normalized_RHS": C.qjson(next_normalized),
        "actual_A_double_grade": doubled["multiplicities"][0],
        "actual_twice_B_plus_C": original["exact_twice_B_plus_C"],
        "actual_strict_order_margin": gap,
    }


def low_grade_sign_cases():
    rows = []
    for same_sign in (True, False):
        grade2 = D.even_arithmetic_order(2, 2 if same_sign else 0, 2, True)
        grade4_E = D.even_arithmetic_order(4, 2 if same_sign else 0, 2, True)
        grade4_D = grade4_E if same_sign else D.even_arithmetic_order(4, 2, 0, True)
        need(
            grade2["pole_order"] == 2
            and grade4_E["pole_order"] == grade4_D["pole_order"] == 0,
            "low-grade pole classification missed an elliptic sign case",
        )
        need(
            grade4_E["signed_order"] == (0 if same_sign else 2),
            "equal/opposite elliptic signs have different regularity orders",
        )
        rows.append(
            {
                "elliptic_signs_agree": same_sign,
                "grade_two_E_point": grade2,
                "grade_four_E_point": grade4_E,
                "grade_four_D_point": grade4_D,
            }
        )
    return {
        "actual_low_source_rows": [adams_source_row(n) for n in (2, 4, 8)],
        "sign_cases": rows,
        "total_interior_poles": 2,
        "order_of_each_pole": 2,
        "all_higher_even_grades_covered_by_uniform_proof": True,
    }


def pole_clearing_coefficients(coefficients, alpha: int):
    R.integer(alpha, -100, 100)
    need(
        alpha != 0 and type(coefficients) is list and 1 <= len(coefficients) <= 65,
        "bounded nonzero integral resonant eigenvalue and coefficient list required",
    )
    for value in coefficients:
        need(
            type(value) is int and value.bit_length() <= 2048,
            "bounded integer Euler coefficient required",
        )
    return [
        value
        - 2 * alpha * (coefficients[n - 2] if n >= 2 else 0)
        + alpha * alpha * (coefficients[n - 4] if n >= 4 else 0)
        for n, value in enumerate(coefficients)
    ]


def principal_part_calibration(cut: int = 20):
    R.integer(cut, 4, 32)
    reciprocal = 5
    c_plus, c_minus, d_plus, d_minus = 2, 2, 3, -3
    coefficients = [
        (c_plus * (n + 1) + d_plus) * reciprocal**n
        + (c_minus * (n + 1) + d_minus) * (-reciprocal) ** n
        for n in range(cut + 1)
    ]
    factors = [
        ([1, -reciprocal], -2, c_plus),
        ([1, reciprocal], -2, c_minus),
        ([1, -reciprocal], -1, d_plus),
        ([1, reciprocal], -1, d_minus),
    ]
    by_rational = [0] * (cut + 1)
    for factor, exponent, weight in factors:
        series = E.integer_power(factor, exponent, cut)
        by_rational = [a + weight * b for a, b in zip(by_rational, series)]
    need(
        coefficients == by_rational,
        "two-double-principal-part formula does not match exact rational expansion",
    )
    for n, value in enumerate(coefficients):
        need(
            value == (4 * (n + 1) * reciprocal**n if n % 2 == 0 else 6 * reciprocal**n),
            "opposite-pole calibration did not retain parity cancellation",
        )
    cleared = pole_clearing_coefficients(coefficients, reciprocal**2)
    need(
        cleared == [4, 30, 100, -750] + [0] * (cut - 3),
        "minimal degree-four factor did not clear the exact principal part",
    )
    with_integer_tail = [value + 1 for value in coefficients]
    modified = pole_clearing_coefficients(with_integer_tail, reciprocal**2)
    need(
        all(value == (1 - reciprocal**2) ** 2 for value in modified[4:]),
        "new integral modified sequence was confused with the original exponential part",
    )
    return {
        "calibration_not_actual_source_residues": True,
        "reciprocal_poles": [reciprocal, -reciprocal],
        "C_plus_C_minus_D_plus_D_minus": [c_plus, c_minus, d_plus, d_minus],
        "principal_coefficients": coefficients,
        "cleared_principal_polynomial": cleared[:4],
        "integer_tail_added_coefficients": with_integer_tail,
        "new_pole_cleared_integer_coefficients": modified,
        "calibration_tail_is_not_claimed_to_have_a_full_natural_boundary": True,
        "source_complex_residues_not_computed": True,
    }


def actual_clearing_factor():
    previous = D.square_field_source_control()
    pe = previous["Frobenius_square_polynomials_E_D"][0]
    factor = M.substituted(pe, 2, 4)
    need(
        factor == [1, 0, 14, 0, 49],
        "actual F49 elliptic pole-clearing factor lost its source sign",
    )
    return {
        "inherited_source_parameters": previous["source_parameters_p_A_B"],
        "source_Q": 49,
        "actual_alpha_E": -7,
        "minimal_normalized_pole_clearing_polynomial": factor,
        "recurrence_lags_zero_two_four": [1, 14, 49],
        "primitive_field_order_reused": 7,
        "new_field_enumerated": False,
        "modified_function_distinct_from_original": True,
    }


def build_payload():
    authenticate_frozen()
    return {
        "schema": "finite-fully-resonant-coherent-poles-v1",
        "provenance": {
            "source_freeze": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "direct_source_Adams_controls": [adams_source_row(n) for n in range(1, 25)],
        "uniform_bound_controls": [
            uniform_bound_control(n) for n in (6, 8, 10, 12, 16, 24, 32)
        ],
        "low_grade_complete_sign_cases": low_grade_sign_cases(),
        "principal_part_and_integer_recurrence_calibration": principal_part_calibration(),
        "actual_cohomological_pole_clearing_factor": actual_clearing_factor(),
        "not_claimed": [
            "finite grade checks prove the infinite threshold",
            "actual source residues are algebraic",
            "the principal-part residual has integer coefficients",
            "the new pole-cleared function equals the old Euler source",
            "the original quarter-power coefficient growth improved",
            "all new local tensor-algebra ramification follows from multiplying determinants",
        ],
    }


def check_payload(candidate: object):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "resonant pole fixture differs from the authenticated exact source replay",
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
            "resonant pole fixture mismatch",
        )
    print(
        "PASS uniform fully resonant source threshold, exact poles and new integer recurrence"
    )


if __name__ == "__main__":
    main()
