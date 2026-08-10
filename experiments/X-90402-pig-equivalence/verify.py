#!/usr/bin/env python3
"""Exact finite regression for T-90404.

All coefficient arithmetic is exact. Logarithms are represented in the free
Q-vector space with basis symbols log(p), one for each prime p in range.
The script checks source/current/carry identities only; it does not address RH.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import Dict, Iterable, List

N_ROWS = 96
MAX_N = 4 * N_ROWS

LogVec = Dict[int, Fraction]


def factor(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def divisors(n: int) -> Iterable[int]:
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            yield d
            if d * d != n:
                yield n // d


def vclean(v: LogVec) -> LogVec:
    return {p: c for p, c in v.items() if c}


def vadd(*vs: LogVec) -> LogVec:
    out: LogVec = {}
    for v in vs:
        for p, c in v.items():
            out[p] = out.get(p, Fraction(0)) + c
    return vclean(out)


def vscale(c: Fraction | int, v: LogVec) -> LogVec:
    cc = Fraction(c)
    return vclean({p: cc * x for p, x in v.items()})


def log_vec(n: int) -> LogVec:
    return {p: Fraction(e) for p, e in factor(n).items()}


def lambda_vec(n: int) -> LogVec:
    fs = factor(n)
    if len(fs) != 1:
        return {}
    p = next(iter(fs))
    return {p: Fraction(1)}


def scalar_convolution(a: List[Fraction], b: List[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        out[n] = sum(a[d] * b[n // d] for d in divisors(n))
    return out


def one_convolve_scalar(a: List[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        out[n] = sum(a[d] for d in divisors(n))
    return out


def one_convolve_vector(a: List[LogVec]) -> List[LogVec]:
    out: List[LogVec] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        out[n] = vadd(*(a[d] for d in divisors(n)))
    return out


def prefix_scalar(a: List[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        out[n] = out[n - 1] + a[n]
    return out


def prefix_vector(a: List[LogVec]) -> List[LogVec]:
    out: List[LogVec] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        out[n] = vadd(out[n - 1], a[n])
    return out


def carry_scalar(pref: List[Fraction], n: int, j: int) -> Fraction:
    return pref[n] - pref[j] - pref[n - j]


def carry_vector(pref: List[LogVec], n: int, j: int) -> LogVec:
    return vadd(pref[n], vscale(-1, pref[j]), vscale(-1, pref[n - j]))


def main() -> None:
    eps = [Fraction(0) for _ in range(MAX_N + 1)]
    eps[1] = Fraction(1)

    delta4 = [Fraction(0) for _ in range(MAX_N + 1)]
    delta4[4] = Fraction(1)

    mu = [Fraction(0) for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        mu[n] = Fraction(mobius(n))

    geom4 = [Fraction(0) for _ in range(MAX_N + 1)]
    x = 1
    while x <= MAX_N:
        geom4[x] = Fraction(1)
        x *= 4

    numerator = eps.copy()
    numerator[4] -= 4

    # B4=(epsilon-4 delta4)*(sum_r delta_(4^r))*mu.
    b4 = scalar_convolution(scalar_convolution(numerator, geom4), mu)
    e4 = one_convolve_scalar(b4)

    expected_e4 = [Fraction(0) for _ in range(MAX_N + 1)]
    expected_e4[1] = Fraction(1)
    x = 4
    while x <= MAX_N:
        expected_e4[x] = Fraction(-3)
        x *= 4
    e4_failures = [n for n in range(1, MAX_N + 1) if e4[n] != expected_e4[n]]

    # b_circ=(epsilon-delta4)*b4.
    circ_filter = eps.copy()
    circ_filter[4] -= 1
    bcirc = scalar_convolution(circ_filter, b4)

    qcirc: List[LogVec] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        qcirc[n] = vscale(-bcirc[n], log_vec(n))
    one_q = one_convolve_vector(qcirc)

    current_failures = []
    for n in range(1, MAX_N + 1):
        rhs = lambda_vec(n)
        if n % 4 == 0:
            rhs = vadd(rhs, vscale(-4, lambda_vec(n // 4)))
        if n == 4:
            # 4 log(4)=8 log(2).
            rhs = vadd(rhs, {2: Fraction(8)})
        if one_q[n] != rhs:
            current_failures.append(n)

    pref_one_q = prefix_vector(one_q)
    psi: List[LogVec] = [{} for _ in range(MAX_N + 1)]
    for x in range(1, MAX_N + 1):
        psi[x] = vadd(psi[x - 1], lambda_vec(x))

    prefix_failures = []
    for x in range(1, MAX_N + 1):
        rhs = vadd(psi[x], vscale(-4, psi[x // 4]))
        if x >= 4:
            rhs = vadd(rhs, {2: Fraction(8)})
        if pref_one_q[x] != rhs:
            prefix_failures.append(x)

    aligned_failures = []
    for n in range(2, N_ROWS + 1):
        for j in range(1, n):
            k = n - j
            lhs = carry_vector(pref_one_q, 4 * n, 4 * j)
            rhs = vadd(
                psi[4 * n],
                vscale(-1, psi[4 * j]),
                vscale(-1, psi[4 * k]),
                vscale(-4, psi[n]),
                vscale(4, psi[j]),
                vscale(4, psi[k]),
                {2: Fraction(-8)},
            )
            if lhs != rhs:
                aligned_failures.append([n, j])

    # delta4*b4 and its exact carry scaling.
    shifted_b4 = scalar_convolution(delta4, b4)
    pref_b4 = prefix_scalar(one_convolve_scalar(b4))
    pref_shift = prefix_scalar(one_convolve_scalar(shifted_b4))
    gauge_failures = []
    for n in range(2, N_ROWS + 1):
        for j in range(1, n):
            lhs = carry_scalar(pref_shift, 4 * n, 4 * j)
            rhs = carry_scalar(pref_b4, n, j)
            if lhs != rhs:
                gauge_failures.append([n, j])

    checks = {
        "one_convolve_b4": {
            "tested_coefficients": MAX_N,
            "failures": e4_failures,
            "pass": not e4_failures,
        },
        "compact_current_coefficient_identity": {
            "tested_coefficients": MAX_N,
            "failures": current_failures,
            "pass": not current_failures,
        },
        "compact_current_prefix_identity": {
            "tested_prefixes": MAX_N,
            "failures": prefix_failures,
            "pass": not prefix_failures,
        },
        "aligned_filtered_chebyshev_carry": {
            "tested_rows": sum(n - 1 for n in range(2, N_ROWS + 1)),
            "failures": aligned_failures,
            "pass": not aligned_failures,
        },
        "delayed_bare_gauge_scaling": {
            "tested_rows": sum(n - 1 for n in range(2, N_ROWS + 1)),
            "failures": gauge_failures,
            "pass": not gauge_failures,
        },
    }

    verdict = (
        "PASS_X_90402_PIG_EQUIVALENCE_ALGEBRA"
        if all(item["pass"] for item in checks.values())
        else "FAIL_X_90402_PIG_EQUIVALENCE_ALGEBRA"
    )
    result = {
        "classification": "FINITE_EXACT_COEFFICIENT_REGRESSION_NOT_RH_PROOF",
        "max_coefficient": MAX_N,
        "max_parent_row": N_ROWS,
        "checks": checks,
        "verdict": verdict,
        "proof_boundary": (
            "Checks exact finite source/current/carry identities only. It does not prove "
            "the von Koch estimate, T-90302, PIG, or RH."
        ),
    }

    path = Path(__file__).resolve().parent / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(verdict)
    print(path)


if __name__ == "__main__":
    main()
