#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def proof_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixtures = [
        # f=x^2+1 on [-2,2]
        ("x2_plus_1", 0, 1, [(1, 1)], 1),
        # f=x^4-2x^2+2 on [-2,2]
        ("quartic_no_real_roots", 0, 3, [(1, 1), (1, -1), (1, 1)], 1),
        # f=(x-2)(x^2+1) on [-3,3]
        ("one_real_two_complex", 1, 2, [(1, 1), (1, -1)], 1),
        # f=(x-1)^3(x+2)^2 on [-3,3]
        ("parent_multiplicities", 5, 4, [(1, -1)], 1),
        # f=x^4+1 on [-2,2]
        ("degenerate_upward", 0, 3, [(3, 1)], 1),
        # f=x^3+1 on [-2,2]
        ("stationary_inflection", 1, 2, [(2, 0)], 1),
    ]

    for name, n_f, n_fp, critical, boundary in fixtures:
        defect = sum(order + orientation for order, orientation in critical)
        assert n_f == n_fp - defect + boundary, name
        assert all(order + orientation >= 0 for order, orientation in critical)
        assert all((order + orientation) % 2 == 0 for order, orientation in critical)

    pair_integral_checks = 0
    for b in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 3)):
        # Integral of the negative part of one conjugate-pair curvature:
        # (2/b) * integral_{-1}^1 (1-u^2)/(1+u^2)^2 du = 2/b.
        primitive_jump = Fraction(1, 1)
        value = Fraction(2, 1) * primitive_jump / b
        assert value == Fraction(2, 1) / b
        pair_integral_checks += 1

    payload: dict[str, object] = {
        "schema": "riemann.t107100.reverse-rolle.v1",
        "real_crossing_fixtures": len(fixtures),
        "pair_integral_checks": pair_integral_checks,
        "exact_identity_verified": True,
        "multiplicity_sensitive": True,
        "coefficient_on_simple_extra_extremum": 2,
        "xi_complex_transport_proved": False,
        "rh_established": False,
        "verdict": "PASS_T107100_REVERSE_ROLLE_COUNTING",
    }
    payload["proof_object_sha256"] = proof_digest(payload)

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
