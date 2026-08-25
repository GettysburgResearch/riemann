#!/usr/bin/env python3
"""Exact replay for T-106610.

Checks finite rational polynomial fixtures, the coherence and projective-edge
inequalities, exact 90-percent constants, and the c+cos firewall algebra.
It does not evaluate Xi or prove RESCOH106610 / RESEDGE106610.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import argparse


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def derivative(a):
    return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]


def integrate(a, constant):
    return [Fraction(constant)] + [a[i] / Fraction(i + 1) for i in range(len(a))]


def evaluate(a, x):
    out = Fraction(0)
    for coefficient in reversed(a):
        out = out * x + coefficient
    return out


def rooted_polynomial(roots):
    out = [Fraction(1)]
    for root in roots:
        out = mul(out, [-Fraction(root), Fraction(1)])
    return out


def fifth_antiderivative(q, constants):
    out = q
    for constant in constants:
        out = integrate(out, Fraction(constant))
    return out


def check_fixture(roots, constants):
    q = rooted_polynomial(roots)
    f = fifth_antiderivative(q, constants)
    qp = derivative(q)

    residues = []
    parent_values = []
    qprime_values = []
    for root in roots:
        x = Fraction(root)
        parent = evaluate(f, x)
        qprime = evaluate(qp, x)
        assert qprime != 0
        residues.append(parent / qprime)
        parent_values.append(parent)
        qprime_values.append(qprime)

    for index in range(len(roots) - 1):
        assert qprime_values[index] * qprime_values[index + 1] < 0
        lhs = parent_values[index] * parent_values[index + 1] < 0
        rhs = residues[index] * residues[index + 1] > 0
        assert lhs == rhs

    transitions = sum(
        left * right < 0 for left, right in zip(residues, residues[1:])
    )
    same_sign = len(residues) - 1 - transitions

    total = sum(residues, Fraction(0))
    square = sum((value * value for value in residues), Fraction(0))
    coherence = total * total / (len(residues) * square)

    positive = sum(value > 0 for value in residues)
    negative = sum(value < 0 for value in residues)
    majority = max(positive, negative)
    assert majority * square >= total * total
    assert transitions <= 2 * (len(residues) - majority)
    assert same_sign >= (2 * coherence - 1) * len(residues) - 1

    edge = sum(
        (right - left) ** 2 / (left * left + right * right)
        for left, right in zip(residues, residues[1:])
        if left * left + right * right
    )
    assert edge >= transitions
    return transitions, same_sign


def main():
    fixtures = [
        ([-5, -3, -1, 1, 3, 5], [0, 0, 0, 0, 0]),
        ([-6, -4, -2, 1, 4, 7], [1, -2, 3, -1, 2]),
        ([-7, -3, -2, 2, 5, 8], [-3, 1, 0, 2, -4]),
        ([-9, -5, -1, 2, 6, 10], [5, -3, 2, 1, -1]),
    ]
    transition_total = 0
    interval_total = 0
    for roots, constants in fixtures:
        transitions, same = check_fixture(roots, constants)
        transition_total += transitions
        interval_total += len(roots) - 1
        assert same == len(roots) - 1 - transitions

    threshold = Fraction(1897, 1994)
    assert Fraction(997, 1000) * (2 * threshold - 1) == Fraction(9, 10)
    assert Fraction(3, 40) + Fraction(11, 500) == Fraction(97, 1000)

    # c+cos firewall at c=2: residues alternate -3,+1 and edge energy is 8/5.
    c = Fraction(2)
    rho_even = -(c + 1)
    rho_odd = c - 1
    edge = (rho_odd - rho_even) ** 2 / (rho_even**2 + rho_odd**2)
    assert edge == Fraction(8, 5)
    assert rho_even < 0 < rho_odd

    payload = {
        "schema": "riemann.x106610.fifth-residue-coherence.v1",
        "classification": "PASS_T106610_FIFTH_RESIDUE_COHERENCE",
        "polynomial_fixtures": len(fixtures),
        "fixture_intervals": interval_total,
        "fixture_sign_transitions": transition_total,
        "coherence_transition_inequality_checked": True,
        "projective_edge_inequality_checked": True,
        "coherence_threshold": "1897/1994",
        "projective_allowance": "97/1000",
        "deep_plus_shallow_identity": "3/40+11/500=97/1000",
        "positive_source_firewall_edge": "8/5",
        "rescoh106610_proved": False,
        "resedge106610_proved": False,
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
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
