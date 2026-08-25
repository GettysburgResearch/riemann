#!/usr/bin/env python3
"""Exact same-characteristic tower spectroscopy for two marked genus-2 traces.

The source-locked all-q theorems give T_(0,3)(q) and T_(2,2)(q).  Setting
q=p^n turns each into an exact virtual power sum.  This producer recovers the
minimal recurrence from initial tower values, verifies held-out values, and
records the resulting trace-level signed Tate spectrum.  It enumerates no
field, curve, polynomial, cohomology group, or modular form.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_exact_frobenius_tower_spectroscopy.json"
NOTE_PATH = HERE / "GENUS2_EXACT_FROBENIUS_TOWER_SPECTROSCOPY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_exact_frobenius_tower_spectroscopy.py"
B3_PATH = HERE / "genus2_b3_primitive_trace_average.json"
M22_PATH = HERE / "genus2_m22_triangular_trace_average.json"

SOURCE_LOCKS: dict[str, dict[str, str]] = {
    B3_PATH.name: {
        "lf_sha256": "5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b",
        "payload_sha256": "e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd",
        "schema": "riemann.function_field.genus2_b3_primitive_trace_average.v1",
        "commit": "65eb68fe150998451799059aca80dce550a75b87",
    },
    M22_PATH.name: {
        "lf_sha256": "a93f288ddce023005989cc0a7ed543d859697e68fa378a24ae7619af35fc9633",
        "payload_sha256": "4d147295e3d2b7bc4b62eb8ba113c946f528606d82dd28d1a1ec002e2f93d60c",
        "schema": "riemann.function_field.genus2_m22_triangular_trace_average.v1",
        "commit": "65f4c7dc0c7340b561d0fb278cda75f1fb7944cd",
    },
}

CONTROL_PRIMES = (3, 5, 7)
TOWER_TERMS = 12
HOLDOUT_TERMS = 4
MAX_SOURCE_BYTES_EACH = 100_000
MAX_EXACT_OPERATIONS = 4_096


@dataclass
class OperationGuard:
    limit: int = MAX_EXACT_OPERATIONS
    used: int = 0

    def consume(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("operation charge must be a nonnegative integer")
        self.used += amount
        if self.used > self.limit:
            raise RuntimeError("exact spectroscopy operation cap exceeded")


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _sha256_lf(path: Path) -> str:
    return hashlib.sha256(_lf_bytes(path.read_bytes())).hexdigest()


def _load_locked_json(path: Path, lock: Mapping[str, str]) -> dict[str, object]:
    raw = path.read_bytes()
    if not 0 < len(raw) <= MAX_SOURCE_BYTES_EACH:
        raise ValueError(f"source outside byte cap: {path.name}")
    if hashlib.sha256(_lf_bytes(raw)).hexdigest() != lock["lf_sha256"]:
        raise ArithmeticError(f"LF source hash mismatch: {path.name}")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict) or value.get("schema") != lock["schema"]:
        raise TypeError(f"source schema mismatch: {path.name}")
    claimed = value.get("payload_sha256")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != lock["payload_sha256"] or claimed != _canonical_sha256(payload):
        raise ArithmeticError(f"canonical source payload mismatch: {path.name}")
    return value


def _require_base_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or prime % 2 == 0
    ):
        raise ValueError("control base must be an odd prime")
    divisor = 3
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("control base must be an odd prime")
        divisor += 2
    return prime


def _require_tower_index(index: int) -> int:
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("tower index must be a positive integer")
    return index


TRACE_POLYNOMIALS: dict[str, tuple[int, ...]] = {
    "chi_(0,3)": (-1, -2, 0, 0, 1),
    "chi_(2,2)": (-2, -2, -1, 2),
}


def evaluate_polynomial(coefficients: Sequence[int], value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("polynomial value must be an integer")
    result = 0
    for coefficient in reversed(coefficients):
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("trace polynomial coefficients must be integers")
        result = result * value + coefficient
    return result


def tower_trace(channel: str, prime: int, index: int) -> int:
    prime = _require_base_prime(prime)
    index = _require_tower_index(index)
    if channel not in TRACE_POLYNOMIALS:
        raise ValueError("unknown marked trace channel")
    return evaluate_polynomial(TRACE_POLYNOMIALS[channel], prime**index)


def virtual_tate_spectrum(channel: str, prime: int) -> tuple[tuple[int, int, int], ...]:
    """Return (Tate exponent, eigenvalue p^j, signed multiplicity)."""

    prime = _require_base_prime(prime)
    if channel not in TRACE_POLYNOMIALS:
        raise ValueError("unknown marked trace channel")
    return tuple(
        (exponent, prime**exponent, coefficient)
        for exponent, coefficient in enumerate(TRACE_POLYNOMIALS[channel])
        if coefficient
    )


def polynomial_multiply(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return tuple(result)


def characteristic_polynomial(roots: Sequence[int]) -> tuple[int, ...]:
    result = (1,)
    for root in roots:
        result = polynomial_multiply(result, (-root, 1))
    return result


def determinant(
    matrix: Sequence[Sequence[int | Fraction]], guard: OperationGuard
) -> Fraction:
    if not matrix:
        return Fraction(1)
    rows = [list(map(Fraction, row)) for row in matrix]
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("determinant requires a square matrix")
    result = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result = -result
        pivot_value = rows[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            if not rows[row][column]:
                continue
            factor = rows[row][column] / pivot_value
            for inner in range(column + 1, size):
                rows[row][inner] -= factor * rows[column][inner]
                guard.consume()
    return result


def solve_square(
    matrix: Sequence[Sequence[int | Fraction]],
    right: Sequence[int | Fraction],
    guard: OperationGuard,
) -> tuple[Fraction, ...]:
    size = len(matrix)
    if size < 1 or len(right) != size or any(len(row) != size for row in matrix):
        raise ValueError("square solve dimension mismatch")
    rows = [
        list(map(Fraction, row)) + [Fraction(value)]
        for row, value in zip(matrix, right)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column]), None)
        if pivot is None:
            raise ArithmeticError("singular recurrence recovery matrix")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        pivot_value = rows[column][column]
        rows[column] = [value / pivot_value for value in rows[column]]
        guard.consume(size + 1)
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[column])
            ]
            guard.consume(size + 1)
    return tuple(row[-1] for row in rows)


def recover_recurrence(
    values: Sequence[int], order: int, guard: OperationGuard
) -> tuple[Fraction, ...]:
    """Recover c_0,...,c_(r-1) in s_(n+r)+sum c_j s_(n+j)=0."""

    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("recurrence order must be positive")
    if len(values) < 2 * order:
        raise ValueError("recurrence recovery needs at least twice the order")
    matrix = tuple(
        tuple(values[row + column] for column in range(order)) for row in range(order)
    )
    right = tuple(-values[row + order] for row in range(order))
    recovered = solve_square(matrix, right, guard)
    for start in range(len(values) - order):
        residual = values[start + order] + sum(
            recovered[column] * values[start + column] for column in range(order)
        )
        guard.consume(order)
        if residual:
            raise ArithmeticError("recovered recurrence failed a tower value")
    return recovered


def hankel_matrix(values: Sequence[int], size: int) -> tuple[tuple[int, ...], ...]:
    if size < 1 or len(values) < 2 * size - 1:
        raise ValueError("insufficient tower values for Hankel matrix")
    return tuple(
        tuple(values[row + column] for column in range(size)) for row in range(size)
    )


def vandermonde_determinant(roots: Sequence[int]) -> int:
    result = 1
    for left in range(len(roots)):
        for right in range(left + 1, len(roots)):
            result *= roots[right] - roots[left]
    return result


def _fraction_list(values: Sequence[Fraction | int]) -> list[list[int]]:
    return [
        [Fraction(value).numerator, Fraction(value).denominator] for value in values
    ]


def _channel_control(
    channel: str, prime: int, guard: OperationGuard
) -> dict[str, object]:
    spectrum = virtual_tate_spectrum(channel, prime)
    roots = tuple(row[1] for row in spectrum)
    multiplicities = tuple(row[2] for row in spectrum)
    order = len(roots)
    values = tuple(
        tower_trace(channel, prime, index) for index in range(1, TOWER_TERMS + 1)
    )
    recovered = recover_recurrence(values[: 2 * order], order, guard)
    characteristic = characteristic_polynomial(roots)
    if recovered != tuple(Fraction(value) for value in characteristic[:-1]):
        raise ArithmeticError("data-recovered and spectrum recurrences disagree")

    training_end = 2 * order
    holdout_end = training_end + HOLDOUT_TERMS
    for start in range(training_end - order, holdout_end - order):
        predicted = -sum(
            recovered[column] * values[start + column] for column in range(order)
        )
        if predicted != values[start + order]:
            raise ArithmeticError("held-out tower prediction failed")
        guard.consume(order)

    full_hankel = hankel_matrix(values, order)
    full_determinant = determinant(full_hankel, guard)
    expected_determinant = vandermonde_determinant(roots) ** 2 * _product(
        multiplicity * root for multiplicity, root in zip(multiplicities, roots)
    )
    if full_determinant != expected_determinant or not full_determinant:
        raise ArithmeticError("nonzero minimal-rank Hankel certificate failed")
    next_determinant = determinant(hankel_matrix(values, order + 1), guard)
    if next_determinant:
        raise ArithmeticError("tower Hankel rank exceeds its virtual spectrum")

    return {
        "channel": channel,
        "base_prime": prime,
        "trace_polynomial_coefficients_in_increasing_q_power": list(
            TRACE_POLYNOMIALS[channel]
        ),
        "virtual_tate_spectrum": [
            {
                "Tate_exponent": exponent,
                "Frobenius_eigenvalue": eigenvalue,
                "signed_multiplicity": multiplicity,
            }
            for exponent, eigenvalue, multiplicity in spectrum
        ],
        "minimal_recurrence_order": order,
        "characteristic_polynomial_coefficients_in_increasing_X_power": list(
            characteristic
        ),
        "recovered_recurrence_coefficients_c0_through_c_(r-1)": _fraction_list(
            recovered
        ),
        "tower_values_n_1_through_12": list(values),
        "training_indices": [1, training_end],
        "held_out_indices": [training_end + 1, holdout_end],
        "held_out_predictions_exact": True,
        "rank_r_Hankel_determinant": [
            full_determinant.numerator,
            full_determinant.denominator,
        ],
        "rank_r_plus_1_Hankel_determinant": [
            next_determinant.numerator,
            next_determinant.denominator,
        ],
        "minimality_certificate": (
            "det(H_r)=prod_j(m_j*lambda_j)*Vandermonde(lambda)^2 is nonzero, "
            "while det(H_(r+1))=0"
        ),
    }


def _product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def build_certificate() -> dict[str, object]:
    b3 = _load_locked_json(B3_PATH, SOURCE_LOCKS[B3_PATH.name])
    m22 = _load_locked_json(M22_PATH, SOURCE_LOCKS[M22_PATH.name])
    if b3.get("status") != "PROVED_EXACT_ALL_ODD_PRIME_POWERS":
        raise ArithmeticError("B3 all-q theorem status drifted")
    if m22.get("status") != "PROVED_EXACT_ALL_ODD_PRIME_POWERS":
        raise ArithmeticError("M22 all-q theorem status drifted")
    if b3.get("theorem", {}).get("marked_stack_trace") != "T_(0,3)(q)=q^4-2*q-1":
        raise ArithmeticError("B3 marked trace formula drifted")
    if m22.get("theorem", {}).get("marked_stack_trace_chi_(2,2)") != "2*q^3-q^2-2*q-2":
        raise ArithmeticError("M22 marked trace formula drifted")

    guard = OperationGuard()
    controls = [
        _channel_control(channel, prime, guard)
        for channel in TRACE_POLYNOMIALS
        for prime in CONTROL_PRIMES
    ]

    ambiguity_witnesses = []
    for q in (3, 5, 7, 9, 25):
        vanishing_factor = (q - 3) * (q - 5) * (q - 7)
        ambiguity_witnesses.append(
            {
                "q": q,
                "cross_characteristic_vanishing_factor": vanishing_factor,
                "agrees_with_three_field_training_panel": q in (3, 5, 7),
            }
        )

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_exact_frobenius_tower_spectroscopy.v1",
        "status": "EXACT_SAME_CHARACTERISTIC_TRACE_RECURRENCES_PROVED_FROM_ALL_Q_THEOREMS",
        "source_theorems": {
            "chi_(0,3)": "T_(0,3)(q)=q^4-2*q-1 for every odd prime power",
            "chi_(2,2)": "T_(2,2)(q)=2*q^3-q^2-2*q-2 for every odd prime power",
            "source_locks": SOURCE_LOCKS,
        },
        "trace_level_spectra": {
            "chi_(0,3)": {
                "tower": "T_n=p^(4n)-2*p^n-1",
                "signed_Tate_multiplicities": {"0": -1, "1": -2, "4": 1},
                "minimal_recurrence": (
                    "T_(n+3)=(1+p+p^4)T_(n+2)-(p+p^4+p^5)T_(n+1)+p^5*T_n"
                ),
                "order": 3,
            },
            "chi_(2,2)": {
                "tower": "T_n=2*p^(3n)-p^(2n)-2*p^n-2",
                "signed_Tate_multiplicities": {"0": -2, "1": -2, "2": -1, "3": 2},
                "minimal_recurrence": (
                    "T_(n+4)=(1+p+p^2+p^3)T_(n+3)"
                    "-(p+p^2+2*p^3+p^4+p^5)T_(n+2)"
                    "+(p^3+p^4+p^5+p^6)T_(n+1)-p^6*T_n"
                ),
                "order": 4,
            },
        },
        "exact_recovery_controls": controls,
        "three_field_ambiguity_firewall": {
            "module": "(q-3)(q-5)(q-7)Q(q)",
            "witnesses": ambiguity_witnesses,
            "conclusion": (
                "a perturbation invisible at q=3,5,7 changes the first same-characteristic "
                "holdout q=3^2 by 48; the exact tower recurrence therefore supplies a "
                "strictly stronger evidence type than cross-characteristic interpolation"
            ),
        },
        "interpretation": {
            "proved": (
                "for each odd prime p, the compactly supported marked-stack trace sequence "
                "over F_(p^n) is the displayed virtual signed Tate power sum and has the "
                "displayed minimal recurrence"
            ),
            "not_proved": [
                "that each individual compactly supported cohomology group is Tate",
                "an isomorphism of motives or Galois representations rather than equality of virtual traces",
                "a Siegel eigenform identification",
                "a number-field transfer",
                "RH or GRH",
            ],
            "signed_multiplicity_warning": (
                "negative coefficients belong to the alternating compactly supported Euler trace; "
                "they are not negative dimensions of an individual cohomology group"
            ),
        },
        "scope": {
            "all_odd_prime_towers": True,
            "control_primes": list(CONTROL_PRIMES),
            "tower_terms_per_control": TOWER_TERMS,
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "random_samples": 0,
            "external_database_queries": 0,
        },
        "provenance": {
            "producer_sha256_lf": _sha256_lf(Path(__file__)),
            "note_sha256_lf": _sha256_lf(NOTE_PATH),
            "test_sha256_lf": _sha256_lf(TEST_PATH),
            "resource_contract": {
                "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "maximum_exact_operations": guard.limit,
                "exact_operations_used": guard.used,
            },
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    group.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    args = parser.parse_args(argv)
    rendered = (
        json.dumps(
            build_certificate(),
            allow_nan=False,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    if args.check:
        if (
            not args.check.is_file()
            or args.check.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("exact Frobenius tower spectroscopy fixture drifted")
        print("PASS_GENUS2_EXACT_FROBENIUS_TOWER_SPECTROSCOPY")
        return 0
    if args.write:
        args.write.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {args.write}")
        return 0
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
