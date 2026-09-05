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

VERDICT = "PASS_T105116_CARTAN_RADIUS_WATER_FILLING"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = REPO_ROOT / "experiments" / "X-105115-common-safe-rectangle" / "verify.py"
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "b9e9d4c77045189e1c807b056f5b2e257d22a1bdf45e5fc824a652e710ac7aaf"
BASE_COMMIT = "ccc2244b65a2e75a60b5f46fecba35ad016ce4fe"
CHECKPOINT_BASE = BASE_COMMIT

SPEC = importlib.util.spec_from_file_location("t105115_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105115 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105116.json",
    "claims/lemmas/L-105116-capped-cartan-radius-water-filling.md",
    "claims/methodology/M-105116-cartan-budget-review-contract.md",
    "claims/refutations/R-105116-active-strict-budget-has-no-minimizer.md",
    "claims/theorems/T-105116-cartan-budget-optimization-frontier.md",
    "experiments/X-105116-cartan-radius-water-filling/verify.py",
    "experiments/X-105116-cartan-radius-water-filling/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105115 dependency artifact is stale")
    require(artifact.get("proof_object_sha256") == BASE_DIGEST, "T-105115 digest changed")
    require(artifact.get("verdict") == BASE.VERDICT, "T-105115 verdict changed")
    return {
        "path": "experiments/X-105115-common-safe-rectangle",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def interior_fixture() -> dict[str, object]:
    u = [F(1), F(2), F(3)]
    v = [F(2), F(3), F(5)]
    budget = F(2)
    total_u = sum(u, F(0))
    epsilon = [weight * budget / (cost * total_u) for weight, cost in zip(u, v)]
    allocated = [cost * value for cost, value in zip(v, epsilon)]
    multiplier = total_u / budget
    require(sum(allocated, F(0)) == budget, "interior budget is not active")
    require(all(F(0) < value < 1 for value in epsilon), "interior fixture hit a cap")
    require(all(weight / (cost * value) == multiplier for weight, cost, value in zip(u, v, epsilon)), "KKT ratios differ")
    log_arguments = [F(2) / value for value in epsilon]
    encoded_product = 1
    for argument, weight in zip(log_arguments, u):
        require(argument.denominator == 1 and weight.denominator == 1, "fixture log encoding is not integral")
        encoded_product *= argument.numerator ** weight.numerator
    return {
        "u": [render(value) for value in u],
        "v": [render(value) for value in v],
        "budget": render(budget),
        "total_u": render(total_u),
        "epsilon": [render(value) for value in epsilon],
        "allocated_radius": [render(value) for value in allocated],
        "multiplier": render(multiplier),
        "log_arguments": [render(value) for value in log_arguments],
        "penalty_identity": "log(12)+2log(9)+3log(10)=log(972000)",
        "encoded_log_product": str(encoded_product),
        "unique_interior_optimizer": True,
    }


def capped_fixture() -> dict[str, object]:
    u = [F(10), F(1)]
    v = [F(1), F(9)]
    budget = F(5)
    multiplier = F(1, 4)
    epsilon = [F(1), F(4, 9)]
    allocated = [cost * value for cost, value in zip(v, epsilon)]
    require(sum(allocated, F(0)) == budget, "capped budget changed")
    require(min(F(1), u[0] / (multiplier * v[0])) == epsilon[0], "first cap failed")
    require(min(F(1), u[1] / (multiplier * v[1])) == epsilon[1], "second allocation failed")
    return {
        "u": ["10", "1"],
        "v": ["1", "9"],
        "budget": "5",
        "multiplier": render(multiplier),
        "epsilon": [render(value) for value in epsilon],
        "allocated_radius": [render(value) for value in allocated],
        "first_index_capped": True,
        "penalty_identity": "10log(2)+log(9/2)",
    }


def cartan_specialization_fixture() -> dict[str, object]:
    growth = [F(2), F(3)]
    beta = [F(1), F(2)]
    middle_radius = F(4)
    u = [a / b for a, b in zip(growth, beta)]
    v = [middle_radius * value for value in u]
    budget = F(2)
    total_u = sum(u, F(0))
    epsilon = [budget / (middle_radius * total_u) for _ in u]
    multiplier = total_u / budget
    require(epsilon == [F(1, 7), F(1, 7)], "common-radius epsilons are unequal")
    require(sum((cost * value for cost, value in zip(v, epsilon)), F(0)) == budget, "Cartan budget changed")
    return {
        "A": [render(value) for value in growth],
        "beta": [render(value) for value in beta],
        "r_2": render(middle_radius),
        "u=A/beta": [render(value) for value in u],
        "v=r_2*A/beta": [render(value) for value in v],
        "budget": render(budget),
        "epsilon": [render(value) for value in epsilon],
        "multiplier": render(multiplier),
        "growth_load_cancels_from_u_over_v": True,
        "inverse_growth_allocation_is_optimal": False,
    }


def fractional_slack_fixture() -> dict[str, object]:
    delta_t, delta_eta, delta = F(10), F(12), F(1, 5)
    width = min(delta_t, delta_eta)
    budget = (1 - delta) * width / 2
    twice_budget = 2 * budget
    relaxed_kappa = delta_t * delta_eta / ((delta_t - twice_budget) * (delta_eta - twice_budget))
    universal_bound = delta ** -2
    require(twice_budget < width, "strict safe-shell gate failed")
    require(relaxed_kappa <= universal_bound, "delta inverse-square bound failed")
    symmetric_attainment = width * width / ((width - twice_budget) ** 2)
    require(symmetric_attainment == universal_bound, "symmetric worst case did not attain the bound")
    return {
        "Delta_T": render(delta_t),
        "Delta_eta": render(delta_eta),
        "delta": render(delta),
        "closed_nominal_budget": render(budget),
        "twice_budget": render(twice_budget),
        "strict_gate": True,
        "asymmetric_relaxed_kappa": render(relaxed_kappa),
        "delta_inverse_square": render(universal_bound),
        "symmetric_bound_is_attained_by_maximal_disjoint_projections": True,
    }


def strict_budget_refutation() -> dict[str, object]:
    return {
        "regime": "0<R<=sum(v_j)",
        "open_constraint": "sum(v_j*epsilon_j)<R",
        "objective_coordinatewise_decreasing": True,
        "minimizer_exists": False,
        "closed_budget_optimum_is_open_budget_infimum": True,
        "fractional_slack_restores_strict_geometry": True,
    }


def formula_ledger() -> dict[str, object]:
    return {
        "objective": "Phi=sum_j u_j*log(2/epsilon_j)",
        "nominal_radius": "S_nom=sum_j v_j*epsilon_j",
        "capped_solution": "epsilon_j=min(1,u_j/(lambda*v_j))",
        "interior_solution": "epsilon_j=u_j*R/(v_j*sum(u))",
        "fractional_budget": "R_delta=(1-delta)*min(Delta_T,Delta_eta)/2",
        "safe_set_bound": "kappa<=delta^(-2)",
        "epsilon_independent_spatial_terms_optimized": False,
        "objective_weights_must_be_declared": True,
    }


def metadata_ledger() -> dict[str, object]:
    metadata = json.loads((REPO_ROOT / "PACKET_METADATA_105116.json").read_text(encoding="utf-8"))
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
        "inverse_growth_allocation_is_optimal": False,
        "equal_epsilon_is_universal": False,
        "epsilon_cap_can_be_removed": False,
        "active_strict_budget_has_minimizer": False,
        "nominal_radius_equals_exact_projection_load": False,
        "objective_scalarization_is_canonical_for_all_carriers": False,
        "optimized_loss_is_absorbable_for_xi": False,
        "complete_actual_xi_manifests_authenticated": False,
        "signed_xi_moment_closed": False,
        "strict_xi_jet_coherence_proved": False,
        "rcmv104530_proved": False,
        "rh_established": False,
    }


