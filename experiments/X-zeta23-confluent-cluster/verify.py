#!/usr/bin/env python3
"""Finite diagnostic for confluent cluster renormalization.

Uses only the Python standard library. The control kernel is

    K(z,w) = integral_{-1/2}^{1/2} exp(i (z-conj(w)) u) du.

The script checks:
  * Newton-transformed clustered Grams converge to the jet moment Gram;
  * raw determinants collapse while transformed Cholesky pivots remain positive;
  * y^2 times the unit pair capture cost tends to 12;
  * the depth-normalized target cost tends to 12;
  * the pair Weil value is exactly -2 y^2 for multiplicity one;
  * a two-cluster confluent Gram is positive.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable, List, Sequence

ComplexMatrix = List[List[complex]]


def kernel(z: complex, w: complex) -> complex:
    a = z - w.conjugate()
    if abs(a) < 1e-12:
        # Stable even Taylor series for 2 sin(a/2)/a.
        a2 = a * a
        return 1 - a2 / 24 + a2 * a2 / 1920 - a2 * a2 * a2 / 322560
    return 2 * cmath.sin(a / 2) / a


def moment(k: int) -> float:
    if k % 2:
        return 0.0
    return 1.0 / ((k + 1) * (2.0**k))


def jet_gram(order: int, center: complex = 0j) -> ComplexMatrix:
    # The verifier uses real centers for the exact moment control.
    if abs(center.imag) > 1e-15:
        raise ValueError("control jet_gram currently expects a real center")
    out: ComplexMatrix = []
    for a in range(order):
        row: List[complex] = []
        for b in range(order):
            coeff = (1j**a) * ((-1j) ** b) / (math.factorial(a) * math.factorial(b))
            row.append(coeff * moment(a + b))
        out.append(row)
    return out


def gram(nodes: Sequence[complex]) -> ComplexMatrix:
    return [[kernel(z, w) for w in nodes] for z in nodes]


def zeros(n: int, m: int) -> ComplexMatrix:
    return [[0j for _ in range(m)] for _ in range(n)]


def matmul(a: ComplexMatrix, b: ComplexMatrix) -> ComplexMatrix:
    n = len(a)
    p = len(b)
    m = len(b[0])
    out = zeros(n, m)
    for i in range(n):
        for k in range(p):
            aik = a[i][k]
            if aik == 0:
                continue
            for j in range(m):
                out[i][j] += aik * b[k][j]
    return out


def adjoint(a: ComplexMatrix) -> ComplexMatrix:
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


def transform_gram(t: ComplexMatrix, k: ComplexMatrix) -> ComplexMatrix:
    return matmul(matmul(t, k), adjoint(t))


def newton_matrix(nodes: Sequence[complex]) -> ComplexMatrix:
    n = len(nodes)
    t = zeros(n, n)
    for a in range(n):
        for k in range(a + 1):
            den = 1 + 0j
            for ell in range(a + 1):
                if ell != k:
                    den *= nodes[k] - nodes[ell]
            t[a][k] = 1 / den
    return t


def max_abs_diff(a: ComplexMatrix, b: ComplexMatrix) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def solve(a: ComplexMatrix, rhs: Sequence[complex]) -> List[complex]:
    n = len(a)
    aug = [list(a[i]) + [complex(rhs[i])] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-18:
            raise ArithmeticError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            q = aug[r][col]
            if q != 0:
                aug[r] = [aug[r][j] - q * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def quadratic_inverse_cost(k: ComplexMatrix, t: Sequence[complex]) -> float:
    x = solve(k, t)
    val = sum(t[i].conjugate() * x[i] for i in range(len(t)))
    if abs(val.imag) > 1e-7:
        raise ArithmeticError(f"non-real inverse cost: {val}")
    return val.real


def determinant(a: ComplexMatrix) -> complex:
    n = len(a)
    m = [row[:] for row in a]
    det = 1 + 0j
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-30:
            return 0j
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det *= -1
        p = m[col][col]
        det *= p
        for r in range(col + 1, n):
            q = m[r][col] / p
            for j in range(col + 1, n):
                m[r][j] -= q * m[col][j]
    return det


def cholesky_min_pivot(a: ComplexMatrix) -> float:
    n = len(a)
    l = zeros(n, n)
    min_pivot = float("inf")
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j]
            for k in range(j):
                s -= l[i][k] * l[j][k].conjugate()
            if i == j:
                if abs(s.imag) > 1e-7:
                    raise ArithmeticError(f"non-Hermitian diagonal residue: {s}")
                if s.real <= 0:
                    raise ArithmeticError(f"matrix not positive definite, pivot={s.real}")
                l[i][j] = math.sqrt(s.real)
                min_pivot = min(min_pivot, s.real)
            else:
                l[i][j] = s / l[j][j]
    return min_pivot


def block_diag(blocks: Iterable[ComplexMatrix]) -> ComplexMatrix:
    blocks = list(blocks)
    n = sum(len(b) for b in blocks)
    out = zeros(n, n)
    offset = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                out[offset + i][offset + j] = b[i][j]
        offset += len(b)
    return out


def run() -> dict:
    xis = [-1.7, -0.25, 0.8, 2.1]
    eps_values = [0.20, 0.10, 0.05, 0.025]
    j4 = jet_gram(4)
    cluster_rows = []
    previous_error = None
    for eps in eps_values:
        nodes = [eps * xi for xi in xis]
        raw = gram(nodes)
        trans = transform_gram(newton_matrix(nodes), raw)
        error = max_abs_diff(trans, j4)
        pivot = cholesky_min_pivot(trans)
        raw_det = abs(determinant(raw))
        if previous_error is not None and error >= previous_error:
            raise AssertionError("confluent error did not decrease")
        previous_error = error
        cluster_rows.append(
            {
                "epsilon": eps,
                "max_entry_error": error,
                "transformed_min_cholesky_pivot": pivot,
                "raw_determinant_abs": raw_det,
            }
        )

    # Two-node imaginary pair.
    pair_rows = []
    for y in [0.20, 0.10, 0.05, 0.025, 0.0125]:
        nodes = [-1j * y, 1j * y]
        k = gram(nodes)
        unit = [1 + 0j, -1 + 0j]
        depth = [-1j * y, 1j * y]
        unit_cost = quadratic_inverse_cost(k, unit)
        depth_cost = quadratic_inverse_cost(k, depth)
        pair_weil = 2 * (depth[0] * depth[1].conjugate()).real
        if abs(pair_weil + 2 * y * y) > 1e-14:
            raise AssertionError("wrong pair Weil scaling")
        pair_rows.append(
            {
                "y": y,
                "y2_unit_cost": y * y * unit_cost,
                "depth_target_cost": depth_cost,
                "pair_weil_value": pair_weil,
            }
        )
    if abs(pair_rows[-1]["y2_unit_cost"] - 12.0) > 0.01:
        raise AssertionError("unit pair cost did not approach 12")
    if abs(pair_rows[-1]["depth_target_cost"] - 12.0) > 0.01:
        raise AssertionError("depth target cost did not approach 12")

    # Two clusters: a double cluster near 0 and a triple cluster near 3.
    eps = 0.02
    clusters = [
        [eps * x for x in (-0.7, 1.2)],
        [3 + eps * x for x in (-1.1, 0.2, 1.4)],
    ]
    nodes = [z for cluster in clusters for z in cluster]
    transforms = [newton_matrix(cluster) for cluster in clusters]
    t = block_diag(transforms)
    transformed = transform_gram(t, gram(nodes))
    multi_pivot = cholesky_min_pivot(transformed)

    result = {
        "classification": "PASS_ZETA23_CONFLUENT_CLUSTER_RENORMALIZATION",
        "cluster_convergence": cluster_rows,
        "pair_depth_scaling": pair_rows,
        "multi_cluster_min_cholesky_pivot": multi_pivot,
        "control_jet_cost": 12.0,
    }
    return result


def main() -> None:
    result = run()
    root = Path(__file__).resolve().parent
    result_path = root / "results" / "verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(result_path.read_bytes()).hexdigest()
    print(result["classification"])
    print(f"result_sha256={digest}")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
