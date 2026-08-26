#!/usr/bin/env python3
"""Prove the exact two-place law and cumulant defect in the quintic family.

The computation is symbolic coefficient algebra plus tiny exact sample rows.
It enumerates no polynomial family, curve, zero, or finite extension.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_two_place_cumulant_defect.json"
NOTE = HERE / "QUADRATIC_FAMILY_TWO_PLACE_CUMULANT_DEFECT.md"
TEST = ROOT / "tests" / "test_quadratic_family_two_place_cumulant_defect.py"
SOURCE_NOTE = HERE / "EULER_DETECTOR_RENORMALIZATION_FLOW.md"
SOURCE_COMMIT = "fe9ba35f67e39c5706cef79d2e7cefd07fce7d67"
SOURCE_BLOB = "e1740dd014cd0f43222b8ec73a09ee1374b7f3cc"
SCHEMA = "riemann.function_field.quadratic_family_two_place_cumulant_defect.v1"
MAX_SERIES_DEGREE = 5
MAX_SAMPLE_Q = 7
OPERATION_CAP = 20_000

Poly = tuple[int, ...]  # coefficients low to high in q


def _trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [0])


def _add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return _trim(
        tuple(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        )
    )


def _scale(poly: Poly, scalar: int) -> Poly:
    return _trim(tuple(scalar * value for value in poly))


def _mul(left: Poly, right: Poly) -> Poly:
    values = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            values[i + j] += a * b
    return _trim(tuple(values))


def _q_power(power: int) -> Poly:
    return (0,) * power + (1,)


def _series_product(*series: tuple[Poly, ...]) -> tuple[Poly, ...]:
    result = [(1,)] + [(0,)] * MAX_SERIES_DEGREE
    for factor in series:
        updated = [(0,)] * (MAX_SERIES_DEGREE + 1)
        for i, left in enumerate(result):
            for j, right in enumerate(factor):
                if i + j <= MAX_SERIES_DEGREE:
                    updated[i + j] = _add(updated[i + j], _mul(left, right))
        result = updated
    return tuple(result)


def _symbolic_coefficients() -> dict[str, Poly]:
    one_over_one_minus_qu = tuple(_q_power(index) for index in range(6))
    one_over_one_plus_u = tuple(((-1) ** index,) for index in range(6))
    one_over_one_plus_u_squared = tuple(
        (((-1) ** index) * (index + 1),) for index in range(6)
    )
    one_minus_qu2 = ((1,), (0,), (0, -1)) + ((0,),) * 3
    one_minus_u = ((1,), (-1,)) + ((0,),) * 4
    one_over_one_minus_u2 = tuple(
        (1,) if index % 2 == 0 else (0,) for index in range(6)
    )
    one_over_one_minus_u2_squared = tuple(
        ((index // 2 + 1),) if index % 2 == 0 else (0,) for index in range(6)
    )

    total = _series_product(one_minus_qu2, one_over_one_minus_qu)
    one_unramified = _series_product(
        one_minus_qu2, one_over_one_minus_qu, one_over_one_plus_u
    )
    two_unramified = _series_product(
        one_minus_qu2,
        one_over_one_minus_qu,
        one_over_one_plus_u_squared,
    )
    one_character = _series_product(one_minus_qu2, one_over_one_minus_u2)
    two_characters = _series_product(
        one_minus_u,
        one_minus_qu2,
        one_over_one_minus_u2_squared,
    )
    return {
        "A": total[5],
        "V": one_unramified[5],
        "W": two_unramified[5],
        "one_character_degree_5": one_character[5],
        "C": two_characters[5],
    }


def _poly_value(poly: Poly, q: int) -> int:
    return sum(coefficient * q**index for index, coefficient in enumerate(poly))


def scalar_rows(q: int, separation_sign: int = 1) -> dict[str, Fraction | int]:
    if q < 3 or q % 2 == 0:
        raise ValueError("q must be odd and at least three")
    if separation_sign not in {-1, 1}:
        raise ValueError("separation_sign must be +/-1")
    polynomials = _symbolic_coefficients()
    integers = {key: _poly_value(poly, q) for key, poly in polynomials.items()}
    if integers["one_character_degree_5"] != 0:
        raise ArithmeticError("one-place mean did not vanish")
    # In every finite field of odd cardinality q, chi(-1)=(-1)^((q-1)/2).
    epsilon = 1 if q % 4 == 1 else -1
    A = integers["A"]
    V = integers["V"]
    W = integers["W"]
    C = integers["C"]
    return {
        "q": q,
        "epsilon": epsilon,
        "s": separation_sign,
        "A": A,
        "V": V,
        "W": W,
        "C": C,
        "v": Fraction(V, A),
        "w": Fraction(W, A),
        "c": Fraction(C, A),
        "u": Fraction(separation_sign * (1 + epsilon) * C, A),
    }


def joint_counts(q: int, separation_sign: int = 1) -> dict[tuple[int, int], int]:
    rows = scalar_rows(q, separation_sign)
    epsilon = int(rows["epsilon"])
    s = separation_sign
    A, V, W, C = (int(rows[key]) for key in ("A", "V", "W", "C"))
    t_x2y = s * C
    t_xy2 = epsilon * s * C
    counts: dict[tuple[int, int], int] = {}
    for x in (-1, 1):
        for y in (-1, 1):
            numerator = W + y * t_x2y + x * t_xy2 + x * y * C
            if numerator % 4:
                raise ArithmeticError("nonintegral nonzero joint cell")
            counts[(x, y)] = numerator // 4
        numerator = V - W - x * t_xy2
        if numerator % 2:
            raise ArithmeticError("nonintegral x-axis joint cell")
        counts[(x, 0)] = numerator // 2
    for y in (-1, 1):
        numerator = V - W - y * t_x2y
        if numerator % 2:
            raise ArithmeticError("nonintegral y-axis joint cell")
        counts[(0, y)] = numerator // 2
    counts[(0, 0)] = A - 2 * V + W
    if min(counts.values()) < 0 or sum(counts.values()) != A:
        raise ArithmeticError("joint law failed positivity or total mass")
    return counts


def _moments_from_counts(
    counts: dict[tuple[int, int], int], order: int
) -> tuple[Fraction, Fraction]:
    total = sum(counts.values())
    local = Fraction(sum(count * x**order for (x, _), count in counts.items()), total)
    aggregate = Fraction(
        sum(count * (x + y) ** order for (x, y), count in counts.items()), total
    )
    return local, aggregate


def _cumulants(moments: dict[int, Fraction]) -> dict[int, Fraction]:
    cumulants: dict[int, Fraction] = {}
    # kappa_n = mu_n - sum_(j=1)^(n-1) binom(n-1,j-1) kappa_j mu_(n-j)
    from math import comb

    for n in range(1, 7):
        value = moments[n]
        for j in range(1, n):
            value -= Fraction(comb(n - 1, j - 1)) * cumulants[j] * moments[n - j]
        cumulants[n] = value
    return cumulants


def cumulant_defects(q: int, separation_sign: int = 1) -> dict[int, Fraction]:
    counts = joint_counts(q, separation_sign)
    local_moments = {0: Fraction(1)}
    aggregate_moments = {0: Fraction(1)}
    for order in range(1, 7):
        local, aggregate = _moments_from_counts(counts, order)
        local_moments[order] = local
        aggregate_moments[order] = aggregate
    local_kappa = _cumulants(local_moments)
    aggregate_kappa = _cumulants(aggregate_moments)
    return {
        order: aggregate_kappa[order] - 2 * local_kappa[order] for order in range(2, 7)
    }


def structural_defects(q: int, separation_sign: int = 1) -> dict[int, Fraction]:
    rows = scalar_rows(q, separation_sign)
    v, w, c, u = (rows[key] for key in ("v", "w", "c", "u"))
    if not all(isinstance(value, Fraction) for value in (v, w, c, u)):
        raise TypeError("expected exact rational rows")
    a = v + c
    return {
        2: 2 * c,
        3: 3 * u,
        4: 8 * c + 6 * w - 6 * v * v - 24 * v * c - 12 * c * c,
        5: 15 * u * (1 - 4 * a),
        6: (
            32 * c
            + 30 * w
            - 30 * a * (2 * v + 8 * c + 6 * w)
            - 90 * u * u
            + 240 * a**3
            + 30 * v * v
            - 60 * v**3
        ),
    }


def _pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _git_blob(path: Path, commit: str = "HEAD") -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def build_payload() -> dict[str, object]:
    symbolic = _symbolic_coefficients()
    expected = {
        "A": (0, 0, 0, 0, -1, 1),
        "V": (-1, 2, -2, 2, -2, 1),
        "W": (-6, 9, -7, 5, -3, 1),
        "one_character_degree_5": (0,),
        "C": (-3, 2),
    }
    if symbolic != expected:
        raise ArithmeticError(f"symbolic coefficient mismatch: {symbolic!r}")
    if _git_blob(SOURCE_NOTE, SOURCE_COMMIT) != SOURCE_BLOB:
        raise RuntimeError("renormalization-flow source blob drifted")

    samples: dict[str, object] = {}
    for q in (3, 5, 7):
        rows = scalar_rows(q)
        direct = cumulant_defects(q)
        structural = structural_defects(q)
        if direct != structural:
            raise ArithmeticError(f"cumulant reconstruction failed at q={q}")
        samples[str(q)] = {
            "epsilon": rows["epsilon"],
            "family_size": rows["A"],
            "joint_counts_s=1": {
                f"{x},{y}": count for (x, y), count in sorted(joint_counts(q).items())
            },
            "defects_orders_2_through_6": {
                str(order): _pair(value) for order, value in direct.items()
            },
        }

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_EXACT_FOR_EVERY_ODD_PRIME_POWER",
        "family": "monic squarefree quintics D over F_q",
        "places": "two distinct rational primes T-a and T-b",
        "variables": "X=chi(D(a)), Y=chi(D(b)) in {-1,0,1}",
        "orientation": "epsilon=chi(-1), s=chi(b-a)",
        "source": {
            "concept_note": SOURCE_NOTE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
        },
        "generating_functions": {
            "family": "(1-q*u^2)/(1-q*u)",
            "one_unramified": "(1-q*u^2)/((1-q*u)*(1+u))",
            "two_unramified": "(1-q*u^2)/((1-q*u)*(1+u)^2)",
            "one_character": "(1-q*u^2)/(1-u^2)",
            "two_characters": "(1-u)*(1-q*u^2)/(1-u^2)^2",
            "mixed_character_unramified": "(1-q*u^2)/((1-u^2)*(1+sigma*u))",
        },
        "degree_five_coefficients_low_to_high_in_q": {
            key: list(value) for key, value in symbolic.items()
        },
        "scalar_law": {
            "A": "q^4*(q-1)",
            "V": "q^5-2*q^4+2*q^3-2*q^2+2*q-1",
            "W": "q^5-3*q^4+5*q^3-7*q^2+9*q-6",
            "C": "2*q-3",
            "moments": {
                "E[X]=E[Y]": "0",
                "E[X^2]=E[Y^2]": "v=V/A",
                "E[X*Y]": "c=C/A",
                "E[X^2*Y]": "s*c",
                "E[X*Y^2]": "epsilon*s*c",
                "E[X^2*Y^2]": "w=W/A",
            },
        },
        "cumulant_defects": {
            "definition": "Delta_m=kappa_m(X+Y)-kappa_m(X)-kappa_m(Y)",
            "u": "s*(1+epsilon)*c",
            "Delta_2": "2*c",
            "Delta_3": "3*u",
            "Delta_4": "8*c+6*w-6*v^2-24*v*c-12*c^2",
            "Delta_5": "15*u*(1-4*(v+c))",
            "Delta_6": "32*c+30*w-30*(v+c)*(2*v+8*c+6*w)-90*u^2+240*(v+c)^3+30*v^2-60*v^3",
            "leading_q_to_infinity": {
                "Delta_2": "4*q^-4+O(q^-5)",
                "Delta_3": "6*s*(1+epsilon)*q^-4+O(q^-5)",
                "Delta_4": "-32*q^-4+O(q^-5)",
                "Delta_5": "-90*s*(1+epsilon)*q^-4+O(q^-5)",
                "Delta_6": "544*q^-4+O(q^-5)",
            },
        },
        "samples": samples,
        "resource_contract": {
            "series_degree": MAX_SERIES_DEGREE,
            "largest_sample_q": MAX_SAMPLE_Q,
            "operation_cap": OPERATION_CAP,
            "finite_field_enumeration": False,
            "curve_enumeration": False,
            "sampling": False,
        },
        "claim_boundary": [
            "The variables are rational-place Euler coefficients in one complete quadratic function-field family, not independent Haar variables.",
            "The q^-4 defects are fixed-degree squarefree-family coupling; no zero statistic, RH implication, or principal-member amplification is inferred.",
            "The result is an all-q theorem, not a recurrence fit to q=3,5,7.",
            "No external novelty claim is made.",
        ],
        "files": {
            "note": NOTE.relative_to(ROOT).as_posix(),
            "producer": Path(__file__).resolve().relative_to(ROOT).as_posix(),
            "test": TEST.relative_to(ROOT).as_posix(),
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(encoded).hexdigest()
    return payload


def _canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    rendered = _canonical_bytes(payload)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("canonical payload drift")
    else:
        OUTPUT.write_bytes(rendered)
    print(payload["payload_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
