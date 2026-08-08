from fractions import Fraction
from functools import lru_cache
from math import comb
import hashlib
import json


def floor_fraction(x):
    return x.numerator // x.denominator


def fracpart(x):
    return x - floor_fraction(x)


def carry_real(x, theta):
    return (
        floor_fraction(x)
        - floor_fraction(theta * x)
        - floor_fraction((1 - theta) * x)
    )


def primes_upto(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    primes = []
    for n in range(2, limit + 1):
        if sieve[n]:
            primes.append(n)
            if n * n <= limit:
                for m in range(n * n, limit + 1, n):
                    sieve[m] = False
    return primes


def factorization(n, primes):
    out = {}
    value = n
    for p in primes:
        if p * p > value:
            break
        if value % p == 0:
            exponent = 0
            while value % p == 0:
                value //= p
                exponent += 1
            out[p] = exponent
    if value > 1:
        out[value] = 1
    return out


def mobius_sieve(limit):
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def producer_value(X, Q, order, target_n, singleton=False):
    mu = mobius_sieve(X)
    w = [0] * (X + 1)
    if singleton:
        w[Q] = 1
    else:
        for q in range(2, Q + 1):
            w[q] = comb(Q - q + order - 1, order - 1)

    U = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        total = 0
        for k in range(1, X // m + 1):
            if mu[k]:
                total += mu[k] * w[m * k]
        U[m] = Fraction(total)

    residual = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        residual[m] = U[m] - U[m + 1]

    incoming = [Fraction(0) for _ in range(X + 2)]
    A = [Fraction(0) for _ in range(X + 2)]
    for m in range(X, 1, -1):
        A[m] = residual[m] + incoming[m]
        ternary = (m + 2) // 3
        binary = m // 2
        for child in (ternary, m - ternary, binary, m - binary):
            if child >= 2:
                incoming[child] += A[m] / 2
    return A[target_n]


@lru_cache(None)
def central_tree(n):
    if n <= 1:
        return ()
    child = n // 2
    return ((n, child),) + central_tree(child) + central_tree(n - child)


def carry_integer(n, j, q):
    return n // q - j // q - (n - j) // q


def main():
    nyman_rows = 0
    for denominator in range(1, 18):
        for numerator in range(1, denominator + 1):
            y = Fraction(numerator, denominator)
            x = 1 / y
            for theta_denominator in range(2, 16):
                for theta_numerator in range(1, theta_denominator):
                    theta = Fraction(theta_numerator, theta_denominator)
                    lhs = (
                        fracpart(theta / y)
                        - theta * fracpart(1 / y)
                        + fracpart((1 - theta) / y)
                        - (1 - theta) * fracpart(1 / y)
                    )
                    assert lhs == carry_real(x, theta)
                    nyman_rows += 1

    limit = 96
    primes = primes_upto(limit)
    weights = {p: index + 2 for index, p in enumerate(primes)}
    ell = [0] * (limit + 1)
    Lambda = [0] * (limit + 1)
    for n in range(2, limit + 1):
        factors = factorization(n, primes)
        ell[n] = sum(exponent * weights[p] for p, exponent in factors.items())
        if len(factors) == 1:
            p = next(iter(factors))
            Lambda[n] = weights[p]

    convolution = [0] * (limit + 1)
    selberg = [0] * (limit + 1)
    for n in range(1, limit + 1):
        convolution[n] = sum(
            Lambda[d] * Lambda[n // d]
            for d in range(1, n + 1)
            if n % d == 0
        )
        selberg[n] = Lambda[n] * ell[n] + convolution[n]
        assert sum(selberg[d] for d in range(1, n + 1) if n % d == 0) == ell[n] ** 2

    selberg_rows = 0
    for n in range(2, limit + 1):
        cumulative = [0] * (n + 1)
        running = 0
        for m in range(1, n + 1):
            running += ell[m] ** 2
            cumulative[m] = running
        for j in range(n + 1):
            row = sum(
                selberg[d] * carry_integer(n, j, d)
                for d in range(1, n + 1)
            )
            expected = cumulative[n] - cumulative[j] - cumulative[n - j]
            assert row == expected
            selberg_rows += 1

    factorial_ell = [0] * (limit + 1)
    for n in range(1, limit + 1):
        factorial_ell[n] = factorial_ell[n - 1] + ell[n]

    tree_carry_rows = 0
    tree_entropy_rows = 0
    for n in range(2, 65):
        tree = central_tree(n)
        for q in range(2, n + 1):
            load = sum(carry_integer(parent, child, q) for parent, child in tree)
            assert load == n // q
            if n >= 3:
                previous = central_tree(n - 1)
                difference = load - sum(
                    carry_integer(parent, child, q)
                    for parent, child in previous
                )
                assert difference == (1 if n % q == 0 else 0)
            tree_carry_rows += 1

        entropy = sum(
            factorial_ell[parent]
            - factorial_ell[child]
            - factorial_ell[parent - child]
            for parent, child in tree
        )
        assert entropy == factorial_ell[n]
        if n >= 3:
            previous_entropy = sum(
                factorial_ell[parent]
                - factorial_ell[child]
                - factorial_ell[parent - child]
                for parent, child in central_tree(n - 1)
            )
            assert entropy - previous_entropy == ell[n]
        tree_entropy_rows += 1

    witnesses = {
        "generic_X8_q4_n3": producer_value(8, 4, 1, 3, singleton=True),
        "order2_X60_Q59_n11": producer_value(60, 59, 2, 11),
        "order3_X520_Q520_n15": producer_value(520, 520, 3, 15),
        "order4_X8000_Q8000_n23": producer_value(8000, 8000, 4, 23),
    }
    expected_witnesses = {
        "generic_X8_q4_n3": Fraction(-1),
        "order2_X60_Q59_n11": Fraction(-13, 16),
        "order3_X520_Q520_n15": Fraction(-91, 256),
        "order4_X8000_Q8000_n23": Fraction(-1168054960769, 4096),
    }
    assert witnesses == expected_witnesses

    mutation_tests = 4
    assert (
        fracpart(Fraction(1, 2) / Fraction(2, 3))
        - Fraction(1, 2) * fracpart(1 / Fraction(2, 3))
        - (
            fracpart(Fraction(1, 2) / Fraction(2, 3))
            - Fraction(1, 2) * fracpart(1 / Fraction(2, 3))
        )
        != carry_real(Fraction(3, 2), Fraction(1, 2))
    )
    assert any(
        sum(Lambda[d] * ell[d] for d in range(1, n + 1) if n % d == 0)
        != ell[n] ** 2
        for n in range(2, limit + 1)
    )
    assert sum(carry_integer(8, 4, q) for q in (2,)) != 8 // 2
    assert witnesses["order3_X520_Q520_n15"] < 0

    result = {
        "schema": "riemann.x29001.atomized-carry-selberg-kummer.v1",
        "verified": True,
        "checks": {
            "nyman_carry_rows": nyman_rows,
            "formal_selberg_carry_rows": selberg_rows,
            "balanced_tree_carry_rows": tree_carry_rows,
            "balanced_tree_entropy_rows": tree_entropy_rows,
            "abel_witnesses": {
                key: str(value) for key, value in witnesses.items()
            },
            "mutation_tests": mutation_tests,
        },
        "verdict": "EXACT_ATOMIZED_CARRY_SELBERG_KUMMER_AND_TREE_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Exact finite floor, formal-log, tree, and Abel-counterexample "
            "algebra only; no atomized energy bound, ETSR recurrence, or RH "
            "claim is certified."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
