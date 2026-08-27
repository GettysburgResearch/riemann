#!/usr/bin/env python3
"""Bounded exact replay for the fixed band-pass beta energy ladder."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md": (
        "a794800a56ff3c168293b9f27b2700b5e87a6360"
    ),
    "research/l-families/atlas/function_field/ffps_extra_notched_mellin_landau_consumer.py": (
        "e64410f78d33fe841f9d157fbdd9f24b42a7e9c6"
    ),
    "research/l-families/atlas/function_field/ffps_extra_notched_mellin_landau_consumer.json": (
        "42e6f76dbfe9d677cd2f10713a4f81377a474279"
    ),
    "tests/test_ffps_extra_notched_mellin_landau_consumer.py": (
        "c3ff0fea530ed4dfe4ad0d28d11de015d379e70e"
    ),
    "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md": (
        "bf4d1baa231086ba7e8eafaecd39730d83c9201a"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py": (
        "2180038eef7ab639477879e806bb13fdbea0b1ec"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.json": (
        "c86a40d6a930603b3897ad12a28acc5f21e80dd6"
    ),
    "tests/test_ffps_mollified_beta_boundary_shell_identity.py": (
        "5e7de97284878c6f9b5a5ac43b83ccaf9528e242"
    ),
    "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md": (
        "f546d1e57c1886c1fddb590cd55b596a96bbefad"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_rh_equivalence.py": (
        "631c9a465f87c592368d04f1ae33810329f295c4"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_rh_equivalence.json": (
        "d316b0eaba5c24d62fb350e1f057c31eb12dccc7"
    ),
    "tests/test_ffps_mollified_beta_rh_equivalence.py": (
        "44d3f3e036202d9a78d992315504fea7d0960588"
    ),
    "research/l-families/atlas/function_field/FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md": (
        "105837343b6b8ef148488f492c66da8feae0334a"
    ),
    "research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py": (
        "53b5a710cb2f6b918958ff7e96801d81e2a0a79c"
    ),
    "research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.json": (
        "efc21abe6b87d16d49b272d0fd0dd65e1f059d57"
    ),
    "tests/test_ffps_boundary_field_near_correlation_criterion.py": (
        "006e1c41f34f4d1e9a8885fb160c7d9886a3a77d"
    ),
}

COEFFICIENT_CAP = 384
TOY_SOURCE_CAP = 20
REPLAY_ORDER_CAP = 4
REPLAY_BOX_ORDER_CAP = 3
TOY_BASE_KERNEL = (Fraction(3), Fraction(-1), Fraction(4), Fraction(2))


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def mobius(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int) -> int:
    return mobius(value) - (mobius(value // 67) if value % 67 == 0 else 0)


def factor_integer(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    factors: dict[int, int] = {}
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        prime += 1
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def beta_square_local(prime: int, exponent: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 2
        or isinstance(exponent, bool)
        or not isinstance(exponent, int)
        or exponent < 0
    ):
        raise ValueError("invalid local-factor input")
    if exponent == 0:
        return 1
    if prime == 67:
        return {1: 4, 2: 1}.get(exponent, 0)
    return int(exponent == 1)


def beta_square_from_euler(value: int) -> int:
    result = 1
    for prime, exponent in factor_integer(value).items():
        result *= beta_square_local(prime, exponent)
    return result


def exceptional_residue_ratio() -> Fraction:
    return Fraction(1 + Fraction(4, 67) + Fraction(1, 67**2), 1 + Fraction(1, 67))


def convolve(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    if not left or not right:
        raise ValueError("convolution inputs must be nonempty")
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def box_kernel(width_cells: int) -> tuple[Fraction, ...]:
    if (
        isinstance(width_cells, bool)
        or not isinstance(width_cells, int)
        or width_cells < 1
    ):
        raise ValueError("width_cells must be a positive integer")
    return (Fraction(1, width_cells),) * width_cells


def finite_difference(
    kernel: tuple[Fraction, ...], step: int, order: int
) -> tuple[Fraction, ...]:
    if not kernel:
        raise ValueError("kernel must be nonempty")
    if isinstance(step, bool) or not isinstance(step, int) or step < 1:
        raise ValueError("step must be a positive integer")
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= REPLAY_ORDER_CAP
    ):
        raise ValueError("order exceeds the bounded replay cap")
    difference = [Fraction(0)] * (step + 1)
    difference[0] = Fraction(1, step)
    difference[step] = Fraction(-1, step)
    result = kernel
    for _ in range(order):
        result = convolve(result, tuple(difference))
    return result


def bandpass_kernel(
    base: tuple[Fraction, ...],
    *,
    step: int,
    order: int,
    box_width: int,
    box_order: int,
) -> tuple[Fraction, ...]:
    if (
        isinstance(box_order, bool)
        or not isinstance(box_order, int)
        or not 0 <= box_order <= REPLAY_BOX_ORDER_CAP
    ):
        raise ValueError("box_order exceeds the bounded replay cap")
    result = finite_difference(base, step, order)
    box = box_kernel(box_width)
    for _ in range(box_order):
        result = convolve(result, box)
    return result


def moments(kernel: tuple[Fraction, ...], highest: int) -> tuple[Fraction, ...]:
    if not kernel:
        raise ValueError("kernel must be nonempty")
    if isinstance(highest, bool) or not isinstance(highest, int) or highest < 0:
        raise ValueError("highest must be a nonnegative integer")
    return tuple(
        sum(
            (value * index**degree for index, value in enumerate(kernel)),
            Fraction(0),
        )
        for degree in range(highest + 1)
    )


def autocorrelation(kernel: tuple[Fraction, ...]) -> dict[int, Fraction]:
    if not kernel:
        raise ValueError("kernel must be nonempty")
    radius = len(kernel) - 1
    return {
        shift: sum(
            (
                kernel[index] * kernel[index + shift]
                for index in range(
                    max(0, -shift), min(len(kernel), len(kernel) - shift)
                )
            ),
            Fraction(0),
        )
        for shift in range(-radius, radius + 1)
    }


def correlation_moments(
    correlation: dict[int, Fraction], highest: int
) -> tuple[Fraction, ...]:
    if not correlation:
        raise ValueError("correlation must be nonempty")
    if isinstance(highest, bool) or not isinstance(highest, int) or highest < 0:
        raise ValueError("highest must be a nonnegative integer")
    return tuple(
        sum(
            (value * shift**degree for shift, value in correlation.items()),
            Fraction(0),
        )
        for degree in range(highest + 1)
    )


def correlation_second_difference(
    correlation: dict[int, Fraction], step: int
) -> dict[int, Fraction]:
    if not correlation:
        raise ValueError("correlation must be nonempty")
    if isinstance(step, bool) or not isinstance(step, int) or step < 1:
        raise ValueError("step must be a positive integer")
    radius = max(abs(shift) for shift in correlation) + step
    return {
        shift: (
            2 * correlation.get(shift, Fraction(0))
            - correlation.get(shift - step, Fraction(0))
            - correlation.get(shift + step, Fraction(0))
        )
        / step**2
        for shift in range(-radius, radius + 1)
    }


def direct_toy_energy(
    source: tuple[Fraction, ...], kernel: tuple[Fraction, ...]
) -> Fraction:
    if not source or not kernel:
        raise ValueError("source and kernel must be nonempty")
    field = convolve(source, kernel)
    return sum((value * value for value in field), Fraction(0))


def gram_toy_energy(
    source: tuple[Fraction, ...], kernel: tuple[Fraction, ...]
) -> Fraction:
    if not source or not kernel:
        raise ValueError("source and kernel must be nonempty")
    gram = autocorrelation(kernel)
    return sum(
        (
            left * right * gram.get(right_index - left_index, Fraction(0))
            for left_index, left in enumerate(source)
            for right_index, right in enumerate(source)
        ),
        Fraction(0),
    )


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    coefficient_failures = [
        value
        for value in range(1, COEFFICIENT_CAP + 1)
        if beta(value) ** 2 != beta_square_from_euler(value)
    ]
    if coefficient_failures:
        raise ArithmeticError("beta-square Euler product failed")
    ratio = exceptional_residue_ratio()
    if ratio != Fraction(2379, 2278):
        raise ArithmeticError("exceptional residue ratio changed")

    step = 2
    order = 3
    box_width = 3
    box_order = 2
    high_pass = finite_difference(TOY_BASE_KERNEL, step, order)
    bandpass = bandpass_kernel(
        TOY_BASE_KERNEL,
        step=step,
        order=order,
        box_width=box_width,
        box_order=box_order,
    )
    high_pass_moments = moments(high_pass, order)
    bandpass_moments = moments(bandpass, order)
    if any(high_pass_moments[index] for index in range(order)):
        raise ArithmeticError("finite difference lost its exact zero order")
    if any(bandpass_moments[index] for index in range(order)):
        raise ArithmeticError("box smoothing changed the exact zero order")
    if high_pass_moments[order] == 0 or bandpass_moments[order] == 0:
        raise ArithmeticError("finite-difference zero order is not exact")

    base_correlation = autocorrelation(TOY_BASE_KERNEL)
    first_difference = finite_difference(TOY_BASE_KERNEL, step, 1)
    first_correlation = autocorrelation(first_difference)
    if first_correlation != correlation_second_difference(base_correlation, step):
        raise ArithmeticError("autocorrelation second-difference identity failed")

    bandpass_correlation = autocorrelation(bandpass)
    bandpass_correlation_moments = correlation_moments(bandpass_correlation, 2 * order)
    if any(bandpass_correlation_moments[index] for index in range(2 * order)):
        raise ArithmeticError("autocorrelation lost its doubled zero order")
    if bandpass_correlation_moments[2 * order] == 0:
        raise ArithmeticError("autocorrelation zero order is not exact")

    source = tuple(
        Fraction(beta(value), value) for value in range(1, TOY_SOURCE_CAP + 1)
    )
    direct_energy = direct_toy_energy(source, bandpass)
    gram_energy = gram_toy_energy(source, bandpass)
    if direct_energy != gram_energy or direct_energy <= 0:
        raise ArithmeticError("finite exact band-pass Gram identity failed")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_results": [
                "K_bd is nonzero compact BV on [0,4log2] with K_ext=D K_bd",
                "the beta boundary and fixed-mollified Mellin-Landau criteria are RH-equivalent",
                "the beta-square diagonal constant is 2379/(2278*zeta(2))",
            ],
        },
        "fixed_parameter_ladder": {
            "parameters": "epsilon>0, ell>0, integers r>=1 and j>=0, all fixed",
            "kernel": "B_(r,j)=eta_ell^(*j)*Delta_epsilon^r K_bd",
            "support": "[0,4log2+r*epsilon+j*ell]",
            "laplace_multiplier": (
                "((1-exp(-epsilon*s))/epsilon)^r*((1-exp(-ell*s))/(ell*s))^j*M_ext(s)/s"
            ),
            "multiplier_fence": (
                "difference and box factors are nonzero for Re(s)>0; "
                "the imported source carrier is used only in 0<Re(s)<1/2"
            ),
            "fixedness_fence": (
                "r,j,epsilon,ell do not depend on X, T, a zero, or a frequency"
            ),
        },
        "energy_criterion": {
            "prefix_field": (
                "H_(r,j;X)(t)=sum_(n<=X) beta(n)/sqrt(n)*B_(r,j)(t-log(n))"
            ),
            "energy": "E_(r,j)(X)=integral_R |H_(r,j;X)(t)|^2 dt",
            "equivalence": "RH iff E_(r,j)(X)=X^o(1)",
            "proof_route": "BV under RH; causality and Cauchy-Schwarz; one-sided Landau converse",
            "estimate_proved": False,
            "rh_proved": False,
        },
        "autocorrelation": {
            "definition": "R_(r,j)(u)=integral B_(r,j)(v)B_(r,j)(v+u)dv",
            "fourier_weight": (
                "|1-exp(-i*epsilon*t)|^(2r)/epsilon^(2r)*"
                "|eta_hat_ell(t)|^(2j)*|K_bd_hat(t)|^2"
            ),
            "zero_frequency_order": "exactly 2r",
            "boundary_mean": "K_bd_hat(0)=3*(1-sqrt(2))^2*(log(2))^2 != 0",
            "high_frequency": "O_fixed((1+|t|)^(-2j-2))",
            "r_equals_one_identity": (
                "R_(1,0)(u)=(2R_bd(u)-R_bd(u-epsilon)-R_bd(u+epsilon))/epsilon^2"
            ),
        },
        "gram_and_diagonal": {
            "gram_identity": (
                "E_(r,j)(X)=sum_(m,n<=X) beta(m)beta(n)/sqrt(mn)*R_(r,j)(log(m/n))"
            ),
            "ratio_support": ("exp(-S)<=m/n<=exp(S), S=4log2+r*epsilon+j*ell"),
            "diagonal": ("R_(r,j)(0)*2379/(2278*zeta(2))*log(X)+O_fixed(1)"),
            "off_diagonal_equivalence": "RH iff the signed off-diagonal is X^o(1)",
        },
        "finite_symbolic_replay": {
            "base_kernel": [str(value) for value in TOY_BASE_KERNEL],
            "step": step,
            "difference_order": order,
            "box_width_cells": box_width,
            "box_order": box_order,
            "bandpass_length": len(bandpass),
            "bandpass_moments_through_r": [str(value) for value in bandpass_moments],
            "autocorrelation_moments_through_2r": [
                str(value) for value in bandpass_correlation_moments
            ],
            "direct_energy": str(direct_energy),
            "gram_energy": str(gram_energy),
        },
        "scope": {
            "new_analytic_estimate": False,
            "horizon_dependent_filter": False,
            "wavelet_or_primitive_pair_bound": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "beta_square_coefficients": COEFFICIENT_CAP,
            "toy_source_terms": TOY_SOURCE_CAP,
            "finite_difference_order": REPLAY_ORDER_CAP,
            "box_convolution_order": REPLAY_BOX_ORDER_CAP,
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "conductor_families": 0,
            "l_functions": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
