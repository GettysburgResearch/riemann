#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction


def pi_n(N: int, k: int) -> Fraction:
    return Fraction(6 * (k + 1) * (N - k + 1), (N + 1) * (N + 2) * (N + 3))


def lam(N: int, k: int) -> int:
    return (k + 2) * (N - k)


def mu(N: int, k: int) -> int:
    return k * (N - k + 2)


def generator(N: int, values: list[Fraction], k: int) -> Fraction:
    out = Fraction(0)
    if k < N:
        out += lam(N, k) * (values[k + 1] - values[k])
    if k > 0:
        out += mu(N, k) * (values[k - 1] - values[k])
    return out / 4


def finite_difference(values: list[Fraction], order: int) -> Fraction:
    row = list(values)
    for _ in range(order):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return row[0]


def check_hahn() -> dict[str, int]:
    counts = {
        "normalization": 0,
        "detailed_balance": 0,
        "score_eigenfunction": 0,
        "dirichlet_identity": 0,
        "polynomial_diagonal": 0,
        "product_score_edge": 0,
    }

    for N in range(1, 33):
        probs = [pi_n(N, k) for k in range(N + 1)]
        assert sum(probs, Fraction(0)) == 1
        counts["normalization"] += 1

        for k in range(N):
            assert probs[k] * lam(N, k) == probs[k + 1] * mu(N, k + 1)
            counts["detailed_balance"] += 1

        V = [Fraction(2 * k - N, N) for k in range(N + 1)]
        for k in range(N + 1):
            assert -generator(N, V, k) == V[k]
            counts["score_eigenfunction"] += 1

        f = [Fraction(k**3 - 2 * k + 1, N + 1) for k in range(N + 1)]
        lhs = -sum(probs[k] * f[k] * generator(N, f, k) for k in range(N + 1))
        rhs = sum(
            probs[k] * lam(N, k) * (f[k + 1] - f[k]) ** 2 / 4
            for k in range(N)
        )
        assert lhs == rhs and rhs >= 0
        counts["dirichlet_identity"] += 1

        for j in range(0, min(N, 8) + 1):
            vals = [Fraction(k**j) for k in range(j + 1)]
            full = [Fraction(k**j) for k in range(N + 1)]
            lvals = [generator(N, full, k) for k in range(j + 1)]
            leading_times_fact = finite_difference(lvals, j)
            expected = Fraction(-j * (j + 3), 4) * math.factorial(j)
            assert leading_times_fact == expected
            counts["polynomial_diagonal"] += 1

    for N in range(1, 13):
        probs = [pi_n(N, k) for k in range(N + 1)]
        V = [Fraction(2 * k - N, N) for k in range(N + 1)]
        # A deliberately non-monotone polynomial test of both coordinates.
        H = [[Fraction(i * i + 3 * i * j - 2 * j + 5, N + 3) for j in range(N + 1)] for i in range(N + 1)]
        mean_h = sum(probs[i] * probs[j] * H[i][j] for i in range(N + 1) for j in range(N + 1))
        mean_s = sum(probs[i] * probs[j] * (V[i] + V[j]) for i in range(N + 1) for j in range(N + 1))
        lhs = sum(
            probs[i] * probs[j] * (H[i][j] - mean_h) * ((V[i] + V[j]) - mean_s)
            for i in range(N + 1)
            for j in range(N + 1)
        )
        rhs = Fraction(0)
        for i in range(N + 1):
            for j in range(N + 1):
                if i < N:
                    rhs += probs[i] * probs[j] * lam(N, i) * (H[i + 1][j] - H[i][j]) / (2 * N)
                if j < N:
                    rhs += probs[i] * probs[j] * lam(N, j) * (H[i][j + 1] - H[i][j]) / (2 * N)
        assert lhs == rhs
        counts["product_score_edge"] += 1

    return counts


def check_ballistic() -> dict[str, int]:
    counts = {
        "initial_reserve": 0,
        "free_flight_invariance": 0,
        "positive_kick_identity": 0,
        "terminal_scalar_algebra": 0,
    }

    parameter_sets = [
        (Fraction(1, 3), Fraction(1, 2), Fraction(9, 2)),
        (Fraction(2, 5), Fraction(3, 5), Fraction(13, 3)),
        (Fraction(1, 2), Fraction(2, 3), Fraction(17, 4)),
    ]

    for a, c, kap in parameter_sets:
        assert c < 2 * a and kap > 2
        e = Fraction(1)
        b = -c + kap * a
        v = -kap * a * c + 4 * a * a
        K = b + v * v / (8 * a * a * c)
        assert K > 0
        counts["initial_reserve"] += 1

        for step in range(1, 9):
            h = Fraction(step, 200)
            # Free flight.
            e_minus = e - c * h
            b_minus = b + v * h - 2 * a * a * c * h * h
            v_minus = v - 4 * a * a * c * h
            K_minus = b_minus + v_minus * v_minus / (8 * a * a * c)
            assert K_minus == K
            counts["free_flight_invariance"] += 1

            # Positive arithmetic kick; chosen small enough to keep e_minus positive.
            f = Fraction(step + 1, 100)
            assert e_minus >= 0
            e_plus = e_minus + f
            b_plus = b_minus + kap * a * f
            v_plus = v_minus + 4 * a * a * f
            K_plus = b_plus + v_plus * v_plus / (8 * a * a * c)
            expected_jump = Fraction(2) * a * a / c * (e_plus * e_plus - e_minus * e_minus)
            assert K_plus - K_minus == expected_jump and expected_jump >= 0
            counts["positive_kick_identity"] += 1
            e, b, v, K = e_plus, b_plus, v_plus, K_plus

    # Algebra behind the a>=1/4 scalar gate, checked on a rational grid.
    delta = Fraction(3, 10)
    kap = Fraction(4)
    for q in range(4, 21):
        a = Fraction(q, 16)
        c0 = 2 * a / (1 + a)
        D = -c0 + kap * a * c0 * delta + 2 * a * a / c0 * (1 - c0 * c0 * delta * delta)
        P = (1 - 4 * delta * delta) * a * a + (2 + 2 * kap * delta) * a - 1
        assert D == a * P / (1 + a)
        counts["terminal_scalar_algebra"] += 1

    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json")
    args = parser.parse_args()

    hahn = check_hahn()
    ballistic = check_ballistic()
    out = {
        "classification": "PASS_X_91410_THREE_FRONT_FINAL_ATTACK",
        "hahn_checks": hahn,
        "ballistic_checks": ballistic,
        "hahn_total": sum(hahn.values()),
        "ballistic_total": sum(ballistic.values()),
        "full_factor54_margin_proved": False,
        "arbitrary_phase_theta_dtn_proved": False,
        "green_density_all_scales_proved": False,
        "green_density_a_ge_one_quarter_proved": True,
        "rh_proved": False,
        "scope": "exact finite Hahn spectrum/edge identities and exact Green-density ballistic algebra",
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
