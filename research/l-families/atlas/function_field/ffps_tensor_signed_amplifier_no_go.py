#!/usr/bin/env python3
"""Exact signed-amplifier no-go for the corrected FFPS tensor phase frame.

For a finite set S of distinct odd marked primes, the formal complete phase
Gram is the Kronecker product of G_p=pI-J on m_p=(p-1)/2 coordinates.  This
producer proves, in exact Gaussian-rational arithmetic, that every complex
weight alpha preserving the native constant-packet amplitude satisfies

    alpha* G_S^(-1) alpha
      = product_(p in S) (p-1)/(p+1)
        + (alpha-1)* G_S^(-1) (alpha-1).

It also resolves the excess into exact tensor modes.  Tiny panels are used as
falsification controls only.  The self-contained operator proof closes before
the corrected PR #751 dependencies are read and source-locked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path

Gaussian = tuple[Fraction, Fraction]
RealMatrix = tuple[tuple[Fraction, ...], ...]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_tensor_signed_amplifier_no_go.json"
NOTE_PATH = HERE / "FFPS_TENSOR_SIGNED_AMPLIFIER_NO_GO.md"
TEST_PATH = ROOT / "tests" / "test_ffps_tensor_signed_amplifier_no_go.py"

PR_751 = 751
DEPENDENCY_SNAPSHOT_COMMIT_751 = "37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2"
DEPENDENCY_SOURCE_BLOBS_751 = {
    "T-106121": "55afc90eaf7d2cd3efa102bcc97b927943731d48",
    "L-106024": "d94787dc2cd1cedd74d33ddc6269daf8de1cc061",
    "R-106122": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
    "R-106123": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
    "L-106126": "b4dbebde403a11696c56a4689b2df8b53326a157",
}
LIVE_AUDITED_HEAD_751 = "98af0db6ec7f77d6333a77a3dac53c4698852f43"
LIVE_SOURCE_BLOBS_751 = {
    "T-106121": "9111983ae4bf199a8315310a9ce090561430c33b",
    "L-106024": "d94787dc2cd1cedd74d33ddc6269daf8de1cc061",
    "R-106122": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
    "R-106123": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
    "L-106126": "b4dbebde403a11696c56a4689b2df8b53326a157",
    "R-106131": "8dde14dd382e0c4fc1bb54d5da21de85ea002f41",
    "L-106131": "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    "T-106140": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
LIVE_GATE_STATUS_751 = {
    "BTPS106121": "OPEN / SUFFICIENT PRINCIPAL POSITIVE MOMENT",
    "BTMS106121": "WITHDRAWN / UNCENTERED NONPRINCIPAL DIAGONAL NOT PAID",
    "BTDS106121": "WITHDRAWN / UNCENTERED NONPRINCIPAL DIAGONAL NOT PAID",
    "WCADD106140": "OPEN / RH-BEARING WITH WCKUM106140",
    "WCKUM106140": "OPEN / RH-BEARING WITH WCADD106140",
    "preferred_live_repair": "T-106140 WICK-CENTERED ADDITIVE/KUMMER CONJUNCTION",
}

PRINCIPAL_JSON_PATH = HERE / "ffps_principal_leverage.json"
PRINCIPAL_NOTE_PATH = HERE / "FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md"
MASK_JSON_PATH = HERE / "ffps_conditioned_mask_no_go.json"
MASK_NOTE_PATH = HERE / "FFPS_CONDITIONED_MASK_NO_GO.md"
FRONTIER_JSON_PATH = HERE / "ffps_coherent_tensor_cost_frontier.json"
FRONTIER_NOTE_PATH = HERE / "FFPS_COHERENT_TENSOR_COST_FRONTIER.md"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "principal_json": {
        "path": PRINCIPAL_JSON_PATH,
        "sha256_lf": "cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3",
        "git_blob": "d96cd12a5fbfe86b63d9c6b7076c8a99aa139f4c",
        "kind": "json",
        "schema": "riemann.function_field.ffps_principal_leverage.v2",
        "role": "corrected complete local phase Gram and tensor leverage",
    },
    "principal_note": {
        "path": PRINCIPAL_NOTE_PATH,
        "sha256_lf": "6b3a0958422f01b44b7702b1088f4e13926d5d11a7725bde2582cd2d371b07e6",
        "git_blob": "e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a",
        "kind": "text",
        "role": "corrected physical-squareclass interpretation and scope firewall",
    },
    "conditioned_mask_json": {
        "path": MASK_JSON_PATH,
        "sha256_lf": "fe6024020775e977e3dfe31822137b579c9cef438f9e94666714179ed43d469b",
        "git_blob": "1aa8ea28e164a8389b66b6b780d5e081e6a96848",
        "kind": "json",
        "schema": "riemann.function_field.ffps_conditioned_mask_no_go.v1",
        "role": "complementary local/product-mask restricted-Gram no-go",
    },
    "conditioned_mask_note": {
        "path": MASK_NOTE_PATH,
        "sha256_lf": "0a3d7d30780b48de82bb2203e1b1ff0eed7912e348b91be329bc202f945b0524",
        "git_blob": "c300500a1563c5299f3ddffd47571309511bb563",
        "kind": "text",
        "role": "restricted metric versus complete metric distinction",
    },
    "tensor_frontier_json": {
        "path": FRONTIER_JSON_PATH,
        "sha256_lf": "f6b65bb4a8cdaaa7c91464d8fba86b7691350bf14cdcc8a68c90848be6f89d51",
        "git_blob": "eb21ae1cdd158395d3547b946f2ee25a84e23e05",
        "kind": "json",
        "schema": "riemann.function_field.ffps_coherent_tensor_cost_frontier.v1",
        "role": "formal coherent tensor cost frontier",
    },
    "tensor_frontier_note": {
        "path": FRONTIER_NOTE_PATH,
        "sha256_lf": "037ec4751504d2387a87e606dbd8eb74dbcc3abb554ccb77ee449fd838a4583e",
        "git_blob": "292487efca3df3971518edba0c0b23b830be2c16",
        "kind": "text",
        "role": "conductor-cost scope and non-individualization firewall",
    },
}

CONTROL_PANELS = ((5, 7), (3, 5, 7))
MAX_CONTROL_PRIME = 31
MAX_TENSOR_DIMENSION = 16
MAX_MATRIX_CELLS = 32_768
MAX_EXACT_OPERATIONS = 250_000
MAX_SOURCE_FILES = 6
MAX_SOURCE_BYTES = 500_000
MAX_WALL_SECONDS = 5.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    matrix_cells: int = 0
    source_files: int = 0
    source_bytes: int = 0

    def operation(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("operation increment must be a nonnegative integer")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount

    def matrix(self, rows: int, columns: int) -> None:
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in (rows, columns)
        ):
            raise ValueError("matrix dimensions must be nonnegative")
        amount = rows * columns
        if self.matrix_cells + amount > MAX_MATRIX_CELLS:
            raise RuntimeError("matrix-cell cap exceeded")
        self.matrix_cells += amount

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("source byte count must be nonnegative")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count


@dataclass(frozen=True)
class ModePenalty:
    active_primes: tuple[int, ...]
    multiplicity: int
    eigenvalue: Fraction
    euclidean_norm_squared: Fraction
    dual_penalty: Fraction
    vector: tuple[Gaussian, ...]


@dataclass(frozen=True)
class AmplifierAnalysis:
    primes: tuple[int, ...]
    dimension: int
    direct_energy: Fraction
    coherent_baseline: Fraction
    excess_energy: Fraction
    mode_penalty_sum: Fraction
    modes: tuple[ModePenalty, ...]
    beta: tuple[Gaussian, ...]


def gaussian(real: int | Fraction = 0, imag: int | Fraction = 0) -> Gaussian:
    return Fraction(real), Fraction(imag)


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_sub(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] - right[0], left[1] - right[1]


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def g_conjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def g_scale(value: Gaussian, scalar: int | Fraction) -> Gaussian:
    factor = Fraction(scalar)
    return value[0] * factor, value[1] * factor


def g_sum(values: Sequence[Gaussian]) -> Gaussian:
    result = gaussian()
    for value in values:
        result = g_add(result, value)
    return result


def _fraction_pair(value: int | Fraction) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _gaussian_pairs(value: Gaussian) -> dict[str, list[int]]:
    return {"real": _fraction_pair(value[0]), "imaginary": _fraction_pair(value[1])}


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
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


def _lf_sha256(path: Path) -> str:
    raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(raw).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _validate_panel(primes: Sequence[int]) -> tuple[int, ...]:
    panel = tuple(primes)
    if not panel:
        raise ValueError("a nonempty marked-prime panel is required")
    if any(isinstance(prime, bool) or not isinstance(prime, int) for prime in panel):
        raise ValueError("marked primes must be integers")
    if len(set(panel)) != len(panel):
        raise ValueError("marked primes must be distinct")
    if any(prime > MAX_CONTROL_PRIME for prime in panel):
        raise ValueError("control prime exceeds the declared cap")
    if any(not _is_prime(prime) or prime == 2 for prime in panel):
        raise ValueError("tensor coordinates require distinct odd primes")
    dimension = 1
    for prime in panel:
        dimension *= (prime - 1) // 2
        if dimension > MAX_TENSOR_DIMENSION:
            raise ValueError("tensor dimension exceeds the declared control cap")
    return panel


def local_dimension(prime: int) -> int:
    _validate_panel((prime,))
    return (prime - 1) // 2


def tensor_dimension(primes: Sequence[int]) -> int:
    dimension = 1
    for prime in _validate_panel(primes):
        dimension *= (prime - 1) // 2
    return dimension


def coherent_baseline(primes: Sequence[int]) -> Fraction:
    result = Fraction(1)
    for prime in _validate_panel(primes):
        result *= Fraction(prime - 1, prime + 1)
    return result


def local_gram(prime: int, guard: ResourceGuard | None = None) -> RealMatrix:
    dimension = local_dimension(prime)
    resource = ResourceGuard() if guard is None else guard
    resource.matrix(dimension, dimension)
    resource.operation(dimension * dimension)
    return tuple(
        tuple(
            Fraction(prime - 1 if row == column else -1) for column in range(dimension)
        )
        for row in range(dimension)
    )


def local_inverse(prime: int, guard: ResourceGuard | None = None) -> RealMatrix:
    dimension = local_dimension(prime)
    resource = ResourceGuard() if guard is None else guard
    resource.matrix(dimension, dimension)
    resource.operation(2 * dimension * dimension)
    j_coefficient = Fraction(2, prime * (prime + 1))
    return tuple(
        tuple(
            Fraction(row == column, prime) + j_coefficient
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def constant_projector(prime: int, guard: ResourceGuard | None = None) -> RealMatrix:
    dimension = local_dimension(prime)
    resource = ResourceGuard() if guard is None else guard
    resource.matrix(dimension, dimension)
    resource.operation(dimension * dimension)
    value = Fraction(1, dimension)
    return tuple(tuple(value for _ in range(dimension)) for _ in range(dimension))


def sum_zero_projector(prime: int, guard: ResourceGuard | None = None) -> RealMatrix:
    constant = constant_projector(prime, guard)
    dimension = len(constant)
    resource = ResourceGuard() if guard is None else guard
    resource.operation(dimension * dimension)
    return tuple(
        tuple(
            Fraction(row == column) - constant[row][column]
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def kronecker_matrix(
    left: RealMatrix, right: RealMatrix, guard: ResourceGuard | None = None
) -> RealMatrix:
    if (
        not left
        or not right
        or any(len(row) != len(left[0]) for row in left)
        or any(len(row) != len(right[0]) for row in right)
    ):
        raise ValueError("Kronecker factors must be nonempty rectangular matrices")
    rows = len(left) * len(right)
    columns = len(left[0]) * len(right[0])
    if max(rows, columns) > MAX_TENSOR_DIMENSION:
        raise ValueError("Kronecker result exceeds the tensor-dimension cap")
    resource = ResourceGuard() if guard is None else guard
    resource.matrix(rows, columns)
    resource.operation(rows * columns)
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def _tensor_matrix(
    primes: Sequence[int], local_builder: object, guard: ResourceGuard
) -> RealMatrix:
    panel = _validate_panel(primes)
    matrix: RealMatrix = ((Fraction(1),),)
    for prime in panel:
        if local_builder == "gram":
            local = local_gram(prime, guard)
        elif local_builder == "inverse":
            local = local_inverse(prime, guard)
        else:
            raise ValueError("unknown tensor matrix builder")
        matrix = kronecker_matrix(matrix, local, guard)
    return matrix


def tensor_gram(
    primes: Sequence[int], guard: ResourceGuard | None = None
) -> RealMatrix:
    resource = ResourceGuard() if guard is None else guard
    return _tensor_matrix(primes, "gram", resource)


def tensor_inverse(
    primes: Sequence[int], guard: ResourceGuard | None = None
) -> RealMatrix:
    resource = ResourceGuard() if guard is None else guard
    return _tensor_matrix(primes, "inverse", resource)


def matrix_multiply(
    left: RealMatrix, right: RealMatrix, guard: ResourceGuard | None = None
) -> RealMatrix:
    if (
        not left
        or not right
        or any(len(row) != len(left[0]) for row in left)
        or any(len(row) != len(right[0]) for row in right)
    ):
        raise ValueError("matrix factors must be nonempty and rectangular")
    if len(left[0]) != len(right):
        raise ValueError("matrix-product dimension mismatch")
    resource = ResourceGuard() if guard is None else guard
    resource.matrix(len(left), len(right[0]))
    resource.operation(2 * len(left) * len(right) * len(right[0]))
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_vector(
    matrix: RealMatrix,
    vector: Sequence[Gaussian],
    guard: ResourceGuard | None = None,
) -> tuple[Gaussian, ...]:
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("matrix-vector dimension mismatch")
    resource = ResourceGuard() if guard is None else guard
    resource.operation(3 * len(matrix) * len(vector))
    return tuple(
        g_sum(
            tuple(
                g_scale(value, coefficient) for coefficient, value in zip(row, vector)
            )
        )
        for row in matrix
    )


def euclidean_inner(
    left: Sequence[Gaussian],
    right: Sequence[Gaussian],
    guard: ResourceGuard | None = None,
) -> Gaussian:
    if len(left) != len(right):
        raise ValueError("inner-product dimension mismatch")
    resource = ResourceGuard() if guard is None else guard
    resource.operation(4 * len(left))
    return g_sum(tuple(g_mul(g_conjugate(a), b) for a, b in zip(left, right)))


def euclidean_norm_squared(
    vector: Sequence[Gaussian], guard: ResourceGuard | None = None
) -> Fraction:
    value = euclidean_inner(vector, vector, guard)
    if value[1] != 0 or value[0] < 0:
        raise ArithmeticError(
            "Hermitian Euclidean norm failed exact reality/positivity"
        )
    return value[0]


def hermitian_energy(
    inverse: RealMatrix,
    vector: Sequence[Gaussian],
    guard: ResourceGuard | None = None,
) -> Fraction:
    resource = ResourceGuard() if guard is None else guard
    applied = matrix_vector(inverse, vector, resource)
    value = euclidean_inner(vector, applied, resource)
    if value[1] != 0 or value[0] < 0:
        raise ArithmeticError("dual energy failed exact reality/positivity")
    return value[0]


def tensor_vector(local_vectors: Sequence[Sequence[Gaussian]]) -> tuple[Gaussian, ...]:
    if not local_vectors or any(not vector for vector in local_vectors):
        raise ValueError("tensor vector needs nonempty local factors")
    result = (gaussian(1),)
    for factor in local_vectors:
        result = tuple(g_mul(left, right) for left in result for right in factor)
        if len(result) > MAX_TENSOR_DIMENSION:
            raise ValueError("tensor vector exceeds the dimension cap")
    return result


def mode_eigenvalue(primes: Sequence[int], active_primes: Sequence[int]) -> Fraction:
    panel = _validate_panel(primes)
    active = tuple(active_primes)
    if len(set(active)) != len(active) or any(prime not in panel for prime in active):
        raise ValueError("active modes must be a subset of the marked panel")
    active_set = set(active)
    result = Fraction(1)
    for prime in panel:
        result *= prime if prime in active_set else Fraction(prime + 1, 2)
    return result


def mode_multiplicity(primes: Sequence[int], active_primes: Sequence[int]) -> int:
    panel = _validate_panel(primes)
    active = tuple(active_primes)
    if len(set(active)) != len(active) or any(prime not in panel for prime in active):
        raise ValueError("active modes must be a subset of the marked panel")
    active_set = set(active)
    result = 1
    for prime in panel:
        if prime in active_set:
            result *= local_dimension(prime) - 1
    return result


def mode_projector(
    primes: Sequence[int],
    active_primes: Sequence[int],
    guard: ResourceGuard | None = None,
) -> RealMatrix:
    panel = _validate_panel(primes)
    active = tuple(active_primes)
    if len(set(active)) != len(active) or any(prime not in panel for prime in active):
        raise ValueError("active modes must be a subset of the marked panel")
    resource = ResourceGuard() if guard is None else guard
    active_set = set(active)
    projector: RealMatrix = ((Fraction(1),),)
    for prime in panel:
        local = (
            sum_zero_projector(prime, resource)
            if prime in active_set
            else constant_projector(prime, resource)
        )
        projector = kronecker_matrix(projector, local, resource)
    return projector


def _all_mode_subsets(primes: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        subset
        for size in range(len(primes) + 1)
        for subset in combinations(primes, size)
    )


def analyze_amplifier(
    primes: Sequence[int],
    alpha: Sequence[Gaussian],
    guard: ResourceGuard | None = None,
) -> AmplifierAnalysis:
    panel = _validate_panel(primes)
    dimension = tensor_dimension(panel)
    values = tuple((Fraction(value[0]), Fraction(value[1])) for value in alpha)
    if len(values) != dimension:
        raise ValueError("amplifier has the wrong tensor dimension")
    if g_sum(values) != gaussian(dimension):
        raise ValueError("amplifier must preserve the native principal amplitude")
    resource = ResourceGuard() if guard is None else guard
    inverse = tensor_inverse(panel, resource)
    gram = tensor_gram(panel, resource)
    beta = tuple(g_sub(value, gaussian(1)) for value in values)
    baseline = coherent_baseline(panel)
    direct = hermitian_energy(inverse, values, resource)
    excess = hermitian_energy(inverse, beta, resource)
    if direct != baseline + excess:
        raise ArithmeticError("exact amplifier Pythagorean identity failed")

    mode_rows = []
    reconstruction = [gaussian() for _ in range(dimension)]
    for active in _all_mode_subsets(panel):
        projector = mode_projector(panel, active, resource)
        component = matrix_vector(projector, beta, resource)
        for index, value in enumerate(component):
            reconstruction[index] = g_add(reconstruction[index], value)
        norm = euclidean_norm_squared(component, resource)
        eigenvalue = mode_eigenvalue(panel, active)
        gram_component = matrix_vector(gram, component, resource)
        expected_component = tuple(g_scale(value, eigenvalue) for value in component)
        if gram_component != expected_component:
            raise ArithmeticError("tensor-mode eigenvalue certificate failed")
        if not active:
            if norm != 0:
                raise ArithmeticError("normalization left an all-constant perturbation")
            continue
        mode_rows.append(
            ModePenalty(
                active_primes=active,
                multiplicity=mode_multiplicity(panel, active),
                eigenvalue=eigenvalue,
                euclidean_norm_squared=norm,
                dual_penalty=norm / eigenvalue,
                vector=component,
            )
        )
    if tuple(reconstruction) != beta:
        raise ArithmeticError("tensor projectors did not resolve the perturbation")
    for left_index, left in enumerate(mode_rows):
        for right in mode_rows[left_index + 1 :]:
            if euclidean_inner(left.vector, right.vector, resource) != gaussian():
                raise ArithmeticError("distinct tensor modes ceased to be orthogonal")
    mode_sum = sum((row.dual_penalty for row in mode_rows), Fraction(0))
    if mode_sum != excess:
        raise ArithmeticError("mode-resolved dual penalty failed")
    if (excess == 0) != all(value == gaussian() for value in beta):
        raise ArithmeticError("unique-extremizer certificate failed")
    return AmplifierAnalysis(
        primes=panel,
        dimension=dimension,
        direct_energy=direct,
        coherent_baseline=baseline,
        excess_energy=excess,
        mode_penalty_sum=mode_sum,
        modes=tuple(mode_rows),
        beta=beta,
    )


def is_rank_one_two_by_three(vector: Sequence[Gaussian]) -> bool:
    values = tuple(vector)
    if len(values) != 6:
        raise ValueError("rank-one control expects a 2-by-3 tensor")
    for left_column, right_column in combinations(range(3), 2):
        determinant = g_sub(
            g_mul(values[left_column], values[3 + right_column]),
            g_mul(values[right_column], values[3 + left_column]),
        )
        if determinant != gaussian():
            return False
    return True


def _serialize_analysis(analysis: AmplifierAnalysis) -> dict[str, object]:
    return {
        "primes": list(analysis.primes),
        "dimension": analysis.dimension,
        "direct_dual_energy": _fraction_pair(analysis.direct_energy),
        "coherent_baseline": _fraction_pair(analysis.coherent_baseline),
        "positive_excess": _fraction_pair(analysis.excess_energy),
        "mode_penalty_sum": _fraction_pair(analysis.mode_penalty_sum),
        "modes": [
            {
                "active_sum_zero_primes": list(row.active_primes),
                "multiplicity": row.multiplicity,
                "gram_eigenvalue": _fraction_pair(row.eigenvalue),
                "euclidean_norm_squared": _fraction_pair(row.euclidean_norm_squared),
                "dual_penalty": _fraction_pair(row.dual_penalty),
            }
            for row in analysis.modes
        ],
    }


def _mode_spectrum(primes: tuple[int, ...]) -> list[dict[str, object]]:
    rows = []
    multiplicity_sum = 0
    for active in _all_mode_subsets(primes):
        multiplicity = mode_multiplicity(primes, active)
        multiplicity_sum += multiplicity
        rows.append(
            {
                "active_sum_zero_primes": list(active),
                "multiplicity": multiplicity,
                "gram_eigenvalue": _fraction_pair(mode_eigenvalue(primes, active)),
            }
        )
    if multiplicity_sum != tensor_dimension(primes):
        raise ArithmeticError("tensor-mode multiplicities do not sum to dimension")
    return rows


def _correlated_deletion_counterexample(guard: ResourceGuard) -> dict[str, object]:
    """Certify that a non-product restricted-Gram mask is a different problem."""

    panel = (5, 7)
    retained_flat = (0, 2, 3, 4)
    retained_joint = ((0, 0), (0, 2), (1, 0), (1, 1))
    gram = tensor_gram(panel, guard)
    guard.matrix(len(retained_flat), len(retained_flat))
    guard.operation(len(retained_flat) ** 2)
    restricted = tuple(
        tuple(gram[row][column] for column in retained_flat) for row in retained_flat
    )
    row_sums = tuple(sum(row, Fraction(0)) for row in restricted)
    guard.operation(2 * len(retained_flat) ** 2)
    denominator = sum(row_sums, Fraction(0))
    native_amplitude = tensor_dimension(panel)
    optimal_weights = tuple(
        Fraction(native_amplitude) * row_sum / denominator for row_sum in row_sums
    )
    if sum(optimal_weights, Fraction(0)) != native_amplitude:
        raise ArithmeticError("restricted optimizer lost the native amplitude")

    # If H is the retained principal block, alpha=N H 1/(1^T H 1).
    # Hence H^(-1)alpha=N 1/(1^T H 1), which certifies both optimality
    # and the exact restricted dual energy without a numerical inversion.
    dual_representative = (gaussian(Fraction(native_amplitude, denominator)),) * len(
        retained_flat
    )
    if matrix_vector(restricted, dual_representative, guard) != tuple(
        gaussian(value) for value in optimal_weights
    ):
        raise ArithmeticError("restricted-Gram optimizer certificate failed")
    restricted_energy = euclidean_inner(
        tuple(gaussian(value) for value in optimal_weights),
        dual_representative,
        guard,
    )
    if restricted_energy[1] != 0:
        raise ArithmeticError("restricted dual energy ceased to be real")
    expected_energy = Fraction(native_amplitude**2, denominator)
    if restricted_energy[0] != expected_energy:
        raise ArithmeticError("restricted dual-energy certificate failed")
    full_value = coherent_baseline(panel)
    if expected_energy >= full_value:
        raise ArithmeticError("correlated-deletion strict improvement disappeared")

    zero_extended = tuple(
        gaussian(optimal_weights[retained_flat.index(index)])
        if index in retained_flat
        else gaussian()
        for index in range(native_amplitude)
    )
    complete_metric_energy = analyze_amplifier(
        panel, zero_extended, guard
    ).direct_energy
    if complete_metric_energy <= full_value:
        raise ArithmeticError("complete-metric no-go failed on deletion control")

    return {
        "primes": list(panel),
        "coordinate_order": (
            "zero-based lexicographic (p=5 coordinate, p=7 coordinate)"
        ),
        "retained_flat_indices": list(retained_flat),
        "retained_joint_coordinates": [list(pair) for pair in retained_joint],
        "restricted_gram": [
            [_fraction_pair(value) for value in row] for row in restricted
        ],
        "restricted_row_sums": [_fraction_pair(value) for value in row_sums],
        "native_amplitude": native_amplitude,
        "restricted_denominator_1H1": _fraction_pair(denominator),
        "restricted_optimal_weights": [
            _fraction_pair(value) for value in optimal_weights
        ],
        "restricted_optimal_dual_energy": _fraction_pair(expected_energy),
        "full_complete_frame_optimum": _fraction_pair(full_value),
        "same_zero_extended_weights_complete_metric_energy": _fraction_pair(
            complete_metric_energy
        ),
        "strict_restricted_improvement": True,
        "interpretation": (
            "Correlated deletion of joint tensor coordinates followed by inversion of "
            "the retained Gram is not covered by the local/product-mask no-go and can "
            "improve this formal restricted metric."
        ),
    }


def _build_symbolic_certificate(guard: ResourceGuard) -> dict[str, object]:
    """Close the exact operator theorem without reading any source artifact."""

    # The local inverse is verified directly on the finite controls.  Its
    # all-p algebra has I coefficient one and J numerator p-(p-m)-m=0.
    for panel in CONTROL_PANELS:
        gram = tensor_gram(panel, guard)
        inverse = tensor_inverse(panel, guard)
        product = matrix_multiply(gram, inverse, guard)
        identity = tuple(
            tuple(Fraction(row == column) for column in range(len(gram)))
            for row in range(len(gram))
        )
        if product != identity:
            raise ArithmeticError("exact Kronecker inverse control failed")

    uniform = (gaussian(1),) * 6
    real_entangled = tuple(gaussian(value) for value in (2, 0, 1, 0, 2, 1))
    complex_entangled = (
        gaussian(1, 1),
        gaussian(1, -1),
        gaussian(1),
        gaussian(1),
        gaussian(1),
        gaussian(1),
    )
    product_complex = tensor_vector(
        (
            (gaussian(1, 1), gaussian(1, -1)),
            (gaussian(1), gaussian(1), gaussian(1)),
        )
    )
    fractional_entangled = (
        gaussian(Fraction(3, 2), Fraction(1, 3)),
        gaussian(Fraction(1, 2), Fraction(-1, 3)),
        gaussian(1),
        gaussian(1),
        gaussian(1),
        gaussian(1),
    )
    controls = []
    for label, panel, vector, expected_rank_one in (
        ("uniform_unique_extremizer", (5, 7), uniform, True),
        ("real_nonproduct", (5, 7), real_entangled, False),
        ("complex_nonproduct", (5, 7), complex_entangled, False),
        ("complex_product", (5, 7), product_complex, True),
        ("fractional_complex_nonproduct", (5, 7), fractional_entangled, False),
        ("three_prime_complex_nonproduct", (3, 5, 7), complex_entangled, False),
    ):
        rank_one = is_rank_one_two_by_three(vector)
        if rank_one != expected_rank_one:
            raise ArithmeticError("product/non-product control classification failed")
        analysis = analyze_amplifier(panel, vector, guard)
        controls.append(
            {
                "label": label,
                "weights": [_gaussian_pairs(value) for value in vector],
                "rank_one_under_2_by_3_flattening": rank_one,
                "analysis": _serialize_analysis(analysis),
            }
        )

    correlated_deletion = _correlated_deletion_counterexample(guard)

    return {
        "theorem": {
            "domain": (
                "every nonempty finite set S of distinct odd marked primes, with "
                "m_p=(p-1)/2 and G_S=tensor_(p in S)(pI_(m_p)-J_(m_p))"
            ),
            "complex_amplitude_constraint": (
                "alpha^*1=N_S (equivalently sum_x alpha_x=N_S because N_S is real)"
            ),
            "local_inverse": ("(pI_m-J_m)^(-1)=p^(-1)I_m+2/[p(p+1)]J_m, m=(p-1)/2"),
            "local_inverse_symbolic_check": (
                "the I coefficient is 1 and the residual J numerator is p-(p-m)-m=0"
            ),
            "tensor_inverse": "G_S^(-1)=tensor_(p in S)G_p^(-1)",
            "constant_eigenvalue": "lambda_S=product_(p in S)(p+1)/2",
            "coherent_baseline": (
                "1^*G_S^(-1)1=N_S/lambda_S=product_(p in S)(p-1)/(p+1)"
            ),
            "exact_pythagorean_identity": (
                "alpha^*G_S^(-1)alpha=L(S)+beta^*G_S^(-1)beta, "
                "beta=alpha-1 and beta^*1=0"
            ),
            "unique_complex_extremizer": (
                "positive definiteness gives equality only at alpha=1; arbitrary "
                "complex phases and non-separable cross-prime weights cannot improve L(S)"
            ),
            "mode_eigenvalue": (
                "lambda_A=product_(p in A)p * product_(p in S\\A)(p+1)/2"
            ),
            "mode_multiplicity": "product_(p in A)(m_p-1)",
            "mode_penalty": (
                "beta^*G_S^(-1)beta=sum_(nonempty A) ||beta_A||_2^2/lambda_A"
            ),
        },
        "mode_spectra": [
            {
                "primes": list(panel),
                "dimension": tensor_dimension(panel),
                "coherent_baseline": _fraction_pair(coherent_baseline(panel)),
                "rows": _mode_spectrum(panel),
            }
            for panel in CONTROL_PANELS
        ],
        "exact_gaussian_rational_controls": controls,
        "correlated_joint_deletion_counterexample": correlated_deletion,
    }


def _read_locked_sources(
    guard: ResourceGuard,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    loaded: dict[str, object] = {}
    manifest = []
    for name, lock in SOURCE_LOCKS.items():
        path = lock.get("path")
        if not isinstance(path, Path) or not path.is_file():
            raise RuntimeError(f"missing source lock: {name}")
        byte_count = path.stat().st_size
        guard.source(byte_count)
        raw = path.read_bytes()
        if len(raw) != byte_count:
            raise RuntimeError(f"source changed while reading: {name}")
        normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest = hashlib.sha256(normalized).hexdigest()
        if digest != lock.get("sha256_lf"):
            raise RuntimeError(f"LF-normalized source lock failed: {name}")
        kind = lock.get("kind")
        if kind == "json":
            value = json.loads(normalized.decode("utf-8"))
            if not isinstance(value, dict):
                raise TypeError(f"source JSON is not an object: {name}")
            if value.get("schema") != lock.get("schema"):
                raise RuntimeError(f"source schema lock failed: {name}")
            loaded[name] = value
        elif kind == "text":
            loaded[name] = None
        else:
            raise RuntimeError(f"unknown source lock kind: {name}")
        manifest.append(
            {
                "id": name,
                "path": _relative(path),
                "kind": kind,
                "role": lock["role"],
                "git_blob": lock["git_blob"],
                "sha256_lf_normalized": digest,
                "bytes": byte_count,
            }
        )
    return loaded, manifest


def _validate_source_semantics(sources: Mapping[str, object]) -> None:
    principal = sources.get("principal_json")
    conditioned = sources.get("conditioned_mask_json")
    frontier = sources.get("tensor_frontier_json")
    if not all(isinstance(value, dict) for value in (principal, conditioned, frontier)):
        raise TypeError("source JSON bundle is incomplete")
    if (
        not isinstance(principal, dict)
        or not isinstance(conditioned, dict)
        or not isinstance(frontier, dict)
    ):
        raise TypeError("source JSON bundle types drifted")

    source = principal.get("source_frontier")
    theorem = principal.get("principal_leverage_theorem")
    if not isinstance(source, dict) or not isinstance(theorem, dict):
        raise TypeError("principal leverage source blocks are missing")
    if (
        source.get("pr") != PR_751
        or source.get("commit") != DEPENDENCY_SNAPSHOT_COMMIT_751
        or source.get("git_blob_ids") != DEPENDENCY_SOURCE_BLOBS_751
        or source.get("live_target") != "T-106121 / FFPS106121"
    ):
        raise RuntimeError("corrected PR #751 provenance changed")
    if (
        theorem.get("local_formula") != "||O_p||^2=(p-1)/(p+1)"
        or theorem.get("tensor_formula")
        != "for distinct marked phases, squared leverage is product_i (p_i-1)/(p_i+1)"
    ):
        raise RuntimeError("principal phase-Gram semantics changed")

    conditioned_source = conditioned.get("source_frontier")
    conditioned_theorem = conditioned.get("theorem")
    if not isinstance(conditioned_source, dict) or not isinstance(
        conditioned_theorem, dict
    ):
        raise TypeError("conditioned-mask source blocks are missing")
    if (
        conditioned_source.get("commit") != DEPENDENCY_SNAPSHOT_COMMIT_751
        or conditioned_source.get("dependency_sha256_lf")
        != SOURCE_LOCKS["principal_json"]["sha256_lf"]
        or conditioned_theorem.get("restricted_inverse")
        != "(pI_a-J_a)^(-1)=p^(-1)I+[p(p-a)]^(-1)J"
    ):
        raise RuntimeError("conditioned-mask prerequisite changed")

    frontier_source = frontier.get("source_frontier")
    budget = frontier.get("exact_budget_theorem")
    if not isinstance(frontier_source, dict) or not isinstance(budget, dict):
        raise TypeError("tensor-frontier source blocks are missing")
    if (
        frontier_source.get("commit") != DEPENDENCY_SNAPSHOT_COMMIT_751
        or frontier_source.get("dependency_sha256_lf")
        != SOURCE_LOCKS["principal_json"]["sha256_lf"]
        or budget.get("model")
        != (
            "M is the squarefree product of distinct marked odd-prime phase coordinates; "
            "L(M)=product_(p|M)(p-1)/(p+1) is squared principal leverage"
        )
    ):
        raise RuntimeError("coherent tensor-frontier prerequisite changed")


def _packet_manifest() -> list[dict[str, str]]:
    result = []
    for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH):
        if not path.is_file():
            raise RuntimeError(f"missing packet artifact: {path}")
        result.append(
            {"path": _relative(path), "sha256_lf_normalized": _lf_sha256(path)}
        )
    return result


def _check_wall(start: float, now: float | None = None) -> None:
    finish = time.monotonic() if now is None else now
    if finish < start:
        raise RuntimeError("monotonic clock moved backwards")
    if finish - start > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")


def build_fixture() -> dict[str, object]:
    start = time.monotonic()
    guard = ResourceGuard()

    # This is deliberately first: no dependency file is opened until the
    # self-contained Kronecker theorem and all exact controls have closed.
    symbolic = _build_symbolic_certificate(guard)
    operations_after_symbolic = guard.exact_operations
    matrix_cells_after_symbolic = guard.matrix_cells
    _check_wall(start)

    sources, source_manifest = _read_locked_sources(guard)
    _validate_source_semantics(sources)
    _check_wall(start)

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_tensor_signed_amplifier_no_go.v1",
        "status": "EXACT_ALL_FINITE_MARKED_PRIME_COMPLETE_FRAME_NO_GO",
        "source_frontier": {
            "pr": PR_751,
            "dependency_snapshot": {
                "commit": DEPENDENCY_SNAPSHOT_COMMIT_751,
                "target_at_snapshot": "T-106121 / FFPS106121",
                "git_blob_ids": DEPENDENCY_SOURCE_BLOBS_751,
                "principal_dependency": PRINCIPAL_JSON_PATH.name,
                "principal_dependency_sha256_lf": SOURCE_LOCKS["principal_json"][
                    "sha256_lf"
                ],
            },
            "live_audit": {
                "head_commit": LIVE_AUDITED_HEAD_751,
                "git_blob_ids": LIVE_SOURCE_BLOBS_751,
                "local_gram_contract": (
                    "L-106024 has the same d94787... blob at the dependency snapshot "
                    "and live audited head, so G_p=pI-J is unchanged."
                ),
                "gate_status": LIVE_GATE_STATUS_751,
            },
        },
        **symbolic,
        "metric_distinction": {
            "complete_frame": (
                "This theorem permits zero coefficients but retains the complete G_S^(-1) metric."
            ),
            "physical_deletion": (
                "Deleting phase coordinates and re-inverting the retained principal block of "
                "G_S is a different operation. Local masks and product-coordinate tensor masks "
                "are covered by the conditioned-mask packet."
            ),
            "noncommutation": (
                "A principal block of G_S^(-1) need not equal the inverse of the corresponding "
                "principal block of G_S."
            ),
            "correlated_joint_deletion": (
                "Arbitrary correlated subsets of joint tensor coordinates are not covered by "
                "the local/product-mask theorem; the exact (5,7) counterexample in this packet "
                "strictly improves the restricted-Gram metric."
            ),
        },
        "source_manifest": source_manifest,
        "packet_manifest": _packet_manifest(),
        "resource_contract": {
            "arithmetic": "exact integers, rationals, and Gaussian rationals only",
            "control_panels": [list(panel) for panel in CONTROL_PANELS],
            "maximum_control_prime": MAX_CONTROL_PRIME,
            "maximum_tensor_dimension": MAX_TENSOR_DIMENSION,
            "maximum_matrix_cells": MAX_MATRIX_CELLS,
            "actual_matrix_cells": guard.matrix_cells,
            "matrix_cells_after_symbolic_theorem": matrix_cells_after_symbolic,
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operations_after_symbolic_theorem": operations_after_symbolic,
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "actual_source_bytes": guard.source_bytes,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "finite_fields_enumerated": 0,
        },
        "scope": {
            "formal_operator_theorem": "every nonempty finite set of distinct odd marked primes",
            "finite_controls_are_theorem_inputs": False,
            "arbitrary_complex_complete_frame_weights": True,
            "arbitrary_correlated_restricted_gram_deletion_ruled_out": False,
            "arbitrary_arithmetic_conditioning_proved": False,
            "varying_conductor_moment_proved": False,
            "principal_member_individualized": False,
            "rh_or_grh_proved": False,
            "external_novelty_claimed": False,
        },
        "firewalls": [
            "The operator theorem closes before any frozen dependency is read; dependencies certify interpretation and provenance only.",
            "Zero-coordinate weighting in the complete inverse metric is not identified with physical deletion and restricted-Gram inversion.",
            "The conditioned-mask dependency rules out local and product-coordinate masks, not arbitrary correlated subsets of joint tensor coordinates.",
            "No arithmetic varying-conductor family, character group, L-function, or zero set is enumerated.",
            "The result does not prove the open BTPS106121, WCADD106140, or WCKUM106140 gates, RH, or GRH; BTMS106121 and BTDS106121 are withdrawn historical gates.",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    _check_wall(start)
    return fixture


def _serialized(fixture: Mapping[str, object]) -> str:
    return json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _serialized(fixture)
    if arguments.check:
        if not arguments.output.is_file():
            raise SystemExit(f"missing fixture: {arguments.output}")
        if arguments.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"stale fixture: {arguments.output}")
        print(f"verified {arguments.output}")
        return 0
    arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
