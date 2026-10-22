#!/usr/bin/env python3
"""Exact residual/gap checker for L-14301 and X-14301.

The checker uses only Python integers and ``fractions.Fraction``.  It verifies
an exact rational enclosure of a real symmetric matrix, a parity involution, a
candidate even vector, exact spanning bases for the even complement and odd
sector, and strict midpoint gap certificates.  Entrywise radii are converted
to a rigorous operator-radius bound by the maximum absolute row sum.

The result applies to every *symmetric, parity-commuting* exact matrix inside
the supplied boxes.  Establishing that a production matrix is the intended
Connes--Consani--Moscovici truncated Weil matrix, and that it commutes with the
stated parity exactly, is a separate provenance/analytic-formula gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "riemann.prolate-ground-certificate.v1"
RESULT_SCHEMA = "riemann.prolate-ground-certificate-result.v1"


class CertificateError(ValueError):
    """Raised when a certificate is malformed or fails a proof gate."""


def parse_fraction(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not a rational string") from exc
    if isinstance(value, dict):
        try:
            numerator = value["numerator"]
            denominator = value["denominator"]
        except KeyError as exc:
            raise CertificateError(
                f"{name} needs numerator and denominator"
            ) from exc
        if (
            isinstance(numerator, bool)
            or isinstance(denominator, bool)
            or not isinstance(numerator, int)
            or not isinstance(denominator, int)
        ):
            raise CertificateError(
                f"{name} numerator and denominator must be integers"
            )
        try:
            return Fraction(numerator, denominator)
        except ZeroDivisionError as exc:
            raise CertificateError(f"{name} is malformed") from exc
    raise CertificateError(
        f"{name} must be an integer, rational string, or fraction object"
    )


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def parse_vector(value: Any, name: str, n: int) -> Vector:
    if not isinstance(value, list) or len(value) != n:
        raise CertificateError(f"{name} must be an array of length {n}")
    return [parse_fraction(x, f"{name}[{i}]") for i, x in enumerate(value)]


def parse_matrix(value: Any, name: str, *, n: int | None = None) -> Matrix:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty square array")
    dimension = len(value) if n is None else n
    if len(value) != dimension:
        raise CertificateError(f"{name} must have {dimension} rows")
    out: Matrix = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != dimension:
            raise CertificateError(f"{name}[{i}] must have length {dimension}")
        out.append(
            [parse_fraction(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)]
        )
    return out


def parse_basis(value: Any, name: str, n: int) -> list[Vector]:
    if not isinstance(value, list):
        raise CertificateError(f"{name} must be an array")
    return [parse_vector(row, f"{name}[{i}]", n) for i, row in enumerate(value)]


def dot(x: Vector, y: Vector) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def matvec(a: Matrix, x: Vector) -> Vector:
    if len(a) != len(x):
        raise CertificateError("matrix-vector dimension mismatch")
    return [dot(row, x) for row in a]


def vec_sub(x: Vector, y: Vector) -> Vector:
    return [a - b for a, b in zip(x, y)]


def vec_scale(c: Fraction, x: Vector) -> Vector:
    return [c * a for a in x]


def is_symmetric(a: Matrix) -> bool:
    n = len(a)
    return all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def matrix_rank(rows: Iterable[Vector], ncols: int) -> int:
    matrix = [row[:] for row in rows]
    if not matrix:
        return 0
    if any(len(row) != ncols for row in matrix):
        raise CertificateError("rank input has inconsistent row length")
    rank = 0
    for col in range(ncols):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][col]
        matrix[rank] = [entry / pivot_value for entry in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank:
                continue
            factor = matrix[row][col]
            if factor != 0:
                matrix[row] = [
                    matrix[row][j] - factor * matrix[rank][j]
                    for j in range(ncols)
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def positive_definite_ldl(a: Matrix) -> tuple[bool, list[Fraction]]:
    """Exact unpivoted LDL test; valid because positive definite matrices have
    positive pivots in every leading principal factorization.
    """
    if not a:
        return True, []
    if not is_symmetric(a):
        return False, []
    n = len(a)
    l = [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
    d: list[Fraction] = []
    for j in range(n):
        pivot = a[j][j] - sum(
            (l[j][k] * l[j][k] * d[k] for k in range(j)), Fraction(0)
        )
        if pivot <= 0:
            return False, d + [pivot]
        d.append(pivot)
        for i in range(j + 1, n):
            numerator = a[i][j] - sum(
                (l[i][k] * l[j][k] * d[k] for k in range(j)), Fraction(0)
            )
            l[i][j] = numerator / pivot
    return True, d


def apply_parity(permutation: list[int], x: Vector) -> Vector:
    return [x[permutation[i]] for i in range(len(x))]


def parity_dimensions(permutation: list[int]) -> tuple[int, int]:
    fixed = sum(1 for i, p in enumerate(permutation) if i == p)
    pairs = sum(1 for i, p in enumerate(permutation) if i < p)
    return fixed + pairs, pairs


def projected_shift_matrix(
    a: Matrix, basis: list[Vector], shift: Fraction
) -> Matrix:
    return [
        [dot(left, matvec(a, right)) - shift * dot(left, right) for right in basis]
        for left in basis
    ]


def fraction_decimal_truncated_toward_zero(
    value: Fraction, digits: int = 18
) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer = value.numerator // value.denominator
    remainder = value.numerator % value.denominator
    if digits <= 0:
        return f"{sign}{integer}"
    scale = 10**digits
    fractional = (remainder * scale) // value.denominator
    return f"{sign}{integer}.{fractional:0{digits}d}"


def validate_permutation(value: Any, n: int) -> list[int]:
    if not isinstance(value, list) or len(value) != n:
        raise CertificateError(f"parity_permutation must have length {n}")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in value):
        raise CertificateError("parity_permutation entries must be integers")
    permutation = list(value)
    if sorted(permutation) != list(range(n)):
        raise CertificateError("parity_permutation must be a permutation")
    if any(permutation[permutation[i]] != i for i in range(n)):
        raise CertificateError("parity_permutation must be an involution")
    return permutation


def verify_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    if certificate.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    interval = certificate.get("matrix_interval")
    if not isinstance(interval, dict):
        raise CertificateError("matrix_interval must be an object")
    lower = parse_matrix(interval.get("lower"), "matrix_interval.lower")
    n = len(lower)
    if n < 2:
        raise CertificateError("matrix dimension must be at least 2")
    upper = parse_matrix(interval.get("upper"), "matrix_interval.upper", n=n)

    if not is_symmetric(lower) or not is_symmetric(upper):
        raise CertificateError("matrix interval endpoints must be symmetric")
    for i in range(n):
        for j in range(n):
            if lower[i][j] > upper[i][j]:
                raise CertificateError(f"empty interval at matrix entry ({i},{j})")

    midpoint = [
        [(lower[i][j] + upper[i][j]) / 2 for j in range(n)] for i in range(n)
    ]
    radii = [
        [(upper[i][j] - lower[i][j]) / 2 for j in range(n)] for i in range(n)
    ]
    operator_radius = max(sum(row, Fraction(0)) for row in radii)

    permutation = validate_permutation(certificate.get("parity_permutation"), n)
    for i in range(n):
        for j in range(n):
            pi, pj = permutation[i], permutation[j]
            if midpoint[i][j] != midpoint[pi][pj]:
                raise CertificateError("matrix midpoint does not commute with parity")
            if radii[i][j] != radii[pi][pj]:
                raise CertificateError("matrix radii are not parity invariant")

    candidate = parse_vector(certificate.get("candidate"), "candidate", n)
    norm2 = dot(candidate, candidate)
    if norm2 <= 0:
        raise CertificateError("candidate must be nonzero")
    if apply_parity(permutation, candidate) != candidate:
        raise CertificateError("candidate is not even")

    even_basis = parse_basis(
        certificate.get("even_complement_basis"), "even_complement_basis", n
    )
    odd_basis = parse_basis(certificate.get("odd_basis"), "odd_basis", n)
    even_dimension, odd_dimension = parity_dimensions(permutation)

    if len(even_basis) != even_dimension - 1:
        raise CertificateError(
            "even_complement_basis has the wrong number of vectors"
        )
    if len(odd_basis) != odd_dimension:
        raise CertificateError("odd_basis has the wrong number of vectors")

    for i, vector in enumerate(even_basis):
        if apply_parity(permutation, vector) != vector:
            raise CertificateError(f"even_complement_basis[{i}] is not even")
        if dot(candidate, vector) != 0:
            raise CertificateError(
                f"even_complement_basis[{i}] is not orthogonal to candidate"
            )
    for i, vector in enumerate(odd_basis):
        if apply_parity(permutation, vector) != vec_scale(Fraction(-1), vector):
            raise CertificateError(f"odd_basis[{i}] is not odd")

    if matrix_rank([candidate, *even_basis], n) != even_dimension:
        raise CertificateError("candidate and even complement do not span H_even")
    if matrix_rank(odd_basis, n) != odd_dimension:
        raise CertificateError("odd_basis does not span H_odd")

    midpoint_times_candidate = matvec(midpoint, candidate)
    mu0 = dot(candidate, midpoint_times_candidate) / norm2
    residual = vec_sub(midpoint_times_candidate, vec_scale(mu0, candidate))
    if dot(candidate, residual) != 0:
        raise CertificateError("internal error: Rayleigh residual is not orthogonal")
    residual_norm2 = dot(residual, residual) / norm2
    rho0_upper = parse_fraction(
        certificate.get("midpoint_residual_norm_upper"),
        "midpoint_residual_norm_upper",
    )
    if rho0_upper < 0 or rho0_upper * rho0_upper < residual_norm2:
        raise CertificateError("midpoint residual bound is too small")

    gap_even_midpoint = parse_fraction(
        certificate.get("midpoint_gap_even"), "midpoint_gap_even"
    )
    gap_odd_midpoint = parse_fraction(
        certificate.get("midpoint_gap_odd"), "midpoint_gap_odd"
    )
    if gap_even_midpoint <= 0 or gap_odd_midpoint <= 0:
        raise CertificateError("declared midpoint gaps must be positive")

    even_gap_matrix = projected_shift_matrix(
        midpoint, even_basis, mu0 + gap_even_midpoint
    )
    odd_gap_matrix = projected_shift_matrix(
        midpoint, odd_basis, mu0 + gap_odd_midpoint
    )
    even_pd, even_pivots = positive_definite_ldl(even_gap_matrix)
    odd_pd, odd_pivots = positive_definite_ldl(odd_gap_matrix)
    if not even_pd:
        raise CertificateError("even-complement midpoint gap is not strict")
    if not odd_pd:
        raise CertificateError("odd-sector midpoint gap is not strict")

    gap_even = gap_even_midpoint - 2 * operator_radius
    gap_odd = gap_odd_midpoint - 2 * operator_radius
    if gap_even <= 0 or gap_odd <= 0:
        raise CertificateError(
            "operator-radius uncertainty consumes a declared parity-sector gap"
        )

    residual_upper = rho0_upper + 2 * operator_radius
    eigenvalue_lower = mu0 - operator_radius - residual_upper**2 / gap_even
    eigenvalue_upper = mu0 + operator_radius
    global_spectral_gap_lower = min(gap_even, gap_odd)
    tangent_upper = residual_upper / gap_even
    aligned_distance_squared_upper = 2 * tangent_upper * tangent_upper

    weighted_result: dict[str, Any] | None = None
    weighted = certificate.get("weighted_projective")
    if weighted is not None:
        if not isinstance(weighted, dict):
            raise CertificateError("weighted_projective must be an object")
        gram = parse_matrix(weighted.get("gram"), "weighted_projective.gram", n=n)
        if not is_symmetric(gram):
            raise CertificateError("weighted_projective.gram must be symmetric")
        for i in range(n):
            for j in range(n):
                if gram[i][j] != gram[permutation[i]][permutation[j]]:
                    raise CertificateError(
                        "weighted_projective.gram does not commute with parity"
                    )
        gram_pd, gram_pivots = positive_definite_ldl(gram)
        if not gram_pd:
            raise CertificateError("weighted_projective.gram is not positive definite")

        candidate_norm_upper = parse_fraction(
            weighted.get("candidate_norm_upper"),
            "weighted_projective.candidate_norm_upper",
        )
        if candidate_norm_upper <= 0 or candidate_norm_upper**2 < norm2:
            raise CertificateError(
                "weighted_projective candidate_norm_upper is too small"
            )
        complement_factor_upper = parse_fraction(
            weighted.get("even_complement_factor_upper"),
            "weighted_projective.even_complement_factor_upper",
        )
        if complement_factor_upper <= 0:
            raise CertificateError(
                "weighted_projective even_complement_factor_upper must be positive"
            )
        target_tail_upper = parse_fraction(
            weighted.get("target_tail_upper"),
            "weighted_projective.target_tail_upper",
        )
        if target_tail_upper < 0:
            raise CertificateError(
                "weighted_projective target_tail_upper must be nonnegative"
            )

        weighted_complement_matrix = [
            [
                complement_factor_upper**2 * dot(left, right)
                - dot(left, matvec(gram, right))
                for right in even_basis
            ]
            for left in even_basis
        ]
        weighted_factor_pd, weighted_factor_pivots = positive_definite_ldl(
            weighted_complement_matrix
        )
        if not weighted_factor_pd:
            raise CertificateError(
                "weighted_projective complement factor is not a strict upper bound"
            )

        weighted_line_distance_upper = (
            target_tail_upper
            + candidate_norm_upper
            * complement_factor_upper
            * tangent_upper
        )
        weighted_result = {
            "candidate_norm_upper": str(candidate_norm_upper),
            "even_complement_factor_upper": str(complement_factor_upper),
            "target_tail_upper": str(target_tail_upper),
            "target_line_distance_upper": str(weighted_line_distance_upper),
            "gram_ldl_pivots": [str(x) for x in gram_pivots],
            "complement_factor_ldl_pivots": [
                str(x) for x in weighted_factor_pivots
            ],
        }

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "status": "PASS",
        "claim_ids": ["L-14301", "X-14301"],
        "dimension": n,
        "parity_dimensions": {"even": even_dimension, "odd": odd_dimension},
        "candidate_norm_squared": str(norm2),
        "midpoint_rayleigh_value": str(mu0),
        "midpoint_residual_norm_squared": str(residual_norm2),
        "midpoint_residual_norm_upper": str(rho0_upper),
        "matrix_operator_radius_upper": str(operator_radius),
        "effective_residual_norm_upper": str(residual_upper),
        "effective_gap_even": str(gap_even),
        "effective_gap_odd": str(gap_odd),
        "global_spectral_gap_lower": str(global_spectral_gap_lower),
        "ground_eigenvalue_interval": {
            "lower": str(eigenvalue_lower),
            "upper": str(eigenvalue_upper),
        },
        "tan_ground_angle_upper": str(tangent_upper),
        "aligned_ground_distance_squared_upper": str(
            aligned_distance_squared_upper
        ),
        "ldl_pivots": {
            "even_complement": [str(x) for x in even_pivots],
            "odd_sector": [str(x) for x in odd_pivots],
        },
        "display_decimals_truncated_toward_zero": {
            "operator_radius_upper": fraction_decimal_truncated_toward_zero(
                operator_radius
            ),
            "effective_residual_norm_upper": fraction_decimal_truncated_toward_zero(
                residual_upper
            ),
            "effective_gap_even": fraction_decimal_truncated_toward_zero(gap_even),
            "effective_gap_odd": fraction_decimal_truncated_toward_zero(gap_odd),
            "ground_eigenvalue_lower": fraction_decimal_truncated_toward_zero(
                eigenvalue_lower
            ),
            "ground_eigenvalue_upper": fraction_decimal_truncated_toward_zero(
                eigenvalue_upper
            ),
            "tan_ground_angle_upper": fraction_decimal_truncated_toward_zero(
                tangent_upper
            ),
            "aligned_ground_distance_squared_upper": (
                fraction_decimal_truncated_toward_zero(
                    aligned_distance_squared_upper
                )
            ),
        },
        "decimal_display_notice": (
            "Decimal strings are truncated toward zero for human display only; "
            "all rigorous values are the exact fractions above."
        ),
        "logical_scope": (
            "Every symmetric parity-commuting exact matrix inside the supplied "
            "entry boxes has a unique global ground state in the even sector, "
            "with the reported eigenvalue and angle bounds. Any weighted "
            "projective result additionally assumes the supplied exact Gram and "
            "target-tail data. Matrix identity, exact parity, Gram identity, and "
            "target provenance are external gates."
        ),
    }
    if weighted_result is not None:
        result["weighted_projective"] = weighted_result
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read JSON certificate {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise CertificateError("certificate root must be an object")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    try:
        raw = args.certificate.read_bytes()
        certificate = load_json(args.certificate)
        result = verify_certificate(certificate)
        result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
    except (OSError, CertificateError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
