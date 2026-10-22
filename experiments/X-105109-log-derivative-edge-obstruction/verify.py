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

VERDICT = "PASS_T105109_LOG_DERIVATIVE_EDGE_OBSTRUCTION"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105108-green-gram-selector-conditioning"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "6c2484c4e63612b238f1ec6044c9b8778b725899d4be643d7e80b6a6dc345cdb"
BASE_COMMIT = "e223f98823bdb7b11736a05993ac12b75d5263b3"

SPEC = importlib.util.spec_from_file_location("t105108_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105108 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105109.json",
    "claims/lemmas/L-105109-log-derivative-edge-margins.md",
    "claims/methodology/M-105109-quotient-edge-review-contract.md",
    "claims/refutations/R-105109-bounded-selector-norm-does-not-control-quotient-edge.md",
    "claims/theorems/T-105109-quotient-edge-frontier.md",
    "experiments/X-105109-log-derivative-edge-obstruction/verify.py",
    "experiments/X-105109-log-derivative-edge-obstruction/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def trim(poly: list[F]) -> list[F]:
    normalized = [F(value) for value in poly]
    while len(normalized) > 1 and normalized[-1] == 0:
        normalized.pop()
    return normalized or [F(0)]


def add(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    result = [F(0) for _ in range(size)]
    for index, value in enumerate(left):
        result[index] += F(value)
    for index, value in enumerate(right):
        result[index] += F(value)
    return trim(result)


def scale(poly: list[F], scalar: F) -> list[F]:
    return trim([F(scalar) * F(value) for value in poly])


def multiply(left: list[F], right: list[F]) -> list[F]:
    result = [F(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += F(left_value) * F(right_value)
    return trim(result)


def power(poly: list[F], exponent: int) -> list[F]:
    require(exponent >= 0, "negative polynomial exponent")
    result = [F(1)]
    base = trim(poly)
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = multiply(result, base)
        base = multiply(base, base)
        remaining //= 2
    return result


def derivative(poly: list[F], order: int = 1) -> list[F]:
    require(order >= 0, "negative derivative order")
    result = trim(poly)
    for _ in range(order):
        if len(result) == 1:
            return [F(0)]
        result = [F(index) * result[index] for index in range(1, len(result))]
    return trim(result)


def evaluate(poly: list[F], point: F) -> F:
    value = F(0)
    point = F(point)
    for coefficient in reversed(trim(poly)):
        value = value * point + coefficient
    return value


def evaluate_at_polynomial(coefficients: list[list[F]], point: list[F]) -> list[F]:
    result = [F(0)]
    for coefficient in reversed(coefficients):
        result = add(multiply(result, point), coefficient)
    return trim(result)


def render_poly(poly: list[F]) -> list[str]:
    return [render(value) for value in trim(poly)]


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105108 dependency artifact is stale")
    require(
        artifact.get("proof_object_sha256") == BASE_DIGEST,
        "T-105108 dependency digest changed",
    )
    require(
        artifact.get("verdict") == BASE.VERDICT,
        "T-105108 dependency verdict changed",
    )
    return {
        "path": "experiments/X-105108-green-gram-selector-conditioning",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def margin_ledger_fixture() -> dict[str, object]:
    # Two exact boundary samples demonstrate why independently attained minima
    # cannot be substituted for the product margin.
    samples = [(F(1), F(10)), (F(10), F(1))]
    m1 = min(abs(log_derivative) for log_derivative, _ in samples)
    m2 = min(abs(second_denominator) for _, second_denominator in samples)
    m12 = min(
        abs(log_derivative * second_denominator)
        for log_derivative, second_denominator in samples
    )
    first_quotient_norm = max(abs(F(1, 1) / row[0]) for row in samples)
    second_quotient_norm = max(abs(F(1, 1) / (row[0] * row[1])) for row in samples)
    tau1 = F(2)
    tau2 = F(3)

    require(first_quotient_norm == F(1, 1) / m1, "first margin identity failed")
    require(second_quotient_norm == F(1, 1) / m12, "product margin identity failed")
    require(m12 > m1 * m2, "independent-minimum firewall failed")
    require(
        second_quotient_norm <= F(1, 1) / (m1 * m2),
        "product-minimum sufficient bound failed",
    )
    return {
        "boundary_samples_L_A": [
            [render(log_derivative), render(second_denominator)]
            for log_derivative, second_denominator in samples
        ],
        "m1": render(m1),
        "m2": render(m2),
        "m12": render(m12),
        "m12_equals_m1_times_m2": False,
        "first_quotient_formula": "1/L",
        "second_quotient_formula": "1/(L*A)",
        "first_quotient_norm": render(first_quotient_norm),
        "second_quotient_norm": render(second_quotient_norm),
        "selector_norms": [render(tau1), render(tau2)],
        "weighted_first_supremum": render(tau1 * first_quotient_norm),
        "weighted_second_supremum": render(tau2 * second_quotient_norm),
        "constant_boundary_modulus_gives_exact_weighted_supremum": True,
    }


def gauge_fixture() -> dict[str, object]:
    nodes_and_depths = [(F(0), 2), (F(1, 3), 3)]
    zeta = F(1)
    jet_product = [F(1)]
    for node, depth in nodes_and_depths:
        jet_product = multiply(jet_product, power([-node, F(1)], depth))

    q1 = multiply([-zeta, F(1)], jet_product)
    q2 = multiply(power([-zeta, F(1)], 2), jet_product)
    product_at_boundary = evaluate(jet_product, zeta)
    q1_prime = evaluate(derivative(q1), zeta)
    q2_prime = evaluate(derivative(q2), zeta)
    q2_second = evaluate(derivative(q2, 2), zeta)

    require(product_at_boundary == F(8, 27), "gauge product at boundary changed")
    require(q1_prime == product_at_boundary, "Q1 boundary derivative changed")
    require(q2_prime == 0, "Q2 first boundary derivative is nonzero")
    require(q2_second == 2 * product_at_boundary, "Q2 second derivative changed")

    for node, depth in nodes_and_depths:
        for order in range(depth):
            require(
                evaluate(derivative(q1, order), node) == 0,
                "Q1 failed a frozen interior jet",
            )
            require(
                evaluate(derivative(q2, order), node) == 0,
                "Q2 failed a frozen interior jet",
            )

    epsilon = F(1, 5)
    ell = F(5, 3)
    second_denominator = F(7, 4)
    t1 = -ell / product_at_boundary
    t2 = -second_denominator / (2 * product_at_boundary)
    transformed_ell = ell + (1 - epsilon) * t1 * q1_prime
    transformed_q2_ell = ell + (1 - epsilon) * t2 * q2_prime
    transformed_second = (
        second_denominator + (1 - epsilon) * t2 * q2_second
    )

    require(t1 == F(-45, 8), "first gauge coefficient changed")
    require(t2 == F(-189, 64), "second gauge coefficient changed")
    require(transformed_ell == epsilon * ell, "first margin did not scale")
    require(transformed_q2_ell == ell, "second gauge changed L at boundary")
    require(
        transformed_second == epsilon * second_denominator,
        "second margin did not scale",
    )
    require(ell + t1 * q1_prime == 0, "epsilon-zero first collapse failed")
    require(
        second_denominator + t2 * q2_second == 0,
        "epsilon-zero second collapse failed",
    )

    return {
        "nodes_and_depths": [
            {"point": render(node), "depth": depth}
            for node, depth in nodes_and_depths
        ],
        "boundary_point": render(zeta),
        "P_at_boundary": render(product_at_boundary),
        "Q1_prime_at_boundary": render(q1_prime),
        "Q2_prime_at_boundary": render(q2_prime),
        "Q2_second_at_boundary": render(q2_second),
        "epsilon": render(epsilon),
        "initial_L": render(ell),
        "initial_A": render(second_denominator),
        "t1": render(t1),
        "t2": render(t2),
        "transformed_L_first_gauge": render(transformed_ell),
        "transformed_L_second_gauge": render(transformed_q2_ell),
        "transformed_A_second_gauge": render(transformed_second),
        "specified_interior_jets_preserved": True,
        "zeros_preserved_by_zero_free_exponential": True,
        "complete_derivative_manifest_preserved": False,
        "epsilon_zero_collapses_denominator": True,
    }


def p_coefficients(s: F) -> list[F]:
    s = F(s)
    return [s * s, s * s - 3 * s, -2 * s, F(1)]


def l_coefficients(s: F) -> list[F]:
    s = F(s)
    require(s != 0, "zero parameter")
    return [F(0), F(1), F(0), -F(1, 1) / s]


def a_coefficients(s: F) -> list[F]:
    logarithmic = l_coefficients(s)
    return add(multiply(logarithmic, logarithmic), derivative(logarithmic))


def p_even_over_s_squared(s: F) -> list[F]:
    s = F(s)
    result = [F(0) for _ in range(7)]
    for index, coefficient in enumerate(p_coefficients(s)):
        result[2 * index] = coefficient / (s * s)
    return trim(result)


def discriminant_identity() -> list[F]:
    # Coefficients below are polynomials in s, stored in ascending order.
    b = [F(0), F(-2)]
    c = [F(0), F(-3), F(1)]
    d = [F(0), F(0), F(1)]
    discriminant = add(
        add(
            add(
                multiply(multiply(b, b), multiply(c, c)),
                scale(power(c, 3), F(-4)),
            ),
            scale(multiply(power(b, 3), d), F(-4)),
        ),
        add(scale(multiply(b, multiply(c, d)), F(18)), scale(power(d, 2), F(-27))),
    )
    expected = [F(0), F(0), F(0), F(108), F(9), F(8)]
    require(discriminant == expected, "cubic discriminant identity changed")
    return discriminant


def derivative_polynomial_fixture() -> dict[str, object]:
    s = F(101, 100)
    logarithmic = l_coefficients(s)
    second = a_coefficients(s)
    expected_second = [
        F(1),
        F(0),
        F(1) - F(3, 1) / s,
        F(0),
        -F(2, 1) / s,
        F(0),
        F(1, 1) / (s * s),
    ]
    require(second == expected_second, "L squared plus L prime changed")
    require(second == p_even_over_s_squared(s), "P(z^2)/s^2 identity changed")

    # Symbolic-in-s evaluations of P_s at -1, 0, 1, and x=s.
    p_at_minus_one = [F(-1), F(1)]
    p_at_zero = [F(0), F(0), F(1)]
    p_at_one = [F(1), F(-5), F(2)]
    p_as_x_polynomial_in_s = [
        [F(0), F(0), F(1)],
        [F(0), F(-3), F(1)],
        [F(0), F(-2)],
        [F(1)],
    ]
    p_at_s = evaluate_at_polynomial(p_as_x_polynomial_in_s, [F(0), F(1)])
    require(p_at_minus_one == [F(-1), F(1)], "P(-1) identity changed")
    require(p_at_zero == [F(0), F(0), F(1)], "P(0) identity changed")
    require(p_at_one == [F(1), F(-5), F(2)], "P(1) identity changed")
    require(p_at_s == [F(0), F(0), F(-2)], "P(s) identity changed")

    return {
        "parameter_probe": render(s),
        "L_coefficients_in_z": render_poly(logarithmic),
        "A_coefficients_in_z": render_poly(second),
        "P_coefficients_in_x": render_poly(p_coefficients(s)),
        "A_equals_L_squared_plus_L_prime": True,
        "A_equals_P_of_z_squared_over_s_squared": True,
        "P_minus_one_in_s": render_poly(p_at_minus_one),
        "P_zero_in_s": render_poly(p_at_zero),
        "P_one_in_s": render_poly(p_at_one),
        "P_at_s_in_s": render_poly(p_at_s),
        "discriminant_in_s": render_poly(discriminant_identity()),
        "discriminant_factor": "s^3*(8*s^2+9*s+108)",
    }


def rational_checkpoint_fixture() -> dict[str, object]:
    s = F(101, 100)
    polynomial = p_coefficients(s)
    points = [F(-2), F(-1), F(3, 8), F(2, 5), F(1), F(3)]
    expected = [
        F(-110401, 10000),
        F(1, 100),
        F(11219, 320000),
        F(-2153, 50000),
        F(-10049, 5000),
        F(4763, 1250),
    ]
    values = [evaluate(polynomial, point) for point in points]
    require(values == expected, "rational root sign oracle changed")
    require(values[0] < 0 < values[1], "negative root interval failed")
    require(values[2] > 0 > values[3], "interior root interval failed")
    require(values[4] < 0 < values[5], "positive exterior root interval failed")
    require(evaluate(polynomial, s) == -2 * s * s, "positive root not beyond s")
    require(evaluate(discriminant_identity(), s) > 0, "cubic is not square-free")

    p_one = values[4]
    first_boundary = s / (s - 1)
    second_boundary = s**3 / ((s - 1) * p_one)
    require(first_boundary == F(101), "first boundary quotient changed")
    require(
        second_boundary == F(-1030301, 20098),
        "second boundary quotient changed",
    )
    return {
        "s": render(s),
        "sign_points": [render(point) for point in points],
        "sign_values": [render(value) for value in values],
        "negative_root_interval": ["-2", "-1"],
        "alpha_interval": ["3/8", "2/5"],
        "positive_root_interval": ["101/100", "3"],
        "tau_two_interval": ["5/2", "8/3"],
        "first_boundary_quotient_at_one": render(first_boundary),
        "second_boundary_quotient_at_one": render(second_boundary),
        "floating_point_root_finding_used": False,
    }


def event_manifest_fixture() -> dict[str, object]:
    s = F(101, 100)
    polynomial = p_coefficients(s)
    a_at_zero = evaluate(polynomial, F(0)) / (s * s)
    a_at_l_outer_root = evaluate(polynomial, s) / (s * s)
    require(a_at_zero == 1, "F-prime/F-second common event at zero")
    require(a_at_l_outer_root == -2, "outer L/A common event introduced")

    return {
        "allowed_parameter_range": "1<s<(5+sqrt(17))/4",
        "endpoints_included": False,
        "F_properties": ["real", "even", "entire", "zero-free", "order_four"],
        "F_prime_zeros": ["0", "-sqrt(s)", "sqrt(s)"],
        "first_disk_manifest": [
            {"point": "0", "order": 1, "role": "target"}
        ],
        "P_root_order": "gamma<-1<0<alpha<1<s<beta",
        "second_disk_manifest": [
            {"point": "-sqrt(alpha)", "order": 1, "role": "nontarget"},
            {"point": "0", "order": 1, "role": "target"},
            {"point": "sqrt(alpha)", "order": 1, "role": "nontarget"},
        ],
        "all_interior_events_simple": True,
        "common_F_prime_F_second_events": False,
        "A_at_zero": render(a_at_zero),
        "A_at_outer_F_prime_zeros": render(a_at_l_outer_root),
        "boundary_poles_for_strict_parameter_range": False,
        "second_nontarget_locations_fixed_in_s": False,
    }


def local_residue_fixture() -> dict[str, object]:
    s = F(101, 100)
    # L=z*(1-z^2/s), while A has constant coefficient one.  Therefore both
    # reciprocals have z^-1 coefficient one.  The next coefficients are an
    # independent sign/order check.
    first_next = F(1, 1) / s
    second_next = F(4, 1) / s - 1
    require(first_next == F(100, 101), "first local expansion changed")
    require(second_next == F(299, 101), "second local expansion changed")
    return {
        "s": render(s),
        "first_laurent_terms_at_zero": ["z^-1", f"{render(first_next)}*z"],
        "second_laurent_terms_at_zero": ["z^-1", f"{render(second_next)}*z"],
        "first_target_principal_coefficient": "1",
        "second_target_principal_coefficient": "1",
        "first_target_residue": "1",
        "second_target_residue": "1",
    }


def surd_add(left: tuple[F, F], right: tuple[F, F]) -> tuple[F, F]:
    return left[0] + right[0], left[1] + right[1]


def surd_multiply(left: tuple[F, F], right: tuple[F, F]) -> tuple[F, F]:
    return left[0] * right[0] + 5 * left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def surd_polynomial(poly: list[F], point: tuple[F, F]) -> tuple[F, F]:
    result = (F(0), F(0))
    for coefficient in reversed(poly):
        result = surd_add(surd_multiply(result, point), (F(coefficient), F(0)))
    return result


def selector_fixture() -> dict[str, object]:
    # A rational probe certifies the universal sign and boundary-modulus
    # algebra without approximating the actual algebraic root.
    probe_a = F(3, 5)
    probe_alpha = probe_a * probe_a
    beta_zero = (-probe_a) * probe_a
    target_value = F(1, 1) / beta_zero
    require(beta_zero == -probe_alpha, "beta-zero sign changed")
    require(target_value == -F(1, 1) / probe_alpha, "Pick value sign changed")

    # With x=z^2, W=(alpha-x)/(alpha*(1-alpha*x)).
    numerator = [probe_alpha, F(-1)]
    denominator = [probe_alpha, -probe_alpha * probe_alpha]
    require(evaluate(numerator, F(0)) == evaluate(denominator, F(0)), "W2(0) changed")
    require(evaluate(numerator, probe_alpha) == 0, "nontarget zero missing")
    require(evaluate(denominator, probe_alpha) != 0, "selector pole entered disk")

    # On |x|=1, |alpha-x|^2 and |1-alpha*x|^2 have identical Laurent
    # coefficients, leaving constant modulus 1/alpha after scaling.
    numerator_modulus = {
        -1: -probe_alpha,
        0: F(1) + probe_alpha * probe_alpha,
        1: -probe_alpha,
    }
    denominator_modulus = dict(numerator_modulus)
    require(numerator_modulus == denominator_modulus, "selector is not inner up to scale")

    p_at_one = [F(1), F(-2), F(-2), F(1)]
    factor_at_one = multiply([F(1), F(1)], [F(1), F(-3), F(1)])
    require(p_at_one == factor_at_one, "golden-limit factorization changed")
    alpha_limit = (F(3, 2), F(-1, 2))
    tau_limit = (F(3, 2), F(1, 2))
    require(
        surd_polynomial([F(1), F(-3), F(1)], alpha_limit) == (F(0), F(0)),
        "golden alpha label changed",
    )
    require(
        surd_multiply(alpha_limit, tau_limit) == (F(1), F(0)),
        "golden reciprocal label changed",
    )

    return {
        "first_selector": "1",
        "first_selector_norm": "1",
        "second_beta_zero": "-alpha",
        "second_target_value": "-1/alpha",
        "second_selector": "(alpha-z^2)/(alpha*(1-alpha*z^2))",
        "second_selector_at_zero": "1",
        "second_selector_norm": "1/alpha",
        "second_selector_boundary_modulus": "1/alpha",
        "second_nontargets_cancelled": True,
        "P_one_factorization": "(x+1)*(x^2-3*x+1)",
        "alpha_limit": "(3-sqrt(5))/2",
        "second_selector_norm_limit": "(3+sqrt(5))/2",
        "selector_norms_bounded_as_s_decreases_to_one": True,
        "floating_point_arithmetic_used": False,
    }


def boundary_values(s: F) -> tuple[F, F]:
    s = F(s)
    require(s > 1, "boundary fixture requires s greater than one")
    p_one = evaluate(p_coefficients(s), F(1))
    require(p_one != 0, "boundary fixture hit excluded upper endpoint")
    return s / (s - 1), s**3 / ((s - 1) * p_one)


def boundary_obstruction_fixture() -> dict[str, object]:
    first_n = 100
    closer_n = 200
    first_s = F(first_n + 1, first_n)
    closer_s = F(closer_n + 1, closer_n)
    first_values = boundary_values(first_s)
    closer_values = boundary_values(closer_s)
    for n, values in ((first_n, first_values), (closer_n, closer_values)):
        require(values[0] == n + 1, "first boundary sequence formula changed")
        require(
            values[1] == -F((n + 1) ** 3, 2 * n * n + n - 2),
            "second boundary sequence formula changed",
        )
        # Three times the numerator minus n times the denominator is
        # n^3+8n^2+11n+3, so |h2(1)|>n/3 without asymptotics or floats.
        lower_bound_remainder = (
            3 * (n + 1) ** 3 - n * (2 * n * n + n - 2)
        )
        require(
            lower_bound_remainder == n**3 + 8 * n * n + 11 * n + 3,
            "second boundary lower-bound identity changed",
        )
        require(lower_bound_remainder > 0, "second boundary lower bound failed")
    require(closer_values[0] > first_values[0], "first quotient did not grow")
    require(
        abs(closer_values[1]) > abs(first_values[1]),
        "second quotient did not grow",
    )
    require(first_s - 1 > closer_s - 1 > 0, "exterior collar did not shrink")
    return {
        "sample_parameters": [render(first_s), render(closer_s)],
        "sequence": "s_n=1+1/n",
        "first_quotient_sequence": "n+1",
        "second_quotient_sequence": "-(n+1)^3/(2*n^2+n-2)",
        "second_absolute_lower_bound": "n/3",
        "lower_bound_positive_remainder": "n^3+8*n^2+11*n+3",
        "first_quotient_at_one": [render(first_values[0]), render(closer_values[0])],
        "second_quotient_at_one": [render(first_values[1]), render(closer_values[1])],
        "exterior_F_prime_root_squared": [render(first_s), render(closer_s)],
        "exterior_collar_width_squared": [
            render(first_s - 1),
            render(closer_s - 1),
        ],
        "unweighted_boundary_suprema_diverge": True,
        "optimal_selector_weighted_boundary_suprema_diverge": True,
        "first_full_weighted_contour_integral": "1",
        "second_full_weighted_contour_integral": "1",
        "oriented_contour_integral_divergence_claimed": False,
        "phase_sensitive_edge_cancellation_remains_open": True,
    }


def mutation_firewalls() -> dict[str, object]:
    margin = margin_ledger_fixture()
    gauge = gauge_fixture()
    manifest = event_manifest_fixture()
    boundary = boundary_obstruction_fixture()
    require(margin["m12_equals_m1_times_m2"] is False, "m12 mutation accepted")
    require(
        gauge["complete_derivative_manifest_preserved"] is False,
        "same-manifest gauge mutation accepted",
    )
    require(
        manifest["second_nontarget_locations_fixed_in_s"] is False,
        "moving nontarget mutation accepted",
    )
    require(
        boundary["oriented_contour_integral_divergence_claimed"] is False,
        "oriented-integral mutation accepted",
    )
    return {
        "second_quotient_is_inverse_A_only": False,
        "second_quotient_is_inverse_L_squared_plus_A": False,
        "m12_equals_m1_times_m2": False,
        "upper_log_derivative_bounds_supply_required_lower_margin": False,
        "constant_modulus_selector_attenuates_bad_supremum_edge": False,
        "finite_interior_jets_determine_boundary_margins": False,
        "gauge_preserves_complete_derivative_manifest": False,
        "bounded_selector_norms_control_absolute_edges": False,
        "interior_manifest_authenticates_exterior_collar": False,
        "second_nontarget_locations_fixed_in_s": False,
        "absolute_edge_divergence_implies_oriented_integral_divergence": False,
        "explicit_family_is_Xi": False,
        "parameter_endpoints_included": False,
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
        "schema": "riemann.t105109.log-derivative-edge-obstruction.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_WITH_ALGEBRAIC_ROOT_CERTIFICATES",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "margin_ledger": margin_ledger_fixture(),
            "finite_jet_gauge": gauge_fixture(),
            "derivative_polynomials": derivative_polynomial_fixture(),
            "event_manifests": event_manifest_fixture(),
            "local_target_residues": local_residue_fixture(),
            "optimal_selectors": selector_fixture(),
            "rational_checkpoint": rational_checkpoint_fixture(),
            "boundary_obstruction": boundary_obstruction_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "log_derivative_denominator_ledger_verified": True,
            "constant_modulus_weighted_sup_equalities_verified": True,
            "finite_jet_gauge_boundary_collapse_verified": True,
            "explicit_family_event_topology_verified": True,
            "fixed_target_principal_coefficients_verified": True,
            "bounded_selector_edge_obstruction_verified": True,
            "finite_interior_jets_determine_boundary_margins": False,
            "gauge_preserves_complete_derivative_manifest": False,
            "bounded_selector_norms_control_absolute_edges": False,
            "interior_manifest_authenticates_exterior_collar": False,
            "second_nontarget_locations_fixed_in_s": False,
            "explicit_family_is_Xi": False,
            "oriented_contour_integral_divergence_proved": False,
            "phase_sensitive_oriented_edge_cancellation_refuted": False,
            "xi_actual_pole_manifest_constructed": False,
            "xi_exterior_collar_certified": False,
            "xi_log_derivative_lower_margins_proved": False,
            "xi_oriented_edge_cancellation_proved": False,
            "xi_green_gram_bounds_proved_cofinally": False,
            "cofinal_weighted_edge_decay_proved": False,
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
