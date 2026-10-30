"""Exact finite checks for the sparse reciprocal character-product proposal.

Python standard library only. No zeros are estimated, and no numerical output
is used to infer an infinite theorem. Run: python replay.py > replay.json
"""

from itertools import product
from math import comb, gcd
import json


def primes_to(n):
    a = bytearray(b"\x01") * (n + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if a[p]:
            a[p * p : n + 1 : p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if a[p]]


def phi(q):
    return sum(gcd(a, q) == 1 for a in range(1, q + 1))


def order(a, q):
    x, k = a % q, 1
    while x != 1:
        x = x * a % q
        k += 1
    return k


def coefficients(q, nmax, primes):
    h = phi(q)
    coeff = {1: 1}
    for p in primes:
        if q % p == 0:
            continue
        f = order(p, q)
        step = p**f
        if step > nmax:
            continue
        exponent = h // f
        local = [(1, 1)]
        power = 1
        for j in range(1, exponent + 1):
            power *= step
            if power > nmax:
                break
            local.append((power, (-1) ** j * comb(exponent, j)))
        updated = {}
        for n, v in coeff.items():
            for m, w in local:
                if n * m > nmax:
                    break
                updated[n * m] = updated.get(n * m, 0) + v * w
        coeff = {n: v for n, v in updated.items() if v}
    assert all(n % q == 1 for n in coeff)
    assert all(n == 1 or n > q for n in coeff)
    for p in primes:
        if p <= nmax and p % q == 1:
            assert coeff.get(p, 0) == -h
    values = sorted((n, v) for n, v in coeff.items() if n > 1)
    return {
        "q": q,
        "phi_q": h,
        "nmax": nmax,
        "nonconstant_terms": len(values),
        "first_nonconstant_n": values[0][0],
        "first_terms": values[:12],
        "support_and_prime_coefficients": "PASS",
    }


def walsh_check():
    h = 8
    matrix = [[(-1) ** ((g & k).bit_count()) for k in range(h)] for g in range(h)]
    cases = 0
    equality_cases = 0
    minimum_by_energy = {}
    for tail in product(range(-2, 3), repeat=h - 1):
        exponents = (-1,) + tail
        values = [sum(a * b for a, b in zip(row, exponents)) for row in matrix]
        energy = sum(x * x for x in exponents)
        negative = sum(x < 0 for x in values)
        assert sum(values) == h * exponents[0]
        assert sum(x * x for x in values) == h * energy
        assert negative * energy >= h * exponents[0] ** 2
        equality_cases += negative * energy == h * exponents[0] ** 2
        minimum_by_energy[energy] = min(minimum_by_energy.get(energy, h), negative)
        cases += 1
    all_inverse = [-sum(row) for row in matrix]
    assert all_inverse == [-8, 0, 0, 0, 0, 0, 0, 0]
    return {
        "group": "(Z/2Z)^3",
        "principal_exponent": -1,
        "other_exponents": "all 5^7 vectors with entries in [-2,2]",
        "cases": cases,
        "inequality": "negative_classes * exponent_energy >= group_order",
        "result": "PASS",
        "equality_cases": equality_cases,
        "sharp_example": {"exponents": [-1] * 8, "prime_coefficients": all_inverse},
        "minimum_negative_classes_by_energy": minimum_by_energy,
    }


def divisor_checks():
    bound = 500
    phis = {q: phi(q) for q in range(1, bound + 1)}
    complement_checks = 0
    for m in range(1, bound + 1):
        assert sum(phis[q] for q in range(1, m + 1) if m % q == 0) == m
        for Q in (2, 3, 5, 11, 31):
            partial = sum(phis[q] for q in range(1, min(Q, m) + 1) if m % q == 0)
            remainder = m - partial
            assert remainder >= 0
            assert -(partial - 1) == -(m - 1) + remainder
            if m <= Q:
                assert remainder == 0
            complement_checks += 1
    # Arbitrary synthetic primitive-zero multiplicities. This checks the exact
    # induction/counting weights, not the existence or locations of L-zeros.
    counts = {d: (d * d + 3 * d + 1) % 7 for d in range(1, 81)}
    counts[1] = 2
    for Q in range(2, 81):
        by_modulus = sum(sum(counts[d] for d in range(1, q + 1) if q % d == 0)
                         for q in range(2, Q + 1))
        by_conductor = (Q - 1) * counts[1] + sum((Q // d) * counts[d] for d in range(2, Q + 1))
        assert by_modulus == by_conductor
    return {
        "totient_identity_through": bound,
        "finite_complement_checks": complement_checks,
        "conductor_counting_checks": 79,
        "multiplicities": "synthetic nonnegative integers; no zero census",
        "result": "PASS",
    }


if __name__ == "__main__":
    bound = 20000
    primes = primes_to(bound)
    result = {
        "status": "PASS",
        "arithmetic": "exact integers",
        "scope": "finite Euler coefficient identities and finite Fourier inequality only",
        "cyclotomic_replays": [coefficients(q, bound, primes) for q in (3, 4, 5, 7, 8, 11, 16, 31, 101)],
        "finite_fourier_replay": walsh_check(),
        "divisor_and_conductor_replay": divisor_checks(),
    }
    print(json.dumps(result, indent=2))
