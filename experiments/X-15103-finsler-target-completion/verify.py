#!/usr/bin/env python3
"""Exact checker for target-pinned scalar completions.

The checker verifies one of three finite rational proof objects:

* ``feasible``: a rational scalar c makes the target-pinned matrix positive
  definite on the Euclidean orthogonal complement of the prescribed target p;
* ``null-obstruction``: a nonzero B-isotropic complement direction has
  nonpositive A-value, ruling out every strict scalar completion;
* ``pair-obstruction``: one B-positive and one B-negative direction impose
  incompatible strict scalar thresholds.

Only exact integer/Fraction arithmetic is used. The checker does not prove the
imported Connes--van Suijlekom real-zero theorem or any Riemann-Hypothesis
conclusion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.target-pinned-finsler-completion.v1"


class CertificateError(ValueError):
    """Malformed or false finite certificate."""


def rational(raw: Any, name: str) -> Fraction:
    if isinstance(raw, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(raw, int):
        return Fraction(raw)
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    num, den = raw.get("numerator"), raw.get("denominator")
    if (
        isinstance(num, bool)
        or not isinstance(num, int)
        or isinstance(den, bool)
        or not isinstance(den, int)
        or den <= 0
    ):
        raise CertificateError(f"bad rational at {name}")
    return Fraction(num, den)


def vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty list")
    return [rational(value, f"{name}[{index}]") for index, value in enumerate(raw)]


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty square matrix")
    rows = []
    for i, row in enumerate(raw):
        if not isinstance(row, list):
            raise CertificateError(f"{name}[{i}] must be a list")
        rows.append([rational(value, f"{name}[{i}][{j}]") for j, value in enumerate(row)])
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise CertificateError(f"{name} must be square")
    return rows


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def mat_vec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if any(len(row) != len(x) for row in a):
        raise CertificateError("matrix-vector dimension mismatch")
    return [dot(row, x) for row in a]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def mat_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or not b or len(a[0]) != len(b):
        raise CertificateError("matrix multiplication dimension mismatch")
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def add_scaled(
    a: list[list[Fraction]], b: list[list[Fraction]], scalar: Fraction
) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix addition dimension mismatch")
    return [
        [x + scalar * y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(a, b)
    ]


def quadratic(a: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return dot(x, mat_vec(a, x))


def require_symmetric(a: list[list[Fraction]], name: str) -> None:
    n = len(a)
    for i in range(n):
        for j in range(i):
            if a[i][j] != a[j][i]:
                raise CertificateError(f"{name} is not symmetric at ({i},{j})")


def complement_basis(p: list[Fraction]) -> list[list[Fraction]]:
    """Return an n by (n-1) rational basis U with U^T p=0."""
    n = len(p)
    pivot = next((i for i, value in enumerate(p) if value != 0), None)
    if pivot is None:
        raise CertificateError("target vector is zero")
    columns: list[list[Fraction]] = []
    for j in range(n):
        if j == pivot:
            continue
        col = [Fraction(0) for _ in range(n)]
        col[j] = Fraction(1)
        col[pivot] = -p[j] / p[pivot]
        if dot(col, p) != 0:
            raise AssertionError("internal complement construction failed")
        columns.append(col)
    return [[columns[j][i] for j in range(n - 1)] for i in range(n)]


def restrict(a: list[list[Fraction]], u: list[list[Fraction]]) -> list[list[Fraction]]:
    return mat_mul(transpose(u), mat_mul(a, u))


def ldl_positive_pivots(a: list[list[Fraction]]) -> list[Fraction]:
    """Exact no-pivot LDL; positive pivots are equivalent to positive definiteness."""
    require_symmetric(a, "restricted matrix")
    n = len(a)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivot = a[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivot <= 0:
            raise CertificateError(f"nonpositive exact LDL pivot at index {i}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivot
    return pivots


def build_pencil(
    q: list[list[Fraction]], p: list[Fraction], eta: list[Fraction]
) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    n = len(p)
    qp = mat_vec(q, p)
    a = [row[:] for row in q]
    b = [[-eta[i] * eta[j] for j in range(n)] for i in range(n)]
    for i in range(n):
        if p[i] == 0 or eta[i] == 0:
            raise CertificateError("every p_i and eta_i must be nonzero")
        a[i][i] -= qp[i] / p[i]
        b[i][i] += eta[i] / p[i]
    if mat_vec(a, p) != [Fraction(0)] * n:
        raise AssertionError("internal A p identity failed")
    if mat_vec(b, p) != [Fraction(0)] * n:
        raise AssertionError("internal B p identity failed")
    return a, b


def slope_inertia(p: list[Fraction], eta: list[Fraction]) -> dict[str, int]:
    positive = sum(eta_i * p_i > 0 for eta_i, p_i in zip(eta, p))
    negative = len(p) - positive
    if positive < 1:
        raise CertificateError("normalization requires at least one positive eta_i p_i")
    return {
        "positive_on_full_space": positive - 1,
        "negative_on_full_space": negative,
        "zero_on_full_space": 1,
        "positive_on_complement": positive - 1,
        "negative_on_complement": negative,
    }


def graph_data(
    q: list[list[Fraction]],
    p: list[Fraction],
    eta: list[Fraction],
    c: Fraction | None,
) -> dict[str, Any]:
    same: list[Fraction] = []
    opposite: list[Fraction] = []
    weights: list[tuple[int, int, Fraction]] = []
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            quotient = q[i][j] / (eta[i] * eta[j])
            if (eta[i] * p[i]) * (eta[j] * p[j]) > 0:
                same.append(quotient)
            else:
                opposite.append(quotient)
            if c is not None:
                weight = -(q[i][j] - c * eta[i] * eta[j]) * p[i] * p[j]
                weights.append((i, j, weight))

    lower = max(same) if same else None
    upper = min(opposite) if opposite else None
    interval_nonempty = not (
        lower is not None and upper is not None and lower > upper
    )

    connected = None
    all_nonnegative = None
    if c is not None:
        all_nonnegative = all(weight >= 0 for _, _, weight in weights)
        adjacency = [[] for _ in range(n)]
        for i, j, weight in weights:
            if weight > 0:
                adjacency[i].append(j)
                adjacency[j].append(i)
        reached = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in adjacency[node]:
                if neighbor not in reached:
                    reached.add(neighbor)
                    stack.append(neighbor)
        connected = len(reached) == n

    return {
        "lower": None if lower is None else fraction_json(lower),
        "upper": None if upper is None else fraction_json(upper),
        "interval_nonempty": interval_nonempty,
        "all_weights_nonnegative_at_c": all_nonnegative,
        "positive_weight_graph_connected_at_c": connected,
        "weights": [
            {"i": i, "j": j, "value": fraction_json(weight)}
            for i, j, weight in weights
        ],
    }


def parse_common(data: dict[str, Any]):
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    q = matrix(data.get("Q"), "Q")
    require_symmetric(q, "Q")
    p = vector(data.get("p"), "p")
    eta = vector(data.get("eta"), "eta")
    n = len(q)
    if len(p) != n or len(eta) != n:
        raise CertificateError("Q, p, and eta dimensions differ")
    if any(value == 0 for value in p):
        raise CertificateError("all target coordinates p_i must be nonzero")
    if any(value == 0 for value in eta):
        raise CertificateError("all boundary coordinates eta_i must be nonzero")
    normalization = dot(eta, p)
    if normalization != 1:
        raise CertificateError("eta^T p must equal exactly 1")
    a, b = build_pencil(q, p, eta)
    u = complement_basis(p)
    return q, p, eta, a, b, u


def verify(data: dict[str, Any]) -> dict[str, Any]:
    q, p, eta, a, b, u = parse_common(data)
    mode = data.get("mode")
    common: dict[str, Any] = {
        "schema": SCHEMA,
        "mode": mode,
        "dimension": len(p),
        "target_normalization": fraction_json(dot(eta, p)),
        "slope_inertia": slope_inertia(p, eta),
        "proof_object_sha256": canonical_sha256(data),
    }

    if mode == "feasible":
        c = rational(data.get("c"), "c")
        t = add_scaled(a, b, c)
        if mat_vec(t, p) != [Fraction(0)] * len(p):
            raise CertificateError("completed matrix does not annihilate p")
        pivots = ldl_positive_pivots(restrict(t, u))
        graph = graph_data(q, p, eta, c)
        return {
            **common,
            "c": fraction_json(c),
            "complement_ldl_pivots": [fraction_json(value) for value in pivots],
            "graph_separator": graph,
            "verdict": "CERTIFIED_STRICT_TARGET_PINNED_COMPLETION",
            "scope_warning": (
                "Exact finite linear algebra only. The imported special-matrix "
                "real-zero theorem, parity/normalization adapter, target transform, "
                "and any cofinal RH implication remain separate gates."
            ),
        }

    if mode == "null-obstruction":
        x = vector(data.get("x"), "x")
        if len(x) != len(p) or all(value == 0 for value in x):
            raise CertificateError("x must be a nonzero vector of the target dimension")
        if dot(p, x) != 0:
            raise CertificateError("x is not in p-perp")
        avalue, bvalue = quadratic(a, x), quadratic(b, x)
        if bvalue != 0:
            raise CertificateError("x is not B-isotropic")
        if avalue > 0:
            raise CertificateError("A is positive on the claimed obstruction")
        return {
            **common,
            "x_A_x": fraction_json(avalue),
            "x_B_x": fraction_json(bvalue),
            "verdict": "CERTIFIED_NO_STRICT_COMPLETION_NULL_DIRECTION",
            "scope_warning": (
                "This rules out only the one-scalar target-pinned completion family "
                "for the supplied finite Q and p."
            ),
        }

    if mode == "pair-obstruction":
        x_plus = vector(data.get("x_plus"), "x_plus")
        x_minus = vector(data.get("x_minus"), "x_minus")
        if len(x_plus) != len(p) or len(x_minus) != len(p):
            raise CertificateError("obstruction vectors have the wrong dimension")
        if all(value == 0 for value in x_plus) or all(value == 0 for value in x_minus):
            raise CertificateError("obstruction vectors must be nonzero")
        if dot(p, x_plus) != 0 or dot(p, x_minus) != 0:
            raise CertificateError("obstruction vectors must lie in p-perp")
        ap, bp = quadratic(a, x_plus), quadratic(b, x_plus)
        am, bm = quadratic(a, x_minus), quadratic(b, x_minus)
        if bp <= 0 or bm >= 0:
            raise CertificateError("expected B-positive and B-negative directions")
        lower, upper = -ap / bp, -am / bm
        if lower < upper:
            raise CertificateError("the two strict scalar thresholds are compatible")
        return {
            **common,
            "positive_direction": {
                "A": fraction_json(ap),
                "B": fraction_json(bp),
                "strict_lower_c": fraction_json(lower),
            },
            "negative_direction": {
                "A": fraction_json(am),
                "B": fraction_json(bm),
                "strict_upper_c": fraction_json(upper),
            },
            "verdict": "CERTIFIED_NO_STRICT_COMPLETION_THRESHOLD_CONFLICT",
            "scope_warning": (
                "This rules out only the one-scalar target-pinned completion family "
                "for the supplied finite Q and p."
            ),
        }

    raise CertificateError("mode must be feasible, null-obstruction, or pair-obstruction")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
