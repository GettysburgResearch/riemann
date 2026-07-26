#!/usr/bin/env python3
"""Exact X-9314 checker for the L-9316 Padé residual-mass budgets."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x9314-pade-residual-mass-budget.v1"
OUTPUT_SCHEMA = "riemann.x9314-pade-residual-mass-budget-verification.v1"
ZERO_GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"
SEGMENT_GATE = "CERTIFIED_FAR_ENDPOINT_RESIDUAL_SEGMENT"


class CertificateError(ValueError):
    pass


class Interval:
    __slots__ = ("lower", "upper")

    def __init__(self, lower: Fraction, upper: Fraction):
        if lower > upper:
            raise CertificateError("reversed interval")
        self.lower = lower
        self.upper = upper

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)

    def square(self) -> "Interval":
        values = (self.lower * self.lower, self.upper * self.upper)
        lower = Fraction(0) if self.lower <= 0 <= self.upper else min(values)
        return Interval(lower, max(values))

    def reciprocal(self) -> "Interval":
        if self.lower <= 0:
            raise CertificateError("denominator interval is not strictly positive")
        return Interval(1 / self.upper, 1 / self.lower)

    def div(self, other: "Interval") -> "Interval":
        return self.mul(other.reciprocal())

    def width(self) -> Fraction:
        return self.upper - self.lower


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        fraction(raw.get("lower"), f"{name}.lower"),
        fraction(raw.get("upper"), f"{name}.upper"),
    )


def parse_vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty list")
    return [fraction(item, f"{name}[{i}]") for i, item in enumerate(raw)]


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def evaluate_polynomial(coefficients: list[Fraction], y: Interval) -> Interval:
    value = Interval(Fraction(0), Fraction(0))
    for coefficient in reversed(coefficients):
        value = value.mul(y).add(Interval(coefficient, coefficient))
    return value


def evaluate_at(coefficients: list[Fraction], y: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coefficients):
        value = value * y + coefficient
    return value


def leverage_interval(
    side: str,
    y: Interval,
    nodes: list[Fraction],
    w: Fraction,
    support: Fraction,
    q: list[Fraction],
) -> Interval:
    if y.lower < support:
        raise CertificateError("residual-mass interval lies below the declared support")
    q_squared = evaluate_polynomial(q, y).square()
    denominator = y.add(Interval(w, w))
    for node in nodes:
        denominator = denominator.mul(y.add(Interval(node, node)))
    if side == "lower":
        numerator = q_squared
    elif side == "upper":
        if w + support <= 0:
            raise CertificateError("upper leverage requires w+A>0")
        numerator = y.sub(Interval(support, support)).mul(q_squared).scale(
            Fraction(1, 1) / (w + support)
        )
    else:
        raise CertificateError("side must be 'lower' or 'upper'")
    return numerator.div(denominator)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise CertificateError("unsupported certificate schema")
    side = data.get("side")
    if side not in ("lower", "upper"):
        raise CertificateError("side must be lower or upper")
    w = fraction(data.get("w"), "w")
    support = fraction(data.get("support_lower"), "support_lower")
    if w < 0 or support < 0:
        raise CertificateError("w and support_lower must be nonnegative")
    raw_nodes = data.get("nodes")
    if not isinstance(raw_nodes, list):
        raise CertificateError("nodes must be a list")
    nodes = [fraction(item, f"nodes[{i}]") for i, item in enumerate(raw_nodes)]
    if any(node <= 0 for node in nodes) or any(
        nodes[i] >= nodes[i + 1] for i in range(len(nodes) - 1)
    ):
        raise CertificateError("nodes must be strictly increasing and positive")
    if w in nodes:
        raise CertificateError("new node w duplicates an old node")
    q = parse_vector(data.get("q"), "q")
    if evaluate_at(q, -w) != 1:
        raise CertificateError("q(-w) must equal one exactly")
    gap = interval(data.get("gap"), "gap")

    raw_items = data.get("zero_bins")
    if not isinstance(raw_items, list) or not raw_items:
        raise CertificateError("zero_bins must be nonempty")
    parsed: list[tuple[str, str, Interval, int, Fraction]] = []
    seen: set[str] = set()
    atom_intervals: list[Interval] = []
    for index, item in enumerate(raw_items):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise CertificateError("bad residual-mass record")
        identifier = item["id"]
        if not identifier or identifier in seen:
            raise CertificateError("residual-mass IDs must be nonempty and unique")
        seen.add(identifier)
        kind = item.get("kind", "atom")
        if kind not in ("atom", "segment"):
            raise CertificateError("kind must be atom or segment")
        gate = item.get("gate")
        expected_gate = ZERO_GATE if kind == "atom" else SEGMENT_GATE
        if not isinstance(gate, dict) or gate.get("status") != expected_gate:
            raise CertificateError("residual-mass semantic gate mismatch")
        multiplicity = integer(item.get("multiplicity"), f"zero_bins[{index}].multiplicity")
        if multiplicity <= 0:
            raise CertificateError("residual-mass multiplicity must be positive")
        y = interval(item.get("y"), f"zero_bins[{index}].y")
        if kind == "atom":
            measure_weight = Fraction(multiplicity)
            atom_intervals.append(y)
        else:
            if y.width() <= 0:
                raise CertificateError("certified segment must have positive length")
            measure_weight = multiplicity * y.width()
        parsed.append((identifier, kind, y, multiplicity, measure_weight))

    atom_intervals.sort(key=lambda value: (value.lower, value.upper))
    for left, right in zip(atom_intervals, atom_intervals[1:]):
        if left.upper >= right.lower:
            raise CertificateError("atomic zero bins overlap or touch")

    rows: list[dict[str, Any]] = []
    total_lower = Fraction(0)
    total_upper = Fraction(0)
    atom_count = segment_count = 0
    for identifier, kind, y, multiplicity, measure_weight in parsed:
        value = leverage_interval(side, y, nodes, w, support, q)
        contribution = value.scale(measure_weight)
        total_lower += contribution.lower
        total_upper += contribution.upper
        atom_count += kind == "atom"
        segment_count += kind == "segment"
        rows.append(
            {
                "id": identifier,
                "kind": kind,
                "multiplicity": multiplicity,
                "measure_weight": fraction_json(measure_weight),
                "y": interval_json(y),
                "leverage": interval_json(value),
                "contribution": interval_json(contribution),
                "contribution_width": fraction_json(contribution.width()),
            }
        )
    rows.sort(
        key=lambda row: Fraction(
            row["contribution_width"]["numerator"],
            row["contribution_width"]["denominator"],
        ),
        reverse=True,
    )

    verdict = (
        "CERTIFIED_NEGATIVE_PADE_RESIDUAL_MASS_BUDGET"
        if gap.upper < total_lower
        else "CERTIFIED_CONSISTENT_PADE_RESIDUAL_MASS_BUDGET"
        if gap.lower >= total_upper
        else "UNRESOLVED_PADE_RESIDUAL_MASS_BUDGET"
    )
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": data.get("classification"),
        "analytic_claim": "L-9316",
        "experiment_id": "X-9314",
        "certificate_sha256": file_sha256(path),
        "side": side,
        "w": fraction_json(w),
        "support_lower": fraction_json(support),
        "q": [fraction_json(value) for value in q],
        "gap": interval_json(gap),
        "certified_residual_mass_contribution": {
            "lower": fraction_json(total_lower),
            "upper": fraction_json(total_upper),
        },
        "gap_minus_certified_mass_upper": fraction_json(gap.upper - total_lower),
        "residual_item_count": len(rows),
        "atomic_bin_count": atom_count,
        "segment_count": segment_count,
        "ranked_items": rows,
        "verdict": verdict,
        "counterexample_nomination": (
            "PENDING_INDEPENDENT_REPRODUCTION"
            if verdict == "CERTIFIED_NEGATIVE_PADE_RESIDUAL_MASS_BUDGET"
            else None
        ),
        "proof_boundary": (
            "Exact rational interval Horner evaluation and exact summation over a "
            "proof-gated residual submeasure. Atomic bins are required to be pairwise "
            "disjoint; segment records represent common far-endpoint residual Lebesgue "
            "measure and may overlap by certified multiplicity."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (OSError, json.JSONDecodeError, CertificateError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 1 if result["verdict"] == "CERTIFIED_NEGATIVE_PADE_RESIDUAL_MASS_BUDGET" else 0


if __name__ == "__main__":
    raise SystemExit(main())
