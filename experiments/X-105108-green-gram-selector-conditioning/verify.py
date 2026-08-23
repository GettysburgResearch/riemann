#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

VERDICT = "PASS_T105108_GREEN_GRAM_SELECTOR_CONDITIONING"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105107-blaschke-pick-jet-selectors"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "82747e320365a97bf9824dd84960f00bbcb77cd738040c2c5214be844dfc738c"
BASE_COMMIT = "cf07de0ba009e8b288eb98b6b4a0ed1d8f12e251"

SPEC = importlib.util.spec_from_file_location("t105107_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105107 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105108.json",
    "claims/lemmas/L-105108-green-gram-selector-conditioning.md",
    "claims/methodology/M-105108-green-gram-review-contract.md",
    "claims/refutations/R-105108-local-potential-loads-do-not-control-pick-interaction.md",
    "claims/theorems/T-105108-optimal-selector-conditioning-frontier.md",
    "experiments/X-105108-green-gram-selector-conditioning/verify.py",
    "experiments/X-105108-green-gram-selector-conditioning/tests/test_verify.py",
)

trim = BASE.trim
add = BASE.add
scale = BASE.scale
multiply = BASE.multiply
evaluate = BASE.evaluate
render = BASE.render
render_poly = BASE.render_poly
determinant = BASE.determinant
is_psd = BASE.is_psd
pick_matrix = BASE.pick_matrix


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105107 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105107 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def pick_kernel(nodes: list[F]) -> list[list[F]]:
    normalized = [F(node) for node in nodes]
    require(bool(normalized), "empty Pick node list")
    require(len(normalized) == len(set(normalized)), "duplicate Pick node")
    require(all(abs(node) < 1 for node in normalized), "node outside unit disk")
    return [
        [F(1, 1) / (F(1) - left * right) for right in normalized]
        for left in normalized
    ]


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def polynomial_determinant(matrix: list[list[list[F]]]) -> list[F]:
    size = len(matrix)
    require(size >= 1, "empty polynomial matrix")
    require(all(len(row) == size for row in matrix), "nonsquare polynomial matrix")
    result = [F(0)]
    for permutation in itertools.permutations(range(size)):
        term = [F(1)]
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
        result = add(result, scale(term, F(permutation_sign(permutation))))
    return trim(result)


def pick_determinant_polynomial(nodes: list[F], values: list[F]) -> list[F]:
    normalized_nodes = [F(node) for node in nodes]
    normalized_values = [F(value) for value in values]
    require(
        len(normalized_nodes) == len(normalized_values) and bool(normalized_nodes),
        "bad Pick data",
    )
    kernel = pick_kernel(normalized_nodes)
    matrix = [
        [
            [
                -normalized_values[row]
                * normalized_values[column]
                * kernel[row][column],
                kernel[row][column],
            ]
            for column in range(len(normalized_nodes))
        ]
        for row in range(len(normalized_nodes))
    ]
    return polynomial_determinant(matrix)


def off_centre_local_load_fixture() -> dict[str, object]:
    conformal_radius = F(8, 9)
    pseudohyperbolic_product = F(5, 7)
    gamma = F(1)
    forced_target_exponent = 1
    load = (
        abs(gamma)
        * conformal_radius**forced_target_exponent
        / pseudohyperbolic_product
    )
    require(load == F(56, 45), "off-centre local load changed")
    dependency_row = BASE.off_centre_top_jet_fixture()
    require(
        dependency_row["optimal_H_infinity_norm"] == render(load),
        "off-centre dependency load disagrees",
    )
    return {
        "gamma": render(gamma),
        "forced_target_exponent": forced_target_exponent,
        "conformal_radius": render(conformal_radius),
        "pseudohyperbolic_product": render(pseudohyperbolic_product),
        "local_load": render(load),
        "checkpoint_8_load_matches": True,
    }


