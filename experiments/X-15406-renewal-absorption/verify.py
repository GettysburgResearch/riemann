#!/usr/bin/env python3
"""Exact finite checker for a von-Mangoldt-type renewal and absorption identity."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15406-renewal-absorption.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} must be a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    x = integer(data.get("window_center"), "window_center")
    raw_h = data.get("kernel")
    if not isinstance(raw_h, list) or not raw_h:
        raise CertificateError("kernel must be a nonempty array")
    H = [frac(v, f"kernel[{i}]") for i, v in enumerate(raw_h)]
    if any(v < 0 for v in H):
        raise CertificateError("kernel must be nonnegative")

    raw_primes = data.get("prime_generators")
    if not isinstance(raw_primes, list) or not raw_primes:
        raise CertificateError("prime_generators must be a nonempty array")
    primes: list[tuple[int, int]] = []
    seen_primes: set[int] = set()
    for i, item in enumerate(raw_primes):
        if not isinstance(item, dict):
            raise CertificateError(f"prime_generators[{i}] must be an object")
        p = integer(item.get("prime"), f"prime_generators[{i}].prime")
        ell = integer(item.get("log_weight"), f"prime_generators[{i}].log_weight")
        if p <= 1 or ell <= 0 or p in seen_primes:
            raise CertificateError("prime generators and log weights must be distinct positive data")
        seen_primes.add(p)
        primes.append((p, ell))

    raw_states = data.get("states")
    if not isinstance(raw_states, list) or not raw_states:
        raise CertificateError("states must be a nonempty array")
    states: list[tuple[int, tuple[int, ...], int]] = []
    state_by_value: dict[int, tuple[tuple[int, ...], int]] = {}
    for i, item in enumerate(raw_states):
        if not isinstance(item, dict):
            raise CertificateError(f"states[{i}] must be an object")
        exponents_raw = item.get("exponents")
        if not isinstance(exponents_raw, list) or len(exponents_raw) != len(primes):
            raise CertificateError("state exponent vector has wrong length")
        exponents = tuple(integer(v, f"states[{i}].exponents") for v in exponents_raw)
        if any(v < 0 for v in exponents):
            raise CertificateError("state exponents must be nonnegative")
        value = 1
        position = 0
        for (p, ell), exponent in zip(primes, exponents):
            value *= p**exponent
            position += ell * exponent
        if value in state_by_value:
            raise CertificateError("duplicate state")
        state_by_value[value] = (exponents, position)
        states.append((value, exponents, position))

    # Require every multiplicative state needed by the declared window.
    if 1 not in state_by_value:
        raise CertificateError("state 1 must be present")

    def kernel_at(position: int) -> Fraction:
        offset = x - position
        return H[offset] if 0 <= offset < len(H) else Fraction(0)

    # Prime-power measure mu and harmonic measure nu.
    mu: dict[int, Fraction] = {}
    for index, (p, ell) in enumerate(primes):
        for value, exponents, _ in states:
            if exponents[index] > 0 and sum(int(e > 0) for e in exponents) == 1:
                mu[value] = Fraction(ell, value)

    # Check the divisor normalization and renewal atom by atom.
    renewal: dict[int, Fraction] = {}
    for value, exponents, position in states:
        divisor_sum = Fraction(0)
        convolution = Fraction(0)
        for q, mu_q in mu.items():
            if value % q:
                continue
            residual = value // q
            if residual not in state_by_value:
                raise CertificateError("state set is not divisor closed")
            ell_q = mu_q * q
            divisor_sum += ell_q
            convolution += mu_q * Fraction(1, residual)
        if divisor_sum != position:
            raise CertificateError("von Mangoldt divisor normalization failed")
        expected = Fraction(position, value)
        if convolution != expected:
            raise CertificateError("renewal atom identity failed")
        renewal[value] = convolution

    A = sum(weight * kernel_at(state_by_value[q][1]) for q, weight in mu.items())
    Z = sum(Fraction(position, value) * kernel_at(position) for value, _, position in states)
    if Z <= 0:
        raise CertificateError("windowed starting mass must be positive")

    absorption_numerator = Fraction(0)
    for value, _, position in states:
        if position == 0:
            continue
        start_mass = Fraction(position, value) * kernel_at(position)
        lambda_value = mu.get(value, Fraction(0)) * value
        absorption_probability = lambda_value / position
        absorption_numerator += start_mass * absorption_probability
    if absorption_numerator != A:
        raise CertificateError("absorption numerator does not equal the positive primitive")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    if frac(claimed.get("primitive"), "claimed.primitive") != A:
        raise CertificateError("claimed primitive mismatch")
    if frac(claimed.get("starting_mass"), "claimed.starting_mass") != Z:
        raise CertificateError("claimed starting mass mismatch")
    probability = A / Z
    if frac(claimed.get("absorption_probability"), "claimed.absorption_probability") != probability:
        raise CertificateError("claimed absorption probability mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_SYNTHETIC_RENEWAL_ABSORPTION_IDENTITY",
        "state_count": len(states),
        "prime_power_count": len(mu),
        "primitive": fj(A),
        "starting_mass": fj(Z),
        "absorption_probability": fj(probability),
        "renewal_atoms": {str(n): fj(v) for n, v in sorted(renewal.items())},
        "proof_boundary": "finite rational divisibility model only; logarithmic weights are synthetic",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
