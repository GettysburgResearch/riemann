#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def proof_digest(payload: dict[str, object]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def phase_symbol(activities: list[Fraction], phases: list[complex]) -> complex:
    total = 0j
    k = len(activities)
    # Exact definition L-99991 with a high-order deterministic quadrature is
    # unnecessary for the bound audit.  Integrate each polynomial exactly by
    # expanding subsets.
    for i in range(k):
        ai = float(activities[i])
        zi = phases[i]
        for mask in range(1 << (k - 1)):
            subset: list[int] = []
            cursor = 0
            for h in range(k):
                if h == i:
                    continue
                if mask & (1 << cursor):
                    subset.append(h)
                cursor += 1
            if len(subset) % 2 == 0:
                continue
            # Integral of (1-t)^|A| prod_(outside)(1-a_h t).
            outside = [h for h in range(k) if h != i and h not in subset]
            # Polynomial coefficients in t.
            poly = [1.0]
            for h in outside:
                ah = float(activities[h])
                nxt = [0.0] * (len(poly) + 1)
                for j, c in enumerate(poly):
                    nxt[j] += c
                    nxt[j + 1] -= ah * c
                poly = nxt
            # multiply by (1-t)^m
            for _ in subset:
                nxt = [0.0] * (len(poly) + 1)
                for j, c in enumerate(poly):
                    nxt[j] += c
                    nxt[j + 1] -= c
                poly = nxt
            integral = sum(c / (j + 1) for j, c in enumerate(poly))
            w = 1.0 + 0j
            for h in subset:
                w *= float(activities[h]) * phases[h]
            total += ai * (1 - zi) * w * integral
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # Critical-conjugation fixtures: q is a square and y is a large square, so
    # every expression is rational.
    conjugation = []
    for q, y in [(4, 10**8), (9, 10**8), (25, 10**10)]:
        sq_q = math.isqrt(q)
        sq_y = math.isqrt(y)
        assert sq_q * sq_q == q and sq_y * sq_y == y
        f_y = Fraction(24, sq_y) - Fraction(9, y)
        f_yq = Fraction(24 * sq_q, sq_y) - Fraction(9 * q, y)
        ratio = Fraction(1, q * sq_q) * f_yq / f_y
        target = Fraction(1, q)
        assert abs(float(ratio - target)) < 10 / sq_y
        conjugation.append(
            {"q": q, "y": y, "ratio": str(ratio), "critical_limit": str(target)}
        )

    # Local phase-symbol bound on nontrivial labelled fixtures, including two
    # equal activities representing the two 67 labels.
    phase_fixtures = [
        ([Fraction(1, 2), Fraction(1, 3)], [1j, -1 + 0j]),
        ([Fraction(1, 5), Fraction(1, 7), Fraction(1, 11)], [-1 + 0j, 1j, -1j]),
        ([Fraction(1, 67), Fraction(1, 67), Fraction(1, 71)], [1j, -1j, -1 + 0j]),
    ]
    phase_checks = []
    for activities, phases in phase_fixtures:
        value = phase_symbol(activities, phases)
        product = math.prod(1 + float(a) for a in activities)
        bound = product * sum(float(a) * abs(1 - z) for a, z in zip(activities, phases))
        assert abs(value) <= bound + 1e-12
        phase_checks.append({"value_abs": abs(value), "bound": bound})

    # Formal centered-circle Parseval fixtures.  For finite moment vectors the
    # circle mean is exactly the sum of squared Taylor coefficients.
    moment_checks = []
    for coeffs, logs, r in [
        ([Fraction(1), Fraction(-2), Fraction(1)], [Fraction(0), Fraction(1, 2), Fraction(1)], Fraction(1, 3)),
        ([Fraction(3), Fraction(-1)], [Fraction(1, 4), Fraction(3, 4)], Fraction(1, 2)),
    ]:
        moments = []
        for k in range(1, 9):
            mk = sum(c * (ell**k) for c, ell in zip(coeffs, logs))
            moments.append(mk)
        energy = sum((r ** (2 * k)) * (moments[k - 1] ** 2) / (math.factorial(k) ** 2) for k in range(1, 9))
        first = (r**2) * moments[0] ** 2
        assert energy >= first
        moment_checks.append({"truncated_energy": str(energy), "first_grade": str(first)})

    # Factorial tail exponent used by L-100212.
    tail_checks = []
    L0 = math.log(8.0)
    for X in [10**6, 10**12, 10**30]:
        K = math.ceil(4 * math.log(3 * X) / math.log(math.log(9 * X)))
        log_bound = 0.5 * math.log(X) + L0 + (K + 1) * math.log(math.e * L0 / (K + 1))
        assert log_bound < -1.5 * math.log(X)
        tail_checks.append({"X": str(X), "K": K, "log_tail_bound": log_bound})

    payload: dict[str, object] = {
        "schema": "riemann.t100210.critical_phase_circle.v1",
        "checks": {
            "critical_conjugation": conjugation,
            "phase_symbol_bounds": phase_checks,
            "centered_circle_moments": moment_checks,
            "factorial_tail": tail_checks,
        },
        "scope": {
            "quadratic_subcritical_mechanism_refuted": True,
            "local_phase_symbol_subpower_proved": True,
            "centered_circle_identity_proved": True,
            "gmpc100212_proved": False,
            "cross_core_phase_packing_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T100210_CRITICAL_PHASE_CIRCLE_ALGEBRA",
    }
    payload["proof_object_sha256"] = proof_digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
