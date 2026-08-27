#!/usr/bin/env python3
"""Bounded replay for the normalized first-rung Gram sign geometry."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_beta_gram_sign_geometry.json"

SOURCE_COMMIT = "3658d4c31cc866e15d48ab1fc9d8d119136da424"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md"
    ): "bd4cbb842e78c1dad5d380c8d20ff14c39bba15e",
    (
        "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py"
    ): "df80000192292cc5fc1cd08013f152fb257054f9",
    (
        "research/l-families/atlas/function_field/"
        "ffps_zero_free_beta_energy_ladder.json"
    ): "7e8889aa0dd1b01674e20158a52502cff0d8dffa",
    "tests/test_ffps_zero_free_beta_energy_ladder.py": (
        "983a1320f89087028f6724fe36aaca5ca1309b15"
    ),
}

DECIMAL_PRECISION = 80
ROOT_BISECTION_STEPS = 128
SIGN_GRID_CELLS = 128
SIMPSON_PANELS_PER_PIECE = 512
MAX_SIMPSON_PANELS_PER_PIECE = 2048
DIRECT_CHECK_SHIFTS = (
    Fraction(0),
    Fraction(1, 8),
    Fraction(1, 3),
    Fraction(3, 5),
    Fraction(9, 10),
    Fraction(1),
    Fraction(5, 4),
    Fraction(7, 4),
    Fraction(2),
)


def check_source_blobs() -> None:
    """Check the complete frozen source quartet by Git blob identity."""
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


def _as_decimal(value: Decimal | Fraction | float | str) -> Decimal:
    if isinstance(value, bool):
        raise TypeError("value must be a finite real number")
    if isinstance(value, Decimal):
        result = value
    elif isinstance(value, Fraction):
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            result = Decimal(value.numerator) / Decimal(value.denominator)
    elif isinstance(value, int):
        result = Decimal(value)
    elif isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("value must be a finite real number")
        result = Decimal(str(value))
    elif isinstance(value, str):
        try:
            result = Decimal(value)
        except Exception as error:
            raise ValueError("value must be a finite real number") from error
    else:
        raise TypeError("value must be a finite real number")
    if not result.is_finite():
        raise ValueError("value must be a finite real number")
    return result


def mass_decimal() -> Decimal:
    """Return M=4*sinh(1/2)^2=e+e^(-1)-2 at fixed precision."""
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        one = Decimal(1)
        return +(one.exp() + (-one).exp() - Decimal(2))


def raw_correlation_decimal(
    shift: Decimal | Fraction | float | str,
) -> Decimal:
    """Return C(|u|)=M^2 R(u) from the exact two-piece formula."""
    radius = _as_decimal(shift).copy_abs()
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        one = Decimal(1)
        two = Decimal(2)
        four = Decimal(4)
        if radius <= one:
            exp_two = two.exp()
            exp_minus_two = (-two).exp()
            first = (exp_two + four - (exp_two + two) * radius) * (-radius).exp()
            second = (two * radius + exp_minus_two * (radius + one)) * radius.exp()
            return +((first - second) / four)
        if radius <= two:
            tail = two - radius
            exp_tail = tail.exp()
            exp_minus_tail = (-tail).exp()
            sinh_tail = (exp_tail - exp_minus_tail) / two
            cosh_tail = (exp_tail + exp_minus_tail) / two
            return +(-(sinh_tail + tail * cosh_tail) / two)
        return Decimal(0)


def correlation_decimal(
    shift: Decimal | Fraction | float | str,
) -> Decimal:
    """Return the normalized autocorrelation R(u)=C(|u|)/M^2."""
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        mass = mass_decimal()
        return +(raw_correlation_decimal(shift) / (mass * mass))


def raw_inner_derivative_decimal(
    radius: Decimal | Fraction | float | str,
) -> Decimal:
    """Return C'(q) on the inner branch 0<=q<=1."""
    q = _as_decimal(radius)
    if not Decimal(0) <= q <= Decimal(1):
        raise ValueError("inner radius must lie in [0,1]")
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        two = Decimal(2)
        four = Decimal(4)
        exp_two = two.exp()
        exp_minus_two = (-two).exp()
        first = ((exp_two + two) * q - two * exp_two - Decimal(6)) * (-q).exp()
        second = ((two + exp_minus_two) * q + two + two * exp_minus_two) * q.exp()
        return +((first - second) / four)


