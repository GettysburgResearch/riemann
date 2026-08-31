"""Non-directed, bounded quadrature for the literal Xi all-order saddle.

The theta evaluator is authenticated to a frozen parent before import. Neither
mpmath precision nor a bounded quadrature window certifies the full integral.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = "af809698fe6cb5046a5bcc00e9175296e4597060"
PARENT_PATH = "research/exploratory/xi_odd_current_double_scaling_scout.py"


def authenticated_parent():
    path = ROOT / PARENT_PATH
    expected = subprocess.run(
        ["git", "show", f"{PARENT}:{PARENT_PATH}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout.replace(b"\r\n", b"\n")
    actual = path.read_bytes().replace(b"\r\n", b"\n")
    if actual != expected:
        raise ValueError("frozen theta evaluator differs from current local file")
    spec = importlib.util.spec_from_file_location("xi_global_parent_scout", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("parent import loader unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, hashlib.sha256(expected).hexdigest()


def scale_parameter(text, lower, upper):
    if type(text) is not str or not 1 <= len(text) <= 64:
        raise ValueError("short numeric parameter string required")
    value = 2 * mp.pi if text == "2*pi" else mp.mpf(text)
    if not mp.isfinite(value) or not lower < value <= upper:
        raise ValueError("parameter outside finite computational resource cap")
    return value


def global_saddle(xi, k):
    """Maximizer of the declared globally concave phase, not a fitted mode."""
    if not mp.isfinite(xi) or xi < 2 or type(k) is not int or k < 1 or k % 2 != 1:
        raise ValueError("xi>=2 and a positive odd integer order required")
    if k.bit_length() > 1024:
        raise ValueError("odd-order bit cap")
    e = mp.exp(xi)
    left = 2 * mp.pi * xi * (e**2 - 1)
    right = 2 * xi * (mp.pi * (e**2 + 1) - mp.mpf("4.5"))
    if left <= k <= right:
        a, branch = xi, "corner"
    else:
        balanced = k < left
        lo = mp.mpf(0) if balanced else xi
        hi = xi if balanced else 2 * xi

        def slope(d):
            if balanced:
                return k / (xi + d) - 2 * mp.pi * e * mp.sinh(d)
            return k / (xi + d) + mp.mpf("4.5") - 2 * mp.pi * mp.cosh(xi) * mp.exp(d)

        while slope(hi) > 0:
            hi *= 2
            if hi > 2048:
                raise RuntimeError("global saddle bracket guard")
        for _ in range(mp.mp.prec + 24):
            mid = (lo + hi) / 2
            if slope(mid) > 0:
                lo = mid
            else:
                hi = mid
        a, branch = (lo + hi) / 2, "balanced" if balanced else "unbalanced"
    j = k / (xi + a) ** 2 + mp.pi * (mp.exp(xi + a) + mp.exp(abs(xi - a)))
    return a, j, branch


def old_balanced_center(xi, k):
    """Deliberately wrong beyond xi; retained only as a falsification control."""
    lo, hi = mp.mpf(0), mp.mpf(1)

    def slope(d):
        return k / (xi + d) - 2 * mp.pi * mp.exp(xi) * mp.sinh(d)

    while slope(hi) > 0:
        hi *= 2
        if hi > 2048:
            raise RuntimeError("old-center comparison bracket guard")
    for _ in range(mp.mp.prec + 24):
        mid = (lo + hi) / 2
        if slope(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run_case(xi_value, gamma_text, b_text="1", dps=55, radius=24):
    if type(xi_value) is not int or not 2 <= xi_value <= 32:
        raise ValueError("integer xi resource cap: 2,...,32")
    if type(dps) is not int or not 40 <= dps <= 120:
        raise ValueError("requested precision cap: 40,...,120")
    if type(radius) is not int or not 16 <= radius <= 48:
        raise ValueError("quadrature radius cap: 16,...,48")
    parent, parent_hash = authenticated_parent()
    started = time.monotonic()
    with mp.workdps(50):
        gamma = scale_parameter(gamma_text, mp.mpf("0.5"), 8)
        b = scale_parameter(b_text, 0, 1_000_000)
        log10k = mp.log10(b * xi_value) + gamma * xi_value / mp.log(10)
        working_dps = dps + max(0, int(mp.ceil(log10k))) + 24
    with mp.workdps(working_dps):
        xi = mp.mpf(xi_value)
        gamma = scale_parameter(gamma_text, mp.mpf("0.5"), 8)
        b = scale_parameter(b_text, 0, 1_000_000)
        k = parent.nearest_odd(b * xi * mp.exp(gamma * xi))
        if k.bit_length() > 1024:
            raise ValueError("odd-order bit cap")
        a, j, branch = global_saddle(xi, k)
        root_j, length = mp.sqrt(j), a * mp.sqrt(j)
        old_a = old_balanced_center(xi, k)
        anchor_l, theta_l = parent.log_phi((xi - a) / 2, dps + 12)
        anchor_r, theta_r = parent.log_phi((xi + a) / 2, dps + 12)
        theta_max = max(theta_l, theta_r)
        cache = {}

        def data(v):
            nonlocal theta_max
            key = v._mpf_
            if key in cache:
                return cache[key]
            if len(cache) > 150_000:
                raise RuntimeError("quadrature evaluation cap")
            d = a + v / root_j
            if d < 0:
                return mp.mpf(0), mp.mpf(0), mp.mpf(0)
            left_phi, nl = parent.log_phi((xi - d) / 2, dps + 12)
            right_phi, nr = parent.log_phi((xi + d) / 2, dps + 12)
            theta_max = max(theta_max, nl, nr)
            log_weight = (
                k * mp.log1p((d - a) / (xi + a))
                + left_phi
                - anchor_l
                + right_phi
                - anchor_r
            )
            r = (xi - d) / (xi + d)
            if r > 0:
                exponent = k * mp.log(r)
                minus, plus = -mp.expm1(exponent), 1 + mp.exp(exponent)
            elif r < 0:
                exponent = k * mp.log(-r)
                minus, plus = 1 + mp.exp(exponent), -mp.expm1(exponent)
            else:
                minus = plus = mp.mpf(1)
            weight = mp.exp(log_weight)
            value = d, weight * minus, weight * plus
            cache[key] = value
            return value

        lower, upper = max(-mp.mpf(radius), -length), mp.mpf(radius)
        nodes = sorted(
            {lower, upper, mp.mpf(0)}
            | {mp.mpf(n) for n in range(-radius, radius + 1, 4) if lower <= n <= upper}
        )

        def integral(power=0, plus=False, v_power=0, tau=None):
            def integrand(v):
                d, minus, positive = data(v)
                result = (positive if plus else minus) * d**power * v**v_power
                if tau is not None:
                    if not tau:
                        response = d / a
                    else:
                        response = mp.cosh(tau * v) + mp.coth(tau * length) * mp.sinh(
                            tau * v
                        )
                    result *= response
                return result

            return mp.quad(integrand, nodes)

        mass = integral(power=1)
        i0plus, i2plus = integral(plus=True), integral(power=2, plus=True)
        gain, phase = xi * i0plus / (2 * mass), i2plus / (2 * xi * mass)
        mean_v, second_v = (
            integral(power=1, v_power=1) / mass,
            integral(power=1, v_power=2) / mass,
        )
        responses = []
        for tau in (mp.mpf(0), mp.mpf("0.25"), mp.mpf("0.75"), mp.mpf(1)):
            value = a * integral(tau=tau) / mass
            responses.append(
                {
                    "tau": str(tau),
                    "scaled_response": mp.nstr(value, 28),
                    "predicted": mp.nstr(mp.exp(tau**2 / 2), 28),
                }
            )

        def out(value):
            return mp.nstr(value, 28)

        return {
            "xi": xi_value,
            "gamma": gamma_text,
            "b": b_text,
            "K": k,
            "phase_branch": branch,
            "saddle_a": out(a),
            "saddle_J": out(j),
            "a_sqrt_J": out(length),
            "kappa": out(k / (xi * mp.sqrt(mp.pi * mp.exp(xi)))),
            "conditional_v_mean": out(mean_v),
            "conditional_v_second_moment": out(second_v),
            "gain": out(gain),
            "phase": out(phase),
            "gain_minus_phase": out(gain - phase),
            "separated_gain_ratio": out(2 * a * gain / xi),
            "separated_phase_ratio": out(2 * xi * phase / a),
            "plus_second_moment": out(i2plus / i0plus),
            "scaled_translated_responses": responses,
            "old_saddle_standardized_shift": out(root_j * (a - old_a)),
            "old_saddle_exp2xi_shift": out(mp.exp(2 * xi) * (a - old_a)),
            "old_saddle_rescaled_standard_shift": out(
                root_j * (a - old_a) * mp.exp((2 - gamma / 2) * xi)
            ),
            "old_saddle_rescaled_prediction": out(-mp.sqrt(b / gamma)),
            "asymptotic_a_error": out(
                a - (gamma - 1) * xi - mp.log(b / (mp.pi * gamma))
            )
            if gamma > 1
            else None,
            "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
            "certified": False,
            "bounded_quadrature_not_full_integral_certificate": True,
            "quadrature_coordinate": "sqrt(J)*(d-a)",
            "quadrature_lower": out(lower),
            "quadrature_upper": out(upper),
            "unique_quadrature_nodes": len(cache),
            "theta_largest_n": theta_max,
            "requested_decimal_digits": dps,
            "working_decimal_digits": working_dps,
            "parent_commit": PARENT,
            "parent_scout_sha256_lf": parent_hash,
            "elapsed_seconds": round(time.monotonic() - started, 3),
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xi", type=int, required=True)
    parser.add_argument("--gamma", required=True)
    parser.add_argument("--b", default="1")
    parser.add_argument("--dps", type=int, default=55)
    parser.add_argument("--radius", type=int, default=24)
    args = parser.parse_args()
    result = run_case(args.xi, args.gamma, args.b, args.dps, args.radius)
    result["producer_sha256_lf"] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
