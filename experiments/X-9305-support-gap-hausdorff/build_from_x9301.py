#!/usr/bin/env python3
"""Build an L-9307 support-gap certificate from a complete X-9301 slab deflation.

The adapter evaluates no special function. It verifies the saturated sign-chain
certificate, requires the X-9301 source to contain every chain bin, reconstructs
a conservative support lower bound, and forms directed residual logarithm
intervals from the shared completed-xi rectangles and selected factor balls.
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

SOURCE_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
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


def build(
    source: dict[str, Any],
    chain: dict[str, Any],
    *,
    log_terms: int,
) -> dict[str, Any]:
    if (
        source.get("schema") != SOURCE_SCHEMA
        or source.get("classification") != "RIEMANN_XI_DIRECTED"
        or source.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("source is not a production X-9301 certificate")
    try:
        base_verification = BASE.verify(source)
        chain_verification = SIGN.verify(chain)
    except Exception as error:
        raise BuildError(f"parent certificate verification failed: {error}") from error

    if chain_verification.get("classification") != SIGN.PRODUCTION:
        raise BuildError("sign chain is not production classified")
    if chain_verification.get("verdict") != "SATURATED_SIGN_CHAIN_ISOLATES_ALL_ZEROS":
        raise BuildError("sign chain does not prove complete slab isolation")

    total_count = integer(chain_verification.get("total_count"), "chain.total_count")
    source_meta = source.get("source")
    if not isinstance(source_meta, dict):
        raise BuildError("X-9301 source metadata is missing")
    if integer(source_meta.get("nearest_count"), "source.nearest_count") != total_count:
        raise BuildError("X-9301 certificate does not remove the complete slab count")
    if len(source.get("zero_bins", [])) != total_count:
        raise BuildError("X-9301 zero-bin count does not equal the complete slab count")
    if source_meta.get("sign_chain_certificate_sha256") != chain_verification.get(
        "certificate_sha256"
    ):
        raise BuildError("X-9301 certificate is not bound to this sign-chain table")

    target = rational(source.get("ordinate"), "source.ordinate")
    chain_target = rational(chain.get("target_ordinate"), "chain.target_ordinate")
    if target != chain_target:
        raise BuildError("target ordinate mismatch")

    slab = chain_verification.get("slab")
    if not isinstance(slab, dict):
        raise BuildError("verified sign chain has no slab")
    slab_lower = rational(slab.get("lower"), "chain.slab.lower")
    slab_upper = rational(slab.get("upper"), "chain.slab.upper")
    if not slab_lower < target < slab_upper:
        raise BuildError("target is not strictly inside the complete slab")
    support_gap = min((target - slab_lower) ** 2, (slab_upper - target) ** 2)
    if support_gap <= 0:
        raise BuildError("computed support gap is not positive")

    terms = integer(log_terms, "log_terms")
    if terms < 32 or terms > 8192:
        raise BuildError("log_terms must be between 32 and 8192")

    points = BASE.parse_points(source)
    raw_bins = source.get("zero_bins")
    if not isinstance(raw_bins, list):
        raise BuildError("source zero_bins must be an array")
    parsed_bins: list[tuple[Fraction, Fraction, int]] = []
    for index, raw in enumerate(raw_bins):
        if not isinstance(raw, dict):
            raise BuildError("zero bin must be an object")
        lower = rational(raw.get("lower_ordinate"), f"zero_bins[{index}].lower")
        upper = rational(raw.get("upper_ordinate"), f"zero_bins[{index}].upper")
        count = integer(raw.get("count_lower"), f"zero_bins[{index}].count")
        if not lower < upper or count != 1:
            raise BuildError("complete sign-chain transport needs one-zero strict bins")
        distance_lower, distance_upper = square_range(target - upper, target - lower)
        parsed_bins.append((distance_lower, distance_upper, count))

    values: list[dict[str, Any]] = []
    for identifier, point in sorted(points.items(), key=lambda item: item[1]["u"]):
        raw_log = BASE.log_positive_interval(point["h"], terms)
        residual = raw_log
        for distance_lower, distance_upper, count in parsed_bins:
            factor = BASE.Interval(
                BASE.log_positive_fraction(point["u"] + distance_lower, terms).lower,
                BASE.log_positive_fraction(point["u"] + distance_upper, terms).upper,
            )
            residual = residual.sub(factor.scale(Fraction(count)))
        values.append(
            {
                "id": identifier,
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

    support_binding = {
        "sign_chain_certificate_sha256": chain_verification["certificate_sha256"],
        "x9301_certificate_sha256": source.get("certificate_sha256"),
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
            "sha256": canonical_sha(support_binding),
            "binding": support_binding,
        },
        "values": values,
        "rows": rows,
        "source": {
            "parent_verdict": base_verification["verdict"],
            "parent_certificate_sha256": source.get("certificate_sha256"),
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
    parser.add_argument("x9301_certificate", type=Path)
    parser.add_argument("sign_chain", type=Path)
    parser.add_argument("--log-terms", type=int, default=512)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(
            load(args.x9301_certificate),
            load(args.sign_chain),
            log_terms=args.log_terms,
        )
        verification = SUPPORT.verify(result)
    except (OSError, json.JSONDecodeError, BuildError) as error:
        print(json.dumps({"built": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    result["initial_verification"] = {
        "verdict": verification["verdict"],
        "certified_negative_rows": verification["certified_negative_rows"],
        "unresolved_rows": verification["unresolved_rows"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "support_gap": result["support_gap"],
                "row_count": len(result["rows"]),
                "verdict": verification["verdict"],
                "certified_negative_rows": verification["certified_negative_rows"],
                "unresolved_rows": verification["unresolved_rows"],
                "certificate_sha256": result["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if verification["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