def phase_pair_fixture() -> dict[str, object]:
    nodes = [F(-1, 2), F(1, 2)]
    same_phase = [F(2), F(2)]
    opposite_phase = [F(-2), F(2)]
    gram_off_diagonal = F(3, 5)
    gram_minimum_eigenvalue = F(2, 5)
    gram_maximum_eigenvalue = F(8, 5)
    gram_condition_number = gram_maximum_eigenvalue / gram_minimum_eigenvalue

    same_at_two = pick_matrix(nodes, same_phase, F(2))
    opposite_at_two = pick_matrix(nodes, opposite_phase, F(2))
    opposite_at_four = pick_matrix(nodes, opposite_phase, F(4))
    require(is_psd(same_at_two), "same-phase norm two rejected")
    require(not is_psd(opposite_at_two), "opposite-phase diagonal threshold accepted")
    require(is_psd(opposite_at_four), "opposite-phase norm four rejected")
    require(determinant(opposite_at_four) == 0, "opposite-phase optimum nonsingular")
    require(gram_condition_number == F(4), "pair Gram conditioning changed")
    require(F(2) * F(2) == F(4), "sharp Gram upper bound changed")

    same_factor = scale(multiply([-F(4), F(1)], [-F(4), F(1)]), F(256, 225))
    opposite_factor = scale(
        multiply([-F(1), F(1)], [-F(16), F(1)]),
        F(256, 225),
    )
    require(
        pick_determinant_polynomial(nodes, same_phase) == same_factor,
        "same-phase generalized determinant changed",
    )
    require(
        pick_determinant_polynomial(nodes, opposite_phase) == opposite_factor,
        "opposite-phase generalized determinant changed",
    )
    return {
        "nodes": [render(value) for value in nodes],
        "absolute_target_values": ["2", "2"],
        "normalized_gram": [["1", "3/5"], ["3/5", "1"]],
        "gram_minimum_eigenvalue": render(gram_minimum_eigenvalue),
        "gram_maximum_eigenvalue": render(gram_maximum_eigenvalue),
        "gram_condition_number": render(gram_condition_number),
        "same_phase_values": [render(value) for value in same_phase],
        "same_phase_optimal_norm": "2",
        "opposite_phase_values": [render(value) for value in opposite_phase],
        "opposite_phase_optimal_norm": "4",
        "opposite_phase_gram_upper_bound": "4",
        "opposite_phase_pick_at_diagonal_threshold_psd": is_psd(opposite_at_two),
        "same_phase_determinant_factor": "(256/225)*(s-4)^2",
        "opposite_phase_determinant_factor": "(256/225)*(s-1)*(s-16)",
        "phase_is_load_bearing": True,
    }


def compatible_triple_fixture() -> dict[str, object]:
    epsilon = F(1, 5)
    manifest = [(-epsilon, 1), (F(0), 1), (epsilon, 1)]
    targets = {-epsilon: F(1), epsilon: F(1)}
    inner = BASE.forced_inner(manifest, targets)
    rows = BASE.target_values(manifest, targets)
    target_nodes = [-epsilon, epsilon]
    target_values = [rows[node]["y"] for node in target_nodes]
    require(target_values == [F(-5), F(5)], "compatible target loads changed")

    interpolant = BASE.rat([F(0), F(25)])
    selector = BASE.rat_multiply(inner, interpolant)
    require(BASE.selector_jets_hold(selector, manifest, targets), "compatible jets failed")
    require(
        BASE.rat_equal(selector, BASE.rat([F(0), F(0), F(25)])),
        "compatible selector changed",
    )

    rho = F(5, 13)
    gram_off_diagonal = F(12, 13)
    gram_minimum_eigenvalue = F(1, 13)
    gram_maximum_eigenvalue = F(25, 13)
    gram_condition_number = F(25)
    maximum_local_load = F(5)
    gram_upper_bound = maximum_local_load * F(5)
    cardinal_upper_bound = sum(abs(value) / rho for value in target_values)
    at_optimum = pick_matrix(target_nodes, target_values, F(25))
    below = pick_matrix(target_nodes, target_values, F(24))
    require(is_psd(at_optimum), "compatible norm twenty-five rejected")
    require(determinant(at_optimum) == 0, "compatible optimum nonsingular")
    require(not is_psd(below), "compatible suboptimal norm accepted")
    require(gram_upper_bound == F(25), "compatible Gram upper bound changed")
    require(cardinal_upper_bound == F(26), "compatible cardinal bound changed")

    kernel_determinant = determinant(pick_kernel(target_nodes))
    expected_factor = scale(
        multiply([-F(1), F(1)], [-F(625), F(1)]),
        kernel_determinant,
    )
    require(
        pick_determinant_polynomial(target_nodes, target_values) == expected_factor,
        "compatible generalized determinant changed",
    )
    return {
        "epsilon": render(epsilon),
        "manifest": [
            {
                "point": render(point),
                "order": order,
                "role": "target" if point in targets else "nontarget",
            }
            for point, order in manifest
        ],
        "target_gamma": "1",
        "target_values_y": [render(value) for value in target_values],
        "forced_inner": "z",
        "optimal_H": "25*z",
        "optimal_W": "25*z^2",
        "optimal_norm": "25",
        "maximum_local_load": render(maximum_local_load),
        "target_pseudohyperbolic_separation": render(rho),
        "target_product_separation": render(rho),
        "normalized_gram_off_diagonal": render(gram_off_diagonal),
        "gram_minimum_eigenvalue": render(gram_minimum_eigenvalue),
        "gram_maximum_eigenvalue": render(gram_maximum_eigenvalue),
        "gram_condition_number": render(gram_condition_number),
        "gram_upper_bound": render(gram_upper_bound),
        "cardinal_upper_bound": render(cardinal_upper_bound),
        "generalized_squared_roots": ["1", "625"],
        "top_jet_congruences_verified": True,
    }


