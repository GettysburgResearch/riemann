"""Exact bounded controls for mixed-rank growth and source regularization.

The Lie algebra is not replaced by fitted diagonal operators. Small
equivariant regularized-log controls use the frozen native Lie quotients.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "4c04db224fedde5d589f05f7183e004a67441a9c"
PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    (
        "replay.py",
        "08090ed1e35c1d20ce2f65c710007406b7419771",
        "9bebf69c2f022897af9bd22dba2022b88799ff91ff8288da9e45743000aa9e63",
    ),
    (
        "MATHEMATICS.md",
        "02d8cda2a0c50876d378eb1eeb29df85b3b096b3",
        "db2ca0196edab3f3c7ef52af3f6c30e61023f3a0080c1285d7fdb6c8844a915c",
    ),
)
OWNED = (
    "MIXED_RANKS_AND_REGULARIZATION.md",
    "REGULARIZATION_REPLAY.md",
    "regularization_replay.py",
    "tests/test_regularization.py",
)
FIXTURE = HERE / "regularization.verification.json"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for name, blob, expected_hash in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", FREEZE + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "frozen source blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected_hash, "frozen source hash mismatch")
        need(
            digest((HERE / name).read_bytes()) == expected_hash,
            "working source hash mismatch",
        )


authenticate_frozen()  # authenticate before importing executable source
SPEC = importlib.util.spec_from_file_location(
    "frozen_koszul23_replay", HERE / "replay.py"
)
need(SPEC is not None and SPEC.loader is not None, "cannot load authenticated replay")
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def profile(ranks: object) -> tuple[int, ...]:
    need(
        isinstance(ranks, tuple) and 1 <= len(ranks) <= 4,
        "rank tuple of length 1..4 required",
    )
    for rank in ranks:
        R.integer(rank, 1, 5)
    need(sum(rank - 1 for rank in ranks) <= 10, "total rank excess exceeds cap")
    return ranks


def identity_coefficients(ranks: object, degree: int) -> list[int]:
    ranks = profile(ranks)
    R.integer(degree, 0, 24)
    return [
        math.prod(math.comb(n + rank - 1, rank - 1) for rank in ranks)
        for n in range(degree + 1)
    ]


def numerator_difference(ranks: object) -> list[int]:
    ranks = profile(ranks)
    exponent = 1 + sum(rank - 1 for rank in ranks)
    sequence = identity_coefficients(ranks, exponent)
    out = [
        sum((-1) ** j * math.comb(exponent, j) * sequence[n - j] for j in range(n + 1))
        for n in range(exponent + 1)
    ]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def numerator_differential(ranks: object) -> list[int]:
    ranks = profile(ranks)
    excess = sorted((rank - 1 for rank in ranks), reverse=True)
    denominator = excess[0] + 1
    out = [Fraction(1)]
    for a in excess[1:]:
        for step in range(1, a + 1):
            new = [Fraction(0)] * (len(out) + 1)
            for n, coefficient in enumerate(out):
                new[n] += (step + n) * coefficient / step
                new[n + 1] += (denominator - step - n) * coefficient / step
            out = new
            denominator += 1
    need(all(value.denominator == 1 for value in out), "numerator is not integral")
    return [int(value) for value in out]


def logarithm_coefficients(sequence: list[int]) -> list[Fraction]:
    need(
        1 <= len(sequence) <= 25 and sequence[0] == 1,
        "normalized bounded series required",
    )
    need(
        all(
            isinstance(value, int) and not isinstance(value, bool) for value in sequence
        ),
        "integer coefficient sequence required",
    )
    out = [Fraction(0)] * len(sequence)
    for n in range(1, len(sequence)):
        out[n] = (
            Fraction(sequence[n])
            - sum((j * out[j] * sequence[n - j] for j in range(1, n)), Fraction(0)) / n
        )
    return out


def deviations(ranks: object, degree: int = 24) -> list[int]:
    R.integer(degree, 1, 24)
    logs = logarithm_coefficients(identity_coefficients(ranks, degree))
    out = []
    for n in range(1, degree + 1):
        value = (-1) ** (n + 1) * sum(
            R.mobius(d) * logs[n // d] / d for d in range(1, n + 1) if n % d == 0
        )
        need(
            value.denominator == 1 and value >= 0,
            "deviation integrality/positivity failed",
        )
        out.append(int(value))
    return out


def finite_profile(ranks: object) -> bool:
    active = tuple(rank for rank in profile(ranks) if rank > 1)
    return len(active) <= 1 or active == (2, 2)


def mixed_control(ranks: object) -> dict[str, object]:
    ranks = profile(ranks)
    numerator = numerator_difference(ranks)
    need(
        numerator == numerator_differential(ranks),
        "independent Hilbert numerators disagree",
    )
    a = sum(rank - 1 for rank in ranks)
    largest = max(rank - 1 for rank in ranks)
    degree = a - largest
    need(len(numerator) == degree + 1, "numerator degree is wrong")
    h1 = math.prod(ranks) - a - 1
    if not finite_profile(ranks):
        need(h1 > degree, "largest-root growth witness missing")
    result = {
        "ranks": list(ranks),
        "numerator": numerator,
        "denominator_exponent": a + 1,
        "h1": h1,
        "finite_parent": finite_profile(ranks),
        "deviations_through_24": deviations(ranks),
    }
    if len(ranks) == 2 and min(ranks) == 2 and max(ranks) >= 3:
        result["exact_trace_class_radius"] = [1, max(ranks) - 1]
    return result


def a_coefficient(p: int, index: int) -> int:
    R.integer(p, 2, 6)
    R.integer(index, 1, 64)
    return sum(R.mobius(index // k) for k in range(1, p) if index % k == 0)


def scale(value, factor):
    return value[0] * factor, value[1] * factor


def gaussian_log(sequence):
    need(
        1 <= len(sequence) <= 25 and sequence[0] == R.ONE,
        "normalized Gaussian series required",
    )
    out = [R.ZERO] * len(sequence)
    for n in range(1, len(sequence)):
        correction = R.ZERO
        for j in range(1, n):
            correction = R.add(
                correction, scale(R.mul(out[j], sequence[n - j]), Fraction(j, n))
            )
        out[n] = R.add(sequence[n], R.neg(correction))
    return out


def adams_control(a: object, b: object, p: int) -> dict[str, object]:
    a, b = R.unitary_roots(a, 2), R.unitary_roots(b, 3)
    R.integer(p, 2, 6)
    degree = 3 * p
    direct = [R.ZERO] * (degree + 1)
    for n in (1, 2, 3):
        weights = R.source_grade(n)[2]
        for j in range(p, degree // n + 1):
            aj = tuple(R.power(root, j) for root in a)
            bj = tuple(R.power(root, j) for root in b)
            trace = R.character(weights, aj, bj)
            direct[n * j] = R.add(
                direct[n * j], scale(trace, Fraction((-1) ** (n + 1), j))
            )
    transformed = [R.ZERO] * (degree + 1)
    for index in range(p, degree + 1):
        ai = tuple(R.power(root, index) for root in a)
        bi = tuple(R.power(root, index) for root in b)
        limit = degree // index
        ha, hb = R.complete_symmetric(ai, limit), R.complete_symmetric(bi, limit)
        logs = gaussian_log([R.mul(x, y) for x, y in zip(ha, hb, strict=True)])
        for j in range(1, limit + 1):
            transformed[index * j] = R.add(
                transformed[index * j],
                scale(logs[j], Fraction(-a_coefficient(p, index), index)),
            )
    need(direct == transformed, "native Lie-block and Adams regularizations disagree")
    return {
        "p": p,
        "through_degree": degree,
        "highest_source_Lie_grade": 3,
        "a": [R.gjson(root) for root in a],
        "b": [R.gjson(root) for root in b],
        "regularized_log_coefficients": [R.gjson(value) for value in direct],
    }


def direct_log_interval(
    t: int | Fraction, p: int, grade_cut: int = 24, power_cut: int = 24
):
    t = R.rational(t)
    R.integer(p, 2, 6)
    R.integer(grade_cut, 1, 32)
    R.integer(power_cut, p, 32)
    radius = abs(t)
    need(radius < 1 and 2 * radius**p < 1, "strict Schatten-p domain required")
    middle = sum(
        Fraction((-1) ** (n + 1) * R.multiplicity(n), j) * t ** (n * j)
        for n in range(1, grade_cut + 1)
        for j in range(p, power_cut + 1)
    )
    grade_error = (
        3
        * (2 * radius**p) ** (grade_cut + 1)
        / (p * (1 - radius) * (1 - 2 * radius**p))
    )
    power_error = (
        6
        * radius ** (power_cut + 1)
        / ((power_cut + 1) * (1 - radius) * (1 - 2 * radius ** (power_cut + 1)))
    )
    error = grade_error + power_error
    return middle - error, middle + error


def adams_log_interval(
    t: int | Fraction, p: int, adams_cut: int = 24, log_cut: int = 24
):
    t = R.rational(t)
    R.integer(p, 2, 6)
    R.integer(adams_cut, p, 32)
    R.integer(log_cut, 1, 32)
    radius = abs(t)
    need(radius < 1 and 2 * radius**p < 1, "strict Schatten-p domain required")
    middle, error = Fraction(0), Fraction(0)
    for index in range(p, adams_cut + 1):
        weight = Fraction(-a_coefficient(p, index), index)
        z = t**index
        middle += weight * sum(
            Fraction(4 + (-1) ** (j + 1) * 2**j, j) * z**j
            for j in range(1, log_cut + 1)
        )
        error += (
            abs(weight)
            * 3
            * (2 * abs(z)) ** (log_cut + 1)
            / ((log_cut + 1) * (1 - 2 * abs(z)))
        )
    error += (
        6
        * (p - 1)
        * radius ** (adams_cut + 1)
        / ((adams_cut + 1) * (1 - radius) * (1 - 2 * radius**p))
    )
    return middle - error, middle + error


def interval_control(t: int | Fraction, p: int) -> dict[str, object]:
    t = R.rational(t)
    direct = direct_log_interval(t, p)
    adams = adams_log_interval(t, p)
    need(
        max(direct[0], adams[0]) <= min(direct[1], adams[1]),
        "rigorous log enclosures are disjoint",
    )
    return {
        "t": R.qjson(t),
        "p": p,
        "ordinary_trace_class": abs(t) < Fraction(1, 2),
        "source_scalar": R.qjson((1 + 2 * t) / (1 - t) ** 4),
        "direct_log_interval": [R.qjson(value) for value in direct],
        "Adams_log_interval": [R.qjson(value) for value in adams],
        "cuts": {
            "grades": 24,
            "block_powers": 24,
            "Adams_indices": 24,
            "scalar_log_powers": 24,
        },
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    old = R.authenticate()  # also binds the old all-rank interlacing theorem
    profiles = (
        (1,),
        (4,),
        (1, 4, 1),
        (2, 2),
        (1, 2, 2, 1),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 3),
        (2, 2, 2),
        (2, 3, 3),
        (3, 4, 4),
    )
    torus = ((R.ONE, R.I), (R.ONE, R.neg(R.ONE), R.I))
    return {
        "schema": "mixed-koszul-canonical-regularization-v1",
        "provenance": {
            "frozen_source_commit": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "all_rank_precursor": old["precursor_commit"],
            "all_rank_precursor_sha256_lf": old["precursor_sha256_lf"],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "arithmetic": "integers, fractions and Gaussian fractions; no floats",
        "coverage": "named profiles, complete source Lie degrees 1..3, finite exact log enclosures using proved infinite tail bounds",
        "mixed_profiles": [mixed_control(ranks) for ranks in profiles],
        "Adams_coefficients": {
            str(p): [a_coefficient(p, n) for n in range(1, 33)] for p in range(2, 7)
        },
        "source_Adams_controls": [adams_control(*torus, p) for p in (2, 3, 4, 6)],
        "beyond_trace_class_controls": [
            interval_control(t, p)
            for t, p in ((Fraction(3, 5), 2), (Fraction(-1, 2), 2), (Fraction(3, 4), 3))
        ],
        "not_machine_proved": [
            "all-rank root simplicity and multiplicity asymptotic",
            "infinite exact determinant identities",
            "counterterm monodromy",
            "an all-parameter arithmetic or functional equation statement",
        ],
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "companion fixture differs from authenticated complete replay",
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
            "companion fixture differs from complete replay",
        )
    print("PASS mixed-rank canonical regularization exact replay")


if __name__ == "__main__":
    main()
