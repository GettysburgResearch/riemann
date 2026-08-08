from __future__ import annotations

from fractions import Fraction
from math import comb
import hashlib
import json


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def producer_from_target(w: list[Fraction], endpoint: int) -> list[Fraction]:
    mu = mobius_sieve(endpoint)
    u = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(1, endpoint + 1):
        value = Fraction(0)
        for k in range(1, endpoint // m + 1):
            if mu[k]:
                value += mu[k] * w[m * k]
        u[m] = value

    incoming = [Fraction(0) for _ in range(endpoint + 2)]
    producer = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(endpoint, 1, -1):
        producer[m] = u[m] - u[m + 1] + incoming[m]
        ternary_left = (m + 2) // 3
        ternary_right = m - ternary_left
        binary_left = m // 2
        binary_right = m - binary_left
        for child in (
            ternary_left,
            ternary_right,
            binary_left,
            binary_right,
        ):
            if child >= 2:
                incoming[child] += producer[m] / 2
    return producer


def abel_witness(endpoint: int, order: int, node: int) -> Fraction:
    target = [Fraction(0) for _ in range(endpoint + 1)]
    for q in range(2, endpoint + 1):
        target[q] = Fraction(comb(endpoint - q + order - 1, order - 1))
    return producer_from_target(target, endpoint)[node]


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def verify_sibling_switch() -> int:
    checked = 0
    for h in range(2, 129):
        for q in range(2, 2 * h + 1):
            lhs = carry(2 * h, h - 1, q) - carry(2 * h, h, q)
            rhs = int(h % q == 0) - int((h + 1) % q == 0)
            assert lhs == rhs
            checked += 1
        assert Fraction(comb(2 * h, h - 1), comb(2 * h, h)) == Fraction(
            h, h + 1
        )
    return checked


def verify_commutator() -> int:
    checked = 0
    for endpoint in (32, 47, 64):
        profile = [Fraction(0) for _ in range(endpoint + 2)]
        for n in range(1, endpoint + 1):
            profile[n] = Fraction(
                (endpoint + 1 - n) * (endpoint + 2 - n),
                (n + 3) * (endpoint + 1),
            )
        difference = [Fraction(0) for _ in range(endpoint + 1)]
        for n in range(1, endpoint + 1):
            difference[n] = profile[n] - profile[n + 1]

        for q in range(2, endpoint + 1):
            direct = Fraction(0)
            k = 1
            while 2 * k * q - 1 <= endpoint:
                direct += profile[2 * k * q - 1] - profile[2 * k * q]
                k += 1

            divisor = Fraction(0)
            for h in range(1, (endpoint + 1) // 2 + 1):
                if 2 * h - 1 <= endpoint and h % q == 0:
                    divisor += difference[2 * h - 1]
            assert direct == divisor
            checked += 1
    return checked


def verify_sibling_transport() -> int:
    checked = 0
    for endpoint in (20, 37, 64):
        flow = [Fraction(0) for _ in range(endpoint + 2)]
        for h in range(1, endpoint + 1):
            flow[h] = Fraction((h * h + 3 * h + 1) % 17, h + 5)

        for q in range(2, endpoint + 2):
            direct = sum(
                (
                    flow[h]
                    * (int(h % q == 0) - int((h + 1) % q == 0))
                    for h in range(1, endpoint + 1)
                ),
                Fraction(0),
            )
            source = Fraction(0)
            for u in range(1, endpoint + 2):
                current = flow[u] if u <= endpoint else Fraction(0)
                if u % q == 0:
                    source += current - flow[u - 1]
            assert direct == source
            checked += 1
    return checked


def verify_gamma_domination() -> int:
    checked = 0
    for denominator_u in (7, 11, 13, 17):
        for denominator_v in (8, 12, 19, 23):
            for numerator_u in range(1, denominator_u):
                u = Fraction(numerator_u, denominator_u)
                for numerator_v in range(1, denominator_v):
                    v = Fraction(numerator_v, denominator_v)
                    inverse_square = 1 / (v * v)
                    m = inverse_square.numerator // inverse_square.denominator
                    lhs = (u * v) ** 4
                    rhs = (Fraction(m) + u) / (m * (m + 1))
                    assert lhs <= rhs
                    checked += 1
    return checked


def verify_matrix_lift() -> int:
    atoms = [
        (Fraction(1, 8), Fraction(1, 4), Fraction(3, 4)),
        (Fraction(1, 4), Fraction(1, 4), Fraction(5, 4)),
        (Fraction(1, 8), Fraction(3, 4), Fraction(3, 4)),
        (Fraction(1, 2), Fraction(3, 4), Fraction(7, 4)),
    ]

    def feature(y: Fraction) -> tuple[Fraction, Fraction, Fraction]:
        return (Fraction(1), y, y * y + Fraction(1, 3))

    direct = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    conditioned = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for weight, t, s in atoms:
        vector = feature(t + s)
        for i in range(3):
            for j in range(3):
                direct[i][j] += weight * vector[i] * vector[j]

    by_t: dict[Fraction, list[tuple[Fraction, Fraction]]] = {}
    for weight, t, s in atoms:
        by_t.setdefault(t, []).append((weight, s))
    for t, rows in by_t.items():
        for weight, s in rows:
            vector = feature(t + s)
            for i in range(3):
                for j in range(3):
                    conditioned[i][j] += weight * vector[i] * vector[j]

    assert direct == conditioned
    assert direct[0][0] > 0
    assert direct[0][0] * direct[1][1] - direct[0][1] ** 2 >= 0
    return 9


def mutation_tests() -> int:
    passed = 0

    try:
        for h in range(2, 20):
            for q in range(2, 2 * h + 1):
                lhs = carry(2 * h, h - 1, q) - carry(2 * h, h, q)
                wrong = int((h + 1) % q == 0) - int(h % q == 0)
                assert lhs == wrong
    except AssertionError:
        passed += 1

    try:
        profile = [Fraction(0), Fraction(5), Fraction(4), Fraction(2), Fraction(0)]
        q = 2
        wrong = profile[2 * q]
        right = profile[2 * q - 1] - profile[2 * q]
        assert wrong == right
    except AssertionError:
        passed += 1

    assert abel_witness(520, 3, 15) < 0
    passed += 1
    assert abel_witness(10_000, 4, 7) < 0
    passed += 1

    u = Fraction(1, 2)
    v = Fraction(1, 2)
    m = 4
    assert (u * v) ** 4 < (Fraction(m) + u) / (m * (m + 1))
    passed += 1

    m = 2
    exp_minus_t_1 = Fraction(5, 12)
    exp_minus_t_2 = Fraction(11, 24)
    v1 = m * (m + 1) * exp_minus_t_1 - m
    v2 = m * (m + 1) * exp_minus_t_2 - m
    assert v1 != v2
    passed += 1

    return passed


def main() -> None:
    third = abel_witness(520, 3, 15)
    fourth = abel_witness(10_000, 4, 7)
    assert third == Fraction(-91, 256)
    assert fourth == Fraction(-10512404675923, 16384)

    result = {
        "classification": "EXACT_MARKOV_PASCAL_GLOBAL_ATTACK_ALGEBRA",
        "third_abel_witness": str(third),
        "fourth_abel_witness": str(fourth),
        "sibling_switch_rows": verify_sibling_switch(),
        "commutator_rows": verify_commutator(),
        "sibling_transport_rows": verify_sibling_transport(),
        "gamma_domination_rational_rows": verify_gamma_domination(),
        "matrix_lift_entries": verify_matrix_lift(),
        "mutation_tests": mutation_tests(),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
