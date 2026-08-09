#!/usr/bin/env python3
"""Regression for L-90004 / T-90006.

This is not the proof of the contour shift.  It authenticates:
  * the exact radical-switching implementation of J_P;
  * the prime-zeta Laurent coefficient at z=0;
  * the predicted shell drift in direct finite data.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import List, Tuple

import mpmath as mp

ZETA_HALF = mp.mpf("-1.4603545088095868128894991525152980124672293310126")
KAPPA = (1 + ZETA_HALF) * mp.log(2) / 2


def mobius_table(n: int) -> List[int]:
    mu = [0] * (n + 1)
    lp = [0] * (n + 1)
    primes: List[int] = []
    mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            mu[i * p] = 0 if p == lp[i] else -mu[i]
    return mu


_MU = mobius_table(80)


def minus_zeta_log_derivative(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return -mp.zeta(s, derivative=1) / mp.zeta(s)


def prime_log_series_cont(s: mp.mpf | mp.mpc, cutoff: int = 70):
    return mp.fsum(
        _MU[m] * minus_zeta_log_derivative(m * s)
        for m in range(1, cutoff + 1)
        if _MU[m]
    )


def shifted_difference_cont(w: mp.mpf | mp.mpc, order: int = 34):
    return mp.fsum(
        (-1) ** (r + 1)
        * mp.rf(w, r)
        / mp.factorial(r)
        * mp.zeta(w + r)
        * prime_log_series_cont(w + r)
        for r in range(1, order + 1)
    )


def endpoint_transform(z: mp.mpf):
    s = z + mp.mpf("0.5")
    g = shifted_difference_cont(s - 1) / s - prime_log_series_cont(s)
    return g / (z * z)


def laurent_check() -> dict:
    mp.mp.dps = 60
    rows = []
    target_a = (1 + ZETA_HALF) / 2
    target_shell = KAPPA
    for text in ("0.05", "0.02", "0.01", "0.005"):
        z = mp.mpf(text)
        ahat = endpoint_transform(z)
        shat = (1 - mp.power(2, -z)) * ahat
        rows.append(
            {
                "z": text,
                "z3_Ahat": mp.nstr(z**3 * ahat, 30),
                "z2_shell_hat": mp.nstr(z**2 * shat, 30),
            }
        )
    last_a = mp.mpf(rows[-1]["z3_Ahat"])
    last_s = mp.mpf(rows[-1]["z2_shell_hat"])
    if abs(last_a - target_a) > mp.mpf("5e-4"):
        raise AssertionError("endpoint Laurent coefficient did not converge")
    if abs(last_s - target_shell) > mp.mpf("5e-4"):
        raise AssertionError("shell Laurent coefficient did not converge")
    return {
        "target_z3_Ahat": mp.nstr(target_a, 40),
        "target_z2_shell_hat": mp.nstr(target_shell, 40),
        "rows": rows,
    }


def sieve(n: int) -> Tuple[List[int], List[float]]:
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    log_rad = [0.0] * (n + 1)
    for p in primes:
        lp = math.log(p)
        for m in range(p, n + 1, p):
            log_rad[m] += lp
    return primes, log_rad


def b_value(x: int, m: int) -> float:
    if m > x:
        return 0.0
    return 2.0 * math.sqrt(m) * (
        math.log(x / m) - 2.0 * (1.0 - math.sqrt(m / x))
    )


def endpoint_scalar(x: int, primes: List[int], log_rad: List[float]) -> float:
    # Exact finite radical switching, evaluated in binary64.
    seed = math.fsum(
        b_value(x, m) * (log_rad[m] - log_rad[m - 1])
        for m in range(2, x + 1)
    )
    ramp = math.fsum(
        math.log(p) / math.sqrt(p) * math.log(x / p)
        for p in primes
        if p <= x
    )
    return seed - ramp


def finite_check(max_x: int) -> dict:
    endpoints = [
        x
        for x in (100_000, 200_000, 500_000, 1_000_000, 2_000_000)
        if x <= max_x
    ]
    if max_x not in endpoints and max_x >= 10_000:
        endpoints.append(max_x)
    endpoints = sorted(set(endpoints))
    primes, log_rad = sieve(max_x)
    needed = sorted(set(endpoints + [x // 2 for x in endpoints]))
    values = {x: endpoint_scalar(x, primes, log_rad) for x in needed}
    rows = []
    kappa_float = float(KAPPA)
    for x in endpoints:
        shell = values[x] - values[x // 2]
        ratio = shell / math.log(x)
        rows.append(
            {
                "X": x,
                "A_X": values[x],
                "shell": shell,
                "shell_over_logX": ratio,
                "centered_remainder": shell - kappa_float * math.log(x),
            }
        )
        if shell >= 0:
            raise AssertionError(f"unexpected nonnegative shell at X={x}")
    # This is a regression corridor, not a theorem or extrapolation.
    if abs(rows[-1]["shell_over_logX"] - kappa_float) > 0.035:
        raise AssertionError("finite shell ratio left the declared regression corridor")
    return {
        "kappa": mp.nstr(KAPPA, 40),
        "max_X": max_x,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("results") / "verification.json",
    )
    args = parser.parse_args()
    if args.max_x < 10_000:
        raise SystemExit("--max-x must be at least 10000")
    result = {
        "classification": "PASS_ENDPOINT_NEGATIVE_DRIFT_REGRESSION",
        "laurent": laurent_check(),
        "finite": finite_check(args.max_x),
        "scope": (
            "Authenticates transform coefficients and finite regression only; "
            "the RH contour shift and eventual sign are proved in T-90006."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("PASS_ENDPOINT_NEGATIVE_DRIFT_REGRESSION")
    print(args.output)


if __name__ == "__main__":
    main()
