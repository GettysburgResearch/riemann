#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

VERDICT = "PASS_T91880_EXPLICIT_NATIVE_TWO_SORTED_COUPLING"

MUTATIONS = (
    "erase_q2_obstruction",
    "bonus_given_declared_score",
    "rough_lift_parent",
    "bulk_causal_reset",
    "missing_native_occurrence",
    "duplicate_incidence",
    "double_child_coefficient",
    "missing_first_owner",
    "owner_injectivity_requirement",
    "label_dependent_quantizer",
    "second_quantizer",
    "bonus_not_identity",
    "drop_small_q",
    "branchwise_detail",
    "row_id_changed",
    "terminal_reversed",
    "signed_error_as_source",
    "cost_gate_failed",
    "wrong_endpoint_orientation",
    "benchmark_bridge",
)

class ContractError(ValueError):
    pass

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def scale(c, a):
    return tuple(c * x for x in a)

def q2_obstruction() -> dict[str, str]:
    getcontext().prec = 80
    rt2 = Decimal(2).sqrt()
    value = Decimal(3) * (Decimal(1) - rt2) / (Decimal(4) * rt2 - Decimal(3))
    if not value < 0:
        raise ContractError("q=2 Hall-score obstruction lost")
    return {
        "formula": "3(1-sqrt(2))/(4sqrt(2)-3)",
        "directed_decimal": str(value),
        "sign": "negative",
    }

