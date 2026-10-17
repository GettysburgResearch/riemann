#!/usr/bin/env python3
"""Exact finite regression checks for two source-specific analytic notes.

These substitutions complement the general proofs. They do not establish
analytic continuation, an infinite Euler-product bound, or any RH statement.
No check relies on Python's assert statement, so python -O retains all checks.
"""

from argparse import ArgumentParser
from fractions import Fraction
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify():
    fraction = Fraction
    local_count = 0
    for q in (2, 3, 7, 13):
        r = fraction(1, q)
        for d in (fraction(1, 5), fraction(-1, 7), fraction(3, 11)):
            for v in (fraction(1, 3), fraction(-1, 4)):
                for e in (fraction(1, 6), fraction(-2, 9)):
                    # Source's four-term local Poisson formula, w=1.
                    source = (
                        1 / (1 - v)
                        + r / (1 - r)
                        + e / (1 - e) * ((1 - r) / (1 - v) + r)
                        - d / (1 - e)
                        * (1 + (1 / r - 1) * r * v / (1 - v))
                    )
                    extracted = (1 - v) * (1 - r) * source / (1 - d)
                    reduced = (
                        (1 - r * v) * (1 - (1 - r) * d - r * e)
                        / ((1 - d) * (1 - e))
                    )
                    require(extracted == reduced,
                            "Exact principal-residue identity failed")
                    correction = (
                        (1 - (1 - r) * d - r * e)
                        / ((1 - d) * (1 - e))
                    )
                    difference = (
                        (r * d + (1 - r) * e - d * e)
                        / ((1 - d) * (1 - e))
                    )
                    require(correction - 1 == difference,
                            "Exact correction subtraction failed")
                    local_count += 1

    inner_count = 0
    for x in (fraction(1, 10), fraction(1, 2), fraction(2)):
        for beta in (fraction(1, 7), fraction(1, 2), fraction(6, 7)):
            for y in (fraction(0), fraction(2, 5), fraction(3)):
                numerator = (
                    ((x - beta) ** 2 + y ** 2)
                    * ((x - 1 + beta) ** 2 + y ** 2)
                )
                denominator = (
                    ((x + 1 - beta) ** 2 + y ** 2)
                    * ((x + beta) ** 2 + y ** 2)
                )
                difference = 4 * x * (x ** 2 + y ** 2 + beta * (1 - beta))
                require(denominator - numerator == difference,
                        "Exact paired Hadamard modulus identity failed")
                require(difference > 0,
                        "The strict right-half-plane inequality failed")
                inner_count += 1

    require(local_count == 48, "Unexpected local substitution count")
    require(inner_count == 27, "Unexpected inner-pair substitution count")
    return {
        "status": "passed",
        "arithmetic": "fractions.Fraction; no floating-point arithmetic",
        "local_poisson_substitutions": local_count,
        "local_identities_per_substitution": 2,
        "paired_inner_substitutions": inner_count,
        "checks_use_assert": False,
        "scope": "Finite exact regression checks complement the written general proofs.",
        "not_certified": [
            "An infinite Euler product or its analytic continuation",
            "The Hecke functional equation or Hadamard factorization",
            "Hardy membership of the actual unlocalized arithmetic source",
            "A new zero-free region, RH, or GRH",
        ],
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("VERIFICATION.json"),
    )
    args = parser.parse_args()
    report = verify()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
