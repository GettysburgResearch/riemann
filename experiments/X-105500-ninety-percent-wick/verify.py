#!/usr/bin/env python3
"""Exact replay for T-105500.

The checker uses only the Python standard library and exact Fraction
arithmetic.  It authenticates finite algebra and rational constants; it does
not prove the analytic Xi transfer.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence

VERDICT = "PASS_T105500_SECOND_CHAOS_NINETY_PERCENT_FRONTIER"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "README_105500.md",
    "PR_BODY_105500_ADDENDUM.md",
    "PACKET_METADATA_105500.json",
    "claims/lemmas/L-105500-confluent-cauchy-index-full-signature.md",
    "claims/lemmas/L-105501-second-chaos-wick-density.md",
    "claims/lemmas/L-105502-second-chaos-wick-rank-reserve.md",
    "claims/refutations/R-105500-positive-index-nuisance-ceiling.md",
    "claims/theorems/T-105500-ninety-percent-wick-pick-frontier.md",
    "claims/methodology/M-105500-hostile-review-contract.md",
    "standalone/2026-08-24-ninety-percent-wick-pick/PROOF.md",
    "reports/gpt56-pro/2026-08-24-ninety-percent-wick-pick.md",
    "experiments/X-105500-ninety-percent-wick/README.md",
    "experiments/X-105500-ninety-percent-wick/replay.sh",
    "experiments/X-105500-ninety-percent-wick/verify.py",
    "experiments/X-105500-ninety-percent-wick/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# Exact polynomial arithmetic and finite full-signature regression.
# Coefficients are low degree first.
# ---------------------------------------------------------------------------

def trim(p: Sequence[F]) -> list[F]:
    out = list(p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a: Sequence[F], b: Sequence[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def poly_derivative(p: Sequence[F]) -> list[F]:
    return trim([F(i) * p[i] for i in range(1, len(p))] or [F(0)])


def poly_eval(p: Sequence[F], x: F) -> F:
    value = F(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def poly_divmod(a: Sequence[F], b: Sequence[F]) -> tuple[list[F], list[F]]:
    dividend = trim(a)
    divisor = trim(b)
    if divisor == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(dividend) < len(divisor):
        return [F(0)], dividend
    quotient = [F(0)] * (len(dividend) - len(divisor) + 1)
    remainder = dividend[:]
    while len(remainder) >= len(divisor) and remainder != [0]:
        offset = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[offset] = coefficient
        for j, value in enumerate(divisor):
            remainder[j + offset] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def poly_gcd(a: Sequence[F], b: Sequence[F]) -> list[F]:
    left, right = trim(a), trim(b)
    while right != [0]:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    lead = left[-1]
    return [value / lead for value in left]


def reduced_residue_hankel(p: Sequence[F]) -> tuple[list[list[F]], int]:
    """Return the full reduced F/F' residue form in a monomial basis.

    Common factors are cancelled exactly.  Expanding the reduced quotient at
    infinity gives the Hankel moment matrix congruent to the direct sum of all
    finite principal-part blocks.
    """
    derivative = poly_derivative(p)
    common = poly_gcd(p, derivative)
    numerator, rem_p = poly_divmod(p, common)
    denominator, rem_q = poly_divmod(derivative, common)
    require(rem_p == [0] and rem_q == [0], "gcd cancellation")
    require(len(numerator) == len(denominator) + 1, "reduced degree")
    dimension = len(denominator) - 1
    if dimension == 0:
        return [], 0

    numerator_rev = list(reversed(numerator))
    denominator_rev = list(reversed(denominator))
    series: list[F] = []
    q0 = denominator_rev[0]
    for n in range(2 * dimension + 1):
        primitive = numerator_rev[n] if n < len(numerator_rev) else F(0)
        correction = sum(
            (
                denominator_rev[j] * series[n - j]
                for j in range(1, min(n, len(denominator_rev) - 1) + 1)
            ),
            F(0),
        )
        series.append((primitive - correction) / q0)

    matrix = [
        [-series[i + j + 2] for j in range(dimension)]
        for i in range(dimension)
    ]
    return matrix, dimension


def symmetric_inertia(matrix: Sequence[Sequence[F]]) -> tuple[int, int, int]:
    """Exact symmetric elimination with one- and two-dimensional pivots."""
    a = [list(row) for row in matrix]
    positive = negative = zero = 0
    while a:
        n = len(a)
        diagonal = next((i for i in range(n) if a[i][i] != 0), None)
        if diagonal is not None:
            a[0], a[diagonal] = a[diagonal], a[0]
            for row in a:
                row[0], row[diagonal] = row[diagonal], row[0]
            pivot = a[0][0]
            if pivot > 0:
                positive += 1
            else:
                negative += 1
            vector = [a[i][0] for i in range(1, n)]
            a = [
                [
                    a[i + 1][j + 1] - vector[i] * vector[j] / pivot
                    for j in range(n - 1)
                ]
                for i in range(n - 1)
            ]
            continue

        pair: tuple[int, int] | None = None
        for i in range(n):
            for j in range(i + 1, n):
                if a[i][j] != 0:
                    pair = (i, j)
                    break
            if pair is not None:
                break
        if pair is None:
            zero += n
            break

        i, j = pair
        order = [i, j] + [k for k in range(n) if k not in (i, j)]
        a = [[a[r][c] for c in order] for r in order]
        off_diagonal = a[0][1]
        positive += 1
        negative += 1
        reduced: list[list[F]] = []
        for r in range(2, n):
            row: list[F] = []
            for c in range(2, n):
                correction = (
                    a[r][0] * a[1][c] + a[r][1] * a[0][c]
                ) / off_diagonal
                row.append(a[r][c] - correction)
            reduced.append(row)
        a = reduced
    return positive, negative, zero


def sign_variation_pair(p: Sequence[F], x: F) -> int:
    derivative = poly_derivative(p)
    return int(poly_eval(p, x) * poly_eval(derivative, x) < 0)


def sturm_sequence(p: Sequence[F]) -> list[list[F]]:
    common = poly_gcd(p, poly_derivative(p))
    squarefree, remainder = poly_divmod(p, common)
    require(remainder == [0], "squarefree quotient")
    sequence = [squarefree, poly_derivative(squarefree)]
    while sequence[-1] != [0]:
        _, rem = poly_divmod(sequence[-2], sequence[-1])
        if rem == [0]:
            break
        sequence.append([-value for value in rem])
    return sequence


def sign_changes(values: Iterable[F]) -> int:
    signs = [1 if value > 0 else -1 for value in values if value != 0]
    return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))


def distinct_root_count(p: Sequence[F], a: F, b: F) -> int:
    sequence = sturm_sequence(p)
    return sign_changes(poly_eval(q, a) for q in sequence) - sign_changes(
        poly_eval(q, b) for q in sequence
    )


def linear_factor(root: int) -> list[F]:
    return [-F(root), F(1)]


def quadratic_factor(a: int, b: int, c: int) -> list[F]:
    return [F(c), F(b), F(a)]


def check_signature_identity(p: Sequence[F], a: F, b: F) -> None:
    derivative = poly_derivative(p)
    require(poly_eval(p, a) != 0 and poly_eval(p, b) != 0, "root endpoint")
    require(
        poly_eval(derivative, a) != 0 and poly_eval(derivative, b) != 0,
        "critical endpoint",
    )
    matrix, dimension = reduced_residue_hankel(p)
    pos, neg, null = symmetric_inertia(matrix)
    require(pos + neg + null == dimension, "inertia dimension")
    require(null == 0, "reduced residue form nondegenerate")
    expected = distinct_root_count(p, a, b)
    actual = (
        pos
        - neg
        + sign_variation_pair(p, a)
        - sign_variation_pair(p, b)
    )
    require(actual == expected, f"signature/root mismatch: {actual} != {expected}")


def full_signature_regression() -> dict[str, int]:
    structured = 0
    roots = [-2, -1, 0, 1, 2]
    for count in range(4):
        for selected in combinations(roots, count):
            for multiplicities in product(range(1, 5), repeat=count):
                base = [F(1)]
                for root, multiplicity in zip(selected, multiplicities):
                    for _ in range(multiplicity):
                        base = poly_mul(base, linear_factor(root))
                for first_nonreal in range(3):
                    for second_nonreal in range(2):
                        polynomial = base[:]
                        for _ in range(first_nonreal):
                            polynomial = poly_mul(
                                polynomial, quadratic_factor(1, 0, 1)
                            )
                        for _ in range(second_nonreal):
                            polynomial = poly_mul(
                                polynomial, quadratic_factor(1, 1, 1)
                            )
                        if len(polynomial) <= 1:
                            continue
                        check_signature_identity(polynomial, F(-4), F(4))
                        structured += 1

    generator = random.Random(105500)
    random_cases = 0
    for degree in range(1, 9):
        for _ in range(500):
            polynomial = [F(generator.randint(-4, 4)) for _ in range(degree)]
            polynomial.append(F(generator.choice([-3, -2, -1, 1, 2, 3])))
            check_signature_identity(polynomial, F(-7), F(7))
            random_cases += 1

    require(structured == 4925, "structured regression count")
    require(random_cases == 4000, "random regression count")
    return {
        "structured_multiplicity_nonreal_cases": structured,
        "seeded_random_sturm_cases": random_cases,
        "total_exact_cases": structured + random_cases,
    }


# ---------------------------------------------------------------------------
# Exact K=2 Wick algebra and rational ninety-percent bridge.
# ---------------------------------------------------------------------------

def wick2_coefficients(maximum_degree: int = 30) -> list[F]:
    coefficients = [F(0)] * (maximum_degree + 1)
    coefficients[0] = F(1)
    for m in range(1, maximum_degree + 1):
        coefficients[m] = sum(
            (coefficients[m - j] for j in range(3, m + 1)), F(0)
        ) / m
    return coefficients


def wick2_algebra_checks() -> dict[str, object]:
    coefficients = wick2_coefficients(30)
    require(
        coefficients[:6] == [F(1), F(0), F(0), F(1, 3), F(1, 4), F(1, 5)],
        "degree-two cancellation coefficients",
    )
    require(all(F(0) <= value <= F(1) for value in coefficients), "coefficient bounds")
    for m in range(1, len(coefficients)):
        require(
            m * coefficients[m]
            == sum((coefficients[m - j] for j in range(3, m + 1)), F(0)),
            "coefficient recurrence",
        )
    return {
        "maximum_degree": 30,
        "first_coefficients": [str(value) for value in coefficients[:12]],
        "degree_one_cancelled": coefficients[1] == 0,
        "degree_two_cancelled": coefficients[2] == 0,
    }


def energy_bound_checks() -> dict[str, str]:
    coefficients = wick2_coefficients(30)
    energies = [
        coefficients[m] ** 2 * F(math.factorial(m), math.factorial(2 * m))
        for m in range(3, 31)
    ]
    require(
        energies[:3] == [F(1, 1080), F(1, 26880), F(1, 756000)],
        "first energy terms",
    )
    tail = F(13, 8316000)
    bound = sum(energies[:3], F(0)) + tail
    require(bound == F(9181, 9504000), "rational energy bound")
    require(sum(energies) < bound < F(1, 1000), "energy inequalities")
    return {
        "m3": "1/1080",
        "m4": "1/26880",
        "m5": "1/756000",
        "m_ge_6_tail": str(tail),
        "rational_upper": str(bound),
        "target_upper": "1/1000",
    }


def ninety_percent_checks() -> dict[str, str]:
    old_ceiling = F(1) - F(821, 5000)
    impossible_eta = (F(9, 10) + F(1) + F(821, 5000)) / 2
    require(old_ceiling == F(4179, 5000), "old route ceiling")
    require(impossible_eta == F(10321, 10000) > 1, "old route impossible eta")

    model_reserve = F(500, 501)
    eta = model_reserve * F(99, 101) ** 2
    output = 2 * eta - 1
    margin = output - F(9, 10)
    require(eta == F(1633500, 1703567), "effective-rank fraction")
    require(output == F(1563433, 1703567), "line proportion fraction")
    require(margin == F(302227, 17035670) > 0, "ninety-percent margin")
    return {
        "old_positive_index_ceiling": str(old_ceiling),
        "old_required_eta_for_ninety_percent": str(impossible_eta),
        "model_effective_rank_lower": str(model_reserve),
        "one_percent_eta_lower": str(eta),
        "conditional_line_fraction": str(output),
        "conditional_line_decimal": f"{float(output):.15f}",
        "exact_margin_over_ninety_percent": str(margin),
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative in CONTENT:
        data = (ROOT / relative).read_bytes().replace(b"\r\n", b"\n")
        hashes[relative] = hashlib.sha256(data).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "verdict": VERDICT,
        "full_signature_regression": full_signature_regression(),
        "wick2_algebra": wick2_algebra_checks(),
        "energy_bound": energy_bound_checks(),
        "ninety_percent_bridge": ninety_percent_checks(),
        "content_sha256": content_hashes(),
        "finite_full_signature_machine_regression": True,
        "pnt_limit_machine_proved": False,
        "montgomery_vaughan_transfer_machine_proved": False,
        "w2xfer105500_proved": False,
        "ninety_percent_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


# Compatibility names used by the unit test.
full_signature_checks = full_signature_regression
wick_algebra_checks = wick2_algebra_checks
record_checks = ninety_percent_checks


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(result["proof_object_sha256"])
    print("EXACT_POLYNOMIAL_REGRESSIONS=8925")
    print("CONDITIONAL_LINE_FRACTION=1563433/1703567")
    print("W2XFER105500_OPEN")
    print("NINETY_PERCENT_UNPROVED")
    print("RH_UNPROVED")