def validate(packet: dict[str, Any], mutation: str | None = None) -> dict[str, Any]:
    p = copy.deepcopy(packet)

    if mutation == "erase_q2_obstruction":
        p["q2_required"] = False
    if not p["q2_required"]:
        raise ContractError("mandatory q=2 regression absent")
    obstruction = q2_obstruction()

    F = Fraction

    target_even = F(p["anchored"]["target_even"])
    target_odd = F(p["anchored"]["target_odd"])
    flow = F(p["anchored"]["flow"])
    if flow != target_odd or flow > target_even:
        raise ContractError("Hall marginal")
    residual_target = target_even - flow

    score_per_target_even = F(p["anchored"]["score_per_target_even"])
    score_per_target_odd = F(p["anchored"]["score_per_target_odd"])
    if score_per_target_even > score_per_target_odd:
        raise ContractError("score ordering")
    residual_score = residual_target * score_per_target_even
    signed_score = target_even * score_per_target_even - target_odd * score_per_target_odd
    score_surplus = residual_score - signed_score
    if score_surplus < 0:
        raise ContractError("residual source is not score-superordinate")

    row_even = tuple(F(x) for x in p["anchored"]["row_per_target_even"])
    row_odd = tuple(F(x) for x in p["anchored"]["row_per_target_odd"])
    bonus = scale(flow, sub(row_even, row_odd))
    if any(x < 0 for x in bonus):
        raise ContractError("negative Hall row bonus")
    signed_row = sub(scale(target_even, row_even), scale(target_odd, row_odd))
    residual_row = scale(residual_target, row_even)
    if add(residual_row, bonus) != signed_row:
        raise ContractError("two-sorted Hall row identity")

    if mutation == "bonus_given_declared_score":
        p["anchored"]["bonus_declared_score"] = "1"
    if F(p["anchored"]["bonus_declared_score"]) != 0:
        raise ContractError("row-only bonus was assigned declared-score packet mass")

    plus = {k: F(v) for k, v in p["bulk"]["plus"].items()}
    minus = {k: F(v) for k, v in p["bulk"]["minus"].items()}
    Pp = sum(plus.values())
    Pm = sum(minus.values())
    if Pp <= Pm:
        raise ContractError("bulk residual not positive")
    coupling = {(o, e): minus[o] * plus[e] / Pp for o in minus for e in plus}
    for o, mass in minus.items():
        if sum(v for (oo, _), v in coupling.items() if oo == o) != mass:
            raise ContractError("bulk negative marginal")
    residual = {
        e: plus[e] - sum(v for (_, ee), v in coupling.items() if ee == e)
        for e in plus
    }
    if any(v < 0 for v in residual.values()) or sum(residual.values()) != Pp - Pm:
        raise ContractError("bulk residual marginal")
    feature = tuple(F(x) for x in p["bulk"]["feature"])
    bulk_output = scale(Pp - Pm, feature)

    if mutation == "bulk_causal_reset":
        p["bulk"]["causal_reset"] = True
    if p["bulk"]["causal_reset"]:
        raise ContractError("forbidden causal reset on Volterra packet")

    if mutation == "rough_lift_parent":
        p["native_parent"] = "rough_lift"
    if p["native_parent"] != "finite_volterra_hybrid":
        raise ContractError("rough lift substituted for native marginal")

    occurrences = set(p["occurrences"])
    anchored = set(p["anchored_occurrences"])
    bulk = set(p["bulk_occurrences"])
    if mutation == "missing_native_occurrence":
        anchored.pop()
    if anchored & bulk or anchored | bulk != occurrences:
        raise ContractError("native sector partition")

    incidence = dict(p["incidence_owner"])
    if mutation == "duplicate_incidence":
        incidence[next(iter(incidence))] = ["edge-1", "edge-2"]
    if set(incidence) != occurrences or any(isinstance(v, list) for v in incidence.values()):
        raise ContractError("source occurrence not owned exactly once")

    first_owner = dict(p["first_owner"])
    if mutation == "missing_first_owner":
        first_owner.pop(next(iter(first_owner)))
    required_rough = set(p["rough_occurrences"])
    if set(first_owner) != required_rough:
        raise ContractError("first-owner domain")
    if mutation == "owner_injectivity_requirement":
        p["require_owner_values_injective"] = True
    if p["require_owner_values_injective"]:
        raise ContractError("invalid injectivity requirement for first owners")
    if len(set(first_owner.values())) == len(first_owner.values()):
        raise ContractError("fixture must exercise many-to-one first ownership")

    child_coeff = {k: F(v) for k, v in p["child_coefficient"].items()}
    child_applications = dict(p["child_coefficient_applications"])
    if mutation == "double_child_coefficient":
        key = next(iter(child_applications))
        child_applications[key] = 2
    if any(child_applications.get(k) != 1 for k in child_coeff):
        raise ContractError("child coefficient applied more than once")
    if sum(child_coeff.values()) >= F(1, 8):
        raise ContractError("child coefficient mass not subcritical")

    quantizers = int(p["realization"]["quantizer_count"])
    if mutation == "second_quantizer":
        quantizers = 2
    if quantizers != 1:
        raise ContractError("more than one realization operator")
    if mutation == "label_dependent_quantizer":
        p["realization"]["label_dependent"] = True
    if p["realization"]["label_dependent"]:
        raise ContractError("label-dependent bulk quantizer")
    if mutation == "bonus_not_identity":
        p["realization"]["bonus_channel"] = "bulk"
    if p["realization"]["bonus_channel"] != "identity":
        raise ContractError("Hall bonus not carried by identity channel")

    row_id = p["row_id"]
    downstream_ids = dict(p["downstream_row_ids"])
    if mutation == "row_id_changed":
        downstream_ids["y4"] = row_id + "-other"
    if any(v != row_id for v in downstream_ids.values()):
        raise ContractError("different realized rows used downstream")

    K = int(p["K"])
    qmax = int(p["qmax"])
    ordinary = {int(q): F(v) for q, v in p["ordinary"].items()}
    detail = {int(q): F(v) for q, v in p["detail"].items()}
    if mutation == "drop_small_q":
        ordinary.pop(2)
    required = set(range(2, qmax + 1))
    if set(ordinary) != required or not set(range(2, K)).issubset(ordinary):
        raise ContractError("q<K coverage missing")
    if mutation == "branchwise_detail":
        detail[2] += 1
    for q in required:
        expected = ordinary[q] - 2 * ordinary.get(4 * q, F(0))
        if detail[q] != expected:
            raise ContractError("detail not formed from common ordinary row")

    omega = {int(q): F(v) for q, v in p["omega"].items()}
    slack = {q: omega[q] - detail[q] for q in required}
    if any(v < 0 for v in slack.values()):
        raise ContractError("negative detail complement")

    terminal_removed = int(p["terminal_removed"])
    terminal_overfill = int(p["terminal_overfill"])
    if mutation == "terminal_reversed":
        terminal_removed, terminal_overfill = terminal_overfill, terminal_removed
    if terminal_removed - terminal_overfill != 581:
        raise ContractError("terminal reserve")

    if mutation == "signed_error_as_source":
        p["signed_error_source_positive"] = True
    if p["signed_error_source_positive"]:
        raise ContractError("signed comparison promoted to source")

    cost_classes = {k: int(v) for k, v in p["native_cost_classes"].items()}
    native_total = sum(cost_classes.values())
    if mutation == "cost_gate_failed":
        native_total = 60989
    if native_total >= 60989:
        raise ContractError("native cost gate")

    if mutation == "wrong_endpoint_orientation":
        p["endpoint_orientation"] = "native_deficit<=F_Lambda"
    if p["endpoint_orientation"] != "F_Lambda<=native_deficit":
        raise ContractError("wrong endpoint orientation")

    if mutation == "benchmark_bridge":
        p["benchmark_bridge"] = True
    if p["benchmark_bridge"]:
        raise ContractError("forbidden benchmark bridge")

    return {
        "bulk_output": [str(x) for x in bulk_output],
        "child_mass": str(sum(child_coeff.values())),
        "native_total": native_total,
        "q2_obstruction": obstruction,
        "row_bonus": [str(x) for x in bonus],
        "row_id": row_id,
        "score_surplus": str(score_surplus),
        "terminal_margin": terminal_removed - terminal_overfill,
    }

