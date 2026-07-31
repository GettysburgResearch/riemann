#!/usr/bin/env python3
"""Exact controls for L-16201--L-16204.

This checker uses integers and fractions.Fraction only. It verifies:

* affine-curvature and prolate-basis off-diagonal falsifiers;
* the exact source/background two-block lower certificate by rational LDL;
* the radical-tail Gram factorization on a nontrivial kernel model;
* the exact two-dimensional generalized spectral-diameter invariant;
* fail-closed schema and Boolean handling.

It is a finite algebra regression, not a CCM/Weil computation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x16201-affine-sector-audit.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
    return value


def frac(value: Any, name: str) -> Fraction:
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
    raise CertificateError(f"{name} must be integer, fraction string, or [p,q]")


def vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list):
        raise CertificateError(f"{name} must be a list")
    return [frac(value, f"{name}[{i}]") for i, value in enumerate(raw)]


def rectangular_matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    rows = [vector(row, f"{name}[{i}]") for i, row in enumerate(raw)]
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise CertificateError(f"{name} rows must have one common positive length")
    return rows


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    rows = rectangular_matrix(raw, name)
    if any(len(row) != len(rows) for row in rows):
        raise CertificateError(f"{name} must be square")
    return rows


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or not b or len(a[0]) != len(b):
        raise CertificateError("matrix dimensions do not match")
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matsub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix dimensions do not match")
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def is_symmetric(a: list[list[Fraction]]) -> bool:
    return a == transpose(a)


def ldl_pivots(a: list[list[Fraction]]) -> list[Fraction]:
    if not is_symmetric(a):
        raise CertificateError("LDL input is not symmetric")
    n = len(a)
    l = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    d = [Fraction(0) for _ in range(n)]
    for i in range(n):
        l[i][i] = Fraction(1)
        pivot = a[i][i] - sum(l[i][k] * l[i][k] * d[k] for k in range(i))
        d[i] = pivot
        if pivot == 0:
            raise CertificateError("zero LDL pivot")
        for j in range(i + 1, n):
            l[j][i] = (
                a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
            ) / pivot
    return d


def canonical_digest(payload: Any) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def verify_affine(payload: dict[str, Any]) -> dict[str, Any]:
    delta = vector(payload.get("delta"), "delta")
    alpha = vector(payload.get("alpha"), "alpha")
    a = matrix(payload.get("A_in_D_basis"), "A_in_D_basis")
    if len(delta) != len(alpha) or len(a) != len(delta):
        raise CertificateError("affine data dimensions do not match")
    if not is_symmetric(a):
        raise CertificateError("A_in_D_basis must be symmetric")
    if any(a[i][i] != alpha[i] for i in range(len(alpha))):
        raise CertificateError("alpha is not the diagonal of A")

    offdiag = max(
        (abs(a[i][j]) for i in range(len(a)) for j in range(i)),
        default=Fraction(0),
    )
    triples = []
    best = Fraction(0)
    for i in range(len(delta)):
        for j in range(i + 1, len(delta)):
            for k in range(j + 1, len(delta)):
                if len({delta[i], delta[j], delta[k]}) < 3:
                    continue
                curvature = (
                    (delta[j] - delta[k]) * alpha[i]
                    + (delta[k] - delta[i]) * alpha[j]
                    + (delta[i] - delta[j]) * alpha[k]
                )
                denom = (
                    abs(delta[j] - delta[k])
                    + abs(delta[k] - delta[i])
                    + abs(delta[i] - delta[j])
                )
                lower = abs(curvature) / denom
                best = max(best, lower)
                triples.append(
                    {
                        "indices": [i, j, k],
                        "curvature": str(curvature),
                        "denominator": str(denom),
                        "residual_lower_bound": str(lower),
                    }
                )
    return {
        "offdiagonal_residual_lower_bound": str(offdiag),
        "affine_curvature_residual_lower_bound": str(best),
        "combined_residual_lower_bound": str(max(offdiag, best)),
        "triples": triples,
    }


def verify_sector(payload: dict[str, Any]) -> dict[str, Any]:
    g_s = frac(payload.get("source_gap"), "source_gap")
    g_b = frac(payload.get("background_gap"), "background_gap")
    eta = frac(payload.get("cross_bound"), "cross_bound")
    claimed = frac(payload.get("claimed_full_gap"), "claimed_full_gap")
    if min(g_s, g_b, claimed) <= 0 or eta < 0:
        raise CertificateError("gap data must be positive and cross bound nonnegative")
    comparison = [[g_s - claimed, -eta], [-eta, g_b - claimed]]
    pivots = ldl_pivots(comparison)
    if any(p <= 0 for p in pivots):
        raise CertificateError("claimed full gap is not strictly certified")
    return {
        "comparison_matrix": [[str(x) for x in row] for row in comparison],
        "ldl_pivots": [str(x) for x in pivots],
        "claimed_full_gap": str(claimed),
        "theta_ratio": str(eta * eta / (g_s * g_b)),
    }


def verify_radical(payload: dict[str, Any]) -> dict[str, Any]:
    q = matrix(payload.get("Q"), "Q")
    j = rectangular_matrix(payload.get("J"), "J")
    p = matrix(payload.get("P"), "P")
    n = len(q)
    if len(j) != n or len(p) != n:
        raise CertificateError("Q, J, P ambient dimensions do not match")
    if not is_symmetric(q) or not is_symmetric(p):
        raise CertificateError("Q and P must be symmetric")
    if matmul(p, p) != p:
        raise CertificateError("P is not idempotent")
    zero = [[Fraction(0) for _ in range(len(j[0]))] for _ in range(n)]
    if matmul(q, j) != zero:
        raise CertificateError("J range is not in the radical")

    i_minus_p = matsub(identity(n), p)
    l_map = matmul(p, j)
    t_map = matmul(i_minus_p, j)
    a_source = matmul(transpose(l_map), matmul(q, l_map))
    q_tail = matmul(transpose(t_map), matmul(q, t_map))
    d_tail = matmul(transpose(t_map), t_map)
    if a_source != q_tail:
        raise CertificateError("radical-tail factorization failed")

    scalar = frac(payload.get("tail_scalar"), "tail_scalar")
    scalar_residual = matsub(a_source, scale(d_tail, scalar))
    return {
        "source_matrix": [[str(x) for x in row] for row in a_source],
        "tail_q_matrix": [[str(x) for x in row] for row in q_tail],
        "tail_gram": [[str(x) for x in row] for row in d_tail],
        "scalar_residual": [[str(x) for x in row] for row in scalar_residual],
        "factorization_exact": True,
    }


def verify_scalarization(payload: dict[str, Any]) -> dict[str, Any]:
    d = matrix(payload.get("D"), "tail_scalarization.D")
    a = matrix(payload.get("A"), "tail_scalarization.A")
    if len(d) != 2 or len(a) != 2:
        raise CertificateError("tail scalarization control must be 2 x 2")
    if not is_symmetric(d) or not is_symmetric(a):
        raise CertificateError("tail scalarization matrices must be symmetric")
    det_d = d[0][0] * d[1][1] - d[0][1] * d[0][1]
    det_a = a[0][0] * a[1][1] - a[0][1] * a[0][1]
    if d[0][0] <= 0 or det_d <= 0:
        raise CertificateError("tail Gram D must be positive definite")
    trace = (
        d[1][1] * a[0][0]
        + d[0][0] * a[1][1]
        - 2 * d[0][1] * a[0][1]
    ) / det_d
    determinant = det_a / det_d
    discriminant = trace * trace - 4 * determinant
    if trace <= 0 or discriminant < 0:
        raise CertificateError("generalized tail spectrum is not positive real")
    relative_square = discriminant / (trace * trace)
    claims = {
        "trace": frac(payload.get("claimed_trace"), "claimed_trace"),
        "determinant": frac(payload.get("claimed_determinant"), "claimed_determinant"),
        "discriminant": frac(payload.get("claimed_discriminant"), "claimed_discriminant"),
        "relative_square": frac(
            payload.get("claimed_relative_square"), "claimed_relative_square"
        ),
    }
    actual = {
        "trace": trace,
        "determinant": determinant,
        "discriminant": discriminant,
        "relative_square": relative_square,
    }
    for name, value in actual.items():
        if claims[name] != value:
            raise CertificateError(f"false tail scalarization claim: {name}")
    return {
        "generalized_trace": str(trace),
        "generalized_determinant": str(determinant),
        "spectral_discriminant": str(discriminant),
        "best_scalar": str(trace / 2),
        "optimal_relative_remainder_squared": str(relative_square),
    }


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    logical = payload.get("logical_gates")
    if not isinstance(logical, dict) or not logical:
        raise CertificateError("logical_gates must be a nonempty object")
    blocking = [name for name, value in logical.items() if value is not True]
    if blocking:
        raise CertificateError("blocking logical gates: " + ", ".join(blocking))

    result = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_OPERATOR_AUDIT",
        "affine_falsifiers": verify_affine(payload.get("affine_falsifier", {})),
        "sector_gap": verify_sector(payload.get("sector_gap", {})),
        "radical_tail": verify_radical(payload.get("radical_tail", {})),
        "tail_scalarization": verify_scalarization(
            payload.get("tail_scalarization", {})
        ),
        "proof_boundary": (
            "Exact finite rational algebra only. No CCM matrix, prolate asymptotic, "
            "Weil primitive, or Riemann-xi value is evaluated."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


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
