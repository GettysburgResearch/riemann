#!/usr/bin/env python3
"""Exact rational checker for the L-2813 target phase-grid remainder."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.phase-grid-remainder.v1"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    num = exact_int(raw.get("numerator"), f"{name}.numerator")
    den = exact_int(raw.get("denominator"), f"{name}.denominator")
    if den <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(num, den)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")

    cutoff = exact_int(data.get("cutoff"), "cutoff")
    cells = exact_int(data.get("cells"), "cells")
    grid_size = exact_int(data.get("grid_size"), "grid_size")
    order = exact_int(data.get("taylor_order"), "taylor_order")
    if cutoff != 100_000_000_000 or cells != 1024:
        raise CertificateError("certificate is not the reviewed target")
    if grid_size < 2 or order < 0:
        raise CertificateError("invalid grid or Taylor order")

    expected_vector = "3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297"
    expected_normalization = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
    if data.get("vector_sha256") != expected_vector:
        raise CertificateError("vector fingerprint mismatch")
    if data.get("normalization_sha256") != expected_normalization:
        raise CertificateError("normalization fingerprint mismatch")

    norm_upper = rational(data.get("norm_upper"), "norm_upper")
    pi_lower = rational(data.get("pi_lower"), "pi_lower")
    pi_upper = rational(data.get("pi_upper"), "pi_upper")
    log_cutoff_upper = rational(data.get("log_cutoff_upper"), "log_cutoff_upper")
    sqrt_cutoff_upper = rational(data.get("sqrt_cutoff_upper"), "sqrt_cutoff_upper")
    eta_ceiling = rational(data.get("eta_ceiling"), "eta_ceiling")
    weight_ceiling = rational(data.get("weight_ceiling"), "weight_ceiling")
    target_radius = rational(data.get("target_radius"), "target_radius")

    if not (0 < pi_lower < pi_upper < 4):
        raise CertificateError("invalid pi bounds")
    if norm_upper <= 0 or log_cutoff_upper <= 0 or sqrt_cutoff_upper <= 0:
        raise CertificateError("positive parameter bounds required")
    if not (0 < eta_ceiling < 1):
        raise CertificateError("eta ceiling must lie in (0,1)")
    if target_radius <= 0:
        raise CertificateError("target radius must be positive")

    # W <= (N/pi) * 2 log(c) sqrt(c).
    derived_weight = (
        norm_upper
        * 2
        * log_cutoff_upper
        * sqrt_cutoff_upper
        / pi_lower
    )
    if derived_weight >= weight_ceiling:
        raise CertificateError("declared weight ceiling is not strict")

    eta_from_grid = pi_upper / grid_size
    if eta_from_grid >= eta_ceiling:
        raise CertificateError("grid does not imply the declared eta ceiling")

    # e^eta <= 1/(1-eta), using the declared rational ceiling.
    exp_upper = 1 / (1 - eta_ceiling)
    remainder = (
        weight_ceiling
        * exp_upper
        * eta_ceiling ** (order + 1)
        / _factorial(order + 1)
    )
    if remainder >= target_radius:
        raise CertificateError("Taylor remainder does not clear the target radius")

    # Also expose the tighter direct rational bound from pi_upper/M.
    tighter_exp = 1 / (1 - eta_from_grid)
    tighter_remainder = (
        derived_weight
        * tighter_exp
        * eta_from_grid ** (order + 1)
        / _factorial(order + 1)
    )

    return {
        "schema": SCHEMA,
        "verified": True,
        "cutoff": cutoff,
        "cells": cells,
        "grid_size": grid_size,
        "taylor_order": order,
        "vector_sha256": expected_vector,
        "normalization_sha256": expected_normalization,
        "derived_weight_upper": fj(derived_weight),
        "declared_weight_ceiling": fj(weight_ceiling),
        "eta_from_grid_upper": fj(eta_from_grid),
        "declared_eta_ceiling": fj(eta_ceiling),
        "coarse_remainder_upper": fj(remainder),
        "tighter_remainder_upper": fj(tighter_remainder),
        "target_radius": fj(target_radius),
        "strictly_below_target_radius": True,
    }


def _factorial(n: int) -> int:
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
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
