#!/usr/bin/env python3
"""Prove the three-place elliptic interference identity.

The all-q proof is formal Euler-product algebra.  The only direct family
controls enumerate the 243 and 3,125 monic quintics over F_3 and F_5.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from itertools import product
from math import comb
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_three_place_elliptic_interference.json"
NOTE = HERE / "QUADRATIC_FAMILY_THREE_PLACE_ELLIPTIC_INTERFERENCE.md"
TEST = ROOT / "tests" / "test_quadratic_family_three_place_elliptic_interference.py"
SOURCE = HERE / "quadratic_family_two_place_cumulant_defect.json"
SOURCE_COMMIT = "a91f98532"
SOURCE_BLOB = "95f29d89e4eaf953ab5ecf0675e061000d7a9cef"
SOURCE_PAYLOAD = "18119e393842cfbe1f3ee7f594466eedf554004f9479f94338675921a3b0f859"
SCHEMA = "riemann.function_field.quadratic_family_three_place_elliptic_interference.v1"
MAX_SERIES_DEGREE = 5
MAX_CANDIDATE_POLYNOMIALS = 4_096
MAX_OUTPUT_BYTES = 32_768
WALL_SECONDS = 4.0

# Sparse polynomials in (q,t), keyed by (q exponent, t exponent).
Poly: TypeAlias = dict[tuple[int, int], int]
Series: TypeAlias = list[Poly]


def _clean(poly: Poly) -> Poly:
    return {key: value for key, value in poly.items() if value}


def _poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return _clean(result)


def _poly_mul(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (q_left, t_left), left_value in left.items():
        for (q_right, t_right), right_value in right.items():
            key = (q_left + q_right, t_left + t_right)
            result[key] = result.get(key, 0) + left_value * right_value
    return _clean(result)


def _series_mul(left: Series, right: Series) -> Series:
    result: Series = [{} for _ in range(MAX_SERIES_DEGREE + 1)]
    for left_degree, left_poly in enumerate(left):
        for right_degree, right_poly in enumerate(right):
            degree = left_degree + right_degree
            if degree <= MAX_SERIES_DEGREE:
                result[degree] = _poly_add(
                    result[degree], _poly_mul(left_poly, right_poly)
                )
    return result


def formal_triple_character_coefficient() -> Poly:
    """Return [u^5] (1-tu+qu^2)(1-qu^2)/(1-u^2)^3."""
    one: Poly = {(0, 0): 1}
    minus_t: Poly = {(0, 1): -1}
    q_poly: Poly = {(1, 0): 1}
    minus_q: Poly = {(1, 0): -1}
    l_polynomial: Series = [one, minus_t, q_poly, {}, {}, {}]
    squarefree_denominator: Series = [one, {}, minus_q, {}, {}, {}]
    inverse_ramified_zeta: Series = [
        ({(0, 0): comb(index // 2 + 2, 2)} if index % 2 == 0 else {})
        for index in range(MAX_SERIES_DEGREE + 1)
    ]
    return _series_mul(
        _series_mul(l_polynomial, squarefree_denominator),
        inverse_ramified_zeta,
    )[MAX_SERIES_DEGREE]


def _chi_prime(value: int, q: int) -> int:
    value %= q
    if value == 0:
        return 0
    return 1 if pow(value, (q - 1) // 2, q) == 1 else -1


def _trim(poly: list[int], q: int) -> list[int]:
    while poly and poly[-1] % q == 0:
        poly.pop()
    return [value % q for value in poly]


def _remainder(dividend: list[int], divisor: list[int], q: int) -> list[int]:
    dividend = _trim(dividend[:], q)
    divisor = _trim(divisor[:], q)
    if not divisor:
        raise ZeroDivisionError("zero polynomial divisor")
    inverse = pow(divisor[-1], -1, q)
    while len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        scalar = dividend[-1] * inverse % q
        for index, value in enumerate(divisor):
            dividend[index + shift] = (dividend[index + shift] - scalar * value) % q
        dividend = _trim(dividend, q)
    return dividend


def _is_squarefree(coefficients: list[int], q: int) -> bool:
    polynomial = _trim(coefficients[:], q)
    derivative = _trim(
        [index * coefficients[index] for index in range(1, len(coefficients))],
        q,
    )
    if not derivative:
        return False
    while derivative:
        polynomial, derivative = derivative, _remainder(polynomial, derivative, q)
    return len(polynomial) == 1


def _evaluate(coefficients: list[int], value: int, q: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % q
    return result


def direct_control(
    q: int,
    places: tuple[int, int, int],
    *,
    remaining_candidates: int = MAX_CANDIDATE_POLYNOMIALS,
) -> dict[str, int | list[int]]:
    """Exhaust one declared prime-field control under the shared atom cap."""
    if q not in {3, 5}:
        raise ValueError("direct controls are restricted to q=3 or q=5")
    if len({place % q for place in places}) != 3:
        raise ValueError("places must be distinct modulo q")
    candidate_count = q**5
    if candidate_count > remaining_candidates:
        raise RuntimeError("candidate-polynomial cap would be exceeded")

    a, b, c = (place % q for place in places)
    epsilon = _chi_prime(-1, q)
    separation_sum = sum(
        (
            _chi_prime(b - a, q),
            _chi_prime(c - a, q),
            _chi_prime(c - b, q),
        )
    )
    elliptic_trace = -sum(_chi_prime((a - z) * (b - z) * (c - z), q) for z in range(q))

    squarefree_count = 0
    triple_product_sum = 0
    third_defect_numerator = 0
    for low_coefficients in product(range(q), repeat=5):
        coefficients = list(low_coefficients) + [1]
        if not _is_squarefree(coefficients, q):
            continue
        squarefree_count += 1
        values = tuple(
            _chi_prime(_evaluate(coefficients, place, q), q) for place in (a, b, c)
        )
        x, y, z = values
        triple_product_sum += x * y * z
        third_defect_numerator += (x + y + z) ** 3 - x**3 - y**3 - z**3

    family_size = q**4 * (q - 1)
    pair_coefficient = 2 * q - 3
    predicted_triple = 3 * elliptic_trace * (q - 2)
    predicted_defect = 3 * (
        1 + epsilon
    ) * pair_coefficient * separation_sum + 18 * elliptic_trace * (q - 2)
    if squarefree_count != family_size:
        raise ArithmeticError("squarefree family size mismatch")
    if triple_product_sum != predicted_triple:
        raise ArithmeticError("triple-character sum mismatch")
    if third_defect_numerator != predicted_defect:
        raise ArithmeticError("third-cumulant interference mismatch")
    return {
        "q": q,
        "places": [a, b, c],
        "candidate_polynomials": candidate_count,
        "squarefree_members": squarefree_count,
        "epsilon": epsilon,
        "separation_sum": separation_sum,
        "elliptic_trace": elliptic_trace,
        "triple_product_sum": triple_product_sum,
        "third_defect_numerator": third_defect_numerator,
    }


def _canonical_sha256(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def _git_blob(path: Path, commit: str) -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _load_source() -> dict[str, object]:
    if _git_blob(SOURCE, SOURCE_COMMIT) != SOURCE_BLOB:
        raise RuntimeError("two-place source blob drifted")
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    if payload.get("payload_sha256") != SOURCE_PAYLOAD:
        raise RuntimeError("two-place source payload sentinel drifted")
    without_hash = dict(payload)
    claimed = without_hash.pop("payload_sha256")
    if _canonical_sha256(without_hash) != claimed:
        raise RuntimeError("two-place source self-hash failed")
    return payload


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    source = _load_source()
    formal = formal_triple_character_coefficient()
    expected = {(1, 1): 3, (0, 1): -6}
    if formal != expected:
        raise ArithmeticError(f"formal triple coefficient drifted: {formal!r}")

    controls: list[dict[str, int | list[int]]] = []
    remaining = MAX_CANDIDATE_POLYNOMIALS
    for q in (3, 5):
        control = direct_control(q, (0, 1, 2), remaining_candidates=remaining)
        remaining -= int(control["candidate_polynomials"])
        controls.append(control)
    elapsed = time.monotonic() - started
    if elapsed > WALL_SECONDS:
        raise RuntimeError("wall-clock cap exceeded")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_EXACT_FOR_EVERY_ODD_PRIME_POWER",
        "family": "monic squarefree quintics over F_q",
        "variables": "X_i=chi(D(a_i)) at three distinct rational places",
        "oriented_elliptic_curve": "E_(a,b,c): y^2=(a-z)*(b-z)*(c-z)",
        "elliptic_trace": "t=q+1-#E(F_q)=-sum_z chi((a-z)*(b-z)*(c-z))",
        "exact_theorems": {
            "triple_L_polynomial": "L(u,psi_abc)=1-t*u+q*u^2",
            "squarefree_series": "(1-t*u+q*u^2)*(1-q*u^2)/(1-u^2)^3",
            "triple_character_sum": "sum_D X_a*X_b*X_c=3*(q-2)*t",
            "family_size": "A=q^4*(q-1)",
            "pair_coefficient": "C=2*q-3",
            "separation_sum": "s=chi(b-a)+chi(c-a)+chi(c-b)",
            "third_cumulant_defect": ("Delta_3=[3*(1+epsilon)*C*s+18*(q-2)*t]/A"),
        },
        "formal_u5_coefficient": {
            "sparse_q_t": [
                {"q_power": q_power, "t_power": t_power, "coefficient": value}
                for (q_power, t_power), value in sorted(formal.items())
            ],
            "rendered": "3*(q-2)*t",
        },
        "direct_controls": controls,
        "source": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
            "payload_sha256": SOURCE_PAYLOAD,
            "imported_rows": {
                "A": source["scalar_law"]["A"],
                "C": source["scalar_law"]["C"],
            },
        },
        "resource_contract": {
            "maximum_candidate_polynomials": MAX_CANDIDATE_POLYNOMIALS,
            "actual_candidate_polynomials": sum(
                int(row["candidate_polynomials"]) for row in controls
            ),
            "largest_direct_field": 5,
            "maximum_series_degree": MAX_SERIES_DEGREE,
            "wall_seconds_cap": WALL_SECONDS,
            "measured_wall_seconds_is_not_canonical": True,
            "floating_point_arithmetic": False,
            "extension_field_enumeration": False,
        },
        "claim_boundary": [
            "The all-q identity uses the standard quadratic Dirichlet L-polynomial of the displayed elliptic curve; direct family controls are only q=3,5.",
            "The elliptic trace is a three-place interaction channel, not a motive attached to an individual detector or a statement about zeros.",
            "The q^-7/2 Weil scale is an upper-envelope scale; the trace t may vanish for particular triples.",
            "No RH, GRH, principal-member amplification, or external novelty claim is made.",
        ],
        "packet_files_lf_sha256": {
            "note": _file_sha256(NOTE),
            "producer": _file_sha256(Path(__file__).resolve()),
            "test": _file_sha256(TEST),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if len(rendered) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("canonical payload drift")
        print(f"verified {OUTPUT}")
    else:
        OUTPUT.write_bytes(rendered)
        print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