def _exp_polynomial_primitive(
    quadratic: Decimal,
    linear: Decimal,
    constant: Decimal,
    point: Decimal,
) -> Decimal:
    """Primitive of exp(2v)*(A v^2+B v+C), evaluated at v."""
    two = Decimal(2)
    four = Decimal(4)
    polynomial = (
        two * quadratic * point * point
        + two * (linear - quadratic) * point
        + two * constant
        - linear
        + quadratic
    ) / four
    return (two * point).exp() * polynomial


def _integrate_branch_product(
    radius: Decimal,
    start: Decimal,
    end: Decimal,
    first_slope: Decimal,
    first_constant: Decimal,
    second_slope: Decimal,
    second_constant: Decimal,
) -> Decimal:
    if end <= start:
        return Decimal(0)
    quadratic = first_slope * second_slope
    linear = first_slope * second_constant + second_slope * first_constant
    constant = first_constant * second_constant
    primitive_difference = _exp_polynomial_primitive(
        quadratic, linear, constant, end
    ) - _exp_polynomial_primitive(quadratic, linear, constant, start)
    return (radius - Decimal(2)).exp() * primitive_difference


def direct_raw_correlation_decimal(
    shift: Decimal | Fraction | float | str,
) -> Decimal:
    """Integrate the two branches of Phi' directly, independently of C(q)."""
    radius = _as_decimal(shift).copy_abs()
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        zero = Decimal(0)
        one = Decimal(1)
        two = Decimal(2)
        if radius > two:
            return zero
        if radius <= one:
            return +sum(
                (
                    _integrate_branch_product(
                        radius,
                        zero,
                        one - radius,
                        one,
                        one,
                        one,
                        radius + one,
                    ),
                    _integrate_branch_product(
                        radius,
                        one - radius,
                        one,
                        one,
                        one,
                        -one,
                        one - radius,
                    ),
                    _integrate_branch_product(
                        radius,
                        one,
                        two - radius,
                        -one,
                        one,
                        -one,
                        one - radius,
                    ),
                ),
                zero,
            )
        return +_integrate_branch_product(
            radius,
            zero,
            two - radius,
            one,
            one,
            -one,
            one - radius,
        )


def root_bracket(steps: int = ROOT_BISECTION_STEPS) -> tuple[Decimal, Decimal]:
    """Return a bounded high-precision display bracket for the unique root."""
    if isinstance(steps, bool) or not isinstance(steps, int) or not 1 <= steps <= 256:
        raise ValueError("bisection steps must lie in [1,256]")
    lower = Decimal(0)
    upper = Decimal(1)
    if raw_correlation_decimal(lower) <= 0 or raw_correlation_decimal(upper) >= 0:
        raise ArithmeticError("root endpoint signs changed")
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        for _ in range(steps):
            midpoint = (lower + upper) / Decimal(2)
            if raw_correlation_decimal(midpoint) > 0:
                lower = midpoint
            else:
                upper = midpoint
    return lower, upper


def correlation(shift: float) -> float:
    """Binary64 display evaluation of the normalized exact formula."""
    if isinstance(shift, bool) or not isinstance(shift, (int, float)):
        raise TypeError("shift must be finite")
    value = float(shift)
    if not math.isfinite(value):
        raise ValueError("shift must be finite")
    radius = abs(value)
    mass = 4.0 * math.sinh(0.5) ** 2
    if radius <= 1.0:
        raw = 0.25 * (
            (math.exp(2.0) + 4.0 - (math.exp(2.0) + 2.0) * radius) * math.exp(-radius)
            - (2.0 * radius + math.exp(-2.0) * (radius + 1.0)) * math.exp(radius)
        )
    elif radius <= 2.0:
        tail = 2.0 - radius
        raw = -0.5 * (math.sinh(tail) + tail * math.cosh(tail))
    else:
        return 0.0
    return raw / (mass * mass)


