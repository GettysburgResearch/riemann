#!/usr/bin/env python3
"""Bounded replay for the source-exact reflection/geodesic RH criteria."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PARENT_COMMIT = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
EXTRA_NOTCHED_COMMIT = "3f10a6be2009f8e499b1bd421fd97b2095a82b06"
EQUIVALENCE_COMMIT = "9f29bdb6ea7375df84de550d62f9d0984634a8dd"
REFLECTION_COMMIT = "356fbf29e958e2ea067bfe5ef912b1f68d0334c6"
SOURCE_BLOBS = {
    PARENT_COMMIT: {
        "claims/lemmas/L-102602-native-completion-defect-and-pole-audit.md": (
            "47966830014aaaaf0ff83f3659a2b04541f45486"
        ),
        "claims/lemmas/L-102700-half-divisor-factorization-of-completion-defect.md": (
            "6d68773121a8c9d32e151f9e83d1546da4814d80"
        ),
        "claims/lemmas/L-102701-common-mother-ratiofour-two-field-form.md": (
            "70eb455a3b2bb0398f8bba22dee82c39ef803156"
        ),
        (
            "claims/lemmas/"
            "L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md"
        ): "6810bcece309b0c54ae6c8fc84b314990004549c",
        (
            "claims/lemmas/"
            "L-102708-uniform-geodesic-source-energy-is-polylogarithmic.md"
        ): "14ae4c9ff5e29f12cf8aa70ead5d4c4dd337d6d7",
    },
    EXTRA_NOTCHED_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md"
        ): "4a9aaf8bef6150bf054d6b6d4a873379db091b14",
    },
    EQUIVALENCE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md"
        ): "053c27bac9f8dec63c4865ab3563a7d985de7cbe",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_rh_equivalence.py"
        ): "60146ce6cc3912de270e9b2d8ad59e6e37b8c8f7",
        (
            "research/l-families/atlas/function_field/"
            "ffps_mollified_beta_rh_equivalence.json"
        ): "c0b5df0b206da90eeceb6df65109dd2fa3853612",
        "tests/test_ffps_mollified_beta_rh_equivalence.py": (
            "44d3f3e036202d9a78d992315504fea7d0960588"
        ),
    },
    REFLECTION_COMMIT: {
        (
            "claims/lemmas/"
            "L-106135-reflection-even-odd-energies-are-exact-complements.md"
        ): "5663c7798843f751c184a6923582df58f0b58a26",
    },
}


def check_source_blobs() -> None:
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


def squared_source_coefficient(n: int) -> Fraction:
    """Coefficient at n in (1-67^-2z)/zeta(2z)."""

    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    root = isqrt(n)
    if root * root != n:
        return Fraction(0)
    return Fraction(beta(root))


def normalized_squared_shift_coefficient(root: int) -> Fraction:
    if isinstance(root, bool) or not isinstance(root, int) or root < 1:
        raise ValueError("root must be a positive integer")
    return Fraction(beta(root), root)


def _multiply_polynomials(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            result[left_degree + right_degree] += left_value * right_value
    return tuple(result)


def d_out_coefficients() -> tuple[Fraction, ...]:
    """Coefficients from D^0 through D^4 of P(D)*(2D-1)."""

    result = (Fraction(1, 2),)
    for factor in (
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(1)),
        (Fraction(3, 2), Fraction(5)),
        (Fraction(-1), Fraction(2)),
    ):
        result = _multiply_polynomials(result, factor)
    return result


def differential_identity(s: Fraction) -> tuple[Fraction, Fraction]:
    """Return P(s)*(2s-1) and D_out(s)."""

    p_value = Fraction(1, 2) * s * (s - 1) * (5 * s + Fraction(3, 2))
    via_common_mother = p_value * (2 * s - 1)
    direct = sum(
        (coefficient * s**degree for degree, coefficient in enumerate(d_out_coefficients())),
        Fraction(0),
    )
    return via_common_mother, direct


def endpoint_source_ledger() -> dict[str, str]:
    return {
        "tau_0": "Lambda_0=lambda^square and Lambda_0*Lambda_0=beta^square",
        "tau_1": "Lambda_1=lambda and Lambda_1*Lambda_1=beta",
        "orientation": "I_1-I_0=integral_0^1 2*(dot(G_tau) *_M G_tau) d tau",
        "native_field": "H_nat=(2D-1)*I_1",
        "squared_field": "H_sq=(2D-1)*I_0",
    }


def reflection_energies(
    norm_squared: Fraction, correlation: Fraction
) -> tuple[Fraction, Fraction]:
    """Return reflection-even and reflection-odd squared norms."""

    if norm_squared < 0 or abs(correlation) > norm_squared:
        raise ValueError("correlation must lie in the Hilbert norm interval")
    even = (norm_squared + correlation) / 2
    odd = (norm_squared - correlation) / 2
    return even, odd


def reflected_negative_part(odd_derivative: Fraction) -> Fraction:
    """Negative part of h=-2*odd_derivative."""

    return 2 * max(odd_derivative, Fraction(0))


def causal_cutoff_valid(horizon: Fraction, cutoff: Fraction) -> bool:
    """A cutoff beyond the horizon cannot meet the causal convolution."""

    return horizon >= 0 and cutoff > horizon


def harmonic_l1_majorant(root_limit: int) -> Fraction:
    if isinstance(root_limit, bool) or not isinstance(root_limit, int) or root_limit < 1:
        raise ValueError("root_limit must be a positive integer")
    return 2 * sum((Fraction(1, root) for root in range(1, root_limit + 1)), Fraction(0))


def implication_graph() -> dict[str, str]:
    return {
        "RH_to_complete_absolute": "normalized Mertens plus compact BV summation",
        "complete_negative_to_RH": "fixed-mollified beta Mellin--Landau equivalence",
        "complete_iff_native_reflection": (
            "h_epsilon=-2*eta_epsilon*D_out*O_(1,R) on the causal horizon"
        ),
        "complete_iff_geodesic": "squared field has O(T) absolute log mass",
        "geodesic_iff_relative_reflection": (
            "C_epsilon=-2*eta_epsilon*D_out*(O_(1,R)-O_(0,R))"
        ),
    }


def run() -> dict[str, object]:
    expected_d_out = (
        Fraction(0),
        Fraction(3, 4),
        Fraction(1, 4),
        Fraction(-6),
        Fraction(5),
    )
    if d_out_coefficients() != expected_d_out:
        raise AssertionError("D_out polynomial coefficients changed")

    differential_samples = {}
    for integer in (2, 3, 5, 7):
        left, right = differential_identity(Fraction(integer))
        if left != right:
            raise AssertionError("extra differential failed to commute")
        differential_samples[str(integer)] = str(left)

    coefficient_samples = {}
    for root in (1, 2, 3, 5, 67, 134, 201):
        square = root * root
        coefficient = squared_source_coefficient(square)
        if coefficient != beta(root):
            raise AssertionError("squared-source coefficient changed")
        coefficient_samples[str(square)] = {
            "raw": str(coefficient),
            "normalized": str(normalized_squared_shift_coefficient(root)),
        }
    for nonsquare in (2, 3, 5, 6, 67, 68):
        if squared_source_coefficient(nonsquare) != 0:
            raise AssertionError("squared source acquired a nonsquare term")

    large_squarefree_root = 1
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53):
        large_squarefree_root *= prime
    if squared_source_coefficient(large_squarefree_root**2) != beta(
        large_squarefree_root
    ):
        raise AssertionError("integer square support lost exactness")

    reflection_samples = {}
    for norm_squared, correlation in (
        (Fraction(5), Fraction(3)),
        (Fraction(5), Fraction(-3)),
        (Fraction(7), Fraction(0)),
    ):
        even, odd = reflection_energies(norm_squared, correlation)
        if even + odd != norm_squared or even - odd != correlation:
            raise AssertionError("reflection projection identity changed")
        reflection_samples[f"N={norm_squared},I={correlation}"] = {
            "even": str(even),
            "odd": str(odd),
        }

    reflected_sign_samples = {}
    for odd_derivative in (Fraction(-3), Fraction(0), Fraction(2)):
        reflected_sign_samples[str(odd_derivative)] = str(
            reflected_negative_part(odd_derivative)
        )

    cutoff_panels = (
        (Fraction(0), Fraction(1)),
        (Fraction(10), Fraction(11)),
        (Fraction(100), Fraction(201, 2)),
    )
    if not all(causal_cutoff_valid(horizon, cutoff) for horizon, cutoff in cutoff_panels):
        raise AssertionError("causal cutoff failed to clear its horizon")

    graph = implication_graph()
    if len(graph) != 5:
        raise AssertionError("reflection/geodesic equivalence graph is incomplete")

    return {
        "frozen_sources": SOURCE_BLOBS,
        "kernel_identity": {
            "Phi_star": "(2D-1)*(A *_M A)",
            "P": "(1/2)*D*(D-1)*(5D+3/2)",
            "K_ext": "P*Phi_star=D_out*(A *_M A)",
            "D_out_coefficients_D0_through_D4": [
                str(value) for value in d_out_coefficients()
            ],
            "samples": differential_samples,
        },
        "source_decomposition": {
            "endpoint_normalization": endpoint_source_ledger(),
            "native": (
                "h_epsilon=eta_epsilon*D_out*(G_1 *_M G_1), "
                "because Lambda_1*Lambda_1=beta"
            ),
            "complete": "h_epsilon=C_epsilon+Q_epsilon",
            "geodesic": (
                "C_epsilon=eta_epsilon*D_out*(I_1-I_0)="
                "eta_epsilon*D_out*integral_0^1 "
                "2*(dot(G_tau) *_M G_tau) d tau"
            ),
            "squared": (
                "Q_epsilon(t)=sum beta(m)/m*kappa_epsilon(t-2log(m))"
            ),
            "coefficient_samples": coefficient_samples,
            "large_exact_square_root": str(large_squarefree_root),
        },
        "reflection": {
            "finite_horizon_fence": (
                "f_(tau,R)=1_[0,R]*f_tau with R>T; correlations agree on x<=T"
            ),
            "projection_identity": "I_tau=N_(tau,R)-2*O_(tau,R)=2*E_(tau,R)-N_(tau,R)",
            "D_kills_norm": (
                "D_out*I_tau=-2*D_out*O_(tau,R)=2*D_out*E_(tau,R)"
            ),
            "native": "h_epsilon=-2*eta_epsilon*D_out*O_(1,R)",
            "relative": (
                "C_epsilon=-2*eta_epsilon*D_out*(O_(1,R)-O_(0,R))"
            ),
            "negative_part": "(-2*r)_-=2*(r)_+",
            "energy_samples": reflection_samples,
            "sign_samples": reflected_sign_samples,
            "causal_cutoff_panels": [
                {"T": str(horizon), "R": str(cutoff)}
                for horizon, cutoff in cutoff_panels
            ],
        },
        "squared_l1": {
            "bound": (
                "integral_0^T |Q_epsilon| <= "
                "2*||kappa_epsilon||_1*H_floor(exp(T/2))"
            ),
            "growth": "O_epsilon(1+T)",
            "majorant_at_root_8": str(harmonic_l1_majorant(8)),
        },
        "equivalence": {
            "criteria": [
                (
                    "RH iff integral_0^T "
                    "(eta_epsilon*D_out*O_(1,R(T)))_+ dt=exp(o(T))"
                ),
                "RH iff integral_0^T (C_epsilon(t))_- dt=exp(o(T))",
                (
                    "RH iff integral_0^T (eta_epsilon*D_out*"
                    "(O_(1,R(T))-O_(0,R(T))))_+ dt=exp(o(T))"
                ),
            ],
            "fixed_epsilon": "every fixed epsilon>0 separately; some iff every",
            "causal_cutoff": "R(T)=T+1 (or any R(T)>T)",
            "implications": graph,
            "native_reflection_estimate_proved": False,
            "geodesic_estimate_proved": False,
            "rh_proved": False,
            "grh_proved": False,
        },
        "open_gates": {
            "native": {
                "name": "NATREF-MOLL106150",
                "quantity": "positive mass of eta_epsilon*D_out*O_(1,R(T))",
            },
            "geodesic": {
                "name": "GEO-WKSFSC106150",
                "quantity": (
                    "positive mass of eta_epsilon*D_out*"
                    "(O_(1,R(T))-O_(0,R(T)))"
                ),
                "load_bearing_rows": [
                    "distinct-product physical overlap",
                    "one-sided orientation of the polarized current",
                ],
            },
        },
        "resource_caps": {
            "differential_samples": len(differential_samples),
            "coefficient_samples": len(coefficient_samples),
            "reflection_samples": len(reflection_samples),
            "prime_intervals_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
