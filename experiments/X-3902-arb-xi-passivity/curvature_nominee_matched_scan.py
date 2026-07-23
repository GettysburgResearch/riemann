#!/usr/bin/env python3
"""Escalate the lowest empirical curvature minima to rigorous L-3904 scans."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any, Sequence

import matched_pole_scan as base

NOMINEE_NODES: tuple[Fraction, ...] = tuple(
    Fraction(text)
    for text in (
        "0.00001",
        "0.00002",
        "0.00004",
        "0.00008",
        "0.00016",
        "0.00032",
        "0.00064",
        "0.00128",
        "0.00256",
        "0.00512",
        "0.01024",
        "0.02048",
        "0.04096",
        "0.08192",
        "0.16384",
        "0.32768",
        "0.45",
        "0.49",
        "0.499",
    )
)
NOMINEE_MODEL_FRACTIONS: tuple[Fraction, ...] = tuple(
    Fraction(index, 8) for index in range(1, 8)
)
NOMINEE_DIMENSIONS: tuple[int, ...] = tuple(range(2, 8))


def load_nominee_heights(path: Path, count: int) -> tuple[tuple[str, Fraction], ...]:
    data = json.loads(path.read_text(encoding="utf-8"))
    nominees = data.get("top_nominees")
    if not isinstance(nominees, list) or len(nominees) < count:
        raise ValueError("nomination file has too few top_nominees")
    heights: list[tuple[str, Fraction]] = []
    seen: set[Fraction] = set()
    for index, row in enumerate(nominees[:count], start=1):
        if not isinstance(row, dict) or "nominee_t" not in row:
            raise ValueError("malformed nominee row")
        height = Fraction(str(row["nominee_t"]))
        if height in seen:
            raise ValueError("duplicate nominee ordinate")
        seen.add(height)
        heights.append((f"curv-{index:02d}", height))
    return tuple(heights)


def configure(heights: tuple[tuple[str, Fraction], ...]) -> None:
    base.HEIGHTS = heights
    base.NODES = NOMINEE_NODES
    base.MODEL_FRACTIONS = NOMINEE_MODEL_FRACTIONS
    base.DIMENSIONS = NOMINEE_DIMENSIONS


def build_template(
    nomination_path: Path, nominee_count: int
) -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    heights = load_nominee_heights(nomination_path, nominee_count)
    configure(heights)
    template, metadata = base.build_template()
    template_metadata = template.setdefault("metadata", {})
    if not isinstance(template_metadata, dict):
        raise ValueError("template metadata must be an object")
    template_metadata.update(
        {
            "experiment_id": "X-3904",
            "nomination_source": str(nomination_path),
            "nominee_count": nominee_count,
            "claim": "L-3904",
        }
    )
    return template, metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nomination", type=Path, required=True)
    parser.add_argument("--nominees", type=int, default=8)
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--verification", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.nominees < 1:
        raise ValueError("nominees must be positive")
    if args.precision_bits < 64:
        raise ValueError("precision_bits must be at least 64")

    from produce_certificate import build_certificate

    template, metadata = build_template(args.nomination, args.nominees)
    certificate, verification = build_certificate(template, args.precision_bits)
    summary = base.summarize(verification, metadata, args.precision_bits)
    nomination = json.loads(args.nomination.read_text(encoding="utf-8"))
    summary.update(
        {
            "schema": "riemann.xi-curvature-nominee-matched-result.v1",
            "experiment_id": "X-3904",
            "nomination_parameters": nomination.get("parameters"),
            "nominees": nomination.get("top_nominees", [])[: args.nominees],
            "node_count_per_height": len(NOMINEE_NODES),
            "model_fractions": [base.fraction_json(value) for value in NOMINEE_MODEL_FRACTIONS],
            "dimensions": list(NOMINEE_DIMENSIONS),
        }
    )
    for path, value in (
        (args.certificate, certificate),
        (args.verification, verification),
        (args.summary, summary),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
