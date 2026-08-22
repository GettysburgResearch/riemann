#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105104_JET_COHERENCE_REVERSE_ROLLE"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105103-confluent-residue-ledger"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "e208cceb8b09c639f6587024e5bef334a37d650435453515f68b8f42512c53c2"
BASE_COMMIT = "eafd6d86055179e5b2fa9b3747ea740b8609ba64"

SPEC = importlib.util.spec_from_file_location("t105103_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105103 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105104.json",
    "claims/lemmas/L-105104-jet-coherence-reverse-rolle-transfer.md",
    "claims/methodology/M-105104-jet-transfer-review-contract.md",
    "claims/refutations/R-105104-ordinary-residues-cannot-see-flat-turn-orientation.md",
    "claims/theorems/T-105104-multiplicity-aware-transfer-frontier.md",
    "experiments/X-105104-jet-coherence-reverse-rolle/verify.py",
    "experiments/X-105104-jet-coherence-reverse-rolle/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105103 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105103 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def evaluate(coefficients: list[F], point: F) -> F:
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value * point + coefficient
    return value


def sign(value: F) -> int:
    return (value > 0) - (value < 0)


def ceil_fraction(value: F) -> int:
    return -((-value.numerator) // value.denominator)


def primitive_zero_count(
    coefficients: list[F],
    left: F,
    right: F,
    critical_points: list[F],
    expected_critical_points: list[F],
) -> dict[str, object]:
    require(left < right, "interval is not oriented")
    require(
        evaluate(coefficients, left) != 0 and evaluate(coefficients, right) != 0,
        "interval endpoint is a parent zero",
    )
    points = sorted(critical_points)
    expected = sorted(expected_critical_points)
    require(len(points) == len(set(points)), "critical manifest has a duplicate")
    require(
        len(expected) == len(set(expected)),
        "frozen expected critical manifest has a duplicate",
    )
    require(
        set(points) == set(expected),
        "critical manifest is incomplete or extraneous",
    )
    require(all(left < point < right for point in points), "critical point is outside")
    events = [BASE.local_event(coefficients, point) for point in points]
    require(
        all(int(event["orders"]["r"]) > 0 for event in events),
        "manifest contains a noncritical point",
    )
    nodes = [left, *points, right]
    values = [evaluate(coefficients, point) for point in nodes]
    edge_zeros = sum(
        values[index] * values[index + 1] < 0
        for index in range(len(values) - 1)
    )
    common = [
        event for event in events if int(event["orders"]["m"]) > 0
    ]
    common_multiplicity = sum(
        int(event["orders"]["m"]) for event in common
    )
    distinct = len(common) + edge_zeros
    multiplicity = common_multiplicity + edge_zeros
    for event in common:
        require(
            int(event["orders"]["m"]) == int(event["orders"]["r"]) + 1,
            "common derivative ladder changed",
        )
    return {
        "interval": [str(left), str(right)],
        "critical_points": [str(point) for point in points],
        "frozen_expected_critical_points": [str(point) for point in expected],
        "critical_events": events,
        "node_values": [str(value) for value in values],
        "strict_sign_change_edges": edge_zeros,
        "common_support_count": len(common),
        "common_parent_multiplicity": common_multiplicity,
        "distinct_real_zero_count": distinct,
        "multiplicity_real_zero_count": multiplicity,
        "primitive_identity_verified": True,
    }


def jet_event(coefficients: list[F], point: F) -> dict[str, object]:
    event = BASE.local_event(coefficients, point)
    m = int(event["orders"]["m"])
    r = int(event["orders"]["r"])
    require(m == 0 and r % 2 == 1, "event is not a noncommon odd-order turn")
    p_principal = event["P_principal_part"]
    q_principal = event["Q_principal_part"]
    require(p_principal, "eligible P principal part is empty")
    require(q_principal, "eligible Q principal part is empty")
    require(p_principal[0]["power"] == -r, "P leading power changed")
    require(q_principal[0]["power"] == -(2 * r - 1), "Q leading power changed")
    rho_jet = F(str(p_principal[0]["coefficient"]))
    q_lead = F(str(q_principal[0]["coefficient"]))
    require(q_lead == rho_jet**2 / r, "Q leading jet square changed")
    return {
        "point": str(point),
        "critical_order": r,
        "rho_jet": str(rho_jet),
        "good_turn": rho_jet < 0,
        "wrong_turn": rho_jet > 0,
        "P_leading_principal_coefficient": str(rho_jet),
        "P_leading_power": -r,
        "Q_leading_principal_coefficient": str(q_lead),
        "Q_leading_power": -(2 * r - 1),
        "ordinary_P_residue": event["P_residue"],
        "ordinary_Q_residue": event["Q_residue"],
        "local_event": event,
    }


def component_index(point: F, common_points: list[F]) -> int:
    return sum(common < point for common in common_points)


def turning_ledger(
    name: str,
    coefficients: list[F],
    left: F,
    right: F,
    critical_points: list[F],
    expected_critical_points: list[F],
) -> dict[str, object]:
    primitive = primitive_zero_count(
        coefficients,
        left,
        right,
        critical_points,
        expected_critical_points,
    )
    points = sorted(critical_points)
    events = [BASE.local_event(coefficients, point) for point in points]
    common_points = [
        point
        for point, event in zip(points, events)
        if int(event["orders"]["m"]) > 0
    ]
    common_order_mass = sum(
        int(event["orders"]["r"])
        for event in events
        if int(event["orders"]["m"]) > 0
    )
    eligible_points = [
        point
        for point, event in zip(points, events)
        if int(event["orders"]["m"]) == 0
        and int(event["orders"]["r"]) % 2 == 1
    ]
    neutral_events = [
        {
            "point": str(point),
            "critical_order": int(event["orders"]["r"]),
            "reason": "NONCOMMON_EVEN_ORDER_STATIONARY_EVENT",
        }
        for point, event in zip(points, events)
        if int(event["orders"]["m"]) == 0
        and int(event["orders"]["r"]) % 2 == 0
    ]
    jets = [jet_event(coefficients, point) for point in eligible_points]
    rho_values = [F(str(row["rho_jet"])) for row in jets]
    turn_count = len(jets)
    good_count = sum(value < 0 for value in rho_values)
    first_carrier = -sum(rho_values, F(0))
    second_moment = sum((value**2 for value in rho_values), F(0))
    coherence: F | None = None
    if turn_count * second_moment > 0:
        coherence = max(first_carrier, F(0)) ** 2 / (
            F(turn_count) * second_moment
        )
        require(F(0) <= coherence <= F(1), "jet coherence left [0,1]")
        require(
            F(good_count) >= F(turn_count) * coherence,
            "jet Cauchy sign bound failed",
        )

    active_components = sorted(
        {
            component_index(point, common_points)
            for point in eligible_points
        }
    )
    active_count = len(active_components)
    sharp_sign_lower = (
        common_order_mass
        + len(common_points)
        + 2 * good_count
        - turn_count
        - active_count
    )
    coarse_sign_lower = common_order_mass + 2 * good_count - turn_count - 1
    require(sharp_sign_lower >= coarse_sign_lower, "component cancellation failed")

    component_rows: list[dict[str, object]] = []
    component_moment_lower = common_order_mass + len(common_points)
    for index in active_components:
        values = [
            F(str(row["rho_jet"]))
            for point, row in zip(eligible_points, jets)
            if component_index(point, common_points) == index
        ]
        count = len(values)
        carrier = max(-sum(values, F(0)), F(0))
        moment = sum((value**2 for value in values), F(0))
        raw_lower = 2 * carrier**2 / moment - count - 1
        integer_lower = max(0, ceil_fraction(raw_lower))
        component_moment_lower += integer_lower
        component_rows.append(
            {
                "component_index": index,
                "turn_count": count,
                "first_carrier_positive_part": str(carrier),
                "second_moment": str(moment),
                "raw_moment_lower_bound": str(raw_lower),
                "nonnegative_integer_lower_bound": integer_lower,
            }
        )

    global_moment_lower: F | None = None
    if coherence is not None:
        global_moment_lower = (
            F(common_order_mass)
            + (2 * coherence - 1) * turn_count
            - 1
        )

    derivative_multiplicity = sum(int(event["orders"]["r"]) for event in events)
    multiplicity_defect = derivative_multiplicity - common_order_mass - turn_count
    require(multiplicity_defect >= 0, "multiplicity defect became negative")
    expected_defect = sum(
        (
            int(event["orders"]["r"])
            if int(event["orders"]["m"]) == 0
            and int(event["orders"]["r"]) % 2 == 0
            else int(event["orders"]["r"]) - 1
            if int(event["orders"]["m"]) == 0
            else 0
        )
        for event in events
    )
    require(multiplicity_defect == expected_defect, "multiplicity split failed")

    exact_count = int(primitive["multiplicity_real_zero_count"])
    require(exact_count >= sharp_sign_lower, f"sharp sign bound failed for {name}")
    require(exact_count >= coarse_sign_lower, f"coarse sign bound failed for {name}")
    require(
        exact_count >= component_moment_lower,
        f"component moment bound failed for {name}",
    )
    if global_moment_lower is not None:
        require(
            F(exact_count) >= global_moment_lower,
            f"global jet bound failed for {name}",
        )

    return {
        "name": name,
        "primitive_zero_count": primitive,
        "common_points": [str(point) for point in common_points],
        "common_derivative_order_mass": common_order_mass,
        "eligible_odd_noncommon_turns": jets,
        "eligible_turn_support_count": turn_count,
        "good_turn_count": good_count,
        "neutral_even_noncommon_events": neutral_events,
        "active_component_count": active_count,
        "jet_first_carrier": str(first_carrier),
        "jet_second_moment": str(second_moment),
        "jet_coherence": None if coherence is None else str(coherence),
        "sharp_sign_lower_bound": sharp_sign_lower,
        "coarse_sign_lower_bound": coarse_sign_lower,
        "component_moment_rows": component_rows,
        "componentwise_moment_lower_bound": component_moment_lower,
        "global_jet_moment_lower_bound": (
            None if global_moment_lower is None else str(global_moment_lower)
        ),
        "derivative_real_zero_multiplicity": derivative_multiplicity,
        "omitted_derivative_multiplicity_defect": multiplicity_defect,
        "exact_multiplicity_identity": (
            f"{derivative_multiplicity}="
            f"{common_order_mass}+{turn_count}+{multiplicity_defect}"
        ),
        "transfer_bounds_verified": True,
    }


def component_combinatorics() -> dict[str, object]:
    checked = 0
    minimum_slack: int | None = None
    by_length: dict[str, int] = {}
    for length in range(1, 9):
        accepted = 0
        for mask in range(1 << length):
            wrong = [bool(mask & (1 << index)) for index in range(length)]
            if any(wrong[index] and wrong[index + 1] for index in range(length - 1)):
                continue
            internal_zeros = sum(
                1 - int(wrong[index]) - int(wrong[index + 1])
                for index in range(length - 1)
            )
            good = length - sum(wrong)
            lower = 2 * good - length - 1
            slack = internal_zeros - lower
            require(slack >= 0, "component sign bound failed")
            minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
            checked += 1
            accepted += 1
        by_length[str(length)] = accepted
    require(minimum_slack == 0, "component certificate lacks a sharp row")
    return {
        "maximum_turn_count": 8,
        "valid_nonadjacent_wrong_patterns_checked": checked,
        "valid_patterns_by_length": by_length,
        "minimum_internal_edge_slack": minimum_slack,
        "bounded_enumeration_only": True,
    }


def ordinary_residue_no_go_firewall() -> dict[str, object]:
    epsilon = F(1, 64)
    plus = [epsilon, F(0), F(0), F(0), F(0), F(0), F(1)]
    minus = [-epsilon, F(0), F(0), F(0), F(0), F(0), F(1)]
    plus_ledger = turning_ledger(
        "x6_plus_1_over_64", plus, F(-1), F(1), [F(0)], [F(0)]
    )
    minus_ledger = turning_ledger(
        "x6_minus_1_over_64", minus, F(-1), F(1), [F(0)], [F(0)]
    )
    plus_event = plus_ledger["eligible_odd_noncommon_turns"][0]
    minus_event = minus_ledger["eligible_odd_noncommon_turns"][0]
    plus_oracle = BASE.infinity_residue_oracle(plus)
    minus_oracle = BASE.infinity_residue_oracle(minus)
    for event in (plus_event, minus_event):
        require(event["critical_order"] == 5, "sextic critical order changed")
        require(event["ordinary_P_residue"] == "0", "P residue sees sextic sign")
        require(event["ordinary_Q_residue"] == "0", "Q residue sees sextic sign")
        require(
            event["Q_leading_principal_coefficient"] == "1/737280",
            "sextic Q jet square changed",
        )
    require(plus_event["rho_jet"] == "1/384", "positive sextic jet changed")
    require(minus_event["rho_jet"] == "-1/384", "negative sextic jet changed")
    require(plus_oracle == minus_oracle, "ordinary global residues distinguish pair")
    require(
        plus_oracle["sum_finite_P_residues"] == "0"
        and plus_oracle["sum_finite_Q_residues"] == "0",
        "ordinary residue oracle is nonzero",
    )
    require(
        plus_ledger["primitive_zero_count"]["multiplicity_real_zero_count"] == 0,
        "positive sextic acquired a real zero",
    )
    require(
        minus_ledger["primitive_zero_count"]["multiplicity_real_zero_count"] == 2,
        "negative sextic lost its two real zeros",
    )
    require(
        evaluate(minus, F(-1, 2)) == 0
        and evaluate(minus, F(1, 2)) == 0,
        "negative sextic exact roots changed",
    )
    return {
        "interval": "[-1,1]",
        "epsilon": str(epsilon),
        "same_endpoint_signs": True,
        "same_derivative_support_and_orders": True,
        "plus": plus_ledger,
        "minus": minus_ledger,
        "ordinary_global_residue_oracle": plus_oracle,
        "factor_in_y": {
            "minus": "(y-1/4)(y^2+y/4+1/16)",
            "plus": "(y+1/4)(y^2-y/4+1/16)",
            "quadratic_discriminant": "-3/16",
        },
        "ordinary_residue_data_insufficient": True,
        "leading_jet_orientation_distinguishes_pair": True,
    }


def canonical_fixtures() -> dict[str, object]:
    return {
        "simple_cubic_recovery": turning_ledger(
            "simple_cubic_recovery",
            [F(1), F(-3), F(0), F(1)],
            F(-2),
            F(2),
            [F(-1), F(1)],
            [F(-1), F(1)],
        ),
        "flat_good_quartic": turning_ledger(
            "flat_good_quartic",
            [F(-1), F(0), F(0), F(0), F(1)],
            F(-2),
            F(2),
            [F(0)],
            [F(0)],
        ),
        "flat_wrong_quartic": turning_ledger(
            "flat_wrong_quartic",
            [F(1), F(0), F(0), F(0), F(1)],
            F(-2),
            F(2),
            [F(0)],
            [F(0)],
        ),
        "common_and_two_good_turns": turning_ledger(
            "common_and_two_good_turns",
            [F(0), F(0), F(-2), F(0), F(1)],
            F(-5, 4),
            F(5, 4),
            [F(-1), F(0), F(1)],
            [F(-1), F(0), F(1)],
        ),
        "common_only_x4": turning_ledger(
            "common_only_x4",
            [F(0), F(0), F(0), F(0), F(1)],
            F(-1),
            F(1),
            [F(0)],
            [F(0)],
        ),
        "neutral_even_stationary": turning_ledger(
            "neutral_even_stationary",
            [F(2), F(0), F(0), F(1)],
            F(-1),
            F(1),
            [F(0)],
            [F(0)],
        ),
        "two_even_stationary_firewall": turning_ledger(
            "two_even_stationary_firewall",
            [F(-10), F(1, 16), F(0), F(-1, 6), F(0), F(1, 5)],
            F(-1),
            F(1),
            [F(-1, 2), F(1, 2)],
            [F(-1, 2), F(1, 2)],
        ),
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
        "schema": "riemann.t105104.jet-coherence-reverse-rolle.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "component_combinatorics": component_combinatorics(),
            "ordinary_residue_no_go_firewall": ordinary_residue_no_go_firewall(),
            "canonical_fixtures": canonical_fixtures(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "arbitrary_multiplicity_real_interval_identity_proved": True,
            "odd_turn_jet_sign_dictionary_proved": True,
            "jet_coherence_transfer_bound_proved": True,
            "common_critical_multiplicity_accounted": True,
            "ordinary_residue_only_extension_refuted": True,
            "jet_data_reconstructed_from_global_boundary_flux": False,
            "xi_effective_turning_proportion_proved": False,
            "xi_multiplicity_defect_controlled": False,
            "xi_jet_moments_estimated": False,
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
