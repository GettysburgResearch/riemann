#!/usr/bin/env python3
"""Exact checker for the finite algebra in L-15110.

The checker uses only integers and fractions.Fraction. It verifies:

* the zero-integral 0/4 target;
* a complete rational basis of its constrained complement;
* the mode-next coercivity floor, centered at the target Rayleigh value;
* the exact projected target residual;
* the Fuchs 4-to-8 rational coefficient and lambda exponent.

It does not evaluate prolate functions, the Weil form, pi, or zeta.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15104-constrained-prolate-mode8.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
    return value


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = integer(value[0], name + "[0]")
        q = integer(value[1], name + "[1]")
        if q == 0:
            raise CertificateError(f"{name} denominator is zero")
        return Fraction(p, q)
    raise CertificateError(f"{name} must be an integer, fraction string, or [p,q]")


def vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty list")
    return [rational(item, f"{name}[{i}]") for i, item in enumerate(raw)]


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty list")
    rows = [vector(row, f"{name}[{i}]") for i, row in enumerate(raw)]
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise CertificateError(f"{name} is ragged")
    return rows


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(x, y)), Fraction())


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    bt = transpose(b)
    return [[dot(row, column) for column in bt] for row in a]


def matvec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [dot(row, x) for row in a]


def diagonal(values: list[Fraction]) -> list[list[Fraction]]:
    n = len(values)
    return [[values[i] if i == j else Fraction() for j in range(n)] for i in range(n)]


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix subtraction mismatch")
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * value for value in row] for row in a]


def rank(a: list[list[Fraction]]) -> int:
    m = [row[:] for row in a]
    if not m:
        return 0
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        value = m[r][c]
        m[r] = [x / value for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                factor = m[i][c]
                m[i] = [x - factor * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r


def solve(a: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a) or len(b) != n:
        raise CertificateError("solve expects one square system")
    m = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for c in range(n):
        pivot = next((i for i in range(c, n) if m[i][c]), None)
        if pivot is None:
            raise CertificateError("singular linear system")
        m[c], m[pivot] = m[pivot], m[c]
        value = m[c][c]
        m[c] = [x / value for x in m[c]]
        for i in range(n):
            if i != c and m[i][c]:
                factor = m[i][c]
                m[i] = [x - factor * y for x, y in zip(m[i], m[c])]
    return [m[i][-1] for i in range(n)]


def ldl_pivots(a: list[list[Fraction]]) -> list[Fraction]:
    n = len(a)
    if any(len(row) != n for row in a):
        raise CertificateError("LDL expects square matrix")
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise CertificateError("LDL matrix is not symmetric")
    l = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    d = [Fraction() for _ in range(n)]
    for j in range(n):
        d[j] = a[j][j] - sum(l[j][k] * l[j][k] * d[k] for k in range(j))
        if d[j] == 0:
            raise CertificateError("zero LDL pivot")
        for i in range(j + 1, n):
            l[i][j] = (
                a[i][j] - sum(l[i][k] * l[j][k] * d[k] for k in range(j))
            ) / d[j]
    return d


def canonical_sha256(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")

    defects = vector(payload.get("defects"), "defects")
    coeffs = vector(payload.get("integral_coefficients"), "integral_coefficients")
    basis = matrix(payload.get("complement_basis"), "complement_basis")
    n = len(defects)
    if len(coeffs) != n or any(len(row) != n for row in basis):
        raise CertificateError("primitive dimension mismatch")
    if n < 3:
        raise CertificateError("at least three prolate modes are required")
    if any(defects[i] > defects[i + 1] for i in range(n - 1)):
        raise CertificateError("defects must be nondecreasing in the supplied model")

    target_indices = payload.get("target_indices")
    if not isinstance(target_indices, list) or len(target_indices) != 2:
        raise CertificateError("target_indices must have length two")
    i0 = integer(target_indices[0], "target_indices[0]")
    i4 = integer(target_indices[1], "target_indices[1]")
    next_index = integer(payload.get("next_index"), "next_index")
    if len({i0, i4, next_index}) != 3 or not all(0 <= i < n for i in (i0, i4, next_index)):
        raise CertificateError("invalid target/next indices")

    a0, a4 = coeffs[i0], coeffs[i4]
    if a0 == 0 or a4 == 0:
        raise CertificateError("target integral coefficients must be nonzero")
    a2 = a0 * a0 + a4 * a4
    functional_norm2 = rational(payload.get("functional_norm2"), "functional_norm2")
    if functional_norm2 <= a2:
        raise CertificateError("functional norm must exceed the low coefficient norm")

    target = [Fraction() for _ in range(n)]
    target[i0] = a4
    target[i4] = -a0
    if dot(coeffs, target) != 0:
        raise CertificateError("constructed target is not zero-integral")

    if len(basis) != n - 2:
        raise CertificateError("complement_basis must contain exactly n-2 rows")
    for row in basis:
        if dot(row, target) != 0 or dot(row, coeffs) != 0:
            raise CertificateError("complement basis violates a constraint")
    if rank(basis) != n - 2:
        raise CertificateError("complement basis is not full rank")
    if rank([target, coeffs]) != 2:
        raise CertificateError("target and integral constraints are dependent")

    bmat = transpose(basis)
    bt = transpose(bmat)
    gram = matmul(bt, bmat)
    dmat = diagonal(defects)
    form = matmul(matmul(bt, dmat), bmat)

    mu = (a4 * a4 * defects[i0] + a0 * a0 * defects[i4]) / a2
    raw_floor = defects[next_index] * a2 / functional_norm2
    centered_floor = raw_floor - mu
    if centered_floor <= 0:
        raise CertificateError("centered mode-next floor is not positive")

    raw_matrix = subtract(form, scale(gram, raw_floor))
    raw_pivots = ldl_pivots(raw_matrix)
    if any(pivot <= 0 for pivot in raw_pivots):
        raise CertificateError("raw mode-next floor is not certified")

    centered_matrix = subtract(
        subtract(form, scale(gram, mu)), scale(gram, centered_floor)
    )
    centered_pivots = ldl_pivots(centered_matrix)
    if any(pivot <= 0 for pivot in centered_pivots):
        raise CertificateError("centered complement floor is not certified")

    dtarget = matvec(dmat, target)
    rhs = matvec(bt, dtarget)
    coordinates = solve(gram, rhs)
    projected_sq_unnormalized = dot(rhs, coordinates)
    projected_sq = projected_sq_unnormalized / a2

    formula_sq = (
        (a0 * a0 * a4 * a4) / (a2 * a2)
        * (defects[i4] - defects[i0]) ** 2
        * (1 - a2 / functional_norm2)
    )
    if projected_sq != formula_sq:
        raise CertificateError("projected residual does not match the closed formula")

    claimed = payload.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    expected_claims = {
        "A2": a2,
        "target_rayleigh": mu,
        "raw_floor": raw_floor,
        "centered_floor": centered_floor,
        "residual_squared": projected_sq,
    }
    for name, expected in expected_claims.items():
        if rational(claimed.get(name), f"claimed.{name}") != expected:
            raise CertificateError(f"false claimed value: {name}")

    fuchs = payload.get("fuchs_ratio")
    if not isinstance(fuchs, dict):
        raise CertificateError("fuchs_ratio must be an object")
    m = integer(fuchs.get("lower_mode"), "fuchs_ratio.lower_mode")
    k = integer(fuchs.get("upper_mode"), "fuchs_ratio.upper_mode")
    if (m, k) != (4, 8):
        raise CertificateError("this checker expects the 4-to-8 Fuchs ratio")
    rational_coefficient = (
        Fraction(2 ** (4 * m + 1), factorial(m))
        / Fraction(2 ** (4 * k + 1), factorial(k))
    )
    if rational(fuchs.get("rational_coefficient"), "fuchs_ratio.rational_coefficient") != rational_coefficient:
        raise CertificateError("false Fuchs rational coefficient")
    if integer(fuchs.get("lambda_power"), "fuchs_ratio.lambda_power") != 2 * m - 2 * k:
        raise CertificateError("false Fuchs lambda exponent")
    if integer(fuchs.get("pi_power"), "fuchs_ratio.pi_power") != m - k:
        raise CertificateError("false Fuchs pi exponent")

    hermite_limit_rational = Fraction(32, 121) * rational_coefficient
    if rational(
        fuchs.get("final_rational_coefficient"),
        "fuchs_ratio.final_rational_coefficient",
    ) != hermite_limit_rational:
        raise CertificateError("false final lambda^-7 rational coefficient")

    proof_object = {
        "A2": str(a2),
        "target_rayleigh": str(mu),
        "raw_mode_next_floor": str(raw_floor),
        "centered_mode_next_floor": str(centered_floor),
        "residual_squared": str(projected_sq),
        "raw_ldl_pivots": [str(x) for x in raw_pivots],
        "centered_ldl_pivots": [str(x) for x in centered_pivots],
        "fuchs_4_to_8_rational_coefficient": str(rational_coefficient),
        "fuchs_lambda_power": 2 * m - 2 * k,
        "fuchs_pi_power": m - k,
        "final_rational_coefficient_times_sqrt3_over_pi4": str(hermite_limit_rational),
    }
    return {
        "schema": SCHEMA,
        "classification": "CERTIFIED_EXACT_FINITE_PROLATE_ALGEBRA",
        "proof_object": proof_object,
        "proof_object_sha256": canonical_sha256(proof_object),
        "proof_boundary": (
            "Exact rational finite algebra only. The checker does not evaluate "
            "prolate eigenfunctions, Fuchs asymptotics, the localized Weil form, "
            "the Hardy metric, or the Riemann zeta function."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "classification": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
