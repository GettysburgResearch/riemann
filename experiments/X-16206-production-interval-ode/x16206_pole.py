"""Arb Frobenius/pole Cauchy emitter for X-16206."""
from __future__ import annotations
from fractions import Fraction
from typing import Any, Iterable
from flint import acb, arb, ctx
from x16206_common import (GAMMA, FROBENIUS_TERMS, FROBENIUS_PREC_BITS,
    POLE_OFFSET, exact_arb, interval_arb, arb_bounds, arb_interval_json, upper_json, fstr)

def poly_next(
    current: list[arb], previous: list[arb], previous2: list[arb], k: int, mu_mid: Fraction
) -> list[arb]:
    den = arb(2 * (k + 1) ** 2)
    a0 = (arb(k * (k + 1) + GAMMA * GAMMA) - exact_arb(mu_mid)) / GAMMA
    degree = max(len(current) + 1, len(previous), len(previous2))
    out = [arb(0) for _ in range(degree)]
    for j, value in enumerate(current):
        out[j] -= a0 * value / den
        out[j + 1] += value / (GAMMA * den)
    for j, value in enumerate(previous):
        out[j] -= 2 * value / den
    for j, value in enumerate(previous2):
        out[j] -= value / (GAMMA * den)
    return out


def poly_eval(coeffs: list[arb], delta: arb) -> arb:
    value = arb(0)
    for coefficient in reversed(coeffs):
        value = value * delta + coefficient
    return value


def max_fraction(values: Iterable[Fraction]) -> Fraction:
    values = list(values)
    if not values:
        raise ValueError("empty maximum")
    return max(values)


def frobenius_cauchy(mu_lo: Fraction, mu_hi: Fraction) -> dict[str, Any]:
    ctx.prec = FROBENIUS_PREC_BITS
    mu_mid = (mu_lo + mu_hi) / 2
    mu_radius = (mu_hi - mu_lo) / 2
    delta = arb(0, fstr(mu_radius))

    tm2: list[arb] = []
    tm1: list[arb] = []
    current: list[arb] = [arb(1)]
    sum_y: list[arb] = [arb(1)]
    sum_yp: list[arb] = [arb(0)]
    last_polys: list[list[arb]] = [current]

    for k in range(FROBENIUS_TERMS):
        nxt = poly_next(current, tm1, tm2, k, mu_mid)
        if len(sum_y) < len(nxt):
            sum_y.extend(arb(0) for _ in range(len(nxt) - len(sum_y)))
            sum_yp.extend(arb(0) for _ in range(len(nxt) - len(sum_yp)))
        for j, value in enumerate(nxt):
            sum_y[j] += value
            sum_yp[j] += (k + 1) * GAMMA * value
        tm2, tm1, current = tm1, current, nxt
        last_polys.append(current)
        if len(last_polys) > 3:
            last_polys.pop(0)

    y = poly_eval(sum_y, delta)
    yp = poly_eval(sum_yp, delta)
    last_abs = [arb_bounds(poly_eval(p, delta).abs_upper())[1] for p in last_polys]
    M = max_fraction(last_abs)
    K = FROBENIUS_TERMS
    q = (
        Fraction(1, 2 * GAMMA)
        + Fraction(GAMMA, 2 * (K + 1) ** 2)
        + Fraction(1, (K + 1) ** 2)
        + Fraction(1, 2 * GAMMA * (K + 1) ** 2)
    )
    if not q < 1:
        raise RuntimeError("Frobenius tail majorant is not contracting")
    y_tail = 3 * q * M / (1 - q)
    yp_tail = GAMMA * M * (
        (3 * K - 3) * q / (1 - q) + 9 * q / (1 - q) ** 2
    )
    y = y.union(y + arb(0, fstr(y_tail)))
    yp = yp.union(yp + arb(0, fstr(yp_tail)))

    # Liouville coordinate at z0 = 1+1/gamma. The substitution z=1+u^2
    # removes the endpoint square-root singularity, so Arb can integrate an
    # analytic interval integrand uniformly over the certified sigma interval.
    sigma_lo = mu_lo / (GAMMA * GAMMA)
    sigma_hi = mu_hi / (GAMMA * GAMMA)
    s = interval_arb(sigma_lo, sigma_hi)
    z = arb(GAMMA + 1) / GAMMA
    ctx.prec = 768
    u_max = (arb(1) / GAMMA).sqrt()
    s_acb = acb(s)
    def xi_integrand(u: acb, analytic: bool) -> acb:
        x = 1 + u * u
        return 2 * ((x * x - s_acb) / (2 + u * u)).sqrt()
    xi_acb = acb.integral(
        xi_integrand,
        0,
        acb(u_max),
        rel_tol=arb(2) ** -500,
        abs_tol=arb(2) ** -500,
        deg_limit=400,
        depth_limit=20,
    )
    if not xi_acb.imag.contains(0):
        raise RuntimeError("Liouville integral acquired a nonzero imaginary part")
    xi = xi_acb.real
    xi_prime = ((z * z - s) / (z * z - 1)).sqrt()

    prefactor = ((z * z - 1) * (z * z - s)) ** Fraction(-1, 4) * xi.sqrt()
    arg = GAMMA * xi
    j0 = arg.bessel_j(0)
    j1 = arg.bessel_j(1)
    bessel = prefactor * j0
    log_prefactor_prime = (
        -arb(1) / 4 * (2 * z / (z * z - 1) + 2 * z / (z * z - s))
        + arb(1) / 2 * xi_prime / xi
    )
    bessel_prime = prefactor * log_prefactor_prime * j0 - prefactor * j1 * GAMMA * xi_prime
    mismatch_value = (y - bessel).abs_upper()
    mismatch_derivative_scaled = ((yp - bessel_prime) / GAMMA).abs_upper()
    mismatch_total = mismatch_value + mismatch_derivative_scaled

    return {
        "pole_point_z": f"{GAMMA + 1}/{GAMMA}",
        "frobenius_terms": FROBENIUS_TERMS,
        "mu_mid": fstr(mu_mid),
        "mu_radius": fstr(mu_radius),
        "y_interval": arb_interval_json(y),
        "yprime_interval": arb_interval_json(yp),
        "xi_interval": arb_interval_json(xi),
        "xi_prime_interval": arb_interval_json(xi_prime),
        "bessel_y_interval": arb_interval_json(bessel),
        "bessel_yprime_interval": arb_interval_json(bessel_prime),
        "initial_value_mismatch_upper": upper_json(arb_bounds(mismatch_value)[1]),
        "initial_derivative_mismatch_over_gamma_upper": upper_json(
            arb_bounds(mismatch_derivative_scaled)[1]
        ),
        "initial_scaled_state_mismatch_upper": upper_json(arb_bounds(mismatch_total)[1]),
        "frobenius_tail_y_upper": upper_json(y_tail),
        "frobenius_tail_yprime_upper": upper_json(yp_tail),
        "tail_contraction_q": fstr(q),
    }
