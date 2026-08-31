"""Source-corrected place Euler product, finite extraction and positive residue."""

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
        "83506c9741bded6c8932163ff8e56b78892155b2",
        "global_lie_cohomology_replay.py",
        "f6420dd1053cd1aab611747b2dec7c4310d55a96",
        "a664886a2b543bcbc0abf2c3657c3b2bdfc2a45210fa491486abb7a47de736a3",
    ),
    (
        "83506c9741bded6c8932163ff8e56b78892155b2",
        "GLOBAL_KOSZUL_LIE_COHOMOLOGY.md",
        "6fc43276dc337c68ae4c3d9f70de22a114d14fa3",
        "6f9e63828238f87fbdb57a48d8372d083bc30054b3fc69ed11e92c9d4587fca4",
    ),
    (
        "83506c9741bded6c8932163ff8e56b78892155b2",
        "S3_LIE_RAMIFICATION_CORRECTION.md",
        "82c013287a4040dc2881dd7f25d2c8185d668eed",
        "2bfd6b59cddf14aaac71390ee80a1393551ecb51e5288ecc668e10de65126fb6",
    ),
    (
        "da203ad2d170835499a0f4f7484f04ff787ee408",
        "finite_group_boundary_replay.py",
        "e39aca60c4d2230635765a75fc82f80556f9f3df",
        "e5f7a1f22b084ba8167fa526706068132cc388705a858d65fe7eabe94d1d0db0",
    ),
    (
        "da203ad2d170835499a0f4f7484f04ff787ee408",
        "FINITE_GROUP_SOURCE_BOUNDARY.md",
        "33872bfcdbe77338d404d184b6548d4adb253bd0",
        "924728399218f8f19ff48d7eaf08f4388de31cd17a37126b597d84b98fce227c",
    ),
)
OWNED = (
    "S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md",
    "SEGRE_PLACE_EULER_REPLAY.md",
    "segre_place_euler_replay.py",
    "tests/test_segre_place_euler.py",
)
FIXTURE = HERE / "segre_place_euler.verification.json"


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
        need(actual == blob, "place Euler dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "place Euler dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working place Euler source changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_arithmetic_lie_euler", HERE / "global_lie_cohomology_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "authenticated arithmetic Lie import failed",
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
S4_SPEC = importlib.util.spec_from_file_location(
    "frozen_s4_euler_source", HERE / "finite_group_boundary_replay.py"
)
need(
    S4_SPEC is not None and S4_SPEC.loader is not None, "authenticated S4 import failed"
)
F = importlib.util.module_from_spec(S4_SPEC)
S4_SPEC.loader.exec_module(F)
C, R = M.C, M.R


def divide(numerator, denominator, cut: int):
    need(denominator and denominator[0] == 1, "unit formal denominator required")
    out = [0] * (cut + 1)
    for n in range(cut + 1):
        out[n] = (numerator[n] if n < len(numerator) else 0) - sum(
            denominator[j] * out[n - j]
            for j in range(1, min(n, len(denominator) - 1) + 1)
        )
    return out


def integer_power(poly, exponent: int, cut: int):
    need(
        isinstance(exponent, int)
        and not isinstance(exponent, bool)
        and abs(exponent) <= 128,
        "bounded integer source exponent required",
    )
    out = [1] + [0] * cut
    for _ in range(abs(exponent)):
        out = M.multiply(out, poly, cut)
    return divide([1], out, cut) if exponent < 0 else out


def good_counts(row):
    values = {(3, 1): "e", (1, -1): "s", (0, 1): "c"}
    out = {key: 0 for key in ("e", "s", "c")}
    branch = 0
    for item in row["finite_fibre_histogram"]:
        key = item["distinct_roots"], item["sign_trace"]
        if key == (2, 0):
            branch += item["number"]
        else:
            out[values[key]] += item["number"]
    need(
        sum(out.values()) + branch == row["field_order"],
        "complete finite source census lost a point",
    )
    return out, branch


def closed_place_data(index: int):
    source = M.native_source(index)
    first, b1 = good_counts(source["primitive_rows"][0])
    second, b2 = good_counts(source["primitive_rows"][1])
    numerators = {
        "e": second["e"] - first["e"] - first["s"],
        "s": second["s"],
        "c": second["c"] - first["c"],
    }
    need(
        all(value >= 0 and value % 2 == 0 for value in numerators.values()),
        "Frobenius-square closed-place counts not nonnegative integral",
    )
    degree_two = {kind: value // 2 for kind, value in numerators.items()}
    need(
        b1 % 2 == 0 and (b2 - b1) % 2 == 0 and (4 - b2) % 4 == 0,
        "even quartic branch orbit pattern was lost",
    )
    branch_orbits = {1: b1, 2: (b2 - b1) // 2, 4: (4 - b2) // 4}
    need(
        all(value >= 0 for value in branch_orbits.values())
        and sum(degree * count for degree, count in branch_orbits.items()) == 4,
        "complete finite branch divisor was not reconstructed",
    )
    q = source["parameters_p_A_B"][0]
    need(
        sum(degree_two.values()) + branch_orbits[2] == (q * q - q) // 2,
        "degree-two base place count disagrees with P1",
    )
    return {
        "parameters": source["parameters_p_A_B"],
        "degree_one_good": first,
        "degree_two_good": degree_two,
        "extension_two_good": second,
        "finite_branch_orbits": [
            [degree, count] for degree, count in branch_orbits.items()
        ],
        "infinity_kind": "C3" if q % 3 == 1 else "C3s",
    }


def place_euler_series(index: int):
    data = closed_place_data(index)
    cut = 2
    out = [1, 0, 0]
    for degree, key in ((1, "degree_one_good"), (2, "degree_two_good")):
        for kind, count in data[key].items():
            factor = M.substituted(M.segre_series(kind, cut), degree, cut)
            out = M.multiply(out, integer_power(factor, count, cut), cut)
    for degree, count in data["finite_branch_orbits"]:
        if degree <= cut:
            factor = M.substituted(M.segre_series("C2", cut), degree, cut)
            out = M.multiply(out, integer_power(factor, count, cut), cut)
    return M.multiply(out, M.segre_series(data["infinity_kind"], cut), cut)


def finite_lie_series(index: int):
    source = M.native_source(index)
    q = source["parameters_p_A_B"][0]
    cut = 2
    out = [1, 0, 0]
    for row in M.lie_rows(cut):
        n, sign = row["grade"], row["parity_sign"]
        a, b, std = row["multiplicities"]
        pairs = [
            ([1, -1], -sign * a),
            ([1, -q], -sign * a),
            (source["polynomials"]["D"], sign * b),
            (source["polynomials"]["E"], sign * std),
        ]
        for polynomial, weight in pairs:
            factor = M.substituted(polynomial, n, cut)
            out = M.multiply(out, integer_power(factor, weight, cut), cut)
    return out


def bad_correction_series(index: int):
    data = closed_place_data(index)
    out = [1, 0, 0]
    for degree, count in data["finite_branch_orbits"]:
        if degree <= 2:
            ratio = divide(M.segre_series("C2", 2), M.local_parent("C2", 2), 2)
            out = M.multiply(
                out, integer_power(M.substituted(ratio, degree, 2), count, 2), 2
            )
    kind = data["infinity_kind"]
    return M.multiply(
        out, divide(M.segre_series(kind, 2), M.local_parent(kind, 2), 2), 2
    )


def global_coefficient_control(index: int):
    data = closed_place_data(index)
    source = M.native_source(index)
    place = place_euler_series(index)
    lie = finite_lie_series(index)
    correction = bad_correction_series(index)
    need(
        place == M.multiply(lie, correction, 2),
        "genuine closed-place Euler and corrected cohomology series disagree",
    )
    b1 = dict(data["finite_branch_orbits"])[1]
    i = int(data["infinity_kind"] == "C3")
    expected_difference = 6 * b1 + 4 * i + 2 * (1 - i)
    need(
        place[1] == source["primitive_rows"][0]["counts"]["Z"]
        and place[2] - lie[2] == expected_difference,
        "exact ramified coefficient correction failed",
    )
    z1, z2 = [row["counts"]["Z"] for row in source["primitive_rows"]]
    need(
        lie[2] == (z1 * z1 + z2) // 2 - source["primitive_rows"][0]["counts"]["E"],
        "regular first-grade zeta and relation grade failed independent trace comparison",
    )
    return {
        "place_Euler_coefficients": place,
        "signed_Lie_coefficients": lie,
        "actual_bad_correction": correction,
        "degree_two_correction": expected_difference,
    }


def source_parent_prefix(kind: str, grade_cut: int, series_cut: int):
    need(kind in ("e", "s", "c"), "good S3 class required")
    R.integer(grade_cut, 1, 8)
    R.integer(series_cut, grade_cut + 1, 16)
    out = [1] + [0] * series_cut
    for row in M.lie_rows(grade_cut):
        n = row["grade"]
        dim, s, c = row["class_traces"]
        sign = (-1) ** n
        if kind == "e":
            factors = [(n, sign * dim, 1)]
        elif kind == "s":
            factors = [(n, sign * (dim + s) // 2, 1), (n, sign * (dim - s) // 2, -1)]
        else:
            invariant, other = (dim + 2 * c) // 3, (dim - c) // 3
            factors = [(n, sign * (invariant - other), 1), (3 * n, sign * other, 1)]
        for order, exponent, eigenvalue in factors:
            if order <= series_cut:
                out = M.multiply(
                    out,
                    M.binomial_factor(order, exponent, eigenvalue, series_cut),
                    series_cut,
                )
    return out


def extraction_control(grade_cut: int):
    R.integer(grade_cut, 1, 8)
    cut = grade_cut + 2
    controls = []
    for kind in ("e", "s", "c"):
        prefix = source_parent_prefix(kind, grade_cut, cut)
        residual = divide(M.segre_series(kind, cut), prefix, cut)
        need(
            residual[: grade_cut + 1] == [1] + [0] * grade_cut,
            "finite source extraction did not cancel required grades",
        )
        controls.append(
            {"class": kind, "parent_prefix": prefix, "Euler_remainder": residual}
        )
    return {
        "extracted_grade_cut": grade_cut,
        "series_cut": cut,
        "source_classes": controls,
    }


def segre_value(kind: str, t: Fraction):
    t = C.exact(t)
    need(0 < t < 1, "positive strict local argument required")
    fe = (1 + 2 * t) / (1 - t) ** 4
    fs = 1 / (1 - t * t) ** 2
    fc = 1 / (1 - t**3)
    values = {
        "e": fe,
        "s": fs,
        "c": fc,
        "C2": (fe + fs) / 2,
        "C3": (fe + 2 * fc) / 3,
        "C3s": fs,
    }
    need(kind in values, "known local source required")
    return values[kind]


def first_tail(kind: str, t: Fraction):
    t = C.exact(t)
    need(0 < t < 1 and kind in ("e", "s", "c"), "positive good source required")
    value = {"e": 1 - 3 * t * t + 2 * t**3, "s": 1 - t * t, "c": 1 - t**3}[kind]
    need(0 < value < 1, "first source extraction tail lost positivity")
    return value


def residue_control(index: int):
    source = M.native_source(index)
    data = closed_place_data(index)
    q = source["parameters_p_A_B"][0]
    x = Fraction(1, q)
    values = {
        name: sum(
            (coefficient * x**i for i, coefficient in enumerate(poly)), Fraction(0)
        )
        for name, poly in source["polynomials"].items()
    }
    proper_residue = values["D"] * values["E"] ** 2 / (1 - x)
    boundary = Fraction(1)
    bad_segre = Fraction(1)
    for degree, count in data["finite_branch_orbits"]:
        boundary *= (1 - x**degree) ** (3 * count)
        bad_segre *= segre_value("C2", x**degree) ** count
    boundary *= (1 - x) ** 2 if q % 3 == 1 else 1 - x * x
    bad_segre *= segre_value(data["infinity_kind"], x)
    good_prefix = Fraction(1)
    for degree, key in ((1, "degree_one_good"), (2, "degree_two_good")):
        for kind, count in data[key].items():
            good_prefix *= first_tail(kind, x**degree) ** count
    upper = proper_residue * boundary * bad_segre * good_prefix
    error = x**3 / ((1 - x) * (1 - 3 * x**6))
    lower = upper * (1 - error)
    need(
        0 < error < 1 and 0 < lower <= upper,
        "positive arithmetic residue interval failed",
    )
    return {
        "Q": q,
        "proper_closure_residue": C.qjson(proper_residue),
        "actual_upstairs_boundary_factor": C.qjson(boundary),
        "actual_bad_Segre_factor": C.qjson(bad_segre),
        "good_place_tail_through_degree_two": C.qjson(good_prefix),
        "proved_omitted_log_bound": C.qjson(error),
        "positive_residue_interval": [C.qjson(lower), C.qjson(upper)],
        "higher_degree_fields_recounted": False,
    }


def first_four_s3_sources():
    rows = M.lie_rows(4)
    expected_characters = [[6, 0, 0], [3, 1, 0], [2, 0, -1], [3, -1, 0]]
    expected_multiplicities = [[1, 1, 2], [1, 0, 1], [0, 0, 1], [0, 1, 1]]
    need(
        [row["class_traces"] for row in rows] == expected_characters
        and [row["multiplicities"] for row in rows] == expected_multiplicities,
        "actual first four S3 Lie sources disagree with sharp-pole source",
    )
    return [
        {
            "grade": row["grade"],
            "character": row["class_traces"],
            "multiplicities": row["multiplicities"],
            "proper_factor_exponents_one_Q_D_E": [
                -row["parity_sign"] * row["multiplicities"][0],
                -row["parity_sign"] * row["multiplicities"][0],
                row["parity_sign"] * row["multiplicities"][1],
                row["parity_sign"] * row["multiplicities"][2],
            ],
        }
        for row in rows
    ]


def bad_numerator_control():
    cut = 12
    denominators = {
        "C2": M.multiply(
            integer_power([1, -1], 4, cut), integer_power([1, 1], 2, cut), cut
        ),
        "C3": M.multiply(integer_power([1, -1], 4, cut), [1, 1, 1], cut),
        "C3s": integer_power([1, 0, -1], 2, cut),
    }
    numerators = {"C2": [1, 1, 3, 1], "C3": [1, -1, 3], "C3s": [1]}
    rows = []
    for kind, numerator in numerators.items():
        product = M.multiply(M.segre_series(kind, cut), denominators[kind], cut)
        need(
            product == numerator + [0] * (cut + 1 - len(numerator)),
            "full invariant Segre series has the wrong bad numerator",
        )
        rows.append(
            {
                "kind": kind,
                "numerator": numerator,
                "denominator": denominators[kind],
                "source_series_checked_through": cut,
            }
        )
    need(
        numerators["C2"][0] == numerators["C2"][-1] == 1,
        "finite branch polynomial lost its algebraic-unit property",
    )
    need(
        numerators["C3"][1] ** 2 - 4 * numerators["C3"][0] * numerators["C3"][2] == -11,
        "split infinity roots not the nonreal conjugate pair of norm 1/3",
    )
    return {
        "local_sources": rows,
        "C2_monic_constant_one": True,
        "C3_root_modulus_squared": [1, 3],
        "quarter_circle_noncollision_requires_characteristic_greater_than_three": True,
    }


def subleading_pole_control(index: int):
    source = M.native_source(index)
    q = source["parameters_p_A_B"][0]
    need(q > 3, "sharp local noncollision requires characteristic greater than three")
    pe = source["polynomials"]["E"]
    need(
        pe[0] == 1 and pe[2] == q and pe[1] * pe[1] <= 4 * q,
        "actual elliptic factor does not satisfy its degree-two Weil constraint",
    )
    cut = 20
    by_source = [1] + [0] * cut
    rows = first_four_s3_sources()
    for row in rows:
        for polynomial, weight in zip(
            ([1, -1], [1, -q], source["polynomials"]["D"], pe),
            row["proper_factor_exponents_one_Q_D_E"],
        ):
            factor = M.substituted(polynomial, row["grade"], cut)
            by_source = M.multiply(by_source, integer_power(factor, weight, cut), cut)
    explicit = [1] + [0] * cut
    factors = (
        ([1, -1], 1, -1),
        ([1, -q], 1, -1),
        (source["polynomials"]["D"], 1, 1),
        (pe, 1, 2),
        ([1, -1], 2, 1),
        ([1, -q], 2, 1),
        (pe, 2, -1),
        (pe, 3, 1),
        (source["polynomials"]["D"], 4, -1),
        (pe, 4, -1),
    )
    for polynomial, grade, weight in factors:
        explicit = M.multiply(
            explicit,
            integer_power(M.substituted(polynomial, grade, cut), weight, cut),
            cut,
        )
    need(
        by_source == explicit,
        "source four-grade product differs from the claimed elliptic denominator",
    )
    pole = M.substituted(pe, 2, 4)
    need(
        pole == [1, 0, pe[1], 0, q] and rows[3]["multiplicities"][0] == 0,
        "quarter-circle pole or grade-four absence of H2 was lost",
    )
    return {
        "parameters": source["parameters_p_A_B"],
        "elliptic_polynomial": list(pe),
        "exact_first_subleading_pole_polynomial": pole,
        "source_four_grade_product_through_degree": cut,
        "source_four_grade_coefficients": by_source,
        "grade_four_trivial_multiplicity": 0,
        "sharp_residual_coefficient_limsup": "Q^(1/4), proved by noncancellation; not fitted",
    }


SQUARE_CLASS = (0, 0, 0, 3, 2)


def s4_lie_sources():
    v = [row[3] for row in F.TABLE]
    w = [value + 1 for value in v]
    first = [a * b for a, b in zip(v, w)]
    second = []
    quotient = []
    r2 = F.source_rows(2)[2]["class_traces"]
    for j, power_class in enumerate(SQUARE_CLASS):
        numerator = (v[j] * v[j] - v[power_class]) * (w[j] * w[j] - w[power_class])
        need(numerator % 4 == 0, "actual exterior-square character not integral")
        second.append(numerator // 4)
        quotient.append((first[j] * first[j] + first[power_class]) // 2 - r2[j])
    need(
        first == F.source_rows(1)[1]["class_traces"] and second == quotient,
        "S4 quadratic relation source differs from Segre presentation",
    )
    rows = []
    for n, character in enumerate((first, second), 1):
        numerators = [
            sum(F.SIZES[j] * F.TABLE[j][rho] * character[j] for j in range(5))
            for rho in range(5)
        ]
        need(
            all(value >= 0 and value % 24 == 0 for value in numerators),
            "S4 Lie multiplicity not nonnegative integral",
        )
        mult = [value // 24 for value in numerators]
        a, sign, two, std, tw = mult
        h1 = 4 * sign + 2 * two + 2 * std + 8 * tw
        rows.append(
            {
                "grade": n,
                "actual_character": character,
                "multiplicities": mult,
                "closed_h0_h1_h2": [a, h1, a],
                "compact_h0_h1_h2": [0, a + 5 * character[0], a],
            }
        )
    return rows


def s4_source_control(index: int):
    R.integer(index, 0, 2)
    panel = F.native_panel(index)
    rows = []
    for primitive in panel["primitive_rows"]:
        local = [primitive["local_stalk_sums"][name] for name in F.NAMES]
        controls = []
        for source in s4_lie_sources():
            values = source["actual_character"]
            by_class = dict(zip(F.CLASSES, values))
            by_class["branch_split"] = Fraction(values[0] + values[1], 2)
            by_class["branch_nonsplit"] = Fraction(values[1] + values[2], 2)
            actual = sum(
                count * by_class[kind]
                for kind, count in primitive["finite_class_census"].items()
            )
            actual += (
                Fraction(values[0] + values[2], 2)
                if primitive["field_order"] % 4 == 1
                else values[1]
            )
            expected = sum(a * b for a, b in zip(source["multiplicities"], local))
            need(
                actual == expected and Fraction(actual).denominator == 1,
                "actual S4 Lie source fibre trace differs from cohomology",
            )
            controls.append(
                {"grade": source["grade"], "complete_source_trace": int(actual)}
            )
        rows.append(
            {
                "extension": primitive["extension"],
                "field_order": primitive["field_order"],
                "controls": controls,
            }
        )
    return rows


def root_certificate():
    lo, hi = Fraction(1, 6), Fraction(1, 5)
    value = lambda x: 1 - 6 * x + 3 * x * x
    need(
        value(lo) > 0 and value(hi) < 0 and hi < 1,
        "S4 interior identity root interval failed",
    )
    need(2 - hi > 1, "S4 conjugate root did not separate from the unit interval")
    return {
        "S3_identity_zero": [-1, 2],
        "S3_noncollision": "2 and odd Q have different prime support",
        "S4_rho_polynomial": [1, -6, 3],
        "S4_positive_rho_interval": [C.qjson(lo), C.qjson(hi)],
        "S4_conjugate_interval": [C.qjson(2 - hi), C.qjson(2 - lo)],
        "S4_noncollision": "a power equal to a rational Q-weight would have an equal conjugate, impossible across 1",
        "criterion_not_a_classification_when_noncollision_fails": True,
    }


def build_payload():
    authenticate_frozen()
    panels = []
    for index in range(3):
        panels.append(
            {
                "closed_place_source": closed_place_data(index),
                "global_coefficient_control": global_coefficient_control(index),
                "positive_residue_control": residue_control(index),
                "exact_subleading_pole_source": subleading_pole_control(index),
            }
        )
    return {
        "schema": "source-corrected-Segre-place-Euler-v1",
        "provenance": {
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "S3_source_panels": panels,
        "S3_finite_extraction": [extraction_control(n) for n in (1, 2, 3, 4, 6)],
        "S3_actual_first_four_Lie_sources": first_four_s3_sources(),
        "full_bad_numerator_noncollision": bad_numerator_control(),
        "S4_actual_first_Lie_sources": s4_lie_sources(),
        "S4_full_source_fibre_controls": [
            s4_source_control(index) for index in range(3)
        ],
        "weight_circle_noncollision_certificate": root_certificate(),
        "maximum_primitive_field_order": 49,
        "not_claimed": [
            "finite samples prove split places in all degrees",
            "local Euler zeros alone prove noncancellation",
            "same infinite Lie operator outside trace class",
            "new Estermann mechanism",
            "first cubic Lie branch survives source correction",
            "coefficient error proves arithmetic RH",
        ],
    }


def check_payload(candidate: object):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "place Euler fixture differs from complete authenticated source replay",
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
            "place Euler fixture mismatch",
        )
    print(
        "PASS actual Segre place Euler source, finite extraction and positive residue"
    )


if __name__ == "__main__":
    main()
