"""Non-directed quadrature of the literal Xi growing-order current.

This is a discovery tool, not a certificate. It evaluates a truncated theta
series and bounded quadrature windows at high precision. Analytic tail and
uniform-limit proofs live in the accompanying note, not in mpmath precision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import mpmath as mp


def nearest_odd(value):
    return max(1, 2 * int(mp.nint((value - 1) / 2)) + 1)


def current_order(xi, mode, parameter):
    if type(parameter) is not str or not 1 <= len(parameter) <= 64:
        raise ValueError("short decimal parameter string required")
    e = mp.exp(xi)
    if mode == "fixed":
        k = int(parameter)
        if str(k) != parameter or k < 1 or k % 2 != 1:
            raise ValueError("fixed order must be an odd positive integer")
        return k
    parameter_value = mp.mpf(parameter)
    if not mp.isfinite(parameter_value) or abs(parameter_value) > 1_000_000:
        raise ValueError("finite parameter resource cap")
    if mode in ("macro", "boundary") and parameter_value <= 0:
        raise ValueError("positive scale parameter required")
    if mode == "micro" and parameter_value < 0:
        raise ValueError("nonnegative microscopic parameter required")
    if mode == "intermediate" and not 0 < parameter_value <= 4:
        raise ValueError("intermediate exponent must lie in (0,4]")
    if mode == "micro":
        return nearest_odd(mp.mpf(parameter) * xi * mp.sqrt(mp.pi * e))
    if mode == "macro":
        return nearest_odd(mp.mpf(parameter) * xi * e)
    if mode == "boundary":
        return nearest_odd(mp.mpf(parameter) * 2 * mp.pi * xi * e**2)
    if mode == "boundary-offset":
        return nearest_odd(
            2 * mp.pi * xi * e**2
            - mp.mpf("3.5") * xi
            - mp.mpf("1.5")
            - 1 / (4 * xi + 2)
            + mp.mpf(parameter)
        )
    if mode == "intermediate":
        return nearest_odd(xi * mp.exp(mp.mpf(parameter) * xi))
    raise ValueError("mode")


def log_phi(t, dps):
    """Even full-line kernel, with the first orbit factored out."""
    t = abs(t)
    x = mp.exp(2 * t)
    coefficient = 3 / (2 * mp.pi * x)
    series = mp.mpf(0)
    threshold = mp.power(10, -(dps + 12))
    for n in range(1, 129):
        term = (n**4 - coefficient * n**2) * mp.exp(-mp.pi * (n * n - 1) * x)
        series += term
        if n >= 2 and term < threshold * series:
            return mp.log(4 * mp.pi**2) + mp.mpf("4.5") * t - mp.pi * x + mp.log(
                series
            ), n
    raise RuntimeError("theta series guard exhausted")


def saddle(xi, k):
    e = mp.exp(xi)
    lo, hi = mp.mpf(0), mp.mpf(1)

    def slope(d):
        return k / (xi + d) - 2 * mp.pi * e * mp.sinh(d)

    while slope(hi) > 0:
        hi *= 2
        if hi > 128:
            raise RuntimeError("saddle bracket guard")
    for _ in range(mp.mp.prec + 20):
        mid = (lo + hi) / 2
        if slope(mid) > 0:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / 2
    j = 2 * mp.pi * e * mp.cosh(a) + k / (xi + a) ** 2
    return a, j


def sinhc(x):
    return mp.sinh(x) / x if x else mp.mpf(1)


def run_case(xi_value, mode, parameter, dps=55, radius=28):
    if type(xi_value) is not int or not 1 <= xi_value <= 20:
        raise ValueError("integer source frequency cap")
    if type(dps) is not int or not 30 <= dps <= 120:
        raise ValueError("precision cap")
    if type(radius) is not int or not 16 <= radius <= 48:
        raise ValueError("quadrature window cap")
    started = time.monotonic()
    with mp.workdps(dps):
        xi = mp.mpf(xi_value)
        e = mp.exp(xi)
        epsilon = 1 / mp.sqrt(mp.pi * e)
        k = current_order(xi, mode, parameter)
        if not 1 <= k <= 100_000_000_001 or k % 2 != 1:
            raise ValueError("odd order resource cap")
        kappa = k * epsilon / xi
        b = k / (xi * e)
        a, j = saddle(xi, k)
        separated = mode in ("macro", "intermediate", "boundary", "boundary-offset")
        center = a if separated else mp.mpf(0)
        scale = 1 / mp.sqrt(j) if separated else epsilon
        anchor = a if separated else epsilon * max(1, kappa / 2)
        phi_center, theta_max = log_phi(xi / 2, dps)
        cache = {}

        def data(d):
            nonlocal theta_max
            key = d._mpf_
            if key in cache:
                return cache[key]
            if len(cache) > 150_000:
                raise RuntimeError("quadrature evaluation cap")
            left, nleft = log_phi((xi - d) / 2, dps)
            right, nright = log_phi((xi + d) / 2, dps)
            theta_max = max(theta_max, nleft, nright)
            log_common = k * mp.log1p(d / xi) + left + right - 2 * phi_center
            if d == 0:
                minus, plus = mp.mpf(0), mp.mpf(2)
            else:
                r = (xi - d) / (xi + d)
                if r > 0:
                    exponent = k * mp.log(r)
                    minus = -mp.expm1(exponent)
                    plus = 1 + mp.exp(exponent)
                elif r < 0:
                    exponent = k * mp.log(-r)
                    minus = 1 + mp.exp(exponent)
                    plus = -mp.expm1(exponent)
                else:
                    minus = plus = mp.mpf(1)
            value = (log_common, minus, plus)
            cache[key] = value
            return value

        log_anchor, minus_anchor, _ = data(anchor)
        reference = log_anchor + mp.log(anchor * minus_anchor)
        lower = max(-mp.mpf(radius), -center / scale) if separated else mp.mpf(0)
        upper = mp.mpf(radius) if separated else mp.mpf(radius) + kappa
        candidates = [lower, upper]
        candidates += [mp.mpf(i) for i in range(-radius, radius + 1, 4)]
        candidates += [mp.mpf(0), (anchor - center) / scale]
        nodes = sorted({t for t in candidates if lower <= t <= upper})

        def integral(power=0, plus=False, v_power=0, h=None):
            def integrand(t):
                d = center + scale * t
                if d < 0:
                    return mp.mpf(0)
                common, minus, positive = data(d)
                value = mp.exp(common - reference)
                value *= positive if plus else d * minus
                value *= d**power
                if v_power:
                    value *= (mp.sqrt(j) * (d - a)) ** v_power
                if h is not None:
                    value *= sinhc(h * d)
                return value

            return mp.quad(integrand, nodes)

        mass = integral()
        moment2 = integral(power=2) / mass
        moment4 = integral(power=4) / mass
        gain = xi * integral(plus=True) / (2 * mass)
        phase = integral(power=2, plus=True) / (2 * xi * mass)
        moment_v1 = integral(v_power=1) / mass
        moment_v2 = integral(v_power=2) / mass
        plus_moment2 = xi**2 * phase / gain
        boundary_mode = mode in ("boundary", "boundary-offset")
        critical_coordinate = (
            k
            - 2 * mp.pi * xi * e**2
            + mp.mpf("3.5") * xi
            + mp.mpf("1.5")
            + 1 / (4 * xi + 2)
        )
        critical_scaled_moment = (
            mp.pi * e**2 * (1 + 1 / (2 * xi)) * (plus_moment2 - xi**2)
        )
        tau = mp.mpf("0.75")
        current_micro = integral(h=tau / epsilon) / mass if not separated else None
        current_fixed = integral(h=mp.mpf(1)) / mass

        def out(v):
            return None if v is None else mp.nstr(v, 28)

        result = {
            "xi": xi_value,
            "mode": mode,
            "parameter": parameter,
            "K": k,
            "kappa": out(kappa),
            "b": out(b),
            "saddle_a": out(a),
            "saddle_J_over_E": out(j / e),
            "m2": out(moment2),
            "m4": out(moment4),
            "micro_scaled_m2": out(moment2 / epsilon**2),
            "micro_predicted_m2": out(mp.mpf("1.5") + kappa**2 / 4)
            if not separated
            else None,
            "micro_scaled_gain": out(k * gain / (mp.pi * xi**2 * e)),
            "micro_scaled_phase": out(2 * k * phase),
            "micro_predicted_phase": out(1 + kappa**2 / 2) if not separated else None,
            "separated_m2_ratio": out(moment2 / a**2),
            "separated_gain_ratio": out(2 * a * gain / xi),
            "separated_phase_ratio": out(2 * xi * phase / a),
            "gain_minus_phase": out(gain - phase),
            "plus_measure_second_moment": out(plus_moment2),
            "critical_inferred_constant": out(
                k
                + j * xi**2 * (1 - phase / gain)
                - 2 * mp.pi * xi * e**2
                + mp.mpf("3.5") * xi
            )
            if boundary_mode
            else None,
            "critical_predicted_constant": out(-mp.mpf("1.5") - 1 / (4 * xi + 2))
            if boundary_mode
            else None,
            "critical_window_coordinate": out(critical_coordinate)
            if boundary_mode
            else None,
            "critical_window_scaled_moment": out(critical_scaled_moment)
            if boundary_mode
            else None,
            "critical_window_residual": out(
                critical_scaled_moment - critical_coordinate
            )
            if boundary_mode
            else None,
            "conditional_v_mean": out(moment_v1),
            "conditional_v_second_moment": out(moment_v2),
            "current_h1": out(current_fixed),
            "current_h1_saddle_prediction": out(sinhc(a)),
            "current_tau075": out(current_micro),
            "current_tau075_prediction": out(
                mp.exp(tau**2 / 4) * sinhc(kappa * tau / 2)
            )
            if not separated
            else None,
            "theta_largest_n": theta_max,
            "unique_quadrature_nodes": len(cache),
            "quadrature_coordinate": "sqrt(J)*(d-a)" if separated else "d/epsilon",
            "quadrature_lower": out(lower),
            "quadrature_upper": out(upper),
            "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
            "precision_decimal_digits": dps,
            "certified": False,
            "bounded_quadrature_not_full_integral_certificate": True,
            "elapsed_seconds": round(time.monotonic() - started, 3),
        }
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xi", type=int, required=True)
    parser.add_argument(
        "--mode",
        choices=(
            "fixed",
            "micro",
            "macro",
            "intermediate",
            "boundary",
            "boundary-offset",
        ),
        required=True,
    )
    parser.add_argument("--parameter", required=True)
    parser.add_argument("--dps", type=int, default=55)
    parser.add_argument("--radius", type=int, default=28)
    args = parser.parse_args()
    result = run_case(args.xi, args.mode, args.parameter, args.dps, args.radius)
    result["producer_sha256_lf"] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
