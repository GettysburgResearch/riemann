"""Bounded exact replay for the actual infinite pole-clearing ladder."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93"
SOURCE_PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = {
    "FINITE_RESONANT_COHERENT_POLES.md": "c415abc8a9b363a1cef6e0cd52adca16a4f6c754",
    "CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md": "7ed7f6d68327df4c5f395142503253b19e8938e4",
    "S3_WEIGHT_CIRCLE_POLE_DIVISOR.md": "381ee262cbd59f671a23f29fa19a9dd6f856463b",
    "finite_resonant_poles_replay.py": "aa3a3d92c7123200de683e963dffa7766b8f251b",
    "finite_resonant_poles.verification.json": "93e472ad61f2e10e707fbacf1e890615e12a396e",
}
OWNED = (
    HERE / "MATHEMATICS.md",
    HERE / "PREREGISTERED_TARGETS.md",
    HERE / "REPLAY.md",
    HERE / "replay.py",
    ROOT / "tests/test_graded_completion_ladder.py",
)
FIXTURE = HERE / "verification.json"
MAX_BYTES = 4_000_000
MAX_BITS = 4096


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def source_bytes() -> dict[str, bytes]:
    result = {}
    for name, expected in PINS.items():
        path = SOURCE_PREFIX + name
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen source blob identity changed")
        data = subprocess.check_output(["git", "cat-file", "blob", expected], cwd=ROOT)
        need(len(data) <= MAX_BYTES, "frozen source exceeds byte cap")
        need(
            digest((ROOT / path).read_bytes()) == digest(data), "working source changed"
        )
        result[name] = data
    return result


def mobius(n: int) -> int:
    integer(n, 1, 128)
    remaining, sign, p = n, 1, 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            sign = -sign
            if remaining % p == 0:
                return 0
        p += 1
    return -sign if remaining > 1 else sign


def source_log(kind: str, n: int) -> int:
    integer(n, 1, 128)
    need(kind in ("e", "s", "c"), "S3 class required")
    if kind == "e":
        return 4 - (-2) ** n
    return (4 if n % 2 == 0 else 0) if kind == "s" else (3 if n % 3 == 0 else 0)


def powered_class(kind: str, exponent: int) -> str:
    integer(exponent, 1, 128)
    need(kind in ("e", "s", "c"), "S3 class required")
    if kind == "e" or (kind == "s" and exponent % 2 == 0):
        return "e"
    return "e" if kind == "c" and exponent % 3 == 0 else kind


def source_row(n: int) -> dict:
    integer(n, 1, 64)
    traces = []
    for kind in ("e", "s", "c"):
        top = (-1) ** (n + 1) * sum(
            mobius(d) * source_log(powered_class(kind, d), n // d)
            for d in range(1, n + 1)
            if n % d == 0
        )
        need(top % n == 0, "nonintegral PBW character")
        traces.append(top // n)
    dim, s, c = traces
    tops = (dim + 3 * s + 2 * c, dim - 3 * s + 2 * c, 2 * (dim - c))
    need(all(t >= 0 and t % 6 == 0 for t in tops), "invalid source multiplicities")
    mult = [t // 6 for t in tops]
    return {"grade": n, "characters": traces, "multiplicities": mult}


def anti_dimension(n: int) -> int:
    integer(n, 2, 128)
    need(n % 2 == 0, "even source grade required")
    top = sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1, 2) if n % d == 0)
    need(top >= 0 and top % (2 * n) == 0, "odd-divisor projection not integral")
    return top // (2 * n)


def error_bound(j: int) -> Fraction:
    integer(j, 1, 64)
    return Fraction(4 ** (j // 3 + 1) - 4, 12 * j)


def multiply(left: list[int], right: list[int], cut: int) -> list[int]:
    integer(cut, 0, 64)
    need(len(left) <= cut + 1 and len(right) <= cut + 1, "polynomial length cap")
    out = [0] * (cut + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right[: cut - i + 1]):
            out[i + j] += a * b
    need(all(abs(c).bit_length() <= MAX_BITS for c in out), "coefficient bit cap")
    return out


def ladder_coefficients(field: int, grade_cap: int, cut: int) -> list[int]:
    need(type(field) is int and field in (7, 49), "actual field panel required")
    integer(grade_cap, 2, 64)
    integer(cut, 0, 64)
    need(grade_cap % 2 == 0, "even ladder cutoff required")
    out = [1] + [0] * cut
    for n in range(4, grade_cap + 1, 2):
        degree = 2 * n if field == 7 else n
        exponent = anti_dimension(n) * (1 if field == 7 else 2)
        factor = [0] * (cut + 1)
        for k in range(min(exponent, cut // degree) + 1):
            factor[degree * k] = math.comb(exponent, k) * 7**k
        out = multiply(out, factor, cut)
    return out


def logarithmic_coefficients(field: int, grade_cap: int, cut: int) -> list[int]:
    """Independent formal logarithmic derivative followed by Newton recurrence."""
    need(type(field) is int and field in (7, 49), "actual field panel required")
    integer(grade_cap, 2, 64)
    integer(cut, 0, 64)
    need(grade_cap % 2 == 0, "even ladder cutoff required")
    derivative = [0] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        degree = 2 * n if field == 7 else n
        row = source_row(n)
        exponent = row["multiplicities"][1] + row["multiplicities"][2]
        exponent *= 1 if field == 7 else 2
        for k in range(1, cut // degree + 1):
            derivative[degree * k] += exponent * degree * (-1) ** (k + 1) * 7**k
    out = [1] + [0] * cut
    for m in range(1, cut + 1):
        top = sum(derivative[k] * out[m - k] for k in range(1, m + 1))
        need(top % m == 0, "formal logarithm lost integral coefficient")
        out[m] = top // m
    return out


def rational_pair(q: Fraction) -> list[int]:
    return [q.numerator, q.denominator]


def dyadic_interval(
    low: Fraction, high: Fraction, bits: int = 96
) -> tuple[Fraction, Fraction]:
    integer(bits, 16, 128)
    need(low <= high, "reversed interval")
    scale = 2**bits
    lower = (low.numerator * scale) // low.denominator
    upper = -((-high.numerator * scale) // high.denominator)
    return Fraction(lower, scale), Fraction(upper, scale)


def log1p_interval(u: Fraction, terms: int = 24) -> tuple[Fraction, Fraction]:
    need(type(u) is Fraction and 0 <= u <= 1, "bounded nonnegative rational required")
    integer(terms, 1, 64)
    y = u / (2 + u)
    partial = 2 * sum(
        (y ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Fraction()
    )
    tail = 2 * y ** (2 * terms + 1) / ((2 * terms + 1) * (1 - y * y))
    return partial, partial + tail


def critical_log_interval(field: int, grade_cap: int) -> dict:
    need(type(field) is int and field in (7, 49), "actual field panel required")
    integer(grade_cap, 4, 64)
    need(grade_cap % 2 == 0, "even ladder cutoff required")
    low, high = Fraction(), Fraction()
    copies = 1 if field == 7 else 2
    for n in range(4, grade_cap + 1, 2):
        lo, hi = log1p_interval(Fraction(7, 2**n))
        lo, hi = dyadic_interval(
            copies * anti_dimension(n) * lo, copies * anti_dimension(n) * hi
        )
        low += lo
        high += hi
    # Display a normalized quantity only at exact powers of two; its convergence
    # is proved analytically, not inferred from this finite panel.
    need(grade_cap & (grade_cap - 1) == 0, "normalization panel uses powers of two")
    log2_low, log2_high = log1p_interval(Fraction(1), 64)
    beta = Fraction(7 * copies, 4)
    exponent = grade_cap.bit_length() - 1
    norm_low, norm_high = dyadic_interval(
        low - beta * exponent * log2_high,
        high - beta * exponent * log2_low,
    )
    return {
        "field": field,
        "grade_cutoff": grade_cap,
        "critical_log_interval": [rational_pair(low), rational_pair(high)],
        "log_product_minus_beta_log_N": [
            rational_pair(norm_low),
            rational_pair(norm_high),
        ],
        "beta": rational_pair(beta),
        "directed_arithmetic": "EXACT_RATIONAL_OUTWARD_DYADIC",
    }


def point_counts() -> dict:
    # Literal ordered solutions; no Legendre-symbol implementation is shared.
    e_points = [
        (x, y) for x in range(7) for y in range(7) if (y * y - x**3 - x) % 7 == 0
    ]
    d_points = [
        (u, v) for u in range(7) for v in range(7) if (v * v + 4 + 27 * u**4) % 7 == 0
    ]
    e_count, d_count = len(e_points) + 1, len(d_points) + 2
    need((e_count, d_count) == (8, 8), "actual seven-point source trace changed")
    traces = [8 - e_count, 8 - d_count]
    squared = [a * a - 14 for a in traces]
    need(squared == [-14, -14], "Frobenius squaring mismatch")
    return {
        "q": 7,
        "parameters_A_B": [1, 0],
        "E_affine_points": e_points,
        "D_affine_points": d_points,
        "infinity_counts": [1, 2],
        "proper_counts": [e_count, d_count],
        "traces": traces,
        "F49_traces_from_squaring": squared,
        "P7": [1, 0, 7],
        "P49": [1, 14, 49],
        "F49_enumerated": False,
    }


def strict_equal(actual: object, expected: object) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return actual.keys() == expected.keys() and all(
            strict_equal(actual[k], v) for k, v in expected.items()
        )
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            strict_equal(a, b) for a, b in zip(actual, expected)
        )
    return actual == expected


def build_payload() -> dict:
    sources = source_bytes()
    prior = json.loads(sources["finite_resonant_poles.verification.json"])
    rows = [source_row(n) for n in range(1, 65)]
    for old in prior["direct_source_Adams_controls"]:
        row = rows[old["grade"] - 1]
        need(
            row["characters"] == old["actual_characters"],
            "frozen primitive character mismatch",
        )
        need(
            row["multiplicities"] == old["multiplicities"],
            "frozen primitive multiplicity mismatch",
        )
    even_rows = []
    for n in range(2, 65, 2):
        row = rows[n - 1]
        a = anti_dimension(n)
        need(
            a == sum(row["multiplicities"][1:]),
            "independent odd-divisor formula failed",
        )
        j = n // 2
        error = Fraction(a) - Fraction(4**j, 4 * j)
        need(
            abs(error) <= error_bound(j), "proved remainder bound failed finite control"
        )
        even_rows.append(
            {
                "grade": n,
                "anti_dimension": a,
                "error": rational_pair(error),
                "error_bound": rational_pair(error_bound(j)),
            }
        )
    panels = []
    for field in (7, 49):
        for cap in (4, 8, 16, 32, 64):
            values = ladder_coefficients(field, cap, 64)
            need(
                values == logarithmic_coefficients(field, cap, 64),
                "independent coefficient recurrence mismatch",
            )
            panels.append(
                {
                    "field": field,
                    "grade_cap": cap,
                    "coefficient_cutoff": 64,
                    "coefficients": values,
                }
            )
    for cap in (4, 8, 16, 32):
        k7 = ladder_coefficients(7, cap, 64)
        k49 = ladder_coefficients(49, cap, 32)
        substituted = [k49[i // 2] if i % 2 == 0 else 0 for i in range(65)]
        need(
            substituted == multiply(k7, k7, 64),
            "correct grading base-change identity failed",
        )
        need(
            ladder_coefficients(49, cap, 64) != multiply(k7, k7, 64),
            "wrong fixed-variable control unexpectedly passed",
        )
        for field in (7, 49):
            initial = ladder_coefficients(field, cap, 64)
            later = ladder_coefficients(field, min(64, cap + 2), 64)
            need(initial[: cap + 2] == later[: cap + 2], "formal stabilization failed")
    # Tuples are converted to lists once here so strict JSON round trips are exact.
    payload = {
        "schema": "actual-graded-completion-v1",
        "source_commit": FREEZE,
        "source_blobs": PINS,
        "source_sha256": {name: digest(data) for name, data in sources.items()},
        "owned_sha256": {
            str(p.relative_to(ROOT)).replace("\\", "/"): digest(p.read_bytes())
            for p in OWNED
        },
        "source_even_grade_controls": even_rows,
        "actual_curves": point_counts(),
        "formal_coefficient_panels": panels,
        "critical_interval_panels": [
            critical_log_interval(field, n)
            for field in (7, 49)
            for n in (8, 16, 32, 64)
        ],
        "proved_analytically_not_by_replay": [
            "degreewise constructible algebra limit and full Euler stabilization",
            "odd-divisor formula for every even grade",
            "scalar radii, fractional branch, and full-source radii",
            "critical power law and Schatten thresholds",
        ],
        "not_claimed": [
            "full native decoder",
            "number-field transfer",
            "RH",
            "F49 enumeration",
            "infinite-rank constructible sheaf",
        ],
    }
    return json.loads(json.dumps(payload))


def check_payload(candidate: object) -> None:
    need(
        strict_equal(candidate, build_payload()),
        "strict primitive replay differs from artifact",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    need(args.write != args.check, "choose exactly one of --write and --check")
    if args.write:
        payload = build_payload()
        data = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
        need(len(data) <= MAX_BYTES, "artifact exceeds byte cap")
        FIXTURE.write_bytes(data)
        print(f"WROTE {FIXTURE.name}: {len(data)} bytes")
    else:
        data = FIXTURE.read_bytes()
        need(len(data) <= MAX_BYTES, "artifact exceeds byte cap")
        check_payload(json.loads(data))
        print(
            "PASS: frozen source, exact coefficients, base change and rational intervals"
        )


if __name__ == "__main__":
    main()
