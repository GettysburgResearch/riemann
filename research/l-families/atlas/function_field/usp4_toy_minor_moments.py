#!/usr/bin/env python3
"""Exact USp(4) Haar moments for the genus-two toy coefficient minor.

If the normalized reciprocal roots are the eigenvalues of U in USp(4), then

    F(U) = (Tr U)^2 - e_2(U)^2

is the q-to-infinity model for (q*a_1^2-a_2^2)/q^2.  This module evaluates
the first six Haar moments by the C_2 Weyl constant-term formula and compares
them with the exact q=3,5,7 histograms.  It uses only small integer Laurent
polynomials; there is no random-matrix simulation or numerical integration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Iterable, Mapping, Sequence


Exponent = tuple[int, int]
Laurent = dict[Exponent, int]
HERE = Path(__file__).resolve().parent
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
FROZEN_MAX_MOMENT = 6
HAAR_STATUS = "RIGOROUS_CERTIFIED_WEYL_CONSTANT_TERM"
COMPARISON_STATUS = "CONJECTURAL_USP4_LIMIT_NOT_A_THEOREM"
HAAR_RANGE_MINIMUM = Fraction(-20, 1)
HAAR_RANGE_MAXIMUM = Fraction(4, 3)


def _clean(poly: Mapping[Exponent, int]) -> Laurent:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(*polynomials: Mapping[Exponent, int]) -> Laurent:
    result: Laurent = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return _clean(result)


def scale(polynomial: Mapping[Exponent, int], coefficient: int) -> Laurent:
    return _clean({exponent: coefficient * value for exponent, value in polynomial.items()})


def multiply(left: Mapping[Exponent, int], right: Mapping[Exponent, int]) -> Laurent:
    result: Laurent = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            result[exponent] = result.get(exponent, 0) + left_coefficient * right_coefficient
    return _clean(result)


def power(polynomial: Mapping[Exponent, int], exponent: int) -> Laurent:
    if exponent < 0:
        raise ValueError("Laurent-polynomial exponent must be nonnegative")
    result: Laurent = {(0, 0): 1}
    factor = dict(polynomial)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, factor)
        remaining //= 2
        if remaining:
            factor = multiply(factor, factor)
    return result


def substitute_square(polynomial: Mapping[Exponent, int]) -> Laurent:
    return {(2 * left, 2 * right): coefficient for (left, right), coefficient in polynomial.items()}


def divide_exact(polynomial: Mapping[Exponent, int], divisor: int) -> Laurent:
    if divisor == 0 or any(coefficient % divisor for coefficient in polynomial.values()):
        raise ArithmeticError("Laurent polynomial is not coefficientwise divisible")
    return _clean({exponent: coefficient // divisor for exponent, coefficient in polynomial.items()})


def constant_term(polynomial: Mapping[Exponent, int]) -> int:
    return polynomial.get((0, 0), 0)


def evaluate_at_identity(polynomial: Mapping[Exponent, int]) -> int:
    return sum(polynomial.values())


def statistic_in_trace_coordinates(left: Fraction, right: Fraction) -> Fraction:
    """Evaluate F for eigenangle traces left=2cos(theta_1), right=2cos(theta_2)."""

    if not -2 <= left <= 2 or not -2 <= right <= 2:
        raise ValueError("trace coordinates must both lie in [-2,2]")
    return (left - right) ** 2 - 4 - left * left * right * right


def trace_character() -> Laurent:
    return {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}


def exterior_square_character() -> Laurent:
    return {
        (0, 0): 2,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
    }


def statistic_character() -> Laurent:
    return add(power(trace_character(), 2), scale(power(exterior_square_character(), 2), -1))


def fundamental_five_character() -> Laurent:
    # wedge^2(Standard_4) = 1 + V_{omega_2}.
    return add(exterior_square_character(), {(0, 0): -1})


def traceless_symmetric_square_character() -> Laurent:
    # V_{2 omega_2} = Sym^2(V_{omega_2}) - 1, of dimension 14.
    five = fundamental_five_character()
    symmetric_square = divide_exact(add(power(five, 2), substitute_square(five)), 2)
    return add(symmetric_square, {(0, 0): -1})


def character_identity_residual() -> Laurent:
    # F = -(1 + chi_{omega_2} + chi_{2 omega_2}).
    return add(
        statistic_character(),
        {(0, 0): 1},
        fundamental_five_character(),
        traceless_symmetric_square_character(),
    )


def weyl_density() -> Laurent:
    density: Laurent = {(0, 0): 1}
    for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
        positive = {root: 1}
        negative = {(-root[0], -root[1]): 1}
        density = multiply(density, add({(0, 0): 1}, scale(positive, -1)))
        density = multiply(density, add({(0, 0): 1}, scale(negative, -1)))
    return density


def haar_moments(max_moment: int = FROZEN_MAX_MOMENT) -> list[int]:
    if not 1 <= max_moment <= FROZEN_MAX_MOMENT:
        raise ValueError(f"max_moment must lie in [1,{FROZEN_MAX_MOMENT}]")
    density = weyl_density()
    weyl_order = constant_term(density)
    if weyl_order != 8:
        raise ArithmeticError(f"unexpected C2 Weyl normalization {weyl_order}")
    statistic = statistic_character()
    moments: list[int] = []
    current: Laurent = {(0, 0): 1}
    for _ in range(max_moment):
        current = multiply(current, statistic)
        numerator = constant_term(multiply(current, density))
        if numerator % weyl_order:
            raise ArithmeticError("Haar constant term is not divisible by the Weyl order")
        moments.append(numerator // weyl_order)
    return moments


def centered_moments(raw_moments: Sequence[int]) -> list[int]:
    """Convert exact raw moments E[F^n] to E[(F-E[F])^n]."""

    if not raw_moments:
        return []
    raw_with_zero = [1, *raw_moments]
    mean = raw_moments[0]
    return [
        sum(
            comb(order, power)
            * (-mean) ** (order - power)
            * raw_with_zero[power]
            for power in range(order + 1)
        )
        for order in range(1, len(raw_moments) + 1)
    ]


def cumulants(raw_moments: Sequence[int]) -> list[int]:
    """Convert exact raw moments to cumulants by the triangular recurrence."""

    raw_with_zero = [1, *raw_moments]
    values = [0]
    for order in range(1, len(raw_with_zero)):
        correction = sum(
            comb(order - 1, index - 1)
            * values[index]
            * raw_with_zero[order - index]
            for index in range(1, order)
        )
        values.append(raw_with_zero[order] - correction)
    return values[1:]


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def finite_moments(family: Mapping[str, object], max_moment: int) -> list[Fraction]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    histogram = {int(key): int(value) for key, value in dict(family["K_histogram"]).items()}
    if sum(histogram.values()) != member_count:
        raise ValueError(f"q={q} histogram count mismatch")
    return [
        Fraction(
            sum(count * numerator**moment for numerator, count in histogram.items()),
            member_count * q ** (2 * moment),
        )
        for moment in range(1, max_moment + 1)
    ]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_fixture(q_scan_fixture: Path = Q_SCAN_FIXTURE) -> dict[str, object]:
    q_scan = json.loads(q_scan_fixture.read_text(encoding="utf-8"))
    if q_scan.get("schema") != "riemann.function_field.genus2_q_scan.v1":
        raise ValueError("unexpected genus-two q-scan schema")
    if q_scan.get("resource_contract", {}).get("frozen_q_values") != [3, 5, 7]:
        raise ValueError("USp(4) comparator requires the frozen q=3,5,7 scan")
    if character_identity_residual():
        raise ArithmeticError("USp(4) character identity failed")
    haar = haar_moments()
    centered = centered_moments(haar)
    haar_cumulants = cumulants(haar)
    source_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    comparisons: list[dict[str, object]] = []
    for family in q_scan["families"]:
        q = int(family["q"])
        moments = finite_moments(family, FROZEN_MAX_MOMENT)
        comparisons.append(
            {
                "q": q,
                "member_count": int(family["member_count"]),
                "moments": [
                    {
                        "order": order,
                        "finite_exact": _fraction_pair(value),
                        "usp4_haar_exact": haar[order - 1],
                        "finite_minus_haar": _fraction_pair(value - haar[order - 1]),
                    }
                    for order, value in enumerate(moments, start=1)
                ],
            }
        )
    payload: dict[str, object] = {
        "schema": "riemann.function_field.usp4_toy_minor_moments.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR.MOMENTS.V1",
        "rigor_level": HAAR_STATUS,
        "definition": (
            "For U in USp(4), F(U)=(Tr U)^2-e_2(U)^2; compare its exact Haar moments "
            "with the exact finite moments of K/q^2=(q*a_1^2-a_2^2)/q^2."
        ),
        "character_identity": {
            "status": "PROVED_EXACT_LAURENT_IDENTITY",
            "formula": "F=-(1+chi_{omega_2}+chi_{2*omega_2})",
            "dimensions_at_identity": {
                "standard": evaluate_at_identity(trace_character()),
                "omega_2": evaluate_at_identity(fundamental_five_character()),
                "2*omega_2": evaluate_at_identity(traceless_symmetric_square_character()),
                "F": evaluate_at_identity(statistic_character()),
            },
            "haar_mean_consequence": -1,
        },
        "range_certificate": {
            "status": "PROVED_EXACT_ELEMENTARY_OPTIMIZATION",
            "trace_coordinates": "X=2*cos(theta_1), Y=2*cos(theta_2), each in [-2,2]",
            "formula": "F=(X+Y)^2-(2+X*Y)^2=(X-Y)^2-4-X^2*Y^2",
            "minimum": _fraction_pair(HAAR_RANGE_MINIMUM),
            "minimum_witnesses": [
                {"X": [-2, 1], "Y": [-2, 1]},
                {"X": [2, 1], "Y": [2, 1]},
            ],
            "maximum": _fraction_pair(HAAR_RANGE_MAXIMUM),
            "maximum_witnesses": [
                {"X": [2, 1], "Y": [-2, 3]},
                {"X": [-2, 3], "Y": [2, 1]},
                {"X": [-2, 1], "Y": [2, 3]},
                {"X": [2, 3], "Y": [-2, 1]},
            ],
            "proof": (
                "The lower bound follows from (X-Y)^2>=0 and X^2Y^2<=16. For the upper "
                "bound, fix Y: the quadratic in X is convex when |Y|<=1, so an endpoint gives "
                "-3Y^2+4|Y|<=4/3; when |Y|>1, checking the feasible vertex and endpoints "
                "gives the same bound."
            ),
        },
        "weyl_certificate": {
            "root_system": "C2",
            "positive_roots_as_exponent_pairs": [[2, 0], [0, 2], [1, 1], [1, -1]],
            "formula": "integral f = CT(f*product_{alpha>0}(1-X^alpha)(1-X^-alpha))/8",
            "density_constant_term": constant_term(weyl_density()),
            "maximum_moment": FROZEN_MAX_MOMENT,
            "haar_moments_orders_1_through_6": haar,
            "haar_centered_moments_orders_1_through_6": centered,
            "haar_cumulants_orders_1_through_6": haar_cumulants,
            "arithmetic": "exact integer Laurent-polynomial convolution",
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/usp4_toy_minor_moments.py",
            "source_sha256_lf_normalized": hashlib.sha256(
                source_text.encode("utf-8")
            ).hexdigest(),
            "runtime_contract": "Python 3.11+ standard library; exact integer/rational arithmetic",
            "input_provenance": "content-bound exact q-scan histogram fixture",
        },
        "finite_source": {
            "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "canonical_sha256": _canonical_sha256(q_scan),
            "coverage": "all monic squarefree quintics over F_q for q=3,5,7",
        },
        "finite_comparisons": comparisons,
        "limit_target": {
            "status": COMPARISON_STATUS,
            "not_a_theorem": True,
            "statement": "For each fixed moment order, the finite K/q^2 moment tends to the USp(4) Haar moment as q tends to infinity.",
            "evidence_scope": "three exact fields q=3,5,7 and moment orders 1 through 6",
            "smallest_gap": "invoke a relevant hyperelliptic-family equidistribution theorem for this compact continuous class function, or evaluate the character correlations directly",
        },
        "firewall": (
            "The Weyl constant terms and the three finite histogram moments are separately exact. "
            "Their convergence is conjectural. F is a toy reciprocal-coefficient statistic, not "
            "an analytic Pick/Loewner, XD, or HCNC kernel."
        ),
        "resource_contract": {
            "maximum_moment": FROZEN_MAX_MOMENT,
            "random_sampling": False,
            "numerical_integration": False,
            "external_dependencies": False,
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare against this checked-in JSON fixture")
    parser.add_argument("--write", type=Path, help="write the exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"USp(4) moment fixture mismatch: {args.check}")
        print(f"OK: exact USp(4) moments match {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact USp(4) moment fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
