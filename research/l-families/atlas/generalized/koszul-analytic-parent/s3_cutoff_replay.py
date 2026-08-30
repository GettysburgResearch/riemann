"""Native S3 whole-grade cutoff anomaly, with exact weighted logarithms."""

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
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
FREEZE = "e79a488982a339eddb512a3e2a384d0e38dc3e4d"
PINS = (
    (
        "s3_ramification_replay.py",
        "3652d5c02afb75723a92ad090f64e558f9c5943f",
        "de6cf92eb82827c92fecc24c66d4e49d8c5bd6557911dd2dadb78bd5be44a8b0",
    ),
    (
        "S3_RAMIFICATION_AND_GRADED_FAMILY.md",
        "ee4f04dbde2dabb6a7d36a820953f8c054e06e0e",
        "4861ad8b4a33b71b35026ff84a6fb81daa96d9e5b2e58d584f5316d8fe868e6e",
    ),
)
OWNED = (
    "S3_GRADE_CUTOFF_ANOMALY.md",
    "S3_CUTOFF_REPLAY.md",
    "s3_cutoff_replay.py",
    "tests/test_s3_cutoff.py",
)
FIXTURE = HERE / "s3_cutoff.verification.json"


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
        need(resolved == blob, "S3 cutoff dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "S3 cutoff dependency hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected,
            "working S3 cutoff dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_s3_source", HERE / "s3_ramification_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None, "cannot load authenticated S3 source"
)
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)
R = S.R


def exact(value: object) -> Fraction:
    need(
        isinstance(value, (int, Fraction)) and not isinstance(value, bool),
        "exact rational required",
    )
    value = Fraction(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 2048,
        "exact rational exceeds bit cap",
    )
    return value


