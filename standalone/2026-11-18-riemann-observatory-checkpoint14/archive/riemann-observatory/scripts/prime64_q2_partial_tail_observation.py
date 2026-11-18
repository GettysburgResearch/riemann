#!/usr/bin/env python3
"""Certify finite Q2 partials and evaluate polynomial models, without certifying the infinite tail."""

import argparse
import json
from pathlib import Path
from time import perf_counter

from flint import __FLINT_VERSION__, acb, acb_series, arb, ctx
from prime64_q2_full_polynomial import L, c0, c1, c2, c3, extract, integrated, q
from sympy import Poly


def integer_count(height):
    count = (arb(height) + arb(1) / 1024).zeta_nzeros()
    integer = count.unique_fmpz()
    assert integer is not None and count == arb(integer)
    return int(integer)


def outward_interval(value):
    assert value.is_finite()

    def endpoint(point):
        mantissa, exponent = point.man_exp()
        return [str(mantissa), int(exponent)]

    return {
        "arb_display": value.str(32),
        "dyadic_lower": endpoint(value.lower()),
        "dyadic_upper": endpoint(value.upper()),
    }


def evaluate_poly(poly, logarithm, constants):
    result = arb(0)
    for powers, rational in Poly(poly, L, q, c0, c1, c2, c3).terms():
        numerator, denominator = rational.as_numer_denom()
        coeff = arb(int(numerator)) / int(denominator)
        for base, exponent in zip((logarithm, *constants), powers):
            if exponent:
                coeff *= base ** int(exponent)
        result += coeff
    return result


def run(heights):
    counts = {height: integer_count(height) for height in heights}
    roots = acb.zeta_zeros(1, counts[heights[-1]])
    assert len(roots) == counts[heights[-1]]
    assert roots[0].imag > 0
    assert all(left.imag < right.imag for left, right in zip(roots, roots[1:]))
    for height in heights:
        prefix = counts[height]
        assert roots[prefix - 1].imag < height
        if prefix < len(roots):
            assert roots[prefix].imag > height

    log_two = arb(2).log()
    positive_partial = arb(0)
    certified = {}
    for index, rho in enumerate(roots, start=1):
        assert rho.real == arb(1) / 2
        derivative = acb_series([rho, 1], 2).zeta()[1]
        assert abs(derivative) > 0
        quotient = derivative * (2 * (-rho * log_two).exp() - 1) / rho
        positive_partial += quotient.real*quotient.real + quotient.imag*quotient.imag
        if index in counts.values():
            certified[index] = 2 * positive_partial

    d2, d1 = extract(True), extract(False)
    p2, wrong3 = integrated(d2, 1), 3 * integrated(d1, 1)
    stieltjes = []
    factorial = 1
    for j in range(4):
        if j > 0:
            factorial *= j
        gamma = acb.stieltjes(j)
        assert gamma.imag.contains(0)
        stieltjes.append(((-1)**j) * gamma.real / factorial)
    constants = (log_two, *stieltjes)

    rows = []
    for height, count in counts.items():
        finite = certified[count]
        center = (arb(height) / (2 * arb.pi())).log()
        main = evaluate_poly(p2, center, constants) / (arb.pi() * height)
        false_main = evaluate_poly(wrong3, center, constants) / (arb.pi() * height)
        rows.append({
            "height": height,
            "positive_zero_count": count,
            "finite_C2_partial": outward_interval(finite),
            "tail_quartic_main_only": outward_interval(main),
            "finite_plus_quartic_observation_only": outward_interval(finite + main),
            "false_tail_3_times_untwisted_control": outward_interval(false_main),
            "finite_plus_false_control": outward_interval(finite + false_main),
        })
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-height", choices=(100, 400, 1000, 10000), type=int, default=1000)
    parser.add_argument("--precision", type=int, default=128)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    heights = [height for height in (100, 400, 1000, 10000) if height <= args.max_height]
    started = perf_counter()
    rows = run(heights)
    print(f"Certified finite partials at {heights} in {perf_counter() - started:.2f} s.")
    for row in rows:
        print(row["height"], row["positive_zero_count"], row["finite_C2_partial"]["arb_display"],
              row["finite_plus_quartic_observation_only"]["arb_display"],
              row["finite_plus_false_control"]["arb_display"])
    if args.output:
        data = {
            "flint_version": __FLINT_VERSION__,
            "precision_bits": ctx.prec,
            "scope": "Complete finite critical-line partials. Tail polynomials are evaluated rigorously as polynomials, with no bound on the asymptotic remainder.",
            "zero_count_margin": "height + 2^(-10)",
            "rows": rows,
        }
        temporary = args.output.with_suffix(args.output.suffix + ".tmp")
        temporary.write_text(json.dumps(data, indent=2) + "\n")
        temporary.replace(args.output)
