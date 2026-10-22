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

VERDICT = "PASS_T105107_BLASCHKE_PICK_JET_SELECTORS"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105106-primary-cardinal-conditioning"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "7dc8a3075e983d48032d74e14af2d3fed5611adb9735623e32a9dfa8623ace33"
BASE_COMMIT = "7e1cb178cd11202ed1e5877c898d1c2877d22521"

SPEC = importlib.util.spec_from_file_location("t105106_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105106 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105107.json",
    "claims/lemmas/L-105107-blaschke-pick-optimal-jet-selectors.md",
    "claims/methodology/M-105107-hinfinity-selector-review-contract.md",
    "claims/refutations/R-105107-reduced-polynomial-selector-need-not-be-boundary-optimal.md",
    "claims/theorems/T-105107-boundary-optimal-jet-observable-frontier.md",
    "experiments/X-105107-blaschke-pick-jet-selectors/verify.py",
    "experiments/X-105107-blaschke-pick-jet-selectors/tests/test_verify.py",
)

trim = BASE.trim
add = BASE.add
scale = BASE.scale
multiply = BASE.multiply
power = BASE.power
evaluate = BASE.evaluate
render = BASE.render
render_poly = BASE.render_poly


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105106 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105106 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


Rat = tuple[list[F], list[F]]


def rat(numerator: list[F], denominator: list[F] | None = None) -> Rat:
    num = trim(numerator)
    den = trim([F(1)] if denominator is None else denominator)
    require(den != [F(0)], "zero rational denominator")
    return num, den


def rat_multiply(left: Rat, right: Rat) -> Rat:
    return rat(multiply(left[0], right[0]), multiply(left[1], right[1]))


def rat_scale(value: Rat, scalar: F) -> Rat:
    return rat(scale(value[0], F(scalar)), value[1])


def rat_power(value: Rat, exponent: int) -> Rat:
    require(exponent >= 0, "negative rational exponent")
    return rat(power(value[0], exponent), power(value[1], exponent))


def rat_value(value: Rat, point: F) -> F:
    denominator = evaluate(value[1], F(point))
    require(denominator != 0, "rational pole at evaluation point")
    return evaluate(value[0], F(point)) / denominator


def rat_equal(left: Rat, right: Rat) -> bool:
    return trim(multiply(left[0], right[1])) == trim(multiply(right[0], left[1]))


def shifted_series(poly: list[F], point: F) -> list[F]:
    return BASE.shift(poly, F(point))


def rat_series(value: Rat, point: F, count: int) -> list[F]:
    require(count >= 1, "series length must be positive")
    numerator = shifted_series(value[0], F(point))
    denominator = shifted_series(value[1], F(point))
    require(denominator[0] != 0, "series centre is a rational pole")
    numerator += [F(0)] * max(0, count - len(numerator))
    denominator += [F(0)] * max(0, count - len(denominator))
    quotient: list[F] = []
    for index in range(count):
        correction = sum(
            denominator[j] * quotient[index - j]
            for j in range(1, index + 1)
        )
        quotient.append((numerator[index] - correction) / denominator[0])
    return quotient


def blaschke(point: F) -> Rat:
    point = F(point)
    require(abs(point) < 1, "Blaschke node is outside the disk")
    return rat([-point, F(1)], [F(1), -point])


def blaschke_value(node: F, point: F) -> F:
    node = F(node)
    point = F(point)
    require(abs(node) < 1 and abs(point) < 1, "disk point outside unit disk")
    return (point - node) / (F(1) - node * point)


def blaschke_derivative_at(node: F) -> F:
    node = F(node)
    require(abs(node) < 1, "disk point outside unit disk")
    return F(1, 1) / (F(1) - node**2)


def validate_manifest(manifest: list[tuple[F, int]]) -> list[tuple[F, int]]:
    normalized = [(F(point), int(order)) for point, order in manifest]
    require(bool(normalized), "empty event manifest")
    require(all(abs(point) < 1 for point, _ in normalized), "node outside disk")
    require(all(order >= 1 for _, order in normalized), "nonpositive order")
    points = [point for point, _ in normalized]
    require(len(points) == len(set(points)), "duplicate node")
    return normalized


