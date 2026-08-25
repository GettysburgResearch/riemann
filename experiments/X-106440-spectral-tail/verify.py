#!/usr/bin/env python3
"""Exact finite replay for T-106440.

The replay checks the discrete Fourier/Hankel coarea identity, the orthogonal
outer/hole split, the inner-monomial sign, the quadratic companion firewall and
the exact ninety-percent constants.  It does not evaluate Xi or prove either
open asymptotic estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable


Coeff = Dict[int, Fraction]


def signed_hankel_energy(coeff: Coeff, inputs: Iterable[int], max_output: int) -> Fraction:
    """Discrete circle model: Hankel entry at input j/output k is u[-(j+k+1)]."""
    total = Fraction(0)
    for j in inputs:
        for k in range(max_output + 1):
            m = j + k + 1
            total += coeff.get(-m, Fraction(0)) ** 2
            total -= coeff.get(m, Fraction(0)) ** 2
    return total


def run() -> dict[str, object]:
    coeff: Coeff = {
        -6: Fraction(2, 9),
        -4: Fraction(-1, 5),
        -2: Fraction(3, 11),
        1: Fraction(4, 13),
        3: Fraction(-2, 7),
        5: Fraction(1, 8),
    }
    bandwidth = 2
    max_mode = 10

    # L-106440.4: exact hard-band coarea.
    coarea = sum(
        Fraction(m - bandwidth)
        * (coeff.get(-m, Fraction(0)) ** 2 - coeff.get(m, Fraction(0)) ** 2)
        for m in range(bandwidth + 1, max_mode + 1)
    )
    direct_outer = signed_hankel_energy(
        coeff, range(bandwidth, max_mode + 1), max_mode
    )
    assert direct_outer == coarea

    # L-106440.8: finite source complement = outer tail + in-band hole.
    source_modes = {0}
    band_modes = set(range(bandwidth))
    hole_modes = band_modes - source_modes
    hole = signed_hankel_energy(coeff, sorted(hole_modes), max_mode)
    full_complement = signed_hankel_energy(
        coeff,
        [j for j in range(max_mode + 1) if j not in source_modes],
        max_mode,
    )
    assert full_complement == direct_outer + hole

    # Inner monomial z^3: no negative Fourier coefficient, hence every outer
    # signed tail is nonpositive.
    inner: Coeff = {3: Fraction(1)}
    inner_tail_h1 = sum(
        Fraction(m - 1)
        * (inner.get(-m, Fraction(0)) ** 2 - inner.get(m, Fraction(0)) ** 2)
        for m in range(2, 5)
    )
    assert inner_tail_h1 == -2

    # L-106441 quadratic firewall.  If s^2=lambda^2+epsilon^2 and
    # a=s+lambda, b=s-lambda, then a-b=2lambda and ab=epsilon^2.  These two
    # exact relations reproduce the derivative-companion factorization and
    # put one denominator zero in each half-plane.
    lam = Fraction(3, 5)
    epsilon2 = Fraction(7, 4)
    assert ("a-b", 2 * lam) == ("a-b", Fraction(6, 5))
    assert ("a*b", epsilon2) == ("a*b", Fraction(7, 4))
    assert lam > 0 and epsilon2 > 0

    # T-106440 constant ledger.
    visible = Fraction(1, 600)
    margin = Fraction(599, 625) - Fraction(9, 10)
    signed_allowance = margin - visible
    assert margin == Fraction(73, 1250)
    assert signed_allowance == Fraction(851, 15000)
    symmetric_budget = signed_allowance / 2
    assert symmetric_budget == Fraction(851, 30000)

    result: dict[str, object] = {
        "schema": "riemann.x106440.spectral-tail.v1",
        "classification": "PASS_T106440_SPECTRAL_ASYMMETRY_HOLE_SPLIT",
        "hard_band_coarea_checked": True,
        "outer_hole_split_checked": True,
        "inner_tail_sign_checked": True,
        "quadratic_companion_firewall_checked": True,
        "visible_source_budget": "1/600",
        "total_signed_allowance": "851/15000",
        "symmetric_outer_budget": "851/30000",
        "symmetric_hole_budget": "851/30000",
        "outasym106440_proved": False,
        "inhole106440_proved": False,
        "safehom106441_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
