#!/usr/bin/env python3
"""Exact verifier for L-14314/L-14315 synthetic controls.

Trust boundary: Python integers and fractions.Fraction only after JSON parsing.
No floating point, eigensolver, special function, or numerical quadrature is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "riemann.exact-prolate-source-repair.v1"
OUT_SCHEMA = "riemann.exact-prolate-source-repair.verification.v1"


class VerificationError(ValueError):
    """Raised when a certificate fails closed."""


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise VerificationError("booleans are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise VerificationError(f"invalid rational string: {value!r}") from exc
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n, d = value["numerator"], value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool) or not isinstance(n, int) or not isinstance(d, int):
            raise VerificationError("fraction object requires integer numerator/denominator")
        if d == 0:
            raise VerificationError("zero denominator")
        return Fraction(n, d)
    raise VerificationError(f"unsupported rational object: {value!r}")


def dot(x: Iterable[Fraction], y: Iterable[Fraction]) -> Fraction:
    xs, ys = list(x), list(y)
    if len(xs) != len(ys):
        raise VerificationError("dimension mismatch in dot product")
    return sum((a * b for a, b in zip(xs, ys)), Fraction(0))


def mat_vec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if any(len(row) != len(x) for row in a):
        raise VerificationError("matrix/vector dimension mismatch")
    return [dot(row, x) for row in a]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or any(len(row) != len(a[0]) for row in a):
        raise VerificationError("ragged matrix")
    return [list(col) for col in zip(*a)]


def symmetric(a: list[list[Fraction]]) -> bool:
    return bool(a) and len(a) == len(a[0]) and a == transpose(a)


def inv2(a: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != 2 or any(len(row) != 2 for row in a):
        raise VerificationError("expected a 2x2 matrix")
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if det == 0:
        raise VerificationError("singular 2x2 matrix")
    return [
        [a[1][1] / det, -a[0][1] / det],
        [-a[1][0] / det, a[0][0] / det],
    ]


def is_spd2(a: list[list[Fraction]]) -> bool:
    return symmetric(a) and len(a) == 2 and a[0][0] > 0 and a[0][0] * a[1][1] - a[0][1] ** 2 > 0


def qform(a: list[list[Fraction]], x: list[Fraction], y: list[Fraction] | None = None) -> Fraction:
    if y is None:
        y = x
    return dot(x, mat_vec(a, y))


def canonical_sha256(data: Any) -> str:
    blob = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def as_string(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify_three_mode(section: dict[str, Any]) -> dict[str, Any]:
    modes = section.get("modes")
    if not isinstance(modes, list) or len(modes) != 3:
        raise VerificationError("three_mode.modes must contain exactly three rows")

    v = [frac(row["value_at_zero"]) for row in modes]
    chi = [frac(row["concentration_eigenvalue"]) for row in modes]
    if any(x == 0 for x in v):
        raise VerificationError("all three even-mode values at zero must be nonzero")
    if not (Fraction(1) >= chi[0] > chi[1] > chi[2] > 0):
        raise VerificationError("concentration eigenvalues must satisfy 1 >= chi0 > chi1 > chi2 > 0")

    m = [v[j] * chi[j] for j in range(3)]
    a = [
        v[1] * m[2] - v[2] * m[1],
        v[2] * m[0] - v[0] * m[2],
        v[0] * m[1] - v[1] * m[0],
    ]
    if all(x == 0 for x in a):
        raise VerificationError("cross-product source vector vanished")

    value_constraint = dot(a, v)
    integral_constraint = dot(a, m)
    if value_constraint != 0 or integral_constraint != 0:
        raise VerificationError("source constraints did not vanish exactly")

    norm_sq = dot(a, a)
    leakage_numerator = 2 * sum((a[j] * a[j] * (1 - chi[j]) for j in range(3)), Fraction(0))
    leakage_sq = leakage_numerator / norm_sq
    leakage_bound_sq = 2 * (1 - chi[2])
    if leakage_sq > leakage_bound_sq:
        raise VerificationError("exact leakage exceeded the first-excluded-mode bound")

    expected = section.get("expected")
    if expected is not None:
        if [frac(x) for x in expected.get("coefficients", [])] != a:
            raise VerificationError("claimed coefficient vector is false")
        if frac(expected.get("normalized_leakage_squared")) != leakage_sq:
            raise VerificationError("claimed normalized leakage is false")
        if frac(expected.get("leakage_bound_squared")) != leakage_bound_sq:
            raise VerificationError("claimed leakage bound is false")

    return {
        "coefficients": [as_string(x) for x in a],
        "value_constraint": as_string(value_constraint),
        "integral_constraint": as_string(integral_constraint),
        "coefficient_norm_squared": as_string(norm_sq),
        "normalized_leakage_squared": as_string(leakage_sq),
        "leakage_bound_squared": as_string(leakage_bound_sq),
        "constraints_exact": True,
        "leakage_gate": "PASS",
    }


def verify_radical(section: dict[str, Any]) -> dict[str, Any]:
    q = [[frac(x) for x in row] for row in section.get("form_matrix", [])]
    if len(q) != 3 or any(len(row) != 3 for row in q) or not symmetric(q):
        raise VerificationError("radical.form_matrix must be symmetric 3x3")
    r = [frac(x) for x in section.get("radical_vector", [])]
    if len(r) != 3 or all(x == 0 for x in r):
        raise VerificationError("radical_vector must be nonzero and three-dimensional")
    if mat_vec(q, r) != [Fraction(0)] * 3:
        raise VerificationError("declared radical vector is not in the radical")

    w = [[frac(x) for x in row] for row in section.get("localized_weight", [])]
    if not is_spd2(w):
        raise VerificationError("localized_weight must be symmetric positive definite 2x2")

    k_local = r[:2]
    if all(x == 0 for x in k_local):
        raise VerificationError("localized radical truncation is zero")
    k = [r[0], r[1], Fraction(0)]
    t = [Fraction(0), Fraction(0), r[2]]
    a = [row[:2] for row in q[:2]]
    y = mat_vec(a, k_local)

    for basis in ([Fraction(1), Fraction(0), Fraction(0)], [Fraction(0), Fraction(1), Fraction(0)]):
        if qform(q, k, basis) != -qform(q, t, basis):
            raise VerificationError("radical-tail cross-form identity failed")
    if qform(q, k) != qform(q, t):
        raise VerificationError("radical-tail energy identity failed")

    winv = inv2(w)
    winv_y = mat_vec(winv, y)
    winv_k = mat_vec(winv, k_local)
    denom = dot(k_local, winv_k)
    if denom <= 0:
        raise VerificationError("weighted projective denominator is nonpositive")
    projective_sq = dot(y, winv_y) - dot(y, winv_k) ** 2 / denom

    n = [-k_local[1], k_local[0]]
    n3 = [n[0], n[1], Fraction(0)]
    dual_denom = qform(w, n)
    if dual_denom <= 0:
        raise VerificationError("dual weighted denominator is nonpositive")
    tail_cross = qform(q, t, n3)
    dual_sq = tail_cross * tail_cross / dual_denom
    if projective_sq != dual_sq:
        raise VerificationError("weighted quotient and radical-tail dual values disagree")

    expected = section.get("expected")
    if expected is not None and frac(expected.get("projective_residual_squared")) != projective_sq:
        raise VerificationError("claimed projective residual is false")

    return {
        "radical_gate": "PASS",
        "cross_form_transport": "PASS",
        "energy_transport": "PASS",
        "projective_residual_squared": as_string(projective_sq),
        "dual_tail_cross_squared": as_string(dual_sq),
        "quotient_duality_exact": True,
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise VerificationError(f"expected schema {SCHEMA!r}")
    if set(data) != {"schema", "three_mode", "radical_tail"}:
        raise VerificationError("certificate must contain exactly schema, three_mode, radical_tail")

    return {
        "schema": OUT_SCHEMA,
        "input_sha256": canonical_sha256(data),
        "three_mode": verify_three_mode(data["three_mode"]),
        "radical_tail": verify_radical(data["radical_tail"]),
        "verdict": "CERTIFIED_EXACT_SOURCE_AND_PROJECTIVE_RADICAL_TAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise VerificationError("top-level JSON value must be an object")
        result = verify_certificate(data)
    except (OSError, json.JSONDecodeError, VerificationError, KeyError, TypeError) as exc:
        parser.error(str(exc))

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
