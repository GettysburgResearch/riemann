#!/usr/bin/env python3
"""Bounded replay for Chebyshev max-cusp refill compensation."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_chebyshev_max_cusp_compensation.json"

SOURCE_COMMIT = "f3ae060d1bba0a7855e09d88b856baf991fc844a"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CHEBYSHEV_STEP_AUTOCORRELATION_NORMAL_FORM.md": "85a009d5f82201158fc6795ba7354122997b5768",
    "research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.py": "79792cb7b7a33a37287db63ded9f28e67649d8b6",
    "research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.json": "ade0f2905908c7dd16d233cd38646307bca5d87f",
    "tests/test_ffps_chebyshev_step_autocorrelation_normal_form.py": "1b2dd31d720c077992fca5ee59d1b94ee2cce5af",
}

MAX_CELL_ORDER = 8
MAX_TABLE_ORDER = 16
PROFILE_SIMPSON_PANELS = 4096
LINEAR_SCALE_REPLAY_ORDER = 127


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_order(order: int) -> None:
    if order < 1:
        raise ValueError("order must be at least one")


def cell_boundaries(order: int) -> tuple[float, ...]:
    validate_order(order)
    degree = order + 1
    return tuple(
        (1 - math.cos(index * math.pi / degree)) / 2 for index in range(degree + 1)
    )


def primitive_energy_ratio(order: int) -> float:
    """||F_r||_2^2/h_r^2 in closed trigonometric form."""
    validate_order(order)
    tangent_squared = math.tan(math.pi / (2 * (order + 1))) ** 2
    return tangent_squared / (6 * (3 - tangent_squared))


def primitive_energy_ratio_cosine(order: int) -> float:
    validate_order(order)
    cosine = math.cos(math.pi / (order + 1))
    return (1 - cosine) / (12 * (1 + 2 * cosine))


def primitive_l1_ratio(order: int) -> float:
    """||F_r||_1/|h_r| in closed form."""
    validate_order(order)
    tangent_squared = math.tan(math.pi / (2 * (order + 1))) ** 2
    return (order + 1) * tangent_squared / 8


def relative_remainder_coefficient(order: int) -> float:
    """lambda_r^2/(4*kappa_r) in the tilted zero-mode bound."""
    validate_order(order)
    return primitive_l1_ratio(order) ** 2 / (4 * primitive_energy_ratio(order))


def sharp_relative_remainder_constant() -> Fraction:
    """Sharp all-order coefficient in the exact L1/Young envelope."""
    return Fraction(3, 16)


def jump_data(order: int) -> tuple[tuple[float, float], ...]:
    """Unit-height atoms (location, signed mass) of the zero-extended step."""
    boundaries = cell_boundaries(order)
    return tuple(
        (
            location,
            float(((-1) ** index) * (1 if index in (0, order + 1) else 2)),
        )
        for index, location in enumerate(boundaries)
    )


def tilted_zero_mode_by_jumps(order: int, z: float) -> float:
    """J_r(z)/h_r^2 from the exact finite jump Green kernel."""
    validate_order(order)
    if z <= 0:
        raise ValueError("z must be positive")
    a = z / 2
    atoms = jump_data(order)

    def green(distance: float) -> float:
        return (-math.expm1(-a * distance) - a * distance) / a**2

    return sum(
        left_mass * right_mass * green(abs(left - right))
        for left, left_mass in atoms
        for right, right_mass in atoms
    )


def tilted_zero_mode_by_jumps_complex(order: int, z: complex) -> complex:
    """Analytic finite-jump transform in the closed right half-plane."""
    validate_order(order)
    if z == 0 or z.real < 0:
        raise ValueError("z must be nonzero with nonnegative real part")
    a = z / 2
    atoms = jump_data(order)
    return sum(
        left_mass
        * right_mass
        * (1 - cmath.exp(-a * abs(left - right)) - a * abs(left - right))
        / a**2
        for left, left_mass in atoms
        for right, right_mass in atoms
    )


def tilted_zero_mode_by_cells(order: int, z: float) -> float:
    """Independent analytic cell-pair integration of J_r(z)/h_r^2."""
    validate_order(order)
    if z <= 0:
        raise ValueError("z must be positive")
    a = z / 2
    boundaries = cell_boundaries(order)
    total = 0.0
    for left_cell in range(order + 1):
        left_start = boundaries[left_cell]
        left_end = boundaries[left_cell + 1]
        left_width = left_end - left_start
        left_sign = (-1) ** left_cell
        diagonal = 2 * (a * left_width + math.expm1(-a * left_width)) / a**2
        total += diagonal
        for right_cell in range(left_cell + 1, order + 1):
            right_start = boundaries[right_cell]
            right_end = boundaries[right_cell + 1]
            right_width = right_end - right_start
            right_sign = (-1) ** right_cell
            cross = (
                math.exp(-a * (right_start - left_end))
                * (-math.expm1(-a * left_width))
                * (-math.expm1(-a * right_width))
                / a**2
            )
            total += 2 * left_sign * right_sign * cross
    return total


def normalized_stieltjes_ratio(order: int, z: float) -> float:
    """J_r(z)/(z h_r^2), strictly decreasing for positive z."""
    return tilted_zero_mode_by_jumps(order, z) / z


def primitive_cell_polynomials(
    order: int, depth: int
) -> tuple[tuple[tuple[float, ...], ...], ...]:
    """Local-power coefficients of the first requested causal primitives."""
    validate_order(order)
    if depth < 1 or depth > order:
        raise ValueError("depth must lie between one and the information order")
    boundaries = cell_boundaries(order)
    layer = tuple((float((-1) ** cell),) for cell in range(order + 1))
    layers = []
    for _ in range(depth):
        integrated = []
        cumulative = 0.0
        for cell, coefficients in enumerate(layer):
            current = (cumulative,) + tuple(
                coefficient / (power + 1)
                for power, coefficient in enumerate(coefficients)
            )
            integrated.append(current)
            width = boundaries[cell + 1] - boundaries[cell]
            cumulative = sum(
                coefficient * width**power for power, coefficient in enumerate(current)
            )
        if abs(cumulative) > 2e-12:
            raise AssertionError("causal primitive did not close")
        layer = tuple(integrated)
        layers.append(layer)
    return tuple(layers)


def integrate_cell_polynomials(
    order: int, polynomials: tuple[tuple[float, ...], ...]
) -> float:
    boundaries = cell_boundaries(order)
    return sum(
        coefficient
        * (boundaries[cell + 1] - boundaries[cell]) ** (power + 1)
        / (power + 1)
        for cell, coefficients in enumerate(polynomials)
        for power, coefficient in enumerate(coefficients)
    )


def primitive_norm_ratio(order: int, depth: int) -> float:
    """||P_depth||_2^2/h_r^2 by exact polynomial cell integration."""
    polynomials = primitive_cell_polynomials(order, depth)[-1]
    boundaries = cell_boundaries(order)
    total = 0.0
    for cell, coefficients in enumerate(polynomials):
        width = boundaries[cell + 1] - boundaries[cell]
        total += sum(
            left
            * right
            * width ** (left_power + right_power + 1)
            / (left_power + right_power + 1)
            for left_power, left in enumerate(coefficients)
            for right_power, right in enumerate(coefficients)
        )
    return total


def primitive_mass_ratio(order: int, depth: int) -> float:
    """Integral P_depth/h_r, in particular b/h_r at depth r."""
    polynomials = primitive_cell_polynomials(order, depth)[-1]
    return integrate_cell_polynomials(order, polynomials)


def second_primitive_energy_ratio(order: int) -> float:
    """||P_2||_2^2/||P_1||_2^2 for the unit-height Chebyshev step."""
    if order < 2:
        raise ValueError("order must be at least two")
    return primitive_norm_ratio(order, 2) / primitive_norm_ratio(order, 1)


def second_primitive_norm_ratio_closed(order: int) -> float:
    """Exact ||P_2||_2^2/h_r^2 in the Chebyshev family."""
    if order < 2:
        raise ValueError("order must be at least two")
    v = math.sin(math.pi / (2 * (order + 1))) ** 2
    return v**2 * (8 - 9 * v) / (120 * (3 - 4 * v) * (16 * v**2 - 20 * v + 5))


def second_primitive_energy_ratio_closed(order: int) -> float:
    """Exact ||P_2||_2^2/||P_1||_2^2 in the Chebyshev family."""
    if order < 2:
        raise ValueError("order must be at least two")
    v = math.sin(math.pi / (2 * (order + 1))) ** 2
    return v * (8 - 9 * v) / (20 * (16 * v**2 - 20 * v + 5))


def second_primitive_scaled_limit() -> float:
    return math.pi**2 / 50


def relative_fixed_tilt_refill(order: int, z: float) -> float:
    """J_r(z)/(z*h_r^2*kappa_r)."""
    return normalized_stieltjes_ratio(order, z) / primitive_energy_ratio(order)


def linear_scale_profile(c: float, panels: int = PROFILE_SIMPSON_PANELS) -> float:
    """The real-positive z/(r+1)->c refill profile by bounded Simpson replay."""
    if c < 0:
        raise ValueError("c must be nonnegative")
    if panels < 2 or panels % 2:
        raise ValueError("panels must be a positive even integer")
    if c == 0:
        return 1.0
    step = math.pi / panels
    scale = c * math.pi / 8

    def residual(theta: float) -> float:
        x = scale * math.sin(theta)
        if abs(x) < 0.01:
            x_squared = x * x
            return x**3 * (
                Fraction(1, 3)
                + x_squared
                * (
                    -Fraction(2, 15)
                    + x_squared * (Fraction(17, 315) - Fraction(62, 2835) * x_squared)
                )
            )
        return x - math.tanh(x)

    terms = [0.0]
    terms.extend(
        (4 if index % 2 else 2) * residual(index * step) for index in range(1, panels)
    )
    terms.append(0.0)
    integral = step * math.fsum(terms) / 3
    return 1152 * integral / (math.pi**3 * c**3)


def linear_scale_profile_complex(
    c: complex, panels: int = PROFILE_SIMPSON_PANELS
) -> complex:
    """Analytic profile replay for a nonzero right-half-plane scale."""
    if c == 0 or c.real <= 0:
        raise ValueError("c must lie in the open right half-plane")
    if panels < 2 or panels % 2:
        raise ValueError("panels must be a positive even integer")
    step = math.pi / panels
    scale = c * math.pi / 8

    def residual(theta: float) -> complex:
        x = scale * math.sin(theta)
        if abs(x) < 0.01:
            x_squared = x * x
            return x**3 * (
                Fraction(1, 3)
                + x_squared
                * (
                    -Fraction(2, 15)
                    + x_squared * (Fraction(17, 315) - Fraction(62, 2835) * x_squared)
                )
            )
        return x - cmath.tanh(x)

    terms = [0j]
    terms.extend(
        (4 if index % 2 else 2) * residual(index * step) for index in range(1, panels)
    )
    terms.append(0j)
    integral = (
        step
        * complex(
            math.fsum(term.real for term in terms),
            math.fsum(term.imag for term in terms),
        )
        / 3
    )
    return 1152 * integral / (math.pi**3 * c**3)


def linear_scale_replay(order: int, c: float) -> float:
    """Finite-order cell replay at z=c(r+1)."""
    validate_order(order)
    if c <= 0:
        raise ValueError("c must be positive")
    z = c * (order + 1)
    return tilted_zero_mode_by_cells(order, z) / (z * primitive_energy_ratio(order))


def linear_scale_replay_complex(order: int, c: complex) -> complex:
    """Finite-order jump replay at a right-half-plane scale z=c(r+1)."""
    validate_order(order)
    if c.real <= 0:
        raise ValueError("c must lie in the open right half-plane")
    z = c * (order + 1)
    return tilted_zero_mode_by_jumps_complex(order, z) / (
        z * primitive_energy_ratio(order)
    )


def stieltjes_partial_sum(order: int, z: float, depth: int) -> float:
    """Alternating depth-M primitive truncation for J_r(z)/(z h_r^2)."""
    validate_order(order)
    if z <= 0:
        raise ValueError("z must be positive")
    if depth < 1 or depth > order:
        raise ValueError("depth must lie between one and the information order")
    q = z**2 / 4
    return sum(
        (-q) ** (level - 1) * primitive_norm_ratio(order, level)
        for level in range(1, depth + 1)
    )


def primitive_energy_ratio_by_cells(order: int) -> float:
    """Independent exact-cell integration, with unit signed height."""
    validate_order(order)
    boundaries = cell_boundaries(order)
    cumulative = 0.0
    total = 0.0
    for cell in range(order + 1):
        width = boundaries[cell + 1] - boundaries[cell]
        slope = (-1) ** cell
        total += cumulative**2 * width
        total += cumulative * slope * width**2
        total += width**3 / 3
        cumulative += slope * width
    if abs(cumulative) > 2e-14:
        raise AssertionError("mean-zero primitive did not close")
    return total


def order_constant(order: int) -> Fraction:
    validate_order(order)
    return Fraction(
        16**order * (2 * order + 3) ** 2,
        (2 * order + 1) * math.comb(2 * order, order) ** 2,
    )


def compensation_product(order: int) -> float:
    return float(order_constant(order)) * primitive_energy_ratio(order)


def compensation_ratio_upper_bound(order: int) -> Fraction:
    """Strict rational upper bound for P_(r+1)/P_r."""
    validate_order(order)
    return Fraction(
        4 * (order + 1) ** 4 * (2 * order + 5) ** 2,
        (order + 2) ** 2 * (2 * order + 1) * (2 * order + 3) ** 3,
    )


def compensation_ratio_gap_numerator(order: int) -> int:
    validate_order(order)
    return 12 * order**4 + 60 * order**3 + 99 * order**2 + 60 * order + 8


def refill_limit() -> float:
    return math.pi**3 / 36


def safe_factor(order: int, width: float, log_x: float) -> float:
    validate_order(order)
    if width <= 0 or log_x < 0:
        raise ValueError("width must be positive and log_x nonnegative")
    return float(order_constant(order)) * (1 + log_x / width) ** (2 * order + 2)


def per_unit_tilt_coefficient(order: int, width: float, z: float) -> float:
    """J_(r,W)(z)/(z W^2 E_(r,W)) by exact dilation."""
    validate_order(order)
    if width <= 0 or z <= 0:
        raise ValueError("width and z must be positive")
    return normalized_stieltjes_ratio(order, z * width)


def cost_charged_refill(order: int, width: float, log_x: float, z: float) -> float:
    return safe_factor(order, width, log_x) * per_unit_tilt_coefficient(order, width, z)


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    for order in range(1, MAX_CELL_ORDER + 1):
        closed = primitive_energy_ratio(order)
        if abs(closed - primitive_energy_ratio_cosine(order)) > 2e-14:
            raise AssertionError("primitive energy trigonometric forms disagree")
        if abs(closed - primitive_energy_ratio_by_cells(order)) > 2e-14:
            raise AssertionError("primitive energy formula failed")
        if abs(closed - primitive_norm_ratio(order, 1)) > 2e-14:
            raise AssertionError("first causal primitive norm failed")
        expected_mass = 1 / (math.factorial(order) * 4**order)
        if abs(primitive_mass_ratio(order, order) - expected_mass) > 2e-14:
            raise AssertionError("terminal primitive sensitivity failed")
        if order >= 2:
            second_by_cells = second_primitive_energy_ratio(order)
            second_closed = second_primitive_energy_ratio_closed(order)
            if abs(second_by_cells - second_closed) > 2e-14:
                raise AssertionError("exact second-primitive formula failed")
            if (
                abs(
                    second_primitive_norm_ratio_closed(order)
                    - primitive_norm_ratio(order, 2)
                )
                > 2e-14
            ):
                raise AssertionError("exact second-primitive norm failed")
            if second_closed * (order + 1) ** 2 >= 1:
                raise AssertionError("all-order second-primitive bound failed")
        if compensation_ratio_upper_bound(order) >= 1:
            raise AssertionError("compensation descent certificate failed")
        if (
            relative_remainder_coefficient(order)
            > float(sharp_relative_remainder_constant()) + 2e-14
        ):
            raise AssertionError("uniform remainder certificate failed")
        for z in (0.25, 1.0, 4.0):
            by_jumps = tilted_zero_mode_by_jumps(order, z)
            by_cells = tilted_zero_mode_by_cells(order, z)
            if abs(by_jumps - by_cells) > 2e-12:
                raise AssertionError("finite tilted formulas disagree")
            if not 0 < by_jumps < z * closed:
                raise AssertionError("global Stieltjes bounds failed")
        exact_stieltjes = normalized_stieltjes_ratio(order, 2)
        for depth in range(1, min(order, 4) + 1):
            signed_error = (-1) ** depth * (
                exact_stieltjes - stieltjes_partial_sum(order, 2, depth)
            )
            if signed_error <= 0:
                raise AssertionError("alternating primitive hierarchy failed")
        complex_z = complex(0.5, 1)
        complex_value = tilted_zero_mode_by_jumps_complex(order, complex_z)
        complex_error = abs(complex_value - complex_z * closed)
        complex_bound = (
            float(sharp_relative_remainder_constant()) * abs(complex_z) ** 2 * closed
        )
        if complex_error > complex_bound + 2e-12 or complex_value == 0:
            raise AssertionError("complex half-disk certificate failed")

    for c in (0.5, 1.0, 2.0, 5.0):
        profile = linear_scale_profile(c)
        if not 0 < profile < 1:
            raise AssertionError("linear-scale profile escaped the unit interval")
    for c in (1.0, 2.0):
        if (
            abs(
                linear_scale_replay(LINEAR_SCALE_REPLAY_ORDER, c)
                - linear_scale_profile(c)
            )
            > 6e-5
        ):
            raise AssertionError("linear-scale finite replay failed")
    complex_c = complex(1, 0.5)
    complex_profile = linear_scale_profile_complex(complex_c)
    if complex_profile.real <= 0:
        raise AssertionError("acute-sector profile lost its positive real part")
    if (
        abs(
            linear_scale_replay_complex(LINEAR_SCALE_REPLAY_ORDER, complex_c)
            - complex_profile
        )
        > 3e-5
    ):
        raise AssertionError("complex linear-scale finite replay failed")

    rows = []
    for order in range(1, MAX_TABLE_ORDER + 1):
        coefficient = primitive_energy_ratio(order)
        product = compensation_product(order)
        rows.append(
            {
                "information_order": order,
                "normalized_refill_coefficient": f"{coefficient:.15f}",
                "scaled_refill_72_rplus1_squared_over_pi2": f"{coefficient * 72 * (order + 1) ** 2 / math.pi**2:.15f}",
                "safe_factor_order_constant": (
                    str(order_constant(order).numerator)
                    if order_constant(order).denominator == 1
                    else f"{order_constant(order).numerator}/{order_constant(order).denominator}"
                ),
                "compensation_product": f"{product:.15f}",
                "product_over_pi3_over_36": f"{product / refill_limit():.15f}",
                "young_relative_coefficient": (
                    f"{relative_remainder_coefficient(order):.15f}"
                ),
                "stieltjes_ratio_at_z1": (
                    f"{normalized_stieltjes_ratio(order, 1):.15f}"
                ),
            }
        )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "max_cusp_compensation": {
            "primitive_energy": "||F_r||_2^2/h_r^2=tan(a)^2/(6*(3-tan(a)^2))=(1-cos(pi/(r+1)))/(12*(1+2*cos(pi/(r+1)))), a=pi/(2(r+1))",
            "absolute_lag_identity": "integral |s| R_r(s) ds=-2||F_r||_2^2",
            "tilted_zero_mode": "integral R_r(s)*exp(-z|s|/2) ds=z||F_r||_2^2+O(z^2)",
            "global_stieltjes_law": "J_K(z)/z=(2*pi)^-1*integral |Khat(xi)|^2/((z/2)^2+xi^2) dxi; as a function of (z/2)^2 this is strictly completely monotone",
            "global_real_tilt_bounds": "for every z>0, 0<J_r(z)<z||F_r||_2^2 and z*J_r(z)->4||K_r||_2^2",
            "finite_jump_formula": "J_r(z)=sum_jk mu_j*mu_k*(1-exp(-a*d_jk)-a*d_jk)/a^2, a=z/2",
            "iterated_primitive_hierarchy": "G_K(q)=sum_(m=1)^M (-q)^(m-1)||P_m||_2^2+(-q)^M G_(P_M)(q), so every truncation has the exact alternating error sign",
            "terminal_cusp_expansion": "J_K(z)=z*sum_(m=1)^r(-z^2/4)^(m-1)||P_m||_2^2+(-1)^r*b^2*(z^2/4)^r+O(z^(2r+1))",
            "second_primitive_exact_norm": "with v=sin(pi/(2*(r+1)))^2, ||P_2||_2^2/h_r^2=v^2*(8-9v)/(120*(3-4v)*(16v^2-20v+5))",
            "second_primitive_exact_ratio": "with v=sin(pi/(2*(r+1)))^2, ||P_2||_2^2/||P_1||_2^2=v*(8-9v)/(20*(16v^2-20v+5))",
            "second_primitive_asymptotic": "||P_2||_2^2/||P_1||_2^2=pi^2/(50*n^2)+61*pi^4/(4800*n^4)+1157*pi^6/(144000*n^6)+O(n^-8), n=r+1",
            "second_primitive_all_order_bound": "0<||P_2||_2^2/||P_1||_2^2<1/(r+1)^2 for every r>=2",
            "sublinear_tilt_limit": "uniformly for positive z_r=o(r), J_r(z_r)/(z_r*h_r^2*kappa_r)->1 and A_r*J_r(z_r)/(z_r*h_r^2)->pi^3/36",
            "linear_scale_tilt_profile": "if z_r/(r+1)->c in (0,infinity), J_r(z_r)/(z_r*h_r^2*kappa_r)->Phi(c)=288/(pi^2*c^3)*(c-(4/pi)*integral_0^pi tanh(c*pi*sin(theta)/8)dtheta), with 0<Phi(c)<1",
            "linear_scale_small_c": "Phi(c)=1-pi^2*c^2/200+17*pi^4*c^4/627200+O(c^6)",
            "superlinear_tilt_collapse": "if z_r/(r+1)->infinity, J_r(z_r)/(z_r*h_r^2*kappa_r)->0",
            "cost_charged_phase_diagram": "for n=r+1->infinity and positive real tilt, if z_r*W_r/n->c in [0,infinity) and n*log(1+log(X)/W_r)->tau in [0,infinity), then G*L->(pi^3/36)*exp(2*tau)*Phi(c), with Phi(0)=1",
            "complex_linear_scale_profile": "the same Phi(c) limit holds locally uniformly on compact subsets of Re(c)>0",
            "profile_stieltjes_representation": "Phi(c)=72/pi^4*sum_(k>=0)(2k+1)^-2*integral_0^pi sin(theta)^3/((2k+1)^2+(c^2/16)*sin(theta)^2)dtheta",
            "profile_zero_free_domain": "Phi is zero-free on C minus (i[4,infinity) union -i[4,infinity)); finite-order transforms are eventually zero-free on each compact subset of Re(c)>0",
            "primitive_L1": "||F_r||_1/|h_r|=(r+1)*tan(a)^2/8",
            "uniform_refill_remainder": "for real z>=0, |J_r(z)/h_r^2-z*kappa_r|<=(3/16)*z^2*kappa_r, uniformly in r; 3/16 is sharp for the exact L1/Young envelope",
            "complex_zero_free_half_disk": "for Re(z)>=0 and 0<|z|<16/3, J_r(z) is nonzero; after width-W dilation the condition is |z|W<16/3",
            "young_coefficient_asymptotic": "q_r=(9*pi^2/512)*(1+pi^2/(12*(r+1)^2)-pi^4/(240*(r+1)^4)+O(r^-6))",
            "normalized_refill_asymptotic": "kappa_r=pi^2/(72(r+1)^2)*(1+O(r^-2))",
            "universal_cost_asymptotic": "A_r~2*pi*r^2",
            "compensation_limit": "A_r*kappa_r=(pi^3/36)*(1+3/(4r)+(8pi^2-27)/(32r^2)+O(r^-3))",
            "strict_descent": "P_(r+1)/P_r<Q_r<1, with 1-Q_r numerator 12r^4+60r^3+99r^2+60r+8",
            "exact_bounds": "pi^3/36<P_r<=25/9 for r>=1, and P_r<=196/135 for r>=2",
            "cost_charged_local_chart": "G*L=P_r*(1+log(X)/W)^(2r+2)*(1+O(zW)); for zW->0 its liminf is at least pi^3/36, with equality requiring r->infinity and r*log(1+log(X)/W)->0",
            "rows": rows,
        },
        "proof_ledger": {
            "exact_primitive_energy": "PROVED",
            "exact_linear_max_cusp_refill": "PROVED",
            "global_positive_tilt_stieltjes_law": "PROVED",
            "finite_jump_transform": "PROVED",
            "global_alternating_primitive_hierarchy": "PROVED",
            "terminal_even_cusp_coefficient": "PROVED",
            "exact_second_primitive_energy": "PROVED",
            "second_primitive_two_scale_asymptotic": "PROVED",
            "sublinear_tilt_compensation_limit": "PROVED",
            "linear_scale_tilt_profile": "PROVED FOR POSITIVE REAL TILT",
            "superlinear_tilt_collapse": "PROVED FOR POSITIVE REAL TILT",
            "cost_charged_real_tilt_phase_diagram": "PROVED",
            "complex_right_half_plane_profile": "PROVED",
            "limiting_profile_stieltjes_zero_free_domain": "PROVED",
            "uniform_in_order_relative_linear_refill": "PROVED",
            "sharp_young_envelope_constant": "PROVED",
            "uniform_complex_zero_free_half_disk": "PROVED",
            "quadratic_decay_of_normalized_refill": "PROVED",
            "finite_nonzero_cost_refill_compensation_limit": "PROVED",
            "compensation_product_strictly_decreases_for_all_orders": "PROVED",
            "cost_charged_moving_local_floor": "PROVED FOR CHEBYSHEV FAMILY",
            "moving_order_Perron_estimate": "NOT PROVED",
            "new_beta_cancellation": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_cell_replay_order": MAX_CELL_ORDER,
            "maximum_table_order": MAX_TABLE_ORDER,
            "two_scale_spot_order": 100,
            "sublinear_tilt_spot_order": 64,
            "linear_scale_replay_order": LINEAR_SCALE_REPLAY_ORDER,
            "profile_simpson_panels": PROFILE_SIMPSON_PANELS,
            "asymptotic_spot_order": 1000,
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "root_searches": 0,
            "random_samples": 0,
            "quadratures": 1,
            "curve_computations": 0,
        },
        "asymptotic_spot_checks": {
            "refill_scaled_at_1000": f"{primitive_energy_ratio(1000) * 72 * 1001**2 / math.pi**2:.15f}",
            "product_over_limit_at_1000": f"{compensation_product(1000) / refill_limit():.15f}",
            "second_primitive_scaled_at_100": f"{second_primitive_energy_ratio(100) * 101**2:.15f}",
            "second_primitive_scaled_limit": f"{second_primitive_scaled_limit():.15f}",
            "sublinear_tilt_ratio_r64_z8": f"{relative_fixed_tilt_refill(64, 8):.15f}",
            "linear_profile_c1": f"{linear_scale_profile(1):.15f}",
            "linear_replay_r127_c1": f"{linear_scale_replay(LINEAR_SCALE_REPLAY_ORDER, 1):.15f}",
            "linear_profile_c2": f"{linear_scale_profile(2):.15f}",
            "linear_replay_r127_c2": f"{linear_scale_replay(LINEAR_SCALE_REPLAY_ORDER, 2):.15f}",
            "complex_profile_c1_plus_half_i": str(
                linear_scale_profile_complex(complex(1, 0.5))
            ),
            "complex_replay_r127_c1_plus_half_i": str(
                linear_scale_replay_complex(LINEAR_SCALE_REPLAY_ORDER, complex(1, 0.5))
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    payload = run(check_sources=not args.no_source_check)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json is not None:
        args.write_json.write_text(text, encoding="utf-8")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError(f"canonical fixture mismatch: {OUTPUT}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
