#!/usr/bin/env python3
"""Bounded exact packet for correlated FFPS restricted-Gram masks.

For a tensor square-phase Gram G, this producer proves the sharp optimizer
on every retained joint support, solves the complete two-prime support-size
problem, exhibits the full-grid-minus-matching improvement, and proves an
arbitrary-d random-fixed-size existence bound.  Frozen FFPS packets are read
only after the self-contained finite algebra closes.

No character family, conductor family, L-function, zero set, or finite field
is enumerated.  Arbitrary formal masks are not asserted to be source-realizable
arithmetic conditions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_correlated_mask_amplifier.json"
NOTE_PATH = HERE / "FFPS_CORRELATED_MASK_AMPLIFIER.md"
TEST_PATH = ROOT / "tests" / "test_ffps_correlated_mask_amplifier.py"

PRINCIPAL_JSON_PATH = HERE / "ffps_principal_leverage.json"
PRINCIPAL_NOTE_PATH = HERE / "FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md"
MASK_JSON_PATH = HERE / "ffps_conditioned_mask_no_go.json"
MASK_NOTE_PATH = HERE / "FFPS_CONDITIONED_MASK_NO_GO.md"
FRONTIER_JSON_PATH = HERE / "ffps_coherent_tensor_cost_frontier.json"
FRONTIER_NOTE_PATH = HERE / "FFPS_COHERENT_TENSOR_COST_FRONTIER.md"
SIGNED_JSON_PATH = HERE / "ffps_tensor_signed_amplifier_no_go.json"
SIGNED_NOTE_PATH = HERE / "FFPS_TENSOR_SIGNED_AMPLIFIER_NO_GO.md"

MAX_EXACT_OPERATIONS = 100_000
MAX_MATRIX_CELLS = 50_000
MAX_ENUMERATED_SUBSETS = 2_048
MAX_TENSOR_DIMENSION = 16
MAX_TWO_PRIME_SIZE_SCAN = 2_000
MAX_SOURCE_FILES = 8
MAX_SOURCE_BYTES_EACH = 40_000
MAX_SOURCE_BYTES_TOTAL = 131_072
MAX_PACKET_FILE_BYTES = 65_536
MAX_WALL_SECONDS = 5.0

LIVE_PR_751_HEAD = "98af0db6ec7f77d6333a77a3dac53c4698852f43"
LIVE_L106024_BLOB = "d94787dc2cd1cedd74d33ddc6269daf8de1cc061"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "principal_json": {
        "path": PRINCIPAL_JSON_PATH,
        "commit": "5c9462064aefe43164fcf5bc0b6d76b575e67a49",
        "git_blob": "d96cd12a5fbfe86b63d9c6b7076c8a99aa139f4c",
        "lf_sha256": "cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3",
        "schema": "riemann.function_field.ffps_principal_leverage.v2",
        "role": "corrected local Gram G_p=pI-J and tensor leverage",
    },
    "principal_note": {
        "path": PRINCIPAL_NOTE_PATH,
        "commit": "5c9462064aefe43164fcf5bc0b6d76b575e67a49",
        "git_blob": "e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a",
        "lf_sha256": "6b3a0958422f01b44b7702b1088f4e13926d5d11a7725bde2582cd2d371b07e6",
        "role": "physical-squareclass interpretation and scope firewall",
    },
    "mask_json": {
        "path": MASK_JSON_PATH,
        "commit": "d6cdca528f664acb8fd9e33541f855faa45bb5ca",
        "git_blob": "1aa8ea28e164a8389b66b6b780d5e081e6a96848",
        "lf_sha256": "fe6024020775e977e3dfe31822137b579c9cef438f9e94666714179ed43d469b",
        "schema": "riemann.function_field.ffps_conditioned_mask_no_go.v1",
        "role": "local and product-coordinate restricted-mask no-go",
    },
    "mask_note": {
        "path": MASK_NOTE_PATH,
        "commit": "d6cdca528f664acb8fd9e33541f855faa45bb5ca",
        "git_blob": "c300500a1563c5299f3ddffd47571309511bb563",
        "lf_sha256": "0a3d7d30780b48de82bb2203e1b1ff0eed7912e348b91be329bc202f945b0524",
        "role": "restricted metric and product-mask boundary",
    },
    "frontier_json": {
        "path": FRONTIER_JSON_PATH,
        "commit": "7d1da8cc11718f138897cd36e8cc83a77c4f65d6",
        "git_blob": "eb21ae1cdd158395d3547b946f2ee25a84e23e05",
        "lf_sha256": "f6b65bb4a8cdaaa7c91464d8fba86b7691350bf14cdcc8a68c90848be6f89d51",
        "schema": "riemann.function_field.ffps_coherent_tensor_cost_frontier.v1",
        "role": "complete-tensor conductor-cost frontier",
    },
    "frontier_note": {
        "path": FRONTIER_NOTE_PATH,
        "commit": "7d1da8cc11718f138897cd36e8cc83a77c4f65d6",
        "git_blob": "292487efca3df3971518edba0c0b23b830be2c16",
        "lf_sha256": "037ec4751504d2387a87e606dbd8eb74dbcc3abb554ccb77ee449fd838a4583e",
        "role": "formal tensor and global-moment firewall",
    },
    "signed_json": {
        "path": SIGNED_JSON_PATH,
        "commit": "4347a83499f697e3a73393c212507e74f927a2f2",
        "git_blob": "5f666e6a6ada7cd79eb9af27038ad64d599d4eee",
        "lf_sha256": "d9d2bd40bbbd22caba3fe67dd2967f092195e5fe7cdff479c21ff6b6c04062aa",
        "schema": "riemann.function_field.ffps_tensor_signed_amplifier_no_go.v1",
        "payload_sha256": "a61fe11c49e38630762931971c573a87be1763974f9a7ee599ccf10f915c1e95",
        "role": "complete-frame signed no-go and correlated-mask warning",
    },
    "signed_note": {
        "path": SIGNED_NOTE_PATH,
        "commit": "4347a83499f697e3a73393c212507e74f927a2f2",
        "git_blob": "1ce6a9c461d5937f4d6bb2de9f430b466ff1e78c",
        "lf_sha256": "85bbfdc3f3d137fa6d9a56d0f5445ad131c3628ecb29286155dce5864c8f7929",
        "role": "metric distinction and exact (5,7) seed example",
    },
}


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    matrix_cells: int = 0
    enumerated_subsets: int = 0
    two_prime_sizes: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def matrix(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("matrix-cell increment must be nonnegative")
        if self.matrix_cells + amount > MAX_MATRIX_CELLS:
            raise RuntimeError("matrix-cell cap exceeded")
        self.matrix_cells += amount

    def subset(self) -> None:
        if self.enumerated_subsets + 1 > MAX_ENUMERATED_SUBSETS:
            raise RuntimeError("enumerated-subset cap exceeded")
        self.enumerated_subsets += 1

    def size_scan(self) -> None:
        if self.two_prime_sizes + 1 > MAX_TWO_PRIME_SIZE_SCAN:
            raise RuntimeError("two-prime size-scan cap exceeded")
        self.two_prime_sizes += 1

    def source(self, byte_count: int) -> None:
        if byte_count < 0:
            raise ValueError("source size must be nonnegative")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    return hashlib.sha1(
        f"blob {len(normalized)}\0".encode("ascii") + normalized
    ).hexdigest()


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, tuple):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


Scalar = Fraction
Matrix = tuple[tuple[Scalar, ...], ...]


def _as_matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    if not rows:
        raise ValueError("matrix must be nonempty")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have one common positive width")
    return tuple(tuple(Fraction(entry) for entry in row) for row in rows)


def local_gram(dimension: int, guard: ResourceGuard) -> Matrix:
    """Return (2m+1)I_m-J_m for m=dimension."""

    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 1:
        raise ValueError("local dimension must be a positive integer")
    guard.matrix(dimension * dimension)
    prime = 2 * dimension + 1
    return _as_matrix(
        [
            [prime - 1 if row == column else -1 for column in range(dimension)]
            for row in range(dimension)
        ]
    )


def kronecker(left: Matrix, right: Matrix, guard: ResourceGuard) -> Matrix:
    left_rows = len(left)
    left_columns = len(left[0])
    right_rows = len(right)
    right_columns = len(right[0])
    guard.matrix(left_rows * left_columns * right_rows * right_columns)
    rows: list[list[Fraction]] = []
    for left_row in range(left_rows):
        for right_row in range(right_rows):
            row: list[Fraction] = []
            for left_column in range(left_columns):
                for right_column in range(right_columns):
                    guard.operation("kronecker_cells")
                    row.append(
                        left[left_row][left_column] * right[right_row][right_column]
                    )
            rows.append(row)
    return _as_matrix(rows)


def tensor_gram(dimensions: Sequence[int], guard: ResourceGuard) -> Matrix:
    normalized = tuple(dimensions)
    if not normalized or any(
        isinstance(value, bool) or not isinstance(value, int) or value < 1
        for value in normalized
    ):
        raise ValueError("tensor dimensions must be positive integers")
    total_dimension = math.prod(normalized)
    if total_dimension > MAX_TENSOR_DIMENSION:
        raise ValueError("tensor dimension exceeds the control cap")
    result = local_gram(normalized[0], guard)
    for dimension in normalized[1:]:
        result = kronecker(result, local_gram(dimension, guard), guard)
    return result


def principal_submatrix(
    matrix: Matrix, support: Sequence[int], guard: ResourceGuard
) -> Matrix:
    normalized = tuple(support)
    if (
        not normalized
        or len(set(normalized)) != len(normalized)
        or min(normalized) < 0
        or max(normalized) >= len(matrix)
    ):
        raise ValueError("support must be a nonempty set of matrix indices")
    guard.matrix(len(normalized) ** 2)
    return _as_matrix(
        [[matrix[row][column] for column in normalized] for row in normalized]
    )


def matrix_vector(
    matrix: Matrix, vector: Sequence[Fraction], guard: ResourceGuard
) -> tuple[Fraction, ...]:
    if len(matrix[0]) != len(vector):
        raise ValueError("matrix-vector dimension mismatch")
    result = []
    for row in matrix:
        total = Fraction(0)
        for entry, value in zip(row, vector):
            guard.operation("matrix_vector")
            total += entry * value
        result.append(total)
    return tuple(result)


def quadratic_form(
    matrix: Matrix, vector: Sequence[Fraction], guard: ResourceGuard
) -> Fraction:
    product = matrix_vector(matrix, vector, guard)
    guard.operation("quadratic_form", len(vector))
    return sum((left * right for left, right in zip(vector, product)), Fraction(0))


def invert_matrix(matrix: Matrix, guard: ResourceGuard) -> Matrix:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("inverse requires a square matrix")
    guard.matrix(2 * size * size)
    augmented = [
        list(row)
        + [Fraction(1 if row_index == column else 0) for column in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for pivot_column in range(size):
        pivot_row = next(
            (
                row
                for row in range(pivot_column, size)
                if augmented[row][pivot_column] != 0
            ),
            None,
        )
        if pivot_row is None:
            raise ArithmeticError("matrix is singular")
        augmented[pivot_column], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[pivot_column],
        )
        pivot = augmented[pivot_column][pivot_column]
        for column in range(2 * size):
            guard.operation("gauss_jordan_scale")
            augmented[pivot_column][column] /= pivot
        for row in range(size):
            if row == pivot_column:
                continue
            factor = augmented[row][pivot_column]
            if factor == 0:
                continue
            for column in range(2 * size):
                guard.operation("gauss_jordan_eliminate")
                augmented[row][column] -= factor * augmented[pivot_column][column]
    return _as_matrix([row[size:] for row in augmented])


def restricted_optimizer(
    gram: Matrix, support: Sequence[int], native_amplitude: int, guard: ResourceGuard
) -> dict[str, object]:
    """Verify the sharp restricted dual-energy optimizer on one support."""

    if native_amplitude <= 0:
        raise ValueError("native amplitude must be positive")
    restricted = principal_submatrix(gram, support, guard)
    ones = (Fraction(1),) * len(restricted)
    row_sums = matrix_vector(restricted, ones, guard)
    denominator = sum(row_sums, Fraction(0))
    if denominator <= 0:
        raise ArithmeticError("restricted denominator must be positive")
    weights = tuple(
        Fraction(native_amplitude) * row_sum / denominator for row_sum in row_sums
    )
    if sum(weights, Fraction(0)) != native_amplitude:
        raise ArithmeticError("restricted optimizer lost native amplitude")
    inverse = invert_matrix(restricted, guard)
    energy = quadratic_form(inverse, weights, guard)
    expected = Fraction(native_amplitude * native_amplitude, denominator)
    if energy != expected:
        raise ArithmeticError("restricted optimizer formula failed")
    return {
        "support": list(support),
        "denominator_1_G_A_1": _fraction_pair(denominator),
        "weights_N_G_A_1_over_E": [_fraction_pair(value) for value in weights],
        "dual_energy": _fraction_pair(energy),
    }


def balanced_square_sum(parts: int, total: int) -> int:
    """Minimum sum of squares of parts nonnegative integers totaling total."""

    if (
        isinstance(parts, bool)
        or not isinstance(parts, int)
        or parts < 1
        or isinstance(total, bool)
        or not isinstance(total, int)
        or total < 0
    ):
        raise ValueError("balanced square sum needs positive parts and total >= 0")
    quotient, remainder = divmod(total, parts)
    return parts * quotient * quotient + remainder * (2 * quotient + 1)


def balanced_degrees(parts: int, total: int) -> tuple[int, ...]:
    quotient, remainder = divmod(total, parts)
    return (quotient + 1,) * remainder + (quotient,) * (parts - remainder)


def balanced_support(
    row_count: int, column_count: int, size: int, guard: ResourceGuard
) -> tuple[tuple[int, int], ...]:
    """Construct simultaneous balanced margins by bipartite Havel-Hakimi."""

    if not 0 <= size <= row_count * column_count:
        raise ValueError("support size lies outside the grid")
    row_degrees = balanced_degrees(row_count, size)
    remaining = list(balanced_degrees(column_count, size))
    support: list[tuple[int, int]] = []
    for row, degree in enumerate(row_degrees):
        order = sorted(
            range(column_count), key=lambda column: (-remaining[column], column)
        )
        chosen = order[:degree]
        if len(chosen) != degree or any(remaining[column] <= 0 for column in chosen):
            raise ArithmeticError("balanced Havel-Hakimi construction failed")
        for column in chosen:
            guard.operation("balanced_support_edges")
            support.append((row, column))
            remaining[column] -= 1
    if any(remaining):
        raise ArithmeticError("balanced construction left column degree")
    return tuple(sorted(support))


def two_prime_energy_from_degrees(
    row_count: int,
    column_count: int,
    size: int,
    row_square_sum: int,
    column_square_sum: int,
) -> int:
    p = 2 * row_count + 1
    q = 2 * column_count + 1
    return p * q * size + size * size - p * row_square_sum - q * column_square_sum


def two_prime_support_energy(
    row_count: int,
    column_count: int,
    support: Sequence[tuple[int, int]],
) -> int:
    normalized = tuple(support)
    if len(set(normalized)) != len(normalized):
        raise ValueError("support cells must be distinct")
    rows = [0] * row_count
    columns = [0] * column_count
    for row, column in normalized:
        if not 0 <= row < row_count or not 0 <= column < column_count:
            raise ValueError("support cell lies outside the grid")
        rows[row] += 1
        columns[column] += 1
    return two_prime_energy_from_degrees(
        row_count,
        column_count,
        len(normalized),
        sum(value * value for value in rows),
        sum(value * value for value in columns),
    )


def two_prime_max_denominator(row_count: int, column_count: int, size: int) -> int:
    if not 1 <= size <= row_count * column_count:
        raise ValueError("support size must be between one and the grid size")
    return two_prime_energy_from_degrees(
        row_count,
        column_count,
        size,
        balanced_square_sum(row_count, size),
        balanced_square_sum(column_count, size),
    )


def two_prime_frontier(
    row_count: int, column_count: int, guard: ResourceGuard
) -> dict[str, object]:
    native = row_count * column_count
    rows: list[dict[str, object]] = []
    best_denominator = -1
    best_sizes: list[int] = []
    for size in range(1, native + 1):
        guard.size_scan()
        denominator = two_prime_max_denominator(row_count, column_count, size)
        if native <= 12:
            support = balanced_support(row_count, column_count, size, guard)
            if (
                two_prime_support_energy(row_count, column_count, support)
                != denominator
            ):
                raise ArithmeticError("balanced support missed the closed maximum")
        if denominator > best_denominator:
            best_denominator = denominator
            best_sizes = [size]
        elif denominator == best_denominator:
            best_sizes.append(size)
        if native <= 12:
            rows.append(
                {
                    "size": size,
                    "row_square_sum_min": balanced_square_sum(row_count, size),
                    "column_square_sum_min": balanced_square_sum(column_count, size),
                    "maximum_denominator": denominator,
                    "optimal_dual_energy": _fraction_pair(
                        Fraction(native * native, denominator)
                    ),
                }
            )
    for size in best_sizes:
        support = balanced_support(row_count, column_count, size, guard)
        if (
            two_prime_support_energy(row_count, column_count, support)
            != best_denominator
        ):
            raise ArithmeticError(
                "optimizing balanced support missed the closed maximum"
            )
    return {
        "m": row_count,
        "n": column_count,
        "p": 2 * row_count + 1,
        "q": 2 * column_count + 1,
        "native_amplitude": native,
        "best_sizes": best_sizes,
        "best_denominator": best_denominator,
        "best_dual_energy": _fraction_pair(Fraction(native * native, best_denominator)),
        "best_density": [_fraction_pair(Fraction(size, native)) for size in best_sizes],
        "best_balanced_supports_constructed": len(best_sizes),
        "size_rows": rows,
    }


def exhaustive_two_prime_audit(
    row_count: int, column_count: int, guard: ResourceGuard
) -> dict[str, int]:
    native = row_count * column_count
    if native > 9:
        raise ValueError("two-prime exhaustive audit exceeds dimension nine")
    maxima = [-1] * (native + 1)
    for mask in range(1 << native):
        guard.subset()
        support = tuple(
            divmod(index, column_count)
            for index in range(native)
            if mask & (1 << index)
        )
        energy = two_prime_support_energy(row_count, column_count, support)
        size = len(support)
        maxima[size] = max(maxima[size], energy)
    for size in range(1, native + 1):
        if maxima[size] != two_prime_max_denominator(row_count, column_count, size):
            raise ArithmeticError("exhaustive two-prime maximum disagreed")
    return {
        "m": row_count,
        "n": column_count,
        "subsets_checked": 1 << native,
        "nonempty_sizes_checked": native,
    }


def full_grid_minus_matching(
    row_count: int, column_count: int, matching_size: int
) -> tuple[tuple[int, int], ...]:
    if not 0 <= matching_size <= min(row_count, column_count):
        raise ValueError("matching size lies outside the grid")
    deleted = {(index, index) for index in range(matching_size)}
    return tuple(
        (row, column)
        for row in range(row_count)
        for column in range(column_count)
        if (row, column) not in deleted
    )


def matching_energy_gain(row_count: int, column_count: int, matching_size: int) -> int:
    return matching_size * (
        matching_size
        + 2 * row_count * column_count
        - 2 * row_count
        - 2 * column_count
        - 3
    )


def matrix_trace(matrix: Matrix, guard: ResourceGuard) -> Fraction:
    guard.operation("matrix_trace", len(matrix))
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def matrix_total(matrix: Matrix, guard: ResourceGuard) -> Fraction:
    guard.operation("matrix_total", len(matrix) ** 2)
    return sum((entry for row in matrix for entry in row), Fraction(0))


def tensor_trace_total_closed(dimensions: Sequence[int]) -> tuple[int, int, int]:
    normalized = tuple(dimensions)
    if not normalized or any(value < 1 for value in normalized):
        raise ValueError("tensor dimensions must be positive")
    native = math.prod(normalized)
    trace = 2 ** len(normalized) * native * native
    total = native * math.prod(value + 1 for value in normalized)
    return native, trace, total


def expected_fixed_size_energy(dimensions: Sequence[int], size: int) -> Fraction:
    native, trace, total = tensor_trace_total_closed(dimensions)
    if native < 2:
        raise ValueError("random fixed-size formula requires N >= 2")
    if not 0 <= size <= native:
        raise ValueError("support size lies outside the tensor grid")
    return Fraction(size, native) * trace + Fraction(
        size * (size - 1), native * (native - 1)
    ) * (total - trace)


def exhaustive_expected_energy_audit(
    dimensions: Sequence[int], guard: ResourceGuard
) -> dict[str, object]:
    gram = tensor_gram(dimensions, guard)
    native, trace, total = tensor_trace_total_closed(dimensions)
    if matrix_trace(gram, guard) != trace or matrix_total(gram, guard) != total:
        raise ArithmeticError("tensor trace/total closed formula failed")
    rows: list[dict[str, object]] = []
    for size in range(native + 1):
        energy_sum = 0
        energies: list[int] = []
        for support in combinations(range(native), size):
            guard.subset()
            energy = sum(gram[left][right] for left in support for right in support)
            guard.operation("subset_energy_cells", size * size)
            if energy.denominator != 1:
                raise ArithmeticError("integer Gram produced fractional energy")
            energy_int = energy.numerator
            energies.append(energy_int)
            energy_sum += energy_int
        average = Fraction(energy_sum, len(energies))
        expected = expected_fixed_size_energy(dimensions, size)
        if average != expected:
            raise ArithmeticError("random fixed-size expectation failed")
        if max(energies) < expected or min(energies) > expected:
            raise ArithmeticError("average did not lie between extrema")
        rows.append(
            {
                "size": size,
                "subset_count": len(energies),
                "expected_energy": _fraction_pair(expected),
                "minimum_energy": min(energies),
                "maximum_energy": max(energies),
                "some_mask_at_least_expectation": max(energies) >= expected,
                "some_mask_exactly_expectation": expected.denominator == 1
                and expected.numerator in energies,
            }
        )
    return {
        "dimensions": list(dimensions),
        "native_amplitude": native,
        "trace": trace,
        "total_1_G_1": total,
        "rows": rows,
    }


def asymptotic_density(dimension_count: int) -> Fraction:
    if dimension_count < 1:
        raise ValueError("tensor order must be positive")
    return Fraction(2 ** (dimension_count - 1), 2**dimension_count - 1)


def asymptotic_leverage_bound(dimension_count: int) -> Fraction:
    if dimension_count < 1:
        raise ValueError("tensor order must be positive")
    return Fraction(2**dimension_count - 1, 4 ** (dimension_count - 1))


def _is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def _validate_primes(
    primes: Sequence[int], residue_class_one: bool = False
) -> tuple[int, ...]:
    normalized = tuple(primes)
    if (
        not normalized
        or len(set(normalized)) != len(normalized)
        or any(not _is_prime(prime) or prime == 2 for prime in normalized)
    ):
        raise ValueError("primes must be distinct odd primes")
    if residue_class_one and any(prime % 4 != 1 for prime in normalized):
        raise ValueError("checkerboard primes must be 1 modulo 4")
    return normalized


def legendre_pair_vector(prime: int) -> tuple[int, ...]:
    """Legendre signs on canonical representatives of {c,-c}, for p=1 mod 4."""

    normalized = _validate_primes((prime,), residue_class_one=True)[0]
    dimension = (normalized - 1) // 2
    values: list[int] = []
    for representative in range(1, dimension + 1):
        euler = pow(representative, (normalized - 1) // 2, normalized)
        sign = 1 if euler == 1 else -1 if euler == normalized - 1 else 0
        opposite = pow(normalized - representative, (normalized - 1) // 2, normalized)
        opposite_sign = 1 if opposite == 1 else -1 if opposite == normalized - 1 else 0
        if sign == 0 or sign != opposite_sign:
            raise ArithmeticError("Legendre sign did not descend to {c,-c}")
        values.append(sign)
    if sum(values) != 0 or values.count(1) != dimension // 2:
        raise ArithmeticError("Legendre pair vector is not exactly balanced")
    return tuple(values)


def tensor_vector(vectors: Sequence[Sequence[int]]) -> tuple[int, ...]:
    normalized = tuple(tuple(vector) for vector in vectors)
    if not normalized or any(not vector for vector in normalized):
        raise ValueError("tensor vectors must be nonempty")
    result = (1,)
    for vector in normalized:
        result = tuple(left * right for left in result for right in vector)
    return result


def checkerboard_closed_form(primes: Sequence[int]) -> dict[str, object]:
    normalized = _validate_primes(primes, residue_class_one=True)
    dimensions = tuple((prime - 1) // 2 for prime in normalized)
    native = math.prod(dimensions)
    constant_eigenvalue = math.prod(dimension + 1 for dimension in dimensions)
    top_eigenvalue = math.prod(normalized)
    denominator = Fraction(native * (constant_eigenvalue + top_eigenvalue), 4)
    leverage = Fraction(native * native, denominator)
    return {
        "primes": list(normalized),
        "dimensions": list(dimensions),
        "native_amplitude": native,
        "support_size": native // 2,
        "constant_tensor_eigenvalue": constant_eigenvalue,
        "all_legendre_tensor_eigenvalue": top_eigenvalue,
        "denominator": _fraction_pair(denominator),
        "sharp_restricted_leverage": _fraction_pair(leverage),
        "complete_tensor_leverage": _fraction_pair(
            Fraction(native, constant_eigenvalue)
        ),
        "closed_leverage_formula": ("4/(product_i((m_i+1)/m_i)+product_i(p_i/m_i))"),
        "uniform_positive_weight_on_support": 2,
    }


def checkerboard_exact_audit(
    primes: Sequence[int], guard: ResourceGuard
) -> dict[str, object]:
    closed = checkerboard_closed_form(primes)
    normalized = tuple(int(prime) for prime in closed["primes"])
    dimensions = tuple(int(value) for value in closed["dimensions"])
    local_vectors = tuple(legendre_pair_vector(prime) for prime in normalized)
    top_vector = tensor_vector(local_vectors)
    native = math.prod(dimensions)
    if len(top_vector) != native or sum(top_vector) != 0:
        raise ArithmeticError("all-prime Legendre tensor is not balanced")
    gram = tensor_gram(dimensions, guard)
    ones = (Fraction(1),) * native
    top = tuple(Fraction(value) for value in top_vector)
    constant_eigenvalue = math.prod(value + 1 for value in dimensions)
    top_eigenvalue = math.prod(normalized)
    if matrix_vector(gram, ones, guard) != (Fraction(constant_eigenvalue),) * native:
        raise ArithmeticError("constant tensor eigenline failed")
    if matrix_vector(gram, top, guard) != tuple(
        Fraction(top_eigenvalue) * value for value in top
    ):
        raise ArithmeticError("all-prime Legendre eigenline failed")
    support = tuple(index for index, sign in enumerate(top_vector) if sign == 1)
    indicator = tuple(Fraction(1 if index in support else 0) for index in range(native))
    denominator = quadratic_form(gram, indicator, guard)
    if (
        _fraction_pair(denominator) != closed["denominator"]
        or len(support) * 2 != native
    ):
        raise ArithmeticError("checkerboard denominator formula failed")
    optimizer = restricted_optimizer(gram, support, native, guard)
    if any(weight != [2, 1] for weight in optimizer["weights_N_G_A_1_over_E"]):
        raise ArithmeticError(
            "checkerboard optimizer is not positive uniform weight two"
        )
    representatives = tuple(product(*(range(1, value + 1) for value in dimensions)))
    retained = [
        list(coordinate)
        for coordinate, sign in zip(representatives, top_vector)
        if sign == 1
    ]
    return {
        **closed,
        "local_legendre_pair_vectors": [list(vector) for vector in local_vectors],
        "retained_canonical_pair_representatives": retained,
        "optimizer": optimizer,
        "direct_matrix_audit": True,
    }


def random_half_prefix_bound(primes: Sequence[int]) -> dict[str, object]:
    normalized = _validate_primes(primes)
    dimensions = tuple((prime - 1) // 2 for prime in normalized)
    native, trace, total = tensor_trace_total_closed(dimensions)
    if native < 2 or native % 2:
        raise ValueError("half-density prefix requires an even native dimension")
    size = native // 2
    expectation = expected_fixed_size_energy(dimensions, size)
    normalized_total = Fraction(total, native * native)
    normalized_expectation = Fraction(expectation, native * native)
    closed = (
        Fraction(2 ** len(normalized) * native, 4 * (native - 1))
        + Fraction(native - 2, 4 * (native - 1)) * normalized_total
    )
    if normalized_expectation != closed:
        raise ArithmeticError("half-density expectation simplification failed")
    return {
        "primes": list(normalized),
        "dimensions": list(dimensions),
        "d": len(normalized),
        "conductor_product_M": math.prod(normalized),
        "native_amplitude": native,
        "support_size": size,
        "b_B_over_N_squared": _fraction_pair(normalized_total),
        "normalized_expected_denominator": _fraction_pair(normalized_expectation),
        "some_mask_leverage_upper_bound": _fraction_pair(
            Fraction(native * native, expectation)
        ),
        "trace": trace,
    }


def _build_exact_mathematics(
    guard: ResourceGuard, deadline: Deadline
) -> dict[str, object]:
    # Complete finite support-size audits use only 832 two-prime masks.
    exhaustive_two_prime = [
        exhaustive_two_prime_audit(2, 3, guard),
        exhaustive_two_prime_audit(2, 4, guard),
        exhaustive_two_prime_audit(3, 3, guard),
    ]

    frontier_5_7 = two_prime_frontier(2, 3, guard)
    asymptotic_controls = [
        two_prime_frontier(10, 13, guard),
        two_prime_frontier(30, 43, guard),
    ]

    full_support = full_grid_minus_matching(2, 3, 0)
    matched_support = full_grid_minus_matching(2, 3, 2)
    full_denominator = two_prime_support_energy(2, 3, full_support)
    matched_denominator = two_prime_support_energy(2, 3, matched_support)
    gain = matching_energy_gain(2, 3, 2)
    if full_denominator != 72 or matched_denominator != 74 or gain != 2:
        raise ArithmeticError("(5,7) matching calculation failed")
    if matched_denominator - full_denominator != gain:
        raise ArithmeticError("matching energy-gain identity failed")

    gram_5_7 = tensor_gram((2, 3), guard)
    flat_support = tuple(row * 3 + column for row, column in matched_support)
    optimizer_5_7 = restricted_optimizer(gram_5_7, flat_support, 6, guard)
    if optimizer_5_7["dual_energy"] != [18, 37]:
        raise ArithmeticError("(5,7) restricted optimizer changed")

    # Verify the general gain identity on small rectangles and every matching.
    matching_controls: list[dict[str, int]] = []
    for row_count, column_count in ((2, 3), (2, 4), (3, 4)):
        full = two_prime_support_energy(
            row_count,
            column_count,
            full_grid_minus_matching(row_count, column_count, 0),
        )
        for matching_size in range(min(row_count, column_count) + 1):
            retained = full_grid_minus_matching(row_count, column_count, matching_size)
            direct_gain = (
                two_prime_support_energy(row_count, column_count, retained) - full
            )
            formula_gain = matching_energy_gain(row_count, column_count, matching_size)
            guard.operation("matching_gain_controls")
            if direct_gain != formula_gain:
                raise ArithmeticError("matching gain formula failed")
            matching_controls.append(
                {
                    "m": row_count,
                    "n": column_count,
                    "k": matching_size,
                    "gain": direct_gain,
                }
            )

    expected_controls = [
        exhaustive_expected_energy_audit((2, 3), guard),
        exhaustive_expected_energy_audit((2, 2, 2), guard),
    ]
    fractional_row = expected_controls[0]["rows"][2]
    if not isinstance(fractional_row, Mapping):
        raise TypeError("fractional refusal row is malformed")
    if fractional_row["expected_energy"] != [216, 5]:
        raise ArithmeticError("fractional expectation control changed")
    if fractional_row["some_mask_exactly_expectation"] is not False:
        raise ArithmeticError("fractional expectation was falsely attained")

    fixed_d_table = [
        {
            "d": tensor_order,
            "limiting_density": _fraction_pair(asymptotic_density(tensor_order)),
            "limiting_leverage_upper_bound": _fraction_pair(
                asymptotic_leverage_bound(tensor_order)
            ),
        }
        for tensor_order in range(1, 6)
    ]
    checkerboard_5_13 = checkerboard_exact_audit((5, 13), guard)
    checkerboard_closed_controls = [
        checkerboard_closed_form((5, 13)),
        checkerboard_closed_form((5, 13, 17)),
    ]
    if checkerboard_5_13["sharp_restricted_leverage"] != [24, 43]:
        raise ArithmeticError("(5,13) checkerboard leverage changed")
    if checkerboard_closed_controls[1]["sharp_restricted_leverage"] != [192, 647]:
        raise ArithmeticError("(5,13,17) checkerboard leverage changed")

    odd_prefix_controls = [
        random_half_prefix_bound(
            tuple(prime for prime in range(3, limit + 1) if _is_prime(prime))
        )
        for limit in (5, 13, 29, 43)
    ]
    deadline.check("after exact mathematics")
    return {
        "restricted_support_optimizer": {
            "domain": (
                "every nonempty joint support A of a tensor Gram G and every "
                "real or complex weight vector alpha with 1^*alpha=N"
            ),
            "sharp_energy": "N^2/(1_A^*G_A*1_A)",
            "unique_extremizer": ("alpha=N*G_A*1_A/(1_A^*G_A*1_A)"),
            "proof": (
                "|1^*alpha|^2 <= (1^*G_A*1)*(alpha^*G_A^(-1)*alpha), "
                "with equality in weighted Cauchy-Schwarz exactly at the displayed alpha"
            ),
        },
        "two_prime_theorem": {
            "setup": ("p=2m+1, q=2n+1, G=(pI_m-J_m) tensor (qI_n-J_n)"),
            "support_energy": ("E_A=p*q*s+s^2-p*sum_i(r_i^2)-q*sum_j(c_j^2)"),
            "balanced_square_sum": ("if s=a*t+b with 0<=b<t, R_t(s)=t*a^2+b*(2a+1)"),
            "fixed_size_maximum": ("E_max(s)=p*q*s+s^2-p*R_m(s)-q*R_n(s)"),
            "existence": (
                "balanced row and column degrees satisfy Gale-Ryser; "
                "the producer also constructs them by bipartite Havel-Hakimi"
            ),
            "search_reduction": (
                "the 2^(m*n) support search reduces exactly to m*n nonempty sizes"
            ),
            "matching_gain": ("E_(full-minus-k-matching)-E_full=k*(k+2*m*n-2*m-2*n-3)"),
            "distinct_prime_corollary": (
                "for distinct p,q>=5, m,n>=2 are distinct and k=2 gives "
                "2*(2*(m-1)*(n-1)-3)>0"
            ),
            "asymptotic": (
                "as m,n tend to infinity, every optimal density tends to 2/3 "
                "and the optimal restricted leverage tends to 3/4"
            ),
            "limit_profile": "E_max(floor(rho*m*n))/(m*n)^2 -> 4*rho-3*rho^2 uniformly",
        },
        "five_seven_example": {
            "full_denominator": full_denominator,
            "full_leverage": [1, 2],
            "deleted_matching": [[0, 0], [1, 1]],
            "retained_coordinates": [list(cell) for cell in matched_support],
            "matching_gain": gain,
            "restricted_denominator": matched_denominator,
            "restricted_leverage": [18, 37],
            "optimizer": optimizer_5_7,
        },
        "arbitrary_d_expected_energy": {
            "setup": (
                "G=tensor_i((2*m_i+1)I_(m_i)-J_(m_i)), "
                "N=product_i m_i, and A is uniform among size-s supports"
            ),
            "trace": "Tr(G)=2^d*N^2",
            "total": "B=1^*G*1=N*product_i(m_i+1)",
            "expectation": ("E[E_A]=(s/N)*Tr(G)+s*(s-1)/(N*(N-1))*(B-Tr(G))"),
            "existence_consequence": (
                "some size-s mask has E_A at least the expectation, hence "
                "restricted leverage at most N^2/E[E_A]"
            ),
            "equality_correction": (
                "an individual mask need not equal the expectation; energies are "
                "integral while the exact average can be fractional"
            ),
            "fixed_d_asymptotic": (
                "if d is fixed and min_i m_i tends to infinity, choose density "
                "2^(d-1)/(2^d-1); some masks have leverage at most "
                "(2^d-1)/4^(d-1)+o(1)"
            ),
            "limit_profile": (
                "2^d*rho-(2^d-1)*rho^2, maximized at rho=2^(d-1)/(2^d-1)"
            ),
            "fractional_refusal_example": {
                "dimensions": [2, 3],
                "size": 2,
                "expected_energy": [216, 5],
                "individual_energies_are_integers": True,
                "exact_attainment": False,
            },
            "fixed_d_table": fixed_d_table,
        },
        "global_legendre_checkerboard": {
            "domain": "every finite set of distinct primes p_i congruent to 1 modulo 4",
            "coordinate_contract": (
                "L-106024 labels each local coordinate by an unordered pair {c,-c}; "
                "the Legendre symbol descends because (-1|p_i)=+1 and is balanced"
            ),
            "support": (
                "under CRT, retain exactly the tuples with product_i(c_i|p_i)=+1; "
                "this is the quadratic-residue/Jacobi parity checkerboard"
            ),
            "spectral_mechanism": (
                "a=(1+w)/2 has Fourier support only on the constant tensor line "
                "and the all-primes Legendre line; G*w=(product_i p_i)*w"
            ),
            "denominator": ("E_A=N/4*(product_i(m_i+1)+product_i(p_i))"),
            "sharp_leverage": ("4/(product_i((m_i+1)/m_i)+product_i(p_i/m_i))"),
            "positive_optimizer": (
                "G_A*1_A is constant, so the sharp weights are uniformly +2 on A; "
                "the gain uses no signed cancellation"
            ),
            "contrast_with_product_masks": (
                "local/product deletions populate lower-order tensor modes and obey "
                "the frozen mask no-go; global parity cancels every lower-order mode "
                "and reaches the all-primes top eigenvalue"
            ),
            "direct_control": checkerboard_5_13,
            "closed_controls": checkerboard_closed_controls,
        },
        "growing_prime_prefix_corollaries": {
            "all_odd_primes_random_mask": {
                "setup": "p ranges over 3<=p<=x, d=pi(x)-1, M=product p, s=N/2",
                "exact_normalized_average": (
                    "2^d*N/(4*(N-1)) + b*(N-2)/(4*(N-1)), b=product_p((p+1)/(p-1))"
                ),
                "finite_existence": (
                    "some half-density formal mask has denominator at least this average"
                ),
                "imported_asymptotics": (
                    "Mertens gives b~C*(log x)^2; PNT gives log M~x and d~x/log x"
                ),
                "leverage": (
                    "at most 2^(2-d)*(1+o(1))="
                    "exp(-(log 2+o(1))*log M/log log M)="
                    "M^(-log 2/log log M+o(1/log log M))"
                ),
                "controls": odd_prefix_controls,
            },
            "one_mod_four_explicit_checkerboard": {
                "setup": "p<=x, p congruent to 1 modulo 4, d=pi(x;4,1)",
                "exact_bound": ("sharp leverage < 2^(2-d), since every p_i/m_i>2"),
                "imported_asymptotics": (
                    "PNT in the progression 1 mod 4 gives log M~x/2 and "
                    "d~x/(2 log x)~log M/log log M"
                ),
                "conductor_form": ("M^(-log 2/log log M+o(1/log log M))"),
                "realization": (
                    "explicit on the fixed source-owned CRT tensor coordinates; "
                    "not an owner-varying FFPS condition or global moment theorem"
                ),
            },
            "comparison": (
                "both formal correlated bounds are subpolynomial in M but far smaller "
                "than the complete tensor's order (log log M)^(-2) leverage"
            ),
        },
        "finite_controls": {
            "exhaustive_two_prime": exhaustive_two_prime,
            "frontier_5_7": frontier_5_7,
            "asymptotic_two_prime": asymptotic_controls,
            "matching": matching_controls,
            "random_fixed_size": expected_controls,
            "checkerboard_5_13": checkerboard_5_13,
            "odd_prime_prefix_half_density": odd_prefix_controls,
        },
    }


def _read_locked_sources(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    parsed: dict[str, dict[str, object]] = {}
    manifest: list[dict[str, object]] = []
    for name, lock in SOURCE_LOCKS.items():
        deadline.check(f"before source {name}")
        path = lock.get("path")
        if not isinstance(path, Path):
            raise TypeError(f"source path is not a Path: {name}")
        size = path.stat().st_size
        guard.source(size)
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"source size changed while reading: {name}")
        if _lf_sha256_bytes(raw) != lock.get("lf_sha256"):
            raise RuntimeError(f"source LF hash mismatch: {name}")
        if _git_blob_sha1(raw) != lock.get("git_blob"):
            raise RuntimeError(f"source git-blob mismatch: {name}")
        row: dict[str, object] = {
            "id": name,
            "path": _relative(path),
            "commit": lock["commit"],
            "git_blob": lock["git_blob"],
            "lf_sha256": lock["lf_sha256"],
            "bytes": size,
            "role": lock["role"],
        }
        if path.suffix == ".json":
            value = json.loads(raw.decode("utf-8"))
            if not isinstance(value, dict):
                raise TypeError(f"source JSON is not an object: {name}")
            if value.get("schema") != lock.get("schema"):
                raise RuntimeError(f"source schema mismatch: {name}")
            pinned_payload = lock.get("payload_sha256")
            if pinned_payload is not None:
                payload = dict(value)
                claimed = payload.pop("payload_sha256", None)
                if claimed != pinned_payload or claimed != _canonical_sha256(payload):
                    raise RuntimeError(f"source payload mismatch: {name}")
                row["payload_sha256"] = pinned_payload
            parsed[name] = value
            row["schema"] = lock["schema"]
        manifest.append(row)
        deadline.check(f"after source {name}")
    if guard.source_files != len(SOURCE_LOCKS):
        raise RuntimeError("not every frozen source was consumed")
    return parsed, manifest


def _validate_source_semantics(
    sources: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    principal = sources["principal_json"]
    local_theorem = principal.get("principal_leverage_theorem")
    source_frontier = principal.get("source_frontier")
    if not isinstance(local_theorem, Mapping) or not isinstance(
        source_frontier, Mapping
    ):
        raise TypeError("principal leverage source lost its theorem or frontier")
    if local_theorem.get("local_formula") != "||O_p||^2=(p-1)/(p+1)":
        raise RuntimeError("local leverage formula changed")
    blob_ids = source_frontier.get("git_blob_ids")
    if not isinstance(blob_ids, Mapping) or blob_ids.get("L-106024") != (
        LIVE_L106024_BLOB
    ):
        raise RuntimeError("principal source lost the frozen L-106024 Gram blob")

    mask = sources["mask_json"]
    mask_theorem = mask.get("theorem")
    if not isinstance(
        mask_theorem, Mapping
    ) or "pure masks worsen every local factor" not in str(
        mask_theorem.get("tensor_corollary")
    ):
        raise RuntimeError("product-mask theorem changed")

    frontier = sources["frontier_json"]
    frontier_scope = frontier.get("scope")
    budget = frontier.get("exact_budget_theorem")
    if not isinstance(frontier_scope, Mapping) or not isinstance(budget, Mapping):
        raise TypeError("tensor frontier source is malformed")
    if (
        frontier_scope.get("source_realization_of_every_formal_tensor_proved")
        is not False
    ):
        raise RuntimeError("tensor source-realization firewall changed")

    signed = sources["signed_json"]
    if signed.get("status") != "EXACT_ALL_FINITE_MARKED_PRIME_COMPLETE_FRAME_NO_GO":
        raise RuntimeError("signed complete-frame theorem status changed")
    signed_scope = signed.get("scope")
    warning = signed.get("correlated_joint_deletion_counterexample")
    signed_frontier = signed.get("source_frontier")
    if not isinstance(signed_scope, Mapping) or not isinstance(warning, Mapping):
        raise TypeError("signed theorem scope or warning is missing")
    if (
        signed_scope.get("arbitrary_correlated_restricted_gram_deletion_ruled_out")
        is not False
    ):
        raise RuntimeError("signed theorem silently swallowed the correlated loophole")
    if warning.get("restricted_optimal_dual_energy") != [18, 37]:
        raise RuntimeError("signed (5,7) seed example changed")
    if not isinstance(signed_frontier, Mapping):
        raise TypeError("signed live frontier is missing")
    live = signed_frontier.get("live_audit")
    if not isinstance(live, Mapping) or live.get("head_commit") != LIVE_PR_751_HEAD:
        raise RuntimeError("live PR #751 audit head changed")
    live_blobs = live.get("git_blob_ids")
    if not isinstance(live_blobs, Mapping) or live_blobs.get("L-106024") != (
        LIVE_L106024_BLOB
    ):
        raise RuntimeError("live PR #751 L-106024 Gram blob changed")
    return {
        "live_pr": 751,
        "live_audited_head": LIVE_PR_751_HEAD,
        "live_L_106024_blob": LIVE_L106024_BLOB,
        "local_gram_unchanged": True,
        "relationship_to_signed_packet": (
            "the committed signed packet closes the complete inverse-metric "
            "problem and explicitly leaves correlated restricted-Gram deletion open; "
            "the present theorem is logically independent and closes that formal optimization"
        ),
        "relationship_to_local_mask_packet": (
            "the local/product-mask no-go remains valid; the improvement requires "
            "a non-product joint support"
        ),
        "relationship_to_frontier": (
            "the existing conductor frontier concerns the unmasked complete tensor; "
            "formal correlated masks do not by themselves alter its arithmetic realization"
        ),
    }


def _packet_lf_sha256(path: Path) -> str:
    size = path.stat().st_size
    if size > MAX_PACKET_FILE_BYTES:
        raise RuntimeError(f"packet file exceeds byte cap: {path.name}")
    return _lf_sha256_bytes(path.read_bytes())


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()
    exact_math = _build_exact_mathematics(guard, deadline)
    operations_before_sources = guard.exact_operations
    subsets_before_sources = guard.enumerated_subsets
    sources, source_manifest = _read_locked_sources(guard, deadline)
    source_relationship = _validate_source_semantics(sources)
    if guard.exact_operations != operations_before_sources:
        raise RuntimeError("source validation entered the exact-math operation ledger")
    if guard.enumerated_subsets != subsets_before_sources:
        raise RuntimeError("source validation entered the finite-control subset ledger")
    deadline.check("before fixture assembly")
    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_correlated_mask_amplifier.v1",
        "status": "EXACT_FORMAL_CORRELATED_RESTRICTED_GRAM_OPTIMIZATION",
        "scope": {
            "formal_tensor_gram": ("G=tensor_i((2*m_i+1)I_(m_i)-J_(m_i))"),
            "weights": "arbitrary real or complex scalars on a retained joint support",
            "two_prime_fixed_size_theorem": "all positive integers m,n",
            "prime_corollary": "every pair of distinct odd primes p,q>=5",
            "arbitrary_d_expectation": "every tensor order d with N>=2",
            "checkerboard": "every finite set of distinct primes p congruent to 1 mod 4",
            "prime_prefix_asymptotics": (
                "formal consequences of the exact bounds plus classical Mertens, "
                "PNT, and PNT in the fixed progression 1 mod 4"
            ),
            "finite_fields_enumerated": 0,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "l_functions_enumerated": 0,
            "random_samples": 0,
        },
        "exact_mathematics": exact_math,
        "source_relationship": source_relationship,
        "source_manifest": source_manifest,
        "firewalls": [
            (
                "An arbitrary subset of joint sign-pair coordinates is a formal "
                "restricted-Gram mask; the packet does not construct an arithmetic "
                "condition realizing that subset in corrected FFPS."
            ),
            (
                "The Legendre checkerboard is explicitly realizable on one fixed "
                "source-owned CRT tensor of unordered {c,-c} coordinates. This does "
                "not realize it across varying owners or conductors."
            ),
            (
                "The exact random-fixed-size formula is an expectation. It proves "
                "existence of a mask with energy at least the average, not exact "
                "attainment of a generally fractional average."
            ),
            (
                "The signed complete-frame no-go and this restricted-Gram gain use "
                "different metrics: a principal block of G^(-1) is not generally "
                "the inverse of the corresponding principal block of G."
            ),
            (
                "No global FFPS mixed, double, centered-incidence, or principal "
                "moment is proved; no conductor loss is paid."
            ),
            (
                "No principal member is individualized, and no RH or GRH statement "
                "is proved."
            ),
            (
                "The fixed-d asymptotic is not uniform in growing d and is not a "
                "global compatible-system or Euler-product theorem."
            ),
            (
                "The growing-d prime-prefix corollaries are separate exact half-density "
                "bounds plus imported classical prime asymptotics; they prove no "
                "WCADD, WCKUM, BPOE, SOCM, or global FFPS moment estimate."
            ),
            "No external novelty claim is made.",
        ],
        "packet_manifest": {
            "producer": {
                "path": _relative(SCRIPT_PATH),
                "lf_sha256": _packet_lf_sha256(SCRIPT_PATH),
            },
            "note": {
                "path": _relative(NOTE_PATH),
                "lf_sha256": _packet_lf_sha256(NOTE_PATH),
            },
            "test": {
                "path": _relative(TEST_PATH),
                "lf_sha256": _packet_lf_sha256(TEST_PATH),
            },
        },
        "resource_contract": {
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operations_before_sources": operations_before_sources,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_matrix_cells": MAX_MATRIX_CELLS,
            "actual_matrix_cells": guard.matrix_cells,
            "maximum_enumerated_subsets": MAX_ENUMERATED_SUBSETS,
            "actual_enumerated_subsets": guard.enumerated_subsets,
            "subsets_before_sources": subsets_before_sources,
            "maximum_two_prime_size_scan": MAX_TWO_PRIME_SIZE_SCAN,
            "actual_two_prime_size_scan": guard.two_prime_sizes,
            "maximum_tensor_dimension": MAX_TENSOR_DIMENSION,
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers and rational numbers only; no floats",
        },
    }
    deadline.check("after fixture assembly")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _render(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="refuse unless the fixture is current"
    )
    arguments = parser.parse_args(argv)
    rendered = _render(build_fixture()).encode("utf-8")
    if len(rendered) > MAX_PACKET_FILE_BYTES:
        raise RuntimeError("rendered fixture exceeds the packet-file byte cap")
    if arguments.check:
        if not OUTPUT_PATH.is_file():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        if OUTPUT_PATH.stat().st_size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError("existing fixture exceeds the packet-file byte cap")
        if OUTPUT_PATH.read_bytes() != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
        print("PASS_FFPS_CORRELATED_MASK_AMPLIFIER")
        return 0
    OUTPUT_PATH.write_bytes(rendered)
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
