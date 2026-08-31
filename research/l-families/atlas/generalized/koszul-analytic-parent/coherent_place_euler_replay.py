"""Actual quadratic coherent place Euler source and surviving elliptic poles."""

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
PINS = (
    (
        "65204d3f6e43b737e36c40b090685cbd068e34e6",
        "segre_place_euler_replay.py",
        "641f12201e7c4fad84119ccb745a6e5ce7173438",
        "048d403416c96de115ced8f6b0eb28faaae12b4c58163a54ec3e6f857d92a0d0",
    ),
    (
        "65204d3f6e43b737e36c40b090685cbd068e34e6",
        "S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md",
        "0f3e295b523f93f364c89db771864ea325af2b63",
        "239903a00da7b669868ba73a3401ecb04f15f7e1147e16321826eb95b26529e2",
    ),
    (
        "efdff67938b4ce8769a3cbaadec359898fec1654",
        "twisted_global_replay.py",
        "974bda6503b75211276ebf187d7bdc60dfae36b6",
        "e80d649b6d3698eb8ae6a179ee86bd84b5ae2199d5ae30f0a7a8acbc908d4bb8",
    ),
    (
        "efdff67938b4ce8769a3cbaadec359898fec1654",
        "RAMIFIED_TWISTED_GLOBAL_COMPLETION.md",
        "e54a39f39833f446fec68840f28b7466fe52aa67",
        "abf3769d0ed574a0dbfac51a1cd83d882b2a661f25c3a92a0f86f3a6fa3216ff",
    ),
)
OWNED = (
    "COHERENT_QUADRATIC_PLACE_EULER.md",
    "COHERENT_PLACE_EULER_REPLAY.md",
    "coherent_place_euler_replay.py",
    "tests/test_coherent_place_euler.py",
)
FIXTURE = HERE / "coherent_place_euler.verification.json"


