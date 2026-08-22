#!/usr/bin/env python3
"""Regression and algebra checks for L-90015 / T-90011.

Authenticates:
  * the exact 3,-7,5,-1 filter moments;
  * the RH-side constant/absolute-zero-sum margin numerically;
  * exact radical-switching evaluation of A_N;
  * negativity of the filtered scalar at every multiple of 729 through --max-x;
  * direct annular-kernel reconstruction at selected endpoints.

The finite scan is discovery/regression only. The Mellin/Landau implications
and the RH-conditional contour shift are mathematical arguments in the claims.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Tuple

import mpmath as mp
import numpy as np

COEFF = np.array([3.0, -7.0, 5.0, -1.0])
RADIX = 9
DEPTH = 3
ANNULUS = RADIX ** DEPTH


def constants() -> dict:
    mp.mp.dps = 80
    half = mp.mpf("0.5")

    def xi(s):
        return (
            mp.mpf("0.5") * s * (s - 1)
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2) * mp.zeta(s)
        )

    zeta_half = mp.zeta(half)
    zero_square_mass = mp.diff(lambda s: mp.log(xi(s)), half, 2)
    moat_constant = (1 + zeta_half) * mp.log(9) ** 2
    absolute_zero_bound = 16 * zero_square_mass
    margin = moat_constant + absolute_zero_bound

    if not (mp.mpf("-2.223") < moat_constant < mp.mpf("-2.222")):
        raise AssertionError("moat constant outside retained interval")
    if not (mp.mpf("0.739") < absolute_zero_bound < mp.mpf("0.740")):
        raise AssertionError("zero-square bound outside retained interval")
    if not margin < mp.mpf("-1.48"):
        raise AssertionError("strict RH-side margin failed")

    return {
        "zeta_half": mp.nstr(zeta_half, 60),
        "zero_square_mass_logxi_second": mp.nstr(zero_square_mass, 60),
        "moat_constant": mp.nstr(moat_constant, 60),
        "absolute_zero_bound": mp.nstr(absolute_zero_bound, 60),
        "margin_upper_bound": mp.nstr(margin, 60),
    }


def algebra() -> dict:
    coeff = [3, -7, 5, -1]
    moment_0 = sum(coeff)
    moment_1 = sum(j * coeff[j] for j in range(4))
    critical_moment = sum(coeff[j] * (3 ** j) for j in range(4))
    if (moment_0, moment_1, critical_moment) != (0, 0, 0):
        raise AssertionError("annular cancellation moments failed")
    for y in (0, 1, 2, 3, 5):
        lhs = 3 - 7*y + 5*y*y - y*y*y
        rhs = (1-y)**2 * (3-y)
        if lhs != rhs:
            raise AssertionError("polynomial factorization failed")
    return {
        "coefficients": coeff,
        "sum_coefficients": moment_0,
        "sum_j_coefficients": moment_1,
        "sum_3powj_coefficients": critical_moment,
        "factorization": "3-7y+5y^2-y^3=(1-y)^2(3-y)",
    }


def sieve(n: int) -> Tuple[np.ndarray, np.ndarray]:
    is_prime = np.ones(n + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p*p:n+1:p] = False
    primes = np.flatnonzero(is_prime)
    log_rad = np.zeros(n + 1, dtype=np.float64)
    for p in primes:
        log_rad[p::p] += math.log(int(p))
    return primes, log_rad


def endpoint_sequence(n: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    primes, log_rad = sieve(n)
    radical_diff = np.empty(n + 1, dtype=np.float64)
    radical_diff[0] = log_rad[0]
    radical_diff[1:] = log_rad[1:] - log_rad[:-1]

    m = np.arange(n + 1, dtype=np.float64)
    sqrt_m = np.sqrt(m)
    log_m = np.zeros(n + 1, dtype=np.float64)
    log_m[1:] = np.log(m[1:])

    c1 = np.cumsum(2 * sqrt_m * radical_diff)
    c2 = np.cumsum(2 * sqrt_m * (log_m + 2) * radical_diff)
    c3 = np.cumsum(4 * m * radical_diff)

    prime_half = np.zeros(n + 1, dtype=np.float64)
    prime_half_log = np.zeros(n + 1, dtype=np.float64)
    logs = np.log(primes.astype(np.float64))
    weights = logs / np.sqrt(primes)
    prime_half[primes] = weights
    prime_half_log[primes] = weights * logs
    p1 = np.cumsum(prime_half)
    p2 = np.cumsum(prime_half_log)

    x = m[1:]
    log_x = np.log(x)
    j_prime = log_x * c1[1:] - c2[1:] + c3[1:] / np.sqrt(x)
    p_prime = log_x * p1[1:] - p2[1:]
    return j_prime - p_prime, primes, log_rad


def annular_value(a: np.ndarray, x: int) -> float:
    return float(
        3*a[x - 1]
        - 7*a[x // 9 - 1]
        + 5*a[x // 81 - 1]
        - a[x // 729 - 1]
    )


def b_value(x: int, n: int) -> float:
    if n > x:
        return 0.0
    return 2.0 * math.sqrt(n) * (
        math.log(x / n) - 2.0 * (1.0 - math.sqrt(n / x))
    )


def w_value(x: int, q: int) -> float:
    if q > x:
        return 0.0
    return math.log(x / q) / math.sqrt(q)


def direct_annular(x: int, primes: np.ndarray, log_rad: np.ndarray) -> float:
    scales = [x, x // 9, x // 81, x // 729]
    coeff = [3.0, -7.0, 5.0, -1.0]
    lower = x // 729

    seed = 0.0
    for n in range(lower + 1, x + 1):
        beta = math.fsum(coeff[j] * b_value(scales[j], n) for j in range(4))
        seed += beta * (log_rad[n] - log_rad[n - 1])

    ramp = 0.0
    for p0 in primes:
        p = int(p0)
        if p <= lower:
            continue
        omega = math.fsum(coeff[j] * w_value(scales[j], p) for j in range(4))
        ramp += math.log(p) * omega
    return seed - ramp


def finite_scan(max_x: int) -> dict:
    if max_x < ANNULUS:
        raise ValueError(f"--max-x must be at least {ANNULUS}")
    a, primes, log_rad = endpoint_sequence(max_x)
    xs = np.arange(ANNULUS, max_x + 1, ANNULUS, dtype=np.int64)
    vals = np.array([annular_value(a, int(x)) for x in xs])
    imax = int(np.argmax(vals))
    imin = int(np.argmin(vals))
    if not np.all(vals < 0):
        bad = int(xs[np.flatnonzero(vals >= 0)[0]])
        raise AssertionError(f"nonnegative annular value at X={bad}")

    selected = sorted(set(
        [int(xs[0]), int(xs[imax]), int(xs[-1])]
        + [x for x in (7290, 72900, 729000, 3_645_000) if x <= max_x]
    ))
    cross = []
    for x in selected:
        direct = direct_annular(x, primes, log_rad)
        prefix = annular_value(a, x)
        err = abs(direct - prefix)
        if err > 5e-8:
            raise AssertionError(f"direct annular reconstruction failed at {x}: {err}")
        cross.append({"X": x, "prefix": prefix, "direct": direct, "abs_error": err})

    return {
        "max_X": max_x,
        "annulus_factor": ANNULUS,
        "tested_multiples": int(len(xs)),
        "maximum": {"X": int(xs[imax]), "value": float(vals[imax])},
        "minimum": {"X": int(xs[imin]), "value": float(vals[imin])},
        "last": {"X": int(xs[-1]), "value": float(vals[-1])},
        "direct_reconstruction": cross,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("results") / "verification.json",
    )
    args = parser.parse_args()
    result = {
        "classification": "PASS_3751_ANNULAR_ENDPOINT_REGRESSION",
        "algebra": algebra(),
        "constants": constants(),
        "finite": finite_scan(args.max_x),
        "scope": (
            "The algebraic moment identities are exact. The constant computation "
            "and finite scan authenticate the written theorem and reconnaissance; "
            "the RH contour shift and Landau converse are not proved by the scan."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("PASS_3751_ANNULAR_ENDPOINT_REGRESSION")
    print(args.output)


if __name__ == "__main__":
    main()
