#!/usr/bin/env python3
"""Exact finite regression for the proposed critical local-to-Bohr theorem.

This program verifies finite identities and small-D data only.  It does not
prove the uniform Farey-cluster estimate of T-22801.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x22801-critical-local-bohr.v1"


class VerificationError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerificationError(f"{name} must be an integer")
    return value


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise VerificationError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise VerificationError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = integer(value[0], name + "[0]")
        q = integer(value[1], name + "[1]")
        if q == 0:
            raise VerificationError(f"{name} denominator is zero")
        return Fraction(p, q)
    raise VerificationError(f"{name} must be an integer, string, or [p,q]")


def mobius(n: int) -> int:
    if n < 1:
        raise VerificationError("mobius input must be positive")
    x = n
    factors = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            factors += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        factors += 1
    return -1 if factors % 2 else 1


def jordan(n: int, order: int) -> int:
    result = n**order
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            result = result // (p**order) * (p**order - 1)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        result = result // (x**order) * (x**order - 1)
    return result


def divisor_coordinate(D: int, q: int, order: int) -> Fraction:
    return sum(
        (Fraction(mobius(d), d**order) for d in range(q, D + 1, q)),
        Fraction(0),
    )


def check_reduced_coefficient_formula(D: int) -> int:
    checks = 0
    for q in range(1, D + 1):
        u = divisor_coordinate(D, q, 1)
        v = divisor_coordinate(D, q, 2)
        for a in range(1, min(8, D + 1)):
            # The coprimality gate belongs to the reduced representation.
            from math import gcd

            if gcd(a, q) != 1:
                continue
            direct_one = sum(
                (Fraction(mobius(q * g), a * g) for g in range(1, D // q + 1)),
                Fraction(0),
            )
            direct_two = sum(
                (
                    Fraction(mobius(q * g), a * a * g * g)
                    for g in range(1, D // q + 1)
                ),
                Fraction(0),
            )
            if direct_one != Fraction(q, a) * u:
                raise VerificationError("first reduced coefficient identity failed")
            if direct_two != Fraction(q * q, a * a) * v:
                raise VerificationError("second reduced coefficient identity failed")
            checks += 2
    return checks


def bohr_energy(D: int) -> Fraction:
    total = Fraction(0)
    for q in range(1, D + 1):
        u = divisor_coordinate(D, q, 1)
        v = divisor_coordinate(D, q, 2)
        total += Fraction(jordan(q, 2), 12) * u * u
        total += Fraction(jordan(q, 4), 180) * v * v
    return total


def add_poly(left: tuple[Fraction, ...], right: tuple[Fraction, ...]):
    return tuple(a + b for a, b in zip(left, right))


def integrate_square(poly: tuple[Fraction, Fraction, Fraction], a: int, b: int):
    coeff = [Fraction(0)] * 5
    for i, x in enumerate(poly):
        for j, y in enumerate(poly):
            coeff[i + j] += x * y
    return sum(
        (
            c * Fraction(b ** (degree + 1) - a ** (degree + 1), degree + 1)
            for degree, c in enumerate(coeff)
        ),
        Fraction(0),
    )


def truncated_local_energy(D: int) -> Fraction:
    """Exact integral of |S_D|^2 over [D,2D].

    On every unit cell no interior d-lattice breakpoint occurs, so S_D is one
    exact quadratic polynomial and its square integrates rationally.
    """
    total = Fraction(0)
    for cell in range(D, 2 * D):
        poly = (Fraction(0), Fraction(0), Fraction(0))
        for d in range(1, D + 1):
            mu = mobius(d)
            if mu == 0:
                continue
            quotient = cell // d
            term = (
                Fraction(quotient * quotient, 1) - Fraction(1, 3),
                Fraction(-2 * quotient, d),
                Fraction(1, d * d),
            )
            poly = add_poly(poly, tuple(mu * x for x in term))
        total += integrate_square(poly, cell, cell + 1)
    return total


def canonical_sha(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    if certificate.get("schema") != SCHEMA:
        raise VerificationError("schema mismatch")
    max_D = integer(certificate.get("max_D"), "max_D")
    if not 1 <= max_D <= 64:
        raise VerificationError("max_D outside exact regression range")
    ratio_upper = rational(certificate.get("ratio_upper"), "ratio_upper")
    if ratio_upper <= 0:
        raise VerificationError("ratio_upper must be positive")

    rows = []
    maximum = (Fraction(-1), -1)
    coefficient_checks = 0
    for D in range(1, max_D + 1):
        coefficient_checks += check_reduced_coefficient_formula(D)
        bohr = bohr_energy(D)
        local = truncated_local_energy(D)
        if bohr <= 0:
            raise VerificationError("Bohr energy is not positive")
        ratio = local / (D * bohr)
        if ratio > ratio_upper:
            raise VerificationError(f"finite local/Bohr ratio fails at D={D}")
        if ratio > maximum[0]:
            maximum = (ratio, D)
        rows.append(
            {
                "D": D,
                "local_energy": str(local),
                "bohr_energy": str(bohr),
                "ratio": str(ratio),
            }
        )

    expected_D = integer(certificate.get("expected_max_D"), "expected_max_D")
    expected_ratio = rational(
        certificate.get("expected_max_ratio"), "expected_max_ratio"
    )
    if maximum != (expected_ratio, expected_D):
        raise VerificationError("maximum finite ratio does not match certificate")

    proof = {
        "schema": SCHEMA,
        "classification": "EXACT_FINITE_REGRESSION_ONLY",
        "max_D": max_D,
        "ratio_upper": str(ratio_upper),
        "maximum_ratio": str(maximum[0]),
        "maximum_ratio_D": maximum[1],
        "coefficient_identity_checks": coefficient_checks,
        "rows": rows,
        "proof_boundary": (
            "This verifies exact reduced coefficients, the Jordan Bohr energy, "
            "and small-D physical integrals for the truncated centered packet. "
            "It does not verify the completed endpoint cancellation or the "
            "uniform Farey operator estimate in T-22801."
        ),
    }
    proof["proof_object_sha256"] = canonical_sha(proof)
    return proof


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(certificate)
        code = 0
    except (OSError, json.JSONDecodeError, VerificationError) as exc:
        result = {"schema": SCHEMA, "classification": "REJECTED", "reason": str(exc)}
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
