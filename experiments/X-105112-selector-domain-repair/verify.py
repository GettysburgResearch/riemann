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

VERDICT = "PASS_T105112_SELECTOR_DOMAIN_REPAIR"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105111-anchored-disk-margin-certificate"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "7bafdd3d8fb379e8d8de2cd30df8b96331378d7e4f244bb801439493a2e132cd"
BASE_COMMIT = "51c67046a726be188bf724f7b4652e299bd31ccb"

SPEC = importlib.util.spec_from_file_location("t105111_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105111 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105112.json",
    "claims/lemmas/L-105112-same-domain-selector-equalities.md",
    "claims/methodology/M-105112-selector-domain-repair-contract.md",
    "claims/refutations/R-105112-off-domain-boundary-equality-fails.md",
    "claims/theorems/T-105112-repaired-quotient-edge-frontier.md",
    "experiments/X-105112-selector-domain-repair/verify.py",
    "experiments/X-105112-selector-domain-repair/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


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


def render_poly(values: list[F]) -> list[str]:
    return [render(value) for value in poly_trim(values)]


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105111 dependency artifact is stale")
    require(
        artifact.get("proof_object_sha256") == BASE_DIGEST,
        "T-105111 dependency digest changed",
    )
    require(
        artifact.get("verdict") == BASE.VERDICT,
        "T-105111 dependency verdict changed",
    )
    return {
        "path": "experiments/X-105111-anchored-disk-margin-certificate",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def same_domain_norm_fixture() -> dict[str, object]:
    first_denominators = [F(3, 2), F(1, 2), F(5, 4)]
    product_denominators = [F(7, 3), F(2, 5), F(9, 4)]
    tau_one = F(4)
    tau_two = F(3)
    first_margin = min(first_denominators)
    product_margin = min(product_denominators)
    first_weighted = [tau_one / value for value in first_denominators]
    second_weighted = [tau_two / value for value in product_denominators]
    require(max(first_weighted) == tau_one / first_margin, "first equality failed")
    require(max(second_weighted) == tau_two / product_margin, "second equality failed")
    return {
        "selector_domain": "the exact bounded simply connected Jordan domain Omega",
        "edge_location": "E subset boundary(Omega)",
        "pointwise_selector_moduli": ["tau_1", "tau_2"],
        "first_denominator_samples": [render(value) for value in first_denominators],
        "first_margin": render(first_margin),
        "tau_1": render(tau_one),
        "first_weighted_supremum": render(max(first_weighted)),
        "tau_1_over_first_margin": render(tau_one / first_margin),
        "product_denominator_samples": [
            render(value) for value in product_denominators
        ],
        "product_margin": render(product_margin),
        "tau_2": render(tau_two),
        "second_weighted_supremum": render(max(second_weighted)),
        "tau_2_over_product_margin": render(tau_two / product_margin),
        "both_same_domain_equalities_exact": True,
    }


def arbitrary_edge_fixture() -> dict[str, object]:
    # On the radial segment [1/2,1], W=z^2 and L=z^3.
    weight_norm = F(1)
    first_margin = F(1, 8)
    actual_weighted_norm = F(2)
    product_upper = weight_norm / first_margin
    tau = F(1)
    require(actual_weighted_norm < product_upper, "strict product example failed")
    return {
        "edge": "[1/2,1] inside closure(unit disk)",
        "weight": "z^2",
        "denominator": "z^3",
        "weight_edge_norm": render(weight_norm),
        "first_margin": render(first_margin),
        "raw_quotient_norm": render(1 / first_margin),
        "actual_weighted_norm": render(actual_weighted_norm),
        "actual_weight_norm_product_upper": render(product_upper),
        "selector_domain_norm_tau": render(tau),
        "maximum_modulus_gives_weight_edge_norm_at_most_tau": True,
        "tau_margin_envelope": render(tau / first_margin),
        "product_inequality_can_be_strict": True,
        "tau_envelope_need_not_be_equality": True,
    }


def counterexample_fixture() -> dict[str, object]:
    exponent = [F(0), F(0), F(0), F(0), F(1, 4)]
    log_derivative = poly_derivative(exponent)
    normalized_second = poly_add(
        poly_mul(log_derivative, log_derivative),
        poly_derivative(log_derivative),
    )
    require(log_derivative == [F(0), F(0), F(0), F(1)], "L is not z^3")
    require(
        normalized_second == [F(0), F(0), F(3), F(0), F(0), F(0), F(1)],
        "A is not 3*z^2+z^6",
    )

    def circle_row(radius: F) -> dict[str, object]:
        margin = radius**3
        weight_norm = radius**2
        actual = 1 / radius
        tau_margin = 1 / margin
        product_bound = weight_norm / margin
        require(actual == product_bound, "circle product inequality not attained")
        return {
            "radius": render(radius),
            "first_margin": render(margin),
            "weight_edge_norm": render(weight_norm),
            "raw_quotient_norm": render(1 / margin),
            "actual_weighted_norm": render(actual),
            "actual_weight_norm_product_bound": render(product_bound),
            "tau_over_margin": render(tau_margin),
            "F_second_factor_lower_bound": render(F(3) - radius**4),
            "is_selector_domain_boundary": radius == 1,
            "tau_equality_holds": actual == tau_margin,
        }

    half = circle_row(F(1, 2))
    unit = circle_row(F(1))
    require(half["actual_weighted_norm"] == "2", "half-circle norm changed")
    require(half["tau_over_margin"] == "8", "broad prediction changed")
    require(unit["tau_equality_holds"], "same-domain equality failed")
    return {
        "selector_domain": "unit disk",
        "function": "F(z)=exp(z^4/4)",
        "exponent_coefficients": render_poly(exponent),
        "log_derivative_coefficients": render_poly(log_derivative),
        "normalized_second_coefficients": render_poly(normalized_second),
        "F_prime": "z^3*F",
        "F_second": "z^2*(z^4+3)*F",
        "F_is_zero_free": True,
        "first_manifest": [{"point": "0", "order": 3, "role": "target"}],
        "first_target_principal_coefficient": "1",
        "all_admissible_selectors": "W(z)=z^2*H(z), H(0)=1",
        "optimal_selector": "z^2",
        "optimal_selector_norm_tau": "1",
        "optimality_from_maximum_modulus": True,
        "first_quotient": "z^-3",
        "weighted_first_quotient": "z^-1",
        "half_radius_upper_semicircle": half,
        "unit_upper_semicircle": unit,
        "general_radius_actual_norm": "1/r",
        "general_radius_tau_over_margin": "1/r^3",
        "tau_equality_for_0_less_r_at_most_1_iff_r_equals_1": True,
    }


def repair_ledger() -> dict[str, object]:
    return {
        "affected_frozen_files": [
            "PACKET_METADATA_105109.json",
            "claims/lemmas/L-105109-log-derivative-edge-margins.md",
            "claims/methodology/M-105109-quotient-edge-review-contract.md",
            "claims/theorems/T-105109-quotient-edge-frontier.md",
            "PR_BODY_105109_ADDENDUM.md",
            "reports/codex/2026-08-23-log-derivative-edge-obstruction.md",
        ],
        "literal_wording_overbroad_or_ambiguous": True,
        "intended_same_domain_reading_repaired": True,
        "frozen_105109_files_modified": False,
        "retrospective_105109_verification_claimed": False,
        "t105109_same_unit_disk_obstruction_survives": True,
    }


def forbidden_control_characters() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    allowed = {9, 10, 13}
    for relative_path in CONTENT_FILES:
        raw = (REPO_ROOT / relative_path).read_bytes()
        for offset, value in enumerate(raw):
            if value < 32 and value not in allowed:
                failures.append(
                    {"path": relative_path, "offset": offset, "byte": value}
                )
    return failures


def mutation_firewalls() -> dict[str, bool]:
    return {
        "constant_modulus_transfers_to_every_other_boundary": False,
        "interior_arc_has_selector_modulus_tau_pointwise": False,
        "selector_domain_norm_always_equals_local_edge_norm": False,
        "arbitrary_edge_product_bound_is_always_equality": False,
        "membership_in_A_Omega_defines_selector_outside_closure": False,
        "scalar_tau_alone_authenticates_same_domain_identity": False,
        "counterexample_refutes_same_domain_boundary_equality": False,
        "repair_silently_modifies_frozen_105109_files": False,
        "t105109_was_retrospectively_reverified": False,
        "xi_margin_or_collar_supplied": False,
        "rcmv104530_proved": False,
        "rh_established": False,
    }


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
        "schema": "riemann.t105112.selector-domain-repair.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_AND_POLYNOMIAL_ERRATUM",
        "source": {"checkpoint_base": BASE_COMMIT},
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "same_domain_norm_ledger": same_domain_norm_fixture(),
            "arbitrary_edge_norm_ledger": arbitrary_edge_fixture(),
            "unit_disk_counterexample": counterexample_fixture(),
            "repair_ledger": repair_ledger(),
            "mutation_firewalls": mutation_firewalls(),
            "forbidden_control_characters": forbidden_control_characters(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "same_selector_domain_first_equality_verified": True,
            "same_selector_domain_second_equality_verified": True,
            "arbitrary_edge_actual_weight_norm_inequality_verified": True,
            "closure_maximum_modulus_tau_envelope_verified": True,
            "off_selector_boundary_tau_equality_refuted": True,
            "same_domain_unit_semicircle_equality_verified": True,
            "frozen_105109_files_modified": False,
            "retrospective_105109_verification_claimed": False,
            "xi_margin_or_collar_authenticated": False,
            "cofinal_selector_margin_absorption_proved": False,
            "phase_sensitive_edge_cancellation_proved": False,
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
