#!/usr/bin/env python3
"""Bind directed completed-xi primitives to saturated sign-chain zero bins."""
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
PARENT = HERE.parent / "X-9301-zero-deflated-xi-modulus"


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SIGN = load_module("verify_sign_chain", HERE / "verify_sign_chain.py")
BASE = load_module(
    "build_pr71_nearest_certificate",
    PARENT / "build_pr71_nearest_certificate.py",
)

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
OUTPUT_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"


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


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def build(
    primitives: dict[str, Any],
    chain: dict[str, Any],
    config: dict[str, Any],
    nearest_count: int,
) -> dict[str, Any]:
    if (
        primitives.get("schema") != PRIMITIVE_SCHEMA
        or primitives.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("primitive schema/normalization mismatch")
    try:
        verified = SIGN.verify(chain)
    except Exception as error:
        raise BuildError(f"sign-chain certificate failed: {error}") from error
    if verified.get("classification") != SIGN.PRODUCTION:
        raise BuildError("sign chain is not production classified")

    total = integer(verified.get("total_count"), "sign_chain.total_count")
    if nearest_count <= 0 or nearest_count > total:
        raise BuildError("nearest_count outside available sign-chain bins")

    ordinate = rational(primitives.get("ordinate"), "primitives.ordinate")
    chain_target = chain.get("target_ordinate")
    if chain_target is None or ordinate != rational(
        chain_target, "sign_chain.target_ordinate"
    ):
        raise BuildError("ordinate mismatch")

    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise BuildError("points missing")
    points: list[dict[str, Any]] = []
    point_ids: set[str] = set()
    for index, point in enumerate(raw_points):
        if (
            not isinstance(point, dict)
            or not isinstance(point.get("id"), str)
            or not point["id"]
            or point["id"] in point_ids
        ):
            raise BuildError("bad primitive point")
        point_ids.add(point["id"])
        x = rational(point.get("x"), f"point {index}.x")
        if (
            x <= 0
            or not isinstance(point.get("xi_rectangle"), dict)
            or point.get("functional_equation_residual_contains_zero") is not True
        ):
            raise BuildError("invalid primitive point")
        canonical = {
            "id": point["id"],
            "u": fraction_json(x * x),
            "xi_rectangle": point["xi_rectangle"],
        }
        points.append({**canonical, "point_sha256": canonical_sha(canonical)})

    rows = BASE.validate_rows(config, point_ids)
    log_terms = integer(config.get("log_terms", 256), "log_terms")

    parsed: list[dict[str, Any]] = []
    for row in verified["bins"]:
        lower = rational(row["lower"], "bin.lower")
        upper = rational(row["upper"], "bin.upper")
        if not lower < upper:
            raise BuildError("zero bin is empty or reversed")
        distance_square_upper = max(
            (ordinate - lower) ** 2,
            (ordinate - upper) ** 2,
        )
        parsed.append(
            {
                "index": integer(row["bin_index"], "bin.index"),
                "lower": lower,
                "upper": upper,
                "B": distance_square_upper,
            }
        )

    parsed.sort(key=lambda zero: (zero["lower"], zero["upper"], zero["index"]))
    for left, right in zip(parsed, parsed[1:]):
        if left["upper"] >= right["lower"]:
            raise BuildError(
                "sign-chain bins overlap or touch; run additional refinement "
                "before X-9301 binding"
            )

    selected = sorted(parsed, key=lambda zero: (zero["B"], zero["index"]))[
        :nearest_count
    ]
    rank = {zero["index"]: index + 1 for index, zero in enumerate(selected)}
    chain_digest = verified["certificate_sha256"]

    zero_bins: list[dict[str, Any]] = []
    for zero in sorted(selected, key=lambda item: (item["lower"], item["upper"])):
        gate_digest = hashlib.sha256(
            f"{chain_digest}:{zero['index']}".encode("ascii")
        ).hexdigest()
        zero_bins.append(
            {
                "id": f"pr71-chain-zero-{zero['index']}",
                "lower_ordinate": fraction_json(zero["lower"]),
                "upper_ordinate": fraction_json(zero["upper"]),
                "count_lower": 1,
                "gate": {"status": GATE, "sha256": gate_digest},
                "distance_rank": rank[zero["index"]],
                "distance_square_upper": fraction_json(zero["B"]),
            }
        )

    output = {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": fraction_json(ordinate),
        "log_terms": log_terms,
        "points": sorted(
            points, key=lambda point: rational(point["u"], "point.u")
        ),
        "zero_bins": zero_bins,
        "rows": rows,
        "source": {
            "primitive_sha256": canonical_sha(primitives),
            "sign_chain_certificate_sha256": chain_digest,
            "nearest_count": nearest_count,
            "selected_chain_bin_indices": [
                zero["index"] for zero in selected
            ],
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("sign_chain", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--nearest-count", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = build(
            load(args.primitives),
            load(args.sign_chain),
            load(args.config),
            args.nearest_count,
        )
    except (OSError, json.JSONDecodeError, BuildError) as error:
        print(
            json.dumps({"built": False, "error": str(error)}, indent=2),
            file=sys.stderr,
        )
        return 2
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "schema": output["schema"],
                "nearest_count": args.nearest_count,
                "selected_chain_bin_indices": output["source"][
                    "selected_chain_bin_indices"
                ],
                "certificate_sha256": output["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