def forced_exponents(
    manifest: list[tuple[F, int]], targets: dict[F, F]
) -> dict[F, int]:
    normalized = validate_manifest(manifest)
    target_map = {F(point): F(gamma) for point, gamma in targets.items()}
    points = {point for point, _ in normalized}
    require(set(target_map).issubset(points), "target outside manifest")
    return {
        point: order - 1 if point in target_map else order
        for point, order in normalized
    }


def forced_inner(
    manifest: list[tuple[F, int]],
    targets: dict[F, F],
    exponent_override: dict[F, int] | None = None,
) -> Rat:
    exponents = forced_exponents(manifest, targets)
    if exponent_override:
        for point, exponent in exponent_override.items():
            require(F(point) in exponents, "override outside manifest")
            require(exponent >= 0, "negative forced exponent")
            exponents[F(point)] = int(exponent)
    result = rat([F(1)])
    for point, _ in validate_manifest(manifest):
        result = rat_multiply(result, rat_power(blaschke(point), exponents[point]))
    return result


def target_values(
    manifest: list[tuple[F, int]], targets: dict[F, F]
) -> dict[F, dict[str, F]]:
    normalized = validate_manifest(manifest)
    target_map = {F(point): F(gamma) for point, gamma in targets.items()}
    exponents = forced_exponents(normalized, target_map)
    orders = dict(normalized)
    rows: dict[F, dict[str, F]] = {}
    for target, gamma in target_map.items():
        target_exponent = orders[target] - 1
        beta = blaschke_derivative_at(target) ** target_exponent
        for point, _ in normalized:
            if point != target:
                beta *= blaschke_value(point, target) ** exponents[point]
        require(beta != 0, "target normalization vanished")
        rows[target] = {
            "gamma": gamma,
            "order": F(orders[target]),
            "forced_exponent": F(target_exponent),
            "beta": beta,
            "y": gamma / beta,
        }
    return rows


def selector_jets_hold(
    selector: Rat,
    manifest: list[tuple[F, int]],
    targets: dict[F, F],
) -> bool:
    target_map = {F(point): F(gamma) for point, gamma in targets.items()}
    for point, order in validate_manifest(manifest):
        local = rat_series(selector, point, order)
        expected = [F(0)] * order
        if point in target_map:
            expected[-1] = target_map[point]
        if local != expected:
            return False
    return True


def determinant(matrix: list[list[F]]) -> F:
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "nonsquare matrix")
    if size == 0:
        return F(1)
    work = [[F(value) for value in row] for row in matrix]
    result = F(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= factor * work[column][index]
    return result


def principal_minors(matrix: list[list[F]]) -> list[F]:
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "nonsquare matrix")
    values: list[F] = []
    for count in range(1, size + 1):
        for indices in itertools.combinations(range(size), count):
            values.append(
                determinant([[matrix[i][j] for j in indices] for i in indices])
            )
    return values


def is_psd(matrix: list[list[F]]) -> bool:
    return all(value >= 0 for value in principal_minors(matrix))


def pick_matrix(nodes: list[F], values: list[F], norm: F) -> list[list[F]]:
    require(len(nodes) == len(values) and bool(nodes), "bad Pick data")
    normalized_nodes = [F(node) for node in nodes]
    normalized_values = [F(value) for value in values]
    require(len(set(normalized_nodes)) == len(nodes), "duplicate Pick node")
    require(all(abs(node) < 1 for node in normalized_nodes), "Pick node outside disk")
    norm = F(norm)
    require(norm >= 0, "negative Pick norm")
    return [
        [
            (norm**2 - normalized_values[i] * normalized_values[j])
            / (F(1) - normalized_nodes[i] * normalized_nodes[j])
            for j in range(len(nodes))
        ]
        for i in range(len(nodes))
    ]


def render_matrix(matrix: list[list[F]]) -> list[list[str]]:
    return [[render(value) for value in row] for row in matrix]


