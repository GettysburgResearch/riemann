#!/usr/bin/env python3
"""Finite checks for the one-safe-line polynomial theorem L-90906."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp


def polynomial_rows(max_k: int) -> list[list[int]]:
    rows = [[1, 1, -1]]
    for k in range(max_k):
        old = rows[-1]
        new = []
        for j in range(len(old) + 1):
            left = old[j - 1] if j - 1 >= 0 else 0
            diag = (2 * k + 3 - j) * old[j] if j < len(old) else 0
            new.append(left + diag)
        rows.append(new)
    return rows


def sign_variations(row: list[int]) -> int:
    signs = [1 if x > 0 else -1 for x in row if x != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def eval_poly(row: list[int], x: mp.mpf) -> mp.mpf:
    total = mp.mpf("0")
    for coeff in reversed(row):
        total = total * x + coeff
    return total


def positive_root(row: list[int], k: int) -> mp.mpf:
    lo = mp.sqrt(2 * k + 2)
    hi = mp.sqrt(2 * k + 3)
    flo = eval_poly(row, lo)
    fhi = eval_poly(row, hi)
    if not (flo > 0 and fhi < 0):
        raise AssertionError((k, flo, fhi))
    for _ in range(180):
        mid = (lo + hi) / 2
        if eval_poly(row, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def gamma_integral(k: int, t: mp.mpf) -> mp.mpf:
    return mp.quad(
        lambda q: q ** (k + mp.mpf("0.5"))
        * mp.e ** (-q - t * t / (4 * q))
        * (1 - t * t / (2 * q)),
        [0, mp.inf],
    ) / mp.sqrt(mp.pi)


def main() -> dict:
    mp.mp.dps = 70
    max_k = 60
    rows = polynomial_rows(max_k)

    exact_gates = []
    roots = []
    previous = mp.mpf("0")
    for k, row in enumerate(rows):
        assert row[0] == math.prod(range(1, 2 * k + 2, 2))
        assert row[-1] == -1
        assert sign_variations(row) == 1
        root = positive_root(row, k)
        assert root > previous
        previous = root
        roots.append(root)
        exact_gates.append(2 * k + 2 < root * root < 2 * k + 3)

    # Recurrence checked independently at generic rational points.
    recurrence_checks = 0
    for k in range(max_k):
        old = rows[k]
        new = rows[k + 1]
        for num, den in [(1, 3), (7, 5), (11, 4)]:
            x = Fraction(num, den)
            q = sum(Fraction(c) * x**j for j, c in enumerate(old))
            dq = sum(Fraction(j * c) * x ** (j - 1) for j, c in enumerate(old) if j)
            rhs = (x + 2 * k + 3) * q - x * dq
            lhs = sum(Fraction(c) * x**j for j, c in enumerate(new))
            assert lhs == rhs
            recurrence_checks += 1

    # Gamma integral: P_k=Q_k/2^(k+1).
    max_integral_error = mp.mpf("0")
    integral_samples = []
    for k in range(0, 9):
        for t_text in ("0.4", "1.1", "2.7", "4.3"):
            t = mp.mpf(t_text)
            p = eval_poly(rows[k], t) / (2 ** (k + 1))
            direct = mp.e ** (-t) * p
            integral = gamma_integral(k, t)
            error = abs(direct - integral)
            max_integral_error = max(max_integral_error, error)
            integral_samples.append([k, float(t), float(error)])

    gates = {
        "coefficient_endpoints": all(row[0] > 0 and row[-1] == -1 for row in rows),
        "one_sign_variation": all(sign_variations(row) == 1 for row in rows),
        "sharp_root_window": all(exact_gates),
        "strict_root_monotonicity": all(roots[i + 1] > roots[i] for i in range(len(roots) - 1)),
        "exact_polynomial_recurrence": recurrence_checks == 3 * max_k,
        "gamma_integral_identity": max_integral_error < mp.mpf("1e-55"),
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    selected = [0, 1, 2, 3, 5, 10, 20, 40, 60]
    return {
        "status": "PASS_X_90905_SAFE_LINE_POLYNOMIALS",
        "gates": gates,
        "orders_checked": max_k + 1,
        "recurrence_checks": recurrence_checks,
        "selected_roots": {
            str(k): {
                "tau": float(roots[k]),
                "tau_squared_minus_2k_plus_2": float(roots[k] ** 2 - (2 * k + 2)),
            }
            for k in selected
        },
        "max_gamma_integral_error": float(max_integral_error),
        "integral_sample_count": len(integral_samples),
        "scope": "Finite exact/high-precision polynomial checks only; no Riemann-data sign and no RH claim.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end=")
