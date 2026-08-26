#!/usr/bin/env python3
"""Exact replay for the full-rational-place quadratic-family notch."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

Q_PANELS = (3, 5, 7, 9, 11)
DIRECT_PANELS = ((3, 0, 5), (5, 0, 3))


def is_prime_power(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value and value % divisor:
        divisor += 1
    if divisor * divisor > value:
        return True
    while value % divisor == 0:
        value //= divisor
    return value == 1


def orientation_sign(q: int) -> int:
    if q < 3 or q % 2 == 0 or not is_prime_power(q):
        raise ValueError("q must be an odd prime power")
    return -1 if q % 4 == 1 else 1


def zeta_numerator_coefficients(q: int) -> list[int]:
    """Coefficients of (1+s*q*u^2)^((q-1)/2)."""
    sign = orientation_sign(q)
    genus = (q - 1) // 2
    coefficients = [0] * (2 * genus + 1)
    for index in range(genus + 1):
        coefficients[2 * index] = math.comb(genus, index) * (sign * q) ** index
    return coefficients


def kernel_coefficient(q: int, index: int) -> int:
    """[v^index](1-q*v)/(1-v)^q."""
    if index < 0:
        return 0
    first = math.comb(q + index - 1, index)
    second = q * math.comb(q + index - 2, index - 1) if index else 0
    return first - second


def full_place_correlation(q: int, degree: int) -> int:
    """Exact full rational-place correlation over squarefree monic inputs."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    sign = orientation_sign(q)
    if degree % 2:
        return 0
    target = degree // 2
    genus = (q - 1) // 2
    return sum(
        math.comb(genus, index)
        * (sign * q) ** index
        * kernel_coefficient(q, target - index)
        for index in range(min(genus, target) + 1)
    )


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def polynomial_remainder(left: list[int], right: list[int], prime: int) -> list[int]:
    output = trim([value % prime for value in left])
    divisor = trim([value % prime for value in right])
    if divisor == [0]:
        raise ZeroDivisionError
    inverse = pow(divisor[-1], -1, prime)
    while len(output) >= len(divisor) and output != [0]:
        scale = output[-1] * inverse % prime
        shift = len(output) - len(divisor)
        for index, value in enumerate(divisor):
            output[index + shift] = (output[index + shift] - scale * value) % prime
        trim(output)
    return output


def polynomial_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left = trim(left[:])
    right = trim(right[:])
    while right != [0]:
        left, right = right, polynomial_remainder(left, right, prime)
    inverse = pow(left[-1], -1, prime)
    return [(value * inverse) % prime for value in left]


def is_squarefree(poly: list[int], prime: int) -> bool:
    derivative = [index * poly[index] % prime for index in range(1, len(poly))]
    derivative = trim(derivative or [0])
    return len(polynomial_gcd(poly, derivative, prime)) == 1


def evaluate(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def quadratic_character(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    return 1 if pow(value, (prime - 1) // 2, prime) == 1 else -1


def direct_prime_correlation(prime: int, degree: int) -> int:
    """Tiny direct control for prime fields only."""
    if prime not in (3, 5):
        raise ValueError("direct replay is capped at primes 3 and 5")
    total = 0
    for lower in itertools.product(range(prime), repeat=degree):
        poly = list(lower) + [1]
        if not is_squarefree(poly, prime):
            continue
        product = 1
        for place in range(prime):
            product *= quadratic_character(evaluate(poly, place, prime), prime)
        total += product
    return total


def q_panel(q: int) -> dict[str, object]:
    sign = orientation_sign(q)
    genus = (q - 1) // 2
    return {
        "q": q,
        "q_mod_4": q % 4,
        "genus": genus,
        "orientation_sign": sign,
        "curve": "y^2=x-x^q",
        "F_q_points": q + 1,
        "F_q2_points": q * q + 1 + sign * q * (q - 1),
        "zeta_numerator": f"(1+({sign})*{q}*u^2)^{genus}",
        "correlations_degrees_0_to_10": [
            full_place_correlation(q, degree) for degree in range(11)
        ],
    }


def run() -> dict[str, object]:
    direct = []
    candidates = 0
    for prime, lower, upper in DIRECT_PANELS:
        for degree in range(lower, upper + 1):
            candidates += prime**degree
            direct.append(
                {
                    "q": prime,
                    "degree": degree,
                    "direct": direct_prime_correlation(prime, degree),
                    "formula": full_place_correlation(prime, degree),
                }
            )
    return {
        "theorem": {
            "auxiliary_curve": "C_q:y^2=x-x^q",
            "zeta_numerator": ("P_q(u)=(1+s_q*q*u^2)^((q-1)/2), s_q=(-1)^((q+1)/2)"),
            "full_place_series": ("sum_n S_(n,q)u^n=P_q(u)*(1-q*u^2)/(1-u^2)^q"),
            "odd_notch": "S_(2k+1,q)=0 for every k>=0",
        },
        "q_panels": [q_panel(q) for q in Q_PANELS],
        "direct_prime_controls": direct,
        "resource_caps": {
            "direct_prime_fields": [3, 5],
            "candidate_polynomials": candidates,
            "maximum_direct_degree": 5,
            "extension_field_elements_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
        "firewalls": [
            "the vanishing is a family correlation, not an individual L-zero",
            "the full-place source uses all rational evaluation places",
            "no growing-closed-place or FFPS source adapter follows",
            "no RH or GRH conclusion is made",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
