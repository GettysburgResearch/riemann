#!/usr/bin/env python3
"""Exact finite regressions for T-105200.

This replay checks polynomial reverse-Rolle/coherence algebra and the exact
Gaussian-model critical-residue formula. It does not prove the analytic
Laplace theorem, Xi asymptotics, the low-order coherence budget, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def trim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return trim([c * x for x in a])


def derivative(a: list[Fraction]) -> list[Fraction]:
    if len(a) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * a[i] for i in range(1, len(a))])


def integral(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(0)] + [a[i] / Fraction(i + 1) for i in range(len(a))]


def evaluate(a: list[Fraction], x: Fraction) -> Fraction:
    out = Fraction(0)
    for c in reversed(a):
        out = out * x + c
    return out


def divrem(
    a: list[Fraction], b: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    r = a[:]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while r != [0] and len(r) >= len(b):
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] = c
        for j in range(len(b)):
            r[k + j] -= c * b[j]
        r = trim(r)
    return trim(q), trim(r)


def sturm(a: list[Fraction]) -> list[list[Fraction]]:
    seq = [trim(a[:]), derivative(a)]
    while seq[-1] != [0]:
        _, rem = divrem(seq[-2], seq[-1])
        if rem == [0]:
            break
        seq.append(scale(rem, Fraction(-1)))
    return seq


def sign(x: Fraction) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def sign_at_infinity(a: list[Fraction], positive: bool) -> int:
    a = trim(a[:])
    out = sign(a[-1])
    if not positive and (len(a) - 1) % 2:
        out = -out
    return out


def variations(signs: list[int]) -> int:
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def count_real_roots(a: list[Fraction]) -> int:
    seq = sturm(a)
    left = variations([sign_at_infinity(p, False) for p in seq])
    right = variations([sign_at_infinity(p, True) for p in seq])
    return left - right


def polynomial_from_roots(roots: tuple[int, ...]) -> list[Fraction]:
    out = [Fraction(1)]
    for root in roots:
        out = mul(out, [Fraction(-root), Fraction(1)])
    return out


def check_polynomial_budgets() -> int:
    root_sets = [
        (-2, 0, 3),
        (-3, -1, 2, 4),
        (-4, -2, 1, 3, 5),
        (-5, -3, -1, 2, 4, 6),
        (-6, -4, -2, 1, 3, 5, 7),
    ]
    checks = 0
    for roots in root_sets:
        q = polynomial_from_roots(roots)
        degree = len(q)
        primitive = scale(integral(q), Fraction(degree))
        for constant in range(-20, 21):
            p = primitive[:]
            p[0] += Fraction(constant)
            p1 = derivative(p)
            p2 = derivative(p1)

            residues: list[Fraction] = []
            regular = True
            for c0 in roots:
                c = Fraction(c0)
                numerator = evaluate(p, c)
                denominator = evaluate(p2, c)
                if numerator == 0 or denominator == 0:
                    regular = False
                    break
                residues.append(numerator / denominator)
            if not regular:
                continue

            wrong = sum(rho > 0 for rho in residues)
            rcount = len(residues)
            first = max(Fraction(0), -sum(residues))
            second = sum(rho * rho for rho in residues)
            coherence = (
                first * first / (Fraction(rcount) * second)
                if second
                else Fraction(0)
            )

            assert Fraction(wrong) <= Fraction(rcount) * (1 - coherence)

            nonreal_p = (len(p) - 1) - count_real_roots(p)
            nonreal_p1 = (len(p1) - 1) - count_real_roots(p1)
            assert nonreal_p - nonreal_p1 == 2 * wrong

            assert nonreal_p <= nonreal_p1 + 2 * rcount * (1 - coherence)
            checks += 3
    return checks


def check_gaussian_model_residue() -> int:
    checks = 0
    for w_num in range(2, 15):
        for v_num in range(1, 8):
            for x_num in range(-10, 11):
                w = Fraction(w_num, 2)
                v = Fraction(v_num, 11)
                x = Fraction(x_num, 3)
                q = v * x / w

                logarithmic_derivative_slope = -v - w * w * (1 + q * q)
                denominator = w * w + v + v * v * x * x
                assert logarithmic_derivative_slope == -denominator
                residue = Fraction(1, 1) / logarithmic_derivative_slope
                assert residue == -Fraction(1, 1) / denominator
                assert residue < 0
                checks += 3
    return checks


def check_transfer_constants() -> int:
    checks = 0
    for num in range(0, 100):
        v2 = Fraction(num, 100)
        coherence = Fraction(1, 1) / (1 + v2)
        transfer = 2 * coherence - 1
        assert transfer == (1 - v2) / (1 + v2)
        assert coherence >= 0
        if v2 < 1:
            assert transfer > 0
        checks += 3
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "polynomial_budget_checks": check_polynomial_budgets(),
        "gaussian_model_residue_checks": check_gaussian_model_residue(),
        "transfer_constant_checks": check_transfer_constants(),
    }
    result = {
        "verdict": "PASS_X_105200_NATURAL_SCALE_RESIDUE_COHERENCE",
        "arithmetic_class": "EXACT_FRACTION_AND_STURM",
        "counts": counts,
        "analytic_gaussian_saddle_proved_by_replay": False,
        "low_order_coherence_budget_proved": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
