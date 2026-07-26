#!/usr/bin/env python3
"""Independently reconstruct b0 from one point difference and old moments."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x9309_kernel", ROOT / "verify_zero_anchor.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load X-9309 kernel")
K = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K
SPEC.loader.exec_module(K)


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        output[i] += value
    for i, value in enumerate(right):
        output[i] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return output


def response_polynomial(nodes: list[Fraction], beta: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        output = polynomial_add(output, [-coefficient * value for value in term])
    return output


def interval_json(value: K.RationalInterval) -> dict[str, dict[str, str]]:
    return {
        "lower": K.fraction_json(value.lower),
        "upper": K.fraction_json(value.upper),
    }


def decimal_interval(raw: Any, name: str) -> K.RationalInterval:
    if not isinstance(raw, dict):
        raise K.CertificateError(f"{name} must be an object")
    try:
        return K.RationalInterval(Fraction(raw["lower"]), Fraction(raw["upper"]))
    except (KeyError, ValueError, ZeroDivisionError) as exc:
        raise K.CertificateError(f"bad decimal interval at {name}") from exc


def verify(
    old_certificate_path: Path,
    old_basis_path: Path,
    zero_high_path: Path,
    direct_verdict_path: Path,
    log_terms: int,
) -> dict[str, Any]:
    certificate = K.load_json(old_certificate_path)
    basis_data, moments = K.load_basis(old_basis_path)
    zero = K.load_json(zero_high_path)
    direct = K.load_json(direct_verdict_path)

    if direct.get("schema") != K.OUTPUT_SCHEMA:
        raise K.CertificateError("unsupported direct verdict schema")
    if direct.get("old_basis_sha256") != K.file_sha256(old_basis_path):
        raise K.CertificateError("direct verdict old-basis binding mismatch")
    if direct.get("zero_high_sha256") != K.file_sha256(zero_high_path):
        raise K.CertificateError("direct verdict zero-primitive binding mismatch")
    if certificate.get("ordinate") != zero.get("ordinate"):
        raise K.CertificateError("ordinate mismatch")
    if basis_data.get("primitive_sha256") != certificate.get("source", {}).get("primitive_sha256"):
        raise K.CertificateError("old primitive digest mismatch")

    points = sorted(
        certificate.get("points", []),
        key=lambda point: K.fraction(point.get("u"), "point.u"),
    )
    if len(points) != 16:
        raise K.CertificateError("expected sixteen old points")
    nodes = [K.fraction(point.get("u"), "point.u") for point in points]
    if nodes[0] != Fraction(1, 2**40):
        raise K.CertificateError("unexpected nearest old node")

    shells = K.deflation_shells(certificate)
    log = K.ExactLogEncloser(log_terms)
    f_zero = K.residual_interval(K.zero_point(zero, "zero primitive"), Fraction(0), shells, log)
    f_reference = K.residual_interval(points[0], nodes[0], shells, log)

    full_beta = K.basis_vector([Fraction(0)] + nodes, 0)
    beta_zero = full_beta[0]
    delta = full_beta[1:]
    delta[0] += beta_zero
    if sum(delta) != 0:
        raise K.CertificateError("reduced coefficient vector is not zero sum")
    polynomial = response_polynomial(nodes, delta)
    if len(polynomial) != 15:
        raise K.CertificateError("reduced response polynomial degree mismatch")

    reduced = f_zero.sub(f_reference).scale(beta_zero)
    for coefficient, moment in zip(polynomial, moments):
        reduced = reduced.add(moment.scale(coefficient))

    direct_interval = decimal_interval(direct.get("b0_interval"), "direct.b0_interval")
    intersection = K.RationalInterval(
        max(reduced.lower, direct_interval.lower),
        min(reduced.upper, direct_interval.upper),
    )
    if intersection.lower > intersection.upper:
        raise K.CertificateError("direct and reduced b0 intervals do not overlap")

    width_budget = sum(
        abs(coefficient) * (moment.upper - moment.lower)
        for coefficient, moment in zip(polynomial, moments)
    )
    return {
        "schema": "riemann.x9309-zero-anchor-reduced-overlap.v1",
        "analytic_claim": "L-9313",
        "reference_node": K.fraction_json(nodes[0]),
        "beta_zero": K.fraction_json(beta_zero),
        "polynomial_coefficients": [K.fraction_json(value) for value in polynomial],
        "old_moment_width_budget": K.fraction_json(width_budget),
        "old_moment_width_budget_decimal": K.decimal_string(width_budget),
        "direct_b0_interval": interval_json(direct_interval),
        "reduced_b0_interval": interval_json(reduced),
        "intersection_b0_interval": interval_json(intersection),
        "intersection_width_decimal": K.decimal_string(intersection.upper - intersection.lower),
        "direct_verdict": direct.get("verdict"),
        "verified_overlap": True,
        "proof_boundary": (
            "Exact rational point-difference and old-moment contraction. The overlap gate is an "
            "algebraic implementation cross-check, not an independence assumption."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-certificate", type=Path, required=True)
    parser.add_argument("--old-basis", type=Path, required=True)
    parser.add_argument("--zero-high", type=Path, required=True)
    parser.add_argument("--direct-verdict", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=240)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(
            args.old_certificate,
            args.old_basis,
            args.zero_high,
            args.direct_verdict,
            args.log_terms,
        )
    except (OSError, K.CertificateError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
