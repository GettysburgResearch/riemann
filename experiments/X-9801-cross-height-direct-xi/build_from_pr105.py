#!/usr/bin/env python3
"""Bind three PR #105 direct-xi primitive tables to one X-9801 portfolio."""
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
SPEC = importlib.util.spec_from_file_location("x9801_verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
MANIFEST_SCHEMA = "riemann.x9801-symmetric-candidates.v1"


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


def interval(value: Any, name: str) -> VERIFY.Interval:
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


def modulus_squared(rectangle: dict[str, Any], name: str) -> VERIFY.Interval:
    real = interval(rectangle.get("real"), f"{name}.real")
    imag = interval(rectangle.get("imag"), f"{name}.imag")
    real_sq = square_interval(real)
    imag_sq = square_interval(imag)
    return VERIFY.Interval(real_sq.lower + imag_sq.lower, real_sq.upper + imag_sq.upper)


def parse_primitive(
    data: dict[str, Any], path: Path, expected_ordinate: Fraction, point_ids: list[str]
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
        rectangle = point.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise BuildError(f"{path}:{point_id} has no xi rectangle")
        h_value = modulus_squared(rectangle, f"{path}.{point_id}.xi_rectangle")
        points.append({"id": point_id, "u": fj(x * x), "h_interval": VERIFY.ij(h_value)})
    return {
        "ordinate": ordinate,
        "scale": integer(
            data.get("common_xi_scale_power_of_two", 0),
            f"{path}.common_xi_scale_power_of_two",
        ),
        "points": points,
    }


def build(
    minus_path: Path,
    center_path: Path,
    plus_path: Path,
    manifest_path: Path,
    candidate_id: str,
) -> dict[str, Any]:
    manifest = load(manifest_path)
    if manifest.get("schema") != MANIFEST_SCHEMA:
        raise BuildError("candidate manifest schema mismatch")
    candidates = manifest.get("candidates")
    if not isinstance(candidates, list):
        raise BuildError("candidate manifest has no candidate array")
    candidate = next(
        (item for item in candidates if isinstance(item, dict) and item.get("id") == candidate_id),
        None,
    )
    if candidate is None:
        raise BuildError(f"unknown candidate ID {candidate_id}")
    origin = rational(manifest.get("origin"), "manifest.origin")
    half_step = rational(manifest.get("half_step"), "manifest.half_step")
    expected = {
        "minus": origin - half_step,
        "center": origin,
        "plus": origin + half_step,
    }
    point_ids = candidate.get("point_ids")
    side = candidate.get("side_exponents")
    center = candidate.get("center_exponents")
    if (
        not isinstance(point_ids, list)
        or not isinstance(side, list)
        or not isinstance(center, list)
        or len(point_ids) != len(side)
        or len(point_ids) != len(center)
        or len(point_ids) < 2
    ):
        raise BuildError("candidate point/exponent arrays are malformed")
    point_ids = [str(value) for value in point_ids]
    side = [integer(value, "side exponent") for value in side]
    center = [integer(value, "center exponent") for value in center]

    paths = {"minus": minus_path, "center": center_path, "plus": plus_path}
    primitive_data = {identifier: load(path) for identifier, path in paths.items()}
    parsed = {
        identifier: parse_primitive(
            primitive_data[identifier], paths[identifier], expected[identifier], point_ids
        )
        for identifier in ("minus", "center", "plus")
    }
    scales = {item["scale"] for item in parsed.values()}
    if len(scales) != 1:
        raise BuildError("the three source tables use different common xi scales")

    heights = []
    for identifier in ("minus", "center", "plus"):
        heights.append(
            {
                "id": identifier,
                "ordinate": fj(parsed[identifier]["ordinate"]),
                "common_xi_scale_power_of_two": parsed[identifier]["scale"],
                "source_sha256": sha256_file(paths[identifier]),
                "points": parsed[identifier]["points"],
            }
        )
    terms = []
    for identifier, exponents in (("minus", side), ("center", center), ("plus", side)):
        for point_id, exponent in zip(point_ids, exponents):
            if exponent:
                terms.append(
                    {
                        "height": identifier,
                        "point": point_id,
                        "exponent": exponent,
                    }
                )
    output: dict[str, Any] = {
        "schema": VERIFY.SCHEMA,
        "classification": VERIFY.PRODUCTION,
        "normalization_id": VERIFY.NORMALIZATION,
        "origin": fj(origin),
        "candidate_id": candidate_id,
        "heights": heights,
        "terms": terms,
        "polynomial_gate": {"status": VERIFY.POLYNOMIAL_GATE},
        "source": {
            "manifest_sha256": sha256_file(manifest_path),
            "candidate_description": candidate.get("description"),
        },
    }
    verification = VERIFY.verify(output)
    output["initial_verification"] = {
        "verdict": verification["verdict"],
        "status": verification["status"],
        "difference_interval": verification["difference_interval"],
        "polynomial_proof_object_sha256": verification["polynomial"][
            "proof_object_sha256"
        ],
    }
    output["certificate_sha256"] = VERIFY.canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minus", type=Path, required=True)
    parser.add_argument("--center", type=Path, required=True)
    parser.add_argument("--plus", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = build(
            args.minus, args.center, args.plus, args.manifest, args.candidate_id
        )
    except (OSError, json.JSONDecodeError, BuildError, VERIFY.CertificateError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "candidate_id": args.candidate_id,
                "status": output["initial_verification"]["status"],
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
