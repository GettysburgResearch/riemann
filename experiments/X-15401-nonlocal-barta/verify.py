#!/usr/bin/env python3
"""Exact checker for finite signed-jump Barta and rank-one polar certificates."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x15401-nonlocal-barta.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def vj(x: Sequence[Fraction]) -> list[dict[str, str]]:
    return [fj(y) for y in x]


def zero_matrix(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def add_outer(A: list[list[Fraction]], v: Sequence[Fraction], scale: Fraction) -> None:
    for i in range(len(v)):
        for j in range(len(v)):
            A[i][j] += scale * v[i] * v[j]


def mat_vec(A: Sequence[Sequence[Fraction]], x: Sequence[Fraction]) -> list[Fraction]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in A]


def dot(x: Sequence[Fraction], y: Sequence[Fraction]) -> Fraction:
    return sum(a * b for a, b in zip(x, y))


def quadratic(A: Sequence[Sequence[Fraction]], x: Sequence[Fraction]) -> Fraction:
    return dot(x, mat_vec(A, x))


def exact_ldl_positive(
    A: Sequence[Sequence[Fraction]], *, semidefinite: bool = False
) -> list[Fraction]:
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise CertificateError("matrix must be nonempty and square")
    L = zero_matrix(n)
    pivots: list[Fraction] = []
    for i in range(n):
        L[i][i] = Fraction(1)
        p = A[i][i] - sum(L[i][k] * L[i][k] * pivots[k] for k in range(i))
        if p < 0 or (p == 0 and not semidefinite):
            raise CertificateError("matrix does not have the required positive pivots")
        if p == 0:
            for row in range(i + 1, n):
                residual = A[row][i] - sum(
                    L[row][k] * L[i][k] * pivots[k] for k in range(i)
                )
                if residual != 0:
                    raise CertificateError("singular LDL pivot has nonzero residual")
                L[row][i] = Fraction(0)
        else:
            for row in range(i + 1, n):
                L[row][i] = (
                    A[row][i]
                    - sum(L[row][k] * L[i][k] * pivots[k] for k in range(i))
                ) / p
        pivots.append(p)
    return pivots


def invert(A: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    n = len(A)
    aug = [
        [Fraction(A[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot_row = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot_row is None:
            raise CertificateError("matrix is singular")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            m = aug[row][col]
            if m:
                aug[row] = [aug[row][j] - m * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def parse_vector(raw: Any, n: int, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or len(raw) != n:
        raise CertificateError(f"{name} must be an array of length {n}")
    return [frac(v, f"{name}[{i}]") for i, v in enumerate(raw)]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    n = integer(data.get("vertex_count"), "vertex_count")
    if n < 2:
        raise CertificateError("vertex_count must be at least two")

    potential = parse_vector(data.get("potential"), n, "potential")
    psi = parse_vector(data.get("psi"), n, "psi")
    if any(x <= 0 for x in psi):
        raise CertificateError("psi must be strictly positive")

    # The dense matrix uses the declared edge sign. The local signed-edge
    # ground-state residual is sign-independent; the sign remains only in the
    # nonnegative transformed edge square.
    H = zero_matrix(n)
    for i in range(n):
        H[i][i] += potential[i]
    barta_values = list(potential)

    raw_edges = data.get("jump_edges")
    if not isinstance(raw_edges, list):
        raise CertificateError("jump_edges must be an array")
    seen: set[tuple[int, int]] = set()
    edges: list[tuple[int, int, Fraction, int]] = []
    for k, raw in enumerate(raw_edges):
        if not isinstance(raw, dict):
            raise CertificateError(f"jump_edges[{k}] must be an object")
        i = integer(raw.get("i"), f"jump_edges[{k}].i")
        j = integer(raw.get("j"), f"jump_edges[{k}].j")
        if not (0 <= i < j < n) or (i, j) in seen:
            raise CertificateError("jump edges must be unique with 0 <= i < j < n")
        seen.add((i, j))
        weight = frac(raw.get("weight"), f"jump_edges[{k}].weight")
        if weight <= 0:
            raise CertificateError("jump weights must be positive")
        sign = integer(raw.get("sign"), f"jump_edges[{k}].sign")
        if sign not in (-1, 1):
            raise CertificateError("jump edge sign must be +1 or -1")
        edges.append((i, j, weight, sign))

        H[i][i] += weight
        H[j][j] += weight
        H[i][j] -= sign * weight
        H[j][i] -= sign * weight

        barta_values[i] += weight * (psi[i] - psi[j]) / psi[i]
        barta_values[j] += weight * (psi[j] - psi[i]) / psi[j]

    barta_floor = min(barta_values)
    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    if frac(claimed.get("barta_floor"), "claimed.barta_floor") != barta_floor:
        raise CertificateError("claimed Barta floor mismatch")

    # Exact signed-edge ground-state identity on a nontrivial control vector.
    test_vector = parse_vector(data.get("identity_vector"), n, "identity_vector")
    ratio = [test_vector[i] / psi[i] for i in range(n)]
    rhs = sum(barta_values[i] * test_vector[i] * test_vector[i] for i in range(n))
    rhs += sum(
        weight * psi[i] * psi[j] * (ratio[i] - sign * ratio[j]) ** 2
        for i, j, weight, sign in edges
    )
    lhs = quadratic(H, test_vector)
    if lhs != rhs:
        raise CertificateError("signed-edge ground-state identity failed")

    # Polar channel: a(u+u-* + u-u+*) = 2a(cc* - ss*).
    u_plus = parse_vector(data.get("u_plus"), n, "u_plus")
    u_minus = parse_vector(data.get("u_minus"), n, "u_minus")
    a = frac(data.get("polar_a"), "polar_a")
    if a <= 0:
        raise CertificateError("polar_a must be positive")
    c = [(u_plus[i] + u_minus[i]) / 2 for i in range(n)]
    s = [(u_plus[i] - u_minus[i]) / 2 for i in range(n)]
    polar_direct = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            polar_direct[i][j] = a * (
                u_plus[i] * u_minus[j] + u_minus[i] * u_plus[j]
            )
    polar_signature = zero_matrix(n)
    add_outer(polar_signature, c, 2 * a)
    add_outer(polar_signature, s, -2 * a)
    if polar_direct != polar_signature:
        raise CertificateError("polar signature identity failed")

    target = frac(claimed.get("target_floor"), "claimed.target_floor")
    if not target < barta_floor:
        raise CertificateError("target_floor must be below the Barta floor")
    shifted_base = [
        [H[i][j] - (target if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    base_pivots = exact_ldl_positive(shifted_base)
    x = mat_vec(invert(shifted_base), s)
    resolvent = dot(s, x)
    if frac(claimed.get("odd_resolvent"), "claimed.odd_resolvent") != resolvent:
        raise CertificateError("claimed odd resolvent mismatch")
    tau = 2 * a
    if not tau * resolvent < 1:
        raise CertificateError("rank-one Birman-Schwinger gate does not pass strictly")

    # Direct dense regression: the positive polar channel may only help.
    full = [[H[i][j] + polar_signature[i][j] for j in range(n)] for i in range(n)]
    shifted_full = [
        [full[i][j] - (target if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    full_pivots = exact_ldl_positive(shifted_full)

    return {
        "schema": SCHEMA,
        "status": "EXACT_SYNTHETIC_NONLOCAL_BARTA_POLAR_FLOOR",
        "edge_signs": [sign for _, _, _, sign in edges],
        "barta_values": vj(barta_values),
        "barta_floor": fj(barta_floor),
        "identity_value": fj(lhs),
        "polar_cosh": vj(c),
        "polar_sinh": vj(s),
        "target_floor": fj(target),
        "odd_resolvent": fj(resolvent),
        "birman_schwinger_product": fj(tau * resolvent),
        "base_shifted_ldl_pivots": vj(base_pivots),
        "full_shifted_ldl_pivots": vj(full_pivots),
        "proof_boundary": "finite rational signed graph regression only; no Riemann-zeta value",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
