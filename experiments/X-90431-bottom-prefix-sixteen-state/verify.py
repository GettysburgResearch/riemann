#!/usr/bin/env python3
from fractions import Fraction
import json
import random
import sys


def mobius_table(limit):
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes = []
    least = [0] * (limit + 1)
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or p * n > limit:
                break
            least[p * n] = p
            if p == least[n]:
                mu[p * n] = 0
                break
            mu[p * n] = -mu[n]
    return mu


def beta(n, q):
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def invert_target(w, endpoint):
    c = [Fraction(0)] * (endpoint + 1)
    for q in range(endpoint, 1, -1):
        rhs = w[q] - sum(c[n] * beta(n, q) for n in range(q + 1, endpoint + 1))
        diagonal = beta(q, q)
        assert diagonal != 0
        c[q] = rhs / diagonal
    return c


def formula_prefix(u):
    c = {}
    prefix = Fraction(0)
    prefix_values = [Fraction(0)] * len(u)
    for m in range(1, len(u)):
        prefix += u[m]
        prefix_values[m] = prefix
    for j in range(2, 16):
        numerator = (
            (j + 1) * (j * u[j] - (j - 2) * u[j + 1])
            - 2 * prefix_values[j + 1]
        )
        c[j] = numerator / (j * (j - 1))
    return c


rng = random.Random(90431)
checks = 0
for endpoint in [16, 17, 24, 31, 40, 55]:
    mu = mobius_table(endpoint)
    for _ in range(12):
        w = [Fraction(0)] * (endpoint + 1)
        for q in range(2, endpoint + 1):
            w[q] = Fraction(rng.randint(-25, 25), rng.randint(1, 13))

        u = [Fraction(0)] * (endpoint + 1)
        for m in range(1, endpoint + 1):
            u[m] = sum(mu[k] * w[m * k] for k in range(1, endpoint // m + 1))
        assert sum(u[1:]) == 0

        direct = invert_target(w, endpoint)
        finite = formula_prefix(u[:17])
        for j in range(2, 16):
            assert direct[j] == finite[j]
            checks += 1

result = {
    "classification": "PASS_X_90431_BOTTOM_PREFIX_SIXTEEN_STATE",
    "random_targets": 72,
    "prefix_coefficient_checks": checks,
    "zero_total_adjoint_checks": 72,
    "pbvg_proved": False,
    "rh_proved": False,
    "scope": "exact finite carry inversion and Mobius-adjoint algebra only",
}
text = json.dumps(result, indent=2, sort_keys=True) + "\n"
if "--json" in sys.argv:
    output_path = sys.argv[sys.argv.index("--json") + 1]
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
else:
    print(text, end="")
