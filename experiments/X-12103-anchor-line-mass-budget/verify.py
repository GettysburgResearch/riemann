#!/usr/bin/env python3
"""Exact checker for L-12103 multi-anchor line-mass budgets."""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.anchor-line-mass-budget.v1"
VERIFY_SCHEMA = "riemann.anchor-line-mass-budget.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a base-10 integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), name + ".numerator")
    denominator = parse_int(value.get("denominator"), name + ".denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("reversed interval")

    @classmethod
    def parse(cls, raw: Any, name: str) -> "Interval":
        if not isinstance(raw, dict):
            raise CertificateError(f"{name} must be an object")
        return cls(
            parse_fraction(raw.get("lower"), name + ".lower"),
            parse_fraction(raw.get("upper"), name + ".upper"),
        )

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def multiply(self, other: "Interval") -> "Interval":
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(products), max(products))

    def to_json(self) -> dict[str, object]:
        return {
            "lower": fraction_json(self.lower),
            "upper": fraction_json(self.upper),
        }


def interval_horner(
    coefficients: list[Fraction], argument: Interval
) -> Interval:
    if not coefficients:
        raise CertificateError("polynomial coefficient array is empty")
    result = Interval(coefficients[-1], coefficients[-1])
    for coefficient in reversed(coefficients[:-1]):
        result = result.multiply(argument).add(
            Interval(coefficient, coefficient)
        )
    return result


def square_lower(interval: Interval) -> Fraction:
    if interval.lower <= 0 <= interval.upper:
        return Fraction(0)
    return min(interval.lower * interval.lower, interval.upper * interval.upper)


def squared_distance_interval(
    ordinate: Fraction, gamma: Interval
) -> Interval:
    left = ordinate - gamma.lower
    right = ordinate - gamma.upper
    high = max(left * left, right * right)
    low = (
        Fraction(0)
        if gamma.lower <= ordinate <= gamma.upper
        else min(left * left, right * right)
    )
    return Interval(low, high)


def product_at(
    value: Fraction,
    old_nodes: list[Fraction],
    anchors: list[Fraction],
) -> Fraction:
    result = Fraction(1)
    for node in old_nodes + anchors:
        result *= value + node
    return result


