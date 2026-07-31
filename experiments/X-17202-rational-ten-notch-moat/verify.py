#!/usr/bin/env python3
"""Exact checker for the X-17202 rational notch/moat certificate.

The default path uses fractions only.  ``--arb`` additionally reconstructs the
pi enclosure and every zero count with python-flint/Arb.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


def q(value: str | int) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    if "/" in value:
        return Fraction(value)
    return Fraction(Decimal(value))


def decimal_string(value: Fraction, digits: int = 24) -> str:
    getcontext().prec = digits + 20
    out = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{out:.{digits}E}"


def verify_rational(cert: dict[str, Any]) -> dict[str, Any]:
    constants = cert["directed_constants"]
    notches = cert["filter"]["notches"]
    pi_lo = q(constants["pi_lo"])
    pi_hi = q(constants["pi_hi"])
    assert pi_lo < pi_hi
    assert len(notches) == 10

    product_notches = Fraction(1)
    notch_sum = Fraction(0)
    low_bound = Fraction(0)
    attenuations: list[dict[str, str]] = []

    for expected, row in enumerate(notches, start=1):
        assert row["index"] == expected
        assert row["count_lo"] == expected - 1
        assert row["count_hi"] == expected
        lo = q(row["gamma_lo"])
        hi = q(row["gamma_hi"])
        width = q(row["width"])
        assert 0 < lo < hi
        assert width > 0
        x_lo = width * lo / 2
        x_hi = width * hi / 2
        delta = max(
            abs(x_lo - pi_lo),
            abs(x_lo - pi_hi),
            abs(x_hi - pi_lo),
            abs(x_hi - pi_hi),
        )
        amplitude = 2 * delta / (width * lo)
        alpha = amplitude * amplitude
        low_bound += 6 * alpha
        product_notches *= width
        notch_sum += width
        attenuations.append(
            {
                "index": str(expected),
                "delta_upper": decimal_string(delta),
                "alpha_upper": decimal_string(alpha),
            }
        )

    assert notch_sum < Fraction(17, 8)
    tail_start = q(constants["tail_start"])
    assert tail_start == Fraction(529, 10)
    dyadic_widths = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16)]
    all_widths = dyadic_widths + [q(row["width"]) for row in notches]
    assert len(all_widths) == 14
    for width in all_widths:
        assert 2 / (width * tail_start) < 1

    product_all = Fraction(1)
    for width in all_widths:
        product_all *= width
    assert product_all == Fraction(1, 2**10) * product_notches

    xi_upper = q(constants["xi_reciprocal_sum_upper"])
    listed_mass_lower = sum(
        Fraction(2) / (q(row["gamma_hi"]) ** 2 + Fraction(1, 4))
        for row in notches
    )
    xi_tail_upper = xi_upper - listed_mass_lower
    assert xi_tail_upper > 0

    box_count = len(all_widths)
    coefficient = Fraction(3) * Fraction(4) ** box_count / product_all**2
    reciprocal_conversion = 1 + Fraction(1, 4) / tail_start**2
    tail_bound = (
        coefficient
        * tail_start ** (-(2 * box_count - 2))
        * reciprocal_conversion
        * xi_tail_upper
    )
    total_line_bound = low_bound + tail_bound
    line_moat = q(constants["nontrivial_zero_moat"])
    assert total_line_bound < line_moat

    # Exact symbolic support is b = 31/8 + 2*sum(r_j) + log(4).
    # log(4) < 3/2, so b < 77/8.
    support_rational_part = Fraction(31, 8) + 2 * notch_sum
    support_upper = support_rational_part + Fraction(3, 2)
    assert support_upper < Fraction(77, 8)

    # For x >= 28, d=x-b > 147/8.  The elementary bounds e>27/10
    # and e>2 give a rational upper bound for the trivial-zero geometric tail.
    trivial_tail_rational = (
        Fraction(3) * Fraction(10, 27) ** 45 / (1 - Fraction(1, 2) ** 36)
    )
    assert trivial_tail_rational < Fraction(2, 10**19)
    tail_domain_moat = q(constants["tail_domain_raw_moat"])
    assert total_line_bound + trivial_tail_rational < tail_domain_moat

    # Replay the deliberately coarse all-real startup bound.  The standard
    # elementary inequalities 27/10 < e < 3 imply the two exponential/log
    # comparisons below.
    assert 3**9 < 20000
    assert 27**10 > 20000 * 10**10
    assert 4 * 20000 < 284**2
    compact_startup_bound = 6 * 10 * 284
    assert compact_startup_bound == 17040
    all_real_moat = q(constants["all_real_raw_moat"])
    assert compact_startup_bound < all_real_moat

    # From e > 1+1+1/2+1/6+1/24 = 65/24 > 27/10,
    # exp(-5/2) < exp(-2) < 100/729 and 1-exp(-2) > 629/729.
    # Hence 3*exp(-5/2)/(1-exp(-2)) < 300/629 < 1.
    assert Fraction(65, 24) > Fraction(27, 10)
    large_x_trivial_bound = Fraction(300, 629)
    assert large_x_trivial_bound < 1
    assert total_line_bound + large_x_trivial_bound < all_real_moat
    return {
        "classification": "EXACT_RATIONAL_CHECK_PASSED",
        "notch_count": len(notches),
        "box_count_profile": box_count,
        "notch_support_sum": decimal_string(notch_sum),
        "product_all_widths": decimal_string(product_all),
        "low_zero_bound": decimal_string(low_bound),
        "xi_tail_upper": decimal_string(xi_tail_upper),
        "unlisted_zero_bound": decimal_string(tail_bound),
        "total_nontrivial_zero_bound": decimal_string(total_line_bound),
        "declared_nontrivial_zero_moat": decimal_string(line_moat),
        "support_upper_using_log4_lt_3_over_2": decimal_string(support_upper),
        "tail_domain_trivial_bound": decimal_string(trivial_tail_rational),
        "tail_domain_raw_moat": decimal_string(tail_domain_moat),
        "compact_startup_bound": str(compact_startup_bound),
        "large_x_trivial_bound": decimal_string(large_x_trivial_bound),
        "all_real_raw_moat": str(all_real_moat),
        "attenuations": attenuations,
    }


def unique_integer(value: Any) -> int:
    integer = value.unique_fmpz()
    if integer is None:
        raise AssertionError(f"Arb did not isolate an integer: {value}")
    return int(integer)


def verify_arb(cert: dict[str, Any]) -> dict[str, Any]:
    try:
        import flint
        from flint import arb, ctx
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit("--arb requires python-flint on PYTHONPATH") from exc

    constants = cert["directed_constants"]
    ctx.prec = int(cert["backend"]["precision_bits"])
    pi_ball = arb.pi()
    assert arb(constants["pi_lo"]) < pi_ball
    assert pi_ball < arb(constants["pi_hi"])

    checked_counts = []
    for row in cert["filter"]["notches"]:
        count_lo = unique_integer(arb(row["gamma_lo"]).zeta_nzeros())
        count_hi = unique_integer(arb(row["gamma_hi"]).zeta_nzeros())
        assert count_lo == row["count_lo"]
        assert count_hi == row["count_hi"]
        checked_counts.append([count_lo, count_hi])

    count_14 = unique_integer(arb(14).zeta_nzeros())
    count_tail = unique_integer(arb(constants["tail_start"]).zeta_nzeros())
    assert count_14 == constants["zero_count_at_14"]
    assert count_tail == constants["zero_count_at_tail_start"]

    c_xi = arb(2) + arb.const_euler() - (arb(4) * arb.pi()).log()
    assert c_xi < arb(47) / 1000
    d = arb(147) / 8
    trivial = 3 * (-(arb(5) / 2) * d).exp() / (1 - (-2 * d).exp())
    assert trivial < arb(4) / (10**20)
    return {
        "classification": "ARB_CHECK_PASSED",
        "python_flint_version": getattr(flint, "__version__", "unknown"),
        "precision_bits": ctx.prec,
        "count_at_14": count_14,
        "count_at_tail_start": count_tail,
        "interval_count_pairs": checked_counts,
        "pi_ball": str(pi_ball),
        "xi_reciprocal_sum_ball": str(c_xi),
        "tail_domain_trivial_ball": str(trivial),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path(__file__).with_name("certificate.json"),
    )
    parser.add_argument("--arb", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cert = json.loads(args.certificate.read_text(encoding="utf-8"))
    result: dict[str, Any] = {"rational": verify_rational(cert)}
    if args.arb:
        result["arb"] = verify_arb(cert)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