def qjson(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def rounded(interval: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    low, high = interval
    need(low <= high, "reversed exact interval")
    grid = 10**15
    return Fraction((low * grid).numerator // (low * grid).denominator, grid), Fraction(
        -((-high * grid).numerator // (-high * grid).denominator), grid
    )


def interval_json(interval: tuple[Fraction, Fraction]) -> list[list[int]]:
    return [qjson(x) for x in rounded(interval)]


def weighted_log(value: Fraction, weight: int = 1) -> tuple[Fraction, Fraction]:
    value = exact(value)
    need(
        isinstance(weight, int)
        and not isinstance(weight, bool)
        and abs(weight).bit_length() <= 512,
        "bounded integer log weight required",
    )
    need(Fraction(1, 8) <= value <= 8, "bounded positive log argument required")
    if weight == 0 or value == 1:
        return Fraction(0), Fraction(0)
    v = (value - 1) / (value + 1)
    power = v
    middle = Fraction(0)
    for j in range(96):
        middle += 2 * weight * power / (2 * j + 1)
        power *= v * v
        error = 2 * abs(weight * power) / ((2 * j + 3) * (1 - v * v))
        if error <= Fraction(1, 10**20):
            return rounded((middle - error, middle + error))
    raise ValueError("weighted logarithm could not meet its certified error cap")


def mobius(n: int) -> int:
    R.integer(n, 1, 256)
    return _mobius(n)


@cache
def _mobius(n: int) -> int:
    count, divisor, remaining = 0, 2, n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            count += 1
            if remaining % divisor == 0:
                return 0
        divisor += 1
    return (-1) ** (count + int(remaining > 1))


def source_grade(n: int, order: int) -> tuple[int, int, tuple[int, ...]]:
    R.integer(n, 1, 256)
    R.integer(order, 2, 3)
    return _source_grade(n, order)


@cache
def _source_grade(n: int, order: int) -> tuple[int, int, tuple[int, ...]]:
    numerator = (-1) ** (n + 1) * sum(
        mobius(r) * (4 + (-1) ** (n // r + 1) * 2 ** (n // r))
        for r in range(1, n + 1)
        if n % r == 0
    )
    need(
        numerator >= 0 and numerator % n == 0,
        "source dimension is not a nonnegative integer",
    )
    dimension = numerator // n
    character = 0
    if n % order == 0:
        m = n // order
        numerator = (-1) ** n * sum(
            mobius(r) * ((-1) ** (m // r + 1) * 2 ** (m // r) + int(order == 3))
            for r in range(1, m + 1)
            if m % r == 0 and r % order != 0
        )
        need(numerator % n == 0, "source S3 character is nonintegral")
        character = numerator // n
    numerators = (
        (dimension + character, dimension - character)
        if order == 2
        else (dimension + 2 * character, dimension - character, dimension - character)
    )
    need(
        all(x >= 0 and x % order == 0 for x in numerators),
        "source eigenmultiplicities are not genuine",
    )
    eigen = tuple(x // order for x in numerators)
    need(sum(eigen) == dimension, "source eigenmultiplicities lost dimension")
    return dimension, character, eigen


def logarithm(sequence: tuple[int, ...]) -> list[Fraction]:
    need(
        1 <= len(sequence) <= 25 and sequence[0] == 1,
        "normalized bounded series required",
    )
    need(
        all(
            isinstance(value, int) and not isinstance(value, bool) for value in sequence
        ),
        "integer source series required",
    )
    out = [Fraction(0)] * len(sequence)
    for n in range(1, len(sequence)):
        out[n] = (
            Fraction(sequence[n])
            - sum((j * out[j] * sequence[n - j] for j in range(1, n)), Fraction(0)) / n
        )
    return out


def character_control() -> dict[str, object]:
    sequences = S.source_sequences(24)
    logs = {kind: logarithm(sequence) for kind, sequence in sequences.items()}
    for n in range(1, 25):
        for order, kind in ((2, "s"), (3, "c")):
            expected = (-1) ** (n + 1) * sum(
                (
                    Fraction(mobius(r), r) * logs[S.power_class(kind, r)][n // r]
                    for r in range(1, n + 1)
                    if n % r == 0
                ),
                Fraction(0),
            )
            need(
                expected == source_grade(n, order)[1],
                "explicit source character disagrees with full Adams inversion",
            )
    for n in range(1, 65):
        need(
            source_grade(n, 2)[0] == R.multiplicity(n),
            "extended source dimensions disagree with frozen parent",
        )
    low = S.native_low_lie()
    for n in (1, 2, 3):
        need(
            source_grade(n, 2)[1] == low[n - 1][1]
            and source_grade(n, 3)[1] == low[n - 1][2],
            "actual low Lie quotient disagrees with character formula",
        )
    # Full PBW log, including genuine source Adams powers at every k.
    for order, kind in ((2, "s"), (3, "c")):
        for degree in range(1, 25):
            value = Fraction(0)
            for n in range(1, degree + 1):
                if degree % n:
                    continue
                k = degree // n
                dimension, character, _ = source_grade(n, order)
                trace = dimension if k % order == 0 else character
                value += Fraction((-1) ** (n + 1) * trace, k)
            need(
                value == logs[kind][degree],
                "full native PBW block log disagrees with rational source",
            )
    return {
        "source_Adams_and_PBW_degree": 24,
        "frozen_dimension_comparison_degree": 64,
        "eigenmultiplicity_coverage": 256,
        "sample_source_grades": [
            {
                "grade": n,
                "order": d,
                "dimension_character_eigenmultiplicities": [
                    source_grade(n, d)[0],
                    source_grade(n, d)[1],
                    list(source_grade(n, d)[2]),
                ],
            }
            for n in (*range(1, 13), 64, 128, 255, 256)
            for d in (2, 3)
        ],
    }


def finite_log(
    order: int, cut: int, x: Fraction = Fraction(-1, 2)
) -> tuple[Fraction, Fraction]:
    R.integer(order, 2, 3)
    R.integer(cut, 2, 256)
    x = exact(x)
    need(
        Fraction(-3, 5) <= x <= Fraction(3, 5),
        "source t^d outside bounded block domain",
    )
    return _finite_log(order, cut, x)


@cache
def _finite_log(order: int, cut: int, x: Fraction) -> tuple[Fraction, Fraction]:
    total = Fraction(0), Fraction(0)
    for n in range(1, cut + 1):
        dimension, character, eigen = source_grade(n, order)
        sign = (-1) ** n
        if n % order:
            need(
                character == 0 and dimension % order == 0,
                "nonmultiple grade lost full root-of-unity orbits",
            )
            terms = (weighted_log(1 - x**n, sign * (dimension // order)),)
        else:
            u = x ** (n // order)
            if order == 2:
                terms = (
                    weighted_log(1 - u, sign * eigen[0]),
                    weighted_log(1 + u, sign * eigen[1]),
                )
            else:
                terms = (
                    weighted_log(1 - u, sign * eigen[0]),
                    weighted_log(1 + u + u * u, sign * eigen[1]),
                )
        for interval in terms:
            total = total[0] + interval[0], total[1] + interval[1]
    return rounded(total)


def finite_band(order: int, cut: int, x: Fraction) -> Fraction:
    R.integer(order, 2, 3)
    R.integer(cut, 2, 256)
    x = exact(x)
    need(abs(x) <= Fraction(3, 5), "bounded band parameter required")
    return (
        sum(((-2 * x) ** n / n for n in range(cut // order + 1, cut + 1)), Fraction(0))
        / order
    )


def error_bound(
    order: int, cut: int, x: Fraction, radius: Fraction, eta: Fraction
) -> Fraction:
    R.integer(order, 2, 3)
    R.integer(cut, 2, 256)
    x, radius, eta = exact(x), exact(radius), exact(eta)
    need(
        abs(x) <= radius**order and 0 < radius < eta < 1,
        "rational radius does not bound the source point",
    )
    need(
        2 * eta ** (order + 1) < 1,
        "outer Cauchy circle exceeds the proved remainder disk",
    )
    a = eta**order
    need(
        2 * a * a < 1 and 2 * eta**6 < 1, "source remainder denominator is not positive"
    )
    ce = 4 * a / (1 - a) + 6 * a * a / ((1 - a) * (1 - 2 * a * a))
    if order == 2:
        cg = eta**6 / ((1 - eta**2) * (1 - 2 * eta**6))
    else:
        cg = eta**3 / (3 * (1 - eta**3)) + eta**6 / ((1 - eta**3) * (1 - 2 * eta**6))
    ratio = radius / eta
    error = cg * ratio ** (cut + 1) / (1 - ratio)
    u_ratio = abs(x) / a
    error += ce * u_ratio ** (cut + 1) / (order * (1 - u_ratio))
    if order == 3:
        b = eta**2
        cp = b**3 / ((1 - b**3) * (1 - 2 * b**3))
        error += cp * ratio ** (2 * cut + 2) / (2 * (1 - ratio * ratio))
    tail = 2 * radius ** (order + 1)
    error += 3 * tail ** (cut + 1) / ((order + 1) * (1 - radius) * (1 - tail))
    return error


def cutoff_control(
    order: int, cut: int, x: Fraction = Fraction(-1, 2)
) -> dict[str, object]:
    x = exact(x)
    if order == 2 and abs(x) <= Fraction(1, 2):
        radius, eta = Fraction(5, 7), Fraction(3, 4)
    elif order == 2:
        radius, eta = Fraction(3, 4), Fraction(7, 9)
    else:
        radius, eta = Fraction(4, 5), Fraction(5, 6)
    observed = finite_log(order, cut, x)
    band = finite_band(order, cut, x)
    corrected = observed[0] + band, observed[1] + band
    source = (1 - x) ** (-2 if order == 2 else -1)
    reference = weighted_log(source)
    error = error_bound(order, cut, x, radius, eta)
    need(
        corrected[0] <= reference[1] + error and corrected[1] >= reference[0] - error,
        "native whole-grade cutoff contradicts the proved finite-band error",
    )
    result = {
        "order": order,
        "cut": cut,
        "source_t_power_d": qjson(x),
        "rational_radius_eta": [qjson(radius), qjson(eta)],
        "native_finite_log": interval_json(observed),
        "finite_band_correction": qjson(band),
        "corrected_log": interval_json(corrected),
        "rational_source_F": qjson(source),
        "source_log": interval_json(reference),
        "proved_absolute_log_error": qjson(error),
        "source_operator_trace_class": abs(x) < Fraction(1, 2) ** order,
    }
    if x == Fraction(-1, 2):
        log_d = weighted_log(Fraction(order))
        limit = reference[0] - log_d[1] / order, reference[1] - log_d[0] / order
        result["anomalous_limit_log"] = interval_json(limit)
        result["Abel_limit_differs"] = True
    return result


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    S.authenticate_frozen()
    R.authenticate()
    # Validate every compressed eigenspace row, not just the displayed sample.
    for n in range(1, 257):
        for order in (2, 3):
            source_grade(n, order)
    return {
        "schema": "native-s3-grade-cutoff-anomaly-v1",
        "provenance": {
            "frozen_S3_source": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "source_characters": character_control(),
        "critical_controls": [
            cutoff_control(d, cut) for d in (2, 3) for cut in (128, 255, 256)
        ],
        "exterior_ray_controls": [
            cutoff_control(d, cut, x)
            for d, magnitude in ((2, Fraction(9, 16)), (3, Fraction(64, 125)))
            for x in (-magnitude, magnitude)
            for cut in (255, 256)
        ],
        "arithmetic": "bounded exact integers and weighted rational atanh intervals, no expanded eigenvalue list",
        "not_machine_proved": [
            "maximal locally uniform product disk",
            "all-point boundary classification on its first circle",
            "compact-complex 1/N transition profile",
            "exterior subsequence limits",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "S3 cutoff fixture differs from authenticated complete replay",
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
            "S3 cutoff fixture differs from complete replay",
        )
    print("PASS native S3 grade-cutoff anomaly exact replay")


if __name__ == "__main__":
    main()
