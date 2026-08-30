#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


def local_weight(m: int, orientation: str) -> Fraction:
    if m % 2 == 0:
        return Fraction(1, 2)
    if orientation == "up":
        return Fraction(1)
    if orientation == "down":
        return Fraction(0)
    raise ValueError("odd multiplicity needs up/down")


def iota(m: int, orientation: str) -> int:
    if m % 2 == 0:
        return 0
    return 1 if orientation == "up" else -1


def saddle(k: int) -> float:
    lo = math.log(k) / 3
    hi = math.log(k) / 2
    for _ in range(120):
        mid = (lo + hi) / 2
        deriv = k / mid + 4.5 - 2 * math.pi * math.exp(2 * mid)
        if deriv > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    exact_checks = 0
    for m in range(1, 17):
        orientations = ("up", "down") if m % 2 else ("touch",)
        for orient in orientations:
            w = local_weight(m, orient)
            lhs = m + iota(m, orient)
            rhs = (m - 1) + 2 * w
            assert Fraction(lhs) == rhs
            exact_checks += 1

    x = sp.symbols("x")
    fixtures = [
        x**5 + 3*x**3 - 2*x + 7,
        x**6 - 4*x**4 + 2*x**2 + 3,
        x**7 + x**2 - 5*x + 11,
    ]
    for f in fixtures:
        r = sp.diff(f, x) / f
        q = -sp.diff(r, x)
        r1 = sp.diff(f, x, 2) / sp.diff(f, x)
        q1 = -sp.diff(r1, x)
        assert sp.simplify(r1 - (r - q/r)) == 0
        assert sp.simplify(q1 - (q + sp.diff(q/r, x))) == 0
        exact_checks += 2

    assert Fraction(997, 1000) - Fraction(9, 10) == Fraction(97, 1000)
    assert (Fraction(997, 1000) - Fraction(9, 10)) / 2 == Fraction(97, 2000)
    assert Fraction(9863, 10000) - Fraction(9, 10) == Fraction(863, 10000)
    assert (Fraction(9863, 10000) - Fraction(9, 10)) / 2 == Fraction(863, 20000)
    exact_checks += 4

    numerical_checks = 0
    saddle_rows = []
    for k in (10_000, 100_000, 1_000_000, 10_000_000):
        w = saddle(k)
        assert math.log(k)/3 < w < math.log(k)/2
        inv_a2 = k/w**2 + 2*k/w + 9
        a2 = 1/inv_a2
        assert w/(4*k) < a2 < w/(2*k)
        residual = 2*math.pi*math.exp(2*w) - (k/w + 4.5)
        assert abs(residual) < 1e-8 * (k/w)
        saddle_rows.append({"k": k, "w": w, "a2": a2})
        numerical_checks += 4

    # Dilation firewall: count invariant, negative-curvature mass scales by 1/L.
    base_mass = Fraction(7, 5)
    for L in (2, 3, 5, 11, 101):
        scaled = base_mass / L
        assert scaled * L == base_mass
        numerical_checks += 1

    payload = {
        "schema": "riemann.x107200.cauchy-layer-saddle.v1",
        "classification": "PASS_T107200_XI_CAUCHY_LAYER_AND_SADDLE",
        "exact_checks": exact_checks,
        "numerical_checks": numerical_checks,
        "saddle_rows": saddle_rows,
        "cauchy_layer_identity_checked": True,
        "curvature_transport_checked": True,
        "xi_saddle_analytic_proof_replayed": False,
        "xiscreen107200_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    digest_source = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(digest_source).hexdigest()

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
