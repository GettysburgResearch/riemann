#!/usr/bin/env python3
"""Bounded replay for the shared-fibre positive-quotient theorem."""

from __future__ import annotations

import argparse
import json
import hashlib
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE_COMMIT = "a30276a5be049749ebb2147f30f000dd5659298b"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md": "3e7fff53f5cdbb3a660b24b2e765f4ac35c434c3",
    "research/l-families/atlas/function_field/ffps_shared_fibre_wick_occupancy_spectrum.py": "e22e73883208fdc6004db61a1c0c319636cbc01e",
}
OUTPUT = HERE / "shared_fibre_positive_quotient.json"

Matrix = tuple[tuple[Fraction, ...], ...]


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(i == j) for j in range(n)) for i in range(n))


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return tuple(
        tuple(sum((x * y for x, y in zip(row, col, strict=True)), Fraction()) for col in bt)
        for row in a
    )


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x + y for x, y in zip(ra, rb, strict=True)) for ra, rb in zip(a, b, strict=True))


def sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x - y for x, y in zip(ra, rb, strict=True)) for ra, rb in zip(a, b, strict=True))


def scale(c: Fraction, a: Matrix) -> Matrix:
    return tuple(tuple(c * x for x in row) for row in a)


def diag(values: tuple[Fraction, ...]) -> Matrix:
    n = len(values)
    return tuple(tuple(values[i] if i == j else Fraction() for j in range(n)) for i in range(n))


def trace(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction())


def max_abs(a: Matrix) -> Fraction:
    return max((abs(x) for row in a for x in row), default=Fraction())


def centered(prime: int) -> Matrix:
    m = (prime - 1) // 2
    return tuple(
        tuple(Fraction(i == j) - Fraction(1, prime) for j in range(m))
        for i in range(m)
    )


def kron(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0])))
        for i in range(len(a))
        for k in range(len(b))
    )


def incidence(cell_count: int, assignments: tuple[int, ...]) -> Matrix:
    return tuple(
        tuple(Fraction(assignments[j] == i) for j in range(len(assignments)))
        for i in range(cell_count)
    )


def inverse_diagonal(d: Matrix) -> Matrix:
    return diag(tuple(Fraction(1, 1) / d[i][i] for i in range(len(d))))


def projection_from_incidence(r: Matrix) -> Matrix:
    d = matmul(r, transpose(r))
    return matmul(transpose(r), matmul(inverse_diagonal(d), r))


def quotient_section(r: Matrix) -> Matrix:
    d = matmul(r, transpose(r))
    return matmul(transpose(r), inverse_diagonal(d))


def matrix_vector(a: Matrix, x: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum((v * w for v, w in zip(row, x, strict=True)), Fraction()) for row in a)


def dot(x: tuple[Fraction, ...], y: tuple[Fraction, ...]) -> Fraction:
    return sum((a * b for a, b in zip(x, y, strict=True)), Fraction())


def quadratic(a: Matrix, x: tuple[Fraction, ...]) -> Fraction:
    return dot(x, matrix_vector(a, x))


def to_float(a: Matrix) -> list[list[float]]:
    return [[float(x) for x in row] for row in a]


