"""Primitive finite S3 fibres and the completed global cohomology determinant."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
GENERALIZED = HERE.parent
PREFIX = "research/l-families/atlas/generalized/"
PINS = (
    (
        "19960780cf9582cea2105ddf3e89bee3e2c3b687",
        "koszul-analytic-parent/s3_cutoff_replay.py",
        "a3758831e98c42728afb6764b53f67b4f16277a7",
        "d0c5500105e3ca2f023ab5e7e6120c4d5d5981125e500a26fb412b6885361f4a",
    ),
    (
        "19960780cf9582cea2105ddf3e89bee3e2c3b687",
        "koszul-analytic-parent/S3_GRADE_CUTOFF_ANOMALY.md",
        "510125c221cab7ddc0753b7576f887de18a3864f",
        "0aad550815ec186864b7222801fbe1255a473d845ed201cbd1c793ed1d0844e6",
    ),
    (
        "567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f",
        "global-s3-prym/closure_replay.py",
        "ed2bdd9b5a15a76d17e3594a46d61c635b8fba91",
        "a238bafed8f3c49ebc5ff7a36656757b1d17b01b4edb317b1c70604064c5e614",
    ),
    (
        "567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f",
        "global-s3-prym/GALOIS_CLOSURE_AND_TWO_ELLIPTIC_MAPS.md",
        "ea9468a34a05f8b76d4e8136462b27b63e654bd8",
        "eff3ef741e8151f719e920979a91014446ea626d04796739dd9de691aa259348",
    ),
)
OWNED = (
    "GLOBAL_COHOMOLOGICAL_COMPLETION.md",
    "GLOBAL_COHOMOLOGY_REPLAY.md",
    "global_cohomology_replay.py",
    "tests/test_global_cohomology.py",
)
FIXTURE = HERE / "global_cohomology.verification.json"
SOURCES = ((5, 1, 1), (7, 1, 1), (7, 4, 4))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for freeze, name, blob, expected in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", freeze + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "global cohomology dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "global cohomology dependency hash mismatch")
        need(
            digest((GENERALIZED / name).read_bytes()) == expected,
            "working global cohomology dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_s3_cutoff_global", HERE / "s3_cutoff_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "cannot load authenticated analytic source",
)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
S, R = C.S, C.R
GEOM_SPEC = importlib.util.spec_from_file_location(
    "frozen_global_closure", GENERALIZED / "global-s3-prym/closure_replay.py"
)
need(
    GEOM_SPEC is not None and GEOM_SPEC.loader is not None,
    "cannot load authenticated geometric source",
)
GEOM = importlib.util.module_from_spec(GEOM_SPEC)
GEOM_SPEC.loader.exec_module(GEOM)


def source_parameters(p: int, A: int, B: int) -> tuple[int, int, int]:
    R.integer(p, 5, 7)
    need(p in (5, 7), "bounded prime field source required")
    R.integer(A, -7, 7)
    R.integer(B, -7, 7)
    need(
        A % p != 0 and (-4 * A**3 - 27 * B**2) % p != 0,
        "generic smooth S3 source required",
    )
    return p, A, B


def native_source(p: int, A: int, B: int) -> dict[str, object]:
    return _native_source(*source_parameters(p, A, B))


@cache
def _native_source(p: int, A: int, B: int) -> dict[str, object]:
    rows = [GEOM.count_source(GEOM.P.Field(p, m), A, B) for m in (1, 2)]
    polynomials = {}
    for name in ("E", "D"):
        trace = p + 1 - rows[0]["counts"][name]
        need(
            trace * trace <= 4 * p,
            "primitive elliptic trace violates the exact weight bound",
        )
        polynomials[name] = (1, -trace, p)
        need(
            rows[1]["counts"][name] == p * p + 1 - (trace * trace - 2 * p),
            "held-out extension count disagrees with source Frobenius polynomial",
        )
    return {
        "parameters_p_A_B": [p, A, B],
        "primitive_rows": rows,
        "polynomials": polynomials,
        "reconstruction": "degree-one complete count plus proved determinant Q; extension degree two is held out",
    }


def sectors(w: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    w = C.exact(w)
    need(abs(w) < 1, "strict grade disk required")
    fe, fs, fc = (1 + 2 * w) / (1 - w) ** 4, 1 / (1 - w * w) ** 2, 1 / (1 - w**3)
    return (fe + 3 * fs + 2 * fc) / 6, (fe - 3 * fs + 2 * fc) / 6, (fe - fc) / 3


def source_hilbert(w: Fraction) -> Fraction:
    w = C.exact(w)
    need(0 <= w < 1, "positive strict grade radius required")
    return (1 + 2 * w) / (1 - w) ** 4


def fibre_trace(row: dict[str, object], w: Fraction) -> Fraction:
    w = C.exact(w)
    need(abs(w) < 1, "strict grade disk required")
    fe, fs, fc = (1 + 2 * w) / (1 - w) ** 4, 1 / (1 - w * w) ** 2, 1 / (1 - w**3)
    values = {(3, 1): fe, (1, -1): fs, (0, 1): fc, (2, 0): (fe + fs) / 2}
    result = sum(
        (
            item["number"] * values[item["distinct_roots"], item["sign_trace"]]
            for item in row["finite_fibre_histogram"]
        ),
        Fraction(0),
    )
    return result + ((fe + 2 * fc) / 3 if row["field_order"] % 3 == 1 else fs)


def fibre_control(source: dict[str, object]) -> list[dict[str, object]]:
    sequence = S.source_sequences(12)
    grades = S.source_rows(12)
    out = []
    for row in source["primitive_rows"]:
        q, m = row["field_order"], row["degree"]
        actual = []
        infinity = S.infinity_trace(q, 12)
        for n in range(13):
            a, b, c = grades[n]["multiplicities_1_sign_std"]
            value = infinity[n]
            for item in row["finite_fibre_histogram"]:
                kind = {(3, 1): "e", (1, -1): "s", (0, 1): "c", (2, 0): "branch"}[
                    item["distinct_roots"], item["sign_trace"]
                ]
                value += item["number"] * (
                    a + c if kind == "branch" else sequence[kind][n]
                )
            expected = (
                a * (q + 1)
                + b * (row["counts"]["D"] - q - 1)
                + c * (row["counts"]["E"] - q - 1)
            )
            need(
                value == expected,
                "native graded fibre trace disagrees with complete curve cohomology",
            )
            actual.append(value)
        rational_controls = []
        for z in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 3)):
            w = z**m
            a, b, c = sectors(w)
            expected = (
                a * (q + 1)
                + b * (row["counts"]["D"] - q - 1)
                + c * (row["counts"]["E"] - q - 1)
            )
            native = fibre_trace(row, w)
            need(
                native == expected,
                "all-grade finite-source rational trace identity failed",
            )
            wrong = fibre_trace(row, z)
            if m == 2:
                need(wrong != expected, "wrong closed-degree grading was not detected")
            rational_controls.append(
                {
                    "z": C.qjson(z),
                    "required_weight_z_power_degree": C.qjson(w),
                    "native_and_cohomological_trace": C.qjson(native),
                    "unpowered_grading_trace": C.qjson(wrong),
                    "wrong_grading_detected_when_degree2": m == 2 and wrong != expected,
                }
            )
        out.append(
            {
                "extension_degree": m,
                "field_order": q,
                "complete_source_counts": row["counts"],
                "finite_fibre_histogram": row["finite_fibre_histogram"],
                "graded_fibre_traces_0_to_12": actual,
                "all_grade_rational_trace_controls": rational_controls,
            }
        )
    return out


def frobenius_traces(polynomial: tuple[int, int, int], degree: int) -> list[int]:
    R.integer(degree, 1, 48)
    need(
        isinstance(polynomial, tuple) and len(polynomial) == 3 and polynomial[0] == 1,
        "elliptic source polynomial required",
    )
    need(
        all(isinstance(x, int) and not isinstance(x, bool) for x in polynomial),
        "integer source polynomial required",
    )
    q, trace = polynomial[2], -polynomial[1]
    need(
        q in (5, 7) and trace * trace <= 4 * q,
        "unsupported or non-Weil source polynomial",
    )
    out = [2, trace]
    for _ in range(2, degree + 1):
        out.append(trace * out[-1] - q * out[-2])
    return out[1:]


def parameters(q: int, z: Fraction, T: Fraction) -> tuple[Fraction, Fraction]:
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded source field required")
    z, T = C.exact(z), C.exact(T)
    need(
        0 < z <= Fraction(1, 3) and 0 <= T <= 1,
        "bounded positive cohomology control required",
    )
    need(q * T * z < 1, "positive-degree determinant logarithm outside its strict disk")
    return z, T


def finite_grade_log(
    source: dict[str, object], z: Fraction, T: Fraction, cut: int
) -> tuple[Fraction, Fraction]:
    q = source["parameters_p_A_B"][0]
    z, T = parameters(q, z, T)
    R.integer(cut, 1, 24)
    total = Fraction(0), Fraction(0)
    pe, pd = source["polynomials"]["E"], source["polynomials"]["D"]
    for n, row in enumerate(S.source_rows(cut)[1:], 1):
        a, b, c = row["multiplicities_1_sign_std"]
        u = T * z**n
        values = (
            (1 + pd[1] * u + q * u * u, b),
            (1 + pe[1] * u + q * u * u, c),
            (1 - u, -a),
            (1 - q * u, -a),
        )
        for value, weight in values:
            interval = C.weighted_log(value, weight)
            total = total[0] + interval[0], total[1] + interval[1]
    return C.rounded(total)


def grade_tail(q: int, z: Fraction, T: Fraction, cut: int) -> Fraction:
    z, T = parameters(q, z, T)
    R.integer(cut, 1, 24)
    dimensions = S.source_sequences(cut)["e"]
    tail = source_hilbert(z) - sum(
        (dimension * z**n for n, dimension in enumerate(dimensions)), Fraction(0)
    )
    need(tail > 0, "infinite positive-grade source tail was lost")
    return 2 * q * T * tail / (1 - q * T * z ** (cut + 1))


def adams_log(
    source: dict[str, object], z: Fraction, T: Fraction, cut: int
) -> Fraction:
    q = source["parameters_p_A_B"][0]
    z, T = parameters(q, z, T)
    R.integer(cut, 1, 48)
    ed = frobenius_traces(source["polynomials"]["D"], cut)
    ee = frobenius_traces(source["polynomials"]["E"], cut)
    total = Fraction(0)
    for m in range(1, cut + 1):
        a, b, c = sectors(z**m)
        total += T**m * ((a - 1) * (1 + q**m) - b * ed[m - 1] - c * ee[m - 1]) / m
    return total


def adams_tail(q: int, z: Fraction, T: Fraction, cut: int) -> Fraction:
    z, T = parameters(q, z, T)
    R.integer(cut, 1, 48)
    h = q * T * z
    cr = (source_hilbert(z) - 1) / z
    return 2 * cr * h ** (cut + 1) / ((cut + 1) * (1 - h))


def determinant_control(
    source: dict[str, object],
    z: Fraction,
    T: Fraction,
    grade_cut: int = 16,
    power_cut: int = 24,
) -> dict[str, object]:
    q = source["parameters_p_A_B"][0]
    z, T = parameters(q, z, T)
    need((1 - T) * (1 - q * T) != 0, "control lies on an explicit grade-zero pole")
    grade = finite_grade_log(source, z, T, grade_cut)
    ge = grade_tail(q, z, T, grade_cut)
    power = adams_log(source, z, T, power_cut)
    pe = adams_tail(q, z, T, power_cut)
    need(
        grade[0] - ge <= power + pe and grade[1] + ge >= power - pe,
        "independent source-grade and cohomological-power enclosures disagree",
    )
    return {
        "z": C.qjson(z),
        "T": C.qjson(T),
        "grade_cut": grade_cut,
        "power_cut": power_cut,
        "finite_grade_log_Gcal": C.interval_json(grade),
        "proved_grade_tail": C.qjson(ge),
        "finite_power_log_Gcal": C.qjson(power),
        "proved_power_tail": C.qjson(pe),
        "explicit_grade_zero_ZP1": C.qjson(1 / ((1 - T) * (1 - q * T))),
        "inside_initial_arithmetic_Euler_disk": q * T < 1,
        "inside_positive_grade_log_disk": q * T * z < 1,
        "full_global_object_includes_grade_zero": True,
    }


def divisor_control(q: int, radius: Fraction, degree: int) -> dict[str, object]:
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded source field required")
    R.integer(degree, 1, 24)
    radius = C.exact(radius)
    need(
        0 < radius and q * radius * radius < 1,
        "strict proved noncancellation range required",
    )
    rows = []
    zero_radii, pole_radii = set(), set()
    for n, row in enumerate(S.source_rows(degree)):
        a, h1, _ = row["h0_h1_h2_dimensions"]
        square = radius ** (-2 * n)
        if h1:
            zero_radii.add(square / q)
        if a:
            pole_radii.update((square, square / (q * q)))
        rows.append(
            {
                "grade": n,
                "zero_radius_squared": C.qjson(square / q),
                "zero_multiplicity": h1,
                "pole_radii_squared": [C.qjson(square), C.qjson(square / (q * q))],
                "each_pole_multiplicity": a,
            }
        )
    need(
        zero_radii.isdisjoint(pole_radii),
        "zero-pole cancellation in the proved noncancellation range",
    )
    return {
        "Q": q,
        "damping_radius": C.qjson(radius),
        "finite_divisor_rows": rows,
        "numerator_zero_count_with_multiplicity": sum(
            row["zero_multiplicity"] for row in rows
        ),
        "denominator_pole_count_with_multiplicity": 2
        * sum(row["each_pole_multiplicity"] for row in rows),
        "all_grade_noncancellation_is_proved_not_inferred_from_this_list": True,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    C.authenticate_frozen()
    S.authenticate_frozen()
    panels = []
    for params in SOURCES:
        source = native_source(*params)
        panels.append(
            {
                "parameters_p_A_B": list(params),
                "primitive_polynomials_E_D": {
                    name: list(poly) for name, poly in source["polynomials"].items()
                },
                "reconstruction_scope": source["reconstruction"],
                "complete_fibre_controls": fibre_control(source),
                "global_determinant_controls": [
                    determinant_control(source, z, T, cut)
                    for z, T in (
                        (Fraction(1, 4), Fraction(1, 10)),
                        (Fraction(1, 10), Fraction(1, 2)),
                    )
                    for cut in (12, 16)
                ],
            }
        )
    return {
        "schema": "source-global-cohomological-completion-v1",
        "provenance": {
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "source_panels": panels,
        "global_divisor_controls": [
            divisor_control(q, Fraction(1, 4), 12) for q in (5, 7)
        ],
        "primitive_field_orders": [5, 25, 7, 49],
        "arithmetic": "exact finite source fields, integers and certified rational logarithms",
        "not_claimed": [
            "same operator as the exponential Lie parent",
            "canonical complex Hilbert norms",
            "cohomology commutes with Hilbert completion of sheaves",
            "one critical circle",
            "usual fixed-z finite functional equation",
            "new arithmetic RH theorem",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "global cohomology fixture differs from authenticated complete replay",
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
            "global cohomology fixture differs from complete replay",
        )
    print("PASS actual-source global cohomological completion exact replay")


if __name__ == "__main__":
    main()
