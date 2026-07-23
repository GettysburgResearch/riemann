#!/usr/bin/env python3
"""Exact verifier for powered shared-budget Robin tail envelopes.

This module uses only Python integers and fractions.Fraction. It reconstructs
all proof values and never trusts a floating optimizer or a supplied DP table.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


SCHEMA = "riemann.robin-powered-tail.v1"


class CertificateError(ValueError):
    """Raised when a certificate is malformed or internally inconsistent."""


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
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller--Rabin for 0 <= n < 2^64."""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p
    if n >= 1 << 64:
        raise CertificateError("prime exceeds the verifier's 64-bit contract")

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Deterministic for unsigned 64-bit integers.
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        a = base % n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(after: int) -> int:
    candidate = max(2, after + 1)
    if candidate > 2 and candidate % 2 == 0:
        candidate += 1
    while not is_prime_u64(candidate):
        candidate += 1 if candidate == 2 else 2
    return candidate


def abundancy_prime_power(p: int, exponent: int) -> Fraction:
    if exponent < 0:
        raise CertificateError("prime-power exponent must be nonnegative")
    return Fraction(p ** (exponent + 1) - 1, p**exponent * (p - 1))


def validate_canonical_data(
    prefix_factors: list[tuple[int, int]], tail_primes: list[int]
) -> None:
    if not prefix_factors:
        raise CertificateError("prefix_factors must be nonempty")
    if not tail_primes:
        raise CertificateError("tail_primes must be nonempty")

    exponents = [exponent for _, exponent in prefix_factors]
    if any(exponent < 1 for exponent in exponents):
        raise CertificateError("prefix exponents must be positive")
    if any(left < right for left, right in zip(exponents, exponents[1:])):
        raise CertificateError("prefix exponents must be nonincreasing")

    primes = [p for p, _ in prefix_factors] + tail_primes
    for index, p in enumerate(primes):
        if not is_prime_u64(p):
            raise CertificateError(f"factor {p} is not prime")
        if index == 0:
            if p != 2:
                raise CertificateError("canonical support must start at prime 2")
        else:
            expected = next_prime(primes[index - 1])
            if p != expected:
                raise CertificateError(
                    f"canonical support gap: expected {expected}, received {p}"
                )


def compute_caps(
    tail_primes: list[int], max_tail_exponent: int, residual_increment_budget: int
) -> list[int]:
    caps: list[int] = []
    for p in tail_primes:
        exponent = 1
        # b is licensed exactly when p^(b-1) <= M0.
        while exponent < max_tail_exponent and p**exponent <= residual_increment_budget:
            exponent += 1
        caps.append(exponent)
    if any(left < right for left, right in zip(caps, caps[1:])):
        raise AssertionError("derived caps must be nonincreasing")
    return caps


