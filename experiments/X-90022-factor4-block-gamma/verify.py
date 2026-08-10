#!/usr/bin/env python3
"""Replay for L-90026.

Authenticates the geometric-delay transform, exact means and critical moment,
the elementary density-envelope constants, and a high-precision stop-loss scan.
The convex-order proof itself is the analytic argument in the claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent


def constants() -> dict[str, str]:
    mp.mp.dps = 80
    gamma = mp.euler
    log4 = mp.log(4)
    mean_y = 3 - gamma - log4
    shift = 4 - mean_y

    def phi_v(s):
        if s == 0:
            return mp.mpf(1)
        return s * mp.zeta(s + 1) / ((s + 1) * (2 * s + 1))

    def phi_y(s):
        if s == 0:
            return mp.mpf(1)
        return (2 - mp.power(4, -s)) * phi_v(s)

    mean_transform = -mp.diff(phi_y, 0)
    if abs(mean_transform - mean_y) > mp.mpf("1e-60"):
        raise AssertionError((mean_transform, mean_y))

    gamma_moment = mp.mpf(16) / 9
    y_shifted_moment = mp.e ** (shift / 8) * phi_y(mp.mpf(-1) / 8)
    rho = y_shifted_moment / gamma_moment
    if not (0 < rho < 1):
        raise AssertionError(rho)

    return {
        "mean_Y": mp.nstr(mean_y, 65),
        "centering_shift": mp.nstr(shift, 65),
        "critical_shifted_Y_moment": mp.nstr(y_shifted_moment, 65),
        "gamma_critical_moment": mp.nstr(gamma_moment, 65),
        "critical_ratio": mp.nstr(rho, 65),
        "geometric_delay_mean": mp.nstr(log4, 65),
    }


def elementary_inequalities() -> dict[str, object]:
    # Exact rational checks used in the two stop-loss ranges.
    if not (10 * 10 * 7 < 27 * 27):
        raise AssertionError("10 sqrt(7) < 27 certificate failed")
    if not (700 < 729):
        raise AssertionError("density envelope certificate failed")
    if not (16 * 20 > 15 * 21):
        raise AssertionError("16/15 > 21/20 failed")
    if not (27 * 20 < 4 * 159):
        raise AssertionError("27/4 < 159/20 failed")
    return {
        "density_envelope": "f_Y(t) < (9/4) exp(-t)",
        "sqrt7_certificate": "700 < 729",
        "small_threshold_margin": "16/15 > 21/20",
        "large_threshold_margin": "27/4 < 159/20",
    }


def carry_tail(t: mp.mpf) -> mp.mpf:
    x = mp.e**t
    n = int(mp.floor(x))
    u = n * (n + 1 - x) / x
    return mp.mpf(1) / (n + 1) + u * u / (n * (n + 1))


def varrho(t: mp.mpf) -> mp.mpf:
    if t < 0:
        return mp.mpf(0)
    x = mp.e**t
    n = int(mp.floor(x))
    s = mp.fsum(mp.mpf(1) / mp.sqrt(k) for k in range(1, n + 1))
    return 2 * n / mp.sqrt(x) - s


def f_y(t: mp.mpf) -> mp.mpf:
    if t < 0:
        return mp.mpf(0)
    return mp.e ** (-t / 2) * (varrho(t) - varrho(t - mp.log(4)))


def numerical_stop_loss(max_b: int, step: mp.mpf) -> dict[str, str]:
    # Numerical quadrature is only a regression for the analytic proof.
    mp.mp.dps = 50
    gamma = mp.euler
    shift = 1 + gamma + mp.log(4)

    def gamma_sl(a):
        if a <= 0:
            return 4 - a
        return (a + 4) * mp.e ** (-a / 2)

    minimum = mp.inf
    where = mp.mpf(0)
    b = mp.mpf(0)
    while b <= max_b:
        # Split at logarithmic integer knots for stable quadrature.
        upper = max(mp.mpf(30), b + 25)
        start_n = max(1, int(mp.floor(mp.e**b)))
        end_n = int(mp.floor(mp.e**upper))
        # Avoid enumerating an enormous number of knots: direct quadrature is
        # used on a modest retained range, with the analytic tail bound beyond.
        cutoff = min(upper, mp.mpf(12))
        knots = [b]
        n0 = max(1, start_n)
        n1 = int(mp.floor(mp.e**cutoff))
        for n in range(n0 + 1, n1 + 1):
            knot = mp.log(n)
            if b < knot < cutoff:
                knots.append(knot)
        knots.append(cutoff)
        sl = mp.quad(lambda t: (t - b) * f_y(t), knots)
        if cutoff < upper:
            # f_Y <= (9/4)e^-t gives this rigorous numerical-tail envelope.
            sl += mp.mpf(9) / 4 * mp.e ** (-cutoff) * (1 + cutoff - b)
        difference = gamma_sl(shift + b) - sl
        if difference < minimum:
            minimum = difference
            where = b
        if difference <= 0:
            raise AssertionError((b, difference))
        b += step
    return {
        "minimum_sampled_stop_loss_margin": mp.nstr(minimum, 35),
        "sampled_at_b": mp.nstr(where, 20),
        "maximum_b": str(max_b),
        "step": str(step),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=8)
    parser.add_argument("--step", type=str, default="0.05")
    parser.add_argument(
        "--output", type=Path, default=HERE / "results" / "verification.json"
    )
    args = parser.parse_args()
    result = {
        "classification": "PASS_FACTOR4_BLOCK_GAMMA_MARTINGALE",
        "constants": constants(),
        "elementary": elementary_inequalities(),
        "stop_loss_regression": numerical_stop_loss(
            args.max_b, mp.mpf(args.step)
        ),
        "scope": (
            "The transform and rational inequalities authenticate the proof. "
            "The stop-loss grid is regression only; L-90026 proves all thresholds."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(args.output)


if __name__ == "__main__":
    main()
