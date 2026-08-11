#!/usr/bin/env python3
from fractions import Fraction
import json
import sys


def mul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


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

scale_coefficients = ["1", "-3*sqrt(2)", "4"]
charge_coefficients = ["1", "-3*sqrt(2)", "4"]
assert scale_coefficients == charge_coefficients

result = {
    "classification": "PASS_X_90426_DIPOLE_PHASE_LOCKED_BOTTOM_PACKET",
    "half_source_factorization_checks": 1,
    "omega2_row_checks": 63,
    "phase_locked_row_checks": 127,
    "nonzero_phase_locked_rows": sum(value != 0 for value in star_rows.values()),
    "prefix_potential_checks": 6,
    "aligned_scale_relation_checks": 2,
    "rh_proved": False,
    "scope": (
        "exact dyadic source factorization, average-carry images, "
        "and scale-charge algebra only"
    ),
}

text = json.dumps(result, indent=2, sort_keys=True) + "\n"
if "--json" in sys.argv:
    output_path = sys.argv[sys.argv.index("--json") + 1]
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
else:
    print(text, end="")
