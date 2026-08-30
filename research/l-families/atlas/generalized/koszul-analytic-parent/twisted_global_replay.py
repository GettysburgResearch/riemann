"""Actual ramified quadratic twist, genus-nine counts, and entire completion."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE = "e2b0ef1b35fa46e81a1f1b447a70f42dd3b92c2e"
PINS = (
    (
        "global_cohomology_replay.py",
        "87fd6d661a88e7830d234963b8dce16b49caa8f2",
        "da202437478ed4a199deb4b2f05ca2e7ce1062faa5d60c1c29bd80c4a8aacf66",
    ),
    (
        "GLOBAL_COHOMOLOGICAL_COMPLETION.md",
        "8ecc724afc29e048097d955b8eb7a872d26f79a7",
        "fadf5a3e609ce64b6c49cb848186495bab579cba5fdb5a5e594638b635469d66",
    ),
)
OWNED = (
    "RAMIFIED_TWISTED_GLOBAL_COMPLETION.md",
    "TWISTED_GLOBAL_REPLAY.md",
    "twisted_global_replay.py",
    "tests/test_twisted_global.py",
)
FIXTURE = HERE / "twisted_global.verification.json"
SOURCES = ((5, 1, 1), (7, 1, 1), (7, 4, 4))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for name, blob, expected in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", FREEZE + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "twisted global dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "twisted global dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working twisted global dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_global_for_twist", HERE / "global_cohomology_replay.py"
)
need(SPEC is not None and SPEC.loader is not None, "authenticated import failed")
G = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)
C, R, S, GEOM = G.C, G.R, G.S, G.GEOM
P = GEOM.P


def count_twisted(p: int, A: int, B: int, degree: int) -> dict[str, object]:
    p, A, B = G.source_parameters(p, A, B)
    R.integer(degree, 1, 3)
    return _count_twisted(p, A, B, degree)


@cache
def _count_twisted(p: int, A: int, B: int, degree: int) -> dict[str, object]:
    field = P.Field(p, degree)
    q = field.q
    squares, fourths, cubics = [0] * q, [0] * q, [0] * q
    for x in range(q):
        square = field.mul(x, x)
        squares[square] += 1
        fourths[field.mul(square, square)] += 1
        cubics[field.cubic(x, A, B)] += 1
    infinity = squares[field.add_constant(0, -3)]
    elliptic, quartic, closure, lifted = 1, 1, infinity, infinity
    for x in range(q):
        fx, gx = field.cubic(x, A, B), GEOM.g_value(field, x, A)
        elliptic += squares[fx]
        quartic += fourths[fx]
        closure += squares[fx] * squares[gx]
        lifted += fourths[fx] * squares[gx]
    sign_curve = 1
    sign_sum, std_sum = 0, 0
    histogram = Counter()
    for u in range(q):
        u2 = field.mul(u, u)
        disc = GEOM.discriminant_value(field, u2, A, B)
        chi, sign = squares[u] - 1, squares[disc] - 1
        roots = cubics[u2]
        need(
            (roots, sign) in ((3, 1), (1, -1), (0, 1), (2, 0)),
            "unexpected normalized S3 fibre",
        )
        histogram[roots, sign, chi] += 1
        sign_curve += squares[field.mul(u, disc)]
        sign_sum += chi * sign
        std_sum += chi * (roots - 1)
    need(sign_sum == sign_curve - q - 1, "sign-twist curve trace failed")
    need(std_sum == quartic - elliptic, "Prym fibre trace failed")
    need(
        lifted - closure == sign_sum + 2 * std_sum,
        "genus-nine regular-source trace decomposition failed",
    )
    need(sum(histogram.values()) == q, "finite twist histogram lost a point")
    return {
        "degree": degree,
        "field_order": q,
        "field_modulus": field.modulus,
        "counts": {
            "E": elliptic,
            "C": quartic,
            "Dchi": sign_curve,
            "Z": closure,
            "Ztilde": lifted,
        },
        "local_sums_Dchi_Prym": [sign_sum, std_sum],
        "Delta": lifted - closure,
        "infinity_points_Z_and_Ztilde": infinity,
        "twisted_stalks_at_zero_and_infinity": [0, 0],
        "finite_fibre_histogram": [
            {
                "distinct_roots": roots,
                "sign_trace": sign,
                "chi_u": chi,
                "number": number,
            }
            for (roots, sign, chi), number in sorted(histogram.items())
        ],
    }


def quartic_from_counts(q: int, sums: list[int]) -> tuple[int, ...]:
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded prime required")
    need(type(sums) is list and len(sums) == 2, "two primitive sums required")
    for value in sums:
        R.integer(value, -1000, 1000)
    partial = P.newton_from_local_sums(sums)
    poly = (*partial, q * partial[1], q * q)
    need(P.quartic_weil(list(poly), q), "source quartic violates weight duality")
    return poly


def native_source(p: int, A: int, B: int) -> dict[str, object]:
    return _native_source(*G.source_parameters(p, A, B))


@cache
def _native_source(p: int, A: int, B: int) -> dict[str, object]:
    rows = [count_twisted(p, A, B, m) for m in (1, 2, 3)]
    polynomials = {}
    for index, name in enumerate(("Dchi", "Prym")):
        poly = quartic_from_counts(
            p, [row["local_sums_Dchi_Prym"][index] for row in rows[:2]]
        )
        predicted = P.local_sums_from_polynomial(list(poly), 3)
        need(
            predicted[2] == rows[2]["local_sums_Dchi_Prym"][index],
            "held-out extension degree three disagrees with source polynomial",
        )
        polynomials[name] = poly
    old = G.native_source(p, A, B)
    for before, after in zip(old["primitive_rows"], rows[:2]):
        for name in ("E", "Z"):
            need(
                before["counts"][name] == after["counts"][name],
                "untwisted source count changed under adapter",
            )
    return {
        "parameters_p_A_B": [p, A, B],
        "primitive_rows": rows,
        "polynomials": polynomials,
        "reconstruction": "two primitive counts plus proved rank-four reciprocal duality; degree three held out",
    }


def power_traces(poly: tuple[int, ...], cut: int) -> list[int]:
    need(type(poly) is tuple and len(poly) == 5, "rank-four tuple required")
    R.integer(cut, 1, 48)
    for value in poly:
        R.integer(value, -1000, 1000)
    need(poly[0] == 1 and poly[-1] in (25, 49), "bounded source quartic required")
    q = 5 if poly[-1] == 25 else 7
    need(P.quartic_weil(list(poly), q), "invalid pure reciprocal source")
    return [-value for value in P.local_sums_from_polynomial(list(poly), cut)]


def fibre_trace(row: dict[str, object], z: Fraction) -> Fraction:
    z = C.exact(z)
    need(abs(z) < 1, "strict grading disk required")
    fe, fs, fc = (1 + 2 * z) / (1 - z) ** 4, 1 / (1 - z * z) ** 2, 1 / (1 - z**3)
    values = {(3, 1): fe, (1, -1): fs, (0, 1): fc, (2, 0): (fe + fs) / 2}
    return sum(
        (
            item["number"]
            * item["chi_u"]
            * values[item["distinct_roots"], item["sign_trace"]]
            for item in row["finite_fibre_histogram"]
        ),
        Fraction(0),
    )


def fibre_control(source: dict[str, object]) -> list[dict[str, object]]:
    sequence, grades = S.source_sequences(12), S.source_rows(12)
    out = []
    for row in source["primitive_rows"]:
        sums = row["local_sums_Dchi_Prym"]
        actual = []
        for n, grade in enumerate(grades):
            a, b, c = grade["multiplicities_1_sign_std"]
            value = 0
            for item in row["finite_fibre_histogram"]:
                roots, sign = item["distinct_roots"], item["sign_trace"]
                unramified = {(3, 1): "e", (1, -1): "s", (0, 1): "c"}
                trace = a + c if sign == 0 else sequence[unramified[roots, sign]][n]
                value += item["number"] * item["chi_u"] * trace
            need(value == b * sums[0] + c * sums[1], "twisted graded stalk sum failed")
            actual.append(value)
        rational = []
        for z in (Fraction(1, 10), Fraction(1, 4)):
            w = z ** row["degree"]
            _, b, c = G.sectors(w)
            value = fibre_trace(row, w)
            need(value == b * sums[0] + c * sums[1], "all-grade twist trace failed")
            rational.append(
                {
                    "z": C.qjson(z),
                    "required_weight": C.qjson(w),
                    "actual_trace": C.qjson(value),
                }
            )
        out.append(
            {
                "degree": row["degree"],
                "finite_grade_traces": actual,
                "all_grade_controls": rational,
            }
        )
    return out


def finite_grade_log(source, z: Fraction, T: Fraction, cut: int):
    q = source["parameters_p_A_B"][0]
    z, T = G.parameters(q, z, T)
    R.integer(cut, 1, 24)
    total = Fraction(0), Fraction(0)
    for n, row in enumerate(S.source_rows(cut)[1:], 1):
        _, b, c = row["multiplicities_1_sign_std"]
        u = T * z**n
        for name, weight in (("Dchi", b), ("Prym", c)):
            poly = source["polynomials"][name]
            value = sum(
                (coefficient * u**i for i, coefficient in enumerate(poly)), Fraction(0)
            )
            interval = C.weighted_log(value, weight)
            total = total[0] + interval[0], total[1] + interval[1]
    return C.rounded(total)


def power_log(source, z: Fraction, T: Fraction, cut: int) -> Fraction:
    q = source["parameters_p_A_B"][0]
    z, T = G.parameters(q, z, T)
    R.integer(cut, 1, 48)
    ud = power_traces(source["polynomials"]["Dchi"], cut)
    vp = power_traces(source["polynomials"]["Prym"], cut)
    total = Fraction(0)
    for m in range(1, cut + 1):
        _, b, c = G.sectors(z**m)
        total -= T**m * (b * ud[m - 1] + c * vp[m - 1]) / m
    return total


def determinant_control(source, z: Fraction, T: Fraction, grade_cut=16, power_cut=24):
    q = source["parameters_p_A_B"][0]
    z, T = G.parameters(q, z, T)
    grade = finite_grade_log(source, z, T, grade_cut)
    grade_error = G.grade_tail(q, z, T, grade_cut)
    power = power_log(source, z, T, power_cut)
    power_error = G.adams_tail(q, z, T, power_cut)
    need(
        grade[0] - grade_error <= power + power_error
        and grade[1] + grade_error >= power - power_error,
        "independent twisted determinant enclosures disagree",
    )
    return {
        "z": C.qjson(z),
        "T": C.qjson(T),
        "grade_cut": grade_cut,
        "power_cut": power_cut,
        "grade_log": C.interval_json(grade),
        "proved_grade_tail": C.qjson(grade_error),
        "power_log": C.qjson(power),
        "proved_power_tail": C.qjson(power_error),
        "grade_zero_factor": 1,
        "has_denominator": False,
        "inside_initial_Euler_T_disk": q * T < 1,
    }


def signed_constants(source, T: Fraction, cut=24):
    q = source["parameters_p_A_B"][0]
    T = C.exact(T)
    need(0 < T and q * T < 1, "strict positive arithmetic disk required")
    R.integer(cut, 12, 48)
    ud = power_traces(source["polynomials"]["Dchi"], cut)
    vp = power_traces(source["polynomials"]["Prym"], cut)
    delta = [-a - 2 * b for a, b in zip(ud, vp)]
    for m, row in enumerate(source["primitive_rows"], 1):
        need(delta[m - 1] == row["Delta"], "primitive signed regular count failed")
    h = q * T
    error = 6 * h ** (cut + 1) / ((cut + 1) ** 5 * (1 - h))
    rows = []
    for order in range(1, 9):
        middle = sum(
            (
                Fraction(delta[m - 1], 2 * m**5) * T**m
                for m in range(order, cut + 1, order)
            ),
            Fraction(0),
        )
        interval = middle - error, middle + error
        rows.append(
            {
                "root_order": order,
                "constant_enclosure": C.interval_json(interval),
                "certified_sign": 1
                if interval[0] > 0
                else -1
                if interval[1] < 0
                else 0,
            }
        )
    return {
        "T": C.qjson(T),
        "power_cut": cut,
        "source_Delta_sequence": delta,
        "proved_tail": C.qjson(error),
        "constant_controls": rows,
        "nonzero_infinite_subsequence_is_a_proof_not_a_finite_test": True,
    }


def twist_order_control() -> dict[str, object]:
    row = S.source_rows(2)[2]
    a, b, c = row["multiplicities_1_sign_std"]
    return {
        "grade": 2,
        "actual_post_source_twist_h0_h1_h2": [0, 4 * (b + c), 0],
        "wrong_input_twist_h0_h1_h2": row["h0_h1_h2_dimensions"],
        "actual_identity_chi_minus_one_trace": -18,
        "wrong_chi_squared_trace": 18,
        "old_C2_stalk_dimension": a + c,
        "new_zero_and_infinity_stalks": [0, 0],
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    panels = []
    for params in SOURCES:
        source = native_source(*params)
        panels.append(
            {
                "parameters_p_A_B": list(params),
                "primitive_rows": source["primitive_rows"],
                "polynomials": {
                    key: list(value) for key, value in source["polynomials"].items()
                },
                "reconstruction": source["reconstruction"],
                "fibre_controls": fibre_control(source),
                "entire_determinant_controls": [
                    determinant_control(source, z, T)
                    for z, T in (
                        (Fraction(1, 4), Fraction(1, 10)),
                        (Fraction(1, 10), Fraction(1, 2)),
                    )
                ],
                "signed_boundary_controls": signed_constants(
                    source, Fraction(1, 2 * params[0])
                ),
            }
        )
    return {
        "schema": "actual-ramified-twist-global-completion-v1",
        "provenance": {
            "freeze": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "source_panels": panels,
        "twist_order_falsifier": twist_order_control(),
        "primitive_field_orders": [5, 25, 125, 7, 49, 343],
        "not_claimed": [
            "positive twisted point-count differences",
            "every root has nonzero radial constant",
            "natural boundary for arbitrary complex T",
            "same exponential Lie operator",
            "one critical circle or fixed-z finite functional equation",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "twisted global fixture differs from authenticated complete replay",
    )


def main() -> None:
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
            "twisted replay fixture mismatch",
        )
    print("PASS actual ramified twist, genus-nine source and entire determinant replay")


if __name__ == "__main__":
    main()
