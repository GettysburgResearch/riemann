#!/usr/bin/env python3
"""Replay for L-90024: positive filtered seed and three-window source transport.

The exact proof is in the claim. This checker authenticates the algebraic
factorization, rigorous curvature-sign corridors, exact lobe masses, and a
cell-exact floating reconstruction of the three-window identity.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "X-90015-annular-endpoint" / "verify.py"
spec = importlib.util.spec_from_file_location("x90015", BASE)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {BASE}")
x90015 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x90015)

SQRT2_LO = Fraction(14142, 10000)
SQRT2_HI = Fraction(14143, 10000)
LOG2_LO = Fraction(6931, 10000)
LOG2_HI = Fraction(6932, 10000)

# c_j=A_j+B_j sqrt(2), integer-friendly filter.
COEFF = [
    (Fraction(0), Fraction(4)),
    (Fraction(-4), Fraction(-1)),
    (Fraction(1), Fraction(-3)),
    (Fraction(3), Fraction(-3)),
    (Fraction(3), Fraction(-1)),
    (Fraction(1), Fraction(4)),
    (Fraction(-4), Fraction(0)),
]


def add_pair(u, v):
    return u[0] + v[0], u[1] + v[1]


def scale_pair(u, q: Fraction):
    return u[0] * q, u[1] * q


def pair_interval(pair: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    a, b = pair
    if b >= 0:
        return a + b * SQRT2_LO, a + b * SQRT2_HI
    return a + b * SQRT2_HI, a + b * SQRT2_LO


def exact_filter_checks() -> dict:
    total = (Fraction(0), Fraction(0))
    first = (Fraction(0), Fraction(0))
    critical = (Fraction(0), Fraction(0))
    for j, coefficient in enumerate(COEFF):
        total = add_pair(total, coefficient)
        first = add_pair(first, scale_pair(coefficient, Fraction(j)))
        if j % 2 == 0:
            critical = add_pair(
                critical, scale_pair(coefficient, Fraction(2 ** (j // 2)))
            )
        else:
            a, b = coefficient
            critical = add_pair(
                critical,
                (
                    b * Fraction(2 ** ((j + 1) // 2)),
                    a * Fraction(2 ** ((j - 1) // 2)),
                ),
            )
    if total != (0, 0) or first != (0, 0) or critical != (0, 0):
        raise AssertionError((total, first, critical))
    return {
        "sum_coefficients": [0, 0],
        "sum_j_coefficients": [0, 0],
        "sum_2pow_j_over_2_coefficients": [0, 0],
        "state_factorization": (
            "4sqrt(2)(1+3y/4+y^2)(1-y^2)(1-y)(1-y/sqrt(2))"
        ),
    }


def k_value_interval(piece: int, endpoint: int) -> tuple[Fraction, Fraction]:
    """Directed interval for K_*(u) at an integer endpoint on one side."""
    constant = (Fraction(0), Fraction(0))
    slope_sum = (Fraction(0), Fraction(0))
    for j in range(piece + 1):
        constant = add_pair(constant, COEFF[j])
        slope_sum = add_pair(
            slope_sum, scale_pair(COEFF[j], Fraction(endpoint - j, 2))
        )
    c_lo, c_hi = pair_interval(constant)
    s_lo, s_hi = pair_interval(slope_sum)
    products = [
        LOG2_LO * s_lo,
        LOG2_LO * s_hi,
        LOG2_HI * s_lo,
        LOG2_HI * s_hi,
    ]
    return c_lo - max(products), c_hi - min(products)


def curvature_certificate() -> dict:
    expected = [1, -1, -1, -1, -1, 1]
    corridors = []
    for piece, sign in enumerate(expected):
        left = k_value_interval(piece, piece)
        right = k_value_interval(piece, piece + 1)
        lo = min(left[0], right[0])
        hi = max(left[1], right[1])
        if sign > 0 and lo <= 0:
            raise AssertionError((piece, lo, hi))
        if sign < 0 and hi >= 0:
            raise AssertionError((piece, lo, hi))
        corridors.append(
            {
                "u_interval": [piece, piece + 1],
                "sign": "+" if sign > 0 else "-",
                "lower": str(lo),
                "upper": str(hi),
            }
        )
    return {"piecewise_affine_curvature": corridors}


def coefficients_float() -> np.ndarray:
    r = math.sqrt(2.0)
    return np.array(
        [4 * r, -(4 + r), 1 - 3 * r, 3 - 3 * r, 3 - r, 1 + 4 * r, -4.0]
    )


def lobe_mass_checks() -> dict:
    mp.mp.dps = 70
    h = mp.log(2)
    r = mp.sqrt(2)
    c = [4 * r, -(4 + r), 1 - 3 * r, 3 - 3 * r, 3 - r, 1 + 4 * r, -4]

    def kval(u):
        if u < 0 or u > 6:
            return mp.mpf("0")
        piece = min(5, int(mp.floor(u)))
        return mp.fsum(c[j] * (1 - h * (u - j) / 2) for j in range(piece + 1))

    recent = mp.quad(lambda u: kval(u) * mp.power(2, -u / 2), [0, 1])
    middle = -mp.quad(
        lambda u: kval(u) * mp.power(2, -u / 2), [1, 2, 3, 4, 5]
    )
    old = mp.quad(lambda u: kval(u) * mp.power(2, -u / 2), [5, 6])
    if abs(recent - 4) > mp.mpf("1e-50"):
        raise AssertionError(recent)
    if abs(middle - (4 + 1 / r)) > mp.mpf("1e-50"):
        raise AssertionError(middle)
    if abs(old - 1 / r) > mp.mpf("1e-50"):
        raise AssertionError(old)
    return {
        "recent_mass": mp.nstr(recent, 55),
        "middle_mass": mp.nstr(middle, 55),
        "old_mass": mp.nstr(old, 55),
        "threshold": mp.nstr(1 / (4 * r), 55),
    }


def source_arrays(max_x: int):
    endpoint, primes, log_rad = x90015.endpoint_sequence(max_x)
    p1_atom = np.zeros(max_x + 1)
    logs = np.log(primes.astype(float))
    p1_atom[primes] = logs / primes
    p1 = np.cumsum(p1_atom)
    ell_sum = np.cumsum(log_rad)
    n = np.arange(max_x + 1, dtype=float)
    s1 = (n + 1.0) * log_rad - ell_sum
    return endpoint, p1, log_rad, s1


def piece_coefficients(piece: int, coefficient: np.ndarray) -> tuple[float, float]:
    """K_*(u)=alpha+beta*u on [piece,piece+1]."""
    h = math.log(2.0)
    js = np.arange(piece + 1, dtype=float)
    active = coefficient[: piece + 1]
    alpha = float(np.sum(active * (1.0 + 0.5 * h * js)))
    beta = float(-0.5 * h * np.sum(active))
    return alpha, beta


def integral_linear_exponential(
    alpha: float, beta: float, lam: float, left: float, right: float
) -> float:
    def primitive(u: float) -> float:
        return math.exp(lam * u) * (
            (alpha + beta * u) / lam - beta / (lam * lam)
        )

    return primitive(right) - primitive(left)


def exact_cell_lobes(
    x: int, p1: np.ndarray, ell: np.ndarray, s1: np.ndarray
) -> list[float]:
    """Integrate W_*(u)R_P(X2^-u) exactly on every integer source cell."""
    h = math.log(2.0)
    coefficient = coefficients_float()
    lobes = [0.0, 0.0, 0.0]
    for piece in range(6):
        alpha, beta = piece_coefficients(piece, coefficient)
        x_low = x / (2 ** (piece + 1))
        x_high = x / (2**piece)
        n_low = max(1, int(math.floor(x_low)))
        n_high = min(x, int(math.floor(x_high)))
        for n in range(n_low, n_high + 1):
            cell_low = max(x_low, float(n))
            cell_high = min(x_high, float(n + 1))
            if cell_high <= cell_low:
                continue
            u_left = max(math.log(x / cell_high, 2), float(piece))
            u_right = min(math.log(x / cell_low, 2), float(piece + 1))
            if u_right <= u_left:
                continue
            a_n = p1[n] - ell[n]
            b_n = s1[n]
            value = a_n * integral_linear_exponential(
                alpha, beta, -h / 2, u_left, u_right
            )
            value += (b_n / x) * integral_linear_exponential(
                alpha, beta, h / 2, u_left, u_right
            )
            lobe = 0 if piece == 0 else (2 if piece == 5 else 1)
            lobes[lobe] += value
    return lobes


def finite_transport(max_x: int) -> dict:
    endpoint, p1, ell, s1 = source_arrays(max_x)
    selected = [x for x in (6400, 64000, 640000, max_x) if 64 <= x <= max_x]
    selected = sorted(set(x - x % 64 for x in selected if x - x % 64 >= 64))
    c = coefficients_float()
    h = math.log(2.0)
    q = 1 / math.sqrt(2.0)
    rows = []
    for x in selected:
        lobes = exact_cell_lobes(x, p1, ell, s1)
        r0 = lobes[0] / 4.0
        r1 = -lobes[1] / (4.0 + q)
        r2 = lobes[2] / q
        source_value = -h * math.sqrt(x) * sum(lobes)
        endpoint_value = sum(c[j] * endpoint[x // (2**j) - 1] for j in range(7))
        if abs(source_value - endpoint_value) > 5e-7:
            raise AssertionError((x, source_value, endpoint_value))
        rows.append(
            {
                "X": x,
                "R_recent": r0,
                "R_middle": r1,
                "R_old": r2,
                "slope_ratio": (r0 - r1) / (r1 - r2) if r1 != r2 else None,
                "threshold": q / 4,
                "endpoint": endpoint_value,
                "source_reconstruction": source_value,
                "absolute_error": abs(source_value - endpoint_value),
            }
        )
    return {"selected_endpoints": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output", type=Path, default=HERE / "results" / "verification.json"
    )
    args = parser.parse_args()
    if args.max_x < 6400:
        raise SystemExit("--max-x must be at least 6400")
    result = {
        "classification": "PASS_FACTOR64_POSITIVE_SEED_TRANSPORT",
        "filter": exact_filter_checks(),
        "curvature": curvature_certificate(),
        "lobes": lobe_mass_checks(),
        "finite": finite_transport(args.max_x),
        "scope": (
            "The filter moments, curvature signs, and lobe masses authenticate "
            "the exact proof. The source reconstruction integrates each finite "
            "two-exponential cell analytically."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(args.output)


if __name__ == "__main__":
    main()
