#!/usr/bin/env python3
"""Independent replay for L/T-90101.

Checks four things:
  1. direct vs Abel-positive formulas for every tested exit kernel c_p(k);
  2. the exact nonnegative-throughput Green/pixel cone decomposition over Q;
  3. the sparse producer consumer against the two T-90007 adversarial sources;
  4. discovery-only tail-budget comparisons (bottom exit vs sparse producer).

The algebraic flow checks use Fraction.  The logarithmic kernel checks use
mpmath at 70 decimal digits.  Tail-budget reconnaissance uses scipy/HiGHS.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import numpy as np
from mpmath import mp
from scipy.optimize import linprog

mp.dps = 70


def children(m: int) -> tuple[int, int, int, int]:
    return (m // 2, m - m // 2, (m + 2) // 3, m - (m + 2) // 3)


def q_weight(m: int, c: int) -> Fraction:
    mult = sum(1 for x in children(m) if x == c)
    return Fraction(c * mult, 2 * m)


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.zeros(n + 1, dtype=np.int64)
    mu[1] = 1
    primes: list[int] = []
    composite = np.zeros(n + 1, dtype=bool)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def w_mp(X: int, q: int) -> mp.mpf:
    if q > X:
        return mp.mpf("0")
    return mp.log(mp.mpf(X) / q) / mp.sqrt(q)


def pixel_G(X: int, n: int, p: int) -> list[Fraction]:
    """G_p(m)=m E_n(m,p)=p W_n(m,p), exactly."""
    G = [Fraction(0)] * (X + 2)
    G[p] = Fraction(p)
    for m in range(2 * n, X + 1):
        G[m] = sum((G[c] for c in children(m) if c >= n), Fraction(0)) / 2
    return G


def kernel_direct(X: int, n: int, p: int, k: int, G: list[Fraction]) -> mp.mpf:
    M = X // k
    total = mp.mpf("0")
    for m in range(n, M + 1):
        dG = G[m] - (G[m - 1] if m - 1 >= n else Fraction(0))
        total += mp.mpf(dG.numerator) / dG.denominator * w_mp(X, m * k)
    return total


def kernel_abel(X: int, n: int, k: int, G: list[Fraction]) -> tuple[mp.mpf, int]:
    M = X // k
    if M < n:
        return mp.mpf("0"), 0
    total = (mp.mpf(G[M].numerator) / G[M].denominator) * w_mp(X, M * k)
    positive_terms = int(total > 0)
    for m in range(n, M):
        gap = w_mp(X, m * k) - w_mp(X, (m + 1) * k)
        assert gap > 0
        term = (mp.mpf(G[m].numerator) / G[m].denominator) * gap
        assert term >= 0
        positive_terms += int(term > 0)
        total += term
    return total, positive_terms


def verify_positive_kernels() -> dict:
    cases = 0
    strictly_positive = 0
    max_error = mp.mpf("0")
    positive_terms = 0
    for X, n in ((72, 5), (96, 7), (132, 11)):
        for p in range(n, min(2 * n, X + 1)):
            G = pixel_G(X, n, p)
            assert all(x >= 0 for x in G)
            for k in range(1, X // n + 1):
                direct = kernel_direct(X, n, p, k, G)
                abel, term_count = kernel_abel(X, n, k, G)
                err = abs(direct - abel)
                max_error = max(max_error, err)
                assert err < mp.mpf("1e-60")
                assert abel >= -mp.mpf("1e-65")
                strictly_positive += int(abel > mp.mpf("1e-60"))
                positive_terms += term_count
                cases += 1
    return {
        "cases": cases,
        "strictly_positive_cases": strictly_positive,
        "positive_abel_terms": positive_terms,
        "max_direct_vs_abel_error": mp.nstr(max_error, 8),
    }



def verify_scale_dictionary() -> dict:
    """Check c_X(k)=k^-1/2 c_(X/k)(1) and its full multiples Möbius transform."""
    cases = 0
    max_kernel_error = mp.mpf("0")
    max_primitive_error = mp.mpf("0")
    for X, n, p0 in ((120, 5, 5), (180, 7, 9), (240, 11, 17)):
        GX = pixel_G(X, n, p0)
        for k in (2, 3, 4, 5):
            if X % k or X // k < p0:
                continue
            Y = X // k
            GY = pixel_G(Y, n, p0)
            left = kernel_direct(X, n, p0, k, GX)
            right = kernel_direct(Y, n, p0, 1, GY) / mp.sqrt(k)
            kernel_error = abs(left - right)
            max_kernel_error = max(max_kernel_error, kernel_error)
            assert kernel_error < mp.mpf("1e-60")

            mu = mobius_sieve(Y // n)
            primitive_left = mp.mpf("0")
            primitive_right = mp.mpf("0")
            for j in range(1, Y // n + 1):
                if mu[j] == 0:
                    continue
                primitive_left += int(mu[j]) * kernel_direct(X, n, p0, k * j, GX)
                primitive_right += int(mu[j]) * kernel_direct(Y, n, p0, j, GY) / mp.sqrt(k)
            primitive_error = abs(primitive_left - primitive_right)
            max_primitive_error = max(max_primitive_error, primitive_error)
            assert primitive_error < mp.mpf("1e-60")
            cases += 1
    return {
        "cases": cases,
        "max_kernel_scaling_error": mp.nstr(max_kernel_error, 8),
        "max_primitive_scaling_error": mp.nstr(max_primitive_error, 8),
    }


def canonical_far_flow(X: int, n: int, S: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """g on F and Sigma on W by exact descending propagation."""
    inflow = [Fraction(0)] * (X + 2)
    g = [Fraction(0)] * (X + 2)
    for m in range(X, 2 * n - 1, -1):
        g[m] = S[m] + inflow[m]
        for c in set(children(m)):
            if c >= n:
                inflow[c] += g[m] * q_weight(m, c)
    sigma = [Fraction(0)] * (X + 2)
    for p in range(n, min(2 * n, X + 1)):
        sigma[p] = S[p] + inflow[p]
    return g, sigma


def solve_h_from_boundary_charge(
    X: int,
    n: int,
    boundary: list[Fraction],
    charge: list[Fraction],
) -> list[Fraction]:
    h = [Fraction(0)] * (X + 2)
    for p in range(n, min(2 * n, X + 1)):
        h[p] = boundary[p]
    for m in range(2 * n, X + 1):
        h[m] = charge[m] + sum(
            (q_weight(m, c) * h[c] for c in set(children(m)) if c >= n),
            Fraction(0),
        )
    return h


def laplacian(X: int, n: int, h: list[Fraction], m: int) -> Fraction:
    return h[m] - sum(
        (q_weight(m, c) * h[c] for c in set(children(m)) if c >= n),
        Fraction(0),
    )


def verify_nonnegative_flow_cone() -> dict:
    exact_cases = 0
    threshold_cases = 0
    for X, n in ((24, 4), (31, 5), (40, 7)):
        # A deterministic signed source; no positivity is assumed.
        S = [Fraction(0)] * (X + 2)
        for m in range(n, X + 1):
            S[m] = Fraction(((17 * m + 3) % 11) - 5, m + 2)
        g, sigma = canonical_far_flow(X, n, S)

        boundary = [Fraction(0)] * (X + 2)
        charge = [Fraction(0)] * (X + 2)
        for p in range(n, min(2 * n, X + 1)):
            boundary[p] = Fraction((3 * p + 1) % 5, 7)
        for m in range(2 * n, X + 1):
            charge[m] = Fraction((5 * m + 2) % 7, 9)
        h = solve_h_from_boundary_charge(X, n, boundary, charge)
        assert all(h[m] >= 0 for m in range(n, X + 1))
        for m in range(2 * n, X + 1):
            assert laplacian(X, n, h, m) == charge[m]
        lhs = sum((S[m] * h[m] for m in range(n, X + 1)), Fraction(0))
        rhs = sum((boundary[p] * sigma[p] for p in range(n, min(2 * n, X + 1))), Fraction(0))
        rhs += sum((charge[m] * g[m] for m in range(2 * n, X + 1)), Fraction(0))
        assert lhs == rhs
        exact_cases += 1

        # Thresholds are superharmonic cuts for the y>=0 problem and decompose
        # into their window trace plus nonnegative internal charges.
        for k in range(n, min(X, 2 * n + 4) + 1):
            ht = [Fraction(0)] * (X + 2)
            for m in range(max(n, k), X + 1):
                ht[m] = Fraction(1)
            bt = [Fraction(0)] * (X + 2)
            at = [Fraction(0)] * (X + 2)
            for p in range(n, min(2 * n, X + 1)):
                bt[p] = ht[p]
            for m in range(2 * n, X + 1):
                at[m] = laplacian(X, n, ht, m)
                assert at[m] >= 0
            rebuilt = solve_h_from_boundary_charge(X, n, bt, at)
            assert rebuilt == ht
            tail = sum((S[m] for m in range(max(n, k), X + 1)), Fraction(0))
            cut = sum((bt[p] * sigma[p] for p in range(n, min(2 * n, X + 1))), Fraction(0))
            cut += sum((at[m] * g[m] for m in range(2 * n, X + 1)), Fraction(0))
            assert tail == cut
            threshold_cases += 1
    return {"exact_pairing_cases": exact_cases, "threshold_decompositions": threshold_cases}


def critical_r_eps(X: int, eps: np.ndarray) -> np.ndarray:
    q = np.arange(1, X + 1, dtype=np.float64)
    w = np.zeros(X + 2)
    w[2 : X + 1] = np.log(X / q[1:]) / np.sqrt(q[1:])
    U = np.zeros(X + 2)
    for k in range(1, X + 1):
        if eps[k] == 0:
            continue
        top = X // k
        m = np.arange(1, top + 1)
        U[1 : top + 1] += eps[k] * w[m * k]
    R = np.zeros(X + 2)
    R[1 : X + 1] = U[1 : X + 1] - U[2 : X + 2]
    return R


def sigma_float(R: np.ndarray, X: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    upper = min(2 * n, X + 1)
    ps = np.arange(n, upper)
    sigma = ps * R[n:upper]
    if 2 * n > X:
        return ps, sigma
    far = np.zeros(X + 1)
    far[2 * n :] = np.arange(2 * n, X + 1) * R[2 * n : X + 1]
    entrance = np.zeros(2 * n)
    hi = X
    while hi >= 2 * n:
        lo = max(2 * n, (2 * hi) // 3 + 1)
        M = np.arange(lo, hi + 1)
        scale = far[lo : hi + 1] / (2.0 * M)
        cs = (M // 2, M - M // 2, (M + 2) // 3, M - (M + 2) // 3)
        idx = np.concatenate(cs)
        weights = np.concatenate(tuple(c * scale for c in cs))
        buf = np.bincount(idx, weights=weights, minlength=hi + 1)
        if len(buf) > 2 * n:
            far[2 * n : len(buf)] += buf[2 * n :]
        entrance[n:] += buf[n : 2 * n]
        hi = lo - 1
    sigma += entrance[n:]
    return ps, sigma


def producer_A(R: np.ndarray, X: int) -> np.ndarray:
    A = np.zeros(X + 2)
    inflow = np.zeros(X + 2)
    for m in range(X, 1, -1):
        A[m] = R[m] + inflow[m]
        for c in children(m):
            if c >= 2:
                inflow[c] += A[m] / 2.0
    return A


def sparse_trace(n: int, X: int) -> dict[int, float]:
    out: dict[int, float] = {n: 1.0}
    for p in range(n + 1, min(2 * n, X + 1)):
        mult = sum(1 for c in children(p) if c == n)
        if mult:
            out[p] = n * mult / (2.0 * p)
    return out


def adversarial_vector(X: int, K0: int = 40) -> np.ndarray:
    mu = mobius_sieve(X)
    eps = np.zeros(X + 1)
    eps[1] = 1
    for k in range(2, X + 1):
        if mu[k] != 0:
            eps[k] = mu[k] if k <= K0 else -1
    return eps


def verify_sparse_adversaries() -> list[dict]:
    rows = []
    expected = {
        (2000, 20): (-0.4712115867, 0.0459306074),
        (3000, 25): (-0.8138646554, -0.5633436528),
    }
    for (X, n), (emin, eprod) in expected.items():
        R = critical_r_eps(X, adversarial_vector(X))
        ps, sigma = sigma_float(R, X, n)
        A = producer_A(R, X)
        trace = sparse_trace(n, X)
        sparse = sum(trace[p] * sigma[p - n] for p in trace)
        assert abs(sparse - n * A[n]) < 2e-11
        assert abs(float(sigma.min()) - emin) < 2e-8
        assert abs(float(n * A[n]) - eprod) < 2e-8
        rows.append(
            {
                "X": X,
                "n": n,
                "min_sigma": float(sigma.min()),
                "min_exit": int(ps[int(np.argmin(sigma))]),
                "nA_n": float(n * A[n]),
                "sparse_trace": {str(k): v for k, v in trace.items()},
            }
        )
    return rows


def G_float(X: int, n: int, p: int) -> np.ndarray:
    G = np.zeros(X + 2)
    G[p] = float(p)
    for m in range(2 * n, X + 1):
        G[m] = 0.5 * sum(G[c] for c in children(m) if c >= n)
    return G


def kernel_coefficients(X: int, n: int, trace: dict[int, float]) -> np.ndarray:
    Kmax = X // n
    q = np.arange(1, X + 1, dtype=np.float64)
    w = np.zeros(X + 1)
    w[1:] = np.log(X / q) / np.sqrt(q)
    G = np.zeros(X + 2)
    for p, a in trace.items():
        G += a * G_float(X, n, p)
    dG = G[n : X + 1] - G[n - 1 : X]
    c = np.zeros(Kmax + 1)
    for k in range(1, Kmax + 1):
        top = X // k
        if top < n:
            continue
        m = np.arange(n, top + 1)
        c[k] = np.dot(dG[: top - n + 1], w[m * k])
    return c


def tail_budget(X: int, n: int, kernel: np.ndarray, K0: int = 40) -> dict:
    mu = mobius_sieve(X)
    Kmax = X // n
    sf = [k for k in range(1, Kmax + 1) if mu[k] != 0]
    deep = [k for k in sf if k > K0]
    known = sum(mu[k] * kernel[k] for k in sf if k <= K0)
    free_min = known - sum(abs(kernel[k]) for k in deep)
    if free_min >= -1e-10:
        return {"status": "FREE", "free_min": float(free_min), "A_star": None}
    m_known = sum(mu[k] / k for k in sf if k <= K0)
    Ns = list(range(K0 + 1, Kmax + 1))
    rows = [np.array([1.0 / k if k <= N else 0.0 for k in deep]) for N in Ns]
    A_ub = np.vstack(rows + [-a for a in rows])
    dvec = np.array([kernel[k] for k in deep])

    def minimum(A: float) -> float | None:
        b = np.concatenate(
            (
                np.array([A / math.sqrt(N) - m_known for N in Ns]),
                np.array([A / math.sqrt(N) + m_known for N in Ns]),
            )
        )
        result = linprog(dvec, A_ub=A_ub, b_ub=b, bounds=[(-1, 1)] * len(deep), method="highs")
        if result.status == 2:  # infeasible: the tail budget is too small for the fixed prefix
            return None
        assert result.success, result.message
        return float(known + result.fun)

    # The admissible class can be empty for very small A because the prefix
    # k<=K0 is frozen.  Locate the first nonempty class, then exploit the
    # monotone enlargement of the feasible set as A grows.
    lo = 1e-8
    lo_value = minimum(lo)
    while lo_value is None:
        lo *= 2
        assert lo < 4096
        lo_value = minimum(lo)
    assert lo_value >= -1e-8

    hi = max(1.0, 2 * lo)
    hi_value = minimum(hi)
    while hi_value is None or hi_value >= 0:
        lo, lo_value = hi, hi_value
        hi *= 2
        assert hi < 4096
        hi_value = minimum(hi)
    for _ in range(24):
        mid = (lo + hi) / 2
        mid_value = minimum(mid)
        assert mid_value is not None
        if mid_value >= 0:
            lo = mid
        else:
            hi = mid
    return {"status": "FINITE", "free_min": float(free_min), "A_star": float(lo)}


def verify_tail_budgets() -> list[dict]:
    rows = []
    for X, n in ((2000, 20), (3000, 25), (3000, 15), (4000, 20), (4000, 15)):
        bottom = kernel_coefficients(X, n, {n: 1.0})
        sparse = kernel_coefficients(X, n, sparse_trace(n, X))
        assert np.min(bottom[1:]) >= -2e-10
        assert np.min(sparse[1:]) >= -2e-10
        b = tail_budget(X, n, bottom)
        s = tail_budget(X, n, sparse)
        rows.append({"X": X, "n": n, "depth": X // n, "bottom_pixel": b, "sparse_producer": s})
    return rows


def main() -> None:
    results = {
        "positive_kernels": verify_positive_kernels(),
        "scale_dictionary": verify_scale_dictionary(),
        "nonnegative_flow_cone": verify_nonnegative_flow_cone(),
        "adversarial_sparse_consumer": verify_sparse_adversaries(),
        "tail_budget_reconnaissance": verify_tail_budgets(),
    }
    script = Path(__file__).read_bytes()
    results["verifier_sha256"] = hashlib.sha256(script).hexdigest()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print("PASS_X_90101_NONNEGATIVE_FLOW_SPARSE_KERNEL")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
