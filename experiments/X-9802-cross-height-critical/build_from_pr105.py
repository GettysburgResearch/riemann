#!/usr/bin/env python3
"""Bind PR #105 center/upper direct-xi tables to an X-9802 response candidate."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x9802_verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
CANDIDATE_SCHEMA = "riemann.x9802-critical-candidate.v1"


class BuildError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BuildError(f"{path} must contain a JSON object")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BuildError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise BuildError(f"{name} must be integer text") from exc
    raise BuildError(f"{name} must be an integer")


def rational(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise BuildError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BuildError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def parse_interval(value: Any, name: str) -> VERIFY.Interval:
    if not isinstance(value, dict):
        raise BuildError(f"{name} must be an object")
    return VERIFY.Interval(
        rational(value.get("lower"), f"{name}.lower"),
        rational(value.get("upper"), f"{name}.upper"),
    )


def square_interval(value: VERIFY.Interval) -> VERIFY.Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    lower = (
        Fraction(0)
        if value.lower <= 0 <= value.upper
        else min(value.lower * value.lower, value.upper * value.upper)
    )
    return VERIFY.Interval(lower, upper)


def modulus_squared(rectangle: Any, name: str) -> VERIFY.Interval:
    if not isinstance(rectangle, dict):
        raise BuildError(f"{name} must be an object")
    real = square_interval(parse_interval(rectangle.get("real"), f"{name}.real"))
    imag = square_interval(parse_interval(rectangle.get("imag"), f"{name}.imag"))
    return VERIFY.Interval(real.lower + imag.lower, real.upper + imag.upper)


def parse_primitive(
    data: dict[str, Any],
    path: Path,
    expected_ordinate: Fraction,
    point_ids: list[str],
) -> dict[str, Any]:
    if (
        data.get("schema") != PRIMITIVE_SCHEMA
        or data.get("normalization_id") != VERIFY.NORMALIZATION
    ):
        raise BuildError(f"{path} has the wrong primitive schema/normalization")
    ordinate = rational(data.get("ordinate"), f"{path}.ordinate")
    if ordinate != expected_ordinate:
        raise BuildError(f"{path} ordinate mismatch")
    raw_points = data.get("points")
    if not isinstance(raw_points, list):
        raise BuildError(f"{path} points missing")
    by_id = {point.get("id"): point for point in raw_points if isinstance(point, dict)}
    points = []
    for point_id in point_ids:
        point = by_id.get(point_id)
        if point is None:
            raise BuildError(f"{path} misses required point {point_id}")
        x = rational(point.get("x"), f"{path}.{point_id}.x")
        if x <= 0:
            raise BuildError("horizontal offsets must be positive")
        if point.get("functional_equation_residual_contains_zero") is not True:
            raise BuildError(f"functional-equation gate failed at {path}:{point_id}")
        h_value = modulus_squared(
            point.get("xi_rectangle"), f"{path}.{point_id}.xi_rectangle"
        )
        if h_value.lower <= 0:
            raise BuildError(f"squared-modulus interval touches zero at {point_id}")
        points.append(
            {"id": point_id, "u": fj(x * x), "h_interval": VERIFY.ij(h_value)}
        )
    return {
        "ordinate": ordinate,
        "scale": integer(
            data.get("common_xi_scale_power_of_two", 0),
            f"{path}.common_xi_scale_power_of_two",
        ),
        "points": points,
    }


def build(center_path: Path, plus_path: Path, candidate_path: Path) -> dict[str, Any]:
    candidate = load(candidate_path)
    if (
        candidate.get("schema") != CANDIDATE_SCHEMA
        or candidate.get("normalization_id") != VERIFY.NORMALIZATION
    ):
        raise BuildError("candidate schema/normalization mismatch")
    origin = rational(candidate.get("origin"), "candidate.origin")
    raw_heights = candidate.get("heights")
    point_ids = candidate.get("point_ids")
    if not isinstance(raw_heights, list) or not isinstance(point_ids, list):
        raise BuildError("candidate heights or point IDs missing")
    expected = {
        str(item.get("id")): rational(item.get("ordinate"), "candidate height ordinate")
        for item in raw_heights
        if isinstance(item, dict)
    }
    if set(expected) != {"center", "plus"}:
        raise BuildError("sharp candidate must declare center and plus heights")
    point_ids = [str(value) for value in point_ids]
    paths = {"center": center_path, "plus": plus_path}
    parsed = {
        identifier: parse_primitive(
            load(paths[identifier]), paths[identifier], expected[identifier], point_ids
        )
        for identifier in ("center", "plus")
    }
    heights = [
        {
            "id": identifier,
            "ordinate": fj(parsed[identifier]["ordinate"]),
            "common_xi_scale_power_of_two": parsed[identifier]["scale"],
            "source_sha256": sha256_file(paths[identifier]),
            "points": parsed[identifier]["points"],
        }
        for identifier in ("center", "plus")
    ]
    output: dict[str, Any] = {
        "schema": VERIFY.SCHEMA,
        "classification": VERIFY.PRODUCTION,
        "normalization_id": VERIFY.NORMALIZATION,
        "origin": fj(origin),
        "candidate_id": candidate.get("id"),
        "heights": heights,
        "terms": candidate.get("terms"),
        "critical_certificate": candidate.get("critical_certificate"),
        "source": {
            "candidate_sha256": sha256_file(candidate_path),
            "candidate_classification": candidate.get("classification"),
        },
    }
    verification = VERIFY.verify(output)
    output["initial_verification"] = {
        "verdict": verification["verdict"],
        "finite_status": verification["finite_status"],
        "portfolio_interval": verification["portfolio_interval"],
        "response_proof_object_sha256": verification["response_certificate"][
            "proof_object_sha256"
        ],
    }
    output["certificate_sha256"] = VERIFY.canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center", type=Path, required=True)
    parser.add_argument("--plus", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = build(args.center, args.plus, args.candidate)
    except (OSError, json.JSONDecodeError, BuildError, VERIFY.CertificateError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "candidate_id": output.get("candidate_id"),
                "finite_status": output["initial_verification"]["finite_status"],
                "verdict": output["initial_verification"]["verdict"],
                "certificate_sha256": output["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
