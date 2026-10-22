#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

VERDICT = "PASS_T105113_BUFFERED_SELECTOR_SHELL_AVERAGE"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105112-selector-domain-repair"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "3748777ede886502e57c6ad77777807b11b98104a8ecba04b60f162b10e2b19c"
BASE_COMMIT = "53c3a24b23335e7b4e77a703b2c3c224821ed749"

SPEC = importlib.util.spec_from_file_location("t105112_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105112 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105113.json",
    "claims/lemmas/L-105113-buffered-selector-shell-averaging.md",
    "claims/methodology/M-105113-shell-average-review-contract.md",
    "claims/refutations/R-105113-incomplete-buffer-manifest-changes-charge.md",
    "claims/theorems/T-105113-shell-average-edge-frontier.md",
    "experiments/X-105113-buffered-selector-shell-average/verify.py",
    "experiments/X-105113-buffered-selector-shell-average/tests/test_verify.py",
)

Gaussian = tuple[F, F]
ZERO: Gaussian = (F(0), F(0))
ONE: Gaussian = (F(1), F(0))
I: Gaussian = (F(0), F(1))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def render_gaussian(value: Gaussian) -> dict[str, str]:
    return {"real": render(value[0]), "imaginary": render(value[1])}


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return (left[0] + right[0], left[1] + right[1])


def g_sub(left: Gaussian, right: Gaussian) -> Gaussian:
    return (left[0] - right[0], left[1] - right[1])


def g_scale(value: Gaussian, scalar: F | int) -> Gaussian:
    scalar = F(scalar)
    return (scalar * value[0], scalar * value[1])


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def i_power(exponent: int) -> Gaussian:
    return (ONE, I, (-ONE[0], F(0)), (F(0), F(-1)))[exponent % 4]


def interval_moment(lower: F, upper: F, exponent: int) -> F:
    return (upper ** (exponent + 1) - lower ** (exponent + 1)) / F(exponent + 1)


def symmetric_moment(radius: F, exponent: int) -> F:
    if exponent % 2:
        return F(0)
    return F(2) * radius ** (exponent + 1) / F(exponent + 1)


def shell_unsigned_moment(inner: F, outer: F, exponent: int) -> F:
    if exponent % 2:
        return F(0)
    return F(2) * interval_moment(inner, outer, exponent)


def shell_signed_moment(inner: F, outer: F, exponent: int) -> F:
    if exponent % 2 == 0:
        return F(0)
    return F(2) * interval_moment(inner, outer, exponent)


def triangular_moment(inner: F, outer: F, exponent: int) -> F:
    """Integral of x^exponent against the parameter-measure triangle."""
    if exponent % 2:
        return F(0)
    return (
        F(2)
        * (outer ** (exponent + 2) - inner ** (exponent + 2))
        / F((exponent + 1) * (exponent + 2))
    )


def poly_trim(values: list[F]) -> list[F]:
    result = list(values)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    return poly_trim(
        [
            (left[index] if index < len(left) else F(0))
            + (right[index] if index < len(right) else F(0))
            for index in range(size)
        ]
    )


def poly_scale(values: list[F], scalar: F | int) -> list[F]:
    return poly_trim([F(scalar) * value for value in values])


