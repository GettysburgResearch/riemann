#!/usr/bin/env python3
"""Exact checker for the scalar signed-edge Barta mean obstruction."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15402-scalar-barta-obstruction.synthetic.v1"


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
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def parse_vector(raw: Any, n: int, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or len(raw) != n:
        raise CertificateError(f"{name} must be an array of length {n}")
    return [frac(item, f"{name}[{index}]") for index, item in enumerate(raw)]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    n = integer(data.get("vertex_count"), "vertex_count")
    if n < 2:
        raise CertificateError("vertex_count must be at least two")

    potential = parse_vector(data.get("potential"), n, "potential")
    psi = parse_vector(data.get("psi"), n, "psi")
    if any(value <= 0 for value in psi):
        raise CertificateError("psi must be strictly positive")

    barta = list(potential)
    exact_defect = Fraction(0)
    edge_signs: list[int] = []
    seen: set[tuple[int, int]] = set()

    raw_edges = data.get("jump_edges")
    if not isinstance(raw_edges, list):
        raise CertificateError("jump_edges must be an array")

    for index, raw in enumerate(raw_edges):
        if not isinstance(raw, dict):
            raise CertificateError(f"jump_edges[{index}] must be an object")
        i = integer(raw.get("i"), f"jump_edges[{index}].i")
        j = integer(raw.get("j"), f"jump_edges[{index}].j")
        if not (0 <= i < j < n) or (i, j) in seen:
            raise CertificateError("edges must be unique with 0 <= i < j < n")
        seen.add((i, j))

        weight = frac(raw.get("weight"), f"jump_edges[{index}].weight")
        if weight <= 0:
            raise CertificateError("edge weights must be positive")
        sign = integer(raw.get("sign"), f"jump_edges[{index}].sign")
        if sign not in (-1, 1):
            raise CertificateError("edge sign must be +1 or -1")
        edge_signs.append(sign)

        # The scalar local Barta residual is independent of the edge sign.
        barta[i] += weight * (psi[i] - psi[j]) / psi[i]
        barta[j] += weight * (psi[j] - psi[i]) / psi[j]
        exact_defect -= weight * (psi[i] - psi[j]) ** 2 / (psi[i] * psi[j])

    potential_sum = sum(potential)
    barta_sum = sum(barta)
    if barta_sum != potential_sum + exact_defect:
        raise CertificateError("mean-obstruction identity failed")
    if exact_defect > 0:
        raise CertificateError("edge defect must be nonpositive")

    barta_floor = min(barta)
    barta_mean = barta_sum / n
    potential_mean = potential_sum / n
    if barta_floor > barta_mean or barta_mean > potential_mean:
        raise CertificateError("floor/mean obstruction ordering failed")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    checks = {
        "barta_floor": barta_floor,
        "barta_mean": barta_mean,
        "potential_mean": potential_mean,
        "edge_defect_sum": exact_defect,
    }
    for name, actual in checks.items():
        if frac(claimed.get(name), f"claimed.{name}") != actual:
            raise CertificateError(f"claimed {name} mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_SCALAR_BARTA_MEAN_OBSTRUCTION",
        "edge_signs": edge_signs,
        "barta_values": [fj(value) for value in barta],
        "barta_floor": fj(barta_floor),
        "barta_mean": fj(barta_mean),
        "potential_mean": fj(potential_mean),
        "edge_defect_sum": fj(exact_defect),
        "identity": "sum(barta)=sum(potential)+edge_defect_sum",
        "ordering": "barta_floor <= barta_mean <= potential_mean",
        "proof_boundary": "finite rational signed graph regression only",
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
