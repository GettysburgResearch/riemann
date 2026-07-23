#!/usr/bin/env python3
"""Expanded rigorous L-3904 scan over nearly the full horizontal range.

This wrapper reuses the exact generator, Arb producer, and checker in
`matched_pole_scan.py` while replacing only the finite search manifest.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Sequence

import matched_pole_scan as base

EXPANDED_NODES: tuple[Fraction, ...] = tuple(
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
EXPANDED_MODEL_FRACTIONS: tuple[Fraction, ...] = tuple(
    Fraction(index, 16) for index in range(1, 16)
)
EXPANDED_DIMENSIONS: tuple[int, ...] = tuple(range(2, 10))


def configure() -> None:
    base.NODES = EXPANDED_NODES
    base.MODEL_FRACTIONS = EXPANDED_MODEL_FRACTIONS
    base.DIMENSIONS = EXPANDED_DIMENSIONS


def build_template():
    configure()
    return base.build_template()


def main(argv: Sequence[str] | None = None) -> int:
    configure()
    return base.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
