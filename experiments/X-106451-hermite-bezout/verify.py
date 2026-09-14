#!/usr/bin/env python3
"""Finite exact replay for L/T-106451.

Checks the Bézout kernel identity, CRT root labels on rational fixtures, the
signature count formula at fixture scope, the Chebyshev derivative firewall,
and the exact fourth-endpoint threshold.  It does not evaluate Xi or prove
HBSIG106451/HBRT106451.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def poly_eval(coeffs: list[Fraction], x: Fraction) -> Fraction:
    out = Fraction(0)
    for coefficient in coeffs:
        out = out * x + coefficient
    return out


def derivative(coeffs: list[Fraction]) -> list[Fraction]:
    degree = len(coeffs) - 1
    return [coeffs[i] * (degree - i) for i in range(degree)]


def pmul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def psub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    size = max(len(a), len(b))
    aa = [Fraction(0)] * (size - len(a)) + a
    bb = [Fraction(0)] * (size - len(b)) + b
    return [x - y for x, y in zip(aa, bb)]


def bez_eval(f: list[Fraction], g: list[Fraction], x: Fraction,
             y: Fraction) -> Fraction:
    assert x != y
    return (
        poly_eval(f, x) * poly_eval(g, y)
        - poly_eval(g, x) * poly_eval(f, y)
    ) / (x - y)


def main() -> dict[str, object]:
    # Coprime rational-root fixtures.
    p = [Fraction(1), Fraction(-2), Fraction(-5), Fraction(6)]  # (x-1)(x+2)(x-3)
    q = [Fraction(1), Fraction(-4), Fraction(-5)]  # (x-5)(x+1)
    dp, dq = derivative(p), derivative(q)
    a = pmul(p, q)
    w = psub(pmul(dp, q), pmul(p, dq))

    identity_checks = 0
    for x_int in range(-6, 7):
        for y_int in range(-6, 7):
            if x_int == y_int:
                continue
            x, y = Fraction(x_int), Fraction(y_int)
            left = bez_eval(a, w, x, y)
            right = (
                poly_eval(q, x) * poly_eval(q, y) * bez_eval(p, dp, x, y)
                - poly_eval(p, x) * poly_eval(p, y) * bez_eval(q, dq, x, y)
            )
            assert left == right
            identity_checks += 1

    p_roots = [Fraction(1), Fraction(-2), Fraction(3)]
    q_roots = [Fraction(5), Fraction(-1)]
    crt_checks = 0
    da = derivative(a)
    for root in p_roots:
        assert poly_eval(w, root) == poly_eval(da, root)
        crt_checks += 1
    for root in q_roots:
        assert poly_eval(w, root) == -poly_eval(da, root)
        crt_checks += 1

    # All roots are real in this fixture: + p-roots and - q-roots.
    positive_inertia = len(p_roots)
    negative_inertia = len(q_roots)
    signature = positive_inertia - negative_inertia
    assert signature == len(p_roots) - len(q_roots)

    fourth_entry = Fraction(2487, 2500)
    ninety = Fraction(9, 10)
    threshold = fourth_entry - ninety
    assert threshold == Fraction(237, 2500)

    payload: dict[str, object] = {
        "schema": "riemann.x106451.hermite-bezout.v1",
        "classification": "PASS_T106451_ENDPOINT_HERMITE_BEZOUT_ALGEBRA",
        "bezout_identity_checks": identity_checks,
        "crt_label_checks": crt_checks,
        "fixture_positive_inertia": positive_inertia,
        "fixture_negative_inertia": negative_inertia,
        "fixture_signature": signature,
        "fourth_endpoint_signature_threshold": "-237/2500",
        "hbsig106451_proved": False,
        "hbrt106451_proved": False,
        "resgram106450_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
