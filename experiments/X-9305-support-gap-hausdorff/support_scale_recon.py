#!/usr/bin/env python3
"""Empirical support-scale scan for L-9307 at the exact PR71 ordinate.

This is discovery arithmetic, not a proof producer.  It evaluates the direct
completed-xi logarithmic modulus far to the right of the critical strip, where
an absolutely convergent Euler product is inexpensive, removes the complete
retained empirical slab-zero list, and scans support-gap chord and first
Hausdorff-localizer rows at exact rational multiples of the certified support
scale A.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import time
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

T = Fraction(20225875608341108140435, 2**32)
SLAB_LOWER = Fraction(75347258181331, 16)
SLAB_UPPER = Fraction(37673629090985, 8)
SUPPORT_GAP = min((T - SLAB_LOWER) ** 2, (SLAB_UPPER - T) ** 2)
ALPHAS = (
    Fraction(1, 8),
    Fraction(3, 16),
    Fraction(1, 4),
    Fraction(3, 8),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(1, 1),
    Fraction(3, 2),
    Fraction(2, 1),
    Fraction(3, 1),
    Fraction(4, 1),
    Fraction(6, 1),
    Fraction(8, 1),
    Fraction(12, 1),
    Fraction(16, 1),
)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [value for value, flag in enumerate(flags) if flag]


def parse_fraction_decimal(text: str) -> Fraction:
    return Fraction(Decimal(text.strip()))


def load_zero_offsets(guide_path: Path, offsets_path: Path | None) -> tuple[list[Fraction], int]:
    getcontext().prec = 100
    guide = [
        parse_fraction_decimal(line)
        for line in guide_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    guide = sorted(value for value in guide if SLAB_LOWER < value < SLAB_UPPER)
    if len(guide) != 172:
        raise ValueError(f"expected 172 guide ordinates in the slab, found {len(guide)}")

    replacement_count = 0
    if offsets_path is not None:
        data = json.loads(offsets_path.read_text(encoding="utf-8"))
        raw_offsets = data.get("nearest_line_zero_signed_offsets")
        if not isinstance(raw_offsets, list):
            raise ValueError("offset JSON has no nearest_line_zero_signed_offsets array")
        for raw in raw_offsets:
            refined = T + parse_fraction_decimal(str(raw))
            index = min(range(len(guide)), key=lambda i: abs(guide[i] - refined))
            guide[index] = refined
            replacement_count += 1
        guide.sort()

    return [value - T for value in guide], replacement_count


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def euler_log_zeta_derivatives(
    s: mp.mpc,
    primes: list[int],
    tolerance: mp.mpf,
) -> tuple[mp.mpc, mp.mpc, mp.mpc, mp.mpf]:
    """Ordinary-precision log zeta and its first two s-derivatives.

    For Re(s)>1,
      log zeta(s) = sum_p sum_{k>=1} p^(-ks)/k.
    The returned tail is a conservative scalar bound for omitted primes, not a
    complete floating-point error bound.
    """

    log_zeta = mp.mpc(0)
    first = mp.mpc(0)
    second = mp.mpc(0)
    sigma = mp.re(s)
    for prime in primes:
        log_prime = mp.log(prime)
        z = mp.exp(-s * log_prime)
        power = z
        exponent = 1
        while True:
            term = power / exponent
            log_zeta += term
            first -= log_prime * power
            second += exponent * log_prime * log_prime * power
            if abs(term) < tolerance:
                break
            exponent += 1
            power *= z
            if exponent > 100:
                raise RuntimeError("Euler factor failed to converge")

    cutoff = mp.mpf(primes[-1])
    omitted_prime_bound = cutoff ** (1 - sigma) / (
        (sigma - 1) * (1 - mp.power(2, -sigma))
    )
    return log_zeta, first, second, omitted_prime_bound


def direct_log_h_and_derivatives(
    u: mp.mpf,
    target: mp.mpf,
    primes: list[int],
    tolerance: mp.mpf,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    x = mp.sqrt(u)
    s = mp.mpc(mp.mpf("0.5") + x, target)
    log_zeta, zeta_first, zeta_second, tail = euler_log_zeta_derivatives(
        s, primes, tolerance
    )

    log_h = 2 * (
        -mp.log(2)
        + mp.log(abs(s))
        + mp.log(abs(s - 1))
        - mp.re(s) * mp.log(mp.pi) / 2
        + mp.re(mp.loggamma(s / 2))
        + mp.re(log_zeta)
    )

    log_xi_first = (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + zeta_first
    )
    log_xi_second = (
        -1 / s**2
        - 1 / (s - 1) ** 2
        + mp.polygamma(1, s / 2) / 4
        + zeta_second
    )
    first_u = mp.re(log_xi_first) / x
    second_u = mp.re(log_xi_second) / (2 * x**2) - mp.re(log_xi_first) / (
        2 * x**3
    )
    return log_h, first_u, second_u, tail


def decimal(value: mp.mpf, digits: int = 50) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", type=Path, required=True)
    parser.add_argument("--offsets-json", type=Path)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--prime-cutoff", type=int, default=10000)
    parser.add_argument(
        "--guide-half-width", default="1/1024",
        help="ordinary first-order perturbation scale for every empirical zero",
    )
    parser.add_argument("--json-out", type=Path, required=True)
    args = parser.parse_args()
    if args.dps < 50 or args.prime_cutoff < 100:
        raise SystemExit("use --dps >= 50 and --prime-cutoff >= 100")

    started = time.time()
    mp.mp.dps = args.dps
    target = mp_fraction(T)
    support_gap = mp_fraction(SUPPORT_GAP)
    zero_offsets_fraction, replacement_count = load_zero_offsets(
        args.guide, args.offsets_json
    )
    zero_offsets = [mp_fraction(value) for value in zero_offsets_fraction]
    primes = sieve_primes(args.prime_cutoff)
    guide_half_width_fraction = Fraction(args.guide_half_width)
    if guide_half_width_fraction < 0:
        raise SystemExit("--guide-half-width must be nonnegative")
    guide_half_width = mp_fraction(guide_half_width_fraction)
    tolerance = mp.power(10, -(args.dps + 10))

    values: list[dict[str, Any]] = []
    residuals: list[mp.mpf] = []
    localizers: list[mp.mpf] = []
    maximum_euler_tail = mp.mpf(0)
    for alpha_fraction in ALPHAS:
        alpha = mp_fraction(alpha_fraction)
        u = alpha * support_gap
        log_h, first_u, second_u, tail = direct_log_h_and_derivatives(
            u, target, primes, tolerance
        )
        residual_log = log_h - mp.fsum(
            mp.log(u + offset * offset) for offset in zero_offsets
        )
        residual_first = first_u - mp.fsum(
            1 / (u + offset * offset) for offset in zero_offsets
        )
        residual_second = second_u + mp.fsum(
            1 / (u + offset * offset) ** 2 for offset in zero_offsets
        )
        localizer = residual_first + (u + support_gap) * residual_second
        maximum_euler_tail = max(maximum_euler_tail, tail)
        residuals.append(residual_log)
        localizers.append(localizer)
        values.append(
            {
                "alpha": fraction_json(alpha_fraction),
                "u_over_A": str(alpha_fraction),
                "u": decimal(u, 60),
                "x": decimal(mp.sqrt(u), 60),
                "sigma": decimal(mp.mpf("0.5") + mp.sqrt(u), 60),
                "residual_log": decimal(residual_log, 60),
                "residual_first": decimal(residual_first, 50),
                "residual_second": decimal(residual_second, 50),
                "first_support_localizer": decimal(localizer, 50),
                "omitted_prime_logzeta_bound": decimal(tail, 12),
            }
        )

    chords: list[dict[str, Any]] = []
    for first, middle, last in itertools.combinations(range(len(ALPHAS)), 3):
        u0 = mp_fraction(ALPHAS[first]) * support_gap
        u1 = mp_fraction(ALPHAS[middle]) * support_gap
        u2 = mp_fraction(ALPHAS[last]) * support_gap
        l1 = mp.log((u1 + support_gap) / (u0 + support_gap))
        l2 = mp.log((u2 + support_gap) / (u0 + support_gap))
        value = l1 * (residuals[last] - residuals[first]) - l2 * (
            residuals[middle] - residuals[first]
        )
        geometry = l1 * l2 * (l2 - l1)
        chords.append(
            {
                "alpha_indices": [first, middle, last],
                "alphas": [str(ALPHAS[index]) for index in (first, middle, last)],
                "value": decimal(value, 50),
                "geometry_normalized_value": decimal(value / geometry, 50),
            }
        )

    chords_by_value = sorted(chords, key=lambda row: mp.mpf(row["value"]))
    chords_by_normalized = sorted(
        chords, key=lambda row: mp.mpf(row["geometry_normalized_value"])
    )
    minimum_chord = chords_by_value[0]
    first, middle, last = minimum_chord["alpha_indices"]
    u0 = mp_fraction(ALPHAS[first]) * support_gap
    u1 = mp_fraction(ALPHAS[middle]) * support_gap
    u2 = mp_fraction(ALPHAS[last]) * support_gap
    l1 = mp.log((u1 + support_gap) / (u0 + support_gap))
    l2 = mp.log((u2 + support_gap) / (u0 + support_gap))

    def zero_chord_derivative(offset: mp.mpf) -> mp.mpf:
        return (
            -l1
            * (
                2 * offset / (u2 + offset * offset)
                - 2 * offset / (u0 + offset * offset)
            )
            + l2
            * (
                2 * offset / (u1 + offset * offset)
                - 2 * offset / (u0 + offset * offset)
            )
        )

    linearized_zero_budget = guide_half_width * mp.fsum(
        abs(zero_chord_derivative(offset)) for offset in zero_offsets
    )
    minimum_chord_value = mp.mpf(minimum_chord["value"])

    localizer_rows = [
        {"alpha": str(alpha), "value": decimal(value, 50)}
        for alpha, value in zip(ALPHAS, localizers)
    ]

    result = {
        "schema": "riemann.x9305-support-scale-reconnaissance.v1",
        "classification": "EMPIRICAL_HIGH_PRECISION_NOT_CERTIFIED",
        "warning": (
            "Ordinary mpmath arithmetic and empirical zero ordinates. The Euler "
            "tail field bounds omitted primes only; it is not a complete rounding "
            "or zero-location error enclosure. No row is a proof certificate."
        ),
        "environment": {
            "python": platform.python_version(),
            "mpmath": mp.__version__,
            "decimal_digits": args.dps,
        },
        "implementation": {
            "script": Path(__file__).name,
            "sha256": sha256_file(Path(__file__)),
            "prime_cutoff": args.prime_cutoff,
            "prime_count": len(primes),
            "euler_factor_tolerance": decimal(tolerance, 12),
        },
        "inputs": {
            "guide_sha256": sha256_file(args.guide),
            "offsets_json_sha256": (
                sha256_file(args.offsets_json) if args.offsets_json else None
            ),
            "empirical_zero_count": len(zero_offsets),
            "refined_replacements": replacement_count,
            "target": fraction_json(T),
            "slab_lower": fraction_json(SLAB_LOWER),
            "slab_upper": fraction_json(SLAB_UPPER),
            "support_gap_A": fraction_json(SUPPORT_GAP),
            "support_gap_decimal": decimal(support_gap, 60),
        },
        "node_count": len(values),
        "chord_row_count": len(chords),
        "values": values,
        "localizers": localizer_rows,
        "minimum_localizer": min(localizer_rows, key=lambda row: mp.mpf(row["value"])),
        "smallest_raw_chords": chords_by_value[:20],
        "smallest_geometry_normalized_chords": chords_by_normalized[:20],
        "minimum_raw_chord": chords_by_value[0],
        "linearized_zero_ordinate_diagnostic": {
            "classification": "FIRST_ORDER_EMPIRICAL_ONLY",
            "assumed_half_width_per_zero": str(guide_half_width_fraction),
            "absolute_budget_on_minimum_raw_chord": decimal(
                linearized_zero_budget, 40
            ),
            "margin_to_linearized_budget_ratio": decimal(
                minimum_chord_value / linearized_zero_budget, 30
            )
            if linearized_zero_budget
            else None,
            "warning": (
                "This is a first-order sensitivity sum at the empirical ordinates, "
                "not an interval enclosure or a proof of the zero locations."
            ),
        },
        "minimum_geometry_normalized_chord": chords_by_normalized[0],
        "maximum_omitted_prime_logzeta_bound": decimal(maximum_euler_tail, 20),
        "all_chords_positive": all(mp.mpf(row["value"]) > 0 for row in chords),
        "all_first_localizers_positive": all(value > 0 for value in localizers),
        "counterexample_candidate": None,
        "elapsed_seconds": time.time() - started,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "minimum_raw_chord": result["minimum_raw_chord"],
        "minimum_geometry_normalized_chord": result["minimum_geometry_normalized_chord"],
        "minimum_localizer": result["minimum_localizer"],
        "all_chords_positive": result["all_chords_positive"],
        "all_first_localizers_positive": result["all_first_localizers_positive"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
