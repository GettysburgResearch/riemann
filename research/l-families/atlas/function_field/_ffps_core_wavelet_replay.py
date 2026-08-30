"""Finite exact identity and support replays for core wavelets."""

from __future__ import annotations

from fractions import Fraction

from _ffps_core_wavelet_arithmetic import EXCEPTIONAL_PRIME, divisors
from _ffps_core_wavelet_panels import (
    core_assembled_panel,
    core_wavelet,
    direct_primitive_panel,
    product_shell_panel,
    recovered_core,
)


def panel_replay() -> dict[str, object]:
    configurations = (
        (0, 8, 16, 6),
        (1, 66, 134, 6),
        (2, 4488, 5000, 6),
    )
    rows = []
    for alpha, lower, upper, sieve in configurations:
        direct = direct_primitive_panel(alpha, sieve, lower, upper)
        shell = product_shell_panel(alpha, sieve, lower, upper)
        assembled = core_assembled_panel(alpha, sieve, lower, upper)
        if direct != shell or shell != assembled:
            raise ArithmeticError("primitive panel/core-wavelet identity failed")
        inversion_checks = 0
        for core in divisors(sieve):
            if recovered_core(alpha, core, lower, upper) != core_wavelet(
                alpha, core, lower, upper
            ):
                raise ArithmeticError("core-wavelet divisor inversion failed")
            inversion_checks += 1
        rows.append(
            {
                "alpha": alpha,
                "core_inversion_checks": inversion_checks,
                "height_block": [lower, upper],
                "panel_digest": direct.digest(),
                "panel_terms": len(direct.terms),
                "physical_scale": EXCEPTIONAL_PRIME**alpha,
                "sieve": sieve,
            }
        )
    return {
        "full_panel_identity": True,
        "identity": (
            "P_I^alpha(d)=sum_N mu(N)W_I^alpha(N)/sqrt(N) 1_(N,d)=1"
            "=sum_(r|d) Z_I^alpha(r)/sqrt(r)"
        ),
        "inverse": (
            "Z_I^alpha(r)=sqrt(r) sum_(s|r) mu(r/s) P_I^alpha(s)"
        ),
        "rows": rows,
    }


def support_replay() -> dict[str, object]:
    checked_pairs = 0
    shell_checks = 0
    prefix_checks = 0
    for alpha, lower, upper in ((0, 8, 16), (1, 66, 134), (2, 4488, 5000)):
        scale = EXCEPTIONAL_PRIME**alpha
        for left in range(1, upper // scale + 1):
            for right in range(1, upper + 1):
                x = scale * left
                y = right
                product_value = left * right
                ratio_radius = max(Fraction(x, y), Fraction(y, x))
                exact_height_square = max(x, y) ** 2
                balanced_height_square = scale * product_value * ratio_radius
                if Fraction(exact_height_square) != balanced_height_square:
                    raise ArithmeticError("balanced logarithmic height identity failed")
                checked_pairs += 1
                if lower < max(x, y) <= upper and ratio_radius <= 16:
                    if not (
                        Fraction(lower * lower, 16 * scale)
                        < product_value
                        <= Fraction(upper * upper, scale)
                    ):
                        raise ArithmeticError("factor-64 product shell failed")
                    shell_checks += 1
                for threshold in (lower, upper):
                    prefix_left = max(x, y) <= threshold
                    divisor_interval = (
                        Fraction(product_value, threshold)
                        <= left
                        <= Fraction(threshold, scale)
                    )
                    if prefix_left != divisor_interval:
                        raise ArithmeticError("prefix divisor interval failed")
                    prefix_checks += 1
    return {
        "balanced_coordinate_identity": (
            "max(Aa,N/a)^2=A*N*max(A*a^2/N,N/(A*a^2))"
        ),
        "checked_pairs": checked_pairs,
        "factor_64_shell_checks": shell_checks,
        "prefix_divisor_interval_checks": prefix_checks,
    }
