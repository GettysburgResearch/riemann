#!/usr/bin/env python3
"""Exact checker for the normalized triangular pole-free window algebra."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15405-triangular-window.synthetic.v1"


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


def convolve(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def triangular(t: Fraction) -> Fraction:
    if t < 0 or t > 2:
        return Fraction(0)
    if t <= 1:
        return t
    return 2 - t


def pole_free(t: Fraction, q: Fraction) -> Fraction:
    return triangular(t) - q * triangular(t - 1)


def integrate_linear_square(a: Fraction, b: Fraction, lo: Fraction, hi: Fraction) -> Fraction:
    return (
        a * a * (hi**3 - lo**3) / 3
        + a * b * (hi**2 - lo**2)
        + b * b * (hi - lo)
    )


def hinge(x: Fraction) -> Fraction:
    return max(Fraction(0), x)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    q = frac(data.get("q"), "q")
    if q != 2:
        raise CertificateError("this certificate fixes q=2")

    coeff = convolve([Fraction(1), -2, 1], [Fraction(1), -q])
    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    raw_coeff = claimed.get("difference_coefficients")
    if not isinstance(raw_coeff, list) or len(raw_coeff) != 4:
        raise CertificateError("difference_coefficients must have length four")
    if [frac(v, f"difference_coefficients[{i}]") for i, v in enumerate(raw_coeff)] != coeff:
        raise CertificateError("difference coefficient mismatch")

    if sum(coeff) != 0 or sum(Fraction(i) * c for i, c in enumerate(coeff)) != 0:
        raise CertificateError("double root at one failed")
    pole_root = Fraction(1, 2)
    pole_value = sum(c * pole_root**i for i, c in enumerate(coeff))
    if pole_value != 0:
        raise CertificateError("pole root failed")

    norm = (
        integrate_linear_square(1, 0, Fraction(0), Fraction(1))
        + integrate_linear_square(-3, 4, Fraction(1), Fraction(2))
        + integrate_linear_square(2, -6, Fraction(2), Fraction(3))
    )
    if frac(claimed.get("normalized_l2_square"), "claimed.normalized_l2_square") != norm:
        raise CertificateError("normalized L2 square mismatch")

    events_raw = data.get("events")
    if not isinstance(events_raw, list) or not events_raw:
        raise CertificateError("events must be a nonempty array")
    events: list[tuple[Fraction, Fraction]] = []
    for i, item in enumerate(events_raw):
        if not isinstance(item, dict):
            raise CertificateError(f"events[{i}] must be an object")
        position = frac(item.get("position"), f"events[{i}].position")
        weight = frac(item.get("weight"), f"events[{i}].weight")
        if weight <= 0:
            raise CertificateError("event weights must be positive")
        events.append((position, weight))

    x = frac(data.get("evaluation_x"), "evaluation_x")
    direct = sum(w * pole_free(x - p, q) for p, w in events)

    def cumulative(y: Fraction) -> Fraction:
        return sum(w * hinge(y - p) for p, w in events)

    finite_difference = sum(coeff[k] * cumulative(x - k) for k in range(4))
    if direct != finite_difference:
        raise CertificateError("direct and finite-difference evaluations disagree")
    if frac(claimed.get("evaluation"), "claimed.evaluation") != direct:
        raise CertificateError("claimed evaluation mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_SYNTHETIC_TRIANGULAR_WINDOW_ALGEBRA",
        "difference_coefficients": [fj(c) for c in coeff],
        "constant_root": fj(sum(coeff)),
        "linear_root": fj(sum(Fraction(i) * c for i, c in enumerate(coeff))),
        "pole_root_value": fj(pole_value),
        "normalized_l2_square": fj(norm),
        "direct_evaluation": fj(direct),
        "finite_difference_evaluation": fj(finite_difference),
        "proof_boundary": "finite rational window algebra only; no zeta or prime computation",
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
