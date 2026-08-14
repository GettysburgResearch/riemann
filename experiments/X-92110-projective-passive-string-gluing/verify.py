#!/usr/bin/env python3
"""Exact regression checks for L-92110/R-92110.

This verifier checks finite rational identities illustrating the compactness
normalization, a positive atomic truncation family with an exact tail bound,
and the scalar-structure firewall. It does not construct the Xi string and
does not prove RH.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Dict, List


def prod(values):
    out = Fraction(1)
    for value in values:
        out *= value
    return out


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def atomic_value(z: Fraction, a: Fraction, b: Fraction, atoms: List[tuple[Fraction, Fraction]]) -> Fraction:
    out = a / z + b
    for mass, location in atoms:
        out += mass / (z + location)
    return out


def run() -> Dict[str, object]:
    checks = 0
    anchor = Fraction(2)
    a = Fraction(3, 7)
    b = Fraction(2, 9)
    atoms = [
        (Fraction(5, 4), Fraction(3)),
        (Fraction(7, 5), Fraction(11, 2)),
        (Fraction(9, 8), Fraction(13)),
    ]
    anchor_value = atomic_value(anchor, a, b, atoms)
    weighted_mass = sum(m / (anchor + s) for m, s in atoms)
    assert anchor_value == a / anchor + b + weighted_mass
    checks += 1

    kernel_checks = 0
    for z in map(Fraction, [1, 3, 5, 8, 13]):
        for mass, location in atoms:
            lhs = mass / (z + location)
            rhs = (anchor + location) / (z + location) * (mass / (anchor + location))
            assert lhs == rhs
            checks += 1
            kernel_checks += 1

    truncation_checks = 0
    monotone_checks = 0
    previous: Dict[Fraction, Fraction] = {}
    nodes = list(map(Fraction, [1, 2, 3, 5, 8]))
    for n in range(1, 17):
        current: Dict[Fraction, Fraction] = {}
        for q in nodes:
            value = sum(Fraction(1, 2**k) / (q + k) for k in range(1, n + 1))
            current[q] = value
            tail_bound = Fraction(1, 2**n) / (q + n + 1)
            finite_tail = sum(Fraction(1, 2**k) / (q + k) for k in range(n + 1, n + 81))
            assert finite_tail < tail_bound
            assert value <= Fraction(1)
            checks += 2
            truncation_checks += 2
            if q in previous:
                assert value > previous[q]
                checks += 1
                monotone_checks += 1
        previous = current

    dual_checks = 0
    qnodes = [Fraction(1), Fraction(2), Fraction(4)]
    coeffs = [Fraction(1), Fraction(-1), Fraction(0)]
    r = qnodes[0]
    for sval in map(Fraction, [0, 1, 3, 7, 19]):
        h = sum(c * (r + sval) / (q + sval) for c, q in zip(coeffs, qnodes))
        denom = Fraction(1)
        for q in qnodes:
            denom *= q + sval
        poly = (r + sval) * sum(
            coeffs[j] * prod(qnodes[i] + sval for i in range(len(qnodes)) if i != j)
            for j in range(len(qnodes))
        )
        assert h == poly / denom
        assert h > 0
        checks += 2
        dual_checks += 2

    moment_atoms = [(Fraction(2, 3), Fraction(0)), (Fraction(5, 7), Fraction(6))]
    moments = [sum(w * (r + s) / (q + s) for w, s in moment_atoms) for q in qnodes]
    assert moments[0] == sum(w for w, _ in moment_atoms)
    assert sum(c * y for c, y in zip(coeffs, moments)) >= 0
    checks += 2

    x1, x2 = Fraction(1), Fraction(2)
    f1, f2 = Fraction(1), Fraction(2)
    forced_offdiag = (f1 + f2) / (x1 + x2)
    assert forced_offdiag == 1
    assert forced_offdiag != 0
    checks += 2

    return {
        "verdict": "PASS_PROJECTIVE_PASSIVE_STRING_GLUING",
        "rh_proved": False,
        "checks": checks,
        "anchor": fstr(anchor),
        "anchor_value": fstr(anchor_value),
        "weighted_measure_mass": fstr(weighted_mass),
        "kernel_ratio_checks": kernel_checks,
        "truncation_tail_checks": truncation_checks,
        "truncation_monotonicity_checks": monotone_checks,
        "finite_string_dual_checks": dual_checks,
        "scalar_firewall_forced_offdiagonal": fstr(forced_offdiag),
        "scope": "exact finite regression only; no Xi string constructed",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