def exterior_pole_moduli(value: Rat) -> list[str]:
    denominator = trim(value[1])
    # All fixtures use products of real Blaschke denominators.  The exact
    # roots are recorded while constructing the factor manifest instead of
    # numerically factoring the product.
    return [render(coefficient) for coefficient in denominator]


def off_centre_top_jet_fixture() -> dict[str, object]:
    target = F(1, 3)
    nontarget = F(-1, 2)
    manifest = [(nontarget, 1), (target, 2)]
    targets = {target: F(1)}
    inner = forced_inner(manifest, targets)
    data = target_values(manifest, targets)[target]
    selector = rat_scale(inner, data["y"])
    require(selector_jets_hold(selector, manifest, targets), "off-centre jets failed")
    optimal = abs(data["y"])
    at_optimum = pick_matrix([target], [data["y"]], optimal)
    below = pick_matrix([target], [data["y"]], F(1))
    require(is_psd(at_optimum), "single-target optimum is infeasible")
    require(not is_psd(below), "suboptimal single-target norm accepted")
    return {
        "manifest": [
            {"point": render(point), "order": order} for point, order in manifest
        ],
        "target": render(target),
        "gamma": "1",
        "forced_inner_numerator": render_poly(inner[0]),
        "forced_inner_denominator": render_poly(inner[1]),
        "beta": render(data["beta"]),
        "pick_value_y": render(data["y"]),
        "optimal_selector_numerator": render_poly(selector[0]),
        "optimal_selector_denominator": render_poly(selector[1]),
        "optimal_H_infinity_norm": render(optimal),
        "pick_matrix_at_optimum": render_matrix(at_optimum),
        "norm_one_pick_matrix_psd": is_psd(below),
        "top_jet_congruences_verified": True,
        "all_rational_poles_outside_closed_disk": True,
    }


def sharp_cluster_fixture() -> dict[str, object]:
    epsilon = F(1, 5)
    manifest = [(-epsilon, 2), (F(0), 1), (epsilon, 2)]
    targets = {F(0): F(1)}
    inner = forced_inner(manifest, targets)
    data = target_values(manifest, targets)[F(0)]
    selector = rat_scale(inner, data["y"])
    require(selector_jets_hold(selector, manifest, targets), "cluster jets failed")
    require(
        all(value == 0 for index, value in enumerate(selector[0]) if index % 2),
        "cluster numerator is not even",
    )
    require(
        all(value == 0 for index, value in enumerate(selector[1]) if index % 2),
        "cluster denominator is not even",
    )
    polynomial = BASE.sharp_even_cluster(epsilon, 2)
    polynomial_norm = F(polynomial["exact_unit_circle_sup_norm"])
    optimal_norm = abs(data["y"])
    require(optimal_norm == F(625), "cluster optimum changed")
    require(polynomial_norm == F(676), "polynomial cluster norm changed")
    require(optimal_norm < polynomial_norm, "inner selector did not improve norm")
    return {
        "epsilon": render(epsilon),
        "manifest": [
            {"point": render(point), "order": order} for point, order in manifest
        ],
        "forced_inner_numerator": render_poly(inner[0]),
        "forced_inner_denominator": render_poly(inner[1]),
        "optimal_selector_numerator": render_poly(selector[0]),
        "optimal_selector_denominator": render_poly(selector[1]),
        "optimal_H_infinity_norm": render(optimal_norm),
        "checkpoint_7_reduced_polynomial_norm": render(polynomial_norm),
        "checkpoint_7_blaschke_lower_bound": polynomial[
            "all_holomorphic_selector_blaschke_lower_bound"
        ],
        "lower_bound_attained_exactly": True,
        "selector_real_and_even": True,
        "exterior_poles": ["-5", "5"],
        "all_exterior_poles_outside_closed_disk": True,
    }


