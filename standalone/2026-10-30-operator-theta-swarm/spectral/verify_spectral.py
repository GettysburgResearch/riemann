#!/usr/bin/env python3
"""Finite exact checks and floating-point diagnostics for the spectral packet.

This does not prove an infinite theorem, certify a zero census, or use directed
rounding. Exact checks use Fraction; numerical checks use NumPy/SciPy binary64.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial, log, pi
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.special import digamma


COUNTS: dict[str, int] = {}


def check(category: str, condition: bool) -> None:
    if not condition:
        raise RuntimeError(f"Failed predicate: {category}")
    COUNTS[category] = COUNTS.get(category, 0) + 1


def laguerre_minus_one(n: int, x: Q) -> Q:
    if n == 0:
        return Q(1)
    return sum((Q(comb(n-1, k-1), factorial(k)) * (-x)**k
                for k in range(1, n+1)), Q(0))


def laguerre_zero(n: int, x: Q) -> Q:
    return sum((Q(comb(n, k), factorial(k)) * (-x)**k
                for k in range(n+1)), Q(0))


def exact_checks() -> None:
    for x in (Q(1, 7), Q(1), Q(7, 2), Q(20)):
        coeff = [Q(1)]
        for n in range(1, 21):
            coeff.append(-x * sum((k * coeff[n-k] for k in range(1, n+1)), Q(0)) / n)
            check("laguerre_generating_coefficients", coeff[-1] == laguerre_minus_one(n, x))
            check("laguerre_observation_coefficients",
                  sum(coeff, Q(0)) == laguerre_zero(n, x))

    for a in (Q(1), Q(3, 2), Q(100)):
        for b in (Q(1, 2), Q(1), Q(7, 3)):
            r = (a-b)/(a+b)
            pref = 4*a*b/(a+b)**2
            for n in (0, 1, 2, 8, 30):
                check("projection_error_exact",
                      pref * sum((r**(2*j) for j in range(n+1)), Q(0))
                      + r**(2*(n+1)) == 1)

    remainder_bound = Q(3, 100)+Q(1, 49)+Q(1, 15000)+Q(1, 1000)
    check("rational_margin", remainder_bound < Q(1, 19))
    check("rational_margin", Q(1, 2)-Q(6, 19) > Q(1, 6))
    check("rational_margin", Q(847, 64) < Q(175, 11))
    check("rational_margin", Q(1, 2**49)+Q(1, 48*2**48) < Q(1, 1000))

    # Exact dissipative identity for B=a(I+S)(I-S)^(-1).
    for n in (1, 2, 6, 10):
        for a in (Q(1), Q(5, 2), Q(100)):
            B = [[(a if i == j else 2*a if i < j else Q(0))
                  for j in range(n+1)] for i in range(n+1)]
            check("rank_one_dissipation_exact",
                  all((B[i][j]+B[j][i])/2 == a
                      for i in range(n+1) for j in range(n+1)))


def mangoldt_up_to(limit: int = 64) -> tuple[np.ndarray, np.ndarray]:
    primes = []
    for p in range(2, limit+1):
        if all(p % q for q in range(2, int(p**.5)+1)):
            primes.append(p)
    values = {}
    for p in primes:
        power = p
        while power <= limit:
            values[power] = log(p)
            power *= p
    ns = np.array(sorted(values), dtype=float)
    return np.log(ns), np.array([values[int(n)] for n in ns])


LOGS, LAMBDAS = mangoldt_up_to()


def f_safe(s: np.ndarray) -> np.ndarray:
    """Actual xi log derivative with only the prime-power tail truncated at 64.

    Used only at Re(s)>50; the analytic tail bound is recorded separately.
    """
    prime = np.exp(-s[:, None]*LOGS[None, :]) @ LAMBDAS
    return 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 - prime


def xi_covariance_cauchy(n: int, a: float, samples: int) -> np.ndarray:
    r = n/(n+1)
    theta = 2*pi*np.arange(samples)/samples
    z = r*np.exp(1j*theta)
    s = .5+a*(1+z)/(1-z)
    if np.min(np.real(s)) <= 50:
        raise ValueError("This diagnostic deliberately stays in Re(s)>50")
    F = 2*a*f_safe(s)
    coeff = np.fft.fft(F)/samples
    coeff = coeff[:n+1]/(r**np.arange(n+1))
    check("cauchy_reality", np.max(np.abs(coeff.imag)) < 1e-9*max(1, a))
    c = coeff.real
    c[1:] /= 2
    return c


def toeplitz(c: np.ndarray) -> np.ndarray:
    idx = np.arange(len(c))
    return c[np.abs(idx[:, None]-idx[None, :])]


def numerical_checks() -> dict:
    margins = []
    for n in (2, 8, 32, 64):
        a = float(100*(n+1))
        c = xi_covariance_cauchy(n, a, 8192)
        c2 = xi_covariance_cauchy(n, a, 16384)
        discrepancy = float(np.max(np.abs(c-c2))/a)
        check("cauchy_resolution_agreement", discrepancy < 2e-12)
        low = float(np.linalg.eigvalsh(toeplitz(c2))[0])
        check("actual_xi_large_anchor_margin", low > a/6)
        margins.append({"N": n, "a": a,
                        "min_eigenvalue_over_a": low/a,
                        "coefficient_discrepancy_over_a": discrepancy})

    semigroup = []
    for n, a, t in ((3, 1., .2), (8, 2.5, .7), (16, 10., .1)):
        S = np.diag(np.ones(n), 1)
        B = a*(np.eye(n+1)+S) @ np.linalg.inv(np.eye(n+1)-S)
        U = expm(-t*B)
        coefficients = np.array([float(laguerre_minus_one(k, Q(str(2*a*t))))
                                 for k in range(n+1)]) * np.exp(-a*t)
        constructed = np.zeros_like(B)
        for k, ck in enumerate(coefficients):
            constructed += ck*np.linalg.matrix_power(S, k)
        error = float(np.max(np.abs(U-constructed)))
        check("semigroup_laguerre_agreement", error < 2e-12)
        top = float(np.linalg.svd(U, compute_uv=False)[0])
        check("semigroup_contractivity", top <= 1+1e-12)
        semigroup.append({"N": n, "a": a, "t": t,
                          "maximum_entry_error": error,
                          "operator_norm": top})

    # Exact finite zero models are controls, not actual zeta data.
    controls = []
    for delta in (0., .2):
        zeros = [.5+delta+5j, .5+delta-5j,
                 .5-delta+5j, .5-delta-5j]
        n, a = 6, 2.
        c = np.zeros(n+1, complex)
        for rho in zeros:
            d = .5+a-rho
            ratio = -(a-.5+rho)/d
            c[0] += 2*a/d
            for k in range(1, n+1):
                c[k] += a*(ratio**k-ratio**(k-1))/d
        ev = np.linalg.eigvalsh(toeplitz(c.real))
        low = float(ev[0])
        if delta == 0:
            check("critical_line_model_control", low > -1e-12)
        else:
            check("off_line_model_control", low < -1e-5)
        controls.append({"model": "finite_symmetric_quartet", "delta": delta,
                         "N": n, "a": a, "minimum_eigenvalue": low})

    projection = []
    for n, a in ((100, 10100.), (1000, 100100.),
                 (100, 10.), (1000, 100.)):
        b = .5
        error2 = np.exp(2*(n+1)*np.log(abs((a-b)/(a+b))))
        projection.append({"N": n, "a": a, "b": b,
                           "squared_projection_error": float(error2)})
    return {"actual_xi_large_anchor_diagnostics": margins,
            "semigroup_diagnostics": semigroup,
            "synthetic_zero_controls": controls,
            "projection_examples": projection}


def main() -> None:
    exact_checks()
    result = numerical_checks()
    result["finite_check_counts"] = COUNTS
    result["runtime"] = {"python": platform.python_version(),
                         "numpy": np.__version__, "scipy": scipy.__version__}
    result["scope"] = {
        "exact": "Fraction identities, scalar margins, rank-one dissipative identity",
        "floating": "binary64 diagnostics; no directed rounding",
        "prime_tail": "truncated at 64 only on Re(s)>50; omitted absolute tail <= integral from 64 to infinity of log(t)t^(-50)dt",
        "not_proved_by_script": ["RH", "new zero-free region", "infinite Toeplitz positivity", "Theorems 1-3"],
    }
    target = Path(__file__).with_name("SPECTRAL_CHECKS.json")
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "pass", "counts": COUNTS,
                      "report": target.name}, sort_keys=True))


if __name__ == "__main__":
    main()
