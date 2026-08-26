#!/usr/bin/env python3
"""Exact bounded replay for the common-mother/outer-notch mismatch."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

Quadratic = tuple[Fraction, Fraction]


FROZEN_BLOBS = {
    "L-102500": "db4590fc23b53ed601e108a77e4d064b7d9d13f9",
    "L-102504": "30edf4116f15984c4dfa133d7ff0609388ae2868",
    "L-102701": "70eb455a3b2bb0398f8bba22dee82c39ef803156",
    "L-102740": "ec2f3aafe1b590a11a9967e298f5dfb0e2d59f55",
    "L-106134": "cf40354ff8810a2d4bea9459cf142c300ba36237",
    "T-106150": "ac15f0106a26303f06779feb484a521978fe3ecf",
    "L-102880-explicit-K_L": "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    "L-102885-stable-image": "045481b73474d67ded5bf9633808e8d8d39c4622",
}


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    return left[0] + right[0], left[1] + right[1]


def qsub(left: Quadratic, right: Quadratic) -> Quadratic:
    return left[0] - right[0], left[1] - right[1]


def qscale(scale: Fraction, value: Quadratic) -> Quadratic:
    return scale * value[0], scale * value[1]


def qstr(value: Quadratic) -> str:
    a, b = value
    if b == 0:
        return str(a)
    sign = "+" if b > 0 else "-"
    magnitude = abs(b)
    radical = "sqrt(2)" if magnitude == 1 else f"{magnitude}*sqrt(2)"
    if a == 0:
        return radical if b > 0 else f"-{radical}"
    return f"{a}{sign}{radical}"


def q_power_two_half(half_exponent: int) -> Quadratic:
    """Return 2^(half_exponent/2) in Q(sqrt(2))."""

    if isinstance(half_exponent, bool) or not isinstance(half_exponent, int):
        raise TypeError("half exponent must be an integer")
    if half_exponent % 2 == 0:
        return Fraction(2) ** (half_exponent // 2), Fraction(0)
    return Fraction(0), Fraction(2) ** ((half_exponent - 1) // 2)


def q_at_integer(s: int) -> Quadratic:
    """q(s)=1-sqrt(2)*2^(-s), for positive integral s."""

    if s <= 0:
        raise ValueError("use a positive integral Mellin sample")
    return Fraction(1), -Fraction(1, 2**s)


def r_at_integer(s: int) -> Fraction:
    if s <= 0:
        raise ValueError("use a positive integral Mellin sample")
    return 1 - Fraction(1, 2**s)


def mother_at_integer(s: int) -> Quadratic:
    """The L-102500 multiplier 2*q(s)^2*r(s)^2/[s^2(s-1/2)]."""

    q_value = q_at_integer(s)
    numerator = qscale(2 * r_at_integer(s) ** 2, qmul(q_value, q_value))
    denominator = Fraction(s * s) * (Fraction(s) - Fraction(1, 2))
    return qscale(1 / denominator, numerator)


def l102740_declared_mother_at_integer(s: int) -> Quadratic:
    """The one-q multiplier printed in L-102740."""

    numerator = qscale(2 * r_at_integer(s) ** 2, q_at_integer(s))
    denominator = Fraction(s * s) * (Fraction(s) - Fraction(1, 2))
    return qscale(1 / denominator, numerator)


def mismatch_at_integer(s: int) -> Quadratic:
    return qsub(mother_at_integer(s), l102740_declared_mother_at_integer(s))


def explicit_piecewise_derivative_outer_at_integer(s: int) -> Quadratic:
    """Direct Mellin integral of the three L-102880 piecewise K_L cells."""

    if s <= 0:
        raise ValueError("use a positive integral Mellin sample")
    cells: tuple[tuple[int, int, Quadratic, Quadratic], ...] = (
        (0, 1, (Fraction(8), Fraction(0)), (Fraction(-4), Fraction(0))),
        (1, 2, (Fraction(-8), Fraction(-8)), (Fraction(0), Fraction(4))),
        (2, 3, (Fraction(0), Fraction(8)), (Fraction(-2), Fraction(0))),
    )
    total: Quadratic = (Fraction(0), Fraction(0))
    for left, right, constant, square_root in cells:
        constant_integral = Fraction(
            Fraction(2) ** (-left * s) - Fraction(2) ** (-right * s), s
        )
        root_integral = qscale(
            1 / (Fraction(s) - Fraction(1, 2)),
            qsub(
                q_power_two_half(left * (1 - 2 * s)),
                q_power_two_half(right * (1 - 2 * s)),
            ),
        )
        total = qadd(total, qscale(constant_integral, constant))
        total = qadd(total, qmul(square_root, root_integral))
    return total


def explicit_derivative_outer_closed_at_integer(s: int) -> Quadratic:
    """Closed symbol 4*q*r^2*(s-1)/[s*(s-1/2)]."""

    factor = (
        4
        * r_at_integer(s) ** 2
        * (s - 1)
        / (Fraction(s) * (Fraction(s) - Fraction(1, 2)))
    )
    return qscale(factor, q_at_integer(s))


def explicit_outer_at_integer(s: int) -> Quadratic:
    return qscale(Fraction(1, s), explicit_derivative_outer_closed_at_integer(s))


def l102740_stable_filter_at_integer(s: int) -> Fraction:
    """V(s)=(5s+3/2)/4, the extra stable filter in L-102740."""

    if s <= 0:
        raise ValueError("use a positive integral Mellin sample")
    return (5 * s + Fraction(3, 2)) / 4


def l102740_outer_at_integer(s: int) -> Quadratic:
    """Multiplier of the one-q current constructed in L-102740."""

    differential = Fraction(1, 2) * (s - 1) * (5 * s + Fraction(3, 2))
    return qscale(differential, l102740_declared_mother_at_integer(s))


def common_mother_outer_at_integer(s: int) -> Quadratic:
    """Multiplier of (1/2)(D-1)(5D+3/2) applied to the true mother."""

    differential = Fraction(1, 2) * (s - 1) * (5 * s + Fraction(3, 2))
    return qscale(differential, mother_at_integer(s))


def l102740_derivative_outer_at_integer(s: int) -> Quadratic:
    return qscale(Fraction(s), l102740_outer_at_integer(s))


def d_out_j_at_integer(s: int) -> Quadratic:
    """D_out*J when (2D-1)J is the true common-mother output."""

    mother = mother_at_integer(s)
    j_multiplier = qscale(Fraction(1, 2 * s - 1), mother)
    d_out = Fraction(1, 2) * s * (s - 1) * (5 * s + Fraction(3, 2)) * (2 * s - 1)
    return qscale(d_out, j_multiplier)


def causal_inverse_peak(k: int) -> Quadratic:
    """(sqrt(2))^k as an exact Q(sqrt(2)) pair."""

    if k < 0:
        raise ValueError("use a nonnegative dyadic depth")
    value: Quadratic = (Fraction(1), Fraction(0))
    root_two: Quadratic = (Fraction(0), Fraction(1))
    for _ in range(k):
        value = qmul(value, root_two)
    return value


def causal_inverse_l1_mass(k: int) -> Quadratic:
    """Sum of the positive causal coefficients through dyadic depth k."""

    if k < 0:
        raise ValueError("use a nonnegative dyadic depth")
    total: Quadratic = (Fraction(0), Fraction(0))
    for depth in range(k + 1):
        total = qadd(total, causal_inverse_peak(depth))
    return total


def anti_causal_inverse_magnitude(k: int) -> Quadratic:
    """Magnitude (sqrt(2))^(-k) of the k-th future coefficient."""

    if k < 1:
        raise ValueError("use a positive future depth")
    value: Quadratic = (Fraction(1), Fraction(0))
    inverse_root_two: Quadratic = (Fraction(0), Fraction(1, 2))
    for _ in range(k):
        value = qmul(value, inverse_root_two)
    return value


def anti_causal_inverse_l1_mass(k: int) -> Quadratic:
    """Sum of future coefficient magnitudes through depth k."""

    if k < 1:
        raise ValueError("use a positive future depth")
    total: Quadratic = (Fraction(0), Fraction(0))
    for depth in range(1, k + 1):
        total = qadd(total, anti_causal_inverse_magnitude(depth))
    return total


def anti_causal_truncation_product(k: int) -> dict[int, Quadratic]:
    """Multiply Q by the first k anti-causal inverse terms.

    Shift exponent ``1`` denotes ``S_2``.  The exact result is
    ``1-(sqrt(2))^(-k) S_2^(-k)``.
    """

    if k < 1:
        raise ValueError("use a positive future depth")
    q_operator: dict[int, Quadratic] = {
        0: (Fraction(1), Fraction(0)),
        1: (Fraction(0), Fraction(-1)),
    }
    truncated_inverse = {
        -depth: qscale(-1, anti_causal_inverse_magnitude(depth))
        for depth in range(1, k + 1)
    }
    product: dict[int, Quadratic] = {}
    for left_shift, left_value in q_operator.items():
        for right_shift, right_value in truncated_inverse.items():
            shift = left_shift + right_shift
            product[shift] = qadd(
                product.get(shift, (Fraction(0), Fraction(0))),
                qmul(left_value, right_value),
            )
    return {shift: value for shift, value in product.items() if value != (0, 0)}


def run() -> dict[str, object]:
    samples = []
    for s in (1, 2, 3, 5):
        mother = mother_at_integer(s)
        printed = l102740_declared_mother_at_integer(s)
        mismatch = mismatch_at_integer(s)
        if mismatch == (Fraction(0), Fraction(0)):
            raise AssertionError("the frozen multipliers unexpectedly agree")
        if mother != qmul(q_at_integer(s), printed):
            raise AssertionError("corrected extra-notch identity failed")
        explicit_direct = explicit_piecewise_derivative_outer_at_integer(s)
        explicit_closed = explicit_derivative_outer_closed_at_integer(s)
        if explicit_direct != explicit_closed:
            raise AssertionError("piecewise L-102880 Mellin integral failed")
        stable_filter = l102740_stable_filter_at_integer(s)
        l102740_outer = l102740_outer_at_integer(s)
        l102740_derivative = l102740_derivative_outer_at_integer(s)
        if l102740_derivative != qscale(stable_filter, explicit_closed):
            raise AssertionError("L-102740 versus explicit K_L filter failed")
        common_outer = common_mother_outer_at_integer(s)
        if common_outer != qmul(q_at_integer(s), l102740_outer):
            raise AssertionError("corrected Q*L_102740 orientation failed")
        d_out_j = d_out_j_at_integer(s)
        if d_out_j != qscale(Fraction(s), common_outer):
            raise AssertionError("D_out*J identity failed")
        if d_out_j != qmul(q_at_integer(s), l102740_derivative):
            raise AssertionError("corrected Q*D(L_102740) orientation failed")
        if d_out_j != qmul(q_at_integer(s), qscale(stable_filter, explicit_closed)):
            raise AssertionError("three-way explicit/common identity failed")
        samples.append(
            {
                "s": s,
                "q": qstr(q_at_integer(s)),
                "L102500_mother": qstr(mother),
                "L102740_printed_mother": qstr(printed),
                "difference": qstr(mismatch),
                "ratio": "q(s)",
                "explicit_piecewise_K_L": qstr(explicit_closed),
                "L102740_stable_filter_V": str(stable_filter),
                "L102740_constructed_D_L": qstr(l102740_derivative),
                "common_mother_differential": qstr(common_outer),
                "D_out_J": qstr(d_out_j),
                "operator_orientation": ("D_out*J=Q*D(L_102740)=Q*V*K_L_explicit"),
            }
        )
    inverse_panels = []
    for k in (0, 1, 2, 4, 8, 16):
        value = causal_inverse_peak(k)
        squared_size = value[0] ** 2 + 2 * value[1] ** 2
        if squared_size != 2**k:
            raise AssertionError("causal inverse growth ledger failed")
        inverse_panels.append(
            {
                "dyadic_depth": k,
                "coefficient": qstr(value),
                "coefficient_squared": str(squared_size),
                "physical_scale": str(2**k),
                "positive_l1_mass_through_depth": qstr(causal_inverse_l1_mass(k)),
            }
        )
    anti_causal_panels = []
    for k in (1, 2, 4, 8, 16):
        coefficient = anti_causal_inverse_magnitude(k)
        squared_size = coefficient[0] ** 2 + 2 * coefficient[1] ** 2
        if squared_size != Fraction(1, 2**k):
            raise AssertionError("anti-causal inverse decay ledger failed")
        expected_product = {
            0: (Fraction(1), Fraction(0)),
            -k: qscale(-1, coefficient),
        }
        if anti_causal_truncation_product(k) != expected_product:
            raise AssertionError("anti-causal inverse orientation failed")
        anti_causal_panels.append(
            {
                "future_depth": k,
                "coefficient_magnitude": qstr(coefficient),
                "coefficient_squared": str(squared_size),
                "positive_l1_mass_through_depth": qstr(anti_causal_inverse_l1_mass(k)),
            }
        )
    return {
        "frozen_head": "98af0db6",
        "frozen_parent_head": "ec6635b4",
        "frozen_blobs": FROZEN_BLOBS,
        "notation": {
            "q(s)": "1-sqrt(2)*2^(-s)",
            "r(s)": "1-2^(-s)",
        },
        "conflict": {
            "L102500_and_L102701": "m_Phi=2*q(s)^2*r(s)^2/[s^2*(s-1/2)]",
            "L102740_printed": "m_Phi=2*q(s)*r(s)^2/[s^2*(s-1/2)]",
            "missing_factor": "q(s)",
            "explicit_L102880_K_L": ("4*q(s)*r(s)^2*(s-1)/[s*(s-1/2)]"),
            "L102740_constructed_D_L": ("q(s)*r(s)^2*(s-1)*(5s+3/2)/[s*(s-1/2)]"),
            "common_mother_D_out_J": ("q(s)^2*r(s)^2*(s-1)*(5s+3/2)/[s*(s-1/2)]"),
        },
        "corrected_adapter": {
            "operator": "Q=I-sqrt(2)*S_2",
            "stable_filter": "V=(5*D+3/2)/4=(5/4)*(D+3/10)",
            "stable_filter_positive_inverse_l1_norm": "8/3",
            "explicit_outer_relation": "L_102740=V*R_L_explicit",
            "identity": ("Q*L_sigma=(1/2)*(D-1)*(5*D+3/2)*H_sigma"),
            "derivative_identity": ("D_out*J=Q*D(L_102740)=Q*V*K_L_explicit"),
            "not_proved": "L_sigma=(1/2)*(D-1)*(5*D+3/2)*H_sigma",
        },
        "exact_samples": samples,
        "causal_inverse": {
            "formal_series": "Q^(-1)=sum_(k>=0) (sqrt(2)*S_2)^k",
            "loss_at_scale_2^k": "(sqrt(2))^k=(2^k)^(1/2)",
            "one_sided_transfer": (
                "positive causal inverse exists, but its horizon norm has "
                "square-root power growth"
            ),
            "subpower_transfer_from_naive_coefficientwise_causal_inverse": False,
            "panels": inverse_panels,
        },
        "anti_causal_inverse": {
            "compact_support_series": ("f=-sum_(j>=1) 2^(-j/2)*S_2^(-j)g for g=Qf"),
            "global_l1_norm": "1+sqrt(2)",
            "zero_mass_one_sided_transfer": (
                "for compact zero-total-mass currents, global negative mass "
                "transfers at factor at most 1+sqrt(2)"
            ),
            "native_prefix_firewall": (
                "uses future/global values; terminal-source/horizon "
                "compatibility is not proved"
            ),
            "panels": anti_causal_panels,
        },
        "impact": {
            "retained": (
                "the exact common-mother self-convolution and its zero-safe "
                "Mellin-Landau detector"
            ),
            "invalid_as_written": (
                "the identification of that self-convolution differential "
                "with either the L-102740 current or explicit L-102880 K_L"
            ),
            "corrected_L106134_labels": (
                "the polynomial right sides of .13-.14 are Q*V*R_L_explicit "
                "and Q*V*K_L_explicit"
            ),
            "corrected_T106150_line": (
                "Q*V*H_K_live=D_out*J plus a Q*V-filtered closed remainder"
            ),
            "required_repair": (
                "prove EXTSRC for the complete source, or prove terminal-safe "
                "anti-causal Q removal; V has a fixed positive stable inverse"
            ),
        },
        "resource_caps": {
            "mellin_samples": len(samples),
            "piecewise_cells_integrated": 3,
            "maximum_dyadic_depth": 16,
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