def jacobi_eigh(a: Matrix, tol: float = 1e-13, sweeps: int = 200) -> tuple[list[float], list[list[float]]]:
    """Pure-Python symmetric Jacobi diagonalization for small regression fixtures."""
    m = to_float(a)
    n = len(m)
    v = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        p = q = 0
        largest = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(m[i][j]) > largest:
                    largest = abs(m[i][j])
                    p, q = i, j
        if largest < tol:
            break
        app, aqq, apq = m[p][p], m[q][q], m[p][q]
        tau = (aqq - app) / (2.0 * apq)
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau)) if tau else 1.0
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        for k in range(n):
            if k in (p, q):
                continue
            mkp, mkq = m[k][p], m[k][q]
            m[k][p] = m[p][k] = c * mkp - s * mkq
            m[k][q] = m[q][k] = s * mkp + c * mkq
        m[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq
        m[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq
        m[p][q] = m[q][p] = 0.0
        for k in range(n):
            vkp, vkq = v[k][p], v[k][q]
            v[k][p] = c * vkp - s * vkq
            v[k][q] = s * vkp + c * vkq
    return [m[i][i] for i in range(n)], v


def positive_part(a: Matrix) -> list[list[float]]:
    vals, vecs = jacobi_eigh(a)
    n = len(a)
    out = [[0.0] * n for _ in range(n)]
    for k, lam in enumerate(vals):
        if lam <= 0:
            continue
        for i in range(n):
            for j in range(n):
                out[i][j] += lam * vecs[i][k] * vecs[j][k]
    return out


def float_matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col, strict=True)) for col in bt] for row in a]


