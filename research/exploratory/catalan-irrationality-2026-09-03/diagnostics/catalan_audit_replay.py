#!/usr/bin/env python3
"""
NON-PROOF DIAGNOSTIC for arXiv:2609.04176v1.

This script independently replays several finite/numerical claims in
Zhi-Wei Sun, "Catalan's constant is irrational":

* exact arithmetic of the final published margin;
* numerical reconstruction of the odd-small-prime constant c_odd;
* numerical reconstruction of the middle-prime integral Lambda_mid;
* finite checking of the reduced occupancy inequality (5.21);
* a cutoff sanity check for the sentence in Lemma 5.5.

It is not a proof certificate.  The quadratures use floating arithmetic,
and the script does not reconstruct Proposition 9.5's full asymptotic ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

try:
    import scipy
    from scipy import integrate, special
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "This diagnostic requires scipy. Install it in an isolated environment."
    ) from exc


EXPECTED_PDF_SHA256 = "1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90"
RHO = 1.0 / 20.0
MID_NUMERATOR = 33042423784278900654572890582560690565493664595111
MID_DENOMINATOR = 187362234062518051579626183549876762148305272280000


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def frac(x: float) -> float:
    return x - math.floor(x)


def small_h(v: float, y: float) -> int:
    """Equation (6.7), evaluated away from its breakpoint set."""
    alpha = frac(20.0 * v)
    beta = frac(41.0 * v)
    gamma = frac(40.0 * v)
    z = (0.5 - y) % 1.0
    eps = 1e-12
    return (
        2 * math.floor(20.0 * v + eps)
        - math.floor(41.0 * v + eps)
        + 2 * int(z < alpha - eps)
        - int(z < v - eps)
        + int(y > beta + eps)
    )


def small_pieces(v: float) -> list[tuple[int, float]]:
    """Constant-y pieces of h_v on [0,1], represented by (value, measure)."""
    alpha = frac(20.0 * v)
    beta = frac(41.0 * v)
    bounds = [0.0, 1.0, 0.5, beta, (0.5 - alpha) % 1.0, (0.5 - v) % 1.0]
    bounds = sorted(set(round(x, 15) for x in bounds if -1e-14 <= x <= 1 + 1e-14))
    if bounds[0] != 0.0:
        bounds.insert(0, 0.0)
    if bounds[-1] != 1.0:
        bounds.append(1.0)
    pieces: list[tuple[int, float]] = []
    for left, right in zip(bounds[:-1], bounds[1:]):
        if right - left <= 1e-14:
            continue
        midpoint = (left + right) / 2.0
        pieces.append((small_h(v, midpoint), right - left))
    return pieces


def k_v(v: float, mass: float) -> float:
    """Integral of the lowest `mass` units in the ladder multiset (6.9)."""
    ladders: list[tuple[int, float]] = []
    # mass <= 2 here; ten ladder levels are far more than needed.
    for level in range(10):
        for value, measure in small_pieces(v):
            ladders.append((value + 2 * level, measure))
    ladders.sort(key=lambda item: item[0])

    remaining = mass
    total = 0.0
    for value, measure in ladders:
        take = min(remaining, measure)
        total += value * take
        remaining -= take
        if remaining <= 1e-12:
            break
    if remaining > 1e-8:
        raise RuntimeError(f"ladder mass underflow at v={v}: {remaining}")
    return total


def q0(v: float) -> float:
    """Equation (6.18)."""
    gamma = frac(40.0 * v)
    positive_part = max(v + gamma - 1.0, 0.0)
    return positive_part + v * v / 2.0 - v * gamma + v / 2.0 + k_v(v, 1.0 + v) - 1.0


def small_integrand(v: float) -> float:
    """The bracketed integrand in (6.21)."""
    return -2.5 * special.zeta(2.0, 1.0 + v) + q0(v) * special.zeta(3.0, 1.0 + v)


def small_breakpoints() -> list[float]:
    """The exact set (6.24), converted to floats after rational deduplication."""
    points: set[Fraction] = {Fraction(0), Fraction(1)}
    for denominator in (19, 20, 40, 41):
        for numerator in range(denominator + 1):
            points.add(Fraction(numerator, denominator))
    for denominator in (82, 84, 122):
        for numerator in range(1, denominator + 1, 2):
            points.add(Fraction(numerator, denominator))
    return [float(x) for x in sorted(points)]


def reconstruct_codd() -> dict[str, Any]:
    points = small_breakpoints()
    integral_value = 0.0
    error_bound = 0.0
    for left, right in zip(points[:-1], points[1:]):
        value, error = integrate.quad(
            small_integrand,
            left,
            right,
            epsabs=1e-13,
            epsrel=1e-13,
            limit=200,
        )
        integral_value += value
        error_bound += error
    i_odd = (RHO**2) * integral_value
    published = 0.006276744728100982604597600317605548503
    return {
        "breakpoint_count": len(points),
        "raw_cell_count": len(points) - 1,
        "I_odd_numeric": i_odd,
        "c_odd_numeric": -i_odd,
        "published_c_odd_decimal": published,
        "absolute_difference": abs((-i_odd) - published),
        "quad_reported_error_sum_scaled": (RHO**2) * error_bound,
    }


def z_mod(x: float, t: float) -> float:
    return (t / 2.0 - x) % t


def middle_e(t: float, rho: float = RHO) -> float:
    """Equations (7.7)-(7.13), selecting the lowest rho-measure."""
    eps = 1e-12
    a = math.floor(1.0 / t + eps)
    d = 1.0 - a * t
    k = math.floor((2.0 + rho) / t + eps)
    e = 2.0 + rho - k * t
    b = math.floor(2.0 / t + eps)
    c = 2.0 - b * t

    bounds = [0.0, t, t / 2.0]
    for value in (e, (t / 2.0 - d) % t, (t / 2.0 - rho) % t):
        if 1e-14 < value < t - 1e-14:
            bounds.append(value)
    bounds = sorted(set(round(value, 15) for value in bounds))

    levels: list[tuple[int, float]] = []
    for left, right in zip(bounds[:-1], bounds[1:]):
        if right - left <= 1e-14:
            continue
        x = (left + right) / 2.0
        z = z_mod(x, t)
        n_b = a + int(z < d - eps)
        n_s = int(z < rho - eps)
        f_t = k - int(x > e + eps)
        base = 2 * n_b - n_s - f_t
        if x < t / 2.0:
            for j in range(1, f_t + 1):
                levels.append((base + 2 * j - 4, right - left))
            levels.append((base + 2 * f_t, right - left))
        else:
            for j in range(1, f_t + 2):
                levels.append((base + 2 * j - 4, right - left))

    levels.sort(key=lambda item: item[0])
    remaining = rho
    selected_integral = 0.0
    for value, measure in levels:
        take = min(remaining, measure)
        selected_integral += value * take
        remaining -= take
        if remaining <= 1e-12:
            break
    if remaining > 1e-8:
        raise RuntimeError(f"middle ladder mass underflow at t={t}: {remaining}")

    c_rho = b * rho + max(rho + c - t, 0.0)
    return c_rho + selected_integral


def middle_primary_breakpoints() -> list[float]:
    points: set[Fraction] = {Fraction(1, 20), Fraction(1)}
    # Floor changes in floor(1/t), floor(2/t), and floor((41/20)/t).
    for numerator in (Fraction(1), Fraction(2), Fraction(41, 20)):
        max_n = int(math.ceil(float(numerator / Fraction(1, 20)))) + 2
        for n in range(1, max_n + 1):
            value = numerator / n
            if Fraction(1, 20) <= value <= 1:
                points.add(value)
    return [float(x) for x in sorted(points)]


def reconstruct_middle() -> dict[str, Any]:
    points = middle_primary_breakpoints()
    value = 0.0
    error = 0.0
    for left, right in zip(points[:-1], points[1:]):
        part, part_error = integrate.quad(
            middle_e,
            left,
            right,
            epsabs=2e-11,
            epsrel=2e-11,
            limit=1000,
        )
        value += part
        error += part_error

    exact = Fraction(MID_NUMERATOR, MID_DENOMINATOR)
    exact_float = float(exact)
    return {
        "primary_breakpoint_count": len(points),
        "Lambda_mid_numeric": value,
        "Lambda_mid_exact_numerator": MID_NUMERATOR,
        "Lambda_mid_exact_denominator": MID_DENOMINATOR,
        "Lambda_mid_exact_float": exact_float,
        "absolute_difference": abs(value - exact_float),
        "quad_reported_error_sum": error,
    }


def phi(q: int, n: int) -> int:
    """Equation (5.1), evaluated in O(1) via (5.2)."""
    quotient, remainder = divmod(n, q)
    return q * quotient * (quotient - 1) // 2 + remainder * quotient


def inequality_521_difference(b: int, s: int, q: int) -> int:
    """Left minus right in (5.21)."""
    return (
        2 * (phi(q, 3 * b + 3) - phi(q, 2 * b + 3) - phi(q, b))
        - phi(q, 2 * b + s + 3)
        - 2 * phi(q, s)
    )


def check_inequality_521(max_b: int) -> dict[str, Any]:
    checked = 0
    minimum: tuple[int, int, int, int] | None = None
    for b in range(20, max_b + 1):
        for s in range(1, b // 20 + 1):
            upper = 2 * b + s + 3
            for q in range(3, upper + 1, 2):
                difference = inequality_521_difference(b, s, q)
                checked += 1
                if minimum is None or difference < minimum[3]:
                    minimum = (b, s, q, difference)
                if difference < 0:
                    return {
                        "max_B": max_b,
                        "cases_checked": checked,
                        "status": "FAIL",
                        "counterexample": {
                            "B": b,
                            "S": s,
                            "Q": q,
                            "left_minus_right": difference,
                        },
                    }
    assert minimum is not None
    return {
        "max_B": max_b,
        "cases_checked": checked,
        "status": "PASS",
        "minimum_case": {
            "B": minimum[0],
            "S": minimum[1],
            "Q": minimum[2],
            "left_minus_right": minimum[3],
        },
        "scope_note": (
            "All odd Q were checked, which is stronger than checking odd prime powers, "
            "but only over the finite B range shown."
        ),
    }


def count_h(k: int, q: int, i: int) -> int:
    """N_{K,Q}(i) from (5.4), for odd q."""
    inverse_two = pow(2, -1, q)
    residue = ((-2 * i - 1) * inverse_two) % q
    first = q if residue == 0 else residue
    if first > k:
        return 0
    return 1 + (k - first) // q


def denominator_layer(b: int, s: int, q: int, upper_index: int) -> int:
    """The denominator layer with a supplied upper row index."""
    return 2 * sum(count_h(b, q, i) for i in range(upper_index + 1)) - phi(q, 2 * b)


def cutoff_sanity_check() -> dict[str, Any]:
    b, s, q = 100, 5, 503
    ideal_upper = 2 * b + s - 1
    actual_upper = 2 * b + s + 2
    ideal = denominator_layer(b, s, q, ideal_upper)
    actual = denominator_layer(b, s, q, actual_upper)
    return {
        "B": b,
        "S": s,
        "Q": q,
        "five_B": 5 * b,
        "Q_is_above_five_B": q > 5 * b,
        "ideal_denominator_layer": ideal,
        "actual_denominator_layer": actual,
        "difference": actual - ideal,
        "interpretation": (
            "The full-row/ideal-row denominator-layer difference can be nonzero "
            "above 5B. Replacing the paper's 5B support sentence by a safe O(B) "
            "cutoff such as 7B preserves the subsequent o(B^2) estimate."
        ),
    }


def margin_arithmetic() -> dict[str, Any]:
    getcontext().prec = 80
    mid_exact = Decimal(MID_NUMERATOR) / Decimal(MID_DENOMINATOR)
    large = Decimal(83) / Decimal(2400)
    raw = Decimal(39) / Decimal(200)
    codd_upper = Decimal("0.006276744728100982604597600317605549")
    published_mid_lower = Decimal("0.17635583792")
    conservative = -codd_upper + published_mid_lower + large - raw
    exact_mid_margin = -codd_upper + mid_exact + large - raw
    paper_threshold = Decimal("0.00966242652523235")
    return {
        "raw_coefficient_39_over_200": str(raw),
        "large_gain_83_over_2400": str(large),
        "codd_upper_endpoint_used": str(codd_upper),
        "published_Lambda_mid_lower_used": str(published_mid_lower),
        "conservative_margin": str(conservative),
        "paper_threshold": str(paper_threshold),
        "conservative_margin_exceeds_threshold": conservative > paper_threshold,
        "margin_using_exact_middle_fraction": str(exact_mid_margin),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, help="Optional path to the attached arXiv PDF")
    parser.add_argument(
        "--max-b",
        type=int,
        default=300,
        help="Finite upper bound for the (5.21) diagnostic (default: 300)",
    )
    args = parser.parse_args()

    result: dict[str, Any] = {
        "status": "NON_PROOF_DIAGNOSTIC",
        "paper": "arXiv:2609.04176v1",
        "environment": {
            "python": platform.python_version(),
            "scipy": scipy.__version__,
        },
        "pdf": None,
        "margin": margin_arithmetic(),
        "small_prime": reconstruct_codd(),
        "middle_prime": reconstruct_middle(),
        "inequality_5_21": check_inequality_521(args.max_b),
        "cutoff_sanity": cutoff_sanity_check(),
        "limitations": [
            "Floating quadrature is not a directed interval certificate.",
            "The finite (5.21) search is not a proof for all B.",
            "The script does not reproduce the 178 merged small-prime cells exactly.",
            "The script does not reproduce the 235 exact affine middle-prime cells.",
            "The script does not derive Proposition 9.5's full same-scalar asymptotic ledger.",
        ],
    }
    if args.pdf is not None:
        digest = sha256_file(args.pdf)
        result["pdf"] = {
            "path": str(args.pdf),
            "sha256": digest,
            "matches_import_receipt": digest == EXPECTED_PDF_SHA256,
            "size_bytes": args.pdf.stat().st_size,
        }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
