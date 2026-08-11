#!/usr/bin/env python3
from fractions import Fraction
import json
import random
import sys


def mul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


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


P = [Fraction(1), Fraction(-3, 2), Fraction(1, 2)]
P_ADJ = [Fraction(1), Fraction(-6), Fraction(8)]
P_STAR = mul(P, P_ADJ)
assert P_STAR == [
    Fraction(1),
    Fraction(-15, 2),
    Fraction(35, 2),
    Fraction(-15),
    Fraction(4),
]


def prefix_from_poly(poly, n):
    return sum(poly[r] for r in range(len(poly)) if 2**r <= n)


def avg_carry_from_prefix(poly, n):
    h_n = prefix_from_poly(poly, n)
    return h_n - Fraction(2, n + 1) * sum(
        prefix_from_poly(poly, j) for j in range(n + 1)
    )


omega_rows = {n: avg_carry_from_prefix(P, n) for n in range(2, 65)}
assert omega_rows[2] == Fraction(-5, 6)
assert omega_rows[3] == Fraction(-1, 2)
assert all(omega_rows[n] == 0 for n in range(4, 65))

star_rows = {n: avg_carry_from_prefix(P_STAR, n) for n in range(2, 129)}
expected = {2: Fraction(-17, 6), 3: Fraction(-1, 2)}
for n in range(4, 8):
    expected[n] = Fraction(101 - 11 * n, n + 1)
for n in range(8, 16):
    expected[n] = Fraction(4 * (n - 31), n + 1)
for n, value in expected.items():
    assert star_rows[n] == value
assert all(star_rows[n] == 0 for n in range(16, 129))

assert prefix_from_poly(P_STAR, 1) == 1
assert prefix_from_poly(P_STAR, 2) == Fraction(-13, 2)
assert prefix_from_poly(P_STAR, 4) == 11
assert prefix_from_poly(P_STAR, 8) == -4
assert prefix_from_poly(P_STAR, 16) == 0
assert sum(prefix_from_poly(P_STAR, j) for j in range(16)) == 0

# Symbolic gauge arithmetic in Q(sqrt(2)), represented by pairs (a,b).
def add_pair(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale_pair(q, x):
    return (q * x[0], q * x[1])


# Full relation coefficients: 1, -3 sqrt(2), 4.
full_log_coefficient = add_pair(
    add_pair((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-3))),
    (Fraction(4), Fraction(0)),
)
# Delete the b_*(1) log X term.
excluded_log_coefficient = add_pair(full_log_coefficient, (Fraction(-1), 0))
assert excluded_log_coefficient == (Fraction(4), Fraction(-3))
# Constants from log(X/2), log(X/4).
excluded_log2_constant = add_pair(
    (Fraction(-8), Fraction(0)),
    (Fraction(0), Fraction(3)),
)
assert excluded_log2_constant == (Fraction(-8), Fraction(3))

# Verify the mandatory u_1 state by finite convolution on random targets.
LIMIT = 96
mu = mobius_table(LIMIT)
b_star = [Fraction(0)] * (LIMIT + 1)
for r, coefficient in enumerate(P_STAR):
    d = 2**r
    for m in range(1, LIMIT // d + 1):
        b_star[d * m] += coefficient * mu[m]

rng = random.Random(90426)
adjoint_checks = 0
for _ in range(48):
    endpoint = rng.randint(16, LIMIT)
    w = [Fraction(0)] * (endpoint + 1)
    # Column one is deliberately deleted.
    for q in range(2, endpoint + 1):
        w[q] = Fraction(rng.randint(-20, 20), rng.randint(1, 11))

    lhs = sum(b_star[q] * w[q] for q in range(2, endpoint + 1))
    u = {}
    for m in [1, 2, 4, 8, 16]:
        u[m] = sum(
            mu[k] * w[m * k]
            for k in range(1, endpoint // m + 1)
        )
    rhs = (
        u[1]
        - Fraction(15, 2) * u[2]
        + Fraction(35, 2) * u[4]
        - 15 * u[8]
        + 4 * u[16]
    )
    assert lhs == rhs

    without_u1 = rhs - u[1]
    if u[1] != 0:
        assert lhs != without_u1
    adjoint_checks += 1

result = {
    "classification": "PASS_X_90426_DIPOLE_PHASE_LOCKED_BOTTOM_PACKET",
    "half_source_factorization_checks": 1,
    "omega2_row_checks": 63,
    "phase_locked_row_checks": 127,
    "nonzero_phase_locked_rows": sum(value != 0 for value in star_rows.values()),
    "prefix_potential_checks": 6,
    "full_vs_deleted_gauge_checks": 2,
    "mandatory_u1_adjoint_checks": adjoint_checks,
    "rh_proved": False,
    "scope": (
        "exact dyadic source factorization, average-carry images, "
        "column-one gauges, and finite Möbius-adjoint algebra only"
    ),
}

text = json.dumps(result, indent=2, sort_keys=True) + "\n"
if "--json" in sys.argv:
    output_path = sys.argv[sys.argv.index("--json") + 1]
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
else:
    print(text, end="")
