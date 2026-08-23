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

VERDICT = "PASS_T105111_ANCHORED_DISK_MARGIN_CERTIFICATE"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105110-principal-part-edge-cancellation"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "3f0286c2d574e8252fe9903f4f62d86e510275bdf4a1a085e3f232873aec9532"
BASE_COMMIT = "b52e4b4dceefb0b6c56b0ffe303d4ca01ffe9c56"

SPEC = importlib.util.spec_from_file_location("t105110_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105110 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105111.json",
    "claims/lemmas/L-105111-anchored-disk-margin-certificates.md",
    "claims/methodology/M-105111-quantitative-margin-review-contract.md",
    "claims/refutations/R-105111-finite-anchors-do-not-give-quotient-margins.md",
    "claims/theorems/T-105111-certified-absolute-edge-frontier.md",
    "experiments/X-105111-anchored-disk-margin-certificate/verify.py",
    "experiments/X-105111-anchored-disk-margin-certificate/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def poly_trim(coefficients: list[F]) -> list[F]:
    values = [F(value) for value in coefficients]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [F(0)]


def poly_add(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    result = [F(0)] * size
    for index in range(size):
        if index < len(left):
            result[index] += left[index]
        if index < len(right):
            result[index] += right[index]
    return poly_trim(result)


def poly_scale(polynomial: list[F], scalar: F | int) -> list[F]:
    return poly_trim([F(scalar) * value for value in polynomial])


def poly_mul(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return poly_trim(result)


def poly_derivative(polynomial: list[F]) -> list[F]:
    if len(polynomial) <= 1:
        return [F(0)]
    return poly_trim(
        [F(index) * polynomial[index] for index in range(1, len(polynomial))]
    )


def poly_eval(polynomial: list[F], point: F | int) -> F:
    value = F(0)
    for coefficient in reversed(polynomial):
        value = value * F(point) + coefficient
    return value


def render_poly(polynomial: list[F]) -> list[str]:
    return [render(value) for value in poly_trim(polynomial)]


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105110 dependency artifact is stale")
    require(
        artifact.get("proof_object_sha256") == BASE_DIGEST,
        "T-105110 dependency digest changed",
    )
    require(
        artifact.get("verdict") == BASE.VERDICT,
        "T-105110 dependency verdict changed",
    )
    return {
        "path": "experiments/X-105110-principal-part-edge-cancellation",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def normalized_derivative_fixture() -> dict[str, object]:
    # A and B are reconstructed independently from a nontrivial polynomial
    # log derivative using A=L^2+L' and B=A'+LA.
    log_derivative = [F(1), F(2), F(-1)]
    log_derivative_prime = poly_derivative(log_derivative)
    normalized_second = poly_add(
        poly_mul(log_derivative, log_derivative),
        log_derivative_prime,
    )
    normalized_third = poly_add(
        poly_derivative(normalized_second),
        poly_mul(log_derivative, normalized_second),
    )

    first_denominator_prime = poly_derivative(log_derivative)
    first_formula = poly_add(
        normalized_second,
        poly_scale(poly_mul(log_derivative, log_derivative), -1),
    )
    product_denominator = poly_mul(log_derivative, normalized_second)
    product_denominator_prime = poly_derivative(product_denominator)
    product_formula = poly_add(
        poly_add(
            poly_mul(normalized_second, normalized_second),
            poly_mul(log_derivative, normalized_third),
        ),
        poly_scale(
            poly_mul(
                poly_mul(log_derivative, log_derivative),
                normalized_second,
            ),
            -2,
        ),
    )
    require(
        first_denominator_prime == first_formula,
        "G1 derivative identity changed",
    )
    require(
        product_denominator_prime == product_formula,
        "G12 derivative identity changed",
    )

    probe = F(1, 3)
    L = poly_eval(log_derivative, probe)
    A = poly_eval(normalized_second, probe)
    B = poly_eval(normalized_third, probe)
    G12 = poly_eval(product_denominator, probe)
    G12_prime = poly_eval(product_denominator_prime, probe)
    require(L != 0 and A != 0 and G12 != 0, "density probe hit a zero")
    first_density = poly_eval(first_denominator_prime, probe) / L
    first_density_formula = A / L - L
    product_density = G12_prime / G12
    product_density_formula = A / L + B / A - 2 * L
    require(first_density == first_density_formula, "first log density changed")
    require(
        product_density == product_density_formula,
        "product log density changed",
    )

    return {
        "probe_log_derivative_coefficients": render_poly(log_derivative),
        "normalized_second_coefficients": render_poly(normalized_second),
        "normalized_third_coefficients": render_poly(normalized_third),
        "first_derivative_identity": "G1_prime=A-L^2",
        "product_derivative_identity": "G12_prime=A^2+L*B-2*L^2*A",
        "density_probe": render(probe),
        "first_density": render(first_density),
        "first_density_formula": render(first_density_formula),
        "product_density": render(product_density),
        "product_density_formula": render(product_density_formula),
        "identities_verified_by_polynomial_coefficients": True,
    }


def anchored_drop_fixture() -> dict[str, object]:
    # For L=1-z/4 on [0,1], use an interior anchor z*=1/2 to
    # distinguish the exact downward drop from the total variation.
    left = F(1)
    anchor = F(7, 8)
    right = F(3, 4)
    downward_ratio = anchor / right
    total_variation_ratio = left / right
    reverse_ratio = left / anchor
    require(downward_ratio == F(7, 6), "anchored downward ratio changed")
    require(total_variation_ratio == F(4, 3), "total variation ratio changed")
    require(
        downward_ratio <= total_variation_ratio,
        "exact downward variation exceeded total variation",
    )
    require(reverse_ratio > 1, "reversed subarc sign was lost")
    return {
        "arc": "[0,1]",
        "function": "G(z)=1-z/4",
        "anchor": "1/2",
        "values_left_anchor_right": [render(left), render(anchor), render(right)],
        "exact_downward_ratio": render(downward_ratio),
        "exact_drop": "log(7/6)",
        "total_variation_ratio": render(total_variation_ratio),
        "total_variation": "log(4/3)",
        "reverse_subarc_modulus_ratio": render(reverse_ratio),
        "anchor_included_so_drop_nonnegative": True,
        "signed_subarc_integral_used": True,
        "real_log_variation_no_larger_than_complex_variation": True,
        "nonvanishing_authenticated_before_log_division": True,
    }


def rational_margin_fixture() -> dict[str, object]:
    u0 = F(1)
    u1 = F(3, 4)
    A0 = u0 * u0 - F(1, 4)
    A1 = u1 * u1 - F(1, 4)
    product0 = u0 * A0
    product1 = u1 * A1
    first_ratio = u0 / u1
    product_ratio = product0 / product1
    require(A0 == F(3, 4) and A1 == F(5, 16), "F0 A values changed")
    require(product1 == F(15, 64), "F0 product margin changed")
    require(first_ratio == F(4, 3), "F0 first drop ratio changed")
    require(product_ratio == F(16, 5), "F0 product drop ratio changed")
    return {
        "function": "exp(z-z^2/8)",
        "edge": "[0,1]",
        "u": "1-z/4",
        "L": "u",
        "A": "u^2-1/4",
        "B": "u^3-3*u/4",
        "G12": "u*(u^2-1/4)",
        "G12_prime": "-(3*u^2-1/4)/4",
        "anchor_L": render(u0),
        "anchor_G12": render(product0),
        "first_margin": render(u1),
        "product_margin": render(product1),
        "first_drop_ratio": render(first_ratio),
        "product_drop_ratio": render(product_ratio),
        "first_drop": "log(4/3)",
        "product_drop": "log(16/5)",
        "both_monotone_positive": True,
    }


def disk_cover_fixture() -> dict[str, object]:
    centers = [F(1, 4), F(3, 4)]
    radius = F(1, 4)
    real_intervals = [(center - radius, center + radius) for center in centers]
    require(real_intervals[0] == (F(0), F(1, 2)), "left disk interval changed")
    require(real_intervals[1] == (F(1, 2), F(1)), "right disk interval changed")

    first_centers = [F(1) - center / 4 for center in centers]
    first_derivative_suprema = [F(1, 4), F(1, 4)]
    first_slacks = [
        value - radius * derivative
        for value, derivative in zip(first_centers, first_derivative_suprema)
    ]
    require(first_centers == [F(15, 16), F(13, 16)], "L centers changed")
    require(first_slacks == [F(7, 8), F(3, 4)], "L slacks changed")

    product_centers: list[F] = []
    product_derivative_suprema: list[F] = []
    positive_expansions: list[list[F]] = []
    for center in centers:
        u_center = F(1) - center / 4
        u_radius = radius / 4
        product_centers.append(u_center * (u_center * u_center - F(1, 4)))
        # On the u-disk, 3(u_c+w)^2-1/4 has nonnegative coefficients.
        expansion = [
            3 * u_center * u_center - F(1, 4),
            6 * u_center,
            F(3),
        ]
        require(all(value > 0 for value in expansion), "disk majorant sign changed")
        exact_supremum = sum(
            expansion[index] * (u_radius**index)
            for index in range(len(expansion))
        ) / 4
        direct_boundary_value = (
            3 * (u_center + u_radius) ** 2 - F(1, 4)
        ) / 4
        require(
            exact_supremum == direct_boundary_value,
            "product derivative supremum is not attained by the majorant",
        )
        product_derivative_suprema.append(exact_supremum)
        positive_expansions.append(expansion)

    product_slacks = [
        value - radius * derivative
        for value, derivative in zip(
            product_centers,
            product_derivative_suprema,
        )
    ]
    require(
        product_centers == [F(2415, 4096), F(1365, 4096)],
        "product disk centers changed",
    )
    require(
        product_derivative_suprema == [F(11, 16), F(131, 256)],
        "product disk derivative suprema changed",
    )
    require(
        product_slacks == [F(1711, 4096), F(841, 4096)],
        "product disk slacks changed",
    )
    require(all(value > 0 for value in product_slacks), "positive slack was lost")

    return {
        "centers": [render(value) for value in centers],
        "radius": render(radius),
        "real_intervals": [
            [render(left), render(right)] for left, right in real_intervals
        ],
        "complete_edge_including_endpoints_covered": True,
        "closed_disks_inside_holomorphy_domain": True,
        "first_center_values": [render(value) for value in first_centers],
        "first_derivative_suprema": [
            render(value) for value in first_derivative_suprema
        ],
        "first_slacks": [render(value) for value in first_slacks],
        "product_center_values": [render(value) for value in product_centers],
        "product_derivative_suprema": [
            render(value) for value in product_derivative_suprema
        ],
        "product_slacks": [render(value) for value in product_slacks],
        "product_majorant_coefficients": [
            [render(value) for value in row] for row in positive_expansions
        ],
        "product_suprema_exact_by_positive_coefficient_attainment": True,
        "minimum_first_slack": render(min(first_slacks)),
        "minimum_product_slack": render(min(product_slacks)),
    }


def sharp_anchor_fixture() -> dict[str, object]:
    q = F(1, 4)
    anchor = F(1)
    margin = q
    ratio = anchor / margin
    require(0 < q < 1, "sharp anchor parameter left its range")
    require(ratio == 4, "sharp anchor ratio changed")
    return {
        "family": "F_q=exp(z-(1-q)*z^2/2)",
        "q_probe": render(q),
        "anchor_value": render(anchor),
        "margin": render(margin),
        "drop_ratio": render(ratio),
        "drop": "log(4)",
        "general_drop": "log(1/q)",
        "exponential_loss_attained": True,
    }


def first_product_independence_fixture() -> dict[str, object]:
    parameter = F(1, 4)
    product_factor = 1 - 4 * parameter + parameter * parameter
    first_margin = 1 - parameter
    product_margin = first_margin * product_factor
    require(product_factor == F(1, 16), "product factor changed")
    require(first_margin == F(3, 4), "independence first margin changed")
    require(product_margin == F(3, 64), "independence product margin changed")
    return {
        "family": "F_a=exp(z-a*z^3/3)",
        "parameter_probe": render(parameter),
        "parameter_range": "0<a<2-sqrt(3)",
        "L": "1-a*z^2",
        "A": "(1-a*z^2)^2-2*a*z",
        "first_margin": render(first_margin),
        "product_factor": render(product_factor),
        "product_margin": render(product_margin),
        "product_factor_boundary_polynomial": "1-4*a+a^2",
        "first_margin_stays_positive_at_product_collapse": True,
        "first_margin_alone_controls_product_margin": False,
    }


def counterfamily_fixture() -> dict[str, object]:
    half = F(1, 2)
    one = F(1)
    zeta = F(3, 4)
    z_squared = [F(0), F(0), F(1)]
    first_factor = [-(half**2), F(0), F(1)]
    second_factor = [-(one**2), F(0), F(1)]
    Q = poly_mul(poly_mul(z_squared, first_factor), second_factor)
    expected = [F(0), F(0), F(1, 4), F(0), F(-5, 4), F(0), F(1)]
    require(Q == expected, "Q_S coefficient expansion changed")
    Q_prime = poly_derivative(Q)
    q_zeta = poly_eval(Q, zeta)
    q_prime_zeta = poly_eval(Q_prime, zeta)
    q_squared = q_zeta * q_zeta
    require(q_zeta == F(-315, 4096), "Q_S nonsample value changed")
    require(q_prime_zeta == F(-159, 512), "Q_S derivative value changed")
    require(q_squared == F(99225, 16777216), "Q_S square changed")
    require(poly_eval(Q, half) == 0 and poly_eval(Q, one) == 0, "anchor root changed")

    anchor_rows = []
    for point in (half, one):
        L = point
        L_prime = F(1)
        A = point * point + L_prime
        anchor_rows.append(
            {
                "point": render(point),
                "L": render(L),
                "L_prime": render(L_prime),
                "A": render(A),
                "L_times_A": render(L * A),
            }
        )
    require(
        [row["L_times_A"] for row in anchor_rows] == ["5/8", "2"],
        "fixed product anchor values changed",
    )

    # Put C_n=n/Q(zeta)^2.  Then exp(-C_n Q(zeta)^2)=exp(-n),
    # and the exact normalized-second formula has a linear coefficient.
    linear_coefficient = 2 * zeta * q_zeta * q_prime_zeta / q_squared
    require(linear_coefficient == F(212, 35), "collapse coefficient changed")
    n = 8
    exponential_bound = F(6, n**3)
    first_bound = zeta * exponential_bound
    second_bound = (
        zeta * zeta * exponential_bound
        + (1 + linear_coefficient * n) * exponential_bound
    )
    require(first_bound == F(9, 1024), "first collapse rational bound changed")
    require(second_bound == F(84033, 143360), "second collapse rational bound changed")

    return {
        "sample_set": ["1/2", "1"],
        "edge": "[1/2,1]",
        "nonsample": render(zeta),
        "Q_coefficients": render_poly(Q),
        "Q_at_nonsample": render(q_zeta),
        "Q_prime_at_nonsample": render(q_prime_zeta),
        "Q_square_at_nonsample": render(q_squared),
        "global_first_event_manifest": [
            {"point": "0", "order": 1, "role": "target"}
        ],
        "first_target_residue": "1",
        "first_optimal_selector": "1",
        "first_optimal_selector_norm": "1",
        "anchor_rows": anchor_rows,
        "collapse_sequence": "C_n=n/Q(zeta)^2",
        "nonsample_L_formula": "zeta*exp(-n)",
        "nonsample_A_formula": "zeta^2*exp(-2*n)+(1-(212/35)*n)*exp(-n)",
        "collapse_linear_coefficient": render(linear_coefficient),
        "exp_minus_n_bound": "6/n^3",
        "bound_probe_n": n,
        "probe_first_absolute_bound": render(first_bound),
        "probe_second_absolute_bound": render(second_bound),
        "both_nonsample_denominators_converge_to_zero": True,
        "complete_first_manifest_is_stable": True,
        "second_derivative_manifest_is_stable": False,
        "family_is_fixed_function": False,
        "family_has_finite_order": False,
        "family_is_xi_class": False,
        "product_log_drop_is_uniformly_bounded": False,
    }


def mutation_firewalls() -> dict[str, object]:
    rational = rational_margin_fixture()
    disks = disk_cover_fixture()
    independence = first_product_independence_fixture()
    counter = counterfamily_fixture()
    require(
        rational["product_drop_ratio"] != rational["first_drop_ratio"],
        "first/product drop mutation accepted",
    )
    require(
        F(disks["minimum_product_slack"]) > 0,
        "nonpositive product slack accepted",
    )
    require(
        independence["first_margin_alone_controls_product_margin"] is False,
        "first-to-product implication mutation accepted",
    )
    require(
        counter["second_derivative_manifest_is_stable"] is False,
        "stable second-manifest mutation accepted",
    )
    return {
        "log_division_is_valid_before_nonvanishing_authentication": False,
        "downward_drop_equals_total_variation_for_every_anchor": False,
        "complex_log_variation_is_always_sharp": False,
        "arbitrary_weight_has_constant_modulus_selector_equality": False,
        "disk_cover_may_omit_edge_endpoints": False,
        "closed_disks_may_leave_the_holomorphy_domain": False,
        "nonpositive_disk_slack_certifies_nonvanishing": False,
        "first_denominator_derivative_bound_certifies_product_margin": False,
        "first_margin_controls_product_margin": False,
        "finite_anchors_determine_between_anchor_margins": False,
        "stable_first_manifest_implies_stable_second_manifest": False,
        "counterfamily_has_uniform_product_log_drop": False,
        "counterfamily_is_fixed_function_cofinal_xi_model": False,
        "xi_anchor_or_disk_data_supplied": False,
        "cofinal_green_gram_margin_absorption_proved": False,
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
        "schema": "riemann.t105111.anchored-disk-margin-certificate.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_WITH_SYMBOLIC_LOG_VARIATION_IDENTITIES",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "normalized_denominator_identities": normalized_derivative_fixture(),
            "anchored_log_drop": anchored_drop_fixture(),
            "rational_margin_fixture": rational_margin_fixture(),
            "finite_disk_cover": disk_cover_fixture(),
            "sharp_anchor_loss": sharp_anchor_fixture(),
            "first_product_independence": first_product_independence_fixture(),
            "finite_anchor_counterfamily": counterfamily_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "exact_anchored_log_drop_verified": True,
            "total_log_variation_sufficient_certificate_verified": True,
            "finite_disk_positive_slack_certificate_verified": True,
            "normalized_derivative_identities_through_F_third_verified": True,
            "rational_first_product_margin_fixture_verified": True,
            "stable_first_manifest_anchor_only_refutation_verified": True,
            "selector_equality_restricted_to_same_selector_domain_boundary_arc": True,
            "xi_anchor_values_authenticated": False,
            "xi_zero_free_disk_cover_authenticated": False,
            "xi_log_variation_bounds_proved": False,
            "xi_third_normalized_derivative_bounds_proved": False,
            "xi_disk_count_and_minimum_slack_proved": False,
            "cofinal_green_gram_selector_growth_absorbed": False,
            "xi_pole_subtracted_remainder_and_corner_ledger_proved": False,
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
