#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


LIMIT = 160
GRAM_LIMIT = 18
EXPECTED_SHA256 = "dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715"


def mobius_table(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
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


MU = mobius_table(max(2 * LIMIT, 4 * GRAM_LIMIT))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def b2(n: int) -> int:
    return MU[n] - (MU[n // 2] if n % 2 == 0 else 0)


def beta(n: int, q: int) -> Fraction:
    if q < 1 or q > n:
        return Fraction(0)
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def carry(n: int, j: int, q: int) -> int:
    if not (0 <= j <= n):
        raise ValueError("j outside row")
    return int((j % q) > (n % q))


def completely_additive_weight(n: int) -> int:
    out = 0
    p = 2
    weight = 1
    m = n
    while p * p <= m:
        while m % p == 0:
            out += weight
            m //= p
        p += 1
        while p > 2 and any(p % r == 0 for r in range(2, int(p**0.5) + 1)):
            p += 1
        weight += 1
    if m > 1:
        count = 0
        for candidate in range(2, m + 1):
            if all(candidate % r for r in range(2, int(candidate**0.5) + 1)):
                count += 1
        out += count
    return out


def prime_power_weight(q: int) -> int:
    for p in range(2, q + 1):
        if any(p % r == 0 for r in range(2, int(p**0.5) + 1)):
            continue
        x = p
        while x < q:
            x *= p
        if x == q:
            count = 0
            for candidate in range(2, p + 1):
                if all(candidate % r for r in range(2, int(candidate**0.5) + 1)):
                    count += 1
            return count
    return 0


def math_comb(n: int, j: int) -> int:
    if j < 0 or j > n:
        return 0
    j = min(j, n - j)
    out = 1
    for k in range(1, j + 1):
        out = out * (n - j + k) // k
    return out


def check_divisor_collapse() -> dict[str, int]:
    cases = 0
    for n in range(1, LIMIT + 1):
        value = sum(b2(d) for d in divisors(n))
        expected = 1 if n == 1 else (-1 if n == 2 else 0)
        if value != expected:
            raise AssertionError(("divisor collapse", n, value, expected))
        cases += 1
    return {"cases": cases}


def check_two_contact() -> dict[str, int]:
    cases = 0
    second_moment_cases = 0
    cross_cases = 0
    for n in range(2, LIMIT + 1):
        row = []
        for j in range(n + 1):
            value = sum(b2(q) * carry(n, j, q) for q in range(2, n + 1))
            expected = -(1 if j == 1 else 0) - (1 if j == n - 1 else 0)
            if value != expected:
                raise AssertionError(("two contact", n, j, value, expected))
            row.append(value)
            cases += 1

            log_binom = completely_additive_weight(math_comb(n, j))
            carry_log = sum(
                prime_power_weight(q) * carry(n, j, q)
                for q in range(2, n + 1)
                if prime_power_weight(q)
            )
            if carry_log != log_binom:
                raise AssertionError(("Kummer", n, j, carry_log, log_binom))
            cross_cases += 1

        square = sum(x * x for x in row)
        expected_square = 4 if n == 2 else 2
        if square != expected_square:
            raise AssertionError(("square", n, square, expected_square))
        additive_n = completely_additive_weight(n)
        cross = sum(
            row[j] * completely_additive_weight(math_comb(n, j))
            for j in range(n + 1)
        )
        if cross != -2 * additive_n:
            raise AssertionError(("cross", n, cross, -2 * additive_n))
        second_moment_cases += 1
    return {
        "pointwise_cases": cases,
        "second_moment_rows": second_moment_cases,
        "formal_cross_cases": cross_cases,
    }


def check_average_collapse() -> dict[str, int]:
    cases = 0
    for n in range(2, LIMIT + 1):
        for m in range(1, n + 1):
            lhs = sum(
                b2(k) * beta(n, m * k)
                for k in range(1, n // m + 1)
            )
            if 2 * m <= n:
                rhs = Fraction(-2 * m, n + 1)
            else:
                rhs = Fraction(2 * m - n - 1, n + 1)
            if lhs != rhs:
                raise AssertionError(("average collapse", n, m, lhs, rhs))
            cases += 1
    return {"cases": cases}


def deterministic_target(X: int, q: int) -> Fraction:
    return Fraction((7 * q + 3) % 19 + 1, (q + 2) * (X + 3))


def deterministic_coeff(X: int, n: int) -> Fraction:
    return Fraction((5 * n + 1) % 11, (n + 1) * (X + 5))


def check_residual_pairing() -> dict[str, int]:
    endpoints = [17, 31, 47]
    cases = 0
    for X in endpoints:
        d = [Fraction(0)] * (X + 1)
        for n in range(2, X + 1):
            d[n] = deterministic_coeff(X, n)
        w = [Fraction(0)] * (X + 1)
        s = [Fraction(0)] * (X + 1)
        for q in range(2, X + 1):
            w[q] = deterministic_target(X, q)
            used = sum(d[n] * beta(n, q) for n in range(q, X + 1))
            s[q] = w[q] - used

        lhs = sum(Fraction(b2(q)) * s[q] for q in range(2, X + 1))
        riesz = sum(Fraction(b2(q)) * w[q] for q in range(2, X + 1))
        harmonic = sum(d[n] / (n + 1) for n in range(2, X + 1))
        rhs = riesz + 2 * harmonic
        if lhs != rhs:
            raise AssertionError(("residual pairing", X, lhs, rhs))
        cases += 1
    return {"endpoints": cases}


def check_adjacent_flow_potential() -> dict[str, int]:
    endpoints = [19, 37, 61]
    cases = 0
    for X in endpoints:
        w = [Fraction(0)] * (X + 1)
        d = [Fraction(0)] * (X + 1)
        F = [Fraction(0)] * (X + 1)
        for q in range(2, X + 1):
            w[q] = deterministic_target(X, q)
        for n in range(2, X + 1):
            d[n] = deterministic_coeff(X, n)
        for j in range(2, X):
            F[j] = Fraction((3 * j + 2) % 7, (j + 3) * (X + 7))

        def residual(vector: list[Fraction]) -> list[Fraction]:
            out = [Fraction(0)] * (X + 1)
            for q in range(2, X + 1):
                out[q] = w[q] - sum(
                    vector[n] * beta(n, q) for n in range(q, X + 1)
                )
            return out

        shifted = d[:]
        for n in range(2, X + 1):
            shifted[n] += F[n - 1] - F[n]

        s0 = residual(d)
        s1 = residual(shifted)
        delta = sum(
            Fraction(b2(q)) * (s1[q] - s0[q])
            for q in range(2, X + 1)
        )
        expected = -sum(
            Fraction(2) * F[j] / ((j + 1) * (j + 2))
            for j in range(2, X)
        )
        if delta != expected:
            raise AssertionError(("flow potential", X, delta, expected))
        cases += 1
    return {"endpoints": cases}


def build_unprojected_gram(X: int) -> tuple[list[int], list[list[Fraction]]]:
    qs = list(range(2, X + 1))
    gradients: dict[int, list[Fraction]] = {}
    for q in qs:
        u = [Fraction(0)] * (X + 1)
        for j in range(1, X + 1):
            u[j] = Fraction(1 if j % q == 0 else 0)
        gradients[q] = [u[j + 1] - u[j] for j in range(X)]
    gram = [
        [
            sum(gradients[q][j] * gradients[r][j] for j in range(X))
            for r in qs
        ]
        for q in qs
    ]
    return qs, gram


def matrix_inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = [
        row[:] + [Fraction(1 if i == j else 0) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        m[col], m[pivot] = m[pivot], m[col]
        scale = m[col][col]
        m[col] = [x / scale for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                factor = m[r][col]
                m[r] = [
                    m[r][k] - factor * m[col][k] for k in range(2 * n)
                ]
    return [row[n:] for row in m]


def inverse_formula(a: int, b: int) -> int:
    return sum(
        MU[a // d] * MU[b // e] * min(d, e)
        for d in divisors(a)
        for e in divisors(b)
    )


def check_green_two_charge() -> dict[str, object]:
    checked = []
    for X in range(3, GRAM_LIMIT + 1):
        qs, gram = build_unprojected_gram(X)
        vector = [Fraction(b2(q)) for q in qs]
        image = [
            sum(gram[i][j] * vector[j] for j in range(len(qs)))
            for i in range(len(qs))
        ]
        expected = [
            Fraction(-3 if q == 2 else (1 if q == 3 else 0))
            for q in qs
        ]
        if image != expected:
            raise AssertionError(("green charge", X, image, expected))
        energy = sum(vector[i] * image[i] for i in range(len(qs)))
        if energy != 5:
            raise AssertionError(("green energy", X, energy))

        inverse = matrix_inverse(gram)
        formula = [
            [Fraction(inverse_formula(a, b)) for b in qs]
            for a in qs
        ]
        if inverse != formula:
            raise AssertionError(("inverse formula", X))
        checked.append({"X": X, "dimension": len(qs), "energy": 5})
    return {"instances": checked}


def check_dyadic_layer_formula() -> dict[str, int]:
    cases = 0
    for m in range(1, LIMIT + 1, 2):
        expected = [MU[m], -2 * MU[m], MU[m], 0, 0]
        values = []
        for exponent in range(5):
            n = (2**exponent) * m
            if n > len(MU) - 1:
                break
            values.append(b2(n))
        if values != expected[:len(values)]:
            raise AssertionError(("dyadic layer", m, values, expected))
        cases += len(values)
    return {"cases": cases}


def check_log_weight_rational_envelope() -> dict[str, int]:
    cases = 0
    for j in range(2, 1000):
        a = Fraction(2, (j + 1) * (j + 2))
        lower_for_log = Fraction(1, j * j)
        upper_for_log = Fraction(1, j * j - 1)
        if not (a >= upper_for_log / 2):
            raise AssertionError(("lower envelope", j, a, upper_for_log / 2))
        if not (a <= 2 * lower_for_log):
            raise AssertionError(("upper envelope", j, a, 2 * lower_for_log))
        cases += 1
    return {"cases": cases}


def build_result() -> dict[str, object]:
    return {
        "schema": "X-26201-dyadic-carry-bridge-v1",
        "checks": {
            "divisor_collapse": check_divisor_collapse(),
            "pointwise_two_contact": check_two_contact(),
            "average_rank_one_collapse": check_average_collapse(),
            "signed_residual_pairing": check_residual_pairing(),
            "adjacent_flow_potential": check_adjacent_flow_potential(),
            "unprojected_green_two_charge": check_green_two_charge(),
            "dyadic_layer_formula": check_dyadic_layer_formula(),
            "flow_cost_rational_envelope": check_log_weight_rational_envelope(),
        },
        "scope": (
            "exact finite algebra only; does not prove Dyadic Signed Slack, "
            "Parity-Dipole Descent, a Green-to-normal transference, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(("proof-object digest mismatch", digest, EXPECTED_SHA256))
    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out_path = Path(__file__).with_name("results") / "verification.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