def parse_positive_list(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty array")
    values = [
        parse_fraction(value, f"{name}[{index}]")
        for index, value in enumerate(raw)
    ]
    if any(value <= 0 for value in values):
        raise CertificateError(f"{name} values must be positive")
    if len(set(values)) != len(values):
        raise CertificateError(f"{name} values must be distinct")
    return values


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    channel = data.get("channel")
    if channel not in ("square", "y-square"):
        raise CertificateError("channel must be square or y-square")
    source_measure = data.get("source_measure")
    if source_measure not in (
        "RAW_UNREMOVED_RESPONSE",
        "SELECTED_FACTOR_RESIDUAL",
        "DIRECTED_ADD_BACK_RESPONSE",
    ):
        raise CertificateError("unsupported source_measure convention")

    ordinate = parse_fraction(data.get("ordinate"), "ordinate")
    old_nodes = parse_positive_list(data.get("old_nodes"), "old_nodes")
    anchors = parse_positive_list(data.get("anchors"), "anchors")
    if set(old_nodes) & set(anchors):
        raise CertificateError("anchor duplicates an old node")

    raw_polynomial = data.get("polynomial")
    if not isinstance(raw_polynomial, list) or not raw_polynomial:
        raise CertificateError("polynomial must be a nonempty array")
    polynomial = [
        parse_fraction(value, f"polynomial[{index}]")
        for index, value in enumerate(raw_polynomial)
    ]
    if all(value == 0 for value in polynomial):
        raise CertificateError("polynomial must be nonzero")

    total = Interval.parse(data.get("total_interval"), "total_interval")
    raw_bins = data.get("zero_bins")
    declared_ids = data.get("declared_bin_ids")
    if not isinstance(raw_bins, list) or not raw_bins:
        raise CertificateError("zero_bins must be a nonempty array")
    if not isinstance(declared_ids, list) or not all(
        isinstance(value, str) for value in declared_ids
    ):
        raise CertificateError("declared_bin_ids must be an array of strings")

    parsed_bins: list[tuple[Fraction, Fraction, str, int, dict[str, Any]]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_bins):
        if not isinstance(raw, dict):
            raise CertificateError(f"zero_bins[{index}] must be an object")
        identifier = raw.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen
        ):
            raise CertificateError("zero-bin IDs must be nonempty and unique")
        seen.add(identifier)
        gate = raw.get("gate")
        if gate != "CERTIFIED_DISJOINT_CRITICAL_LINE_ZERO_BIN":
            raise CertificateError(f"{identifier}: blocking zero-bin gate")
        if raw.get("survives_source_measure") is not True:
            raise CertificateError(
                f"{identifier}: bin mass was removed or not source-bound"
            )
        gamma = Interval.parse(raw.get("gamma_interval"), f"{identifier}.gamma")
        multiplicity = parse_int(raw.get("multiplicity_lower"), f"{identifier}.multiplicity")
        if multiplicity <= 0:
            raise CertificateError(f"{identifier}: multiplicity must be positive")
        parsed_bins.append(
            (
                gamma.lower,
                gamma.upper,
                identifier,
                multiplicity,
                raw,
            )
        )

    parsed_bins.sort(key=lambda item: (item[0], item[1], item[2]))
    for left, right in zip(parsed_bins, parsed_bins[1:]):
        if not left[1] < right[0]:
            raise CertificateError("certified zero bins are not strictly disjoint")
    if declared_ids != [item[2] for item in parsed_bins]:
        raise CertificateError(
            "declared_bin_ids must equal the ordered zero-bin IDs"
        )

    leverage_sum = Fraction(0)
    summaries: list[dict[str, Any]] = []
    for gamma_lower, gamma_upper, identifier, multiplicity, raw in parsed_bins:
        gamma = Interval(gamma_lower, gamma_upper)
        y_interval = squared_distance_interval(ordinate, gamma)
        polynomial_interval = interval_horner(polynomial, y_interval)
        q2_lower = square_lower(polynomial_interval)
        denominator_upper = product_at(
            y_interval.upper, old_nodes, anchors
        )
        if denominator_upper <= 0:
            raise CertificateError("response denominator is not positive")
        leverage = q2_lower / denominator_upper
        if channel == "y-square":
            leverage *= y_interval.lower
        claimed = raw.get("claimed_leverage_lower")
        if claimed is not None and parse_fraction(
            claimed, f"{identifier}.claimed_leverage_lower"
        ) != leverage:
            raise CertificateError(f"{identifier}: claimed leverage mismatch")
        weighted = multiplicity * leverage
        leverage_sum += weighted
        summaries.append(
            {
                "id": identifier,
                "gamma_interval": gamma.to_json(),
                "multiplicity_lower": multiplicity,
                "y_interval": y_interval.to_json(),
                "polynomial_interval": polynomial_interval.to_json(),
                "q_squared_lower": fraction_json(q2_lower),
                "denominator_upper": fraction_json(denominator_upper),
                "leverage_lower": fraction_json(leverage),
                "weighted_leverage_lower": fraction_json(weighted),
            }
        )

    claimed_sum = data.get("claimed_leverage_sum")
    if claimed_sum is not None and parse_fraction(
        claimed_sum, "claimed_leverage_sum"
    ) != leverage_sum:
        raise CertificateError("claimed_leverage_sum mismatch")

    strict = total.upper < leverage_sum
    status = (
        "CERTIFIED_LINE_MASS_BUDGET_CONTRADICTION"
        if strict
        else "NO_STRICT_LINE_MASS_CONTRADICTION"
    )
    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "channel": channel,
        "source_measure": source_measure,
        "ordinate": fraction_json(ordinate),
        "total_interval": total.to_json(),
        "line_mass_leverage_lower": fraction_json(leverage_sum),
        "strict_reversal": strict,
        "bins": summaries,
        "proof_boundary": (
            "This verifies exact finite response leverage and the strict budget "
            "comparison. It does not establish the direct-xi response theorem, "
            "the zero-bin proofs, or independent primitive reproduction."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 1 if result["strict_reversal"] else 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
