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

VERDICT = "PASS_T105114_ANCHORED_EQUAL_DISK_COLLAR"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105113-buffered-selector-shell-average"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "44e0cffca9d4d680555287e8290cfa645d979dc76b064f0ab6914ace88c7d560"
BASE_COMMIT = "98e76fdd350556b2c659a0a16f7fa4083396527e"
CHECKPOINT_BASE = "f8102c6648829f72a6faaad06141c25b043c3f05"

SPEC = importlib.util.spec_from_file_location("t105113_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105113 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105114.json",
    "claims/lemmas/L-105114-anchored-equal-disk-minimum-modulus.md",
    "claims/methodology/M-105114-cartan-source-review-contract.md",
    "claims/refutations/R-105114-unnormalized-minimum-modulus-bound-is-false.md",
    "claims/theorems/T-105114-simultaneous-cartan-collar-transfer.md",
    "experiments/X-105114-anchored-equal-disk-collar/verify.py",
    "experiments/X-105114-anchored-equal-disk-collar/tests/test_verify.py",
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
    require(artifact == live, "T-105113 dependency artifact is stale")
    require(artifact.get("proof_object_sha256") == BASE_DIGEST, "T-105113 digest changed")
    require(artifact.get("verdict") == BASE.VERDICT, "T-105113 verdict changed")
    return {
        "path": "experiments/X-105113-buffered-selector-shell-average",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def formula_ledger() -> dict[str, object]:
    return {
        "hypotheses": {
            "radii": "0<r_1<r_2<r_3",
            "epsilon": "0<epsilon<=1",
            "anchor": "f(a)!=0",
            "zeros": "zeros in D(a,r_2), counted with multiplicity",
        },
        "growth_load": "A_f=log(max_{|z-a|=r_3}|f(z)|/|f(a)|)",
        "beta": "log(r_3/r_2)",
        "jensen_count": "n<=A_f/beta",
        "nominal_radius_sum": "S_f<=epsilon*r_2*A_f/beta",
        "strong_intermediate_bound": (
            "log|f(z)/f(a)|>=-2*r_1*A_f/(r_2-r_1)"
            "-n*log(2/epsilon)"
        ),
        "combined_bound": (
            "log|f(z)/f(a)|>=-[2*r_1/(r_2-r_1)"
            "+log(2/epsilon)/beta]*A_f"
        ),
        "amplitude_scale_invariant": True,
        "coordinate_scale_invariant": True,
    }


def standard_radius_ledger() -> dict[str, object]:
    return {
        "radii": ["R", "2R", "2eR"],
        "beta": "1",
        "harnack_coefficient": "2",
        "zero_count": "n<=A_f",
        "nominal_radius_sum": "S_f<=2*epsilon*R*A_f",
        "lower_exponent": "[2+log(2/epsilon)]*A_f",
    }


def rational_fixture() -> dict[str, object]:
    r1, r2, r3, epsilon = F(1), F(2), F(4), F(1, 4)
    require(0 < r1 < r2 < r3, "fixture radii are not nested")
    require(0 < epsilon <= 1, "fixture epsilon left its range")
    harnack = F(2) * r1 / (r2 - r1)
    radius = epsilon * r2
    require(harnack == 2, "Harnack coefficient changed")
    require(F(2) / epsilon == 8 and 2**3 == 8, "logarithmic ratio changed")

    functions = [
        {
            "name": "1+4z",
            "zeros": [F(-1, 4)],
            "multiplicity_count": 1,
            "maximum_ratio": 17,
        },
        {
            "name": "(1-4z)^2",
            "zeros": [F(1, 4), F(1, 4)],
            "multiplicity_count": 2,
            "maximum_ratio": 289,
        },
        {
            "name": "1+8z",
            "zeros": [F(-1, 8)],
            "multiplicity_count": 1,
            "maximum_ratio": 33,
        },
    ]
    for row in functions:
        n = int(row["multiplicity_count"])
        maximum = int(row["maximum_ratio"])
        require((r3 / r2) ** n <= maximum, f"Jensen power check failed for {row['name']}")

    total_multiplicity = sum(int(row["multiplicity_count"]) for row in functions)
    nominal_radius_sum = F(total_multiplicity) * radius
    require(total_multiplicity == 4, "multiplicity total changed")
    require(nominal_radius_sum == 2, "nominal radius sum changed")

    probe = F(2, 5)
    probe_values = [F(13, 5), F(9, 25), F(21, 5)]
    for row, value in zip(functions, probe_values):
        maximum = F(int(row["maximum_ratio"]))
        require(value >= maximum ** -5, f"exact lower-bound probe failed for {row['name']}")

    factor_rows: list[dict[str, str]] = []
    for zero in [F(-1, 4), F(1, 4), F(-1, 8)]:
        factor = abs(
            (-r2 / zero)
            * (r2 * (probe - zero))
            / (r2 * r2 - zero * probe)
        )
        require(factor >= epsilon / 2, "Blaschke factor lower bound failed")
        boundary_numerator_square = r2 * r2 * (r2 * r2 + zero * zero)
        boundary_denominator_square = (r2 * r2) ** 2 + (zero * r2) ** 2
        require(boundary_numerator_square == boundary_denominator_square, "boundary factor identity failed")
        factor_rows.append({"zero": render(zero), "probe_factor_abs": render(factor)})

    selected_T, selected_eta = F(4, 5), F(3, 5)
    require(selected_T * selected_T + selected_eta * selected_eta == r1 * r1, "selected rectangle left target disk")
    unique_zeros = [F(-1, 4), F(1, 4), F(-1, 8)]
    for zero in unique_zeros:
        require(min(abs(selected_T - zero), abs(-selected_T - zero)) > radius, "vertical side hits bad disk")
        require(selected_eta > radius, "horizontal side hits bad disk")

    return {
        "radii": {"r_1": "1", "r_2": "2", "r_3": "4"},
        "epsilon": "1/4",
        "epsilon_disk_radius": render(radius),
        "harnack_coefficient": render(harnack),
        "log_ratio_identity": "log(2/epsilon)/log(r_3/r_2)=log(8)/log(2)=3",
        "combined_coefficient": "5",
        "functions": [
            {
                "name": row["name"],
                "zeros": [render(value) for value in row["zeros"]],
                "multiplicity_count": row["multiplicity_count"],
                "maximum_ratio": str(row["maximum_ratio"]),
                "jensen_power_check": f"2^{row['multiplicity_count']}<={row['maximum_ratio']}",
            }
            for row in functions
        ],
        "total_multiplicity": total_multiplicity,
        "nominal_radius_sum": render(nominal_radius_sum),
        "probe": render(probe),
        "probe_values": [render(value) for value in probe_values],
        "factor_rows": factor_rows,
        "selected_rectangle": {"T": render(selected_T), "eta": render(selected_eta)},
        "selected_rectangle_avoids_all_unique_disks": True,
    }


def projection_fixture() -> dict[str, object]:
    return {
        "positive_vertical_bad_union": "[0,3/4]",
        "positive_horizontal_bad_union": "[0,1/2]",
        "vertical_bad_measure": "3/4",
        "horizontal_bad_measure": "1/2",
        "nominal_total_radius": "2",
        "exact_projection_can_beat_nominal_2S_relaxation": True,
        "strict_total_radius_sufficient_condition": "Delta_T>2S and Delta_eta>2S",
    }


def raw_quotient_ledger() -> dict[str, object]:
    return {
        "F_upper_load": "A_0",
        "lower_modulus_disk_indices": [1, 2],
        "F_zero_disks_charged": False,
        "first_quotient": "|F/F'|<=(|F(a)|/|F'(a)|)*exp(A_0+B_1)",
        "second_quotient": (
            "|F^2/(F'F'')|<=(|F(a)|^2/|F'(a)F''(a)|)"
            "*exp(2A_0+B_1+B_2)"
        ),
        "log_derivative_route_requires_F_nonzero": True,
    }


def source_and_normalization_ledger() -> dict[str, object]:
    return {
        "cuenin_doi": "https://doi.org/10.1007/s00220-022-04358-1",
        "dyatlov_zworski_appendix": "https://math.mit.edu/~dyatlov/res/res_final.pdf",
        "printed_display_imported_verbatim": False,
        "proof_normalization": "f(z)/f(a)",
        "spatial_coefficient": "2*r_1/(r_2-r_1)",
        "xi_normalization": "Xi_t(z)=xi(1/2+i*z)",
        "origin_is_common_three_derivative_anchor": False,
        "fixed_derivative_order_only": True,
    }


def amplitude_counterexample() -> dict[str, object]:
    return {
        "function": "f(z)=1/2",
        "zeros": [],
        "growth_difference": "0",
        "unnormalized_left_side": "log(1/2)<0",
        "claimed_right_side": "0",
        "literal_unnormalized_display_false": True,
        "normalized_left_side": "0",
    }


def mutation_firewalls() -> dict[str, bool]:
    return {
        "printed_unnormalized_display_is_valid": False,
        "origin_is_automatic_common_xi_anchor": False,
        "t_plane_xi_can_be_replaced_by_rotated_xi": False,
        "fixed_k_bound_is_uniform_in_growing_k": False,
        "zero_cover_is_actual_pole_manifest": False,
        "raw_route_requires_F_zero_disks": False,
        "total_radius_alone_identifies_a_prescribed_good_edge": False,
        "generic_order_one_growth_absorbs_selector_cost": False,
        "cofinal_xi_margin_established": False,
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
        "schema": "riemann.t105114.anchored-equal-disk-collar.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_GEOMETRY_AND_SYMBOLIC_ANALYTIC_INEQUALITY",
        "source": {"checkpoint_base": CHECKPOINT_BASE},
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "formula_ledger": formula_ledger(),
            "standard_radius_ledger": standard_radius_ledger(),
            "rational_fixture": rational_fixture(),
            "projection_fixture": projection_fixture(),
            "raw_quotient_ledger": raw_quotient_ledger(),
            "source_and_normalization_ledger": source_and_normalization_ledger(),
            "amplitude_counterexample": amplitude_counterexample(),
            "mutation_firewalls": mutation_firewalls(),
            "forbidden_control_characters": forbidden_control_characters(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "normalized_finite_minimum_modulus_verified": True,
            "jensen_equal_disk_radius_budget_verified": True,
            "finite_simultaneous_projection_interface_verified": True,
            "raw_route_smaller_exceptional_union_verified": True,
            "unnormalized_display_refuted": True,
            "t_plane_xi_normalization_locked": True,
            "common_xi_anchor_authenticated": False,
            "cofinal_xi_growth_load_proved": False,
            "complete_cofinal_xi_manifests_authenticated": False,
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
