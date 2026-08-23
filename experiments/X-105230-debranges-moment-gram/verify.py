#!/usr/bin/env python3
"""Exact fixtures for L-105224/T-105230.

This replay checks Gaussian-rational safe-pole and sampling algebra. It does not
machine-prove the finite de Branges integral formula or any entire-Xi passage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Tuple

GR = Tuple[F, F]


def z(a=0, b=0) -> GR:
    return (F(a), F(b))


def sub(x: GR, y: GR) -> GR:
    return (x[0] - y[0], x[1] - y[1])


def mul(x: GR, y: GR) -> GR:
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def inv(x: GR) -> GR:
    d = x[0] * x[0] + x[1] * x[1]
    assert d
    return (x[0] / d, -x[1] / d)


def div(x: GR, y: GR) -> GR:
    return mul(x, inv(y))


def scale(x: GR, q: F) -> GR:
    return (x[0] * q, x[1] * q)


def abs2(x: GR) -> F:
    return x[0] * x[0] + x[1] * x[1]


def g_at(x: F) -> GR:
    out = z(6)
    for h in (1, 2, 3):
        out = div(out, z(x, h))
    return out


def verify() -> dict:
    lambdas = [z(0, -h) for h in (1, 2, 3)]
    gammas = []
    for j, lam in enumerate(lambdas):
        den = z(1)
        for r, other in enumerate(lambdas):
            if r != j:
                den = mul(den, sub(lam, other))
        gammas.append(div(z(6), den))
    assert gammas == [z(-3), z(6), z(-3)]

    gm = g_at(F(-1))
    gp = g_at(F(1))
    assert gm == z(F(3, 5))
    assert gp == z(F(-3, 5))
    assert abs2(gm) == abs2(gp) == F(9, 25)

    def fixture(C: int) -> dict:
        samples = []
        for x in (-1, 1):
            px = F(x**3 - 3*x + C)
            gprime = F(6*x)
            gx = g_at(F(x))
            rho = px / gprime
            u = scale(gx, gprime)
            v = scale(gx, px)
            samples.append((gx, rho, u, v, gprime))

        N = sum(abs2(t[0]) for t in samples)
        A = -sum(abs2(t[0]) * t[1] for t in samples)
        B = sum(abs2(t[0]) * t[1] * t[1] for t in samples)

        U2 = sum(abs2(t[2]) / (t[4] * t[4]) for t in samples)
        V2 = sum(abs2(t[3]) / (t[4] * t[4]) for t in samples)
        cross = sum(
            mul(t[3], (t[2][0], -t[2][1]))[0] / (t[4] * t[4])
            for t in samples
        )
        assert U2 == N
        assert V2 == B
        assert cross == -A
        assert N * B - A * A == U2 * V2 - cross * cross
        return {
            "C": C,
            "N": str(N),
            "A": str(A),
            "B": str(B),
            "defect": str(N * B - A * A),
        }

    coherent = fixture(0)
    offset = fixture(1)
    assert coherent == {
        "C": 0, "N": "18/25", "A": "6/25",
        "B": "2/25", "defect": "0",
    }
    assert offset == {
        "C": 1, "N": "18/25", "A": "6/25",
        "B": "1/10", "defect": "9/625",
    }

    payload = {
        "schema": "riemann.x105230.debranges_gram.v1",
        "classification": "PASS_T105230_DEBRANGES_MOMENT_GRAM_FIXTURES",
        "arithmetic": "EXACT_GAUSSIAN_RATIONAL",
        "verified": {
            "safe_pole_residues": ["-3", "6", "-3"],
            "safe_weight_at_pm1": "9/25",
            "sampling_norm_count": True,
            "sampling_norm_second_moment": True,
            "sampling_cross_first_moment": True,
            "wedge_defect_identity": True,
        },
        "fixtures": [coherent, offset],
        "finite_debranges_integral_machine_proved": False,
        "entire_xi_exhaustion_proved": False,
        "dbae105230_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = verify()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
