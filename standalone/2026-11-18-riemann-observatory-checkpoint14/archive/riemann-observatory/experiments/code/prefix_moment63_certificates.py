#!/usr/bin/env python3
"""Certify finite-lattice bounds from exact or enclosed limiting prefix jets."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from math import comb, prod
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("An interval has its lower endpoint above its upper endpoint.")

    def as_json(self) -> dict[str, str]:
        return {"lower": str(self.lower), "upper": str(self.upper)}


def rational(value: object) -> Fraction:
    if type(value) is int or isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"Invalid rational endpoint {value!r}.") from exc
    raise ValueError("Use JSON integers or strings for exact rational endpoints.")


def interval(value: object) -> Interval:
    if isinstance(value, list):
        if len(value) != 2:
            raise ValueError("An interval must have two rational endpoints.")
        return Interval(rational(value[0]), rational(value[1]))
    exact = rational(value)
    return Interval(exact, exact)


def multiply(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    """Multiply polynomials stored in ascending power order."""
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i + j] += first * second
    return result


def from_roots(roots: Iterable[int]) -> list[Fraction]:
    result = [Fraction(1)]
    for root in roots:
        result = multiply(result, [Fraction(-root), Fraction(1)])
    return result


def taylor_basis(size: int) -> list[list[Fraction]]:
    """Return p_0,...,p_(size-1) such that [b^k]C = integral p_(k-1) dν."""
    legendre = [[Fraction(1)]]
    for j in range(1, size):
        product = multiply(legendre[-1], [Fraction(-j * (j + 1)), Fraction(1)])
        legendre.append([term / (j * (j + 1)) for term in product])

    integrated = []
    for degree in range(size):
        coefficients = [Fraction(0)] * (degree + 1)
        for i in range(degree + 1):
            terms = multiply(legendre[i], legendre[degree - i])
            for j, value in enumerate(terms):
                coefficients[j] += value / (degree + 1)
        integrated.append(coefficients)

    rows = []
    for degree in range(size):
        coefficients = [Fraction(0)] * (degree + 1)
        for i in range(degree + 1):
            for j, value in enumerate(integrated[i]):
                coefficients[j] += comb(degree, i) * value
        rows.append(coefficients)
    return rows


def taylor_functional(
    polynomial: Sequence[Fraction], basis: Sequence[Sequence[Fraction]]
) -> list[Fraction]:
    """Find the unique row that integrates a polynomial against the Taylor data."""
    residual = list(polynomial)
    row = [Fraction(0)] * len(basis)
    for degree in range(len(polynomial) - 1, -1, -1):
        row[degree] = residual[degree] / basis[degree][degree]
        for j in range(degree):
            residual[j] -= row[degree] * basis[degree][j]
    return row


def enclose(row: Sequence[Fraction], data: Sequence[Interval]) -> Interval:
    """Project the original coefficient box through a rational linear row."""
    lower = upper = Fraction(0)
    for scale, bounds in zip(row, data, strict=True):
        first, last = scale * bounds.lower, scale * bounds.upper
        lower += min(first, last)
        upper += max(first, last)
    return Interval(lower, upper)


def nonnegative(lower: Fraction, upper: Fraction, label: str) -> Interval:
    lower = max(Fraction(0), lower)
    if upper < lower:
        raise ValueError(f"The {label} bounds exclude every nonnegative value.")
    return Interval(lower, upper)


def certificates(
    data: Sequence[Interval], constant: Interval | None = None
) -> dict[str, object]:
    cutoff = len(data)
    if cutoff == 0:
        raise ValueError("Supply at least one nonconstant Taylor coefficient.")
    if any(bounds.upper < 0 for bounds in data):
        raise ValueError("A nonconstant Taylor coefficient is strictly negative.")
    if any(bounds.upper < data[0].lower for bounds in data[1:]):
        raise ValueError("Every higher Taylor coefficient must be at least the first.")
    if constant is not None and constant.upper < 0:
        raise ValueError("The constant term is strictly negative.")

    basis = taylor_basis(cutoff)
    moment_bounds = []
    for degree in range(cutoff):
        monomial = [Fraction(0)] * degree + [Fraction(1)]
        moment_bounds.append(enclose(taylor_functional(monomial, basis), data))

    total_mass = nonnegative(
        moment_bounds[0].lower, moment_bounds[0].upper, "total weighted mass"
    )
    sites = [m * (m - 1) for m in range(2, cutoff + 1)]
    first_tail = cutoff * (cutoff + 1)
    denominator = prod(first_tail - x for x in sites)
    tail_row = taylor_functional(from_roots(sites), basis)
    integral = enclose(tail_row, data)
    positive_integral = nonnegative(integral.lower, integral.upper, "tail polynomial integral")
    normalized_upper = positive_integral.upper / denominator

    weights = []
    masses = []
    for index, site in enumerate(sites):
        m = index + 2
        others = sites[:index] + sites[index + 1:]
        derivative = prod(site - other for other in others)
        cardinal = [term / derivative for term in from_roots(others)]
        row = taylor_functional(cardinal, basis)
        error_scale = abs(derivative) * (first_tail - site)
        margin_row = [
            coefficient - tail / (derivative * (first_tail - site))
            for coefficient, tail in zip(row, tail_row, strict=True)
        ]
        cardinal_bounds = enclose(row, data)
        margin_bounds = enclose(margin_row, data)
        if derivative > 0:
            low, high = margin_bounds.lower, cardinal_bounds.upper
        else:
            low, high = cardinal_bounds.lower, margin_bounds.upper
        mass = nonnegative(low, min(high, total_mass.upper), f"mass at multiplicity {m}")
        masses.append(mass)
        weights.append({
            "multiplicity": m,
            "node": site,
            "weighted_mass_t_m": mass.as_json(),
            "weight_W_m": Interval(mass.lower / site**2, mass.upper / site**2).as_json(),
            "cardinal_integral": cardinal_bounds.as_json(),
            "cardinal_error_bound": str(positive_integral.upper / error_scale),
        })

    tail_lower = total_mass.lower - sum(mass.upper for mass in masses)
    tail_upper = min(normalized_upper, total_mass.upper - sum(mass.lower for mass in masses))
    tail = nonnegative(tail_lower, tail_upper, "total tail weighted mass")
    if tail.upper == 0 and positive_integral.lower > 0:
        raise ValueError("The tail bounds force zero mass but a positive tail polynomial integral.")
    if total_mass.upper == 0 and any(not bounds.lower <= 0 <= bounds.upper for bounds in data):
        raise ValueError("Zero total weighted mass requires all nonconstant coefficients to vanish.")

    tail_status = "undetermined"
    if tail.upper == 0:
        tail_status = "zero_tail"
    elif positive_integral.lower > 0 or tail.lower > 0:
        tail_status = "positive_tail"

    result = {
        "cutoff_M": cutoff,
        "moments_y0_through_yM_minus_1": [bounds.as_json() for bounds in moment_bounds],
        "tail_polynomial_integral": integral.as_json(),
        "tail_polynomial_at_first_tail_node": str(denominator),
        "normalized_tail_functional": [str(term / denominator) for term in tail_row],
        "normalized_tail_weighted_mass_upper_bound": str(normalized_upper),
        "tail_weighted_mass": tail.as_json(),
        "tail_W_m_sum_upper_bound": str(tail.upper / first_tail**2),
        "tail_constant_term_contribution_upper_bound": str(tail.upper / cutoff**2),
        "tail_status_if_feasible": tail_status,
        "weights_through_cutoff": weights,
    }
    if constant is not None:
        constant_lower = sum(mass.lower / (i + 1)**2 for i, mass in enumerate(masses))
        constant_upper = sum(mass.upper / (i + 1)**2 for i, mass in enumerate(masses))
        simple = nonnegative(
            constant.lower - constant_upper - tail.upper / cutoff**2,
            constant.upper - constant_lower,
            "simple weight W_1",
        )
        result["simple_weight_W_1"] = simple.as_json()
    return result


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field {key!r}.")
        result[key] = value
    return result


def run(document: object) -> dict[str, object]:
    if not isinstance(document, dict):
        raise ValueError("Input must be a JSON object.")
    allowed = {"provenance", "coefficient_source", "taylor_coefficients", "constant_term"}
    if document.keys() - allowed:
        names = ", ".join(repr(key) for key in sorted(document.keys() - allowed))
        raise ValueError(f"Unknown input fields: {names}.")
    provenance = document.get("provenance")
    if provenance not in ("synthetic_profile", "certified_limiting_coefficients"):
        raise ValueError(
            "Set provenance to synthetic_profile or certified_limiting_coefficients."
        )
    source = document.get("coefficient_source")
    if not isinstance(source, str) or not source.strip():
        raise ValueError("Describe the limiting coefficient source in coefficient_source.")
    try:
        source.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("coefficient_source must be valid Unicode text.") from exc
    coefficients = document.get("taylor_coefficients")
    if not isinstance(coefficients, list):
        raise ValueError("taylor_coefficients must be an array starting with [b^1]C.")
    data = [interval(value) for value in coefficients]
    constant = interval(document["constant_term"]) if "constant_term" in document else None
    return {
        "provenance": provenance,
        "coefficient_source": source,
        "feasibility_checked": False,
        "scope": (
            "Bounds and tail conclusions apply if a nonnegative triangular-lattice profile "
            "realizes the supplied limiting Taylor data. The tool has not verified feasibility "
            "or provenance. Finite-N staircase derivatives are outside this input model."
        ),
        **certificates(data, constant),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON input path or - for standard input")
    args = parser.parse_args()
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text("utf-8")
        result = run(json.loads(source, object_pairs_hook=unique_object))
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
