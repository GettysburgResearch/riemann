#!/usr/bin/env python3
from fractions import Fraction
import json
import random
import sys

Y = {2: Fraction(-17, 6), 3: Fraction(-1, 2)}
for n in range(4, 8):
    Y[n] = Fraction(101 - 11 * n, n + 1)
for n in range(8, 16):
    Y[n] = Fraction(4 * (n - 31), n + 1)

S = {16: Fraction(0)}
running = Fraction(0)
for n in range(15, 1, -1):
    running += Y[n]
    S[n] = running
assert all(S[n] < 0 for n in range(2, 16))


def lhs(c):
    return sum(Y[n] * c[n] for n in range(2, 16))


def abel(c):
    return S[2] * c[2] + sum(
        S[n] * (c[n] - c[n - 1]) for n in range(3, 16)
    )


def upper(c):
    return S[2] * c[2] + sum(
        (-S[n]) * max(c[n - 1] - c[n], Fraction(0))
        for n in range(3, 16)
    )


checks = 0
for k in range(2, 16):
    c = {n: Fraction(int(n == k)) for n in range(2, 16)}
    assert lhs(c) == abel(c)
    assert lhs(c) <= upper(c)
    checks += 1

for slope in range(-4, 5):
    for intercept in range(-3, 4):
        c = {n: Fraction(intercept + slope * n) for n in range(2, 16)}
        assert lhs(c) == abel(c)
        assert lhs(c) <= upper(c)
        checks += 1

rng = random.Random(90428)
for _ in range(256):
    c = {
        n: Fraction(rng.randint(-20, 20), rng.randint(1, 9))
        for n in range(2, 16)
    }
    assert lhs(c) == abel(c)
    assert lhs(c) <= upper(c)
    checks += 1

result = {
    "classification": "PASS_X_90428_PHASE_LOCKED_BOTTOM_VARIATION",
    "suffix_sign_checks": 14,
    "abel_and_upper_bound_checks": checks,
    "pbvg_proved_for_critical_inverse": False,
    "rh_proved": False,
    "scope": "finite fourteen-row suffix and Abel-variation algebra only",
}
text = json.dumps(result, indent=2, sort_keys=True) + "\n"
if "--json" in sys.argv:
    output_path = sys.argv[sys.argv.index("--json") + 1]
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
else:
    print(text, end="")
