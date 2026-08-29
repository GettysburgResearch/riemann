#!/usr/bin/env python3
"""Audit utilities for the optimized D-0801 carrier continuation.

STATUS: exact combinatorial checks and analytic Taylor-bound formulas are mixed
with ordinary floating-point result summaries. Nothing in this module is a
proof of a matrix sign.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence


def taylor_remainder_bound(
    absolute_weight_sum: float,
    delta: float,
    log_cutoff: float,
    order: int,
) -> float:
    """Return W exp(eta) eta^(R+1)/(R+1)! with eta=|delta| log(c)."""
    if absolute_weight_sum < 0:
        raise ValueError("absolute_weight_sum must be nonnegative")
    if log_cutoff <= 0:
        raise ValueError("log_cutoff must be positive")
    if order < 0:
        raise ValueError("order must be nonnegative")
    eta = abs(delta) * log_cutoff
    return (
        absolute_weight_sum
        * math.exp(eta)
        * eta ** (order + 1)
        / math.factorial(order + 1)
    )


def evaluate_fixed_vector_taylor(
    carrier: float,
    delta: float,
    moments: Sequence[complex],
) -> float:
    """Evaluate alpha(T+delta)-Re sum_r (-i delta)^r M_r/r!.

    The moments are the complete prime-side fixed-vector moments. This returns
    only the polynomial midpoint; use :func:`taylor_remainder_bound` for a
    rigorous real-arithmetic remainder formula (its floating evaluation here is
    still not directed rounded).
    """
    if carrier + delta <= 0:
        raise ValueError("carrier + delta must be positive")
    if not moments:
        raise ValueError("at least one moment is required")
    prime_value = sum(
        ((-1j * delta) ** r / math.factorial(r)) * moment
        for r, moment in enumerate(moments)
    ).real
    alpha = math.log((carrier + delta) / (2 * math.pi)) / (2 * math.pi)
    return alpha - prime_value


def validate_continuation_summary(data: dict[str, Any]) -> list[str]:
    """Fail closed on inconsistent term counts or promoted candidates."""
    if data.get("experiment_id") != "X-0901":
        raise ValueError("unexpected experiment_id")
    if data.get("counterexample_candidate") is not None:
        raise ValueError("an empirical summary must not promote a candidate")
    rows = data.get("cells")
    if not isinstance(rows, list) or not rows:
        raise ValueError("cells must be a nonempty list")

    messages: list[str] = []
    for row in rows:
        total = int(row["total_prime_power_terms"])
        expected = int(row["prime_count"]) + int(row["higher_prime_power_count"])
        if total != expected:
            raise ValueError(f"term-count mismatch for cutoff {row['cutoff']}")
        if int(row["K"]) <= 0:
            raise ValueError("K must be positive")
        if not math.isfinite(float(row["leading_margin"])):
            raise ValueError("leading margin must be finite")
        messages.append(
            f"c={row['cutoff']} K={row['K']} terms={total} "
            f"margin={row['leading_margin']:+.17g}"
        )
    return messages


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "summary",
        type=Path,
        nargs="?",
        default=Path(__file__).with_name("results") / "continuation-summary.json",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    data = load_json(args.summary)
    for message in validate_continuation_summary(data):
        print(message)
    audit = data["local_carrier_audit_c1e10_K1024"]
    bound = taylor_remainder_bound(
        float(audit["absolute_weight_sum"]),
        0.01,
        math.log(10**10),
        int(audit["moment_order"]),
    )
    print(f"recomputed |delta|=0.01 remainder: {bound:.17g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
