#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105200_XI_SUMMABLE_RESIDUE_COHERENCE"
REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_FILES = (
    "PACKET_METADATA_105200.json",
    "claims/lemmas/L-105200-centered-monochromatic-defect.md",
    "claims/lemmas/L-105201-summable-residue-coherence-tail.md",
    "claims/lemmas/L-105202-second-level-debt-suppression.md",
    "claims/refutations/R-105200-unquantified-coherence-is-not-summable.md",
    "claims/refutations/R-105201-stepwise-endpoint-loss-does-not-sum.md",
    "claims/theorems/T-105200-xi-summable-reverse-rolle-tail.md",
    "claims/methodology/M-105200-hostile-review-contract.md",
    "experiments/X-105200-xi-residue-coherence/verify.py",
    "experiments/X-105200-xi-residue-coherence/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def weighted_moment(weights: list[F], frequencies: list[F], power: int) -> F:
    total_weight = sum(weights, F(0))
    require(total_weight > 0, "weights must have positive total mass")
    return sum((w * u**power for w, u in zip(weights, frequencies)), F(0)) / total_weight


def centered_defect_fixture(weights: list[F], frequencies: list[F]) -> dict[str, str]:
    mu = weighted_moment(weights, frequencies, 1)
    kappa2 = weighted_moment(weights, frequencies, 2)
    variance = weighted_moment(weights, [u - mu for u in frequencies], 2)
    third = weighted_moment(weights, [u - mu for u in frequencies], 3)

    coefficient_mean = sum(
        (w * (kappa2 - u * u) for w, u in zip(weights, frequencies)), F(0)
    )
    require(coefficient_mean == 0, "centered monochromatic coefficient lost zero mean")

    lhs = weighted_moment(
        weights,
        [(u * u - kappa2) * (u - mu) for u in frequencies],
        1,
    )
    rhs = 2 * mu * variance + third
    require(lhs == rhs, "centered covariance decomposition failed")

    return {
        "mean": str(mu),
        "kappa_squared": str(kappa2),
        "variance": str(variance),
        "third_centered_moment": str(third),
        "coefficient_mean": str(coefficient_mean),
        "covariance_identity": str(lhs),
    }


def coherence(values: list[F]) -> F:
    require(values, "coherence requires a nonempty list")
    count = F(len(values))
    return sum(values, F(0)) ** 2 / (count * sum((x * x for x in values), F(0)))


def coherence_exhaustion() -> dict[str, int | str]:
    grid = [F(k, 16) for k in range(-4, 5)]
    checks = 0
    sharpest_gap = F(0)
    for a in grid:
        for b in grid:
            for c in grid:
                eps = [a, b, c]
                delta = max(abs(x) for x in eps)
                if delta >= 1:
                    continue
                values = [1 + x for x in eps]
                C = coherence(values)
                bound = delta**2 / (1 - delta) ** 2 if delta else F(0)
                gap = bound - (1 - C)
                require(gap >= 0, "coherence variance bound failed")
                sharpest_gap = min(sharpest_gap, gap)
                checks += 1
    return {"checks": checks, "minimum_bound_gap": str(sharpest_gap)}


def harmonic_recurrence_checks() -> dict[str, int]:
    checks = 0
    for q in range(2, 13):
        kappa2 = F(q * q)
        for fplus in [F(1), F(-2), F(3, 2), F(-5, 3)]:
            for defect in [F(0), F(1, 7), F(-1, 9)]:
                fminus = (defect - fplus) / kappa2
                rho = fminus / fplus
                expected = -F(1, q * q) + F(1, q * q) * defect / fplus
                require(rho == expected, "critical-residue carrier algebra failed")
                checks += 1

        # At a zero of the middle derivative, exact harmonic recurrence makes
        # the lower derivative vanish and hence the second-level debt vanish.
        f_middle = F(5)
        f_upper = F(-q * q) * f_middle
        f_lower = F(0)
        debt = f_lower * f_lower / (f_middle * f_upper)
        require(debt == 0, "pure harmonic second-level debt must vanish")
        checks += 1
    return {"checks": checks}


def moment_log_convexity_checks() -> dict[str, int | str]:
    fixtures = [
        ([F(1), F(2), F(3)], [F(1), F(2), F(5)]),
        ([F(3), F(1), F(4), F(2)], [F(1), F(3), F(4), F(9)]),
        ([F(5), F(7)], [F(2), F(11)]),
    ]
    checks = 0
    max_ratio = F(0)
    for weights, frequencies in fixtures:
        for m in range(1, 9):
            M_m = sum((w * u**m for w, u in zip(weights, frequencies)), F(0))
            M_p1 = sum((w * u ** (m + 1) for w, u in zip(weights, frequencies)), F(0))
            M_p2 = sum((w * u ** (m + 2) for w, u in zip(weights, frequencies)), F(0))
            ratio = M_p1 * M_p1 / (M_m * M_p2)
            require(ratio <= 1, "moment log-convexity ratio exceeded one")
            max_ratio = max(max_ratio, ratio)
            checks += 1
    return {"checks": checks, "maximum_ratio": str(max_ratio)}


def product_tail_checks() -> dict[str, int | str]:
    # Exact rational model: C_m >= 1-K/m^2. Verify the elementary product
    # lower bound product(1-x_m) >= 1-sum x_m on a fail-closed range.
    checks = 0
    minimum_gap = None
    for K in [F(1, 100), F(1, 50), F(1, 25)]:
        for M in [10, 20, 40]:
            product = F(1)
            total = F(0)
            for m in range(M, M + 80):
                x = 2 * K / (m * m)
                require(0 <= x < 1, "invalid product-tail fixture")
                product *= 1 - x
                total += x
            gap = product - (1 - total)
            require(gap >= 0, "finite product union bound failed")
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
            checks += 1
    return {"checks": checks, "minimum_gap": str(minimum_gap or F(0))}


def nonsummable_o1_firewall(blocks: int = 250) -> dict[str, str | int]:
    # epsilon_m=1/floor(sqrt(m)) tends to zero but its squared block mass is
    # asymptotically harmonic. Use the exact two-point coherence formula.
    total_defect = F(0)
    previous = F(0)
    strict_growth = 0
    for k in range(2, blocks + 2):
        epsilon = F(1, k)
        C = F(1, 1) / (1 + epsilon * epsilon)
        block_size = 2 * k + 1
        total_defect += block_size * (1 - C)
        require(total_defect > previous, "firewall defect sum did not grow")
        strict_growth += 1
        previous = total_defect
    require(total_defect > 5, "firewall horizon too short to exhibit divergence")
    return {
        "blocks": blocks,
        "strict_growth_checks": strict_growth,
        "final_exact_partial_sum": str(total_defect),
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative in CONTENT_FILES:
        path = REPO_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative}")
        hashes[relative] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return hashes


def build_result() -> dict[str, object]:
    centered = [
        centered_defect_fixture([F(1), F(2), F(1)], [F(1), F(3), F(8)]),
        centered_defect_fixture([F(4), F(1), F(5), F(2)], [F(2), F(5), F(7), F(13)]),
        centered_defect_fixture([F(3), F(7)], [F(11), F(19)]),
    ]
    result = {
        "verdict": VERDICT,
        "centered_defect_fixtures": centered,
        "coherence_bound": coherence_exhaustion(),
        "harmonic_recurrence": harmonic_recurrence_checks(),
        "moment_log_convexity": moment_log_convexity_checks(),
        "product_tail": product_tail_checks(),
        "unquantified_o1_firewall": nonsummable_o1_firewall(),
        "content_sha256": content_hashes(),
        "analytic_saddle_estimates_machine_proved": False,
        "finite_prefix_controlled": False,
        "rpch104501_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_result()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(VERDICT)
    print(result["proof_object_sha256"])
    print("RH UNPROVED")


if __name__ == "__main__":
    main()
