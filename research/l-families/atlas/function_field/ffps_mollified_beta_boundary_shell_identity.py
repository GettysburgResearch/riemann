#!/usr/bin/env python3
"""Exact replay for the mollified-beta boundary-shell identity.

The replay is symbolic and finite.  It authenticates the source packets,
checks the Q(sqrt(2)) dyadic filters, and exercises the elementary boundary
difference/Jordan-mass algebra.  It does not estimate the beta detector.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

Quadratic = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

EQUIVALENCE_COMMIT = "a678292fd6d19d5b18f499aef35d2263cfc2b4ec"
SCOUT_COMMIT = "1a4e7f73addaeec3d13e83b7a8a967b42a47ce1b"
KERNEL_COMMIT = "9f29bdb6ea7375df84de550d62f9d0984634a8dd"

SOURCE_BLOBS = {
    EQUIVALENCE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md"
        ): "f546d1e57c1886c1fddb590cd55b596a96bbefad",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_rh_equivalence.py"
        ): "631c9a465f87c592368d04f1ae33810329f295c4",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_rh_equivalence.json"
        ): "d316b0eaba5c24d62fb350e1f057c31eb12dccc7",
        "tests/test_ffps_mollified_beta_rh_equivalence.py": (
            "44d3f3e036202d9a78d992315504fea7d0960588"
        ),
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md"
        ): "49e6f2fa54922991213f406c518f0468db4ed3a4",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_geodesic_rh_criterion.py"
        ): "6d9963fd27187da5ad19267124135bafbbbcecaf",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_geodesic_rh_criterion.json"
        ): "db9e1171fe35d586c32beda3eab0afc409a0a6af",
        "tests/test_ffps_mollified_geodesic_rh_criterion.py": (
            "7abb329cd8fb1e23d1344ed9a1e01be983ade277"
        ),
    },
    SCOUT_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_BETA_FINITE_SCOUT.md"
        ): "b7cc861cd327b17aed18cefcefc74afda560d433",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_finite_scout.py"
        ): "d48b99fd5e05d12fa7936da2f86b3b0de9990ce3",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_finite_scout.json"
        ): "d401fec015b6340090d73d489f6eaa93c9f21c8d",
        "tests/test_ffps_mollified_beta_finite_scout.py": (
            "8218b8049613c97f7d048cb04ea46549f879bf27"
        ),
    },
    KERNEL_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md"
        ): "8dff1025fd7d794497b71c2ba2920a51ff9095f2",
        (
            "research/l-families/atlas/function_field/"
            "ffps_signed_differential_atomic_shell_firewall.py"
        ): "729b48ad4ff5cd31fbe9e99d6abf2ab78124cf17",
        (
            "research/l-families/atlas/function_field/"
            "ffps_signed_differential_atomic_shell_firewall.json"
        ): "d5f4bf77edb3b9cb533926ee01886b75ea4271a6",
        "tests/test_ffps_signed_differential_atomic_shell_firewall.py": (
            "c31a53b2f5cb774a750f7c7ff8614fe8160a63ed"
        ),
    },
}


def check_source_blobs() -> None:
    """Authenticate every source packet used by the proof."""

    for commit, rows in SOURCE_BLOBS.items():
        for path, expected in rows.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    return left[0] + right[0], left[1] + right[1]


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qstr(value: Quadratic) -> str:
    rational, radical = value
    if radical == 0:
        return str(rational)
    radical_sign = "+" if radical > 0 else "-"
    radical_size = abs(radical)
    radical_text = "sqrt(2)" if radical_size == 1 else f"{radical_size}*sqrt(2)"
    if rational == 0:
        return radical_text if radical > 0 else f"-{radical_text}"
    return f"{rational}{radical_sign}{radical_text}"


def poly_mul(
    left: tuple[Quadratic, ...], right: tuple[Quadratic, ...]
) -> tuple[Quadratic, ...]:
    result = [(Fraction(0), Fraction(0))] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = qadd(
                result[left_index + right_index], qmul(left_value, right_value)
            )
    return tuple(result)


def kernel_dyadic_polynomial() -> tuple[Quadratic, ...]:
    """Coefficients of C(z)=(1-z)^2*(1-sqrt(2)*z)^2."""

    rational_square = (
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(0)),
        (Fraction(1), Fraction(0)),
    )
    radical_square = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    )
    return poly_mul(rational_square, radical_square)


def odd_compressed_polynomial() -> tuple[Quadratic, ...]:
    """Coefficients after beta's exact 2-adic source pairing."""

    one_minus_z_over_sqrt_two = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1, 2)),
    )
    return poly_mul(kernel_dyadic_polynomial(), one_minus_z_over_sqrt_two)


def qeval(coefficients: tuple[Quadratic, ...], point: Quadratic) -> Quadratic:
    result = (Fraction(0), Fraction(0))
    power = (Fraction(1), Fraction(0))
    for coefficient in coefficients:
        result = qadd(result, qmul(coefficient, power))
        power = qmul(power, point)
    return result


