#!/usr/bin/env python3
"""Bounded control for first-boundary trace-zero extinction at the odd notch.

The theorem is symbolic.  The only enumeration is the exceptional n=3
prime-field regression over 20,175 monic quintics for q=3,5,7.
"""

from __future__ import annotations

import argparse
import itertools
import json
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md"
BASE_COMMIT = "6e4609dfe1b073f1eb58445fdd1d7164dbc450d6"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md": (
        "a1b8476ddd3cad6f63ff205392426ae9c2d0829c"
    ),
    "research/l-families/atlas/function_field/quadratic_family_closed_place_weight_notch.json": (
        "964935a3a936f03011366546d966ef1473c4e832"
    ),
}

CONTROL_PRIMES = (3, 5, 7)
MAX_CANDIDATES = 25_000
MAX_FIELD_EVALUATIONS = 150_000
MAX_WALL_SECONDS = 5.0


def _trim(poly: list[int], prime: int) -> list[int]:
    result = [coefficient % prime for coefficient in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def _poly_divmod(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    top = _trim(numerator, prime)
    bottom = _trim(denominator, prime)
    if bottom == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(top) - len(bottom) + 1)
    inverse = pow(bottom[-1], -1, prime)
    while top != [0] and len(top) >= len(bottom):
        shift = len(top) - len(bottom)
        coefficient = top[-1] * inverse % prime
        quotient[shift] = coefficient
        for index, value in enumerate(bottom):
            top[index + shift] = (top[index + shift] - coefficient * value) % prime
        top = _trim(top, prime)
    return _trim(quotient, prime), top


def _poly_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    first = _trim(left, prime)
    second = _trim(right, prime)
    while second != [0]:
        _, remainder = _poly_divmod(first, second, prime)
        first, second = second, remainder
    inverse = pow(first[-1], -1, prime)
    return _trim([(value * inverse) % prime for value in first], prime)


def _derivative(poly: list[int], prime: int) -> list[int]:
    if len(poly) <= 1:
        return [0]
    return _trim([index * poly[index] for index in range(1, len(poly))], prime)


def _evaluate(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def _quadratic_symbol(value: int, prime: int) -> int:
    residue = value % prime
    if residue == 0:
        return 0
    power = pow(residue, (prime - 1) // 2, prime)
    if power == 1:
        return 1
    if power == prime - 1:
        return -1
    raise RuntimeError("Euler criterion failed")


def exceptional_quintic_control(prime: int) -> dict[str, int]:
    """Enumerate the one exceptional first boundary n=3 over a prime field."""

    if prime not in CONTROL_PRIMES:
        raise ValueError("prime is outside the declared exceptional control set")
    candidate_count = prime**5
    if candidate_count > MAX_CANDIDATES:
        raise RuntimeError("candidate cap exceeded")

    squarefree_count = 0
    support_forced = 0
    first_boundary_trace_zero = 0
    field_evaluations = 0
    for coefficients in itertools.product(range(prime), repeat=5):
        poly = [*coefficients, 1]
        if len(_poly_gcd(poly, _derivative(poly, prime), prime)) != 1:
            continue
        squarefree_count += 1
        values = [_evaluate(poly, value, prime) for value in range(prime)]
        field_evaluations += prime
        if field_evaluations > MAX_FIELD_EVALUATIONS:
            raise RuntimeError("field-evaluation cap exceeded")
        has_linear_factor = any(value == 0 for value in values)
        oriented_trace_coefficient = sum(
            _quadratic_symbol(-value, prime) for value in values
        )
        if not has_linear_factor:
            support_forced += 1
        elif oriented_trace_coefficient == 0:
            first_boundary_trace_zero += 1

    expected_squarefree = prime**5 - prime**4
    if squarefree_count != expected_squarefree:
        raise RuntimeError("squarefree quintic count failed")
    return {
        "q": prime,
        "monic_quintic_candidates": candidate_count,
        "squarefree_quintics": squarefree_count,
        "support_forced": support_forced,
        "first_boundary_trace_zero": first_boundary_trace_zero,
        "all_raw_zeros_in_first_two_strata": (
            support_forced + first_boundary_trace_zero
        ),
        "field_evaluations": field_evaluations,
    }


def first_boundary_certificate(q: int, n: int, multiplicity: int) -> dict[str, object]:
    """Return the symbolic first-boundary nonvanishing certificate."""

    if isinstance(q, bool) or not isinstance(q, int) or q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd integer at least three")
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError("family degree n must be an integer at least two")
    if (
        isinstance(multiplicity, bool)
        or not isinstance(multiplicity, int)
        or multiplicity < 1
    ):
        raise ValueError("first-boundary multiplicity must be positive")
    h_value = n // 2
    if n % 2 == 0:
        return {
            "q": q,
            "n": n,
            "h": h_value,
            "residual": f"{multiplicity}*D_0={multiplicity}",
            "nonzero": True,
            "certificate": "D_0=1 and m_h>0",
        }
    if n >= 5:
        return {
            "q": q,
            "n": n,
            "h": h_value,
            "residual": f"{multiplicity}*D_1",
            "nonzero": True,
            "certificate": "h>=2; D_1 is a sum of q odd many +/-1 values",
            "D_1_parity": 1,
        }
    return {
        "q": q,
        "n": n,
        "h": h_value,
        "residual": f"{multiplicity}*D_1",
        "nonzero": None,
        "certificate": "n=3 permits linear roots and is the unique exception",
    }


def _check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{BASE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def build_report() -> dict[str, object]:
    started = time.monotonic()
    rows = [exceptional_quintic_control(prime) for prime in CONTROL_PRIMES]
    if sum(row["monic_quintic_candidates"] for row in rows) != 20_175:
        raise RuntimeError("candidate ledger mismatch")
    expected = {
        3: (72, 30, 102, 162),
        5: (1024, 406, 1430, 2500),
        7: (5712, 2184, 7896, 14406),
    }
    for row in rows:
        actual = (
            row["support_forced"],
            row["first_boundary_trace_zero"],
            row["all_raw_zeros_in_first_two_strata"],
            row["squarefree_quintics"],
        )
        if actual != expected[row["q"]]:
            raise RuntimeError(f"exceptional q={row['q']} regression failed")
    report = {
        "schema": "riemann.function_field.quadratic_first_boundary_trace_zero_density.v1",
        "status": "EXACT_FIRST_BOUNDARY_EXTINCTION_WITH_BOUNDED_N3_CONTROL",
        "base_commit": BASE_COMMIT,
        "exact_theorem": {
            "scope": "every odd prime power q and every n>=4",
            "first_boundary": "min degree(P)=floor(n/2)",
            "residual": "S_(n,Q)=m_h*D_(n-2h)",
            "even_n": "m_h*D_0=m_h>0",
            "odd_n_at_least_5": "m_h*D_1!=0 because D_1 is odd",
            "density_consequence": "the first boundary contributes exactly zero",
        },
        "exceptional_n3_prime_field_controls": rows,
        "resource_contract": {
            "monic_quintic_candidates": 20_175,
            "field_evaluations": sum(row["field_evaluations"] for row in rows),
            "maximum_candidates": MAX_CANDIDATES,
            "maximum_field_evaluations": MAX_FIELD_EVALUATIONS,
            "irreducibles_enumerated": 0,
            "l_function_zeros_enumerated": 0,
        },
        "firewalls": [
            "The theorem concerns zeros of a raw family correlation sum.",
            "The n=3 enumeration is a regression control, not an asymptotic proof.",
            "Deeper factor-degree boundaries remain open.",
            "No individual L-function zero theorem, RH, or GRH is proved.",
        ],
    }
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return report


def run_checks() -> dict[str, object]:
    _check_source_blobs()
    report = build_report()
    for n_value in range(4, 15):
        row = first_boundary_certificate(3, n_value, 1 + n_value % 3)
        if row["nonzero"] is not True:
            raise RuntimeError("symbolic nonvanishing certificate failed")
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "exact trace-zero extinction",
        "D_1\\equiv q\\equiv1",
        "B_{q,n}^{(1)}=0",
        "second boundary",
        "not zeros of an individual L-function",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="run source and exact control checks"
    )
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