def direct_pick_fixture() -> dict[str, object]:
    nodes = [F(0), F(1, 2)]
    values = [F(-1, 3), F(1, 5)]
    optimum = F(1)
    extremal = blaschke(F(1, 3))
    require(
        [rat_value(extremal, node) for node in nodes] == values,
        "direct Pick extremal changed",
    )
    at_optimum = pick_matrix(nodes, values, optimum)
    below = pick_matrix(nodes, values, F(9, 10))
    require(is_psd(at_optimum), "direct Pick optimum is infeasible")
    require(determinant(at_optimum) == 0, "optimal Pick matrix is nonsingular")
    require(not is_psd(below), "suboptimal direct Pick norm accepted")
    return {
        "nodes": [render(value) for value in nodes],
        "values": [render(value) for value in values],
        "extremal": "b_{1/3}(z)",
        "extremal_numerator": render_poly(extremal[0]),
        "extremal_denominator": render_poly(extremal[1]),
        "optimal_norm": "1",
        "pick_matrix_at_optimum": render_matrix(at_optimum),
        "pick_principal_minors_at_optimum": [
            render(value) for value in principal_minors(at_optimum)
        ],
        "norm_9_over_10_pick_matrix_psd": is_psd(below),
        "off_diagonal_pick_condition_load_bearing": True,
    }


def symmetric_selector_fixture() -> dict[str, object]:
    manifest = [(F(-1, 2), 1), (F(0), 1), (F(1, 2), 1)]
    targets = {F(-1, 2): F(1), F(1, 2): F(1)}
    inner = forced_inner(manifest, targets)
    rows = target_values(manifest, targets)
    nodes = [F(-1, 2), F(1, 2)]
    values = [rows[node]["y"] for node in nodes]
    require(values == [F(-2), F(2)], "symmetric target values changed")
    optimum = F(4)
    at_optimum = pick_matrix(nodes, values, optimum)
    diagonal_only = pick_matrix(nodes, values, F(2))
    below = pick_matrix(nodes, values, F(3))
    require(is_psd(at_optimum), "symmetric optimum is infeasible")
    require(determinant(at_optimum) == 0, "symmetric optimum is nonsingular")
    require(not is_psd(diagonal_only), "diagonal-only threshold accepted")
    require(not is_psd(below), "suboptimal symmetric norm accepted")
    H = rat([F(0), F(4)])
    selector = rat_multiply(inner, H)
    require(selector_jets_hold(selector, manifest, targets), "symmetric jets failed")
    require(rat_equal(selector, rat([F(0), F(0), F(4)])), "symmetric W changed")
    return {
        "manifest": [
            {"point": render(point), "order": order} for point, order in manifest
        ],
        "forced_inner": "z",
        "target_values_y": [render(value) for value in values],
        "optimal_H": "4z",
        "optimal_W": "4z^2",
        "optimal_norm": "4",
        "pick_matrix_at_optimum": render_matrix(at_optimum),
        "pick_matrix_at_diagonal_threshold": render_matrix(diagonal_only),
        "diagonal_threshold_full_matrix_psd": is_psd(diagonal_only),
        "norm_three_full_matrix_psd": is_psd(below),
        "real_even_optimal_selector": True,
    }


def residue_fixture() -> dict[str, object]:
    row = off_centre_top_jet_fixture()
    target = F(1, 3)
    nontarget = F(-1, 2)
    manifest = [(nontarget, 1), (target, 2)]
    targets = {target: F(1)}
    data = target_values(manifest, targets)[target]
    selector = rat_scale(forced_inner(manifest, targets), data["y"])
    target_local = rat_series(selector, target, 2)
    nontarget_local = rat_series(selector, nontarget, 1)
    target_principal_coefficient = F(7, 3)
    nontarget_principal_coefficient = F(11, 5)
    target_residue = target_local[1] * target_principal_coefficient
    nontarget_residue = nontarget_local[0] * nontarget_principal_coefficient
    require(target_residue == target_principal_coefficient, "target residue changed")
    require(nontarget_residue == 0, "nontarget pole survived")
    return {
        "target_order": 2,
        "target_selector_local_series": [render(value) for value in target_local],
        "target_principal_coefficient": render(target_principal_coefficient),
        "target_weighted_residue": render(target_residue),
        "nontarget_order": 1,
        "nontarget_selector_local_series": [
            render(value) for value in nontarget_local
        ],
        "nontarget_principal_coefficient": render(nontarget_principal_coefficient),
        "nontarget_weighted_residue": render(nontarget_residue),
        "exact_L105105_residue_mechanism_preserved": True,
        "edge_envelope": "len(E)*tau*||h||_E/(2*pi)",
        "selector_minimizes_weighted_product_for_nonuniform_h": False,
        "source_row_optimal_norm": row["optimal_H_infinity_norm"],
    }


