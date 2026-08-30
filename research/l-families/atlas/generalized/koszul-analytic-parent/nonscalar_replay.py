"""Native involution controls for the nonscalar grade-radius theorem.

Actual source eigencharacters determine each finite involution block.
Large multiplicities are used only as integer weights of bounded logs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "f8b385d69c8b5eea13ef7f474a23835bf0dbbd2f"
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    (
        "critical_boundary_replay.py",
        "5274f3a70d595ac730fd5520e4d540d568449b60",
        "14d3c21b20fb1e3071810d2f32625997a284553c379a19ad115b7fbe332cfb3a",
    ),
    (
        "CRITICAL_GRADE_BOUNDARY.md",
        "c1ab0530d4d7c2485051792ae95fa66a2b0b2c92",
        "6d83c759a177d85d6f64c8f64e8ffcb9527416c187191bd37d4959d9df240216",
    ),
)
OWNED = (
    "NONSCALAR_GRADE_RADIUS.md",
    "NONSCALAR_REPLAY.md",
    "nonscalar_replay.py",
    "tests/test_nonscalar.py",
)
FIXTURE = HERE / "nonscalar.verification.json"


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
        need(resolved == blob, "frozen nonscalar dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "frozen nonscalar dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working nonscalar dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_critical_replay", HERE / "critical_boundary_replay.py"
)
need(SPEC is not None and SPEC.loader is not None, "cannot load authenticated source")
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
R = C.R


def native_sequence(k: int, degree: int, involution: bool) -> list[int]:
    R.integer(k, 3, 5)
    R.integer(degree, 0, 64)
    need(isinstance(involution, bool), "explicit Boolean involution flag required")
    return [
        ((1 if n % 2 == 0 else 0) if involution else n + 1)
        * math.comb(n + k - 1, k - 1)
        for n in range(degree + 1)
    ]


def logarithm(sequence: list[int]) -> list[Fraction]:
    need(
        1 <= len(sequence) <= 65 and sequence[0] == 1,
        "bounded normalized series required",
    )
    need(
        all(
            isinstance(value, int) and not isinstance(value, bool) for value in sequence
        ),
        "integer source coefficients required",
    )
    out = [Fraction(0)] * len(sequence)
    for n in range(1, len(sequence)):
        out[n] = (
            Fraction(sequence[n])
            - sum((j * out[j] * sequence[n - j] for j in range(1, n)), Fraction(0)) / n
        )
    return out


@cache
def source_characters(k: int, degree: int) -> tuple[tuple[int, int, int, int], ...]:
    R.integer(k, 3, 5)
    R.integer(degree, 1, 64)
    identity = logarithm(native_sequence(k, degree, False))
    involution = logarithm(native_sequence(k, degree, True))
    out = []
    for n in range(1, degree + 1):
        dimension = (-1) ** (n + 1) * sum(
            R.mobius(d) * identity[n // d] / d for d in range(1, n + 1) if n % d == 0
        )
        character = (-1) ** (n + 1) * sum(
            R.mobius(d) * (identity if d % 2 == 0 else involution)[n // d] / d
            for d in range(1, n + 1)
            if n % d == 0
        )
        need(
            dimension.denominator == character.denominator == 1,
            "source character is nonintegral",
        )
        dimension, character = int(dimension), int(character)
        need(
            dimension >= abs(character) and (dimension + character) % 2 == 0,
            "source character cannot be a genuine involution",
        )
        if n % 2:
            need(character == 0, "odd source character must vanish by conjugacy")
        out.append(
            (
                dimension,
                character,
                (dimension + character) // 2,
                (dimension - character) // 2,
            )
        )
    return tuple(out)


def native_control(k: int) -> dict[str, object]:
    R.integer(k, 3, 5)
    sequence = native_sequence(k, 64, True)
    numerator = [math.comb(k, j) if j % 2 == 0 else 0 for j in range(k + 1)]
    denominator = [0] * (2 * k + 1)
    for j in range(k + 1):
        denominator[2 * j] = (-1) ** j * math.comb(k, j)
    actual = [
        sum(denominator[j] * sequence[n - j] for j in range(min(n, 2 * k) + 1))
        for n in range(65)
    ]
    need(
        actual == numerator + [0] * (64 - k),
        "native even-source rational identity failed",
    )
    rows = source_characters(k, 64)
    if k == 3:
        a, b = (R.ONE, R.neg(R.ONE)), (R.ONE, R.ONE, R.ONE)
        for n in (1, 2, 3):
            trace = R.character(R.source_grade(n)[2], a, b)
            need(
                trace == (Fraction(rows[n - 1][1]), Fraction(0)),
                "native Lie quotient character disagrees",
            )
    return {
        "ranks": [2, k],
        "input": "diag(1,-1) and identity_k",
        "source_even_numerator": numerator,
        "source_denominator": denominator,
        "coverage_through_degree": 64,
        "source_involution_rows": [
            {
                "degree": n,
                "dimension": row[0],
                "trace": row[1],
                "plus_eigenspace": row[2],
                "minus_eigenspace": row[3],
            }
            for n, row in enumerate(rows, 1)
        ],
        "radius_formula": "tan(pi/(2k)); lies strictly between 1/(k-1) and its square root",
    }


def log1p_interval(u: Fraction, terms: int = 32) -> tuple[Fraction, Fraction]:
    need(isinstance(u, Fraction), "exact internal Fraction required")
    need(
        max(u.numerator.bit_length(), u.denominator.bit_length()) <= 2048,
        "internal logarithm input exceeds bit cap",
    )
    R.integer(terms, 8, 48)
    need(abs(u) < 1, "log1p power series requires |u|<1")
    middle = sum(((-1) ** (j + 1) * u**j / j for j in range(1, terms + 1)), Fraction(0))
    error = abs(u) ** (terms + 1) / ((terms + 1) * (1 - abs(u)))
    return middle - error, middle + error


def finite_log(cut: int, real_t: Fraction | None = None) -> tuple[Fraction, Fraction]:
    R.integer(cut, 2, 64)
    if real_t is not None:
        real_t = R.rational(real_t)
        need(
            0 < real_t < Fraction(3, 5) and 3 * real_t**2 < 1,
            "real control must lie strictly before the nonscalar zero radius",
        )
    total = Fraction(0), Fraction(0)
    for n, (dimension, character, plus, minus) in enumerate(
        source_characters(3, cut), 1
    ):
        if n % 2:
            need(
                character == 0 and dimension % 2 == 0,
                "odd involution block is not paired",
            )
            u = Fraction(1, 3) ** n if real_t is None else -(real_t ** (2 * n))
            block = C.interval_scale(log1p_interval(u), dimension // 2)
        else:
            tn = Fraction(-1, 3) ** (n // 2) if real_t is None else real_t**n
            block = C.interval_add(
                C.interval_scale(log1p_interval(-tn), plus),
                C.interval_scale(log1p_interval(tn), minus),
            )
        total = C.interval_add(total, C.rounded(C.interval_scale(block, (-1) ** n)))
    return C.rounded(total)


@cache
def residual_cauchy_bound() -> Fraction:
    # V(t) = -3 log(1-t^2) - log D_2(t), bounded at radius 2/3.
    x = Fraction(4, 9)
    dimensions = source_characters(3, 64)
    singular_sum = sum(
        (row[0] * x**n for n, row in enumerate(dimensions, 1)), Fraction(0)
    )
    singular_sum += 27 * Fraction(8, 9) ** 65
    return Fraction(12, 5) + Fraction(3, 2) * singular_sum


def boundary_error(cut: int) -> Fraction:
    R.integer(cut, 2, 64)
    return 8 * residual_cauchy_bound() * Fraction(7, 8) ** (cut + 1) + Fraction(
        45, 4
    ) * Fraction(2, 3) ** (cut + 1)


def boundary_control(cut: int) -> dict[str, object]:
    observed = finite_log(cut)
    half = cut // 2
    harmonic = sum((Fraction(1, j) for j in range(1, half + 1)), Fraction(0))
    corrected = C.interval_add(observed, (harmonic, harmonic))
    expected = C.log_interval(Fraction(27, 64))
    error = boundary_error(cut)
    need(
        corrected[0] <= expected[1] + error and corrected[1] >= expected[0] - error,
        "nonscalar cutoff contradicts the proved Cauchy/block tail bound",
    )
    gamma = harmonic - C.log_interval(half + 1)[1], harmonic - C.log_interval(half)[0]
    limit_base = C.log_interval(Fraction(27, 32))
    limit = limit_base[0] - gamma[1], limit_base[1] - gamma[0]
    return {
        "cut": cut,
        "point": "t=i/sqrt(3), with t^2=-1/3 used exactly",
        "log_DN_plus_H_floor_N_over_2": C.interval_json(corrected),
        "log_regular_part_27_over_64": C.interval_json(expected),
        "proved_absolute_log_error": R.qjson(error),
        "log_N_times_DN": C.interval_json(
            C.interval_add(observed, C.log_interval(cut))
        ),
        "log_limit_constant_27_exp_minus_gamma_over_32": C.interval_json(limit),
        "all_block_eigenvalue_multiplicities_nonnegative": True,
        "ordinary_trace_class": False,
        "Schatten_two": True,
    }


def real_control(t: Fraction, cut: int) -> dict[str, object]:
    t = R.rational(t)
    observed = finite_log(cut, t)
    source = (1 + 3 * t * t) / (1 - t * t) ** 3
    expected = C.log_interval(source)
    ratio = Fraction(3, 2) * t
    root_ratio = 3 * t * t
    half = cut // 2
    root_tail = root_ratio ** (half + 1) / ((half + 1) * (1 - root_ratio))
    v_tail = residual_cauchy_bound() * ratio ** (cut + 1) / (1 - ratio)
    block_tail = 3 * (2 * t * t) ** (cut + 1) / (2 * (1 - t) * (1 - 2 * t * t))
    error = root_tail + v_tail + block_tail
    need(
        observed[0] <= expected[1] + error and observed[1] >= expected[0] - error,
        "real ordered-product control contradicts the analytic tail",
    )
    return {
        "t": R.qjson(t),
        "cut": cut,
        "source_F": R.qjson(source),
        "finite_source_log": C.interval_json(observed),
        "source_log": C.interval_json(expected),
        "proved_log_error": R.qjson(error),
        "ordinary_trace_class": t < Fraction(1, 2),
        "within_nonscalar_grade_radius": 3 * t * t < 1,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    C.authenticate_frozen()
    C.M.authenticate_frozen()
    R.authenticate()
    return {
        "schema": "koszul-nonscalar-grade-radius-v1",
        "provenance": {
            "frozen_critical_commit": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "arithmetic": "integers and exact rational log intervals; no expanded Hilbert states",
        "source_controls": [native_control(k) for k in (3, 4, 5)],
        "boundary_controls": [boundary_control(cut) for cut in (32, 48, 63, 64)],
        "strictly_beyond_trace_class_real_controls": [
            real_control(Fraction(11, 20), cut) for cut in (32, 64)
        ],
        "not_machine_proved": [
            "all-unitary first-zero-circle theorem",
            "all-k trigonometric radius inequalities",
            "Mertens cutoff limit",
            "every-point product behavior outside the analytic disk",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "nonscalar fixture differs from authenticated complete replay",
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
            "nonscalar fixture differs from complete replay",
        )
    print("PASS nonscalar native grade-radius exact replay")


if __name__ == "__main__":
    main()
