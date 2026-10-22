#!/usr/bin/env python3
"""Exact lightweight replay for L-93018, L-93019, and R-93020.

Arithmetic:
- fractions.Fraction for every Hardy-transform identity;
- integer/formal-prime-log arithmetic for the Q4 logarithmic-derivative
  convolution;
- no zero table, prime scan, or asymptotic computation.

The replay does not prove the Q4 mean bound, endpoint PIG, or RH.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Dict, List


FormalLog = Dict[int, Fraction]


def add_log(a: FormalLog, b: FormalLog, scale: Fraction = Fraction(1)) -> FormalLog:
    out: Dict[int, Fraction] = defaultdict(Fraction)
    for p, value in a.items():
        out[p] += value
    for p, value in b.items():
        out[p] += scale * value
    return {p: value for p, value in out.items() if value}


def scale_log(a: FormalLog, scale: Fraction) -> FormalLog:
    return {p: scale * value for p, value in a.items() if scale * value}


def spf_sieve(n: int) -> List[int]:
    spf = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(n: int, spf: List[int]) -> Dict[int, int]:
    out: Dict[int, int] = defaultdict(int)
    while n > 1:
        p = spf[n]
        out[p] += 1
        n //= p
    return dict(out)


def mobius(n: int, spf: List[int]) -> int:
    factors = factor(n, spf)
    if any(e > 1 for e in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def log_formal(n: int, spf: List[int]) -> FormalLog:
    return {p: Fraction(e) for p, e in factor(n, spf).items()}


def lambda_formal(n: int, spf: List[int]) -> FormalLog:
    factors = factor(n, spf)
    if len(factors) != 1:
        return {}
    p = next(iter(factors))
    return {p: Fraction(1)}


def is_power_of_four(n: int) -> bool:
    if n < 4:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1


def q4_source(n: int, spf: List[int]) -> FormalLog:
    out = lambda_formal(n, spf)
    if n % 4 == 0:
        out = add_log(out, lambda_formal(n // 4, spf), Fraction(-4))
    if is_power_of_four(n):
        # 3 log 4 = 6 log 2.
        out = add_log(out, {2: Fraction(6)})
    return out


def a4(n: int, spf: List[int]) -> int:
    value = mobius(n, spf)
    power = 4
    while power <= n:
        if n % power == 0:
            value -= 3 * mobius(n // power, spf)
        power *= 4
    return value


def divisors(n: int) -> List[int]:
    out: List[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out


def prefix_and_mean(c: List[Fraction]) -> tuple[List[Fraction], List[Fraction], List[Fraction]]:
    kmax = len(c) - 1
    prefix = [Fraction(0) for _ in range(kmax + 1)]
    mean = [Fraction(0) for _ in range(kmax + 1)]
    partial_prefix = [Fraction(0) for _ in range(kmax + 1)]
    first_moment = Fraction(0)
    running_prefix_sum = Fraction(0)
    for n in range(1, kmax + 1):
        prefix[n] = prefix[n - 1] + c[n]
        first_moment += n * c[n]
        mean[n] = Fraction(2, n) * first_moment - prefix[n]
        running_prefix_sum += prefix[n]
        partial_prefix[n] = running_prefix_sum
    return prefix, mean, partial_prefix


def run() -> dict:
    rng = random.Random(93018)

    hardy_prefix_checks = 0
    finite_backward_checks = 0
    zero_boundary_checks = 0
    boundary_firewall_checks = 0
    a4_coefficient_checks = 0
    convolution_checks = 0
    hostile_mutations = 0

    # Universal finite Hardy and backward identities.
    for kmax in range(5, 31):
        for _ in range(11):
            c = [Fraction(0)]
            for _n in range(1, kmax + 1):
                c.append(Fraction(rng.randint(-9, 9), rng.randint(1, 13)))
            prefix, mean, partial = prefix_and_mean(c)

            for n in range(1, kmax + 1):
                hardy = prefix[n] - Fraction(2, n) * sum(
                    prefix[:n], Fraction(0)
                )
                assert mean[n] == hardy
                hardy_prefix_checks += 1

                rhs = (
                    mean[n]
                    - 2
                    * (n + 1)
                    * sum(
                        (
                            mean[k] / ((k + 1) * (k + 2))
                            for k in range(n, kmax + 1)
                        ),
                        Fraction(0),
                    )
                    + 2
                    * (n + 1)
                    * partial[kmax]
                    / ((kmax + 1) * (kmax + 2))
                )
                assert rhs == prefix[n]
                finite_backward_checks += 1

                # Dropping the finite boundary is generically detected.
                no_boundary = (
                    mean[n]
                    - 2
                    * (n + 1)
                    * sum(
                        (
                            mean[k] / ((k + 1) * (k + 2))
                            for k in range(n, kmax + 1)
                        ),
                        Fraction(0),
                    )
                )
                if partial[kmax] != 0 and no_boundary != prefix[n]:
                    hostile_mutations += 1

    # Finite-support fixtures with zero total and zero first moment.
    # Then C and M vanish after kmax, so the infinite inversion truncates.
    for kmax in range(6, 36):
        for _ in range(9):
            c = [Fraction(0)]
            for _n in range(1, kmax - 1):
                c.append(Fraction(rng.randint(-8, 8), rng.randint(1, 11)))
            total = sum(c[1:], Fraction(0))
            weighted = sum(
                (n * c[n] for n in range(1, kmax - 1)),
                Fraction(0),
            )
            x = weighted - kmax * total
            y = (kmax - 1) * total - weighted
            c.append(x)
            c.append(y)
            assert sum(c[1:], Fraction(0)) == 0
            assert sum(
                (n * c[n] for n in range(1, kmax + 1)),
                Fraction(0),
            ) == 0
            prefix, mean, _partial = prefix_and_mean(c)
            assert prefix[kmax] == 0
            assert mean[kmax] == 0

            for n in range(1, kmax + 1):
                rhs = mean[n] - 2 * (n + 1) * sum(
                    (
                        mean[k] / ((k + 1) * (k + 2))
                        for k in range(n, kmax + 1)
                    ),
                    Fraction(0),
                )
                assert rhs == prefix[n]
                zero_boundary_checks += 1

    # Exact linear-mode firewall c(n)=1.
    for n in range(1, 128):
        telescoping_tail = Fraction(1, n + 1)
        wrong = Fraction(1) - 2 * (n + 1) * telescoping_tail
        true_prefix = Fraction(n)
        assert wrong == -1
        assert wrong != true_prefix
        boundary = Fraction(n + 1)
        assert wrong + boundary == true_prefix
        boundary_firewall_checks += 1
        hostile_mutations += 1

    # Formal prime-log replay of the logarithmic-derivative convolution.
    limit = 512
    spf = spf_sieve(limit)
    for n in range(1, limit + 1):
        factors = factor(n, spf)
        e = factors.get(2, 0)
        m = n // (2**e)
        mu_m = mobius(m, spf)
        if e == 0:
            predicted = mu_m
        elif e == 1:
            predicted = -mu_m
        else:
            predicted = 3 * ((-1) ** (e + 1)) * mu_m
        assert a4(n, spf) == predicted
        a4_coefficient_checks += 1

        lhs: FormalLog = {}
        for d in divisors(n):
            lhs = add_log(
                lhs,
                q4_source(d, spf),
                Fraction(a4(n // d, spf)),
            )

        rhs = scale_log(log_formal(n, spf), Fraction(-a4(n, spf)))
        if n % 4 == 0:
            rhs = add_log(
                rhs,
                log_formal(n // 4, spf),
                Fraction(4 * a4(n // 4, spf)),
            )
        assert lhs == rhs
        convolution_checks += 1

        # Hostile mutations: remove the gauge or flip the scale-four sign.
        no_gauge = lambda_formal(n, spf)
        if n % 4 == 0:
            no_gauge = add_log(
                no_gauge,
                lambda_formal(n // 4, spf),
                Fraction(-4),
            )
        if is_power_of_four(n) and no_gauge != q4_source(n, spf):
            hostile_mutations += 1

        wrong_rhs = scale_log(log_formal(n, spf), Fraction(a4(n, spf)))
        if lhs != wrong_rhs:
            hostile_mutations += 1

    return {
        "classification": "PASS_X_93018_Q4_HARDY_LOGDERIVATIVE",
        "arithmetic_class": "EXACT_RATIONAL_AND_FORMAL_PRIME_LOGS",
        "hardy_prefix_checks": hardy_prefix_checks,
        "finite_backward_inversion_checks": finite_backward_checks,
        "zero_boundary_inversion_checks": zero_boundary_checks,
        "linear_boundary_firewall_checks": boundary_firewall_checks,
        "scale_four_mobius_coefficient_checks": a4_coefficient_checks,
        "formal_log_derivative_convolution_checks": convolution_checks,
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "finite prefix/mean Hardy identity",
            "finite backward inversion with boundary",
            "boundary-free inversion on exact zero-boundary fixtures",
            "linear-mode boundary firewall",
            "explicit scale-four Mobius coefficients",
            "coefficientwise Q4 logarithmic-derivative convolution",
        ],
        "does_not_prove": [
            "the square-root Q4 mean bound",
            "the endpoint PIG bound",
            "the Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    record = run()
    payload = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
