#!/usr/bin/env python3
"""Build an X-9305 certificate from far-right direct-xi rectangles and a sign chain.

The adapter evaluates no special function.  It verifies the complete saturated
Hardy-Z chain, checks all primitive fingerprints and functional-equation gates,
forms exact modulus-square and logarithm intervals, removes every slab factor,
and emits every three-node support-gap chord row.
"""
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
ROOT = HERE.parent
X9301 = ROOT / "X-9301-zero-deflated-xi-modulus"
X9304 = ROOT / "X-9304-sign-chain-zero-bins"


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SUPPORT = load_module("verify_support_gap", HERE / "verify_support_gap.py")
BASE = load_module(
    "verify_zero_deflated_modulus", X9301 / "verify_zero_deflated_modulus.py"
)
SIGN = load_module("verify_sign_chain", X9304 / "verify_sign_chain.py")

PRIMITIVE_SCHEMA = "riemann.x9305-support-scale-primitives.v1"
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


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Any) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def square_range(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    if lower > upper:
        raise BuildError("square interval is reversed")
    high = max(lower * lower, upper * upper)
    if lower <= 0 <= upper:
        low = Fraction(0)
    else:
        low = min(lower * lower, upper * upper)
    return low, high


def parse_primitive_points(
    primitives: dict[str, Any],
) -> list[dict[str, Any]]:
    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 3:
        raise BuildError("support-scale primitives need at least three points")
    points: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise BuildError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise BuildError("primitive point IDs must be nonempty and unique")
        seen.add(identifier)
        u = rational(raw.get("u"), f"points[{index}].u")
        if u <= 0:
            raise BuildError("support-scale nodes must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise BuildError("primitive xi_rectangle must be an object")
        real = BASE.interval(rectangle.get("real"), f"points[{index}].real")
        imag = BASE.interval(rectangle.get("imag"), f"points[{index}].imag")
        if raw.get("functional_equation_residual_contains_zero") is not True:
            raise BuildError("functional-equation residual gate failed")
        canonical = {
            "id": identifier,
            "alpha": raw.get("alpha"),
            "u": fj(u),
            "x_interval": raw.get("x_interval"),
            "xi_rectangle": rectangle,
        }
        if raw.get("point_sha256") != canonical_sha(canonical):
            raise BuildError(f"primitive point digest mismatch at {identifier}")
        points.append(
            {
                "id": identifier,
                "u": u,
                "h": BASE.modulus_squared(real, imag),
            }
        )
    points.sort(key=lambda point: point["u"])
    if any(left["u"] >= right["u"] for left, right in zip(points, points[1:])):
        raise BuildError("support-scale nodes are not strictly increasing")
    return points


def build(
    primitives: dict[str, Any],
    chain: dict[str, Any],
    *,
    log_terms: int,
) -> dict[str, Any]:
    if (
        primitives.get("schema") != PRIMITIVE_SCHEMA
        or primitives.get("classification") != "RIEMANN_XI_DIRECTED"
        or primitives.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("primitive schema, class, or normalization mismatch")
    try:
        chain_verification = SIGN.verify(chain)
    except Exception as error:
        raise BuildError(f"sign-chain verification failed: {error}") from error
    if (
        chain_verification.get("classification") != SIGN.PRODUCTION
        or chain_verification.get("verdict")
        != "SATURATED_SIGN_CHAIN_ISOLATES_ALL_ZEROS"
    ):
        raise BuildError("sign chain does not prove complete production isolation")

    total_count = integer(chain_verification.get("total_count"), "chain.total_count")
    target = rational(primitives.get("ordinate"), "primitives.ordinate")
    chain_target = rational(chain.get("target_ordinate"), "chain.target_ordinate")
    if target != chain_target:
        raise BuildError("target ordinate mismatch")

    primitive_slab = primitives.get("slab")
    chain_slab = chain_verification.get("slab")
    if not isinstance(primitive_slab, dict) or not isinstance(chain_slab, dict):
        raise BuildError("primitive or chain slab is missing")
    slab_lower = rational(chain_slab.get("lower"), "chain.slab.lower")
    slab_upper = rational(chain_slab.get("upper"), "chain.slab.upper")
    if (
        rational(primitive_slab.get("lower"), "primitives.slab.lower")
        != slab_lower
        or rational(primitive_slab.get("upper"), "primitives.slab.upper")
        != slab_upper
    ):
        raise BuildError("primitive and chain slabs differ")
    if not slab_lower < target < slab_upper:
        raise BuildError("target is not strictly inside the complete slab")
    support_gap = min((target - slab_lower) ** 2, (slab_upper - target) ** 2)
    if support_gap <= 0:
        raise BuildError("support gap is not positive")
    if rational(primitives.get("support_gap"), "primitives.support_gap") != support_gap:
        raise BuildError("primitive support gap does not match the exact slab")

    terms = integer(log_terms, "log_terms")
    if terms < 32 or terms > 8192:
        raise BuildError("log_terms must be between 32 and 8192")
    points = parse_primitive_points(primitives)

    raw_bins = chain_verification.get("bins")
    if not isinstance(raw_bins, list) or len(raw_bins) != total_count:
        raise BuildError("verified sign chain does not expose the complete bin list")
    bins: list[tuple[Fraction, Fraction]] = []
    for index, raw in enumerate(raw_bins):
        if not isinstance(raw, dict) or raw.get("exact_zero_count") != 1:
            raise BuildError("each chain bin must contain exactly one zero")
        lower = rational(raw.get("lower"), f"bins[{index}].lower")
        upper = rational(raw.get("upper"), f"bins[{index}].upper")
        if not lower < upper:
            raise BuildError("chain bin is empty or reversed")
        bins.append((lower, upper))
    bins.sort()
    for left, right in zip(bins, bins[1:]):
        if left[1] >= right[0]:
            raise BuildError("closed chain bins overlap or touch; refine them further")

    distance_ranges = [
        square_range(target - upper, target - lower) for lower, upper in bins
    ]
    values: list[dict[str, Any]] = []
    for point in points:
        residual = BASE.log_positive_interval(point["h"], terms)
        for distance_lower, distance_upper in distance_ranges:
            factor = BASE.Interval(
                BASE.log_positive_fraction(point["u"] + distance_lower, terms).lower,
                BASE.log_positive_fraction(point["u"] + distance_upper, terms).upper,
            )
            residual = residual.sub(factor)
        values.append(
            {
                "id": point["id"],
                "u": fj(point["u"]),
                "residual_log": ij(residual),
            }
        )

    rows = [
        {
            "id": f"sg-{first['id']}-{middle['id']}-{last['id']}",
            "kind": "support-gap-chord",
            "nodes": [first["id"], middle["id"], last["id"]],
        }
        for first, middle, last in itertools.combinations(values, 3)
    ]
    binding = {
        "primitive_certificate_sha256": primitives.get("certificate_sha256"),
        "sign_chain_certificate_sha256": chain_verification[
            "certificate_sha256"
        ],
        "support_gap": fj(support_gap),
        "complete_count": total_count,
        "slab": {"lower": fj(slab_lower), "upper": fj(slab_upper)},
    }
    output = {
        "schema": SUPPORT.SCHEMA,
        "classification": SUPPORT.PRODUCTION,
        "support_gap": fj(support_gap),
        "log_terms": terms,
        "support_gate": {
            "status": SUPPORT.SUPPORT_GATE,
            "sha256": canonical_sha(binding),
            "binding": binding,
        },
        "values": values,
        "rows": rows,
        "source": {
            "primitive_certificate_sha256": primitives.get("certificate_sha256"),
            "sign_chain_certificate_sha256": chain_verification[
                "certificate_sha256"
            ],
            "complete_count": total_count,
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("sign_chain", type=Path)
    parser.add_argument("--log-terms", type=int, default=768)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = build(
            load(args.primitives),
            load(args.sign_chain),
            log_terms=args.log_terms,
        )
        verification = SUPPORT.verify(output)
    except (
        OSError,
        json.JSONDecodeError,
        BuildError,
        SUPPORT.CertificateError,
    ) as error:
        print(json.dumps({"built": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    output["initial_verification"] = {
        "verdict": verification["verdict"],
        "certified_negative_rows": verification["certified_negative_rows"],
        "unresolved_rows": verification["unresolved_rows"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": output["schema"],
                "row_count": len(output["rows"]),
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
