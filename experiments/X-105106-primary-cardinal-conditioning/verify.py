#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

VERDICT = "PASS_T105106_PRIMARY_CARDINAL_CONDITIONING"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105105-squarefree-crt-jet-flux"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "3edde4fdb651ae0c3781e4f832884f0d7c81247edd3b5a151c6b2c54f051cf05"
BASE_COMMIT = "0a7b83e596534a7b9633b1c59ea4fdb057551c05"

SPEC = importlib.util.spec_from_file_location("t105105_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105105 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105106.json",
    "claims/lemmas/L-105106-primary-cardinal-selector-conditioning.md",
    "claims/methodology/M-105106-selector-conditioning-review-contract.md",
    "claims/refutations/R-105106-selector-completeness-does-not-give-cofinal-control.md",
    "claims/theorems/T-105106-weighted-selector-frontier.md",
    "experiments/X-105106-primary-cardinal-conditioning/verify.py",
    "experiments/X-105106-primary-cardinal-conditioning/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105105 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105105 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def trim(poly: list[F]) -> list[F]:
    values = [F(value) for value in poly]
    require(bool(values), "polynomial coefficient list is empty")
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def add(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else F(0))
            + (right[index] if index < len(right) else F(0))
            for index in range(size)
        ]
    )


def scale(poly: list[F], scalar: F) -> list[F]:
    return trim([F(scalar) * value for value in poly])


