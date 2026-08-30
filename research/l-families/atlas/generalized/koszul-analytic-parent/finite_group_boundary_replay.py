"""Actual S4 grading completion and the scalar-kernel boundary control."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from functools import cache
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
GENERALIZED = HERE.parent
PREFIX = "research/l-families/atlas/generalized/"
PINS = (
    (
        "c2a8e0477e7aaa9774692b51a7466dfed3e01589",
        "koszul-analytic-parent/global_boundary_replay.py",
        "190cb0f3335178fbf222dde921bdf521a784ccbd",
        "696ce4d04b898ae682fec424a1f48fae58f60c5578c470b5147672d8d8976aac",
    ),
    (
        "c2a8e0477e7aaa9774692b51a7466dfed3e01589",
        "koszul-analytic-parent/GLOBAL_DUALITY_AND_GRADING_BOUNDARY.md",
        "14e88aa7fd6afa8a796c0c8f122add8432405e80",
        "af8ec655af78ffa997d3ebb17f7fe2b1266c785436e588305e9caee83d5e74ff",
    ),
    (
        "d19f421b438485c953469be59c4df8f79a30d2bf",
        "global-s4-resolvent/producer.py",
        "29aa48b52f6d223b4a42766e59e0d1187837ebef",
        "8259d41c9d11f9e1e9d6785165e0a91d08cd0efbe20c3b9e799a61bb299c781d",
    ),
    (
        "d19f421b438485c953469be59c4df8f79a30d2bf",
        "global-s4-resolvent/S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md",
        "677c01d762091472180edbb5d4df38dcce106e24",
        "7277181fc6f0d20f53e47fc39719a68e5ba4b6279db9b14a43e0352c90a5cab1",
    ),
    (
        "d19f421b438485c953469be59c4df8f79a30d2bf",
        "global-s4-resolvent/artifact.json",
        "b4d4b3f6dd4311bd146b248d0c4e640e1878836a",
        "a6df006f372a82cb53c072e2001627b590c4dcaecfbd2acf8e53f8530549d212",
    ),
)
OWNED = (
    "FINITE_GROUP_SOURCE_BOUNDARY.md",
    "FINITE_GROUP_REPLAY.md",
    "finite_group_boundary_replay.py",
    "tests/test_finite_group_boundary.py",
)
FIXTURE = HERE / "finite_group_boundary.verification.json"
CYCLES = ((1, 1, 1, 1), (1, 1, 2), (2, 2), (1, 3), (4,))
SIZES = (1, 6, 3, 8, 6)
TABLE = (
    (1, 1, 2, 3, 3),
    (1, -1, 0, 1, -1),
    (1, 1, 2, -1, -1),
    (1, 1, -1, 0, 0),
    (1, -1, 0, -1, 1),
)
NAMES = ("one", "sign", "two", "std", "tw")
CLASSES = (
    "identity",
    "transposition",
    "double_transposition",
    "three_cycle",
    "four_cycle",
)


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
        need(resolved == blob, "finite-group dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "finite-group dependency hash mismatch")
        need(
            digest((GENERALIZED / name).read_bytes()) == expected,
            "working finite-group dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_boundary_s4", HERE / "global_boundary_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None, "authenticated boundary import failed"
)
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)
C, R, G = B.C, B.R, B.G
S4_SPEC = importlib.util.spec_from_file_location(
    "frozen_s4_geometry", GENERALIZED / "global-s4-resolvent/producer.py"
)
need(
    S4_SPEC is not None and S4_SPEC.loader is not None, "authenticated S4 import failed"
)
S4 = importlib.util.module_from_spec(S4_SPEC)
S4_SPEC.loader.exec_module(S4)
ARTIFACT = json.loads(
    (GENERALIZED / "global-s4-resolvent/artifact.json").read_text(encoding="utf-8")
)


def source_sequences(cut: int) -> tuple[tuple[int, ...], ...]:
    R.integer(cut, 0, 96)
    return _source_sequences(cut)


@cache
def _source_sequences(cut: int) -> tuple[tuple[int, ...], ...]:
    rows = []
    for cycles in CYCLES:
        h = [1] + [0] * cut
        for length in cycles:
            for n in range(length, cut + 1):
                h[n] += h[n - length]
        rows.append(
            tuple(value * (value - (h[n - 1] if n else 0)) for n, value in enumerate(h))
        )
    return tuple(rows)


def rational_sequence(numerator, order: int, exponent: int, cut: int) -> list[int]:
    return [
        sum(
            coefficient * comb((n - i) // order + exponent - 1, exponent - 1)
            for i, coefficient in enumerate(numerator)
            if n >= i and (n - i) % order == 0
        )
        for n in range(cut + 1)
    ]


def source_rows(cut: int) -> list[dict[str, object]]:
    R.integer(cut, 0, 96)
    sequences = source_sequences(cut)
    rational = (
        ([1, 6, 3], 1, 6),
        ([1, 2, 4, 4, 1], 2, 4),
        ([1, 0, 1], 2, 3),
        ([1], 3, 2),
        ([1], 4, 1),
    )
    for sequence, (numerator, order, exponent) in zip(sequences, rational):
        need(
            list(sequence) == rational_sequence(numerator, order, exponent, cut),
            "native symmetric-power character differs from rational series",
        )
    rows = []
    for n in range(cut + 1):
        traces = [seq[n] for seq in sequences]
        mult = []
        for rho in range(5):
            numerator = sum(SIZES[j] * TABLE[j][rho] * traces[j] for j in range(5))
            need(
                numerator >= 0 and numerator % 24 == 0,
                "source multiplicity is not a nonnegative integer",
            )
            mult.append(numerator // 24)
        a, sign, two, std, tw = mult
        dimension = comb(n + 2, 2) * comb(n + 3, 3)
        need(
            sum(d * m for d, m in zip(TABLE[0], mult)) == dimension == traces[0],
            "actual S4 source dimension mismatch",
        )
        conductor = 3 * (dimension - traces[1]) + (dimension - traces[2]) // 2
        need(
            (dimension - traces[2]) % 2 == 0, "double inertia codimension not integral"
        )
        h1 = 4 * sign + 2 * two + 2 * std + 8 * tw
        need(
            h1 == conductor - 2 * dimension + 2 * a, "all-grade Euler-Poincare mismatch"
        )
        rows.append(
            {
                "grade": n,
                "class_traces": traces,
                "multiplicities": mult,
                "h0_h1_h2": [a, h1, a],
                "conductor": conductor,
                "kappa": h1 // 2 - a,
            }
        )
    return rows


def class_values(z: Fraction) -> tuple[Fraction, ...]:
    z = C.exact(z)
    need(abs(z) < 1, "strict grading disk required")
    return (
        (1 + 6 * z + 3 * z * z) / (1 - z) ** 6,
        (1 + 2 * z + 4 * z * z + 4 * z**3 + z**4) / (1 - z * z) ** 4,
        (1 + z * z) / (1 - z * z) ** 3,
        1 / (1 - z**3) ** 2,
        1 / (1 - z**4),
    )


def sectors(z: Fraction) -> tuple[Fraction, ...]:
    values = class_values(z)
    return tuple(
        sum(
            (Fraction(SIZES[j] * TABLE[j][rho], 24) * values[j] for j in range(5)),
            Fraction(0),
        )
        for rho in range(5)
    )


def native_panel(index: int) -> dict[str, object]:
    R.integer(index, 0, 2)
    return _native_panel(index)


@cache
def _native_panel(index: int) -> dict[str, object]:
    frozen = ARTIFACT["panels"][index]
    rows = [
        S4.count_source(S4.make_field(frozen["p"], m), frozen["b"], frozen["c"])
        for m in (1, 2)
    ]
    need(
        json.dumps(rows, sort_keys=True)
        == json.dumps(frozen["rows"][:2], sort_keys=True),
        "small primitive source counts differ from frozen full reconstruction",
    )
    return {
        "id": frozen["id"],
        "p": frozen["p"],
        "b": frozen["b"],
        "c": frozen["c"],
        "primitive_rows": rows,
        "polynomials": frozen["polynomials"],
    }


def native_trace(row, z: Fraction) -> Fraction:
    values = class_values(z)
    by_class = dict(zip(CLASSES, values))
    by_class["branch_split"] = (values[0] + values[1]) / 2
    by_class["branch_nonsplit"] = (values[1] + values[2]) / 2
    value = sum(
        (
            number * by_class[label]
            for label, number in row["finite_class_census"].items()
        ),
        Fraction(0),
    )
    value += (values[0] + values[2]) / 2 if row["field_order"] % 4 == 1 else values[1]
    return value


def fibre_controls(panel) -> list[dict[str, object]]:
    grades = source_rows(24)
    out = []
    for row in panel["primitive_rows"]:
        local = [row["local_stalk_sums"][name] for name in NAMES]
        controls = []
        for z in (Fraction(1, 10), Fraction(1, 4), Fraction(-1, 4)):
            w = z ** row["extension"]
            trace = native_trace(row, w)
            expected = sum((m * t for m, t in zip(sectors(w), local)), Fraction(0))
            need(trace == expected, "actual full S4 ramification series mismatch")
            controls.append(
                {
                    "z": C.qjson(z),
                    "required_weight": C.qjson(w),
                    "trace": C.qjson(trace),
                }
            )
        grade_traces = []
        for grade in grades:
            traces = grade["class_traces"]
            values = dict(zip(CLASSES, traces))
            values["branch_split"] = Fraction(traces[0] + traces[1], 2)
            values["branch_nonsplit"] = Fraction(traces[1] + traces[2], 2)
            actual = sum(
                number * values[label]
                for label, number in row["finite_class_census"].items()
            )
            actual += (
                Fraction(traces[0] + traces[2], 2)
                if row["field_order"] % 4 == 1
                else traces[1]
            )
            expected = sum(m * t for m, t in zip(grade["multiplicities"], local))
            actual = Fraction(actual)
            need(
                actual == expected and actual.denominator == 1,
                "finite-grade S4 stalk trace mismatch",
            )
            grade_traces.append(int(actual))
        out.append(
            {
                "extension": row["extension"],
                "field_order": row["field_order"],
                "finite_class_census": row["finite_class_census"],
                "rational_controls": controls,
                "graded_traces": grade_traces,
            }
        )
    return out


def power_data(panel, cut: int):
    R.integer(cut, 1, 48)
    q = panel["p"]
    sums = [
        S4.P.local_sums_from_polynomial(panel["polynomials"][name], cut)
        for name in ("D", "R", "E", "tw")
    ]
    rows = []
    for m in range(1, cut + 1):
        local = [q**m + 1] + [sequence[m - 1] for sequence in sums]
        zcount = sum(d * t for d, t in zip(TABLE[0], local))
        need(
            0 <= zcount <= 24 * (q**m + 1),
            "regular source count violates geometric bound",
        )
        if m <= 2:
            need(
                zcount
                == panel["primitive_rows"][m - 1][
                    "Z_points_from_normalized_local_regular_character"
                ],
                "regular trace differs from primitive normalized fibre count",
            )
        rows.append((local, zcount))
    return rows


def finite_L(panel, value: Fraction, grade: int) -> Fraction:
    value = C.exact(value)
    R.integer(grade, 0, 3)
    need((1 - value) * (1 - panel["p"] * value) != 0, "explicit finite-grade pole")
    mult = source_rows(grade)[grade]["multiplicities"]
    result = ((1 - value) * (1 - panel["p"] * value)) ** (-mult[0])
    for name, exponent in zip(("D", "R", "E", "tw"), mult[1:]):
        factor = sum(
            (c * value**i for i, c in enumerate(panel["polynomials"][name])),
            Fraction(0),
        )
        result *= factor**exponent
    return result


def finite_duality(panel, cut: int) -> dict[str, object]:
    R.integer(cut, 0, 3)
    q, z, T = panel["p"], Fraction(2, 3), Fraction(1, 13)
    rows = source_rows(cut)
    K = sum(row["kappa"] for row in rows)
    W = sum(row["grade"] * row["kappa"] for row in rows)
    left, right = Fraction(1), Fraction(1)
    for n in range(cut + 1):
        left *= finite_L(panel, T * z**n, n)
        right *= finite_L(panel, 1 / (q * T * z**n), n)
    prefactor = Fraction(q) ** K * T ** (2 * K) * z ** (2 * W)
    need(left == prefactor * right, "actual finite-source functional equation failed")
    return {"cut": cut, "K": K, "W": W, "source_functional_equation": True}


def boundary_constant(panel, order: int, T: Fraction, cut=24):
    R.integer(order, 1, 12)
    R.integer(cut, 12, 48)
    T = C.exact(T)
    q = panel["p"]
    need(0 < T and q * T < 1, "strict positive arithmetic disk required")
    data = power_data(panel, cut)
    middle = sum(
        (
            Fraction(5, 12) * data[m - 1][1] * T**m / m**7
            for m in range(order, cut + 1, order)
        ),
        Fraction(0),
    )
    h = q * T
    error = 20 * h ** (cut + 1) / ((cut + 1) ** 7 * (1 - h))
    return middle - error, middle + error


def radial_control(panel, order: int, radius: Fraction, T: Fraction, cut=24):
    R.integer(order, 1, 2)
    R.integer(cut, 12, 48)
    radius, T = C.exact(radius), C.exact(T)
    q = panel["p"]
    need(
        Fraction(9, 10) <= radius < 1 and 0 < T and q * T < 1,
        "bounded radial source control required",
    )
    z = radius if order == 1 else -radius
    total = Fraction(0)
    for m, (local, _) in enumerate(power_data(panel, cut), 1):
        total += (
            T**m * sum((a * b for a, b in zip(sectors(z**m), local)), Fraction(0)) / m
        )
    middle = (1 - radius) ** 6 * total
    h = q * T
    error = 20 * h ** (cut + 1) / ((cut + 1) * (1 - h))
    observed = middle - error, middle + error
    target = boundary_constant(panel, order, T, cut)
    need(
        target[0] > 0 and observed[0] > target[1] / 2,
        "radial source bound did not exceed half the proved limiting constant",
    )
    return {
        "root_order": order,
        "radius": C.qjson(radius),
        "T": C.qjson(T),
        "scaled_finite_log": C.interval_json((middle, middle)),
        "proved_log_tail": C.qjson(error),
        "observed_interval": C.interval_json(observed),
        "boundary_constant": C.interval_json(target),
        "above_half_actual_constant": True,
    }


def scalar_kernel_control(q: int, T: Fraction, cut=24):
    R.integer(q, 5, 7)
    need(q in (5, 7), "bounded scalar source field required")
    R.integer(cut, 4, 48)
    T = C.exact(T)
    need(0 < T and q * T < 1, "strict positive scalar source disk required")
    actual = sum(
        (Fraction(q**m + 1, 2 * m * m) * T**m for m in range(1, cut + 1)), Fraction(0)
    )
    wrong = sum(
        (Fraction(q**m + 1, 2 * m * m) * T**m for m in range(2, cut + 1, 2)),
        Fraction(0),
    )
    missing = actual - wrong
    need(missing >= (q + 1) * T / 2, "scalar resonance loss was not detected")
    z = Fraction(1, 4)
    averaged = Fraction(q + 1, 2) * (1 / (1 - z) + 1 / (1 + z))
    need(
        averaged == (q + 1) / (1 - z * z),
        "actual quadratic-cover scalar average failed",
    )
    return {
        "Q": q,
        "T": C.qjson(T),
        "cut": cut,
        "root_order": 2,
        "actual_partial_constant": C.qjson(actual),
        "wrong_identity_only": C.qjson(wrong),
        "omitted_positive_scalar_terms": C.qjson(missing),
        "first_omitted_term_lower_bound": C.qjson((q + 1) * T / 2),
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    panels = []
    for index in range(3):
        panel = native_panel(index)
        q = panel["p"]
        T = Fraction(1, 2 * q)
        constants = [
            {"order": h, "interval": C.interval_json(boundary_constant(panel, h, T))}
            for h in range(1, 9)
        ]
        panels.append(
            {
                "source_id": panel["id"],
                "parameters": [q, panel["b"], panel["c"]],
                "primitive_recount_degrees": [1, 2],
                "reused_polynomial_source_freeze": "d19f421b438485c953469be59c4df8f79a30d2bf",
                "fibre_controls": fibre_controls(panel),
                "finite_duality": [finite_duality(panel, n) for n in range(3)],
                "boundary_constants": constants,
                "radial_controls": [
                    radial_control(panel, h, Fraction(999, 1000), T) for h in (1, 2)
                ],
            }
        )
    return {
        "schema": "finite-group-source-boundary-s4-v1",
        "provenance": {
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "actual_S4_grade_rows": source_rows(24),
        "source_panels": panels,
        "actual_scalar_kernel_falsifiers": [
            scalar_kernel_control(q, Fraction(1, 2 * q)) for q in (5, 7)
        ],
        "primitive_field_orders_in_this_replay": [5, 25, 7, 49],
        "frozen_larger_reconstruction_reused_not_recomputed": True,
        "not_claimed": [
            "identity is sole leading term without scalar hypothesis",
            "arbitrary complex-T natural boundary",
            "new reconstruction of degree-eight polynomial from two counts",
            "one critical circle or bounded finite-prefactor infinite duality",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "finite-group fixture differs from complete authenticated replay",
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
            "finite-group fixture mismatch",
        )
    print("PASS actual S4 source, finite-group boundary and scalar-kernel replay")


if __name__ == "__main__":
    main()
