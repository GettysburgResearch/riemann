#!/usr/bin/env python3
"""Exact replay for dyadic beta-bridge scale renormalization."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

SOURCE_CONTRACTS = {
    "fad8ce2c4ce8633c5bb67356e6765800eac3d440": {
        "research/l-families/atlas/function_field/FFPS_ENDPOINT_SAMPLING_SQUARE_ROOT_FRONTIER.md": "35129f7f69f9ed4f2a457bd5e8c593c497b76834",
        "research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.py": "186cc2b2efe1b7af328bc374eee83de2f5dba871",
        "research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.json": "f447f0172f987cee7b75fb12543cb6fb4602e85b",
        "tests/test_ffps_endpoint_sampling_square_root_frontier.py": "85376a33e497badd8542b1829e4d36f63a7b72ee",
    },
    "d1af013130ae4004c629b916950e34545b0a65f1": {
        "research/l-families/atlas/function_field/FFPS_PREFIX_TRUNCATED_ROUGH_RANKIN_FRONTIER.md": "fa63811afd3ecc23b2ea26089a7544f093023c4e",
        "research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.py": "f004b2a418eba090899adb938337aff34cbb1ddb",
        "research/l-families/atlas/function_field/ffps_prefix_truncated_rough_rankin_frontier.json": "ef899a0a37a25d56c94478943faa95894e27ff3d",
        "tests/test_ffps_prefix_truncated_rough_rankin_frontier.py": "fb7f68fde6dbb0f75c498785e2d40b03ebfcb334",
    },
}

TOY_LIMIT = 256
TOY_ROUGH_MODULUS = 30


def check_source_contracts() -> None:
    for commit, paths in SOURCE_CONTRACTS.items():
        for path, expected in paths.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=3,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {path}")


def prefix_sums(increments: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    rows = [Fraction(0)]
    for value in increments:
        rows.append(rows[-1] + value)
    return tuple(rows)


def is_squarefree(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("squarefree support values must be positive integers")
    return all(
        value % (divisor * divisor) for divisor in range(2, math.isqrt(value) + 1)
    )


def validate_prefixes(prefixes: tuple[Fraction, ...]) -> int:
    if len(prefixes) < 3 or prefixes[0] != 0:
        raise ValueError("prefix vector must contain F_0=0 and at least two terms")
    return len(prefixes) - 1


def dyadic_boundaries(limit: int) -> tuple[int, ...]:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 2:
        raise ValueError("limit must be an integer at least two")
    rows = [0, 1]
    value = 2
    while value < limit:
        rows.append(value)
        value *= 2
    rows.append(limit)
    return tuple(sorted(set(rows)))


def dyadic_bridge(prefixes: tuple[Fraction, ...]) -> Fraction:
    limit = validate_prefixes(prefixes)
    maximum = abs(prefixes[1])
    left = 1
    while left < limit:
        right = min(2 * left, limit)
        maximum = max(
            maximum,
            *(
                abs(prefixes[height] - prefixes[left])
                for height in range(left + 1, right + 1)
            ),
        )
        left *= 2
    return maximum


def floor_ratio_bridge(prefixes: tuple[Fraction, ...]) -> Fraction:
    """An integer enlargement covering floors of real ratio-two intervals."""
    limit = validate_prefixes(prefixes)
    maximum = abs(prefixes[1])
    for left in range(1, limit):
        for right in range(left + 1, min(limit, 2 * left + 1) + 1):
            maximum = max(maximum, abs(prefixes[right] - prefixes[left]))
    return maximum


def maximal_prefix(prefixes: tuple[Fraction, ...]) -> Fraction:
    validate_prefixes(prefixes)
    return max(abs(value) for value in prefixes[1:])


def scale_filter(
    prefixes: tuple[Fraction, ...], dilation: int, omega: Fraction
) -> tuple[Fraction, ...]:
    limit = validate_prefixes(prefixes)
    if isinstance(dilation, bool) or not isinstance(dilation, int) or dilation < 2:
        raise ValueError("dilation must be an integer at least two")
    return tuple(
        prefixes[height] - omega * prefixes[height // dilation]
        for height in range(limit + 1)
    )


def inverse_scale_filter(
    prefixes: tuple[Fraction, ...], dilation: int, omega: Fraction
) -> tuple[Fraction, ...]:
    limit = validate_prefixes(prefixes)
    if isinstance(dilation, bool) or not isinstance(dilation, int) or dilation < 2:
        raise ValueError("dilation must be an integer at least two")
    rows = []
    for height in range(limit + 1):
        total = Fraction(0)
        scale = Fraction(1)
        reduced = height
        while reduced >= 1:
            total += scale * prefixes[reduced]
            reduced //= dilation
            scale *= omega
        rows.append(total)
    return tuple(rows)


def sharp_ratio_panel() -> dict[str, object]:
    increments = [Fraction(0) for _ in range(16)]
    increments[4] = Fraction(1)
    increments[7] = Fraction(-2)
    increments[9] = Fraction(-1)
    prefixes = prefix_sums(tuple(increments))
    dyadic = dyadic_bridge(prefixes)
    ratio = floor_ratio_bridge(prefixes)
    if dyadic != 1 or ratio != 3:
        raise ArithmeticError("the exact factor-three ratio control changed")
    return {
        "dyadic_bridge": str(dyadic),
        "floor_ratio_bridge": str(ratio),
        "sharp_pair": [5, 10],
        "sharp_increment": str(abs(prefixes[10] - prefixes[5])),
    }


def scale_panel() -> dict[str, object]:
    limit = 243
    increments = tuple(
        Fraction(((-1) ** index) * ((index % 7) - 3), index + 5)
        for index in range(1, limit + 1)
    )
    ordinary = prefix_sums(increments)
    dilation = 3
    omega = Fraction(-2, 5)
    duplicate = scale_filter(ordinary, dilation, omega)
    recovered = inverse_scale_filter(duplicate, dilation, omega)
    if recovered != ordinary:
        raise ArithmeticError("terminating scale inverse failed")
    ordinary_dyadic = dyadic_bridge(ordinary)
    duplicate_dyadic = dyadic_bridge(duplicate)
    ordinary_ratio = floor_ratio_bridge(ordinary)
    duplicate_ratio = floor_ratio_bridge(duplicate)
    if ordinary_ratio > 3 * ordinary_dyadic or duplicate_ratio > 3 * duplicate_dyadic:
        raise ArithmeticError("ratio-two bridge escaped the factor-three cover")
    modulus = abs(omega)
    if duplicate_dyadic > (1 + 3 * modulus) * ordinary_dyadic:
        raise ArithmeticError("forward dyadic scale bound failed")
    if ordinary_dyadic > (1 + 2 * modulus) / (1 - modulus) * duplicate_dyadic:
        raise ArithmeticError("inverse dyadic scale bound failed")
    ordinary_max = maximal_prefix(ordinary)
    if ordinary_dyadic > 2 * ordinary_max:
        raise ArithmeticError("bridge-to-maximal comparison failed")
    if ordinary_max > (limit.bit_length() + 1) * ordinary_dyadic:
        raise ArithmeticError("maximal-to-bridge telescoping failed")
    return {
        "dilation": dilation,
        "omega": str(omega),
        "limit": limit,
        "inverse_exact": True,
        "ordinary_dyadic_bridge": str(ordinary_dyadic),
        "duplicate_dyadic_bridge": str(duplicate_dyadic),
        "ordinary_floor_ratio_bridge": str(ordinary_ratio),
        "duplicate_floor_ratio_bridge": str(duplicate_ratio),
        "forward_bound": "B_D<=(1+3*|omega|)*B_M",
        "inverse_bound": "B_M<=(1+2*|omega|)/(1-|omega|)*B_D",
    }


def rough_hidden_excursion() -> dict[str, object]:
    limit = TOY_LIMIT
    queries = (37, 91, 155, 219)
    boundaries = tuple(sorted({*dyadic_boundaries(limit), *queries}))
    support = tuple(
        value
        for value in range(1, limit + 1)
        if math.gcd(value, TOY_ROUGH_MODULUS) == 1 and is_squarefree(value)
    )
    cells = []
    for left, right in pairwise(boundaries):
        members = tuple(value for value in support if left < value <= right)
        cells.append((left, right, members))
    left, right, members = max(cells, key=lambda row: len(row[2]))
    half = len(members) // 2
    amplitude = Fraction(1, 16)
    coefficients = [Fraction(0) for _ in range(limit)]
    for offset, index in enumerate(members[: 2 * half]):
        phase = Fraction(-1 if index % 2 else 1)
        sign = Fraction(1 if offset < half else -1)
        coefficients[index - 1] = sign * amplitude * phase
        if coefficients[index - 1] ** 2 > Fraction(1, index):
            raise ArithmeticError("rough hidden coefficient escaped its envelope")
    twisted = tuple(
        coefficient * Fraction(-1 if index % 2 else 1)
        for index, coefficient in enumerate(coefficients, start=1)
    )
    prefixes = prefix_sums(twisted)
    if any(prefixes[query] != 0 for query in queries):
        raise ArithmeticError("rough hidden excursion leaked into a query")
    if any(prefixes[boundary] != 0 for boundary in dyadic_boundaries(limit)):
        raise ArithmeticError("rough hidden excursion crossed a dyadic boundary")
    hidden_height = dyadic_bridge(prefixes)
    if hidden_height != half * amplitude:
        raise ArithmeticError("rough hidden bridge height changed")
    gap_count = len(boundaries) - 1
    lower_bound = Fraction(len(support), 2 * gap_count * 16) - Fraction(1, 32)
    if hidden_height < lower_bound:
        raise ArithmeticError("rough support pigeonhole lower bound failed")
    return {
        "limit": limit,
        "rough_modulus": TOY_ROUGH_MODULUS,
        "query_endpoints": list(queries),
        "dyadic_boundaries_adjoined": list(dyadic_boundaries(limit)),
        "rough_support_size": len(support),
        "chosen_cell": [left, right],
        "chosen_cell_support_size": len(members),
        "half_excursion_size": half,
        "hidden_bridge_height": str(hidden_height),
        "all_queries_zero": True,
        "all_dyadic_boundaries_zero": True,
        "coefficient_envelope": ("squarefree rough-supported |a_n|<=n^(-1/2)"),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contracts()
    return {
        "source_contracts": SOURCE_CONTRACTS,
        "theorem": {
            "dyadic_to_ratio_cover": "B_F<=C_F<=3*B_F, with factor 3 sharp source-blindly",
            "bridge_to_maximal": "B_F<=2*M_F and M_F<=(2+floor(log_2 X))*B_F",
            "literal_beta_scale": ("(1-a)/(1+2a)*B_M<=B_beta<=(1+3a)*B_M, a=67^(-1/2)"),
            "rough_scale": ("B_M<=(3*C_sf-2)*B_A and B_A<=(3*C_sm-2)*B_M"),
            "rh_normal_form": (
                "RH iff the augmented dyadic beta bridge, ordinary weighted "
                "Mobius bridge, or subfrontier rough-Mobius bridge is X^o(1)"
            ),
            "rough_sparse_no_go": (
                "support alone retains the square-root query exponent because "
                "all primes above y remain y-rough"
            ),
        },
        "exact_replays": {
            "sharp_ratio_cover": sharp_ratio_panel(),
            "scale_filter": scale_panel(),
            "rough_hidden_excursion": rough_hidden_excursion(),
        },
        "scope": {
            "literal_beta_bridge_estimate_proved": False,
            "mobius_bridge_estimate_proved": False,
            "rough_bridge_estimate_proved": False,
            "dyadic_endpoint_gate_needed_separately": False,
            "duplicate_67_contraction": False,
            "rough_support_sparse_source_blind_contraction": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "largest_increment_count": 256,
            "largest_prefix_vector_length": 257,
            "largest_ratio_pair_scan": 243,
            "rough_modulus": TOY_ROUGH_MODULUS,
            "floating_point_operations": 0,
            "large_matrices": 0,
            "zeta_zeros": 0,
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
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
