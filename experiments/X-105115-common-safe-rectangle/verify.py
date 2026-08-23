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

VERDICT = "PASS_T105115_COMMON_SAFE_RECTANGLE"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105114-anchored-equal-disk-collar"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "15ff7ba8056a9beb5e942945c9f92dcce566f7d737bc04f8f2db6895109c3284"
BASE_COMMIT = "aa7b44947f8b0f9c37bb8adc2141079b57729d04"
CHECKPOINT_BASE = "c071fc31168847b901542be04ed6fc30c60b29d9"

SPEC = importlib.util.spec_from_file_location("t105114_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105114 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105115.json",
    "claims/lemmas/L-105115-common-safe-rectangle-projection.md",
    "claims/methodology/M-105115-common-safe-rectangle-review-contract.md",
    "claims/refutations/R-105115-nonstrict-radius-gate-is-insufficient.md",
    "claims/theorems/T-105115-common-safe-rectangle-frontier.md",
    "experiments/X-105115-common-safe-rectangle/verify.py",
    "experiments/X-105115-common-safe-rectangle/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105114 dependency artifact is stale")
    require(artifact.get("proof_object_sha256") == BASE_DIGEST, "T-105114 digest changed")
    require(artifact.get("verdict") == BASE.VERDICT, "T-105114 verdict changed")
    return {
        "path": "experiments/X-105114-anchored-equal-disk-collar",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def merged_intervals(
    intervals: list[tuple[F, F]], window: tuple[F, F]
) -> list[tuple[F, F]]:
    lo, hi = window
    clipped = sorted(
        (max(lo, left), min(hi, right))
        for left, right in intervals
        if max(lo, left) < min(hi, right)
    )
    merged: list[tuple[F, F]] = []
    for left, right in clipped:
        if not merged or left > merged[-1][1]:
            merged.append((left, right))
        else:
            old_left, old_right = merged[-1]
            merged[-1] = (old_left, max(old_right, right))
    return merged


def interval_measure(intervals: list[tuple[F, F]]) -> F:
    return sum((right - left for left, right in intervals), F(0))


def geometry_fixture() -> dict[str, object]:
    disks = [
        (F(2), F(1), F(1, 2)),
        (F(-3), F(-2), F(1, 4)),
        (F(2), F(-1), F(1, 4)),
    ]
    t_window = (F(1), F(4))
    eta_window = (F(0), F(3))
    delta_t = t_window[1] - t_window[0]
    delta_eta = eta_window[1] - eta_window[0]
    total_radius = sum((row[2] for row in disks), F(0))
    t_raw = [(abs(x) - radius, abs(x) + radius) for x, _, radius in disks]
    eta_raw = [(abs(y) - radius, abs(y) + radius) for _, y, radius in disks]
    t_merged = merged_intervals(t_raw, t_window)
    eta_merged = merged_intervals(eta_raw, eta_window)
    bad_t = interval_measure(t_merged)
    bad_eta = interval_measure(eta_merged)
    good_t = delta_t - bad_t
    good_eta = delta_eta - bad_eta

    require(total_radius == 1, "fixture total radius changed")
    require(bad_t == F(3, 2), "vertical projection measure changed")
    require(bad_eta == F(3, 2), "horizontal projection measure changed")
    require(2 * total_radius < delta_t, "vertical strict gate failed")
    require(2 * total_radius < delta_eta, "horizontal strict gate failed")

    selected_t, selected_eta = F(7, 2), F(5, 2)
    for x, y, radius in disks:
        require(abs(selected_t - abs(x)) > radius, "selected vertical line is unsafe")
        require(abs(selected_eta - abs(y)) > radius, "selected horizontal line is unsafe")

    def rows(intervals: list[tuple[F, F]]) -> list[list[str]]:
        return [[render(left), render(right)] for left, right in intervals]

    return {
        "closed_disks": [
            {"x": render(x), "y": render(y), "radius": render(radius)}
            for x, y, radius in disks
        ],
        "windows": {"T": ["1", "4"], "eta": ["0", "3"]},
        "deltas": {"T": render(delta_t), "eta": render(delta_eta)},
        "total_radius": render(total_radius),
        "twice_total_radius": render(2 * total_radius),
        "merged_bad_T": rows(t_merged),
        "merged_bad_eta": rows(eta_merged),
        "bad_measures": {"T": render(bad_t), "eta": render(bad_eta)},
        "good_measures": {"T": render(good_t), "eta": render(good_eta)},
        "safe_product_measure": render(good_t * good_eta),
        "selected_safe_pair": {"T": render(selected_t), "eta": render(selected_eta)},
        "strict_total_radius_gate_holds": True,
        "supporting_line_product_is_only_sufficient_for_finite_edges": True,
    }


def sharpness_fixture() -> dict[str, object]:
    interval = (F(1), F(3))
    radius = F(1)
    center = F(2)
    bad = merged_intervals([(center - radius, center + radius)], interval)
    bad_measure = interval_measure(bad)
    delta = interval[1] - interval[0]
    require(delta == 2 * radius, "sharpness equality changed")
    require(bad_measure == delta, "one disk no longer covers the parameter interval")
    for probe in (F(5, 4), F(2), F(11, 4)):
        require(abs(probe - center) <= radius, "sharpness probe escaped the disk")
    return {
        "parameter_interval": "(1,3)",
        "disk": "closed D(2,1)",
        "Delta": "2",
        "S": "1",
        "Delta_equals_2S": True,
        "bad_measure": render(bad_measure),
        "safe_measure": "0",
        "nonstrict_gate_is_insufficient": True,
        "sharpness_scope": "coordinatewise using only total radius",
    }


def tonelli_ledger() -> dict[str, object]:
    delta_t = F(3)
    delta_eta = F(3)
    good_t = F(3, 2)
    good_eta = F(3, 2)
    q_integral = F(18)
    full_measure = delta_t * delta_eta
    safe_measure = good_t * good_eta
    unrestricted_mean = q_integral / full_measure
    safe_bound = q_integral / safe_measure
    kappa = full_measure / safe_measure
    relaxed_kappa = full_measure / ((delta_t - 2) * (delta_eta - 2))
    require(safe_bound == kappa * unrestricted_mean, "Tonelli normalization changed")
    require(kappa <= relaxed_kappa, "total-radius relaxation is too small")
    return {
        "aggregate": "one prescribed nonnegative measurable cost q(T,eta)",
        "full_integral_Q": render(q_integral),
        "full_parameter_measure": render(full_measure),
        "safe_product_measure": render(safe_measure),
        "unrestricted_mean": render(unrestricted_mean),
        "selected_safe_bound": render(safe_bound),
        "exact_kappa": render(kappa),
        "total_radius_relaxed_kappa": render(relaxed_kappa),
        "full_shell_integrability_required_for_kappa_comparison": True,
        "unsafe_raw_singularities_are_automatically_integrable": False,
        "safe_only_fallback": "average the restricted integral without citing the unrestricted shell budget",
    }


def raw_quotient_ledger() -> dict[str, object]:
    m0, a1, a2 = F(6), F(2), F(3)
    selected_t, selected_eta = F(7, 2), F(5, 2)
    length = 4 * (selected_t + selected_eta)
    i1, i2 = F(5), F(7)
    b1, b2 = F(1), F(2)
    q1 = m0 / a1
    q2 = m0 * m0 / (a1 * a2)
    return {
        "loads": {"M_0": render(m0), "a_1": render(a1), "a_2": render(a2)},
        "quotient_sup_bounds": {"F/F'": render(q1), "F^2/(F'F'')": render(q2)},
        "selected_edge_length": render(length),
        "weighted_integral_bounds": {
            "using_I_1": render(q1 * i1),
            "using_I_2": render(q2 * i2),
            "using_b_1": render(length * q1 * b1),
            "using_b_2": render(length * q2 * b2),
        },
        "F_zero_disks_required": False,
        "denominator_zero_cover_required": ["F'", "F''"],
        "post_cancellation_minimality_claimed": False,
    }


def selector_firewall() -> dict[str, object]:
    return {
        "same_domain_optimal_selector_constant_modulus": True,
        "outer_optimal_selector_constant_modulus_on_intermediate_edge_is_guaranteed": False,
        "outer_selector_upper_norm_bound_remains_available": True,
        "fixed_outer_carriers_required_for_shell_average": True,
        "rebuilding_after_rectangle_selection_is_allowed": False,
    }


def metadata_ledger() -> dict[str, object]:
    metadata = json.loads((REPO_ROOT / "PACKET_METADATA_105115.json").read_text(encoding="utf-8"))
    require(metadata["checkpoint_base_sha"] == CHECKPOINT_BASE, "metadata base changed")
    dependency = metadata["dependency_checkpoint"]
    require(dependency["commit"] == BASE_COMMIT, "metadata dependency commit changed")
    require(dependency["proof_object_sha256"] == BASE_DIGEST, "metadata dependency digest changed")
    require(metadata["rh_established"] is False, "metadata claims RH")
    return {
        "checkpoint_base": metadata["checkpoint_base_sha"],
        "dependency_commit": dependency["commit"],
        "dependency_digest": dependency["proof_object_sha256"],
        "heavy_computation_run": metadata["heavy_computation_run"],
        "rh_established": metadata["rh_established"],
    }


def mutation_firewalls() -> dict[str, bool]:
    return {
        "supporting_line_product_exhausts_all_safe_rectangles": False,
        "nonstrict_total_radius_gate_suffices": False,
        "twice_total_radius_is_the_exact_projection_measure": False,
        "restricted_average_has_no_normalization_loss": False,
        "unsafe_raw_singularities_need_no_integrability_check": False,
        "raw_route_requires_F_zero_disks": False,
        "outer_selector_intermediate_edge_equality_is_guaranteed": False,
        "selectors_may_be_rebuilt_after_parameter_selection": False,
        "cartan_zero_cover_is_complete_actual_pole_manifest": False,
        "cofinal_xi_safe_shell_established": False,
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
    failures = forbidden_control_characters()
    require(not failures, f"forbidden control characters: {failures}")
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
        "schema": "riemann.t105115.common-safe-rectangle.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_INTERVAL_GEOMETRY_AND_SYMBOLIC_INEQUALITY",
        "source": {"checkpoint_base": CHECKPOINT_BASE},
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "geometry_fixture": geometry_fixture(),
            "sharpness_fixture": sharpness_fixture(),
            "tonelli_ledger": tonelli_ledger(),
            "raw_quotient_ledger": raw_quotient_ledger(),
            "selector_firewall": selector_firewall(),
            "metadata_ledger": metadata_ledger(),
            "mutation_firewalls": mutation_firewalls(),
            "forbidden_control_characters": forbidden_control_characters(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "finite_supporting_line_projection_verified": True,
            "exact_safe_product_measure_verified": True,
            "strict_total_radius_gate_verified": True,
            "restricted_tonelli_normalization_verified": True,
            "raw_quotient_edge_envelopes_verified": True,
            "full_shell_integrability_authenticated_for_xi": False,
            "cofinal_xi_safe_shell_established": False,
            "complete_actual_xi_manifests_authenticated": False,
            "selector_margin_absorption_proved": False,
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
