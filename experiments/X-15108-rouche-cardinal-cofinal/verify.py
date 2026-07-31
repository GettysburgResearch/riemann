#!/usr/bin/env python3
"""Exact rational consumer for the Rouché--cardinal finite gate."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.rouche-cardinal-finite-gate.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("Boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("Boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("Malformed rational")
        return Fraction(n, d)
    raise ValueError(f"Unsupported rational: {x!r}")


def dump_rat(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("Wrong schema")

    h = rat(data["physical_node_spacing"])
    xi_boundary = [rat(x) for x in data["xi_boundary_lower"]]
    boundary_error = [rat(x) for x in data["transform_boundary_error_upper"]]
    derivative = [rat(x) for x in data["xi_derivative_lower"]]
    real_error = [rat(x) for x in data["transform_real_error_upper"]]
    mass_lower = [rat(x) for x in data["phase_mass_lower"]]
    mass_upper = [rat(x) for x in data["phase_mass_upper"]]
    residual = [rat(x) for x in data["residual_residue_upper"]]
    bmat = [[rat(x) for x in row] for row in data["cardinal_derivative_upper"]]

    n = len(xi_boundary)
    vectors = [boundary_error, derivative, real_error, mass_lower, mass_upper, residual]
    if n == 0 or any(len(v) != n for v in vectors):
        raise ValueError("Vector dimension mismatch")
    if len(bmat) != n or any(len(row) != n for row in bmat):
        raise ValueError("Derivative matrix dimension mismatch")
    if h <= 0:
        raise ValueError("Node spacing must be positive")

    deltas = []
    rouche_slacks = []
    for k in range(n):
        if xi_boundary[k] <= 0 or derivative[k] <= 0:
            raise ValueError("Xi moat and derivative floor must be positive")
        if boundary_error[k] < 0 or real_error[k] < 0:
            raise ValueError("Transform errors must be nonnegative")
        if boundary_error[k] >= xi_boundary[k]:
            raise ValueError(f"Rouche boundary gate failed at {k}")
        if mass_lower[k] <= 0 or mass_upper[k] < mass_lower[k]:
            raise ValueError("Invalid phase mass interval")
        if residual[k] < 0:
            raise ValueError("Residual radius must be nonnegative")
        if any(x < 0 for x in bmat[k]):
            raise ValueError("Derivative upper bounds must be nonnegative")
        rouche_slacks.append(xi_boundary[k] - boundary_error[k])
        deltas.append(real_error[k] / (h * derivative[k]))

    margins = []
    normalized_losses = []
    for k in range(n):
        loss = mass_upper[k] * bmat[k][k] * deltas[k] + residual[k]
        for ell in range(n):
            if ell != k:
                loss += mass_upper[ell] * bmat[k][ell] * deltas[ell]
        margin = mass_lower[k] - loss
        if margin <= 0:
            raise ValueError(f"Cardinal residue margin failed at {k}: {margin}")
        margins.append(margin)
        normalized_losses.append(loss / mass_lower[k])

    canonical_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    return {
        "status": "CERTIFIED_ROUCHE_CARDINAL_ARITHMETIC_COMPLETION",
        "rouche_slacks": [dump_rat(x) for x in rouche_slacks],
        "node_displacement_upper": [dump_rat(x) for x in deltas],
        "residue_margin_lower": [dump_rat(x) for x in margins],
        "normalized_loss_upper": [dump_rat(x) for x in normalized_losses],
        "maximum_normalized_loss_upper": dump_rat(max(normalized_losses)),
        "boundary_scalar": 0,
        "certificate_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
