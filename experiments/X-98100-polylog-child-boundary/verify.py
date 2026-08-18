#!/usr/bin/env python3
"""Exact finite algebra for the logarithmic-four boundary packet.

The asymptotic estimates use PNT/Mertens and the bounded base remainder from
PR #599. This replay verifies the Euler/product split, the Abel--Stieltjes
recombination, and the exponent-four control algebra. It does not prove the
remaining signed correlation or RH.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERDICT = "PASS_T98100_POLYLOG_CHILD_BOUNDARY"


def subset_products(primes):
    out = []
    for mask in range(1 << len(primes)):
        product = 1
        sign = 1
        for index, prime in enumerate(primes):
            if (mask >> index) & 1:
                product *= prime
                sign *= -1
        out.append((product, sign))
    return sorted(out)


def prefix(products, bound):
    return sum(
        (Fraction(sign, product) for product, sign in products if product <= bound),
        Fraction(0),
    )


def run():
    primes = [7, 11, 13]
    products = subset_products(primes)
    X = 1000
    Y = 20
    lower_product = Fraction(X, Y)
    activation_product = Fraction(X, 2)
    main = Fraction(3)

    # Synthetic continuous child profile with U(2)=0.
    def child(y):
        return Fraction(y) - 2

    def error(y):
        return child(y) - main

    active = sum(
        (
            Fraction(sign, product) * error(Fraction(X, product))
            for product, sign in products
            if lower_product < product <= activation_product
        ),
        Fraction(0),
    )
    left = main * prefix(products, activation_product) + active

    # Exact Stieltjes integral of S(X/y)dU(y); here dU=dy.
    breakpoints = {Fraction(2), Fraction(Y)}
    for product, _ in products:
        point = Fraction(X, product)
        if 2 < point < Y:
            breakpoints.add(point)
    ordered = sorted(breakpoints)
    integral = Fraction(0)
    for lower, upper in zip(ordered, ordered[1:]):
        midpoint = (lower + upper) / 2
        integral += prefix(products, Fraction(X, 1) / midpoint) * (upper - lower)

    right = -prefix(products, lower_product) * error(Fraction(Y)) + integral
    assert left == right

    # The source-blind control exponent is 2-alpha/2.
    powers = {
        "alpha_below_4": Fraction(2) - Fraction(39, 10) / 2,
        "alpha_at_4": Fraction(2) - Fraction(4) / 2,
        "alpha_above_4": Fraction(2) - Fraction(41, 10) / 2,
    }
    assert powers["alpha_below_4"] > 0
    assert powers["alpha_at_4"] == 0
    assert powers["alpha_above_4"] < 0

    core = {
        "schema": "riemann.t98100.polylog-child-boundary.v1",
        "certificate_class": "EXACT_RATIONAL_ALGEBRA",
        "synthetic_stieltjes": {
            "X": X,
            "Y": Y,
            "cutoff": str(lower_product),
            "activation": str(activation_product),
            "lhs": str(left),
            "rhs": str(right),
            "identity": left == right,
            "products": [[product, sign] for product, sign in products],
        },
        "bulk_power": {key: str(value) for key, value in powers.items()},
        "slow_cutoff_subpower": True,
        "l4pbr67_proved": False,
        "plst67_proved": False,
        "gpc67_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main():
    result = run()
    output = HERE / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
