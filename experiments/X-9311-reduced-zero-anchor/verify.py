#!/usr/bin/env python3
"""Exact finite audit of the reduced PR #103 zero-anchor contraction."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction

WIDTHS = [
    "2.828071869222290280884311858E-32",
    "1.286057064875397921993863321E-43",
    "1.988421841774870004548452287E-54",
    "1.175493950145145246683494602E-64",
    "2.747579815705865474897300640E-74",
    "2.561340916824773299983733625E-83",
    "9.543743392637506133804713416E-92",
    "1.422107763170988029524258125E-99",
    "8.475010054222902011834355409E-107",
    "2.019625467619877652365141021E-113",
    "1.923255177426525688361649608E-119",
    "7.300998396176616690223298992E-125",
    "1.094793370014924141650451357E-129",
    "6.266636693158138930134884099E-134",
    "1.217679564087200075919942680E-137",
]


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        result[i] += value
    for i, value in enumerate(right):
        result[i] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def response(nodes: list[Fraction], beta: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = poly_mul(term, [node, Fraction(1)])
        result = poly_add(result, [-coefficient * value for value in term])
    return result


def basis(nodes: list[Fraction]) -> list[Fraction]:
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-1 / denominator)
    return output


def rational(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def main() -> None:
    old_nodes = [Fraction(1, 2 ** (2 * k)) for k in range(20, 4, -1)]
    full_beta = basis([Fraction(0)] + old_nodes)
    beta_zero = full_beta[0]
    delta = full_beta[1:]
    delta[0] += beta_zero
    if sum(delta) != 0:
        raise SystemExit("reduced coefficients are not zero sum")
    polynomial = response(old_nodes, delta)
    if len(polynomial) != 15:
        raise SystemExit("reduced response does not have degree at most fourteen")
    widths = [Fraction(value) for value in WIDTHS]
    budget = sum(abs(coefficient) * width for coefficient, width in zip(polynomial, widths))
    result = {
        "schema": "riemann.x9311-zero-anchor-reduced-contraction.v1",
        "reference_node": rational(old_nodes[0]),
        "beta_zero": rational(beta_zero),
        "polynomial_coefficients": [rational(value) for value in polynomial],
        "moment_width_budget": rational(budget),
        "verified_moment_width_below_1e_minus_19": budget < Fraction(1, 10**19),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("ascii")
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    if not result["verified_moment_width_below_1e_minus_19"]:
        raise SystemExit(1)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