def base_packet() -> dict[str, Any]:
    F = Fraction
    qmax = 24
    K = 8
    ordinary = {q: F(500 - 3 * q, 20) for q in range(2, qmax + 1)}
    detail = {q: ordinary[q] - 2 * ordinary.get(4 * q, F(0)) for q in ordinary}
    omega = {q: detail[q] + F(1, q + 11) for q in ordinary}
    occurrences = ["a1", "a2", "a3", "b1", "b2"]
    return {
        "q2_required": True,
        "native_parent": "finite_volterra_hybrid",
        "anchored": {
            "target_even": "5",
            "target_odd": "3",
            "flow": "3",
            "score_per_target_even": "6/5",
            "score_per_target_odd": "3/2",
            "row_per_target_even": ["7/5", "8/5", "2"],
            "row_per_target_odd": ["1", "6/5", "3/2"],
            "bonus_declared_score": "0",
        },
        "bulk": {
            "plus": {"e1": "5", "e2": "4"},
            "minus": {"o1": "3", "o2": "2"},
            "feature": ["2", "3", "5"],
            "causal_reset": False,
        },
        "occurrences": occurrences,
        "anchored_occurrences": ["a1", "a2", "a3"],
        "bulk_occurrences": ["b1", "b2"],
        "incidence_owner": {
            "a1": "anchored-residual",
            "a2": "anchored-edge",
            "a3": "anchored-child",
            "b1": "bulk-edge",
            "b2": "bulk-residual",
        },
        "rough_occurrences": ["67", "4691", "4757"],
        "first_owner": {"67": "67", "4691": "67", "4757": "67"},
        "require_owner_values_injective": False,
        "child_coefficient": {"child-67": "1/20", "child-71": "1/40"},
        "child_coefficient_applications": {"child-67": 1, "child-71": 1},
        "realization": {
            "quantizer_count": 1,
            "label_dependent": False,
            "anchor_channel": "identity",
            "bonus_channel": "identity",
            "bulk_channel": "markov",
        },
        "row_id": "rid-X-native-two-sorted",
        "downstream_row_ids": {
            "comparison": "rid-X-native-two-sorted",
            "terminal": "rid-X-native-two-sorted",
            "complement": "rid-X-native-two-sorted",
            "y4": "rid-X-native-two-sorted",
            "endpoint": "rid-X-native-two-sorted",
        },
        "K": K,
        "qmax": qmax,
        "ordinary": {str(k): str(v) for k, v in ordinary.items()},
        "detail": {str(k): str(v) for k, v in detail.items()},
        "omega": {str(k): str(v) for k, v in omega.items()},
        "terminal_removed": 5033,
        "terminal_overfill": 4452,
        "signed_error_source_positive": False,
        "native_cost_classes": {
            "thinning": 12012,
            "nonterminal_signed": 3,
            "terminal_signed": 48972,
            "positive_omissions": 1,
            "identity_channels": 0,
            "port": 0,
        },
        "endpoint_orientation": "F_Lambda<=native_deficit",
        "benchmark_bridge": False,
    }

def run(output: Path | None = None, mutations: bool = True) -> dict[str, Any]:
    packet = base_packet()
    baseline = validate(packet)
    rejected = []
    if mutations:
        for mutation in MUTATIONS:
            try:
                validate(packet, mutation)
            except ContractError:
                rejected.append(mutation)
            else:
                raise AssertionError(f"hostile mutation survived: {mutation}")
    payload = {
        "arithmetic_class": "EXACT_FRACTION_PLUS_DIRECTED_DECIMAL_Q2",
        "classification": VERDICT,
        "baseline": baseline,
        "hostile_mutations_rejected": len(rejected),
        "mutations": rejected,
        "rh_established_by_replay": False,
        "scope": "finite algebra and type firewalls; frozen analytic inputs are not replayed",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = sha256(canonical).hexdigest()
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()
    payload = run(args.output, mutations=args.mutations)
    print(payload["classification"])
    print(payload["proof_object_sha256"])

if __name__ == "__main__":
    main()
