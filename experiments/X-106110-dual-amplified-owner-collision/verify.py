#!/usr/bin/env python3
"""Finite replay for T-106110.

This verifies finite algebra and orthogonality identities only.  It does not
prove either open hybrid moment or RH.
"""

from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Dict, Iterable, List

PRIMES = (5, 7, 11, 13)
TOL = 2.0e-8


def primitive_root(p: int) -> int:
    factors: List[int] = []
    n = p - 1
    q = 2
    while q * q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError(f"no primitive root modulo {p}")


def discrete_logs(p: int) -> Dict[int, int]:
    g = primitive_root(p)
    out: Dict[int, int] = {}
    x = 1
    for j in range(p - 1):
        out[x] = j
        x = (x * g) % p
    assert len(out) == p - 1
    return out


def chi(p: int, logs: Dict[int, int], j: int, u: int) -> complex:
    return cmath.exp(2j * math.pi * j * logs[u % p] / (p - 1))


def close(a: complex, b: complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol * (1.0 + abs(a) + abs(b))


def first_odd_primes(n: int) -> List[int]:
    out: List[int] = []
    x = 3
    while len(out) < n:
        is_prime = True
        d = 2
        while d * d <= x:
            if x % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            out.append(x)
        x += 2
    return out


def deterministic_coeffs(p: int, trial: int) -> Dict[int, complex]:
    return {
        u: complex(((u + 2 * trial) % 5) - 2, ((2 * u + trial) % 7) - 3)
        / (1 + u)
        for u in range(1, p)
    }


def main() -> None:
    checks = 0

    # R-106110: the Q-fixed external weight cancels the reciprocal fibre
    # energy and leaves the number of fibres.
    qs = first_odd_primes(20)
    for n in range(1, 21):
        local = sum((Fraction(1, q) for q in qs[:n]), Fraction(0, 1))
        q_weighted = sum((Fraction(q, q) for q in qs[:n]), Fraction(0, 1))
        assert local > 0
        assert q_weighted == n
        checks += 1

    # Sharp principal embedding on one multiplicative squareclass.  The Gram
    # is p I - J on the (p-1)/2 sign classes.
    for p in PRIMES:
        m = (p - 1) // 2
        const = [1] * m
        energy = p * sum(x * x for x in const) - sum(const) ** 2
        principal = sum(const) ** 2
        assert energy * (p - 1) == principal * (p + 1)
        checks += 1
        for trial in range(5):
            b = [((3 * i + trial) % 7) - 3 for i in range(1, m + 1)]
            energy = p * sum(x * x for x in b) - sum(b) ** 2
            principal = sum(b) ** 2
            assert energy >= 0
            assert energy * (p - 1) >= principal * (p + 1)
            checks += 1

    # L-106110: summing all opposite-owner fibres before squaring is exactly
    # the expanded cross-fibre energy.
    for p in PRIMES:
        reps = [pow(i, 2, p) for i in range(1, (p - 1) // 2 + 1)]
        for trial in range(4):
            fibres: List[List[complex]] = []
            for q_index in range(1, 4 + trial):
                fibres.append(
                    [
                        complex((q_index + j + trial) % 5 - 2,
                                (2 * q_index + j) % 3 - 1)
                        for j in range(len(reps))
                    ]
                )
            direct = 0j
            expanded = 0j
            phase_fields: List[List[complex]] = []
            for fibre in fibres:
                vals: List[complex] = []
                for h in range(1, p):
                    vals.append(
                        sum(
                            fibre[j]
                            * cmath.exp(2j * math.pi * h * reps[j] / p)
                            for j in range(len(reps))
                        )
                    )
                phase_fields.append(vals)
            for h in range(p - 1):
                direct += abs(sum(field[h] for field in phase_fields)) ** 2
            for left in phase_fields:
                for right in phase_fields:
                    expanded += sum(
                        left[h] * right[h].conjugate() for h in range(p - 1)
                    )
            assert close(direct, expanded)
            checks += 1

    # L-106112: the unordered semiprime owner field is one Wick square minus
    # the repeated-prime diagonal.
    for p in PRIMES:
        logs = discrete_logs(p)
        labels = list(range(1, min(p, 7)))
        x = {u: complex((u % 4) - 1, (2 * u % 5) - 2) / (u + 1) for u in labels}
        for j in range(p - 1):
            vals = {u: x[u] * chi(p, logs, j, u) for u in labels}
            lhs = sum(
                vals[labels[a]] * vals[labels[b]]
                for a in range(len(labels))
                for b in range(a + 1, len(labels))
            )
            rhs = 0.5 * (
                sum(vals.values()) ** 2 - sum(v * v for v in vals.values())
            )
            assert close(lhs, rhs)
            checks += 1

    # L-106113: complete-character fourth moment equals the product-collision
    # form.
    for p in PRIMES:
        logs = discrete_logs(p)
        units = list(range(1, p))
        for trial in range(2):
            x = deterministic_coeffs(p, trial)
            lhs = 0.0
            for j in range(p - 1):
                amp = sum(x[u] * chi(p, logs, j, u) for u in units)
                lhs += abs(amp) ** 4
            lhs /= p - 1
            rhs = 0j
            for a, b, c, d in product(units, repeat=4):
                if (a * b - c * d) % p == 0:
                    rhs += x[a] * x[b] * (x[c] * x[d]).conjugate()
            assert close(lhs, rhs)
            checks += 1

    # Even characters see the union of the + and - product-collision loci.
    for p in PRIMES:
        logs = discrete_logs(p)
        units = list(range(1, p))
        even_js = list(range(0, p - 1, 2))
        for trial in range(2):
            x = deterministic_coeffs(p, trial + 3)
            lhs = 0.0
            for j in even_js:
                amp = sum(x[u] * chi(p, logs, j, u) for u in units)
                lhs += abs(amp) ** 4
            lhs /= len(even_js)
            rhs = 0j
            for a, b, c, d in product(units, repeat=4):
                ab = (a * b) % p
                cd = (c * d) % p
                if ab == cd or ab == (-cd) % p:
                    rhs += x[a] * x[b] * (x[c] * x[d]).conjugate()
            assert close(lhs, rhs)
            checks += 1

    # Atomic diagonal source inequality ell/c^2 <= 1/c whenever ell | c.
    for ell in PRIMES:
        for k in range(1, 51):
            c = ell * k
            assert Fraction(ell, c * c) <= Fraction(1, c)
            checks += 1

    # A coherent opposite-owner sum and its true diagonal are distinct from
    # the Q-weighted fixed-fibre moment.
    for n in range(2, 21):
        values = [1.0 / math.sqrt(q) for q in qs[:n]]
        coherent = abs(sum(values)) ** 2
        diagonal = sum(v * v for v in values)
        q_weighted = float(n)
        assert coherent >= diagonal
        assert q_weighted > diagonal
        checks += 1

    result = {
        "schema": "riemann.x106110.dual-amplified-owner-collision.v1",
        "verdict": "PASS_X_106110_DUAL_AMPLIFIED_OWNER_COLLISION",
        "checks": checks,
        "proved_by_replay": {
            "q_fixed_fibre_dimension_firewall": True,
            "all_q_amplification_before_square": True,
            "sharp_squareclass_principal_embedding": True,
            "equal_pair_semiprime_wick_identity": True,
            "complete_character_product_collision_identity": True,
            "even_character_plus_minus_collision_identity": True,
            "atomic_diagonal_weight_inequality": True,
        },
        "not_proved": {
            "dapro106110": True,
            "dakum106110": True,
            "bci102990": True,
            "riemann_hypothesis": True,
        },
    }
    assert checks == 327, checks
    print(json.dumps(result, indent=2, sort_keys=True))

    out = Path(__file__).with_name("results") / "verification.generated.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