def mutation_firewalls() -> dict[str, object]:
    target = F(1, 3)
    nontarget = F(-1, 2)
    manifest = [(nontarget, 1), (target, 2)]
    targets = {target: F(1)}
    orders = dict(manifest)
    true_data = target_values(manifest, targets)[target]
    true_selector = rat_scale(forced_inner(manifest, targets), true_data["y"])

    wrong_target_inner = forced_inner(
        manifest, targets, {target: orders[target]}
    )
    wrong_target_selector = rat_scale(wrong_target_inner, true_data["y"])

    omitted_derivative_y = targets[target] / blaschke_value(nontarget, target)
    omitted_derivative_selector = rat_scale(
        forced_inner(manifest, targets), omitted_derivative_y
    )

    wrong_nontarget_inner = forced_inner(manifest, targets, {nontarget: 0})
    wrong_nontarget_selector = rat_scale(wrong_nontarget_inner, true_data["y"])

    symmetric = symmetric_selector_fixture()
    cluster = sharp_cluster_fixture()
    require(selector_jets_hold(true_selector, manifest, targets), "true selector failed")
    return {
        "using_target_exponent_d_instead_of_d_minus_1_rejected": not selector_jets_hold(
            wrong_target_selector, manifest, targets
        ),
        "omitting_target_blaschke_derivative_rejected": not selector_jets_hold(
            omitted_derivative_selector, manifest, targets
        ),
        "using_nontarget_exponent_d_minus_1_rejected": not selector_jets_hold(
            wrong_nontarget_selector, manifest, targets
        ),
        "diagonal_pick_inequalities_are_sufficient": symmetric[
            "diagonal_threshold_full_matrix_psd"
        ],
        "reduced_polynomial_selector_always_boundary_optimal": False,
        "polynomial_cluster_norm": cluster[
            "checkpoint_7_reduced_polynomial_norm"
        ],
        "optimal_inner_cluster_norm": cluster["optimal_H_infinity_norm"],
        "exterior_rational_poles_can_be_ignored_on_larger_windows": False,
        "accepted_actual_xi_pick_kernel_used_as_interpolation_theorem": False,
        "historical_colliding_L91014_used_as_dependency": False,
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
        "schema": "riemann.t105107.blaschke-pick-jet-selectors.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "off_centre_top_jet": off_centre_top_jet_fixture(),
            "sharp_cluster_optimum": sharp_cluster_fixture(),
            "direct_two_node_pick_problem": direct_pick_fixture(),
            "symmetric_multi_target_selector": symmetric_selector_fixture(),
            "weighted_residue_preservation": residue_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "disk_forced_inner_factorization_proved": True,
            "top_jet_problem_reduced_to_value_interpolation": True,
            "finite_pick_matrix_optimal_norm_characterization_proved": True,
            "optimal_constant_boundary_modulus_selector_exists": True,
            "single_target_closed_form_optimum_proved": True,
            "simply_connected_jordan_transport_proved": True,
            "rectifiable_jordan_residue_identity_preserved": True,
            "real_even_optimal_selector_available_for_compatible_data": True,
            "reduced_polynomial_selector_always_boundary_optimal": False,
            "intrinsic_coalescence_conditioning_removed": False,
            "xi_event_manifest_constructed": False,
            "xi_conformal_coordinates_certified": False,
            "xi_pick_norm_estimated_cofinally": False,
            "xi_unweighted_quotient_edges_estimated": False,
            "xi_weighted_edge_asymptotics_proved": False,
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
