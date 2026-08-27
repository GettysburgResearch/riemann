#!/usr/bin/env python3
"""Exact replay for the endpoint-sampling square-root frontier."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from itertools import pairwise
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "31c0e730ffe80683798d9cc830c26e9d451a8759"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_SINGLE_HARMONIC_MAXIMAL_PHASE_TRANSPORT.md": (
        "6c3b9487fe6bea2bc133c4d6283eb7e972797139"
    ),
    "research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.py": (
        "9662f1d429d4acf1c3e1b1f0968f163e5aa8eee9"
    ),
    "research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.json": (
        "8da26ca2b9ba3dc52b5620aeb5b02bcb44ffcca4"
    ),
    "tests/test_ffps_single_harmonic_maximal_phase_transport.py": (
        "23e7cbcbc7b25d1fb3e030ea26be8468ba594c4b"
    ),
}

TOY_LIMIT = 256
TOY_SQRT_MESH = 2

Gaussian = tuple[Fraction, Fraction]


def check_source_contract() -> None:
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
            raise RuntimeError(f"source blob mismatch: {path}")


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gconjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def gscale(value: Gaussian, scalar: Fraction) -> Gaussian:
    return value[0] * scalar, value[1] * scalar


def gnorm2(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def gpower(value: Gaussian, exponent: int) -> Gaussian:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    result = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        result = gmul(result, value)
    return result


def prefix_sums(values: tuple[Gaussian, ...]) -> tuple[Gaussian, ...]:
    total = (Fraction(0), Fraction(0))
    rows = [(Fraction(0), Fraction(0))]
    for value in values:
        total = gadd(total, value)
        rows.append(total)
    return tuple(rows)


def validate_endpoints(limit: int, endpoints: tuple[int, ...]) -> tuple[int, ...]:
    if (
        isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 2
        or not endpoints
        or any(
            isinstance(value, bool) or not isinstance(value, int) for value in endpoints
        )
    ):
        raise ValueError("limit and endpoints must be nontrivial integers")
    completed = tuple(sorted({0, limit, *endpoints}))
    if completed[0] != 0 or completed[-1] != limit:
        raise ValueError("endpoints must lie in the sampled interval")
    if any(value < 0 or value > limit for value in completed):
        raise ValueError("endpoints must lie in the sampled interval")
    return completed


def hidden_excursion(
    limit: int, endpoints: tuple[int, ...], unit: Gaussian
) -> tuple[tuple[Gaussian, ...], dict[str, object]]:
    completed = validate_endpoints(limit, endpoints)
    root = isqrt(limit)
    if root * root != limit or gnorm2(unit) != 1:
        raise ValueError("the exact replay uses a square limit and a unit phase")
    left, right = max(
        pairwise(completed),
        key=lambda pair: pair[1] - pair[0],
    )
    gap = right - left
    half = gap // 2
    amplitude = Fraction(1, root)
    coefficients = [(Fraction(0), Fraction(0)) for _ in range(limit)]
    for offset in range(1, 2 * half + 1):
        index = left + offset
        sign = Fraction(1) if offset <= half else Fraction(-1)
        phase = gpower(unit, index)
        coefficients[index - 1] = gscale(gconjugate(phase), sign * amplitude)
        if gnorm2(coefficients[index - 1]) > Fraction(1, index):
            raise ArithmeticError("coefficient escaped the n^(-1/2) envelope")
    twisted_terms = tuple(
        gmul(coefficient, gpower(unit, index))
        for index, coefficient in enumerate(coefficients, start=1)
    )
    prefixes = prefix_sums(twisted_terms)
    if any(prefixes[endpoint] != (0, 0) for endpoint in completed):
        raise ArithmeticError("hidden excursion leaked into a sampled endpoint")
    maximum_square = max(gnorm2(value) for value in prefixes)
    expected_square = (half * amplitude) ** 2
    if maximum_square != expected_square:
        raise ArithmeticError("hidden excursion height changed")
    return tuple(coefficients), {
        "limit": limit,
        "endpoints": list(completed),
        "sample_count_including_boundaries": len(completed),
        "largest_gap": gap,
        "half_excursion_length": half,
        "maximum_square": str(maximum_square),
        "all_sampled_prefixes_zero": True,
        "coefficient_envelope": "|a_n|<=n^(-1/2)",
    }


def dyadic_endpoints(limit: int) -> tuple[int, ...]:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 2:
        raise ValueError("limit must be an integer at least two")
    rows = [0, 1]
    value = 2
    while value < limit:
        rows.append(value)
        value *= 2
    rows.append(limit)
    return tuple(sorted(set(rows)))


def square_root_grid(limit: int, mesh: int) -> tuple[int, ...]:
    if (
        isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 2
        or isinstance(mesh, bool)
        or not isinstance(mesh, int)
        or mesh < 1
    ):
        raise ValueError("limit and mesh must be positive integers")
    root = isqrt(limit)
    if root * root != limit:
        raise ValueError("the exact replay uses a square limit")
    endpoints = [0]
    step = mesh
    while step < root:
        endpoints.append(step * step)
        step += mesh
    endpoints.append(limit)
    return tuple(endpoints)


def bridge_norm_panel() -> dict[str, object]:
    increments = tuple(
        (
            Fraction(((-1) ** index) * (index + 2), index + 1),
            Fraction(index - 3, index + 2),
        )
        for index in range(16)
    )
    prefixes = prefix_sums(increments)
    endpoints = dyadic_endpoints(len(increments))
    endpoint_square = max(gnorm2(prefixes[value]) for value in endpoints)
    bridge_square = Fraction(0)
    for left, right in pairwise(endpoints):
        for height in range(left, right + 1):
            bridge_square = max(
                bridge_square, gnorm2(gadd(prefixes[height], gneg(prefixes[left])))
            )
    maximal_square = max(gnorm2(value) for value in prefixes)
    residual_square = max(endpoint_square, bridge_square)
    if not residual_square <= 4 * maximal_square:
        raise ArithmeticError("endpoint/bridge lower comparison changed")
    if not maximal_square <= 4 * residual_square:
        raise ArithmeticError("endpoint/bridge upper comparison changed")
    return {
        "limit": len(increments),
        "endpoints": list(endpoints),
        "endpoint_max_square": str(endpoint_square),
        "bridge_max_square": str(bridge_square),
        "full_max_square": str(maximal_square),
        "squared_comparison": "max(E^2,B^2)/4<=M^2<=4*max(E^2,B^2)",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    unit = (Fraction(3, 5), Fraction(4, 5))
    _, dyadic_no_go = hidden_excursion(TOY_LIMIT, dyadic_endpoints(TOY_LIMIT), unit)
    root_grid = square_root_grid(TOY_LIMIT, TOY_SQRT_MESH)
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imports": (
                "one-harmonic maximal-prefix RH equivalence and exact common "
                "guarded frequency"
            ),
        },
        "source_blind_sampling": {
            "envelope": "|a_n|<=C/sqrt(n)",
            "sufficient_mesh": (
                "if max_j(sqrt(e_(j+1))-sqrt(e_j))<=R, then "
                "max_Y|F_Y(t)|<=max_(e in E)|F_e(t)|+2*C*R"
            ),
            "sufficient_count": "O(sqrt(X)/R+1) endpoints",
            "sharp_lower_bound": (
                "for m sampled endpoints, some admissible sequence has every "
                "sample zero and max prefix >=sqrt(X)/(2*(m+1))-1/(2*sqrt(X))"
            ),
            "subpower_frontier": (
                "worst-case subpower error requires m>=X^(1/2-o(1)); "
                "m=X^(1/2+o(1)) suffices"
            ),
            "dyadic_or_logarithmic_verdict": (
                "cannot control arbitrary admissible coefficients source-blindly"
            ),
            "adaptive_verdict": (
                "the same lower bound holds for deterministic adaptive value "
                "queries by answering zero and hiding an excursion in the final "
                "largest gap; randomized guarantees are not analyzed"
            ),
        },
        "literal_beta_bridge": {
            "endpoint_gate": ("E_h(X)=max_(e in dyadic endpoints)|D_e(t_(h,X))|"),
            "bridge_gate": (
                "B_h(X)=max_j max_(2^j<Y<=2^(j+1))"
                "|sum_(2^j<n<=Y)beta(n)n^(-1/2-it_(h,X))|"
            ),
            "exact_comparison": (
                "max(E_h,B_h)/2<=max_(Y<=X)|D_Y(t_(h,X))|<=2*max(E_h,B_h)"
            ),
            "local_phase_transport": ("(1+|t|log2)^(-1)B_0<=B_t<= (1+|t|log2)B_0"),
            "canonical_residual_gate": (
                "given dyadic endpoint control, the exact residual is the maximal "
                "beta bridge B_0=X^o(1); no universal minimality claim is made"
            ),
            "rh_equivalence": (
                "RH iff both the dyadic endpoint gate and beta bridge gate are X^o(1)"
            ),
        },
        "square_root_endpoint_theorem": {
            "literal_beta_constant": "C=2 because |beta(n)|<=2",
            "mesh_error": "4*R",
            "theorem": (
                "for any fixed nonzero harmonic, a predetermined square-root "
                "mesh with R=X^o(1) gives an endpoint-only RH-equivalent target"
            ),
            "endpoint_count": "X^(1/2+o(1))",
        },
        "bounded_replay": {
            "dyadic_hidden_excursion": dyadic_no_go,
            "square_root_grid": {
                "limit": TOY_LIMIT,
                "mesh": TOY_SQRT_MESH,
                "endpoints": list(root_grid),
                "count": len(root_grid),
            },
            "bridge_norm": bridge_norm_panel(),
        },
        "scope": {
            "literal_beta_square_root_sampler": True,
            "literal_beta_dyadic_endpoints_alone": False,
            "arbitrary_coefficient_log_sampler_refuted": True,
            "adaptive_sampler_refuted_source_blindly": True,
            "beta_bridge_estimate_proved": False,
            "endpoint_only_logarithmic_rh_criterion_proved": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "toy_limit": TOY_LIMIT,
            "toy_sqrt_mesh": TOY_SQRT_MESH,
            "floating_point_operations": 0,
            "zeta_zeros": 0,
            "large_matrices": 0,
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
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
