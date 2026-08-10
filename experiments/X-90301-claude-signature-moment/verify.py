#!/usr/bin/env python3
"""Diagnostic replay for the Claude zeta-23 import and extensions.

This script checks only finite algebra/numerics:
  * the optimized two-trace constant c_*(lambda) and its thresholds;
  * the short-window/hybrid-conductor constant table;
  * the elementary omitted-Euler-factor inequality used uniformly in q;
  * a Nyström reconnaissance for the xi' scalar-window optimum.

It is not a proof of the analytic asymptotics in T-90301.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable


def c_star(lam: float) -> float:
    if not (0.0 < lam <= 1.0):
        raise ValueError("lambda must lie in (0,1]")
    a = lam / math.sqrt(2.0)
    t = math.tan(a)
    return math.sqrt(2.0) * t / (1.0 + a * t)


def lower_bounds(lam: float) -> dict[str, float]:
    c = c_star(lam)
    on_line = max(0.0, 2.0 - 1.0 / c)
    distinct_rank_trace = (3.0 - 1.0 / c) / 2.0
    distinct = max(c, distinct_rank_trace)
    return {
        "lambda": lam,
        "c_star": c,
        "on_line_and_simple": on_line,
        "distinct": distinct,
        "distinct_rank_trace": distinct_rank_trace,
    }


def bisect_root(f, lo: float, hi: float, iterations: int = 120) -> float:
    flo = f(lo)
    fhi = f(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("root is not bracketed")
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def smallest_prime_factors(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, int(math.isqrt(n)) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def distinct_prime_factors(n: int, spf: list[int]) -> Iterable[int]:
    while n > 1:
        p = spf[n]
        yield p
        while n % p == 0:
            n //= p


def check_euler_factor_bound(limit: int = 100_000) -> dict[str, float | int]:
    spf = smallest_prime_factors(limit)
    max_ratio = 0.0
    max_q = 2
    min_slack = float("inf")
    for q in range(2, limit + 1):
        lhs = sum((math.log(p) ** 2) / (p - 1.0) for p in distinct_prime_factors(q, spf))
        rhs = math.log(q)
        slack = rhs - lhs
        if slack < -2e-14:
            raise AssertionError((q, lhs, rhs, slack))
        ratio = lhs / rhs
        if ratio > max_ratio:
            max_ratio = ratio
            max_q = q
        min_slack = min(min_slack, slack)
    return {
        "limit": limit,
        "max_lhs_over_log_q": max_ratio,
        "argmax_q": max_q,
        "minimum_slack": min_slack,
    }


def gauss_legendre(n: int) -> tuple[list[float], list[float]]:
    """Nodes and weights on [-1/2,1/2], pure Python Newton iteration."""
    nodes = [0.0] * n
    weights = [0.0] * n
    m = (n + 1) // 2
    for i in range(m):
        z = math.cos(math.pi * (i + 0.75) / (n + 0.5))
        for _ in range(100):
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z_next = z - p1 / pp
            if abs(z_next - z) < 2e-16:
                z = z_next
                break
            z = z_next
        # map [-1,1] to [-1/2,1/2]
        x = 0.5 * z
        w = 1.0 / ((1.0 - z * z) * pp * pp)
        nodes[i] = -x
        nodes[n - 1 - i] = x
        weights[i] = w
        weights[n - 1 - i] = w
    return nodes, weights


def d1(s: float) -> float:
    """D_1(s)=s-4s^2+sum_{k>=0} a_k s^(2k+3), 0<=s<=1."""
    if not (0.0 <= s <= 1.0 + 1e-15):
        raise ValueError("D1 replay is scoped to [0,1]")
    total = s - 4.0 * s * s
    coeff = 4.0  # a_0
    power = s * s * s
    k = 0
    while True:
        term = coeff * power
        total += term
        if abs(term) < 2e-19 or k >= 100:
            break
        coeff *= 2.0 * (k + 1.0) / ((k + 2.0) * (2.0 * k + 3.0))
        power *= s * s
        k += 1
    return total


def cholesky_solve(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(a)
    l = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j]
            for k in range(j):
                s -= l[i][k] * l[j][k]
            if i == j:
                if s <= 0.0:
                    raise ArithmeticError(f"matrix is not positive definite at {i}: {s}")
                l[i][j] = math.sqrt(s)
            else:
                l[i][j] = s / l[j][j]
    y = [0.0] * n
    for i in range(n):
        s = b[i]
        for k in range(i):
            s -= l[i][k] * y[k]
        y[i] = s / l[i][i]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = y[i]
        for k in range(i + 1, n):
            s -= l[k][i] * x[k]
        x[i] = s / l[i][i]
    return x


def xi_prime_nystrom(n: int) -> dict[str, float | int]:
    nodes, weights = gauss_legendre(n)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        wi = weights[i]
        for j in range(n):
            matrix[i][j] = wi * weights[j] * d1(abs(nodes[i] - nodes[j]))
        matrix[i][i] += wi
    solution = cholesky_solve(matrix, weights)
    c = sum(w * x for w, x in zip(weights, solution))
    return {
        "n": n,
        "c": c,
        "simple_on_line": 2.0 - 1.0 / c,
        "distinct": (3.0 - 1.0 / c) / 2.0,
        "minimum_profile_value": min(solution),
        "maximum_profile_value": max(solution),
    }


def main() -> None:
    table_pairs = [
        (1.00, 0.00),
        (0.90, 0.00),
        (0.75, 0.00),
        (0.60, 0.00),
        (1.00, 0.10),
        (1.00, 0.25),
        (1.00, 0.50),
        (1.00, 0.75),
        (0.75, 0.25),
    ]
    table = []
    for alpha, theta in table_pairs:
        lam = alpha / (1.0 + theta)
        row = {"alpha": alpha, "theta": theta}
        row.update(lower_bounds(lam))
        table.append(row)

    # c_* is increasing: c_*'(lambda)=1/(1+a tan a)^2 > 0.
    grid = [i / 1000.0 for i in range(1, 1001)]
    cvals = [c_star(x) for x in grid]
    if any(y <= x for x, y in zip(cvals, cvals[1:])):
        raise AssertionError("c_star failed monotonicity sample")

    lam_crit = bisect_root(lambda x: c_star(x) - 0.5, 0.5, 0.6)
    theta_crit = 1.0 / lam_crit - 1.0
    if abs(c_star(1.0) - 0.7532960678560707) > 2e-15:
        raise AssertionError("Montgomery-Taylor constant drift")

    euler = check_euler_factor_bound()

    # Endpoint budget: q<=T^theta and H>=T^alpha imply
    # log H/log(qT) >= alpha/(1+theta), up to harmless conductor constants.
    budget_checks = []
    for alpha, theta in [(0.6, 0.0), (0.75, 0.25), (1.0, 0.75)]:
        for log_t in (20.0, 50.0, 100.0):
            log_h = alpha * log_t
            log_qt = (1.0 + theta) * log_t
            actual = log_h / log_qt
            worst = alpha / (1.0 + theta)
            if abs(actual - worst) > 2e-15:
                raise AssertionError("budget identity failed")
            budget_checks.append({
                "alpha": alpha,
                "theta": theta,
                "log_T": log_t,
                "lambda": actual,
            })

    xi_rows = [xi_prime_nystrom(n) for n in (40, 80, 160, 320, 640)]
    if any(row["minimum_profile_value"] <= 0.0 for row in xi_rows):
        raise AssertionError("unconstrained xi-prime optimizer sampled negative")
    if not (0.868640 < xi_rows[-1]["simple_on_line"] < 0.868646):
        raise AssertionError("xi-prime reconnaissance outside expected interval")

    result = {
        "status": "PASS_X_90301_CLAUDE_SIGNATURE_MOMENT",
        "montgomery_taylor": lower_bounds(1.0),
        "critical_lambda_for_positive_on_line_bound": lam_crit,
        "critical_theta_at_alpha_one": theta_crit,
        "short_window_hybrid_table": table,
        "euler_factor_bound": euler,
        "budget_checks": budget_checks,
        "xi_prime_nystrom": xi_rows,
        "scope": "finite diagnostic checks only; no analytic asymptotic and no RH claim",
    }

    out_path = Path(__file__).resolve().parent / "results" / "verification.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"])


if __name__ == "__main__":
    main()
