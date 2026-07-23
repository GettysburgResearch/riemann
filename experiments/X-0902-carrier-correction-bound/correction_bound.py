#!/usr/bin/env python3
"""Uniform high-carrier correction bounds for the D-0801 piecewise family.

This module evaluates the explicit bound derived in L-0901. The bound controls
all exact archimedean and pole Rayleigh corrections relative to the scalar
high-carrier screen, uniformly for every unit vector in C^K.

The arithmetic here is ordinary Python floating point and is therefore a
reproducibility aid, not itself a directed-rounding proof certificate.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class CorrectionBound:
    cutoff: int
    carrier: float
    cells: int
    log_cutoff: float
    integration_by_parts_constant: float
    archimedean_bound: float
    pole_bound: float
    total_bound: float


def correction_bound(cutoff: int, carrier: float, cells: int) -> CorrectionBound:
    """Return the L-0901 uniform normalized operator bound.

    The normalized exact matrix is compared with

        log(T/(2*pi))/(2*pi) * I - S_K(T,c).

    Parameters are required to lie in the regime used by the proof:
    c >= 2, T > 0, and K >= 1.
    """
    if not isinstance(cutoff, int) or isinstance(cutoff, bool) or cutoff < 2:
        raise ValueError("cutoff must be an integer at least 2")
    if not math.isfinite(carrier) or carrier <= 0:
        raise ValueError("carrier must be finite and positive")
    if not isinstance(cells, int) or isinstance(cells, bool) or cells < 1:
        raise ValueError("cells must be a positive integer")

    L = math.log(cutoff)
    # B dominates |F(0)| + |F(2L)| + Var(F) in the oscillatory residual.
    B = (cells / L) * (math.log(cells) + 2.0) + 6.0 * cells + 5.0
    arch = (B + 1.0 / L) / (math.pi * carrier)
    pole = 4.0 * math.sqrt(cutoff) * cells * cells / (
        math.pi * L * carrier * carrier
    )
    return CorrectionBound(
        cutoff=cutoff,
        carrier=carrier,
        cells=cells,
        log_cutoff=L,
        integration_by_parts_constant=B,
        archimedean_bound=arch,
        pole_bound=pole,
        total_bound=arch + pole,
    )


def evaluate_ladder(
    carrier: float, rows: Iterable[tuple[int, int, float]]
) -> dict:
    cells = []
    for cutoff, K, leading_margin in rows:
        bound = correction_bound(cutoff, carrier, K)
        cells.append(
            {
                **asdict(bound),
                "empirical_leading_margin": leading_margin,
                "margin_to_bound_ratio": leading_margin / bound.total_bound,
                "correction_can_reverse_reported_sign": leading_margin <= bound.total_bound,
            }
        )
    return {
        "experiment_id": "X-0902",
        "status": "PROPOSED_BOUND_WITH_ORDINARY_FLOAT_EVALUATION",
        "carrier": carrier,
        "cells": cells,
        "counterexample_candidate": None,
        "warning": (
            "The analytic inequality is recorded in L-0901. These decimal "
            "evaluations are not directed-rounding certificates, and the "
            "underlying prime Toeplitz margins remain ordinary numerical values."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--carrier", type=float, default=4709203636353.65)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = [
        (10**8, 1024, 0.006643091775833554),
        (10**9, 1024, 0.0023504233978552946),
        (10**10, 1024, 0.0006076603725748697),
        (10**10, 2048, 0.0006027589005261902),
        (10**11, 1024, 0.00026896626427230785),
    ]
    result = evaluate_ladder(args.carrier, rows)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