def qderivative(coefficients: tuple[Quadratic, ...]) -> tuple[Quadratic, ...]:
    return tuple(
        (Fraction(index) * coefficient[0], Fraction(index) * coefficient[1])
        for index, coefficient in enumerate(coefficients)
        if index > 0
    )


def rational_poly_mul(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return tuple(result)


def reflection_primitive_coefficients() -> tuple[Fraction, ...]:
    """Coefficients of R(D)=D_out/D from D^0 through D^3."""

    result = (Fraction(1, 2),)
    for factor in (
        (Fraction(-1), Fraction(1)),
        (Fraction(3, 2), Fraction(5)),
        (Fraction(-1), Fraction(2)),
    ):
        result = rational_poly_mul(result, factor)
    return result


def mobius(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    value = n
    parity = 0
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            parity += 1
            if value % prime == 0:
                return 0
        prime += 1
    if value > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(n: int) -> int:
    return mobius(n) - (mobius(n // 67) if n % 67 == 0 else 0)


def source_pair(m: int) -> tuple[int, int, int]:
    """Return beta(m), beta(2m), and beta(4m) for an odd m."""

    if isinstance(m, bool) or not isinstance(m, int) or m < 1 or m % 2 == 0:
        raise ValueError("m must be a positive odd integer")
    return beta(m), beta(2 * m), beta(4 * m)


def cell_difference(cells: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Unit-step causal difference, including the terminal falling edge."""

    if not cells:
        return ()
    extended = (Fraction(0),) + cells + (Fraction(0),)
    return tuple(
        extended[index + 1] - extended[index] for index in range(len(cells) + 1)
    )


def boundary_sample() -> dict[str, object]:
    """A finite exact sample of telescoping and the Jordan obstruction."""

    cells = (Fraction(3),)
    difference = cell_difference(cells)
    positive = sum((max(value, Fraction(0)) for value in difference), Fraction(0))
    negative = sum((max(-value, Fraction(0)) for value in difference), Fraction(0))
    absolute = sum((abs(value) for value in difference), Fraction(0))
    signed = sum(difference, Fraction(0))
    return {
        "epsilon": "1",
        "G_cells": [str(value) for value in cells],
        "difference_cells": [str(value) for value in difference],
        "positive_mass": str(positive),
        "negative_mass": str(negative),
        "absolute_mass": str(absolute),
        "signed_mass": str(signed),
        "terminal_boundary_cell": "0",
    }


def run() -> dict[str, object]:
    expected_kernel = (
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(-2)),
        (Fraction(3), Fraction(4)),
        (Fraction(-4), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    )
    if kernel_dyadic_polynomial() != expected_kernel:
        raise AssertionError("kernel dyadic polynomial changed")

    expected_odd = (
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(-5, 2)),
        (Fraction(5), Fraction(5)),
        (Fraction(-8), Fraction(-7, 2)),
        (Fraction(4), Fraction(2)),
        (Fraction(0), Fraction(-1)),
    )
    odd_polynomial = odd_compressed_polynomial()
    if odd_polynomial != expected_odd:
        raise AssertionError("odd-source dyadic polynomial changed")

    expected_reflection_primitive = (
        Fraction(3, 4),
        Fraction(1, 4),
        Fraction(-6),
        Fraction(5),
    )
    if reflection_primitive_coefficients() != expected_reflection_primitive:
        raise AssertionError("reflection primitive polynomial changed")

    one = (Fraction(1), Fraction(0))
    inverse_sqrt_two = (Fraction(0), Fraction(1, 2))
    if qeval(odd_polynomial, one) != (Fraction(0), Fraction(0)):
        raise AssertionError("affine-tail constant root was lost")
    if qeval(qderivative(odd_polynomial), one) != (Fraction(0), Fraction(0)):
        raise AssertionError("affine-tail double root was lost")
    if qeval(odd_polynomial, inverse_sqrt_two) != (Fraction(0), Fraction(0)):
        raise AssertionError("exponential-tail root was lost")
    if qeval(qderivative(odd_polynomial), inverse_sqrt_two) != (
        Fraction(0),
        Fraction(0),
    ):
        raise AssertionError("exponential-tail double root was lost")

    source_samples = {}
    for odd in (1, 3, 5, 9, 67, 201, 335):
        at_m, at_twice_m, at_four_m = source_pair(odd)
        if at_twice_m != -at_m or at_four_m != 0:
            raise AssertionError("beta 2-adic source compression failed")
        source_samples[str(odd)] = [at_m, at_twice_m, at_four_m]

    sample = boundary_sample()
    if sample["signed_mass"] != sample["terminal_boundary_cell"]:
        raise AssertionError("boundary telescoping sample failed")
    if Fraction(sample["absolute_mass"]) != (
        2 * Fraction(sample["negative_mass"]) + Fraction(sample["signed_mass"])
    ):
        raise AssertionError("Jordan balance identity failed")

    return {
        "schema": "riemann.function_field.ffps_mollified_beta_boundary_shell.v1",
        "status": (
            "exact boundary-shell and primitive-detector equivalence; "
            "no detector estimate and no RH or GRH proof"
        ),
        "frozen_sources": SOURCE_BLOBS,
        "primitive_kernel": {
            "translation": "tau_a f(t)=f(t-a)",
            "causal_primitive": "K_bd(t)=K_ext((−infinity,t])",
            "distributional_identity": "D*K_bd=K_ext",
            "support": "[0,4*log(2)]",
            "regularity": "compact ordinary BV function",
            "laplace_multiplier": "M_ext(s)/s (removable at s=0)",
            "base_primitive": "w(t)=1_[0,infinity)*(13+3t-8exp(t/2))",
            "base_derivative": ("D*w=5*delta_0+(3-4exp(t/2))*1_[0,infinity)dt"),
        },
        "odd_fiber_compression": {
            "source_identity": (
                "S_beta=(I-2^(-1/2)*tau_log(2))*"
                "sum_(m odd) beta(m)/sqrt(m)*delta_log(m)"
            ),
            "beta_relations": "beta(2m)=-beta(m), beta(4m)=0 for odd m",
            "source_samples_beta_m_beta_2m_beta_4m": source_samples,
            "kernel_polynomial_C": [qstr(value) for value in expected_kernel],
            "compressed_polynomial_P": [qstr(value) for value in expected_odd],
            "factorization": ("P(z)=(1-z)^2*(1-sqrt(2)z)^2*(1-z/sqrt(2))"),
            "tail_annihilation": {
                "P(1)": qstr(qeval(odd_polynomial, one)),
                "P_prime(1)": qstr(qeval(qderivative(odd_polynomial), one)),
                "P(1/sqrt(2))": qstr(qeval(odd_polynomial, inverse_sqrt_two)),
                "P_prime(1/sqrt(2))": qstr(
                    qeval(qderivative(odd_polynomial), inverse_sqrt_two)
                ),
            },
            "compressed_kernel": "psi=P(tau_log(2))*w",
            "compressed_kernel_support": "[0,5*log(2)]",
            "boundary_field": ("G(t)=sum_(m odd) beta(m)/sqrt(m)*psi(t-log(m))"),
        },
        "finite_difference": {
            "all_fixed_epsilon": "h_epsilon=(I-tau_epsilon)G/epsilon",
            "scout_width": "epsilon=log(2)/2 gives a half-dyadic first difference",
            "signed_boundary": (
                "integral_0^T h_epsilon=(1/epsilon)*"
                "integral_(T-epsilon)^T G, with G=0 on t<0"
            ),
            "cell_telescope": (
                "H_j=(B_j-B_(j-1))/epsilon for B_j="
                "integral_(j epsilon)^((j+1)epsilon) G"
            ),
            "jordan_balance": (
                "integral|h_epsilon|=2*integral(h_epsilon)_-+integral h_epsilon"
            ),
            "absolute_l1_comparison": (
                "||h_epsilon||_[0,T] <= 2||G||_[0,T]/epsilon; "
                "||G||_[0,T] <= epsilon*(floor(T/epsilon)+1)*"
                "||h_epsilon||_[0,T]"
            ),
            "exact_cell_sample": sample,
        },
        "native_reflection": {
            "R_of_D": "D_out/D=5D^3-6D^2+(1/4)D+3/4",
            "R_coefficients_D0_through_D3": [
                str(value) for value in expected_reflection_primitive
            ],
            "primitive": "G=R(D)*I_1",
            "finite_horizon": ("G=(3/4)N_(1,R)-2R(D)O_(1,R) for x<R"),
            "norm_removal": ("(I-tau_epsilon) kills the constant (3/4)N_(1,R) exactly"),
        },
        "equivalence": {
            "criterion": (
                "RH iff integral_0^T |G| dt=exp(o(T)) iff "
                "integral_0^T (G)_- dt=exp(o(T))"
            ),
            "mollified_absolute_equivalence": (
                "for every fixed epsilon>0, ||G||_1=exp(o(T)) iff "
                "||h_epsilon||_1=exp(o(T))"
            ),
            "proof_inputs": (
                "normalized Mertens plus compact-BV summation for RH=>; "
                "Mellin-Landau and nonvanishing of M_ext(s)/s in "
                "0<Re(s)<1/2 for the converse"
            ),
            "primitive_estimate_proved": False,
            "mollified_estimate_proved": False,
            "rh_proved": False,
            "grh_proved": False,
        },
        "no_go": {
            "formal_scope": "finite-difference/boundary algebra alone",
            "counterexample": (
                "G=A*1_[0,epsilon) has zero terminal boundary and zero signed "
                "mass after 2epsilon, but negative mass A and absolute mass 2A"
            ),
            "odd_fiber_obstruction": (
                "P(0)=1, so dyadic shifts do not annihilate an independent "
                "odd source fiber"
            ),
            "remaining_burden": (
                "control of Jordan mass must use cancellation between distinct "
                "odd source indices or equivalent RH-bearing arithmetic"
            ),
        },
        "resource_caps": {
            "maximum_polynomial_degree": 5,
            "source_samples": len(source_samples),
            "prime_intervals_enumerated": 0,
            "source_ranges_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
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