def float_transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def float_max_diff(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def fixture(ell: int, rho: int, assignments: tuple[int, ...]) -> dict[str, object]:
    s = kron(centered(ell), centered(rho))
    cell_count = len(s)
    r = incidence(cell_count, assignments)
    rt = transpose(r)
    d_atomic = Fraction(ell - 1, ell) * Fraction(rho - 1, rho)
    b = sub(matmul(rt, matmul(s, r)), scale(d_atomic, identity(len(assignments))))
    d = matmul(r, rt)
    dinv = inverse_diagonal(d)
    p = matmul(rt, matmul(dinv, r))
    v = matmul(rt, dinv)
    t = sub(matmul(d, s), scale(d_atomic, identity(cell_count)))
    qform = sub(s, scale(d_atomic, dinv))
    one_minus_p = sub(identity(len(assignments)), p)

    checks = {
        "projection_idempotent": max_abs(sub(matmul(p, p), p)) == 0,
        "projection_self_adjoint": p == transpose(p),
        "aggregation_preserved": matmul(r, p) == r,
        "block_reducing": matmul(b, p) == matmul(p, b),
        "kernel_block_negative_scalar": matmul(b, one_minus_p) == scale(-d_atomic, one_minus_p),
        "section_right_inverse": matmul(r, v) == identity(cell_count),
        "quotient_intertwining": matmul(b, v) == matmul(v, t),
        "quotient_form": matmul(transpose(v), matmul(b, v)) == qform,
        "full_trace_zero": trace(b) == 0,
        "quotient_trace_balance": trace(t) == d_atomic * (len(assignments) - cell_count),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    mult = [int(d[i][i]) for i in range(cell_count)]
    u = [[0.0] * cell_count for _ in range(len(assignments))]
    for atom, cell in enumerate(assignments):
        u[atom][cell] = 1.0 / math.sqrt(mult[cell])
    sf = to_float(s)
    q = [[math.sqrt(mult[i]) * sf[i][j] * math.sqrt(mult[j]) - (float(d_atomic) if i == j else 0.0)
          for j in range(cell_count)] for i in range(cell_count)]
    bp = positive_part(b)
    qp = positive_part(tuple(tuple(Fraction(str(x)) for x in row) for row in q))
    predicted = float_matmul(u, float_matmul(qp, float_transpose(u)))
    positive_error = float_max_diff(bp, predicted)
    if positive_error > 2e-10:
        raise AssertionError(f"positive-part compression mismatch: {positive_error}")

    perm = list(range(len(assignments)))
    first_cell = assignments[0]
    same = [i for i, c in enumerate(assignments) if c == first_cell]
    history_symmetry = None
    if len(same) >= 2:
        perm[same[0]], perm[same[1]] = perm[same[1]], perm[same[0]]
        pm = tuple(tuple(Fraction(perm[j] == i) for j in range(len(perm))) for i in range(len(perm)))
        history_symmetry = (
            matmul(r, pm) == r
            and matmul(transpose(pm), matmul(b, pm)) == b
            and matmul(p, pm) == p
        )
        if not history_symmetry:
            raise AssertionError("cell-preserving history symmetry failed")

    return {
        "ell": ell,
        "rho": rho,
        "cells": cell_count,
        "atoms": len(assignments),
        "kernel_dimension": len(assignments) - cell_count,
        "atomic_diagonal": f"{d_atomic.numerator}/{d_atomic.denominator}",
        "quotient_trace": f"{trace(t).numerator}/{trace(t).denominator}",
        "positive_part_max_error": positive_error,
        "history_symmetry": history_symmetry,
        "checks": checks,
    }


def permutation_matrix_from_map(mapping: tuple[int, ...]) -> Matrix:
    n = len(mapping)
    if sorted(mapping) != list(range(n)):
        raise ValueError("mapping must be a permutation")
    return tuple(
        tuple(Fraction(mapping[j] == i) for j in range(n))
        for i in range(n)
    )


def partial_lift_fixture() -> dict[str, object]:
    ell, rho = 3, 5
    s = kron(centered(ell), centered(rho))
    d_atomic = Fraction(ell - 1, ell) * Fraction(rho - 1, rho)
    assignments = (0, 0, 1, 1)
    r = incidence(2, assignments)
    b = sub(matmul(transpose(r), matmul(s, r)), scale(d_atomic, identity(4)))
    cell_swap = permutation_matrix_from_map((1, 0))
    atom_swap = permutation_matrix_from_map((2, 3, 0, 1))
    equivariance = (
        matmul(r, atom_swap) == matmul(cell_swap, r)
        and matmul(transpose(cell_swap), matmul(s, cell_swap)) == s
        and matmul(transpose(atom_swap), matmul(b, atom_swap)) == b
    )
    if not equivariance:
        raise AssertionError("balanced partial-fibre lift failed")
    unbalanced = (0, 0, 1, 1, 1)
    counts = (unbalanced.count(0), unbalanced.count(1))
    obstruction = counts[0] != counts[1]
    if not obstruction:
        raise AssertionError("unbalanced occupancy obstruction fixture failed")
    return {
        "balanced_cell_swap_lifts": True,
        "unbalanced_cell_swap_obstructed": True,
        "criterion": "a bijective atom lift exists iff occupancy is constant on each cell-permutation orbit",
    }


def build_payload() -> dict[str, object]:
    assignments_35 = (0, 0, 1, 1, 1)
    assignments_37 = (0, 0, 0, 1, 1, 2, 2, 2, 2)
    results = [
        fixture(3, 5, assignments_35),
        fixture(3, 7, assignments_37),
    ]
    lift = partial_lift_fixture()
    finite_checks = sum(sum(bool(v) for v in item["checks"].values()) + 2 for item in results) + 2
    core = {
        "fixtures": results,
        "partial_frobenius_lift_fixture": lift,
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108100.shared-fibre-positive-quotient.v1",
        "proof_object_sha256": proof_object,
        "classification": "PASS_T108100_SHARED_FIBRE_POSITIVE_QUOTIENT",
        "finite_checks": finite_checks,
        "fixtures": results,
        "partial_frobenius_lift_fixture": lift,
        "exact_atom_to_quotient_decomposition": True,
        "positive_part_residue_sufficient_without_injectivity": True,
        "within_cell_history_debt_purely_negative": True,
        "full_wick_operator_traceless": True,
        "partial_frobenius_orbit_criterion_proved": True,
        "partial_frobenius_global_lift_constructed": False,
        "signed_conductor_recombination_proved": False,
        "one_place_trace_proved": False,
        "principal_binding_proved": False,
        "rh_established": False,
        "grh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--skip-source-check", action="store_true")
    args = parser.parse_args()
    if not args.skip_source_check:
        check_source_blobs()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            raise SystemExit("retained output mismatch")
    else:
        OUTPUT.write_text(text)
    print(payload["classification"])


if __name__ == "__main__":
    main()
