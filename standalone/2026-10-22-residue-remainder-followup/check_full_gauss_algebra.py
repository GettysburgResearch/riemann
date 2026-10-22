#!/usr/bin/env python3
"""Exact finite algebra checks for the full-modulus Gauss push-forward.

This checks neither an analytic large sieve nor an infinite operator bound.
All character values and sums are integer pairs a+b*omega, omega^2+omega+1=0.
There are no floating-point Gauss sums or numerical tolerances.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


THEOREM_SHA256 = "9d95cb27a11804cd553d7b836b3dcecaeb52bee633fbdc7cfe4893d9c59a6d8b"
MAX_MODULUS_NORM = 2500
ZERO = (0, 0)
ONE = (1, 0)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def power(x, n):
    assert n >= 0
    out = ONE
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out


ROOTS = tuple(power((1, 1), k) for k in range(6))
assert len(set(ROOTS)) == 6 and power((1, 1), 6) == ONE


def primary(x):
    associates = [mul(u, x) for u in ROOTS]
    choices = [a for a in associates if a[0] % 3 == 1 and a[1] % 3 == 0]
    assert len(choices) == 1
    return choices[0]


def bezout(a, b):
    """Return g,x,y with g>0 and a*x+b*y=gcd(a,b)."""
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    if old_r < 0:
        old_r, old_x, old_y = -old_r, -old_x, -old_y
    assert old_r > 0 and a * old_x + b * old_y == old_r
    return old_r, old_x, old_y


class Quotient:
    """O/(c), using an exact triangular ideal-lattice basis.

    Multiplication by c=a+b*omega has integer matrix
    [[a,-b],[b,a-b]]. Its column Hermite basis is
    [(h11,0),(h12,h22)], h22=gcd(b,a-b), h11=N(c)/h22.
    """

    def __init__(self, modulus):
        self.modulus = modulus
        a, b = modulus
        self.size = norm(modulus)
        g, x, y = bezout(b, a - b)
        assert self.size % g == 0
        self.h11 = self.size // g
        self.h22 = g
        self.h12 = (a * x - b * y) % self.h11
        assert self.h11 * self.h22 == self.size
        assert self.reduce(modulus) == ZERO
        assert self.reduce(mul(modulus, (0, 1))) == ZERO

    def reduce(self, x):
        a, b = x
        q, r = divmod(b, self.h22)
        return ((a - q * self.h12) % self.h11, r)

    def representatives(self):
        return tuple((a, b) for b in range(self.h22) for a in range(self.h11))

    def multiply(self, x, y):
        return self.reduce(mul(x, y))

    def power(self, x, n):
        out = self.reduce(ONE)
        x = self.reduce(x)
        while n:
            if n & 1:
                out = self.multiply(out, x)
            x = self.multiply(x, x)
            n //= 2
        return out


PRIMES = (
    ("split_7", primary((3, 1))),
    ("conjugate_split_7", primary((2, -1))),
    ("split_13", primary((4, 1))),
    ("inert_5_norm_25", primary((5, 0))),
)
PRIME_NORMS = tuple(norm(p) for _, p in PRIMES)
assert PRIME_NORMS == (7, 7, 13, 25)
NPRIMES = len(PRIMES)
UNIT_FACTORS = (0,) * NPRIMES


@lru_cache(maxsize=None)
def ideal_generator(factors):
    out = ONE
    for (_, p), exponent in zip(PRIMES, factors):
        out = mul(out, power(p, exponent))
    assert out[0] % 3 == 1 and out[1] % 3 == 0
    return out


@lru_cache(maxsize=None)
def ideal_norm(factors):
    out = 1
    for q, exponent in zip(PRIME_NORMS, factors):
        out *= q ** exponent
    assert norm(ideal_generator(factors)) == out
    return out


@lru_cache(maxsize=None)
def quotient(factors):
    return Quotient(ideal_generator(factors))


PRIME_RINGS = tuple(Quotient(p) for _, p in PRIMES)
PRIME_PHASES = []
for ring, q in zip(PRIME_RINGS, PRIME_NORMS):
    root_lookup = {ring.reduce(z): k for k, z in enumerate(ROOTS)}
    assert len(root_lookup) == 6
    table = {}
    for x in ring.representatives():
        if x == ZERO:
            table[x] = None
        else:
            value = ring.power(x, (q - 1) // 6)
            assert value in root_lookup
            table[x] = root_lookup[value]
            assert ring.power(x, q - 1) == ring.reduce(ONE)
    assert set(v for v in table.values() if v is not None) == set(range(6))
    PRIME_PHASES.append(table)


def prime_phase(index, x):
    return PRIME_PHASES[index][PRIME_RINGS[index].reduce(x)]


def character_phase(factors, x):
    """None is the literal zero; local exponent 6 is still zero on nonunits."""
    answer = 0
    for i, exponent in enumerate(factors):
        if exponent:
            phase = prime_phase(i, x)
            if phase is None:
                return None
            answer += exponent * phase
    return answer % 6


def character(factors, x):
    phase = character_phase(factors, x)
    return ZERO if phase is None else ROOTS[phase]


def scalar(k, x):
    return (k * x[0], k * x[1])


def enumerate_moduli():
    ranges = []
    for q in PRIME_NORMS:
        exponent = 0
        while q ** (exponent + 1) <= MAX_MODULUS_NORM:
            exponent += 1
        ranges.append(range(exponent + 1))
    found = [tuple(f) for f in product(*ranges) if ideal_norm(tuple(f)) <= MAX_MODULUS_NORM]
    return sorted(found, key=lambda f: (ideal_norm(f), f))


def label_cases(modulus_factors):
    """All active-prime exponents 0..5 and one external-prime exponent 0..5.

    The first absent prime in the fixed displayed basis is the external
    prime. It makes R0 nontrivial while remaining a unit at every c-prime.
    Every listed modulus has an absent prime at the norm cap 2500.
    """
    active = [i for i, e in enumerate(modulus_factors) if e]
    external = next(i for i, e in enumerate(modulus_factors) if not e)
    for entries in product(range(6), repeat=len(active) + 1):
        out = [0] * NPRIMES
        for i, e in zip(active, entries[:-1]):
            out[i] = e
        out[external] = entries[-1]
        yield tuple(out)


@lru_cache(maxsize=None)
def unit_data(factors):
    ring = quotient(factors)
    data = []
    for x in ring.representatives():
        phase = character_phase(factors, x)
        if phase is not None:
            data.append((x, phase))
    phi = ideal_norm(factors)
    for q, e in zip(PRIME_NORMS, factors):
        if e:
            phi = (phi // q) * (q - 1)
    assert len(data) == phi
    return tuple(data)


@lru_cache(maxsize=None)
def base_pushforward(c, t):
    m = tuple(e - f for e, f in zip(c, t))
    ring_m = quotient(m)
    accum = {y: ZERO for y in ring_m.representatives()}
    for x, phase in unit_data(c):
        y = ring_m.reduce(x)
        accum[y] = add(accum[y], ROOTS[phase])
    return m, accum


def run_checks():
    moduli = enumerate_moduli()
    summary = []
    totals = Counter()
    mutation_witnesses = {}
    for c in moduli:
        per = Counter()
        for r in label_cases(c):
            t = tuple(min(e, f) for e, f in zip(c, r))
            r0 = tuple(e - f for e, f in zip(r, t))
            m, accum = base_pushforward(c, t)
            ring_m = quotient(m)
            r0_generator = ideal_generator(r0)
            assert all(min(e, f) == 0 for e, f in zip(m, r0))
            disappearing = any(ec > 0 and em == 0 for ec, em in zip(c, m))
            per["label_cases"] += 1
            if disappearing:
                assert all(value == ZERO for value in accum.values()), ("nonzero disappearing-prime fiber", c, r)
                per["vanishing_cases"] += 1
                if "omit_disappearing_prime_filter" not in mutation_witnesses:
                    phase_r0 = character_phase(c, r0_generator)
                    if phase_r0 is not None:
                        for y in ring_m.representatives():
                            phase_y = character_phase(c, y)
                            if phase_y is not None:
                                wrong = scalar(ideal_norm(t), ROOTS[(phase_y - phase_r0) % 6])
                                if wrong != ZERO:
                                    mutation_witnesses["omit_disappearing_prime_filter"] = {
                                        "c_exponents": c, "R_exponents": r, "y": y,
                                        "actual": ZERO, "wrong": wrong,
                                    }
                                    break
                continue

            per["surviving_cases"] += 1
            phase_r0 = character_phase(c, r0_generator)
            assert phase_r0 is not None
            fiber_size = ideal_norm(t)
            visited = set()
            for s, value in accum.items():
                y = ring_m.reduce(mul(r0_generator, s))
                visited.add(y)
                phase_y = character_phase(c, y)
                expected = ZERO if phase_y is None else scalar(fiber_size, ROOTS[(phase_y - phase_r0) % 6])
                assert value == expected, ("push-forward mismatch", c, r, y, value, expected)
                per["coefficient_equalities"] += 1
                if phase_y is not None:
                    if fiber_size > 1 and "omit_fiber_factor_Nt" not in mutation_witnesses:
                        wrong = ROOTS[(phase_y - phase_r0) % 6]
                        if wrong != value:
                            mutation_witnesses["omit_fiber_factor_Nt"] = {
                                "c_exponents": c, "R_exponents": r, "y": y,
                                "actual": value, "wrong": wrong,
                            }
                    if "omit_conjugation" not in mutation_witnesses:
                        wrong = scalar(fiber_size, ROOTS[(phase_y + phase_r0) % 6])
                        if wrong != value:
                            mutation_witnesses["omit_conjugation"] = {
                                "c_exponents": c, "R_exponents": r, "y": y,
                                "actual": value, "wrong": wrong,
                            }
            assert len(visited) == ring_m.size
            if m == UNIT_FACTORS:
                per["surviving_modulus_one_cases"] += 1

        active = [i for i, e in enumerate(c) if e]
        histogram = Counter()
        for y, _ in unit_data(c):
            phases = tuple(prime_phase(i, y) for i in active)
            assert all(p is not None for p in phases)
            histogram[phases] += 1
        character_signatures = set()
        for t_entries in product(range(6), repeat=len(active)):
            total = ZERO
            signature = []
            for phases, count in sorted(histogram.items()):
                base = sum(c[i] * p for i, p in zip(active, phases)) % 6
                shifted = sum((c[i] + e) * p for i, e, p in zip(active, t_entries, phases)) % 6
                total = add(total, scalar(count, ROOTS[(shifted - base) % 6]))
                signature.append(shifted)
            expected = (len(unit_data(c)), 0) if not any(t_entries) else ZERO
            assert total == expected, ("orthogonality mismatch", c, t_entries, total, expected)
            character_signatures.add(tuple(signature))
            per["orthogonality_quotients_checked"] += 1
        num_characters = 6 ** len(active)
        assert len(character_signatures) == num_characters
        per["characters_distinguished"] = num_characters
        per["ordered_character_pairs_covered"] = num_characters ** 2
        per["offdiagonal_character_pairs_covered"] = num_characters * (num_characters - 1)
        totals.update(per)
        summary.append({
            "modulus_exponents": c,
            "primary_generator": ideal_generator(c),
            "norm": ideal_norm(c),
            "unit_count": len(unit_data(c)),
            **dict(per),
        })

    assert set(mutation_witnesses) == {
        "omit_disappearing_prime_filter", "omit_fiber_factor_Nt", "omit_conjugation"
    }
    assert max(ideal_norm(c) for c in moduli) == 2401
    assert any(c[0] and c[1] for c in moduli)
    assert any(c[2] == 3 for c in moduli)
    assert any(c[3] == 2 for c in moduli)
    return {
        "status": "PASS",
        "scope": "Finite quotient-ring character algebra only; no analytic large-sieve, functional-equation, infinite operator, or zero-free claim is verified.",
        "arithmetic": "Exact Z[omega] integer pairs; omega^2+omega+1=0; character phases evaluated by finite-field Euler powers; no floating point.",
        "basis_primes": [
            {"name": name, "primary_generator": p, "norm": q}
            for (name, p), q in zip(PRIMES, PRIME_NORMS)
        ],
        "sixth_roots_integer_pairs": ROOTS,
        "modulus_coverage": "All products of the four displayed prime ideals with norm at most 2500; includes repeated prime powers, both primes above 7, inert 5, and the unit ideal.",
        "label_coverage": "For each modulus: every exponent 0..5 at each modulus prime, and every exponent 0..5 at the first absent prime in the displayed basis. Other exponents are zero. This is the exact finite test set, not all labels.",
        "orthogonality_coverage": "For every displayed modulus m, all t exponent vectors 0..5 on rad(m). Exact sums for all quotient-exponent classes and distinct character signatures cover every ordered character pair; no modulus mt enumeration is required.",
        "modulus_count": len(moduli),
        "maximum_modulus_norm": max(ideal_norm(c) for c in moduli),
        "totals": dict(totals),
        "mutations_rejected": mutation_witnesses,
        "moduli": summary,
    }


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: exact assertions must remain enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("FINITE_FULL_GAUSS_ALGEBRA_CHECKS.json"))
    parser.add_argument("--theorem", type=Path, help="Optional exact reviewed theorem file; its SHA256 must match the frozen identity.")
    args = parser.parse_args()
    theorem_authentication = {"expected_sha256": THEOREM_SHA256, "authenticated": False}
    if args.theorem:
        actual = hashlib.sha256(args.theorem.read_bytes()).hexdigest()
        assert actual == THEOREM_SHA256, ("theorem hash mismatch", actual)
        theorem_authentication.update({"authenticated": True, "actual_sha256": actual})
    report = run_checks()
    report["theorem_identity"] = theorem_authentication
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "modulus_count": report["modulus_count"], "maximum_modulus_norm": report["maximum_modulus_norm"], "totals": report["totals"], "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
