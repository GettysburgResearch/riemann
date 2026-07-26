#!/usr/bin/env python3
"""Bind one X-5604 exact count artifact to X-9703 direct-xi primitives."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VERIFY = load_module("verify_count_only", HERE / "verify.py")
PRIMITIVE_SCHEMA = "riemann.x9703-count-only-primitives.v1"
COUNT_SCHEMA = "riemann.x5604-slab-discrepancy.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class BuildError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BuildError(f"{path} must contain an object")
    return value


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


def rational(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise BuildError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BuildError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def parse_count_endpoint(value: Any, name: str) -> Fraction:
    if isinstance(value, dict):
        fraction_text = value.get("fraction")
        if not isinstance(fraction_text, str):
            raise BuildError(f"{name}.fraction is missing")
        return Fraction(fraction_text)
    if isinstance(value, str):
        return Fraction(value)
    raise BuildError(f"{name} has unsupported endpoint encoding")


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def build(
    primitives: dict[str, Any],
    count: dict[str, Any],
    count_digest: str,
    log_terms: int,
) -> dict[str, Any]:
    if (
        primitives.get("schema") != PRIMITIVE_SCHEMA
        or primitives.get("classification") != "RIEMANN_XI_DIRECTED"
        or primitives.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("primitive schema, class, or normalization mismatch")
    if count.get("schema") != COUNT_SCHEMA:
        raise BuildError("count artifact schema mismatch")
    classification = count.get("classification")
    if not isinstance(classification, str) or "RIGOROUS" not in classification:
        raise BuildError("count artifact is not rigorously classified")

    primitive_slab = primitives.get("slab")
    if not isinstance(primitive_slab, dict):
        raise BuildError("primitive slab is missing")
    lower = rational(primitive_slab.get("lower"), "primitives.slab.lower")
    upper = rational(primitive_slab.get("upper"), "primitives.slab.upper")
    target = rational(primitives.get("target"), "primitives.target")
    if parse_count_endpoint(count.get("a"), "count.a") != lower:
        raise BuildError("count and primitive lower endpoints differ")
    if parse_count_endpoint(count.get("b"), "count.b") != upper:
        raise BuildError("count and primitive upper endpoints differ")
    count_target = count.get("target")
    if count_target is not None:
        if not isinstance(count_target, dict):
            raise BuildError("count.target must be an object")
        if parse_count_endpoint(count_target.get("fraction"), "count.target.fraction") != target:
            raise BuildError("count and primitive target ordinates differ")
        if count_target.get("strictly_inside") is not True:
            raise BuildError("count artifact does not place target strictly inside")

    n_a = integer(count.get("N_a", {}).get("integer"), "count.N_a.integer")
    n_b = integer(count.get("N_b", {}).get("integer"), "count.N_b.integer")
    total_count = integer(count.get("N_total_in_slab"), "count.N_total_in_slab")
    if n_b - n_a != total_count or total_count < 0:
        raise BuildError("count difference is inconsistent")
    if integer(primitives.get("declared_total_count"), "declared_total_count") != total_count:
        raise BuildError("configured and recomputed total counts differ")

    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 3:
        raise BuildError("primitive table needs at least three points")
    points: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise BuildError("primitive point must be an object")
        identifier = raw.get("id")
        u = rational(raw.get("u"), f"points[{index}].u")
        rectangle = raw.get("xi_rectangle")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen
            or u <= 0
            or not isinstance(rectangle, dict)
        ):
            raise BuildError("invalid primitive point")
        seen.add(identifier)
        canonical = {"id": identifier, "u": fj(u), "xi_rectangle": rectangle}
        if raw.get("point_sha256") != canonical_sha(canonical):
            raise BuildError(f"primitive point digest mismatch at {identifier}")
        points.append({**canonical, "point_sha256": raw["point_sha256"]})
    points.sort(key=lambda point: rational(point["u"], "point.u"))

    rows = [
        {
            "id": f"co-{first['id']}-{middle['id']}-{last['id']}",
            "points": [first["id"], middle["id"], last["id"]],
        }
        for first, middle, last in itertools.combinations(points, 3)
    ]
    output: dict[str, Any] = {
        "schema": VERIFY.SCHEMA,
        "classification": VERIFY.PRODUCTION,
        "normalization_id": NORMALIZATION,
        "slab": {"lower": fj(lower), "upper": fj(upper)},
        "target": fj(target),
        "total_count_interval": {
            "lower": fj(Fraction(total_count)),
            "upper": fj(Fraction(total_count)),
        },
        "count_gate": {
            "status": VERIFY.COUNT_GATE,
            "sha256": count_digest,
            "N_a": n_a,
            "N_b": n_b,
        },
        "log_terms": log_terms,
        "points": points,
        "rows": rows,
        "source": {
            "primitive_certificate_sha256": primitives.get("certificate_sha256"),
            "count_artifact_sha256": count_digest,
            "slab_id": primitives.get("slab_id"),
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("count_artifact", type=Path)
    parser.add_argument("--log-terms", type=int, default=768)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = build(
            load(args.primitives),
            load(args.count_artifact),
            file_sha256(args.count_artifact),
            args.log_terms,
        )
        verification = VERIFY.verify(output)
    except (OSError, json.JSONDecodeError, BuildError, VERIFY.CertificateError) as error:
        print(json.dumps({"built": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    output["initial_verification"] = {
        "verdict": verification["verdict"],
        "certified_negative_rows": verification["certified_negative_rows"],
        "unresolved_rows": verification["unresolved_rows"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "slab_id": output["source"]["slab_id"],
                "row_count": len(rows := output["rows"]),
                "verdict": verification["verdict"],
                "certified_negative_rows": verification["certified_negative_rows"],
                "unresolved_rows": verification["unresolved_rows"],
                "certificate_sha256": output["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if verification["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
