#!/usr/bin/env python3
"""Exact finite-algebra replay for the Target-Lorenz native endpoint packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def greedy_remove(targets: list[Fraction], demand: Fraction) -> list[Fraction]:
    assert 0 <= demand <= sum(targets)
    out: list[Fraction] = []
    remaining = demand
    for target in targets:
        take = min(target, remaining)
        out.append(take / target)
        remaining -= take
    assert remaining == 0
    return out


def vector_sum(coeffs: list[Fraction], vectors: list[tuple[Fraction, ...]]) -> tuple[Fraction, ...]:
    return tuple(sum(c * v[k] for c, v in zip(coeffs, vectors)) for k in range(len(vectors[0])))


def check_leaf_fixture(
    even_targets: list[Fraction],
    even_rows: list[tuple[Fraction, ...]],
    odd_targets: list[Fraction],
    odd_rows: list[tuple[Fraction, ...]],
) -> dict:
    demand = sum(odd_targets)
    used = greedy_remove(even_targets, demand)
    used_row = vector_sum(used, even_rows)
    odd_row = tuple(sum(v[k] for v in odd_rows) for k in range(len(odd_rows[0])))
    bonus = tuple(a - b for a, b in zip(used_row, odd_row))
    assert all(x >= 0 for x in bonus)

    residual_coeff = [Fraction(1) - u for u in used]
    residual_row = vector_sum(residual_coeff, even_rows)
    even_row = tuple(sum(v[k] for v in even_rows) for k in range(len(even_rows[0])))
    signed_row = tuple(a - b for a, b in zip(even_row, odd_row))
    physical = tuple(a + b for a, b in zip(residual_row, bonus))
    assert physical == signed_row
    assert all(x >= 0 for x in physical)
    assert sum(c * t for c, t in zip(residual_coeff, even_targets)) == sum(even_targets) - demand
    return {
        "used": [str(x) for x in used],
        "bonus": [str(x) for x in bonus],
        "physical": [str(x) for x in physical],
    }


def exact_source_fubini() -> dict:
    fixtures = [
        (
            [Fraction(5), Fraction(4), Fraction(3)],
            [(Fraction(20), Fraction(15), Fraction(10)), (Fraction(12), Fraction(8), Fraction(4)), (Fraction(6), Fraction(3), Fraction(1))],
            [Fraction(2), Fraction(3)],
            [(Fraction(5), Fraction(3), Fraction(2)), (Fraction(6), Fraction(3), Fraction(1))],
        ),
        (
            [Fraction(7), Fraction(5), Fraction(4), Fraction(2)],
            [(Fraction(28), Fraction(21), Fraction(14)), (Fraction(15), Fraction(10), Fraction(5)),
             (Fraction(8), Fraction(4), Fraction(2)), (Fraction(2), Fraction(1), Fraction(0))],
            [Fraction(3), Fraction(4)],
            [(Fraction(8), Fraction(5), Fraction(3)), (Fraction(7), Fraction(4), Fraction(2))],
        ),
    ]
    weights = [Fraction(3, 5), Fraction(7, 11)]
    records = [check_leaf_fixture(*fixture) for fixture in fixtures]
    total = []
    for k in range(len(records[1]["physical"])):
        total.append(sum(w * Fraction(rec["physical"][k]) for w, rec in zip(weights, records)))
    assert all(x >= 0 for x in total)
    return {
        "leaf_count": len(records),
        "records": records,
        "weighted_common_parent": [str(x) for x in total],
    }


def check_two_ledgers() -> dict:
    source_stages = {
        "target_lorenz_leaf": "positive_source",
        "bottom_omission": "positive_source",
        "top_omission": "positive_source",
        "common_thinning": "positive_source",
        "positive_quantizer": "positive_source",
    }
    observation_stages = {
        "retained_cell_mismatch": "signed_observation",
        "intrinsic_collar_comparison": "signed_observation",
        "terminal_comparison": "signed_observation",
    }
    assert set(source_stages.values()) == {"positive_source"}
    assert set(observation_stages.values()) == {"signed_observation"}
    assert set(source_stages).isdisjoint(observation_stages)
    return {"source_stages": source_stages, "observation_stages": observation_stages}


def check_native_reserve() -> dict:
    # Exact algebra in s=sqrt(K)>0:
    # [s/(s+130)] [1+129/s] = (s+129)/(s+130) < 1.
    for s in [Fraction(1), Fraction(2), Fraction(10), Fraction(1000), Fraction(10**9)]:
        used = s / (s + 130) * (1 + Fraction(129, 1) / s)
        reserve = 1 - used
        assert used == (s + 129) / (s + 130)
        assert reserve == Fraction(1, 1) / (s + 130) > 0
    return {
        "identity": "tau_s*(1+129/s)=(s+129)/(s+130)",
        "relative_reserve": "1/(s+130)",
        "ordinary_from_detail": "positive radix-four inverse",
    }


def check_native_cost() -> dict:
    charges = {
        "square_root_thinning": 12012,
        "nonterminal_signed_comparison": 4,
        "terminal_signed_comparison": 4452 * 11,
        "positive_omissions": 1,
        "port_and_large_endpoint_base": 0,
    }
    total = sum(charges.values())
    assert charges["terminal_signed_comparison"] == 48972
    assert total == 60989
    assert total < 61000
    return {"charges": charges, "total": total, "published_bound": 61000}


def validate_packet(packet: dict) -> bool:
    if any(stage["type"] != "positive_source" for stage in packet["source_stages"]):
        return False
    if any(stage["type"] != "signed_observation" for stage in packet["observation_stages"]):
        return False
    owners = [stage["owner"] for stage in packet["source_stages"]]
    if len(owners) != len(set(owners)):
        return False
    if packet["child_convention"] != "actual_response_internal_colour":
        return False
    if packet["root_global_port"] != 0:
        return False
    if packet["exported_recursive_family_size"] != 0:
        return False
    if not packet["covers_small_columns_q_below_K"]:
        return False
    if not packet["slack_defined_after_all_column_feasibility"]:
        return False
    if packet["uses_rh_bearing_benchmark_bridge"]:
        return False
    return True


def hostile_mutations() -> dict:
    baseline = {
        "source_stages": [
            {"name": "target_lorenz_leaf", "type": "positive_source", "owner": "leaf"},
            {"name": "bottom_omission", "type": "positive_source", "owner": "bottom"},
            {"name": "top_omission", "type": "positive_source", "owner": "top"},
            {"name": "common_thinning", "type": "positive_source", "owner": "thin"},
            {"name": "positive_quantizer", "type": "positive_source", "owner": "quantizer"},
        ],
        "observation_stages": [
            {"name": "retained_cell_mismatch", "type": "signed_observation"},
            {"name": "intrinsic_collar", "type": "signed_observation"},
            {"name": "terminal_comparison", "type": "signed_observation"},
        ],
        "child_convention": "actual_response_internal_colour",
        "root_global_port": 0,
        "exported_recursive_family_size": 0,
        "covers_small_columns_q_below_K": True,
        "slack_defined_after_all_column_feasibility": True,
        "uses_rh_bearing_benchmark_bridge": False,
    }
    assert validate_packet(baseline)

    import copy
    mutations: dict[str, bool] = {}

    p = copy.deepcopy(baseline)
    p["source_stages"].append({"name": "mismatch", "type": "signed_observation", "owner": "mismatch"})
    mutations["signed_observation_relabelled_positive_source"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["source_stages"][1]["owner"] = "leaf"
    mutations["duplicate_source_owner"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["child_convention"] = "full_child_capacity"
    mutations["full_child_capacity_substituted_for_actual_response"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["root_global_port"] = 1
    mutations["root_port_made_nonzero"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["exported_recursive_family_size"] = 1
    mutations["exported_recursive_family_made_nonempty"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["covers_small_columns_q_below_K"] = False
    mutations["small_columns_q_below_K_omitted"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["slack_defined_after_all_column_feasibility"] = False
    mutations["native_slack_defined_before_feasibility"] = not validate_packet(p)

    p = copy.deepcopy(baseline)
    p["uses_rh_bearing_benchmark_bridge"] = True
    mutations["rh_bearing_benchmark_bridge_imported"] = not validate_packet(p)

    assert all(mutations.values())
    return mutations


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=RESULT)
    args = parser.parse_args()

    payload = {
        "arithmetic_class": "EXACT_RATIONAL_AND_TYPED_LEDGER",
        "classification": "PASS_TARGET_LORENZ_TWO_LEDGER_NATIVE_ENDPOINT_PACKET",
        "source_fubini": exact_source_fubini(),
        "two_ledger_types": check_two_ledgers(),
        "native_reserve": check_native_reserve(),
        "native_cost": check_native_cost(),
        "exported_recursive_family_size": 0,
        "root_global_port_demand": 0,
        "hostile_mutations_detected": hostile_mutations(),
        "endpoint_currency": "J_Lambda(X)-H(d_X)=<Y4,Omega_X-Xi(d_X)>",
        "forbidden_currency": "J_Lambda(X)-4sqrt(X)",
        "replay_scope": (
            "checks exact common-source/Fubini algebra, mathematical types, reserve and "
            "cost constants; it does not independently replay the analytic endpoint frame, "
            "the compact/tail AVLT certificates or the Mellin-Landau consumer"
        ),
        "rh_established_by_replay": False,
    }
    payload["proof_object_sha256"] = canonical_hash(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
