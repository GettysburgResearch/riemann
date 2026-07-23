#!/usr/bin/env python3
"""Exact-rational enclosure for alpha(T)=log(T/(2*pi))/(2*pi).

The proof backend uses only Python integers and fractions.Fraction. It encloses
pi by Machin's formula with alternating arctangent series and encloses real
logarithms by a positive atanh series after exact power-of-two range reduction.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.alpha-rational.v1"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def positive_fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if numerator <= 0 or denominator <= 0:
        raise CertificateError(f"{name} must be positive")
    return Fraction(numerator, denominator)


def arctan_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    if not 0 <= x <= 1:
        raise CertificateError("arctan series requires 0 <= x <= 1")
    if terms < 1:
        raise CertificateError("arctan term count must be positive")
    total = Fraction(0)
    power = x
    square = x * x
    for k in range(terms):
        term = power / (2 * k + 1)
        total = total + term if k % 2 == 0 else total - term
        power *= square
    next_term = power / (2 * terms + 1)
    adjacent = total + next_term if terms % 2 == 0 else total - next_term
    return min(total, adjacent), max(total, adjacent)


def pi_interval(atan5_terms: int, atan239_terms: int) -> tuple[Fraction, Fraction]:
    a5_lo, a5_hi = arctan_interval(Fraction(1, 5), atan5_terms)
    a239_lo, a239_hi = arctan_interval(Fraction(1, 239), atan239_terms)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


def floor_log2_fraction(x: Fraction) -> int:
    if x <= 0:
        raise CertificateError("logarithm argument must be positive")
    numerator, denominator = x.numerator, x.denominator
    k = numerator.bit_length() - denominator.bit_length()

    def power_at_most(j: int) -> bool:
        if j >= 0:
            return (denominator << j) <= numerator
        return denominator <= (numerator << (-j))

    while not power_at_most(k):
        k -= 1
    while power_at_most(k + 1):
        k += 1
    return k


def log_unit_interval(y: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    if not Fraction(1) <= y <= Fraction(2):
        raise CertificateError("range-reduced logarithm argument must lie in [1,2]")
    if terms < 1:
        raise CertificateError("log term count must be positive")
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += 2 * power / (2 * j + 1)
        power *= z2
    if z == 0:
        tail = Fraction(0)
    else:
        tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return partial, partial + tail


def log_fraction_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    k = floor_log2_fraction(x)
    y = x / (2**k) if k >= 0 else x * (2 ** (-k))
    log2_lo, log2_hi = log_unit_interval(Fraction(2), terms)
    y_lo, y_hi = log_unit_interval(y, terms)
    if k >= 0:
        return k * log2_lo + y_lo, k * log2_hi + y_hi
    return k * log2_hi + y_lo, k * log2_lo + y_hi


def divide_intervals(
    numerator: tuple[Fraction, Fraction], denominator: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    nlo, nhi = numerator
    dlo, dhi = denominator
    if dlo <= 0:
        raise CertificateError("division denominator interval must be positive")
    candidates = (nlo / dlo, nlo / dhi, nhi / dlo, nhi / dhi)
    return min(candidates), max(candidates)


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def fraction_json(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    carrier = positive_fraction(data.get("carrier"), "carrier")
    atan5_terms = exact_int(data.get("atan_1_5_terms"), "atan_1_5_terms")
    atan239_terms = exact_int(data.get("atan_1_239_terms"), "atan_1_239_terms")
    log_terms = exact_int(data.get("log_terms"), "log_terms")
    scale_bits = exact_int(data.get("output_scale_bits"), "output_scale_bits")
    if min(atan5_terms, atan239_terms, log_terms) < 1:
        raise CertificateError("all term counts must be positive")
    if scale_bits < 1 or scale_bits > 4096:
        raise CertificateError("output_scale_bits must lie in [1,4096]")

    pi_lo, pi_hi = pi_interval(atan5_terms, atan239_terms)
    if not (Fraction(3) < pi_lo < pi_hi < Fraction(4)):
        raise CertificateError("internal pi enclosure failed its sanity check")

    two_pi = (2 * pi_lo, 2 * pi_hi)
    x_interval = divide_intervals((carrier, carrier), two_pi)
    log_lo = log_fraction_interval(x_interval[0], log_terms)[0]
    log_hi = log_fraction_interval(x_interval[1], log_terms)[1]
    alpha_lo, alpha_hi = divide_intervals((log_lo, log_hi), two_pi)

    scale = 1 << scale_bits
    lower_num = floor_fraction(alpha_lo * scale)
    upper_num = ceil_fraction(alpha_hi * scale)
    if lower_num > upper_num:
        raise CertificateError("internal dyadic enclosure is inverted")

    return {
        "schema": SCHEMA,
        "carrier": fraction_json(carrier),
        "method": {
            "pi": "Machin formula with alternating arctangent enclosures",
            "log": "exact power-of-two range reduction and positive atanh series",
            "atan_1_5_terms": atan5_terms,
            "atan_1_239_terms": atan239_terms,
            "log_terms": log_terms,
        },
        "alpha_dyadic_interval": {
            "lower_num": lower_num,
            "upper_num": upper_num,
            "scale_bits": scale_bits,
        },
        "width_dyadic_units": upper_num - lower_num,
        "strictly_positive": lower_num > 0,
        "scope": "Exact enclosure of alpha(T) only; no prime sum or explicit-formula gate is checked.",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2))
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
