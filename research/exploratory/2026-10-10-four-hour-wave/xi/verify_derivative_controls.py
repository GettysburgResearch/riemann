#!/usr/bin/env python3
"""Exact finite controls for the derivative/companion research packet.

These controls are synthetic. They neither evaluate actual xi nor establish
the analytic theta-tail saddle theorem; those are separate proof obligations.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def moment(epsilon: Q, order: int) -> Q:
    return 1 + epsilon * 2**order


def quartic(epsilon: Q, lam: Q, q: Q) -> Q:
    return (
        epsilon * (1 + 2 * lam) * q**4
        - (1 + lam) * q**3
        + (lam - 1) * q
        + epsilon * (1 - 2 * lam)
    )


def fg(epsilon: Q, q: Q) -> tuple[Q, Q, Q]:
    ch = (q + 1 / q) / 2
    sh = (q - 1 / q) / 2
    ch2 = (q**2 + 1 / q**2) / 2
    sh2 = (q**2 - 1 / q**2) / 2
    return -ch + epsilon * ch2, -sh + 2 * epsilon * sh2, 4 * epsilon * ch2 - ch


def derivative_geometry(epsilon: Q, c: Q, max_order: int) -> int:
    need(epsilon == c / (2 * c**2 - 1), "source normalization")
    need(Q(10, 17) <= epsilon < 1, "thin-strip coefficient range")
    other = 1 / (2 * c)
    need(2 * epsilon * (-c)**2 - c - epsilon == 0, "negative cosine root")
    need(2 * epsilon * other**2 + other - epsilon == 0, "real cosine root")
    need(-c < -1 < 0 < other < 1, "original complete zero geometry")
    for order in range(1, max_order + 1):
        w = epsilon * 2**order
        if order % 2:
            # sin z (1 + 2*w*cos z); the extra root is strictly inside (-1,0).
            need(-1 < -1 / (2 * w) < 0, f"odd derivative {order}")
        else:
            # P(-1)>0, P(0)<0, P(1)>0 locates the two distinct quadratic roots.
            need(w - 1 > 0 and -w < 0 and w + 1 > 0, f"even derivative {order}")
    return max_order


def root_bracket(epsilon: Q, lam: Q, bits: int = 80) -> dict[str, str]:
    lower, upper = Q(1), Q(2)
    need(quartic(epsilon, lam, lower) < 0, "lower ray endpoint")
    need(quartic(epsilon, lam, upper) > 0, "upper ray endpoint")
    for _ in range(bits):
        midpoint = (lower + upper) / 2
        value = quartic(epsilon, lam, midpoint)
        if value == 0:
            lower = midpoint - Q(1, 2**(bits + 2))
            upper = midpoint + Q(1, 2**(bits + 2))
            break
        if value < 0:
            lower = midpoint
        else:
            upper = midpoint
    need(quartic(epsilon, lam, lower) < 0 < quartic(epsilon, lam, upper), "strict bracket")
    need(upper - lower <= Q(1, 2**bits), "bracket width")
    for q in (Q(1), Q(5, 4), Q(3, 2), Q(2), Q(4)):
        f, g, h = fg(epsilon, q)
        need(quartic(epsilon, lam, q) == 2 * q**2 * (f + lam * g), "quartic identity")
        need(g >= 0 and h > 0, "companion derivative ray sign")
    return {"lambda": str(lam), "exp_y_lower": str(lower), "exp_y_upper": str(upper)}


def sector_control(epsilon: Q, order: int, q: Q) -> None:
    mu = moment(epsilon, order + 1) / moment(epsilon, order)
    var = moment(epsilon, order + 2) / moment(epsilon, order) - mu**2
    need(var / mu**2 <= Q(1, 64), "sector eta squared input")
    weights = ((Q(1), Q(1)), (Q(2), epsilon))
    p = p1 = p2 = n = n1 = Q(0)
    for u, mass in weights:
        base = mass * u**order
        positive = base * (1 + u / mu) * q**u.numerator
        reflected = base * (1 - u / mu) / q**u.numerator
        p += positive
        p1 += u * positive
        p2 += u**2 * positive
        n += reflected
        n1 += u * reflected
    mean = p1 / p
    tilted_var = p2 / p - mean**2
    need(tilted_var >= 0, "positive tilted variance")
    sign = (-1)**order
    need(p + sign * n > 0 and p1 - sign * n1 > 0, "frozen companion sector")
    ratio = mean * (p + sign * n) / (p1 - sign * n1)
    # At T=0, eta<=1/8 gives alpha<=1/16 and beta<9/128,
    # so (alpha+beta)/(1-beta)<17/119=1/7.
    need(abs(ratio - 1) < Q(1, 7), "quantified companion error")


def main() -> None:
    epsilon = Q(10, 17)
    c = Q(5, 4)
    geometry_cases = derivative_geometry(epsilon, c, 64)
    thin_strips = []
    for bits in range(1, 17):
        q = 1 + Q(1, 2**bits)
        ch = (q + 1 / q) / 2
        eps = ch / ((q**2 + 1 / q**2) / 2)
        geometry_cases += derivative_geometry(eps, ch, 32)
        f, _, _ = fg(eps, q)
        need(f == 0, "exact nonreal root at pi + i log q")
        rho = (1 - eps) / (4 * eps - 1)
        need(rho > 0, "wrong extremum residue")
        thin_strips.append({"exp_delta": str(q), "epsilon": str(eps), "rho": str(rho)})

    rho = (1 - epsilon) / (4 * epsilon - 1)
    need(rho == Q(7, 23), "exact fixture residue")
    need(4 * epsilon - 1 == Q(23, 17), "lower curvature")
    need(fg(epsilon, Q(2))[2] == Q(15, 4), "upper curvature")
    lam0 = moment(epsilon, 0) / moment(epsilon, 1)
    need(lam0 == Q(27, 37), "native companion lambda")
    need(-rho / lam0 == Q(-259, 621), "negative adjacent endpoint quotient")
    brackets = [root_bracket(epsilon, lam) for lam in (Q(1, 100), Q(1, 2), lam0, Q(1), Q(2), Q(10))]

    product = Q(1)
    for order in range(64):
        mu = moment(epsilon, order + 1) / moment(epsilon, order)
        mu_next = moment(epsilon, order + 2) / moment(epsilon, order + 1)
        var = moment(epsilon, order + 2) / moment(epsilon, order) - mu**2
        eta_squared = var / mu**2
        need(mu_next == mu * (1 + eta_squared), "adjacent mean identity")
        need((1 / mu - 1 / mu_next) / (1 / mu_next) == eta_squared, "parameter defect identity")
        product *= 1 + eta_squared
    need(product == (moment(epsilon, 65) / moment(epsilon, 64)) / (moment(epsilon, 1) / moment(epsilon, 0)), "telescoping drift")

    sectors = 0
    for order in (8, 9, 16, 17, 32, 33):
        for q in (Q(1), Q(5, 4), Q(2), Q(4), Q(16)):
            sector_control(epsilon, order, q)
            sectors += 1

    # The closed-form sufficient error constant is verified with rational bounds.
    need(Q(65) < Q(9)**2, "sqrt 65 upper bound")
    need((Q(8, 96) + Q(17, 96)) / (1 - Q(17, 96)) == Q(25, 79), "sector constant")

    result = {
        "status": "PASS_EXACT_DERIVATIVE_CONTROLS",
        "arithmetic": "fractions.Fraction only",
        "derivative_geometry_cases": geometry_cases,
        "thin_strip_fixtures": thin_strips,
        "strict_ray_root_brackets": brackets,
        "parameter_drift_identities": 64,
        "companion_sector_cases": sectors,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual_xi_evaluated": False,
        "smooth_source_contour_numerically_verified": False,
        "theta_tail_saddle_theorem_numerically_verified": False,
        "rh_proved": False,
    }
    output = Path(__file__).with_name("verification.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"], f"geometry_cases={geometry_cases} sector_cases={sectors} ray_brackets={len(brackets)}")


if __name__ == "__main__":
    main()