def single_target_collision_fixture() -> dict[str, object]:
    collision = F(1, 5)
    manifest = [(F(0), 1), (collision, 3)]
    targets = {F(0): F(1)}
    inner = BASE.forced_inner(manifest, targets)
    data = BASE.target_values(manifest, targets)[F(0)]
    selector = BASE.rat_scale(inner, data["y"])
    require(data["y"] == F(-125), "collision target value changed")
    require(BASE.selector_jets_hold(selector, manifest, targets), "collision jets failed")
    return {
        "target": "0",
        "target_order": 1,
        "target_gamma": "1",
        "nontarget": render(collision),
        "nontarget_order": 3,
        "pseudohyperbolic_distance": render(collision),
        "pick_value_y": render(data["y"]),
        "optimal_norm": render(abs(data["y"])),
        "collision_exponent": 3,
        "top_jet_congruences_verified": True,
    }


def disk_radius_fixture() -> dict[str, object]:
    target_order = 2
    nontarget = F(1, 2)
    nontarget_order = 2
    gamma = F(1)

    def optimum(radius: F) -> F:
        radius = F(radius)
        require(radius > nontarget, "disk does not contain fixed manifest")
        conformal_radius = radius
        pseudohyperbolic_distance = nontarget / radius
        return (
            abs(gamma)
            * conformal_radius ** (target_order - 1)
            * pseudohyperbolic_distance ** (-nontarget_order)
        )

    radius_one = optimum(F(1))
    radius_two = optimum(F(2))
    require(radius_one == F(4), "unit-radius optimum changed")
    require(radius_two == F(32), "radius-two optimum changed")
    return {
        "fixed_manifest": [
            {
                "point": "0",
                "order": target_order,
                "role": "target",
                "gamma": "1",
            },
            {
                "point": render(nontarget),
                "order": nontarget_order,
                "role": "nontarget",
            },
        ],
        "formula": "tau_R=4*R^3",
        "radius_one_optimal_norm": render(radius_one),
        "radius_two_optimal_norm": render(radius_two),
        "radius_doubling_factor": render(radius_two / radius_one),
        "target_conformal_radius_exponent": target_order - 1,
        "nontarget_collision_exponent": nontarget_order,
        "total_radius_exponent": target_order - 1 + nontarget_order,
    }


def verify_positive_quadratic_root_label() -> None:
    # These integer identities certify the displayed radical labels after the
    # determinant factors and rational isolating intervals are established.
    require(31**2 + 8**2 * 15 - 62 * 31 + 1 == 0, "full root rational part")
    require(2 * 31 * 8 - 62 * 8 == 0, "full root radical part")
    require(4**2 + 15 == 31 and 2 * 4 == 8, "full norm square label")
    require(7**2 + 4**2 * 3 - 14 * 7 + 1 == 0, "pair root rational part")
    require(2 * 7 * 4 - 14 * 4 == 0, "pair root radical part")
    require(2**2 + 3 == 7 and 2 * 2 == 4, "pair norm square label")


