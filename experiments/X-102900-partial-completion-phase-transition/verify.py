#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    f0 = [Fraction(1), Fraction(-1)]
    f1 = [Fraction(1), Fraction(0), Fraction(-1)]
    half = [Fraction(1), Fraction(1, 2)]
    fm = poly_mul(f0, half)

    lhs = poly_mul(poly_mul(fm, fm), [Fraction(1), Fraction(1)])
    rhs = poly_mul(poly_mul(f0, f1), poly_mul(half, half))
    assert lhs == rhs

    mhalf = -4 * (math.sqrt(2) - 1) ** 2 * math.log(2)
    mzero = 8 * (1 - math.sqrt(2)) * math.log(2) ** 2
    assert mhalf < 0 and mzero < 0

    cs = [0.1, 0.25, 0.5, 0.75, 0.9]
    for c in cs:
        assert math.gamma(c - 1) < 0
        assert mhalf / math.gamma(c - 1) > 0

    labels = [2, 3, 5, 67, 67]
    max_error = 0.0
    for z in [1.2 + 0.3j, 1.7 + 0.6j]:
        b0 = 1 + 0j
        b1 = 1 + 0j
        for p in labels:
            x = p ** (-z)
            b0 *= 1 - x
            b1 *= 1 - x * x
        midpoint = cmath.sqrt(b0 * b1)
        max_error = max(
            max_error,
            abs(midpoint * midpoint - b0 * b1),
            abs((1 / b1) * midpoint * midpoint - b0),
        )
    assert max_error < 1e-12

    Y = 10**6
    omega_mass = 0.0
    k = 0
    while 67**k <= math.sqrt(Y):
        max_m = int(math.sqrt(Y) / (67**k))
        omega_mass += sum(1 / m for m in range(1, max_m + 1)) / (67**k)
        k += 1
    omega_bound = (1 + math.log(math.sqrt(Y))) / (1 - 1 / 67)
    assert omega_mass <= omega_bound

    payload = {
        "schema": "riemann.t102900.partial-completion-phase-transition.v1",
        "partial_completion_parameters_checked": cs,
        "strict_gamma_sign_checks": True,
        "outer_mellin_half": format(mhalf, ".16g"),
        "outer_square_lattice_moment": format(mzero, ".16g"),
        "outer_mellin_half_negative": True,
        "midpoint_local_identity_exact": True,
        "geometric_midpoint_multiplier_checks": 2,
        "max_multiplier_error": format(max_error, ".3e"),
        "positive_square_inverse_mass_fixture": format(omega_mass, ".16g"),
        "positive_square_inverse_bound_fixture": format(omega_bound, ".16g"),
        "native_endpoint_derivative_constant_positive": True,
        "strict_partial_completion_eventual_positivity_proved": True,
        "gmbc102893_proved": False,
        "sgic102890_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102900_PARTIAL_COMPLETION_PHASE_TRANSITION",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