def need(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def digest(data: bytes):
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen():
    for freeze, name, blob, expected in PINS:
        actual = subprocess.check_output(
            ["git", "rev-parse", freeze + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(actual == blob, "coherent place Euler dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(
            digest(frozen) == expected, "coherent place Euler dependency hash mismatch"
        )
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working coherent place Euler source changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_source_place_euler", HERE / "segre_place_euler_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "authenticated place Euler import failed",
)
E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E)
TWIST_SPEC = importlib.util.spec_from_file_location(
    "frozen_joint_s3_quadratic_source", HERE / "twisted_global_replay.py"
)
need(
    TWIST_SPEC is not None and TWIST_SPEC.loader is not None,
    "authenticated quadratic import failed",
)
T = importlib.util.module_from_spec(TWIST_SPEC)
TWIST_SPEC.loader.exec_module(T)
M, C, R = E.M, E.C, E.R
KINDS = {(3, 1): "e", (1, -1): "s", (0, 1): "c", (2, 0): "C2"}


def native_source(index: int):
    R.integer(index, 0, 2)
    old = M.native_source(index)
    p, A, B = old["parameters_p_A_B"]
    rows = [T.count_twisted(p, A, B, degree) for degree in (1, 2)]
    for before, after in zip(old["primitive_rows"], rows):
        need(
            all(before["counts"][name] == after["counts"][name] for name in ("E", "Z")),
            "joint source changed the already authenticated original curves",
        )
    polynomials = {
        name: T.quartic_from_counts(p, [row["local_sums_Dchi_Prym"][j] for row in rows])
        for j, name in enumerate(("Dchi", "Prym"))
    }
    return {
        "parameters": old["parameters_p_A_B"],
        "old": old,
        "primitive_rows": rows,
        "twisted_polynomials": polynomials,
        "new_primitive_field_cap": 49,
        "quartic_reconstruction": "actual rank-four source, first two primitive traces and proved reciprocal duality; historical degree-three holdout belongs to the frozen source",
    }


def signed_series(poly, epsilon: int):
    need(type(epsilon) is int and epsilon in (-1, 1), "actual quadratic sign required")
    return [coefficient * epsilon**n for n, coefficient in enumerate(poly)]


def even_series(poly):
    return [coefficient if n % 2 == 0 else 0 for n, coefficient in enumerate(poly)]


def fibre_kind(item):
    key = item["distinct_roots"], item["sign_trace"]
    need(key in KINDS, "unknown actual S3 fibre")
    return KINDS[key]


def zero_kind(source):
    zeros = [
        item
        for item in source["primitive_rows"][0]["finite_fibre_histogram"]
        if item["chi_u"] == 0
    ]
    need(
        len(zeros) == 1 and zeros[0]["number"] == 1,
        "the unique quadratic branch point at zero was lost",
    )
    kind = fibre_kind(zeros[0])
    need(kind in ("e", "s", "c"), "old cubic source must be unramified at zero")
    return kind


def closed_coefficient_control(index: int):
    source = native_source(index)
    old_data = E.closed_place_data(index)
    rows = source["primitive_rows"]
    out = [1, 0, 0]
    rational_second_trace = 0
    coherent_grade_two_sum = 0
    fixed_grade_two_sum = 0
    for item in rows[0]["finite_fibre_histogram"]:
        kind = fibre_kind(item)
        base = M.segre_series(kind, 2)
        chi = item["chi_u"]
        factor = even_series(base) if chi == 0 else signed_series(base, chi)
        out = M.multiply(out, E.integer_power(factor, item["number"], 2), 2)
        coherent_grade_two_sum += item["number"] * base[2]
        fixed_grade_two_sum += item["number"] * chi * base[2]
        if chi != 0:
            rational_second_trace += (
                item["number"] * ({"e": 6, "s": 6, "c": 0, "C2": 3}[kind])
            )
    infinity = even_series(M.segre_series(old_data["infinity_kind"], 2))
    out = M.multiply(out, infinity, 2)
    coherent_grade_two_sum += infinity[2]
    delta1, delta2 = [row["Delta"] for row in rows]
    numerator = delta2 - rational_second_trace
    need(numerator % 2 == 0, "actual quadratic closed-degree-two trace is not integral")
    closed_two = numerator // 2
    out = M.multiply(out, [1, 0, closed_two], 2)
    need(
        out[1] == delta1,
        "coherent first coefficient is not the actual anti-regular trace",
    )

    anti = [1, 0, 0]
    for name, exponent in (("Dchi", 1), ("Prym", 2)):
        anti = M.multiply(
            anti, E.integer_power(source["twisted_polynomials"][name], exponent, 2), 2
        )
    q = source["parameters"][0]
    pe = source["old"]["polynomials"]["E"]
    lie = M.multiply(anti, [1, 0, -1 - q], 2)
    lie = E.divide(lie, M.substituted(pe, 2, 2), 2)
    expected_lie2 = (
        Fraction(delta1 * delta1 + delta2, 2)
        - source["old"]["primitive_rows"][0]["counts"]["E"]
    )
    need(
        lie[2] == expected_lie2,
        "actual quartic factors and independent anti-trace formula disagree",
    )
    b1 = dict(old_data["finite_branch_orbits"])[1]
    kind0 = zero_kind(source)
    zero_correction = {"e": 21, "s": 3, "c": 0}[kind0]
    infinity_correction = 7 if q % 3 == 1 else 3
    correction = 6 * b1 + zero_correction + infinity_correction
    need(
        out == M.multiply(lie, [1, 0, correction], 2),
        "full coherent place source differs from actual corrected Lie cohomology",
    )
    untwisted = E.place_euler_series(index)
    need(
        all(abs(a) <= b for a, b in zip(out, untwisted)),
        "source coefficient majorization failed",
    )
    return {
        "parameters": source["parameters"],
        "coherent_place_coefficients": out,
        "finite_twisted_Lie_coefficients": lie,
        "untwisted_place_coefficients": untwisted,
        "actual_anti_regular_trace": delta1,
        "extension_two_anti_trace": delta2,
        "rational_point_second_power_trace": rational_second_trace,
        "closed_degree_two_first_grade_trace": closed_two,
        "zero_Frobenius_kind": kind0,
        "zero_correction": zero_correction,
        "finite_old_branch_correction": 6 * b1,
        "infinity_correction": infinity_correction,
        "total_actual_bad_correction": correction,
        "rational_grade_two_coherent_and_fixed_module_traces": [
            coherent_grade_two_sum,
            fixed_grade_two_sum,
        ],
        "primitive_field_orders": [row["field_order"] for row in rows],
    }


def new_bad_source_control():
    cut = 12
    numerator = {
        "zero_e": [1, 0, 14, 0, 9],
        "zero_s": [1],
        "zero_c": [1],
        "infinity_C3": [1, 0, 3, 0, 10, 0, 7, 0, 3],
        "infinity_C3s": [1],
    }
    denominator = {
        "zero_e": E.integer_power([1, 0, -1], 4, cut),
        "zero_s": E.integer_power([1, 0, -1], 2, cut),
        "zero_c": [1, 0, 0, 0, 0, 0, -1],
        "infinity_C3": M.multiply(
            E.integer_power([1, 0, -1], 4, cut), [1, 0, 1, 0, 1], cut
        ),
        "infinity_C3s": E.integer_power([1, 0, -1], 2, cut),
    }
    sources = {
        "zero_e": "e",
        "zero_s": "s",
        "zero_c": "c",
        "infinity_C3": "C3",
        "infinity_C3s": "C3s",
    }
    rows = []
    for label, kind in sources.items():
        actual = even_series(M.segre_series(kind, cut))
        product = M.multiply(actual, denominator[label], cut)
        need(
            product == numerator[label] + [0] * (cut + 1 - len(numerator[label])),
            "new full-inertia even source does not have the claimed numerator",
        )
        rows.append(
            {
                "source": label,
                "numerator": numerator[label],
                "denominator": denominator[label],
                "actual_source_prefix": actual,
                "new_grade_one_stalk_trace": actual[1],
            }
        )
    reciprocal = [[9, 14, 1], [3, 7, 10, 3, 1]]
    need(
        all(poly[-1] == 1 and poly[0] in (3, 9) for poly in reciprocal),
        "monic reciprocal norm obstruction lost its prime-three constant",
    )
    return {
        "local_sources": rows,
        "reciprocal_integer_polynomials_in_Weil_power": reciprocal,
        "norm_obstruction_prime": 3,
        "requires_characteristic_greater_than_three": True,
        "not_the_naive_invariant_input_algebra": True,
    }


def extraction_control(grade_cut: int, epsilon: int):
    R.integer(grade_cut, 1, 6)
    need(
        type(epsilon) is int and epsilon in (-1, 1), "actual joint-source sign required"
    )
    cut = grade_cut + 2
    rows = []
    for kind in ("e", "s", "c"):
        parent = signed_series(E.source_parent_prefix(kind, grade_cut, cut), epsilon)
        actual = signed_series(M.segre_series(kind, cut), epsilon)
        residual = E.divide(actual, parent, cut)
        need(
            residual[: grade_cut + 1] == [1] + [0] * grade_cut,
            "coherent chi^n source failed integral finite Koszul extraction",
        )
        rows.append(
            {
                "class": kind,
                "quadratic_sign": epsilon,
                "actual_parent_prefix": parent,
                "actual_remainder": residual,
            }
        )
    return {"grade_cut": grade_cut, "source_classes": rows}


def first_four_factor_control(index: int):
    source = native_source(index)
    old = source["old"]
    q = source["parameters"][0]
    rows = E.first_four_s3_sources()
    cut = 20
    actual = [1] + [0] * cut
    cohomology = []
    for row in rows:
        n = row["grade"]
        a, b, std = row["multiplicities"]
        if n % 2:
            factors = (
                (source["twisted_polynomials"]["Dchi"], b),
                (source["twisted_polynomials"]["Prym"], std),
            )
            ranks = [0, 4 * b + 4 * std, 0]
        else:
            factors = (
                ([1, -1], a),
                ([1, -q], a),
                (old["polynomials"]["D"], -b),
                (old["polynomials"]["E"], -std),
            )
            ranks = [a, 2 * b + 2 * std, a]
        for polynomial, exponent in factors:
            actual = M.multiply(
                actual,
                E.integer_power(M.substituted(polynomial, n, cut), exponent, cut),
                cut,
            )
        cohomology.append(
            {
                "grade": n,
                "quadratic_twist_present": bool(n % 2),
                "proper_h0_h1_h2": ranks,
            }
        )
    explicit = [1] + [0] * cut
    pe, pd = old["polynomials"]["E"], old["polynomials"]["D"]
    factors = (
        (source["twisted_polynomials"]["Dchi"], 1, 1),
        (source["twisted_polynomials"]["Prym"], 1, 2),
        ([1, -1], 2, 1),
        ([1, -q], 2, 1),
        (pe, 2, -1),
        (source["twisted_polynomials"]["Prym"], 3, 1),
        (pd, 4, -1),
        (pe, 4, -1),
    )
    for polynomial, n, exponent in factors:
        explicit = M.multiply(
            explicit,
            E.integer_power(M.substituted(polynomial, n, cut), exponent, cut),
            cut,
        )
    need(
        actual == explicit,
        "coherent actual four-grade source differs from explicit factorization",
    )
    anti = M.multiply(
        source["twisted_polynomials"]["Dchi"],
        E.integer_power(source["twisted_polynomials"]["Prym"], 2, 8),
        12,
    )
    need(
        len(anti) == 13 and anti[0] == 1 and anti[-1] == q**6,
        "anti-regular degree-twelve source determinant lost purity or rank",
    )
    pole = M.substituted(pe, 2, 4)
    need(
        cohomology[0]["proper_h0_h1_h2"] == [0, 12, 0]
        and cohomology[3]["proper_h0_h1_h2"][2] == 0,
        "coherent first pole removal or grade-four absence of H2 failed",
    )
    return {
        "parameters": source["parameters"],
        "actual_cohomology_by_grade": cohomology,
        "anti_regular_degree_twelve_polynomial": anti,
        "twisted_standard_polynomial": list(source["twisted_polynomials"]["Prym"]),
        "exact_first_pole_polynomial": pole,
        "four_grade_source_product_through_degree": cut,
        "four_grade_coefficients": actual,
        "same_elliptic_denominator_as_untwisted": pole
        == E.subleading_pole_control(index)["exact_first_subleading_pole_polynomial"],
        "first_grade_main_Q_pole_absent_from_actual_source": True,
    }


def build_payload():
    authenticate_frozen()
    return {
        "schema": "coherent-quadratic-place-Euler-v1",
        "provenance": {
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "closed_place_and_ramification_controls": [
            closed_coefficient_control(index) for index in range(3)
        ],
        "new_even_inertia_sources": new_bad_source_control(),
        "coherent_finite_extraction": [
            extraction_control(n, epsilon)
            for n in (1, 2, 3, 4, 6)
            for epsilon in (-1, 1)
        ],
        "actual_first_four_cohomological_factors": [
            first_four_factor_control(index) for index in range(3)
        ],
        "maximum_new_primitive_field_order": 49,
        "not_claimed": [
            "fixed chi module equals coherent graded algebra",
            "chi is constant on extension-field points",
            "ordinary infinite Lie operator has enlarged ideal domain",
            "finite coefficients prove sharp limsup",
            "new RH theorem",
            "a coefficientwise majorant alone proves quarter-power cancellation",
        ],
    }


def check_payload(candidate: object):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "coherent place Euler fixture differs from authenticated source replay",
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
            "coherent place Euler fixture mismatch",
        )
    print("PASS actual coherent quadratic place Euler source and elliptic pole scale")


if __name__ == "__main__":
    main()
