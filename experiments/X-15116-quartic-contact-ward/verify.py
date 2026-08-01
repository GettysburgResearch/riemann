#!/usr/bin/env python3
"""Exact verifier for the quartic finite-jet contact Ward identity.

Uses only integers, fractions.Fraction, JSON, and SHA-256.  This is a finite
renormalization regression; it does not evaluate xi or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.quartic-contact-ward.v1"


def rat(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n = value["numerator"]
        d = value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator or denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational {value!r}")


def dump(value: Fraction) -> Any:
    if value.denominator == 1:
        return value.numerator
    return {"numerator": value.numerator, "denominator": value.denominator}


def moment(values: list[Fraction], order: int) -> Fraction:
    return sum(x ** order for x in values)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    raw = [rat(x) for x in data["raw_spectrum"]]
    ren = [rat(x) for x in data["renormalized_spectrum"]]
    if len(raw) != len(ren) or not raw:
        raise ValueError("spectra must have the same positive length")
    q4 = rat(data["linear_counterterm_order4"])

    pairs = data["grading_pairs"]
    if not isinstance(pairs, list) or len(pairs) * 2 != len(raw):
        raise ValueError("grading_pairs must partition the spectrum")
    seen: set[int] = set()
    for pair in pairs:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("malformed grading pair")
        i, j = pair
        if isinstance(i, bool) or isinstance(j, bool) or not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("grading indices must be integers")
        if i == j or i < 0 or j < 0 or i >= len(raw) or j >= len(raw):
            raise ValueError("invalid grading pair")
        if i in seen or j in seen:
            raise ValueError("grading pairs overlap")
        seen.update((i, j))
        if raw[i] != -raw[j] or ren[i] != -ren[j]:
            raise ValueError("grading does not anti-pair both spectra")
    if seen != set(range(len(raw))):
        raise ValueError("grading pairs do not cover the spectrum")

    counter = [a - k for a, k in zip(raw, ren)]
    for i, j in pairs:
        if counter[i] != -counter[j]:
            raise ValueError("counterterm breaks the grading")

    raw2 = moment(raw, 2)
    ren2 = moment(ren, 2)
    raw3 = moment(raw, 3)
    ren3 = moment(ren, 3)
    raw4 = moment(raw, 4)
    ren4 = moment(ren, 4)
    if raw2 != ren2:
        raise ValueError("quadratic lower gate does not match")
    if raw3 != 0 or ren3 != 0 or moment(counter, 3) != 0:
        raise ValueError("cubic parity gate fails")

    a3d = sum(a ** 3 * d for a, d in zip(raw, counter))
    a2d2 = sum(a ** 2 * d ** 2 for a, d in zip(raw, counter))
    ad3 = sum(a * d ** 3 for a, d in zip(raw, counter))
    d4 = moment(counter, 4)

    # The matrices are diagonal in this exact control, so the general
    # noncommutative order-four formula reduces to the binomial trace formula.
    required_q4 = 4 * a3d - 6 * a2d2 + 4 * ad3 - d4
    scalar4 = raw4 - q4
    defect = scalar4 - ren4
    if defect != required_q4 - q4:
        raise ValueError("internal quartic contact identity failed")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    status = (
        "CERTIFIED_CONTACT_FREE_QUARTIC_WARD"
        if defect == 0
        else "CERTIFIED_QUARTIC_CONTACT_ANOMALY"
    )
    return {
        "status": status,
        "dimension": len(raw),
        "raw_second_moment": dump(raw2),
        "renormalized_second_moment": dump(ren2),
        "raw_third_moment": dump(raw3),
        "renormalized_third_moment": dump(ren3),
        "raw_fourth_moment": dump(raw4),
        "renormalized_fourth_moment": dump(ren4),
        "trace_A3D": dump(a3d),
        "trace_A2D2": dump(a2d2),
        "trace_AD3": dump(ad3),
        "trace_D4": dump(d4),
        "supplied_linear_counterterm_order4": dump(q4),
        "required_nonlinear_counterterm_order4": dump(required_q4),
        "scalar_minus_cyclic_order4": dump(defect),
        "certificate_sha256": digest,
        "scope": "exact finite contact accounting only; no Riemann tensor identity",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