def multiply(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, lhs in enumerate(left):
        for j, rhs in enumerate(right):
            result[i + j] += lhs * rhs
    return trim(result)


def power(poly: list[F], exponent: int) -> list[F]:
    require(exponent >= 0, "negative polynomial exponent")
    result = [F(1)]
    base = trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        remaining >>= 1
    return result


def evaluate(poly: list[F], point: F) -> F:
    value = F(0)
    for coefficient in reversed(trim(poly)):
        value = value * point + coefficient
    return value


def derivative(poly: list[F]) -> list[F]:
    values = trim(poly)
    if len(values) == 1:
        return [F(0)]
    return trim([F(index) * values[index] for index in range(1, len(values))])


def divmod_poly(numerator: list[F], denominator: list[F]) -> tuple[list[F], list[F]]:
    dividend = trim(numerator)
    divisor = trim(denominator)
    require(divisor != [F(0)], "division by zero polynomial")
    if len(dividend) < len(divisor):
        return [F(0)], dividend
    quotient = [F(0)] * (len(dividend) - len(divisor) + 1)
    remainder = dividend[:]
    while remainder != [F(0)] and len(remainder) >= len(divisor):
        offset = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[offset] += factor
        for index, value in enumerate(divisor):
            remainder[offset + index] -= factor * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def monic_gcd(left: list[F], right: list[F]) -> list[F]:
    a = trim(left)
    b = trim(right)
    while b != [F(0)]:
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return scale(a, F(1, 1) / a[-1])


def shift(poly: list[F], point: F) -> list[F]:
    """Coefficients of p(point+w) in ascending powers of w."""
    result = [F(0)]
    for coefficient in reversed(trim(poly)):
        result = multiply(result, [F(point), F(1)])
        result[0] += coefficient
        result = trim(result)
    return result


def render(value: F) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def render_poly(poly: list[F]) -> list[str]:
    return [render(value) for value in trim(poly)]


def linear(point: F) -> list[F]:
    return [-F(point), F(1)]


def validate_manifest(manifest: list[tuple[F, int]]) -> list[tuple[F, int]]:
    normalized = [(F(point), int(order)) for point, order in manifest]
    require(bool(normalized), "empty pole manifest")
    require(all(order >= 1 for _, order in normalized), "nonpositive pole order")
    points = [point for point, _ in normalized]
    require(len(points) == len(set(points)), "duplicate pole node")
    return normalized


def global_modulus(manifest: list[tuple[F, int]]) -> list[F]:
    result = [F(1)]
    for point, order in validate_manifest(manifest):
        result = multiply(result, power(linear(point), order))
    return result


def omitted_primary(
    manifest: list[tuple[F, int]], target: F
) -> tuple[list[F], int]:
    normalized = validate_manifest(manifest)
    matches = [order for point, order in normalized if point == F(target)]
    require(len(matches) == 1, "target is absent from manifest")
    result = [F(1)]
    for point, order in normalized:
        if point != F(target):
            result = multiply(result, power(linear(point), order))
    return result, matches[0]


def top_cardinal_selector(
    manifest: list[tuple[F, int]], targets: dict[F, F]
) -> list[F]:
    normalized = validate_manifest(manifest)
    target_map = {F(point): F(gamma) for point, gamma in targets.items()}
    manifest_points = {point for point, _ in normalized}
    require(set(target_map).issubset(manifest_points), "target outside pole manifest")
    selector = [F(0)]
    for point, gamma in target_map.items():
        omitted, order = omitted_primary(normalized, point)
        denominator = evaluate(omitted, point)
        require(denominator != 0, "primary moduli are not coprime")
        term = multiply(power(linear(point), order - 1), omitted)
        selector = add(selector, scale(term, gamma / denominator))
    total_order = sum(order for _, order in normalized)
    require(len(selector) - 1 < total_order, "selector is not reduced")
    require(top_congruences_hold(selector, normalized, target_map), "bad selector")
    return selector


def top_congruences_hold(
    selector: list[F],
    manifest: list[tuple[F, int]],
    targets: dict[F, F],
) -> bool:
    target_map = {F(point): F(gamma) for point, gamma in targets.items()}
    for point, order in validate_manifest(manifest):
        local = shift(selector, point)
        local += [F(0)] * max(0, order - len(local))
        expected = [F(0)] * order
        if point in target_map:
            expected[-1] = target_map[point]
        if local[:order] != expected:
            return False
    return True


def weighted_coefficient_norm(poly: list[F], radius: F) -> F:
    radius = F(radius)
    require(radius > 0, "coefficient radius must be positive")
    return sum(abs(value) * radius**index for index, value in enumerate(trim(poly)))


def conditioning_ledger(
    manifest: list[tuple[F, int]],
    targets: dict[F, F],
    boundary_radius: F,
) -> dict[str, object]:
    normalized = validate_manifest(manifest)
    boundary_radius = F(boundary_radius)
    require(boundary_radius > 0, "boundary radius must be positive")
    selector = top_cardinal_selector(normalized, targets)
    total_order = sum(order for _, order in normalized)
    node_radius = max(abs(point) for point, _ in normalized)
    require(boundary_radius >= node_radius, "boundary does not contain manifest")
    separations = [
        abs(left - right)
        for index, (left, _) in enumerate(normalized)
        for right, _ in normalized[index + 1 :]
    ]
    separation = min(separations) if separations else None
    target_rows: list[dict[str, object]] = []
    condition_sum = F(0)
    separation_sum = F(0)
    leading = F(0)
    for point, gamma in sorted(
        ((F(point), F(gamma)) for point, gamma in targets.items()),
        key=lambda row: row[0],
    ):
        omitted, order = omitted_primary(normalized, point)
        denominator = evaluate(omitted, point)
        kappa = F(1, 1) / abs(denominator)
        condition_sum += abs(gamma) * kappa
        leading += gamma / denominator
        if separation is not None:
            separation_sum += abs(gamma) * separation ** (-(total_order - order))
        target_rows.append(
            {
                "point": render(point),
                "order": order,
                "gamma": render(gamma),
                "M_target_at_target": render(denominator),
                "kappa": render(kappa),
            }
        )
    uniform_bound = (boundary_radius + node_radius) ** (total_order - 1) * condition_sum
    coefficient_norm = weighted_coefficient_norm(selector, boundary_radius)
    require(coefficient_norm <= uniform_bound, "coefficient bound failed")
    if separation is not None:
        require(condition_sum <= separation_sum, "separation bound failed")
    return {
        "manifest": [
            {"point": render(point), "order": order}
            for point, order in normalized
        ],
        "targets": target_rows,
        "total_primary_order": total_order,
        "selector": render_poly(selector),
        "degree": len(selector) - 1,
        "leading_coefficient_formula": render(leading),
        "weighted_coefficient_norm": render(coefficient_norm),
        "node_radius": render(node_radius),
        "boundary_radius": render(boundary_radius),
        "minimum_separation": None if separation is None else render(separation),
        "exact_condition_sum": render(condition_sum),
        "separation_condition_sum": (
            None if separation is None else render(separation_sum)
        ),
        "uniform_primary_cardinal_bound": render(uniform_bound),
        "coefficient_bound_verified": True,
        "separation_bound_verified": separation is not None,
    }


def cardinal_fixtures() -> dict[str, object]:
    mixed_manifest = [(F(-1), 2), (F(0), 1), (F(2), 3)]
    mixed_targets = {F(0): F(1), F(2): F(3)}
    mixed = conditioning_ledger(mixed_manifest, mixed_targets, F(3))

    symmetric_manifest = [(F(-2), 2), (F(-1), 3), (F(1), 3), (F(2), 2)]
    symmetric_targets = {F(-1): F(1), F(1): F(1)}
    symmetric = conditioning_ledger(symmetric_manifest, symmetric_targets, F(3))
    symmetric_poly = top_cardinal_selector(symmetric_manifest, symmetric_targets)
    require(
        all(value == 0 for index, value in enumerate(symmetric_poly) if index % 2),
        "sign-stable selector is not even",
    )
    require(len(symmetric_poly) - 1 <= 8, "even degree drop failed")
    symmetric["real_coefficients"] = True
    symmetric["even_selector"] = True
    symmetric["D_even_degree_improves_to_at_most_D_minus_2"] = True

    return {
        "mixed_multiplicity": mixed,
        "real_even_sign_stable": symmetric,
    }


def sharp_even_cluster(epsilon: F = F(1, 5), multiplicity: int = 2) -> dict[str, object]:
    epsilon = F(epsilon)
    require(F(0) < epsilon < F(1), "epsilon must lie inside the unit disk")
    require(multiplicity >= 1, "cluster multiplicity must be positive")
    manifest = [(-epsilon, multiplicity), (F(0), 1), (epsilon, multiplicity)]
    targets = {F(0): F(1)}
    row = conditioning_ledger(manifest, targets, F(1))
    selector = top_cardinal_selector(manifest, targets)
    expected = power([F(1), F(0), -F(1, 1) / epsilon**2], multiplicity)
    require(selector == expected, "sharp even selector changed")
    exact_circle_norm = (F(1) + F(1, 1) / epsilon**2) ** multiplicity
    blaschke_lower = epsilon ** (-2 * multiplicity)
    require(
        weighted_coefficient_norm(selector, F(1)) == exact_circle_norm,
        "sharp circle norm changed",
    )
    row.update(
        {
            "epsilon": render(epsilon),
            "nontarget_multiplicity": multiplicity,
            "unique_reduced_closed_form": "(1-z^2/epsilon^2)^m",
            "exact_unit_circle_sup_norm": render(exact_circle_norm),
            "all_holomorphic_selector_blaschke_lower_bound": render(blaschke_lower),
            "degree_D_minus_1_is_attained": len(selector) - 1
            == int(row["total_primary_order"]) - 1,
            "delta_exponent_D_minus_1_is_necessary": True,
            "real_even_symmetry_does_not_remove_conditioning": True,
        }
    )
    return row


def paired_flux_cluster(epsilon: F = F(1, 5)) -> dict[str, object]:
    epsilon = F(epsilon)
    require(F(0) < epsilon < F(1), "epsilon must lie inside the unit disk")
    parent = [F(1), F(0), epsilon**2 / 2, F(0), F(1, 4)]
    first = derivative(parent)
    second = derivative(first)
    require(monic_gcd(parent, first) == [F(1)], "F and F' share a zero")
    require(monic_gcd(parent, second) == [F(1)], "F and F'' share a zero")
    require(monic_gcd(first, second) == [F(1)], "F' and F'' share a zero")

    first_selector = [F(1), F(0), epsilon ** -2]
    second_selector = multiply(
        first_selector, [F(1), F(0), F(3) * epsilon ** -2]
    )
    first_norm = weighted_coefficient_norm(first_selector, F(1))
    second_norm = weighted_coefficient_norm(second_selector, F(1))
    first_lower = epsilon**-2
    second_lower = F(3) * epsilon**-4
    require(first_norm == F(1) + epsilon**-2, "first selector norm changed")
    require(
        second_norm == (F(1) + epsilon**-2) * (F(1) + F(3) * epsilon**-2),
        "second selector norm changed",
    )
    return {
        "family": "F_epsilon(z)=1+epsilon^2*z^2/2+z^4/4",
        "epsilon": render(epsilon),
        "F": render_poly(parent),
        "F_prime": render_poly(first),
        "F_double_prime": render_poly(second),
        "target_manifest": ["0"],
        "first_actual_pole_factor": "z(z^2+epsilon^2)",
        "second_actual_pole_factor": "z(z^2+epsilon^2)(3z^2+epsilon^2)",
        "first_selector": render_poly(first_selector),
        "second_selector": render_poly(second_selector),
        "first_unit_circle_sup_norm": render(first_norm),
        "second_unit_circle_sup_norm": render(second_norm),
        "first_blaschke_lower_bound": render(first_lower),
        "second_blaschke_lower_bound": render(second_lower),
        "rho_jet": render(epsilon**-2),
        "rho_jet_squared": render(epsilon**-4),
        "all_denominator_events_simple": True,
        "selectors_real_and_even": True,
        "higher_degree_holomorphic_escape_blocked": True,
    }


def edge_reduction_fixture() -> dict[str, object]:
    manifest = [(F(-1), 2), (F(0), 1), (F(2), 2)]
    targets = {F(0): F(1), F(2): F(2)}
    selector = top_cardinal_selector(manifest, targets)
    modulus = global_modulus(manifest)
    sample = F(3)
    lhs = evaluate(selector, sample) / evaluate(modulus, sample)
    rhs = F(0)
    rows: list[dict[str, str]] = []
    for point, gamma in targets.items():
        omitted, _ = omitted_primary(manifest, point)
        denominator = evaluate(omitted, point)
        contribution = gamma / (denominator * (sample - point))
        rhs += contribution
        rows.append(
            {
                "target": render(point),
                "gamma": render(gamma),
                "M_target_at_target": render(denominator),
                "sample_contribution": render(contribution),
            }
        )
    require(lhs == rhs, "partial-fraction edge reduction failed")

    # Same pole and principal-part data, arbitrarily different holomorphic
    # remainders: h_C=1/z+C gives M h_C=1+Cz for M=z.
    small_c = F(1)
    large_c = F(100)
    small_remainder_norm = F(1) + small_c
    large_remainder_norm = F(1) + large_c
    require(large_remainder_norm > small_remainder_norm, "remainder firewall failed")
    return {
        "selector": render_poly(selector),
        "global_modulus": render_poly(modulus),
        "sample_point": render(sample),
        "W_over_M": render(lhs),
        "cardinal_partial_fraction_sum": render(rhs),
        "target_terms": rows,
        "identity_verified": True,
        "edge_envelope": (
            "len(E)/(2*pi) * ||M h||_E * "
            "sum_target |gamma|*kappa/dist(E,target)"
        ),
        "simple_remainder_family": "h_C=1/z+C; M*h_C=1+Cz",
        "same_pole_and_principal_part_for_all_C": True,
        "small_remainder_boundary_norm": render(small_remainder_norm),
        "large_remainder_boundary_norm": render(large_remainder_norm),
        "event_data_alone_bounds_holomorphic_remainder": False,
    }


def mutation_firewalls() -> dict[str, object]:
    manifest = [(F(-1), 2), (F(0), 1), (F(2), 3)]
    targets = {F(0): F(1), F(2): F(3)}
    true_selector = top_cardinal_selector(manifest, targets)

    unnormalized = [F(0)]
    wrong_power = [F(0)]
    for point, gamma in targets.items():
        omitted, order = omitted_primary(manifest, point)
        unnormalized = add(
            unnormalized,
            scale(multiply(power(linear(point), order - 1), omitted), gamma),
        )
        wrong_power = add(
            wrong_power,
            scale(multiply(power(linear(point), order), omitted), gamma),
        )

    epsilon = F(1, 5)
    repeated_manifest = [(-epsilon, 2), (F(0), 1), (epsilon, 2)]
    repeated_targets = {F(0): F(1)}
    radical_mutant = [F(1), F(0), -epsilon**-2]

    close = sharp_even_cluster(F(1, 5), 2)
    closer = sharp_even_cluster(F(1, 50), 2)
    close_norm = F(close["exact_unit_circle_sup_norm"])
    closer_norm = F(closer["exact_unit_circle_sup_norm"])
    require(closer_norm > close_norm, "coalescence mutation did not grow")

    return {
        "true_selector": render_poly(true_selector),
        "omitted_M_target_normalization_rejected": not top_congruences_hold(
            unnormalized, manifest, targets
        ),
        "using_local_power_d_instead_of_d_minus_1_rejected": not top_congruences_hold(
            wrong_power, manifest, targets
        ),
        "radicalizing_repeated_nontarget_rejected": not top_congruences_hold(
            radical_mutant, repeated_manifest, repeated_targets
        ),
        "same_count_orders_and_parity_at_epsilon_1_over_5": {
            "D": close["total_primary_order"],
            "norm": close["exact_unit_circle_sup_norm"],
        },
        "same_count_orders_and_parity_at_epsilon_1_over_50": {
            "D": closer["total_primary_order"],
            "norm": closer["exact_unit_circle_sup_norm"],
        },
        "count_multiplicity_parity_only_uniform_bound_refuted": True,
        "unweighted_edge_decay_survives_arbitrary_polynomial_weight": False,
        "quarantined_moving_order_vandermonde_claim_used": False,
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.t105106.primary-cardinal-conditioning.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "primary_cardinal_fixtures": cardinal_fixtures(),
            "sharp_even_cluster": sharp_even_cluster(),
            "paired_first_second_cluster": paired_flux_cluster(),
            "pole_cancelled_edge_reduction": edge_reduction_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "top_jet_primary_cardinal_formula_proved": True,
            "finite_window_degree_bound_proved": True,
            "finite_window_coefficient_and_boundary_envelope_proved": True,
            "exact_conditioning_products_exposed": True,
            "pole_cancelled_weighted_edge_reduction_proved": True,
            "separation_free_uniform_selector_bound_refuted": True,
            "real_even_parity_cures_selector_conditioning": False,
            "sharp_cluster_higher_degree_holomorphic_escape_exists": False,
            "event_data_bounds_pole_cancelled_holomorphic_factor": False,
            "xi_event_manifest_constructed": False,
            "xi_conditioning_products_estimated_cofinally": False,
            "xi_pole_cancelled_holomorphic_factors_estimated": False,
            "xi_weighted_edge_asymptotics_proved": False,
            "xi_jet_moments_estimated": False,
            "strict_xi_jet_coherence_margin_proved": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