def poly_mul(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly_trim(result)


def poly_derivative(values: list[F]) -> list[F]:
    if len(values) <= 1:
        return [F(0)]
    return poly_trim([F(index) * values[index] for index in range(1, len(values))])


def poly_eval(values: list[F], point: F | int) -> F:
    result = F(0)
    point = F(point)
    for value in reversed(values):
        result = result * point + value
    return result


def render_poly(values: list[F]) -> list[str]:
    return [render(value) for value in poly_trim(values)]


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105112 dependency artifact is stale")
    require(
        artifact.get("proof_object_sha256") == BASE_DIGEST,
        "T-105112 dependency digest changed",
    )
    require(
        artifact.get("verdict") == BASE.VERDICT,
        "T-105112 dependency verdict changed",
    )
    return {
        "path": "experiments/X-105112-selector-domain-repair",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def signed_shell_area_components(
    polynomial: list[F],
    t0: F,
    t1: F,
    eta0: F,
    eta1: F,
) -> tuple[Gaussian, Gaussian]:
    vertical = ZERO
    horizontal = ZERO
    scale = (t1 - t0) * (eta1 - eta0)
    for degree, coefficient in enumerate(polynomial):
        for y_power in range(degree + 1):
            x_power = degree - y_power
            scalar = F(math.comb(degree, y_power)) * coefficient
            monomial = g_scale(i_power(y_power), scalar)
            vertical = g_add(
                vertical,
                g_scale(
                    monomial,
                    shell_signed_moment(t0, t1, x_power)
                    * triangular_moment(eta0, eta1, y_power),
                ),
            )
            horizontal = g_add(
                horizontal,
                g_scale(
                    monomial,
                    triangular_moment(t0, t1, x_power)
                    * shell_signed_moment(eta0, eta1, y_power),
                ),
            )
    return (g_scale(g_mul(I, vertical), 1 / scale), g_scale(horizontal, -1 / scale))


def averaged_oriented_edge_components(
    polynomial: list[F],
    t0: F,
    t1: F,
    eta0: F,
    eta1: F,
) -> tuple[Gaussian, Gaussian]:
    vertical = ZERO
    horizontal = ZERO
    scale = (t1 - t0) * (eta1 - eta0)
    for degree, coefficient in enumerate(polynomial):
        for y_power in range(degree + 1):
            x_power = degree - y_power
            scalar = F(math.comb(degree, y_power)) * coefficient
            i_term = i_power(y_power)
            vertical_difference = F(1) - F((-1) ** x_power)
            vertical = g_add(
                vertical,
                g_scale(
                    i_term,
                    scalar
                    * vertical_difference
                    * interval_moment(t0, t1, x_power)
                    * triangular_moment(eta0, eta1, y_power),
                ),
            )
            negative_i_term = (i_term[0], -i_term[1])
            horizontal = g_add(
                horizontal,
                g_scale(
                    g_sub(negative_i_term, i_term),
                    scalar
                    * triangular_moment(t0, t1, x_power)
                    * interval_moment(eta0, eta1, y_power),
                ),
            )
    return (g_scale(g_mul(I, vertical), 1 / scale), g_scale(horizontal, 1 / scale))


def orientation_fixture() -> dict[str, object]:
    t0, t1 = F(1), F(3)
    eta0, eta1 = F(2), F(5)
    polynomial = [F(2), F(-3), F(1), F(2)]
    area_vertical, area_horizontal = signed_shell_area_components(
        polynomial, t0, t1, eta0, eta1
    )
    edge_vertical, edge_horizontal = averaged_oriented_edge_components(
        polynomial, t0, t1, eta0, eta1
    )
    require(area_vertical == edge_vertical, "vertical orientation identity failed")
    require(area_horizontal == edge_horizontal, "horizontal orientation identity failed")
    require(
        g_add(area_vertical, area_horizontal) == ZERO,
        "entire-polynomial contour charge is not zero",
    )
    require(area_vertical != ZERO, "orientation fixture is vacuous")
    return {
        "rectangle_parameters": {"T_0": "1", "T_1": "3", "eta_0": "2", "eta_1": "5"},
        "polynomial_coefficients": render_poly(polynomial),
        "vertical_area_component": render_gaussian(area_vertical),
        "vertical_oriented_edge_average": render_gaussian(edge_vertical),
        "horizontal_area_component": render_gaussian(area_horizontal),
        "horizontal_oriented_edge_average": render_gaussian(edge_horizontal),
        "vertical_sign": "+i*sgn(x)",
        "horizontal_sign": "-sgn(y)",
        "total_contour_charge": render_gaussian(ZERO),
        "coordinate_and_orientation_identity_exact": True,
    }


def bivariate_integral(
    coefficients: dict[tuple[int, int], F],
    x_moment,
    y_moment,
) -> F:
    return sum(
        coefficient * x_moment(x_power) * y_moment(y_power)
        for (x_power, y_power), coefficient in coefficients.items()
    )


def tonelli_fixture() -> dict[str, object]:
    t0, t1 = F(1), F(3)
    eta0, eta1 = F(2), F(5)
    delta_t = t1 - t0
    delta_eta = eta1 - eta0
    # K(x,y)=2+x^2+3y^2 is nonnegative everywhere.
    coefficients = {(0, 0): F(2), (2, 0): F(1), (0, 2): F(3)}
    vertical_weighted = bivariate_integral(
        coefficients,
        lambda power: shell_unsigned_moment(t0, t1, power),
        lambda power: triangular_moment(eta0, eta1, power),
    )
    horizontal_weighted = bivariate_integral(
        coefficients,
        lambda power: triangular_moment(t0, t1, power),
        lambda power: shell_unsigned_moment(eta0, eta1, power),
    )
    boundary_vertical = bivariate_integral(
        coefficients,
        lambda power: (F(1) + F((-1) ** power))
        * interval_moment(t0, t1, power),
        lambda power: triangular_moment(eta0, eta1, power),
    )
    boundary_horizontal = bivariate_integral(
        coefficients,
        lambda power: triangular_moment(t0, t1, power),
        lambda power: (F(1) + F((-1) ** power))
        * interval_moment(eta0, eta1, power),
    )
    require(vertical_weighted == boundary_vertical, "vertical Tonelli mean failed")
    require(horizontal_weighted == boundary_horizontal, "horizontal Tonelli mean failed")
    mean = (vertical_weighted + horizontal_weighted) / (delta_t * delta_eta)

    vertical_unweighted = bivariate_integral(
        coefficients,
        lambda power: shell_unsigned_moment(t0, t1, power),
        lambda power: symmetric_moment(eta1, power),
    )
    horizontal_unweighted = bivariate_integral(
        coefficients,
        lambda power: symmetric_moment(t1, power),
        lambda power: shell_unsigned_moment(eta0, eta1, power),
    )
    vertical_upper = vertical_unweighted / delta_t
    horizontal_upper = horizontal_unweighted / delta_eta
    require(
        mean <= vertical_upper + horizontal_upper,
        "inverse-width shell upper bound failed",
    )
    return {
        "nonnegative_cost": "K(x,y)=2+x^2+3*y^2",
        "vertical_weighted_area": render(vertical_weighted),
        "vertical_parameter_edge_integral": render(boundary_vertical),
        "horizontal_weighted_area": render(horizontal_weighted),
        "horizontal_parameter_edge_integral": render(boundary_horizontal),
        "normalized_exact_mean": render(mean),
        "vertical_unweighted_area": render(vertical_unweighted),
        "vertical_inverse_width": "1/Delta_T",
        "vertical_upper_component": render(vertical_upper),
        "horizontal_unweighted_area": render(horizontal_unweighted),
        "horizontal_inverse_width": "1/Delta_eta",
        "horizontal_upper_component": render(horizontal_upper),
        "tonelli_mean_exact": True,
        "coordinate_width_pairing_exact": True,
    }


def sharp_width_fixture() -> dict[str, object]:
    t0, t1 = F(1), F(3)
    eta0, eta1 = F(2), F(5)
    vertical_boundary_cost = F(2) * eta0
    vertical_area = F(2) * (t1 - t0) * eta0
    horizontal_boundary_cost = F(2) * t0
    horizontal_area = F(2) * (eta1 - eta0) * t0
    require(vertical_area / (t1 - t0) == vertical_boundary_cost, "vertical sharpness failed")
    require(horizontal_area / (eta1 - eta0) == horizontal_boundary_cost, "horizontal sharpness failed")
    return {
        "vertical_indicator_boundary_cost": render(vertical_boundary_cost),
        "vertical_indicator_area_over_Delta_T": render(vertical_area / (t1 - t0)),
        "horizontal_indicator_boundary_cost": render(horizontal_boundary_cost),
        "horizontal_indicator_area_over_Delta_eta": render(horizontal_area / (eta1 - eta0)),
        "both_width_constants_attained": True,
    }


def prescribed_weight_fixture() -> dict[str, object]:
    rectangles = {"A": (F(0), F(2)), "B": (F(2), F(0))}
    component_means = (F(1), F(1))
    rows: list[dict[str, object]] = []
    for lambda_one, lambda_two in ((F(3), F(1)), (F(1), F(3)), (F(1), F(1))):
        aggregate_mean = lambda_one + lambda_two
        costs = {
            name: lambda_one * values[0] + lambda_two * values[1]
            for name, values in rectangles.items()
        }
        selected = min(costs, key=costs.get)
        require(costs[selected] <= aggregate_mean, "prescribed aggregate selection failed")
        rows.append(
            {
                "weights": [render(lambda_one), render(lambda_two)],
                "aggregate_mean": render(aggregate_mean),
                "selected_rectangle": selected,
                "selected_cost": render(costs[selected]),
            }
        )
    universal_componentwise = any(
        values[0] <= component_means[0] and values[1] <= component_means[1]
        for values in rectangles.values()
    )
    require(not universal_componentwise, "fixture accidentally has a universal rectangle")
    require(rows[0]["selected_rectangle"] != rows[1]["selected_rectangle"], "selection did not depend on weights")
    return {
        "two_rectangle_costs": {name: [render(v[0]), render(v[1])] for name, v in rectangles.items()},
        "component_means": ["1", "1"],
        "prescribed_weight_rows": rows,
        "one_aggregate_cost_used_per_prescribed_pair": True,
        "selected_rectangle_can_depend_on_weights": True,
        "universal_componentwise_rectangle_exists": universal_componentwise,
    }


def cubic_fixture() -> dict[str, object]:
    function = [F(1), F(0), F(-1), F(1, 3)]
    first = poly_derivative(function)
    second = poly_derivative(first)
    third = poly_derivative(second)
    require(first == [F(0), F(-2), F(1)], "cubic first derivative changed")
    require(second == [F(-2), F(2)], "cubic second derivative changed")
    require(third == [F(2)], "cubic third derivative changed")

    residue_p_zero = poly_eval(function, 0) / poly_eval(second, 0)
    residue_p_two = poly_eval(function, 2) / poly_eval(second, 2)
    residue_q_zero = residue_p_zero**2
    residue_q_one = poly_eval(function, 1) ** 2 / (
        poly_eval(first, 1) * poly_eval(third, 1)
    )
    residue_q_two = residue_p_two**2
    require(
        (residue_p_zero, residue_p_two, residue_q_zero, residue_q_one, residue_q_two)
        == (F(-1, 2), F(-1, 6), F(1, 4), F(-1, 18), F(1, 36)),
        "cubic residues changed",
    )

    p_charges = [residue_p_zero, residue_p_zero, residue_p_zero + residue_p_two]
    q_charges = [
        residue_q_zero,
        residue_q_zero + residue_q_one,
        residue_q_zero + residue_q_one + residue_q_two,
    ]
    require(p_charges == [F(-1, 2), F(-1, 2), F(-2, 3)], "P charge jumps changed")
    require(q_charges == [F(1, 4), F(7, 36), F(2, 9)], "Q charge jumps changed")

    selector_one = [F(1), F(-1, 2)]
    selector_two = [F(1), F(-3, 2), F(1, 2)]
    require(poly_eval(selector_one, 0) == 1, "W1 target congruence failed")
    require(poly_eval(selector_one, 2) == 0, "W1 nontarget congruence failed")
    require(poly_eval(selector_two, 0) == 1, "W2 target congruence failed")
    require(poly_eval(selector_two, 1) == 0, "W2 F'' cancellation failed")
    require(poly_eval(selector_two, 2) == 0, "W2 F' cancellation failed")

    z = [F(0), F(1)]
    function_squared = poly_mul(function, function)
    first_carrier_left = poly_scale(poly_mul(poly_mul(z, selector_one), function), 2)
    first_carrier_right = poly_scale(poly_mul(function, first), -1)
    require(first_carrier_left == first_carrier_right, "W1 carrier cancellation failed")
    second_carrier_left = poly_scale(
        poly_mul(poly_mul(z, selector_two), function_squared), 4
    )
    second_carrier_right = poly_mul(poly_mul(first, second), function_squared)
    require(second_carrier_left == second_carrier_right, "W2 carrier cancellation failed")

    return {
        "F_coefficients": render_poly(function),
        "F_prime_coefficients": render_poly(first),
        "F_second_coefficients": render_poly(second),
        "F_third_coefficients": render_poly(third),
        "outer_actual_manifests": {
            "P": [{"point": "0", "order": 1, "role": "target"}, {"point": "2", "order": 1, "role": "nontarget"}],
            "Q": [{"point": "0", "order": 1, "role": "target"}, {"point": "1", "order": 1, "role": "nontarget"}, {"point": "2", "order": 1, "role": "nontarget"}],
        },
        "residues": {
            "P_at_0": render(residue_p_zero),
            "P_at_2": render(residue_p_two),
            "Q_at_0": render(residue_q_zero),
            "Q_at_1": render(residue_q_one),
            "Q_at_2": render(residue_q_two),
        },
        "core_only_normalized_P_charges_for_T_regions": [render(v) for v in p_charges],
        "core_only_normalized_Q_charges_for_T_regions": [render(v) for v in q_charges],
        "W_1_coefficients": render_poly(selector_one),
        "W_2_coefficients": render_poly(selector_two),
        "selector_values": {
            "W1_at_0": render(poly_eval(selector_one, 0)),
            "W1_at_2": render(poly_eval(selector_one, 2)),
            "W2_at_0": render(poly_eval(selector_two, 0)),
            "W2_at_1": render(poly_eval(selector_two, 1)),
            "W2_at_2": render(poly_eval(selector_two, 2)),
        },
        "canceled_first_carrier": "-F/(2*z)",
        "canceled_second_carrier": "F^2/(4*z)",
        "buffered_normalized_charges": ["-1/2", "1/4"],
        "complete_outer_manifest_restores_invariance": True,
    }


def manifest_ledger() -> dict[str, object]:
    return {
        "manifest_type": "complete actual-pole manifest on outer rectangle",
        "actual_first_order_formula": "max(r-m,0)",
        "actual_second_order_formula": "max(r+s-2*m,0)",
        "target_set": "eligible real events strictly inside fixed core",
        "all_other_outer_events": "zero congruence to full actual order",
        "outer_boundary_raw_regular": True,
        "intermediate_raw_irregular_parameter_pairs_form_null_set": True,
        "abstract_finiteness_is_not_Xi_authentication": True,
    }


def mutation_firewalls() -> dict[str, bool]:
    return {
        "core_only_manifest_transports_through_uncanceled_buffer": False,
        "separately_minimized_carriers_supply_one_common_rectangle": False,
        "one_rectangle_works_for_every_weight_pair": False,
        "good_rectangle_is_independent_of_prescribed_weights": False,
        "vertical_shell_is_divided_by_Delta_eta": False,
        "horizontal_shell_is_divided_by_Delta_T": False,
        "contour_charge_is_silently_normalized_by_two_pi_i": False,
        "shell_budget_discards_selector_cost": False,
        "qualitative_finite_shell_integrability_is_a_cofinal_bound": False,
        "finite_outer_event_set_is_an_authenticated_Xi_manifest": False,
        "absolute_second_budget_supplies_signed_first_moment_lower_bound": False,
        "multiple_target_defect_is_closed": False,
        "strict_xi_jet_coherence_proved": False,
        "rcmv104530_proved": False,
        "rh_established": False,
    }


def forbidden_control_characters() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    allowed = {9, 10, 13}
    for relative_path in CONTENT_FILES:
        raw = (REPO_ROOT / relative_path).read_bytes()
        for offset, value in enumerate(raw):
            if value < 32 and value not in allowed:
                failures.append({"path": relative_path, "offset": offset, "byte": value})
    return failures


def content_hashes() -> dict[str, str]:
    control_failures = forbidden_control_characters()
    require(not control_failures, f"forbidden control characters: {control_failures}")
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
        "schema": "riemann.t105113.buffered-selector-shell-average.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_POLYNOMIAL_AND_RECTANGULAR_INTEGRAL",
        "source": {"checkpoint_base": BASE_COMMIT},
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "coordinate_orientation_ledger": orientation_fixture(),
            "tonelli_width_ledger": tonelli_fixture(),
            "sharp_width_ledger": sharp_width_fixture(),
            "prescribed_weight_quantifier_ledger": prescribed_weight_fixture(),
            "cubic_buffer_ledger": cubic_fixture(),
            "manifest_ledger": manifest_ledger(),
            "mutation_firewalls": mutation_firewalls(),
            "forbidden_control_characters": forbidden_control_characters(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "fixed_core_outer_buffer_charge_verified": True,
            "signed_two_parameter_shell_identity_verified": True,
            "tonelli_mean_identity_verified": True,
            "simultaneous_prescribed_weight_selection_verified": True,
            "coordinate_width_pairing_verified": True,
            "sharp_measurable_width_constants_verified": True,
            "core_only_transport_refuted": True,
            "complete_buffer_cubic_invariance_verified": True,
            "complete_cofinal_xi_manifests_authenticated": False,
            "cofinal_weighted_xi_shell_bound_proved": False,
            "positive_signed_xi_first_moment_proved": False,
            "multiplicity_defect_closed": False,
            "strict_xi_jet_coherence_proved": False,
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