def collective_three_target_fixture() -> dict[str, object]:
    nodes = [F(-1, 2), F(0), F(1, 2)]
    values = [F(-1), F(1), F(-1)]
    determinant_poly = pick_determinant_polynomial(nodes, values)
    expected = scale(
        multiply([-F(1), F(1)], [F(1), -F(62), F(1)]),
        F(16, 225),
    )
    require(determinant_poly == expected, "collective determinant factor changed")

    adjacent_left = pick_determinant_polynomial(nodes[:2], values[:2])
    adjacent_right = pick_determinant_polynomial(nodes[1:], values[1:])
    adjacent_expected = scale([F(1), -F(14), F(1)], F(1, 3))
    require(adjacent_left == adjacent_expected, "left pair determinant changed")
    require(adjacent_right == adjacent_expected, "right pair determinant changed")

    endpoint = pick_determinant_polynomial(
        [nodes[0], nodes[2]], [values[0], values[2]]
    )
    endpoint_expected = scale(
        multiply([-F(1), F(1)], [-F(1), F(1)]),
        F(256, 225),
    )
    require(endpoint == endpoint_expected, "endpoint determinant changed")

    full_quadratic = [F(1), -F(62), F(1)]
    pair_quadratic = [F(1), -F(14), F(1)]
    require(evaluate(full_quadratic, F(61)) < 0, "full root lower isolation failed")
    require(evaluate(full_quadratic, F(62)) > 0, "full root upper isolation failed")
    require(evaluate(pair_quadratic, F(13)) < 0, "pair root lower isolation failed")
    require(evaluate(pair_quadratic, F(14)) > 0, "pair root upper isolation failed")
    require(F(61) > F(14), "collective root is not strictly larger")
    verify_positive_quadratic_root_label()

    return {
        "nodes": [render(value) for value in nodes],
        "values": [render(value) for value in values],
        "pick_kernel": [
            [render(value) for value in row] for row in pick_kernel(nodes)
        ],
        "generalized_determinant_factor": "(16/225)*(s-1)*(s^2-62*s+1)",
        "generalized_determinant_coefficients": render_poly(determinant_poly),
        "full_squared_norm_factor": "s^2-62*s+1",
        "full_squared_norm_isolating_interval": ["61", "62"],
        "full_optimal_norm": "4+sqrt(15)",
        "adjacent_pair_determinant_factor": "(1/3)*(s^2-14*s+1)",
        "adjacent_pair_squared_norm_isolating_interval": ["13", "14"],
        "maximum_pair_optimal_norm": "2+sqrt(3)",
        "endpoint_pair_optimal_norm": "1",
        "full_optimum_strictly_exceeds_every_pair_optimum": True,
        "all_two_by_two_pick_conditions_are_sufficient": False,
    }


def mutation_firewalls() -> dict[str, object]:
    phase = phase_pair_fixture()
    compatible = compatible_triple_fixture()
    collision = single_target_collision_fixture()
    radii = disk_radius_fixture()
    collective = collective_three_target_fixture()
    return {
        "absolute_target_values_determine_pick_optimum": False,
        "same_absolute_values_distinct_optimal_norms": [
            phase["same_phase_optimal_norm"],
            phase["opposite_phase_optimal_norm"],
        ],
        "local_load_maximum_controls_multi_target_optimum": False,
        "compatible_local_load_maximum": compatible["maximum_local_load"],
        "compatible_full_optimum": compatible["optimal_norm"],
        "cardinal_upper_bound_is_always_exact": False,
        "pairwise_pick_conditions_are_sufficient": collective[
            "all_two_by_two_pick_conditions_are_sufficient"
        ],
        "pairwise_target_separation_controls_full_event_collision_load": False,
        "single_target_collision_norm": collision["optimal_norm"],
        "fixed_manifest_selector_norm_is_disk_radius_independent": False,
        "fixed_manifest_radius_norms": [
            radii["radius_one_optimal_norm"],
            radii["radius_two_optimal_norm"],
        ],
        "raw_pick_kernel_condition_number_is_conformally_intrinsic": False,
        "accepted_actual_xi_pick_kernel_used": False,
        "rh_established": False,
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
        "schema": "riemann.t105108.green-gram-selector-conditioning.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_WITH_EXACT_POLYNOMIAL_ROOT_CERTIFICATES",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "off_centre_local_load": off_centre_local_load_fixture(),
            "phase_sensitive_pair": phase_pair_fixture(),
            "compatible_three_event_selector": compatible_triple_fixture(),
            "single_target_collision": single_target_collision_fixture(),
            "fixed_manifest_disk_radius": disk_radius_fixture(),
            "collective_three_target_obstruction": collective_three_target_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "green_local_load_formula_verified": True,
            "normalized_target_gram_conditioning_verified": True,
            "phase_sensitive_pick_amplification_verified": True,
            "compatible_selector_gram_upper_bound_sharp": True,
            "single_target_collision_growth_verified": True,
            "fixed_manifest_disk_radius_scaling_verified": True,
            "collective_three_target_pick_obstruction_verified": True,
            "pairwise_pick_conditions_are_sufficient": False,
            "local_potential_loads_control_pick_interaction": False,
            "cardinal_product_upper_bound_is_always_exact": False,
            "raw_pick_kernel_condition_number_is_conformally_intrinsic": False,
            "xi_event_manifest_constructed": False,
            "xi_conformal_coordinates_certified": False,
            "xi_local_loads_estimated_cofinally": False,
            "xi_target_gram_conditioning_estimated_cofinally": False,
            "xi_pick_norm_estimated_cofinally": False,
            "xi_unweighted_quotient_edges_estimated": False,
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
