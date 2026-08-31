"""An actual constructible graded algebra for the elliptic clearing factor."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE = "e196fa1e4265b482ad1fa495436ed0e4ff088419"
PINS = (
    (
        "finite_resonant_poles_replay.py",
        "aa3a3d92c7123200de683e963dffa7766b8f251b",
        "9b10306e55d4376ecce752a76fc6cde2104075412ab64dc9f43ac6c5d63fb1ba",
    ),
    (
        "FINITE_RESONANT_COHERENT_POLES.md",
        "c415abc8a9b363a1cef6e0cd52adca16a4f6c754",
        "e505816f1e38adab31b24aa5272f07a3e879d9649b12eb43b3721c040973d79b",
    ),
)
OWNED = (
    "CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md",
    "CONSTRUCTIBLE_POLE_CLEARING_REPLAY.md",
    "constructible_pole_clearing_replay.py",
    "tests/test_constructible_pole_clearing.py",
)
FIXTURE = HERE / "constructible_pole_clearing.verification.json"


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
        need(actual == blob, "constructible source dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(
            digest(frozen) == expected, "constructible source dependency hash mismatch"
        )
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working constructible dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_resonant_source", HERE / "finite_resonant_poles_replay.py"
)
need(SPEC is not None and SPEC.loader is not None, "authenticated source import failed")
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)
D, M, C, R, E = F.D, F.M, F.C, F.R, F.E
A = D.A


def standard_determinant(kind: str):
    need(kind in ("e", "s", "c", "C2", "C3"), "actual standard stalk required")
    return {"e": [1, -2, 1], "s": [1, 0, -1], "c": [1, 1, 1], "C2": [1, -1], "C3": [1]}[
        kind
    ]


def local_source(place: str, kind: str, epsilon: int = 1, cut: int = 8):
    R.integer(cut, 2, 16)
    need(type(epsilon) is int and epsilon in (-1, 1), "actual quadratic sign required")
    need(
        place in ("good", "old_branch", "zero", "infinity"),
        "declared source stratum required",
    )
    if place == "good":
        need(kind in ("e", "s", "c"), "good S3 class required")
        base = A.signed_series(M.segre_series(kind, cut), epsilon)
        stalk = kind
    elif place == "old_branch":
        need(kind == "C2", "old branch must retain its full C2 invariant algebra")
        base = A.signed_series(M.segre_series("C2", cut), epsilon)
        stalk = "C2"
    elif place == "zero":
        need(kind in ("e", "s", "c"), "old unramified zero Frobenius required")
        base = A.even_series(M.segre_series(kind, cut))
        stalk = kind
    else:
        need(kind in ("C3", "C3s"), "actual residual infinity class required")
        base = A.even_series(M.segre_series(kind, cut))
        stalk = "C3"
    determinant = M.substituted(standard_determinant(stalk), 2, cut)
    divided = E.divide(base, determinant, cut)
    symmetric = E.integer_power(standard_determinant(stalk), -1, cut // 2)
    by_tensor = [
        sum(base[n - 2 * k] * symmetric[k] for k in range(n // 2 + 1))
        for n in range(cut + 1)
    ]
    need(
        divided == by_tensor, "stalkwise tensor/Sym source lost its grading convolution"
    )
    need(
        all(type(x) is int for x in divided),
        "constructible source traces must remain integral",
    )
    return {
        "place": place,
        "Frobenius_kind": kind,
        "quadratic_sign": epsilon,
        "original_A_series": base,
        "standard_stalk_determinant_in_t_squared": determinant,
        "declared_B_series": divided,
        "tensor_Sym_series": by_tensor,
    }


def averaged(series, weights, divisor):
    numerators = [
        sum(weight * row[n] for row, weight in zip(series, weights))
        for n in range(len(series[0]))
    ]
    need(
        all(value % divisor == 0 for value in numerators),
        "inertia character average is not integral",
    )
    return [value // divisor for value in numerators]


def extension_order_control(epsilon: int = 1, cut: int = 8):
    R.integer(cut, 4, 16)
    old = local_source("old_branch", "C2", epsilon, cut)
    ambient = averaged(
        [
            local_source("good", kind, epsilon, cut)["declared_B_series"]
            for kind in ("e", "s")
        ],
        [1, 1],
        2,
    )
    need(
        old["declared_B_series"][3] == 23 * epsilon and ambient[3] == 26 * epsilon,
        "old C2 degree-three operation-order counterfeit disappeared",
    )
    infinity = []
    for kind in ("C3", "C3s"):
        declared = local_source("infinity", kind, 1, cut)["declared_B_series"]
        if kind == "C3":
            full = A.even_series(
                averaged(
                    [
                        local_source("good", h, 1, cut)["declared_B_series"]
                        for h in ("e", "c")
                    ],
                    [1, 2],
                    3,
                )
            )
            expected = [25, 38]
        else:
            full = A.even_series(local_source("good", "s", 1, cut)["declared_B_series"])
            expected = [3, 4]
        need(
            [declared[4], full[4]] == expected,
            "infinity crossed-invariant sector was discarded",
        )
        infinity.append(
            {
                "kind": kind,
                "declared_and_ambient_grade_four": expected,
                "declared": declared,
                "ambient_first": full,
            }
        )
    zeros = []
    for kind in ("e", "s", "c"):
        declared = local_source("zero", kind, 1, cut)["declared_B_series"]
        full = A.even_series(local_source("good", kind, 1, cut)["declared_B_series"])
        need(
            declared == full,
            "central quadratic zero inertia must commute with the untwisted standard addition",
        )
        zeros.append({"kind": kind, "both_operations": declared})
    return {
        "quadratic_sign": epsilon,
        "old_C2_declared": old["declared_B_series"],
        "old_C2_ambient_first": ambient,
        "old_C2_degree_three_pair": [23 * epsilon, 26 * epsilon],
        "infinity_order_controls": infinity,
        "zero_commuting_controls": zeros,
    }


def source_coefficient_control(index: int):
    R.integer(index, 0, 2)
    source = A.native_source(index)
    old = A.closed_coefficient_control(index)
    q = source["parameters"][0]
    pe = source["old"]["polynomials"]["E"]
    actual = [1, 0, 0]
    standard_sum = 0
    for item in source["primitive_rows"][0]["finite_fibre_histogram"]:
        kind = A.fibre_kind(item)
        chi = item["chi_u"]
        place = "zero" if chi == 0 else ("old_branch" if kind == "C2" else "good")
        local = local_source(place, kind, 1 if chi == 0 else chi, 2)
        actual = M.multiply(
            actual, E.integer_power(local["declared_B_series"], item["number"], 2), 2
        )
        standard_sum += item["number"] * {"e": 2, "s": 0, "c": -1, "C2": 1}[kind]
    infinity_kind = "C3" if q % 3 == 1 else "C3s"
    actual = M.multiply(
        actual, local_source("infinity", infinity_kind, 1, 2)["declared_B_series"], 2
    )
    actual = M.multiply(actual, [1, 0, old["closed_degree_two_first_grade_trace"]], 2)
    need(
        standard_sum == pe[1],
        "all rational standard stalks do not reproduce elliptic H1",
    )
    predicted = M.multiply(
        old["coherent_place_coefficients"], M.substituted(pe, 2, 2), 2
    )
    need(
        actual == predicted,
        "constructible full-place coefficients do not match the actual standard L factor",
    )
    return {
        "parameters": source["parameters"],
        "original_E_chi_coefficients": old["coherent_place_coefficients"],
        "new_B_coefficients_by_all_stalks": actual,
        "new_B_coefficients_by_elliptic_cohomology": predicted,
        "actual_standard_stalk_sum_including_ramification": standard_sum,
        "elliptic_polynomial": pe,
        "closed_degree_two_first_grade_unchanged": old[
            "closed_degree_two_first_grade_trace"
        ],
        "primitive_field_orders": [
            row["field_order"] for row in source["primitive_rows"]
        ],
    }


def analytic_case_control():
    relation = F.adams_source_row(2)
    need(
        relation["multiplicities"] == [1, 0, 1],
        "extra standard module is not the actual second relation summand",
    )
    fourth, eighth = F.adams_source_row(4), F.adams_source_row(8)
    nonresonant = []
    for index in range(3):
        source = A.native_source(index)
        q = source["parameters"][0]
        need(q in (5, 7), "existing nonsquare-field source required")
        polynomials = source["old"]["polynomials"]
        # An integral elliptic polynomial over a nonsquare field cannot have
        # an eigenvalue with alpha^2=Q: its conjugate would force determinant -Q.
        common_elliptic_roots = polynomials["E"] == polynomials["D"]
        order = D.even_arithmetic_order(4, int(common_elliptic_roots), 1, False)
        need(
            order["pole_order"] > 0,
            "nonresonant grade-four pole must survive the degree-two clearing",
        )
        nonresonant.append(
            {
                "parameters": source["parameters"],
                "elliptic_polynomials_E_D": [polynomials["E"], polynomials["D"]],
                "E_and_D_have_common_roots": common_elliptic_roots,
                "nonresonance_from_nonsquare_Q_and_integral_positive_determinant": True,
                "grade_four_order_control": order,
                "new_root_growth_power_of_Q": [1, 8],
            }
        )
    resonant = F.actual_clearing_factor()
    return {
        "actual_second_relation": relation,
        "actual_fourth_relation": fourth,
        "actual_eighth_relation": eighth,
        "nonsquare_source_cases": nonresonant,
        "fully_resonant_source": resonant,
        "fully_resonant_new_root_limsup": 1,
        "constructible_source_defined_in_both_cases": True,
        "ordinary_single_infinite_sheaf_or_old_Lie_parity_not_claimed": True,
    }


def build_payload():
    authenticate_frozen()
    return {
        "schema": "constructible-source-elliptic-pole-clearing-v1",
        "provenance": {
            "source_freeze": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "standard_stalk_determinants": {
            kind: standard_determinant(kind) for kind in ("e", "s", "c", "C2", "C3")
        },
        "good_source_tensor_controls": [
            local_source("good", kind, epsilon)
            for kind in ("e", "s", "c")
            for epsilon in (-1, 1)
        ],
        "extension_order_controls": [
            extension_order_control(epsilon) for epsilon in (-1, 1)
        ],
        "actual_global_coefficients": [
            source_coefficient_control(index) for index in range(3)
        ],
        "sharp_analytic_dichotomy": analytic_case_control(),
        "not_claimed": [
            "j_* commutes with tensor or symmetric powers",
            "new B equals original A",
            "new B equals ambient-first extension",
            "fully resonant clearance holds without resonance",
            "old degree-one Koszul parity transfers to internal degree-two generators",
            "one infinite-rank constructible sheaf or new ordinary Fredholm convergence",
            "an archimedean or RH consequence",
        ],
    }


def check_payload(candidate: object):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "constructible source fixture differs from its authenticated exact replay",
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
            "constructible source fixture mismatch",
        )
    print(
        "PASS actual constructible pole-clearing source, ramified tensor order and analytic dichotomy"
    )


if __name__ == "__main__":
    main()