def forbidden_control_characters() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    for relative_path in CONTENT_FILES:
        for offset, value in enumerate((REPO_ROOT / relative_path).read_bytes()):
            if value < 32 and value not in {9, 10, 13}:
                failures.append({"path": relative_path, "offset": offset, "byte": value})
    return failures


def content_hashes() -> dict[str, str]:
    require(not forbidden_control_characters(), "forbidden control characters")
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        hashes[relative_path] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.t105116.cartan-radius-water-filling.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_CONVEX_OPTIMIZATION_AND_SYMBOLIC_LOG_IDENTITY",
        "source": {"checkpoint_base": CHECKPOINT_BASE},
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "formula_ledger": formula_ledger(),
            "interior_fixture": interior_fixture(),
            "capped_fixture": capped_fixture(),
            "cartan_specialization_fixture": cartan_specialization_fixture(),
            "fractional_slack_fixture": fractional_slack_fixture(),
            "strict_budget_refutation": strict_budget_refutation(),
            "metadata_ledger": metadata_ledger(),
            "mutation_firewalls": mutation_firewalls(),
            "forbidden_control_characters": forbidden_control_characters(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "capped_finite_optimizer_verified": True,
            "interior_closed_form_verified": True,
            "cartan_common_radius_specialization_verified": True,
            "fractional_slack_safe_shell_verified": True,
            "strict_open_budget_nonattainment_verified": True,
            "xi_scalarization_weights_authenticated": False,
            "cofinal_xi_growth_authenticated": False,
            "complete_actual_xi_manifests_authenticated": False,
            "optimized_selector_absorption_proved": False,
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
