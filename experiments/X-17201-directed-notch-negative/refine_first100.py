#!/usr/bin/env python3
"""Certified first-100-zero refinement for the retained X-17201 filter.

This is deliberately separate from the FFT producer.  Arb supplies certified
balls for the first 100 zeta zeros and proves that N(237)=100.  Under RH, the
Hadamard identity

    sum_{gamma > 0} 2/(1/4 + gamma**2)
        = 2 + EulerGamma - log(4*pi)

then bounds every unlisted zero without a numerical zero table.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any

from filter_core import FilterSpec, standard_spec


X_TEXT = "18.05113474606469"
FFT_TEXT = "-1.4359116748533417e-14"
ZERO_COUNT = 100
TAIL_START = 237
PRECISION_BITS = 320


def q_decimal(text: str) -> Fraction:
    return Fraction(Decimal(text))


def unique_integer(value: Any) -> int:
    integer = value.unique_fmpz()
    if integer is None:
        raise AssertionError(f"Arb did not isolate an integer: {value}")
    return int(integer)


def run_arb() -> dict[str, Any]:
    try:
        import flint
        from flint import acb, arb, ctx
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit("python-flint is required; put repo/.deps on PYTHONPATH") from exc

    ctx.prec = PRECISION_BITS
    spec = standard_spec(
        dyadic_level=8,
        notch_count=2,
        highpass_order=8,
        highpass_delta=Fraction(1, 128),
    )
    assert isinstance(spec, FilterSpec)
    assert len(spec.widths) == 10

    def qacb(value: Fraction) -> Any:
        return acb(value.numerator) / value.denominator

    def ghat(z: Any) -> Any:
        value = (-qacb(spec.base_shift) * z).exp()
        for width in spec.widths:
            rwz = qacb(width) * z
            box = (1 - (-rwz).exp()) / rwz
            value *= box * box
        h = arb(4).log()
        value *= 1 - 2 * (-h * z).exp()
        hp = (1 - (-qacb(spec.highpass_delta) * z).exp()) / 2
        value *= hp ** spec.highpass_order
        return value

    # Bulk zeta_zeros returns certified balls, indexed with multiplicity.
    zeros = acb.zeta_zeros(1, ZERO_COUNT)
    assert len(zeros) == ZERO_COUNT
    count_at_tail_start = unique_integer(arb(TAIL_START).zeta_nzeros())
    assert count_at_tail_start == ZERO_COUNT

    x = arb(X_TEXT)
    listed_abs = arb(0)
    listed_mass = arb(0)
    spectral = arb(0)
    coefficients = []
    for zero in zeros:
        gamma = zero.imag
        z = acb(0, gamma)
        coefficient = ghat(z)
        listed_abs += 2 * abs(coefficient)
        listed_mass += 2 / (gamma * gamma + arb(1) / 4)
        spectral += -2 * ((z * x).exp() * coefficient).real
        coefficients.append(coefficient)

    # Complete reciprocal mass, and hence the higher-zero mass, under RH.
    xi_mass = arb(2) + arb.const_euler() - (arb(4) * arb.pi()).log()
    reciprocal_tail_mass = xi_mass - listed_mass
    assert reciprocal_tail_mass > 0

    product_widths = Fraction(1)
    for width in spec.widths:
        product_widths *= width
    d = len(spec.widths)
    transform_constant_q = Fraction(3) * Fraction(4) ** d / product_widths**2
    transform_constant = arb(transform_constant_q.numerator) / transform_constant_q.denominator
    t = arb(TAIL_START)
    unlisted_abs = (
        transform_constant
        * t ** (-(2 * d - 2))
        * (1 + 1 / (4 * t * t))
        * reciprocal_tail_mass
    )
    line_envelope = listed_abs + unlisted_abs

    # Tight declared rational ceilings make the certificate easy to audit.
    assert listed_abs < arb(1400) / 10**17       # 1.4000e-14
    assert unlisted_abs < arb(942) / 10**18      # 9.4200e-16
    assert line_envelope < arb(1494) / 10**17    # 1.4940e-14

    # At the reported FFT minimizer, certify the tiny trivial-zero correction.
    # The sign follows the same -sum_z exp((z-1/2)x) Ghat(z-1/2)
    # convention as search.py's nontrivial spectral model.
    trivial = arb(0)
    trivial_terms = 32
    for k in range(1, trivial_terms + 1):
        lam = arb(2 * k) + arb(1) / 2
        trivial += (-(-lam * x).exp() * ghat(acb(-lam))).real

    # For k>K, use |term_k| <= 2^(1-m) W^-2 lambda^-2d
    # exp(-(x-b)lambda), then sum the exponentials geometrically.
    support_max = (
        qacb(spec.base_shift).real
        + 2 * sum((qacb(width).real for width in spec.widths), arb(0))
        + arb(4).log()
        + spec.highpass_order * qacb(spec.highpass_delta).real
    )
    distance = x - support_max
    assert distance > 0
    next_lam = arb(2 * (trivial_terms + 1)) + arb(1) / 2
    trivial_tail_abs = (
        arb(1)
        / (2 ** (spec.highpass_order - 1))
        / (arb(product_widths.numerator) / product_widths.denominator) ** 2
        * next_lam ** (-2 * d)
        * (-distance * next_lam).exp()
        / (1 - (-2 * distance).exp())
    )
    assert trivial_tail_abs < arb(1) / 10**90
    assert abs(trivial) + trivial_tail_abs < arb(3) / 10**30

    fft = arb(FFT_TEXT)
    point_center = spectral + trivial
    point_lower = point_center - unlisted_abs - trivial_tail_abs
    point_upper = point_center + unlisted_abs + trivial_tail_abs
    # The FFT sample lies inside the complete RH-permitted point interval.
    assert point_lower < fft
    assert fft < point_upper

    fft_q = q_decimal(FFT_TEXT)
    declared_line_envelope_q = Fraction(1494, 10**17)
    assert abs(fft_q) < declared_line_envelope_q

    return {
        "classification": "CERTIFIED_ARB_FIRST100_RH_LINE_REFINEMENT",
        "backend": {
            "python_flint_version": getattr(flint, "__version__", "unknown"),
            "precision_bits": ctx.prec,
        },
        "filter": {
            "widths": [f"{w.numerator}/{w.denominator}" for w in spec.widths],
            "profile_box_count": d,
            "product_widths_exact": (
                f"{product_widths.numerator}/{product_widths.denominator}"
            ),
            "transform_tail_constant_exact": (
                f"{transform_constant_q.numerator}/{transform_constant_q.denominator}"
            ),
        },
        "zero_completeness": {
            "listed_positive_zeros": ZERO_COUNT,
            "tail_start": TAIL_START,
            "arb_N_tail_start": count_at_tail_start,
            "first_gamma_ball": str(zeros[0].imag),
            "last_gamma_ball": str(zeros[-1].imag),
        },
        "hadamard_reciprocal_mass": {
            "identity": "2 + EulerGamma - log(4*pi)",
            "complete_mass_ball": str(xi_mass),
            "listed_mass_ball": str(listed_mass),
            "unlisted_mass_ball": str(reciprocal_tail_mass),
        },
        "rh_line_envelope": {
            "listed_first100_abs_sum_ball": str(listed_abs),
            "unlisted_all_higher_zeros_abs_bound_ball": str(unlisted_abs),
            "combined_line_envelope_ball": str(line_envelope),
            "declared_rational_ceiling": "747/50000000000000000",
            "declared_decimal_ceiling": "1.494e-14",
            "scope": "nontrivial-zero line, conditional on RH",
        },
        "point_comparison": {
            "x_exact_decimal": X_TEXT,
            "first100_spectral_value_ball": str(spectral),
            "trivial_first32_value_ball": str(trivial),
            "trivial_after32_abs_bound_ball": str(trivial_tail_abs),
            "complete_RH_point_lower_ball": str(point_lower),
            "complete_RH_point_upper_ball": str(point_upper),
            "fft_value": FFT_TEXT,
            "fft_minus_first100_midpoint_interpretation": (
                "about -6.2461e-16; rigorously covered by the 9.409e-16 "
                "all-higher-zero allowance"
            ),
            "fft_inside_complete_RH_interval": True,
            "fft_abs_below_declared_line_envelope": True,
        },
        "verdict": {
            "exact_support_attempt_warranted": False,
            "reason": (
                "The apparent crossing used a 50-zero truncation.  The certified "
                "first-100 plus complete higher-zero RH envelope exceeds the FFT "
                "magnitude, and the FFT value is inside the rigorous point interval."
            ),
            "noise_diagnosis": (
                "The data do not justify calling the full discrepancy FFT noise: "
                "unlisted genuine zeros can account for it.  It is conclusively not "
                "a certified RH-envelope exceedance."
            ),
        },
        "analytic_dependencies": (
            "Hadamard reciprocal-mass identity and RH; Arb certifies the first 100 "
            "zero balls and N(237)=100.  The Q_G interpretation retains T-15404's "
            "explicit-formula normalization and finite-C18 extension dependencies."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("results") / "refinement-first100-x18p051134746.json",
    )
    args = parser.parse_args()
    result = run_arb()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
