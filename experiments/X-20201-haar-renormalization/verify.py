#!/usr/bin/env python3
"""Exact algebra regression for the proposed Haar-renormalization RH criteria.

This checker evaluates no zeta, xi, zero, prime, or transcendental quantity. It
verifies the finite algebra used by T-20201/L-20201/T-20202 using integers and
fractions.Fraction only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20201-haar-renormalization.v1"
RESULT_SCHEMA = "riemann.x20201-haar-renormalization.verification.v1"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rat(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    n = exact_int(raw.get("numerator"), f"{name}.numerator")
    d = exact_int(raw.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(value: Fraction) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def ldl_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
    for j in range(n):
        pivot = matrix[j][j] - sum(
            (lower[j][k] * lower[j][k] * pivots[k] for k in range(j)),
            Fraction(0),
        )
        if pivot <= 0:
            raise CertificateError(f"Hankel LDL pivot {j} is not positive")
        pivots.append(pivot)
        for i in range(j + 1, n):
            lower[i][j] = (
                matrix[i][j]
                - sum(
                    (lower[i][k] * lower[j][k] * pivots[k] for k in range(j)),
                    Fraction(0),
                )
            ) / pivot
    return pivots


def require_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty list")
    return value


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("classification") != "SYNTHETIC_ALGEBRA":
        raise CertificateError("classification must be SYNTHETIC_ALGEBRA")

    spectral_rows = []
    for i, row in enumerate(require_list(data.get("cosine_samples"), "cosine_samples")):
        if not isinstance(row, dict):
            raise CertificateError(f"cosine_samples[{i}] must be an object")
        c = rat(row.get("cosine"), f"cosine_samples[{i}].cosine")
        if not -1 <= c <= 1:
            raise CertificateError("cosine sample must lie in [-1,1]")
        psi_t = 2 * (1 - c)
        cos_2 = 2 * c * c - 1
        psi_2t = 2 * (1 - cos_2)
        defect = 4 * psi_t - psi_2t
        square = 4 * (1 - c) ** 2
        if defect != square or defect < 0:
            raise CertificateError("spectral square identity failed")
        claimed = rat(row.get("claimed_defect"), f"cosine_samples[{i}].claimed_defect")
        if claimed != defect:
            raise CertificateError("claimed spectral defect mismatch")
        spectral_rows.append({"cosine": fj(c), "defect": fj(defect)})

    finite = data.get("finite_node")
    if not isinstance(finite, dict):
        raise CertificateError("finite_node must be an object")
    psi_t = rat(finite.get("psi_t"), "finite_node.psi_t")
    psi_2t = rat(finite.get("psi_2t"), "finite_node.psi_2t")
    defect = 4 * psi_t - psi_2t
    screw_quadratic = 2 * defect
    if rat(finite.get("claimed_screw_quadratic"), "finite_node.claimed_screw_quadratic") != screw_quadratic:
        raise CertificateError("finite-node Haar identity failed")

    cocycle = data.get("cocycle")
    if not isinstance(cocycle, dict):
        raise CertificateError("cocycle must be an object")
    p1 = rat(cocycle.get("psi_t"), "cocycle.psi_t")
    p2 = rat(cocycle.get("psi_2t"), "cocycle.psi_2t")
    p4 = rat(cocycle.get("psi_4t"), "cocycle.psi_4t")
    d2_t = 4 * p1 - p2
    d2_2t = 4 * p2 - p4
    d4_t = 16 * p1 - p4
    if d4_t != 4 * d2_t + d2_2t:
        raise CertificateError("dilation cocycle failed")
    if rat(cocycle.get("claimed_d4"), "cocycle.claimed_d4") != d4_t:
        raise CertificateError("claimed cocycle value mismatch")

    pole = data.get("pole_square")
    if not isinstance(pole, dict):
        raise CertificateError("pole_square must be an object")
    a = rat(pole.get("a"), "pole_square.a")
    if a <= 0:
        raise CertificateError("pole a must be positive")
    direct_pole = 16 * (a + 1 / a - 2) - 4 * (a * a + 1 / (a * a) - 2)
    square_pole = -4 * (a + 1 / a - 2) ** 2
    if direct_pole != square_pole:
        raise CertificateError("pole square identity failed")
    if rat(pole.get("claimed_value"), "pole_square.claimed_value") != direct_pole:
        raise CertificateError("claimed pole value mismatch")

    lerch_rows = []
    for i, row in enumerate(require_list(data.get("lerch_samples"), "lerch_samples")):
        if not isinstance(row, dict):
            raise CertificateError(f"lerch_samples[{i}] must be an object")
        y = rat(row.get("y"), f"lerch_samples[{i}].y")
        if not 0 <= y <= 1:
            raise CertificateError("Lerch y must lie in [0,1]")
        left = Fraction(3, 4) - y + y * y / 4
        right = (1 - y) * (3 - y) / 4
        if left != right or left < 0:
            raise CertificateError("positive Lerch factorization failed")
        claimed = rat(row.get("claimed_value"), f"lerch_samples[{i}].claimed_value")
        if claimed != left:
            raise CertificateError("claimed Lerch value mismatch")
        lerch_rows.append({"y": fj(y), "value": fj(left)})

    moment = data.get("moment_model")
    if not isinstance(moment, dict):
        raise CertificateError("moment_model must be an object")
    order = exact_int(moment.get("order"), "moment_model.order")
    if order < 0 or order > 8:
        raise CertificateError("moment order must lie in [0,8]")
    atoms = []
    for i, row in enumerate(require_list(moment.get("atoms"), "moment_model.atoms")):
        if not isinstance(row, dict):
            raise CertificateError(f"moment_model.atoms[{i}] must be an object")
        t = rat(row.get("t"), f"moment_model.atoms[{i}].t")
        w = rat(row.get("weight"), f"moment_model.atoms[{i}].weight")
        if t < 0 or w <= 0:
            raise CertificateError("moment atoms require t>=0 and weight>0")
        atoms.append((t, w))
    if len({t for t, _ in atoms}) < order + 1:
        raise CertificateError("not enough distinct atoms for strict Hankel controls")
    moments = [
        sum((w * t**k for t, w in atoms), Fraction(0))
        for k in range(2 * order + 2)
    ]
    h0 = [[moments[i + j] for j in range(order + 1)] for i in range(order + 1)]
    h1 = [[moments[i + j + 1] for j in range(order + 1)] for i in range(order + 1)]
    p0 = ldl_pivots(h0)
    p1s = ldl_pivots(h1)

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "verified": True,
        "classification": "SYNTHETIC_ALGEBRA",
        "spectral_square_rows": spectral_rows,
        "finite_node": {
            "defect": fj(defect),
            "screw_quadratic": fj(screw_quadratic),
        },
        "cocycle": {
            "d2_t": fj(d2_t),
            "d2_2t": fj(d2_2t),
            "d4_t": fj(d4_t),
        },
        "pole_square_value": fj(direct_pole),
        "lerch_rows": lerch_rows,
        "moment_model": {
            "moments": [fj(x) for x in moments],
            "h0_pivots": [fj(x) for x in p0],
            "h1_pivots": [fj(x) for x in p1s],
        },
        "verdict": "EXACT_HAAR_RENORMALIZATION_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Synthetic exact algebra only. This checker does not verify the zeta screw "
            "identity, Landau transfer, prime formula, all-order Hankel positivity, or RH."
        ),
    }
    result["proof_object_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        result = {"schema": RESULT_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
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
