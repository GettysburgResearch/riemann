#!/usr/bin/env python3
"""Exact finite regression for L-26204 affine/Skorokhod comparison.

Arithmetic class: integers + fractions + formal prime-log coefficient vectors.
This checker proves only the finite identities encoded below.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

X = 12
Y = 13  # prime oversupport
PRIME_POWERS = (2, 3, 4, 5, 7, 8, 9, 11)
PRIMES = (2, 3, 5, 7, 11, 13)


def factor_log_vector(n: int) -> tuple[int, ...]:
    exponents = []
    r = n
    for p in PRIMES:
        e = 0
        while r % p == 0:
            e += 1
            r //= p
        exponents.append(e)
    if r != 1:
        raise AssertionError(f"undeclared prime factor in {n}: {r}")
    return tuple(exponents)


def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vec_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vec_scale(c: Fraction, a):
    return tuple(c * x for x in a)


def objective_form(b: dict[int, Fraction], endpoint: int) -> tuple[Fraction, ...]:
    out = tuple(Fraction(0) for _ in PRIMES)
    for m in range(2, endpoint + 1):
        coeff = b.get(m, Fraction(0))
        out = vec_add(
            out,
            vec_scale(
                coeff,
                vec_sub(factor_log_vector(m), factor_log_vector(m - 1)),
            ),
        )
    return out


def vq(b: dict[int, Fraction], q: int, endpoint: int) -> Fraction:
    total = Fraction(0)
    k = 1
    while k * q <= endpoint:
        total += b.get(k * q, Fraction(0)) - b.get(k * q + 1, Fraction(0))
        k += 1
    return total


def mangoldt_vector(q: int) -> tuple[Fraction, ...]:
    # Lambda(p^a)=log p, and zero otherwise.
    for i, p in enumerate(PRIMES):
        r = q
        while r % p == 0:
            r //= p
        if r == 1:
            return tuple(
                Fraction(1 if j == i else 0) for j in range(len(PRIMES))
            )
    return tuple(Fraction(0) for _ in PRIMES)


def dual_objective_from_responses(b, endpoint):
    out = tuple(Fraction(0) for _ in PRIMES)
    for q in PRIME_POWERS:
        out = vec_add(
            out,
            vec_scale(vq(b, q, endpoint), mangoldt_vector(q)),
        )
    if endpoint >= Y:
        out = vec_add(
            out,
            vec_scale(vq(b, Y, endpoint), mangoldt_vector(Y)),
        )
    return out


def run() -> dict:
    # Nonnegative benchmark and a signed equality state. The target is defined
    # source-bound as the exact response of b_star.
    b0 = {
        m: Fraction((X + 1 - m) * (m + 1), 24)
        for m in range(2, X + 1)
    }
    b_star = dict(b0)
    perturb = {
        2: Fraction(7, 6),
        3: Fraction(-5, 4),
        4: Fraction(2, 3),
        6: Fraction(11, 8),
        8: Fraction(-7, 5),
        10: Fraction(2, 1),
        12: Fraction(1, 1),
    }
    for m, u in perturb.items():
        b_star[m] -= u  # u=b0-b_star

    target = {q: vq(b_star, q, X) for q in PRIME_POWERS}
    C = max(
        Fraction(0),
        *(b0[m] - b_star[m] for m in range(2, X + 1)),
    )

    # Affine oversupport lift.
    b_tilde = {
        m: b_star.get(m, Fraction(0)) + C for m in range(2, Y + 1)
    }
    assert all(b_tilde[m] >= b0[m] for m in range(2, X + 1))
    assert all(b_tilde[m] >= 0 for m in range(2, Y + 1))
    assert all(vq(b_tilde, q, Y) == target[q] for q in PRIME_POWERS)
    assert vq(b_tilde, Y, Y) == C

    # Formal objective identities.
    assert objective_form(b_star, X) == dual_objective_from_responses(
        b_star, X
    )
    assert objective_form(b_tilde, Y) == dual_objective_from_responses(
        b_tilde, Y
    )
    expected_lift = vec_add(
        objective_form(b_star, X), vec_scale(C, factor_log_vector(Y))
    )
    assert objective_form(b_tilde, Y) == expected_lift

    # Prefix Skorokhod regulator.
    a = {m: max(Fraction(0), -b_star[m]) for m in range(2, X + 1)}
    sigma = {1: Fraction(0)}
    running = Fraction(0)
    for m in range(2, X + 1):
        running = max(running, a[m])
        sigma[m] = running
    lam = {m: sigma[m] - sigma[m - 1] for m in range(2, X + 1)}
    b_down = {m: b_star[m] + sigma[m] for m in range(2, X + 1)}
    assert all(v >= 0 for v in b_down.values())
    assert sum(lam.values(), Fraction(0)) == max(
        a.values(), default=Fraction(0)
    )
    assert sum(lam.values(), Fraction(0)) <= C

    # Exact residual formula for the prefix regulator.
    for q in PRIME_POWERS:
        rhs = sum(
            lam[j]
            * (
                Fraction(1 if X % q == 0 else 0)
                - Fraction(1 if (j - 1) % q == 0 else 0)
            )
            for j in range(2, X + 1)
        )
        assert vq(b_down, q, X) - target[q] == rhs

    # Formal contact-debt identity.
    P_form = dual_objective_from_responses(b_star, X)
    residual = {
        q: vq(b_down, q, X) - target[q] for q in PRIME_POWERS
    }
    endpoint_positive = {
        q: residual[q] if X % q == 0 else Fraction(0)
        for q in PRIME_POWERS
    }
    L_down_form = objective_form(b_down, X)
    for q, coeff in endpoint_positive.items():
        L_down_form = vec_sub(
            L_down_form, vec_scale(coeff, mangoldt_vector(q))
        )
    gap_form = vec_sub(P_form, L_down_form)

    contact_form = tuple(Fraction(0) for _ in PRIMES)
    for j in range(2, X + 1):
        ratio_num = j - 1
        ratio_den = gcd(j - 1, X)
        contact_form = vec_add(
            contact_form,
            vec_scale(
                lam[j],
                vec_sub(
                    factor_log_vector(ratio_num),
                    factor_log_vector(ratio_den),
                ),
            ),
        )
    assert gap_form == contact_form

    # Mutation tests.
    mutations = 0
    try:
        bad = dict(b_tilde)
        bad[Y] -= Fraction(1, 17)
        assert vq(bad, Y, Y) == C
    except AssertionError:
        mutations += 1
    try:
        bad_y = 12  # composite and charges old rows
        bad = {
            m: b_star.get(m, Fraction(0)) + C
            for m in range(2, bad_y + 1)
        }
        assert all(
            vq(bad, q, bad_y) == target[q] for q in PRIME_POWERS
        )
    except AssertionError:
        mutations += 1
    try:
        bad_C = C - Fraction(1, 100)
        assert all(
            b_star[m] + bad_C >= b0[m] for m in range(2, X + 1)
        )
    except AssertionError:
        mutations += 1
    try:
        bad_sigma = dict(sigma)
        bad_sigma[X] = Fraction(0)
        assert bad_sigma[X] >= a[X]
    except AssertionError:
        mutations += 1
    assert mutations == 4

    result = {
        "schema": "X-26202-v1",
        "classification": "EXACT_AFFINE_GREEN_SKOROKHOD_COMPARISON",
        "X": X,
        "oversupport_prime": Y,
        "boundary_charge": str(C),
        "maximum_negative_excursion": str(max(a.values())),
        "prefix_contact_mass": str(sum(lam.values(), Fraction(0))),
        "old_prime_power_rows_preserved": len(PRIME_POWERS),
        "new_boundary_charge": str(vq(b_tilde, Y, Y)),
        "formal_log_primes": list(PRIMES),
        "mutation_tests": "4/4 PASS",
        "proof_boundary": (
            "Exact finite algebra only; no cofinal affine-charge estimate "
            "or RH conclusion."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_sha256"] = sha256(canonical.encode()).hexdigest()
    return result


if __name__ == "__main__":
    result = run()
    out = Path(__file__).with_name("verification.json")
    out.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))
