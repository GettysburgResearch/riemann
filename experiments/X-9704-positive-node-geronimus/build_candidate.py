#!/usr/bin/env python3
"""Build X-9704 one-point Schur certificates from a frozen old response table."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASE_PATH = ROOT / "X-9302-total-count-zero-deflation" / "verify_total_count_deflation.py"


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


BASE = load_module("verify_total_count_deflation_x9704", BASE_PATH)
CHECK = load_module("verify_x9704", HERE / "verify.py")

PRIMITIVE_SCHEMA = "riemann.x9704-positive-node-primitives.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class BuildError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BuildError(f"{path} must contain a JSON object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BuildError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as error:
            raise BuildError(f"{name} must be integer text") from error
    raise BuildError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BuildError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Any) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def decimal_fraction(text: Any, name: str) -> Fraction:
    if not isinstance(text, str):
        raise BuildError(f"{name} must be finite decimal text")
    try:
        return Fraction(Decimal(text))
    except Exception as error:
        raise BuildError(f"{name} is not finite decimal text") from error


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    output = [
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * coefficient for coefficient in poly]


def divide_by_y_plus_a(poly: list[Fraction], a: Fraction) -> list[Fraction]:
    if len(poly) < 2:
        raise BuildError("cannot divide a constant polynomial")
    degree = len(poly) - 1
    quotient = [Fraction(0)] * degree
    quotient[-1] = poly[-1]
    for k in range(degree - 1, 0, -1):
        quotient[k - 1] = poly[k] - a * quotient[k]
    remainder = poly[0] - a * quotient[0]
    if remainder != 0:
        raise BuildError("claimed polynomial division has nonzero remainder")
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def parse_basis(basis: dict[str, Any]) -> list[Any]:
    rows = basis.get("basis_rows")
    if not isinstance(rows, list) or len(rows) < 3 or len(rows) % 2 != 1:
        raise BuildError("basis_rows must have odd length at least three")
    rows = sorted(rows, key=lambda row: integer(row.get("degree"), "basis degree"))
    if [integer(row.get("degree"), "basis degree") for row in rows] != list(
        range(len(rows))
    ):
        raise BuildError("basis degrees are not contiguous from zero")
    output = []
    for index, row in enumerate(rows):
        lower = decimal_fraction(
            row.get("lower_exact_decimal"), f"basis_rows[{index}].lower"
        )
        upper = decimal_fraction(
            row.get("upper_exact_decimal"), f"basis_rows[{index}].upper"
        )
        output.append(BASE.Interval(lower, upper))
    return output


def deflated_value(point: dict[str, Any], shells: list[dict[str, Any]], terms: int) -> Any:
    value = BASE.log_positive_interval(point["h"], terms)
    u = point["u"]
    for shell in shells:
        value = value.sub(
            BASE.log_positive_fraction(u + shell["B"], terms).scale(
                Fraction(shell["count"])
            )
        )
    return value


def parse_new_point(primitives: dict[str, Any], point_id: str) -> dict[str, Any]:
    raw_points = primitives.get("points")
    if not isinstance(raw_points, list):
        raise BuildError("new primitive points must be an array")
    matches = [point for point in raw_points if point.get("id") == point_id]
    if len(matches) != 1:
        raise BuildError(f"expected exactly one new primitive point {point_id!r}")
    raw = matches[0]
    x = rational(raw.get("x"), f"{point_id}.x")
    u = rational(raw.get("u"), f"{point_id}.u")
    if x <= 0 or u != x * x:
        raise BuildError("new primitive x/u identity failed")
    rectangle = raw.get("xi_rectangle")
    if not isinstance(rectangle, dict):
        raise BuildError("new primitive xi_rectangle missing")
    real = BASE.interval(rectangle.get("real"), f"{point_id}.real")
    imag = BASE.interval(rectangle.get("imag"), f"{point_id}.imag")
    if raw.get("functional_equation_residual_contains_zero") is not True:
        raise BuildError("new primitive functional-equation gate failed")
    return {"id": point_id, "x": x, "u": u, "h": BASE.modulus_squared(real, imag)}


def build(
    old_certificate: dict[str, Any],
    basis: dict[str, Any],
    primitives: dict[str, Any],
    *,
    point_id: str,
    reference_id: str,
    delta0: Fraction,
    delta1: Fraction,
    log_terms: int,
) -> dict[str, Any]:
    if (
        old_certificate.get("classification") != CHECK.PRODUCTION
        or old_certificate.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("old certificate is not a production direct-xi table")
    try:
        old_verification = BASE.verify(old_certificate)
    except Exception as error:
        raise BuildError(f"old certificate verification failed: {error}") from error

    if (
        primitives.get("schema") != PRIMITIVE_SCHEMA
        or primitives.get("classification") != CHECK.PRODUCTION
        or primitives.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("new primitive schema/classification/normalization mismatch")
    if old_certificate.get("ordinate") != primitives.get("ordinate"):
        raise BuildError("old and new primitive ordinates differ")
    old_scale = integer(
        old_certificate.get("common_xi_scale_power_of_two", 0), "old scale"
    )
    new_scale = integer(
        primitives.get("common_xi_scale_power_of_two", 0), "new scale"
    )
    if old_scale != new_scale:
        raise BuildError("common xi scales differ")

    source = old_certificate.get("source")
    if not isinstance(source, dict):
        raise BuildError("old certificate source metadata missing")
    if basis.get("primitive_sha256") != source.get("primitive_sha256"):
        raise BuildError("basis and old certificate primitive digests differ")
    if basis.get("total_count_sha256") != source.get("total_count_sha256"):
        raise BuildError("basis and old certificate count digests differ")
    if basis.get("ordinate") != old_certificate.get("ordinate"):
        raise BuildError("basis and old certificate ordinates differ")

    terms = integer(log_terms, "log_terms")
    if terms < 32 or terms > 4096:
        raise BuildError("log_terms must lie in [32,4096]")
    moments = parse_basis(basis)
    old_points = BASE.parse_points(old_certificate)
    if reference_id not in old_points:
        raise BuildError("reference point is absent from old table")
    _, shells = BASE.parse_count_windows(old_certificate, CHECK.PRODUCTION)
    new_point = parse_new_point(primitives, point_id)

    old_nodes = [
        point["u"]
        for _, point in sorted(old_points.items(), key=lambda item: item[1]["u"])
    ]
    w = new_point["u"]
    if w in old_nodes:
        raise BuildError("new node duplicates an old node")

    polynomial = [Fraction(1)]
    for node in old_nodes:
        polynomial = poly_mul(polynomial, [node, Fraction(1)])
    d_minus_w = Fraction(1)
    for node in old_nodes:
        d_minus_w *= node - w
    beta_w = -Fraction(1) / d_minus_w

    p_gamma = divide_by_y_plus_a(
        poly_add([Fraction(1)], poly_scale(polynomial, beta_w)), w
    )
    reference_u = old_points[reference_id]["u"]
    p_reference = poly_add(
        p_gamma,
        poly_scale(divide_by_y_plus_a(polynomial, reference_u), -beta_w),
    )
    if len(p_reference) > len(moments):
        raise BuildError("reduced polynomial exceeds old moment degree")

    f_new = deflated_value(new_point, shells, terms)
    f_reference = deflated_value(old_points[reference_id], shells, terms)
    b0 = f_new.sub(f_reference).scale(beta_w)
    for index, coefficient in enumerate(p_reference):
        b0 = b0.add(moments[index].scale(coefficient))

    output = {
        "schema": CHECK.SCHEMA,
        "classification": CHECK.PRODUCTION,
        "normalization_id": NORMALIZATION,
        "w": fj(w),
        "old_moments": [ij(value) for value in moments],
        "b0_interval": ij(b0),
        "delta0": fj(delta0),
        "delta1": fj(delta1),
        "source_gate": {
            "status": CHECK.PRODUCTION_GATE,
            "old_basis_sha256": canonical_sha(basis),
            "old_primitive_sha256": source["primitive_sha256"],
            "count_profile_sha256": source["total_count_sha256"],
            "new_primitive_sha256": canonical_sha(primitives),
        },
        "source": {
            "old_parent_verdict": old_verification["verdict"],
            "old_certificate_sha256": old_certificate.get("certificate_sha256"),
            "new_primitive_certificate_sha256": primitives.get("certificate_sha256"),
            "point_id": point_id,
            "reference_id": reference_id,
            "x": fj(new_point["x"]),
            "beta_w": fj(beta_w),
            "reduced_polynomial_coefficients": [fj(value) for value in p_reference],
            "log_terms": terms,
            "common_xi_scale_power_of_two": old_scale,
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old_certificate", type=Path)
    parser.add_argument("old_basis", type=Path)
    parser.add_argument("new_primitives", type=Path)
    parser.add_argument("--point-id", required=True)
    parser.add_argument("--reference-id", default="x-5")
    parser.add_argument("--delta0", required=True)
    parser.add_argument("--delta1", required=True)
    parser.add_argument("--log-terms", type=int, default=240)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(
            load(args.old_certificate),
            load(args.old_basis),
            load(args.new_primitives),
            point_id=args.point_id,
            reference_id=args.reference_id,
            delta0=Fraction(args.delta0),
            delta1=Fraction(args.delta1),
            log_terms=args.log_terms,
        )
        verification = CHECK.verify(result)
    except (
        OSError,
        json.JSONDecodeError,
        BuildError,
        CHECK.CertificateError,
        ZeroDivisionError,
    ) as error:
        print(json.dumps({"built": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    result["initial_verification"] = {
        "verdict": verification["verdict"],
        "negative_rows": len(verification["negative_rows"]),
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "point_id": args.point_id,
                "w": result["w"],
                "b0_interval": result["b0_interval"],
                "verdict": verification["verdict"],
                "certificate_sha256": result["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 1 if verification["verdict"] == "UNRESOLVED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