def compute_envelope(
    prefix_factors: list[tuple[int, int]],
    tail_primes: list[int],
    integer_bound: int,
    a: int,
    d: int,
) -> dict[str, Any]:
    validate_canonical_data(prefix_factors, tail_primes)
    if integer_bound < 1:
        raise CertificateError("integer_bound must be positive")
    if a < 0:
        raise CertificateError("dual.a must be nonnegative")
    if d < 1:
        raise CertificateError("dual.d must be positive")

    prefix_value = product(p**exponent for p, exponent in prefix_factors)
    prefix_abundancy = Fraction(1)
    for p, exponent in prefix_factors:
        prefix_abundancy *= abundancy_prime_power(p, exponent)

    max_tail_exponent = prefix_factors[-1][1]
    tail_baseline = product(tail_primes)
    if prefix_value * tail_baseline > integer_bound:
        raise CertificateError("mandatory tail already exceeds integer_bound")

    tail_budget = integer_bound // prefix_value
    residual_increment_budget = tail_budget // tail_baseline
    caps = compute_caps(
        tail_primes, max_tail_exponent, residual_increment_budget
    )

    tail_baseline_abundancy = Fraction(1)
    for p in tail_primes:
        tail_baseline_abundancy *= abundancy_prime_power(p, 1)
    base_abundancy = prefix_abundancy * tail_baseline_abundancy

    n = len(tail_primes)
    prefix_products = [1]
    for p in tail_primes:
        prefix_products.append(prefix_products[-1] * p)

    next_values = [Fraction(1) for _ in range(n + 1)]
    argmax_rows: dict[str, list[int]] = {}

    for level in range(max_tail_exponent, 1, -1):
        licensed_length = sum(1 for cap in caps if cap >= level)
        level_gain = Fraction(1)
        candidates: list[Fraction] = []
        for length in range(licensed_length + 1):
            if length:
                p = tail_primes[length - 1]
                level_gain *= (
                    abundancy_prime_power(p, level)
                    / abundancy_prime_power(p, level - 1)
                )
            weight = level_gain**d / Fraction(prefix_products[length] ** a, 1)
            candidates.append(weight * next_values[length])

        row: list[Fraction] = []
        row_argmax: list[int] = []
        current = candidates[0]
        current_argmax = 0
        for previous_length in range(n + 1):
            if (
                previous_length <= licensed_length
                and candidates[previous_length] > current
            ):
                current = candidates[previous_length]
                current_argmax = previous_length
            row.append(current)
            row_argmax.append(current_argmax)
        next_values = row
        argmax_rows[str(level)] = row_argmax

    dynamic_value = next_values[n] if max_tail_exponent >= 2 else Fraction(1)
    powered_bound = (
        base_abundancy**d
        * Fraction(residual_increment_budget**a, 1)
        * dynamic_value
    )

    separate_ceiling = prefix_abundancy
    for p, cap in zip(tail_primes, caps):
        separate_ceiling *= abundancy_prime_power(p, cap)
    separate_power = separate_ceiling**d
    joint_power = min(powered_bound, separate_power)

    return {
        "prefix_value": prefix_value,
        "prefix_abundancy": prefix_abundancy,
        "tail_baseline": tail_baseline,
        "tail_budget": tail_budget,
        "residual_increment_budget": residual_increment_budget,
        "caps": caps,
        "base_abundancy": base_abundancy,
        "dynamic_value": dynamic_value,
        "powered_bound": powered_bound,
        "separate_ceiling": separate_ceiling,
        "separate_power": separate_power,
        "joint_power": joint_power,
        "argmax_rows": argmax_rows,
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    prefix_raw = data.get("prefix_factors")
    if not isinstance(prefix_raw, list):
        raise CertificateError("prefix_factors must be an array")
    prefix_factors: list[tuple[int, int]] = []
    for index, item in enumerate(prefix_raw):
        if not isinstance(item, dict):
            raise CertificateError(f"prefix_factors[{index}] must be an object")
        prefix_factors.append(
            (
                parse_int(item.get("prime"), f"prefix_factors[{index}].prime"),
                parse_int(
                    item.get("exponent"),
                    f"prefix_factors[{index}].exponent",
                ),
            )
        )

    tail_raw = data.get("tail_primes")
    if not isinstance(tail_raw, list):
        raise CertificateError("tail_primes must be an array")
    tail_primes = [
        parse_int(value, f"tail_primes[{index}]")
        for index, value in enumerate(tail_raw)
    ]

    integer_bound = parse_int(data.get("integer_bound"), "integer_bound")
    dual = data.get("dual")
    if not isinstance(dual, dict):
        raise CertificateError("dual must be an object")
    a = parse_int(dual.get("a"), "dual.a")
    d = parse_int(dual.get("d"), "dual.d")
    target_lower = parse_fraction(data.get("target_lower"), "target_lower")
    if target_lower <= 0:
        raise CertificateError("target_lower must be positive")

    result = compute_envelope(prefix_factors, tail_primes, integer_bound, a, d)
    target_power = target_lower**d
    computed_status = (
        "CERTIFIED_PRUNE"
        if result["joint_power"] < target_power
        else "UNRESOLVED"
    )

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    claimed_caps = claimed.get("caps")
    if claimed_caps != result["caps"]:
        raise CertificateError("claimed caps do not match exact reconstruction")
    if parse_fraction(
        claimed.get("separate_ceiling"), "claimed.separate_ceiling"
    ) != result["separate_ceiling"]:
        raise CertificateError("claimed separate ceiling mismatch")
    if parse_fraction(
        claimed.get("powered_bound"), "claimed.powered_bound"
    ) != result["powered_bound"]:
        raise CertificateError("claimed powered bound mismatch")
    if parse_fraction(
        claimed.get("joint_power"), "claimed.joint_power"
    ) != result["joint_power"]:
        raise CertificateError("claimed joint powered bound mismatch")
    if claimed.get("status") != computed_status:
        raise CertificateError("claimed status mismatch")

    return {
        "schema": SCHEMA,
        "status": computed_status,
        "caps": result["caps"],
        "residual_increment_budget": str(
            result["residual_increment_budget"]
        ),
        "separate_ceiling": fraction_json(result["separate_ceiling"]),
        "separate_alone_prunes": result["separate_ceiling"] < target_lower,
        "powered_bound": fraction_json(result["powered_bound"]),
        "powered_strictly_improves_separate": (
            result["powered_bound"] < result["separate_power"]
        ),
        "joint_power": fraction_json(result["joint_power"]),
        "target_power": fraction_json(target_power),
        "argmax_rows": result["argmax_rows"],
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)

    try:
        result = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(
            json.dumps(
                {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)},
                sort_keys=True,
            )
        )
        return 2

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