def _simpson_piece(power: int, start: float, end: float, panels: int) -> float:
    width = (end - start) / panels

    def integrand(point: float) -> float:
        return point**power * correlation(point)

    total = integrand(start) + integrand(end)
    total += 4.0 * sum(
        integrand(start + index * width) for index in range(1, panels, 2)
    )
    total += 2.0 * sum(
        integrand(start + index * width) for index in range(2, panels, 2)
    )
    return width * total / 3.0


def simpson_absolute_moment(
    power: int, panels_per_piece: int = SIMPSON_PANELS_PER_PIECE
) -> float:
    """Bounded display quadrature for integral |u|^power R(u) du."""
    if isinstance(power, bool) or not isinstance(power, int) or not 0 <= power <= 4:
        raise ValueError("moment power must lie in [0,4]")
    if (
        isinstance(panels_per_piece, bool)
        or not isinstance(panels_per_piece, int)
        or panels_per_piece < 2
        or panels_per_piece > MAX_SIMPSON_PANELS_PER_PIECE
        or panels_per_piece % 2
    ):
        raise ValueError("panels per piece must be even and lie in [2,2048]")
    return 2.0 * (
        _simpson_piece(power, 0.0, 1.0, panels_per_piece)
        + _simpson_piece(power, 1.0, 2.0, panels_per_piece)
    )


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    direct_residuals = [
        abs(raw_correlation_decimal(shift) - direct_raw_correlation_decimal(shift))
        for shift in DIRECT_CHECK_SHIFTS
    ]
    maximum_direct_residual = max(direct_residuals)
    if maximum_direct_residual > Decimal("1e-75"):
        raise ArithmeticError("closed autocorrelation drifted from direct integration")

    lower, upper = root_bracket()
    if raw_correlation_decimal(lower) <= 0 or raw_correlation_decimal(upper) >= 0:
        raise ArithmeticError("display root bracket lost its signs")

    derivative_samples = [
        raw_inner_derivative_decimal(Fraction(index, SIGN_GRID_CELLS))
        for index in range(SIGN_GRID_CELLS + 1)
    ]
    if any(value >= 0 for value in derivative_samples):
        raise ArithmeticError("inner derivative sample lost negativity")

    sign_samples = 0
    for index in range(2 * SIGN_GRID_CELLS + 1):
        radius = Decimal(index) / Decimal(SIGN_GRID_CELLS)
        value = raw_correlation_decimal(radius)
        if radius < lower and value <= 0:
            raise ArithmeticError("inner positive sign sample failed")
        if upper < radius < Decimal(2) and value >= 0:
            raise ArithmeticError("outer negative sign sample failed")
        if radius == Decimal(2) and value != 0:
            raise ArithmeticError("support endpoint failed to vanish")
        sign_samples += 1

    moment_zero = simpson_absolute_moment(0)
    moment_one = simpson_absolute_moment(1)
    moment_two = simpson_absolute_moment(2)
    exact_moment_one = (2.0 - math.sinh(2.0)) / (16.0 * math.sinh(0.5) ** 4)
    if abs(moment_zero) > 2e-13:
        raise ArithmeticError("zeroth moment quadrature drifted")
    if not math.isclose(moment_one, exact_moment_one, rel_tol=0.0, abs_tol=4e-12):
        raise ArithmeticError("absolute first moment quadrature drifted")
    if not math.isclose(moment_two, -2.0, rel_tol=0.0, abs_tol=2e-13):
        raise ArithmeticError("second moment quadrature drifted")

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        root_midpoint = (lower + upper) / Decimal(2)
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "frozen_normalization": (
                "Phi(x)=e^(x-1)(1-|x-1|)_+, M=4sinh^2(1/2), J_1=Phi'/M"
            ),
            "source_imported_at_runtime": False,
        },
        "exact_autocorrelation": {
            "definition": "R(u)=integral_R J_1(v)J_1(v+u)dv",
            "normalization": "R(u)=C(|u|)/M^2",
            "mass": "M=4sinh^2(1/2)=e+e^(-1)-2",
            "inner_piece_0_le_q_le_1": (
                "C(q)=((e^2+4-(e^2+2)q)e^(-q)-(2q+e^(-2)(q+1))e^q)/4"
            ),
            "outer_piece_1_le_q_le_2": ("C(q)=-(sinh(2-q)+(2-q)cosh(2-q))/2"),
            "outside_piece_q_ge_2": "C(q)=0",
            "endpoint_values": {
                "C(0)": "1+sinh(2)/2",
                "C(1)": "-e/2",
                "C(2)": "0",
            },
        },
        "sign_geometry": {
            "unique_node": "xi is the unique q in (0,1) with C(q)=0",
            "display_root_lower": format(lower, "f"),
            "display_root_upper": format(upper, "f"),
            "display_root_midpoint": format(root_midpoint, ".16f"),
            "rounding_contract": (
                "80-digit Decimal display bracket only; the exact proof uses "
                "strict monotonicity and endpoint signs"
            ),
            "positive": "R(u)>0 iff |u|<xi",
            "negative": "R(u)<0 iff xi<|u|<2",
            "zeros": "R(u)=0 at |u|=xi and for |u|>=2",
            "inner_derivative": (
                "4C'(q)=((e^2+2)q-2e^2-6)e^(-q)-((2+e^(-2))q+2+2e^(-2))e^q<0 on [0,1]"
            ),
        },
        "ratio_annuli": {
            "radius": "rho=max(a/b,b/a)=e^|log(a/b)|",
            "positive": "1<=rho<e^xi",
            "nodal": "rho=e^xi",
            "negative": "e^xi<rho<e^2",
            "support_boundary_and_exterior": "rho>=e^2 gives R(log(a/b))=0",
            "oriented_positive": "e^(-xi)<a/b<e^xi",
            "oriented_negative": ("e^(-2)<a/b<e^(-xi) or e^xi<a/b<e^2"),
        },
        "integral_identities": {
            "zeroth_moment": "integral_R R(u)du=0",
            "absolute_first_moment": (
                "integral_R |u|R(u)du=(2-sinh(2))/(16sinh^4(1/2))"
            ),
            "second_moment": "integral_R u^2R(u)du=-2",
            "half_shell_balance": {
                "integral_0^1_R": "sinh(1)/(2M^2)",
                "integral_1^2_R": "-sinh(1)/(2M^2)",
            },
            "origin": ("R(0)=(1+sinh(2)/2)/(16sinh^4(1/2))"),
        },
        "programme_boundary": {
            "translate_gram_positive_definite": True,
            "physical_kernel_pointwise_nonnegative": False,
            "no_positivity_shortcut": (
                "Fourier/Gram positivity holds only after quadratic assembly; "
                "the physical off-diagonal kernel is negative on the outer annulus"
            ),
            "energy_or_off_diagonal_estimate_proved": False,
            "rh_or_grh_proved": False,
        },
        "bounded_replay": {
            "direct_branch_integral_checks": len(DIRECT_CHECK_SHIFTS),
            "maximum_direct_decimal_residual": format(maximum_direct_residual, ".3E"),
            "root_bisection_steps": ROOT_BISECTION_STEPS,
            "derivative_samples": len(derivative_samples),
            "sign_samples": sign_samples,
            "simpson_panels_per_piece": SIMPSON_PANELS_PER_PIECE,
            "display_moments": {
                "zeroth": format(moment_zero, ".16g"),
                "absolute_first": format(moment_one, ".16g"),
                "second": format(moment_two, ".16g"),
            },
        },
        "proof_ledger": {
            "piecewise_physical_autocorrelation": "PROVED EXACT",
            "unique_interior_node_and_complete_sign_geometry": "PROVED EXACT",
            "ratio_annulus_translation": "PROVED EXACT",
            "integral_and_moment_identities": "PROVED EXACT",
            "bounded_decimal_and_quadrature_checks": "REGRESSION ONLY",
            "energy_or_off_diagonal_estimate": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "frozen_blobs": len(SOURCE_BLOBS),
            "direct_formula_shifts": len(DIRECT_CHECK_SHIFTS),
            "root_bisection_steps": ROOT_BISECTION_STEPS,
            "sign_grid_cells_per_unit": SIGN_GRID_CELLS,
            "simpson_panels_per_piece": SIMPSON_PANELS_PER_PIECE,
            "zeta_zeros": 0,
            "primes": 0,
            "curves": 0,
            "random_samples": 0,
        },
    }


def canonical_text(result: dict[str, object]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = canonical_text(result)
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise RuntimeError("canonical JSON drift")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
