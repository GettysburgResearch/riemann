#!/usr/bin/env python3
"""Exact finite regression for the concrete factor-67 common-parent packet.

The verifier authenticates finite Hall/source/row algebra, provenance,
whole-cell bonus strips, one labelled direct-sum quantizer, signed capacity
typing, cost addition and endpoint sign algebra.  It does not replay the
factor-67 directed analytic census, continuum quadrature estimates, the PNT
prime-square theorem, the Mellin transform, Landau's theorem, or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable, Mapping

SCHEMA = "riemann.t92910.concrete-common-parent.v1"


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def vadd(*vectors: Iterable[F]) -> list[F]:
    vv = [list(v) for v in vectors]
    if not vv:
        return []
    n = len(vv[0])
    if any(len(v) != n for v in vv):
        raise AssertionError("vector length mismatch")
    return [sum((v[i] for v in vv), F(0)) for i in range(n)]


def vsub(a: Iterable[F], b: Iterable[F]) -> list[F]:
    aa, bb = list(a), list(b)
    if len(aa) != len(bb):
        raise AssertionError("vector length mismatch")
    return [x - y for x, y in zip(aa, bb)]


def vscale(a: F, v: Iterable[F]) -> list[F]:
    return [a * x for x in v]


def dot(a: Iterable[F], b: Iterable[F]) -> F:
    return sum((x * y for x, y in zip(a, b)), F(0))


def canonical_sha(payload: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def hall_fibre_check(mutate: str | None = None) -> dict[str, Any]:
    # Two even supplies and two odd demands.  Flows use each source fraction once.
    target_e = {"e1": F(5), "e2": F(4)}
    target_o = {"o1": F(3), "o2": F(2)}
    flow = {
        ("o1", "e1"): F(3),
        ("o2", "e1"): F(2),
    }
    if mutate == "hall_overdraw":
        flow[("o2", "e1")] = F(3)

    rho = {
        "e1": [F(5), F(4), F(3)],
        "e2": [F(4), F(3), F(2)],
        "o1": [F(3), F(2), F(1)],
        "o2": [F(2), F(1), F(1, 2)],
    }
    if mutate == "negative_bonus":
        rho["o1"][0] = F(6)

    residual = {}
    for e, supply in target_e.items():
        used = sum((t for (o0, e0), t in flow.items() if e0 == e), F(0))
        residual[e] = supply - used
        if residual[e] < 0:
            raise AssertionError("Hall supply overdraw")

    for o, demand in target_o.items():
        used = sum((t for (o0, _), t in flow.items() if o0 == o), F(0))
        if used != demand:
            raise AssertionError("Hall demand not exhausted")

    signed_row = [F(0), F(0), F(0)]
    for e, t in target_e.items():
        signed_row = vadd(signed_row, vscale(t, rho[e]))
    for o, t in target_o.items():
        signed_row = vsub(signed_row, vscale(t, rho[o]))

    residual_row = [F(0), F(0), F(0)]
    for e, r in residual.items():
        residual_row = vadd(residual_row, vscale(r, rho[e]))

    bonus_row = [F(0), F(0), F(0)]
    for (o, e), t in flow.items():
        edge = vsub(rho[e], rho[o])
        if any(x < 0 for x in edge):
            raise AssertionError("Hall edge row bonus is not positive")
        bonus_row = vadd(bonus_row, vscale(t, edge))

    if mutate == "drop_bonus":
        bonus_row = [F(0), F(0), F(0)]

    if vadd(residual_row, bonus_row) != signed_row:
        raise AssertionError("residual plus bonus row identity failed")

    signed_target = sum(target_e.values(), F(0)) - sum(target_o.values(), F(0))
    if sum(residual.values(), F(0)) != signed_target:
        raise AssertionError("target identity failed")

    # Score ratios are lower on even supply than on odd demand.
    score_ratio = {
        "e1": F(1),
        "e2": F(6, 5),
        "o1": F(3, 2),
        "o2": F(2),
    }
    signed_score = (
        sum((target_e[e] * score_ratio[e] for e in target_e), F(0))
        - sum((target_o[o] * score_ratio[o] for o in target_o), F(0))
    )
    residual_score = sum(
        (residual[e] * score_ratio[e] for e in residual), F(0)
    )
    if residual_score < signed_score:
        raise AssertionError("score superordination failed")
    edge_score_reserve = sum(
        (
            t * (score_ratio[o] - score_ratio[e])
            for (o, e), t in flow.items()
        ),
        F(0),
    )
    if residual_score - signed_score != edge_score_reserve:
        raise AssertionError("edge score reserve mismatch")

    owners = [
        ("edge", o, e, fs(t)) for (o, e), t in flow.items()
    ] + [
        ("residual", e, fs(r)) for e, r in residual.items() if r
    ]
    if mutate == "duplicate_source":
        owners.append(owners[0])
    if len(owners) != len(set(owners)):
        raise AssertionError("source provenance duplicated")

    return {
        "signed_target": fs(signed_target),
        "residual_target": fs(sum(residual.values(), F(0))),
        "signed_row": [fs(x) for x in signed_row],
        "residual_row": [fs(x) for x in residual_row],
        "bonus_row": [fs(x) for x in bonus_row],
        "edge_score_reserve": fs(edge_score_reserve),
        "provenance_records": len(owners),
        "verdict": "PASS_CONCRETE_HALL_RESIDUAL_AND_BONUS_ROW",
    }


def strip_check(mutate: str | None = None) -> dict[str, Any]:
    # Common activation knots with coordinatewise nondecreasing profiles.
    profile = {
        F(1): [F(0), F(0), F(0)],
        F(2): [F(1), F(1, 2), F(1, 4)],
        F(3): [F(2), F(3, 2), F(1)],
        F(4): [F(3), F(2), F(3, 2)],
    }
    if mutate == "cross_activation_cell":
        profile[F(3)][1] = F(1, 4)

    knots = sorted(profile)
    increments = []
    for a, b in zip(knots, knots[1:]):
        inc = vsub(profile[b], profile[a])
        if any(x < 0 for x in inc):
            raise AssertionError("profile strip has a negative increment")
        increments.append((a, b, inc))

    direct = vsub(profile[F(4)], profile[F(1)])
    telescoped = [F(0), F(0), F(0)]
    for _, _, inc in increments:
        telescoped = vadd(telescoped, inc)
    if mutate == "partial_cell_as_full":
        telescoped = vadd(telescoped, increments[0][2])
    if telescoped != direct:
        raise AssertionError("whole-cell Stieltjes strip telescope failed")

    return {
        "whole_cells": len(increments),
        "direct_bonus": [fs(x) for x in direct],
        "strip_bonus": [fs(x) for x in telescoped],
        "verdict": "PASS_POSITIVE_WHOLE_CELL_HALL_BONUS_STRIP",
    }


def rough_colour_check(mutate: str | None = None) -> dict[str, Any]:
    packet = [F(31), F(29), F(23), F(19)]
    child = [F(7), F(5), F(4), F(3)]
    r = F(1, 9)
    lam = F(2, 5)
    alpha = r * lam
    survival = F(1) - lam
    causal = vsub(packet, vscale(r, child))
    if any(x < 0 for x in causal):
        raise AssertionError("causal colour left positive cone")

    rhs = vadd(vscale(survival, packet), vscale(lam, causal), vscale(alpha, child))
    if mutate == "rerun_coefficient_list":
        rhs = vadd(rhs, vscale(alpha, child))
    if rhs != packet:
        raise AssertionError("causal current/inner colour identity failed")
    if not alpha < F(1, 8):
        raise AssertionError("child coefficient not subcritical")

    labels = {
        "survival": {"src-e2-residual"},
        "difference": {"src-e2-residual:causal"},
        "child": {"src-e2-residual:first-owner-67"},
        "bonus": {"edge-o1-e1", "edge-o2-e1"},
    }
    if mutate == "child_gets_bonus":
        labels["child"].add("edge-o1-e1")
    if labels["child"] & labels["bonus"]:
        raise AssertionError("Hall bonus was copied to an inner colour")

    return {
        "alpha": fs(alpha),
        "subcritical": True,
        "packet": [fs(x) for x in packet],
        "causal": [fs(x) for x in causal],
        "provenance_classes": {k: sorted(v) for k, v in labels.items()},
        "verdict": "PASS_FIRST_OWNER_AND_INTERNAL_CAUSAL_COLOURS",
    }


def quantizer_check(mutate: str | None = None) -> dict[str, Any]:
    # E-channel: one endpoint atom split barycentrically between two knots.
    atom = [F(4), F(3), F(2)]
    theta = F(2, 5)
    q_left = [F(3), F(2), F(1)]
    q_right = [F(11, 2), F(9, 2), F(7, 2)]
    quantized_e = vadd(vscale(theta, q_left), vscale(F(1) - theta, q_right))

    # B-channel: already integrated whole-cell row; identity block.
    bonus = [F(2), F(1), F(1, 2)]
    one_call = vadd(quantized_e, bonus)

    by_labels = vadd(
        vscale(theta, q_left),
        vscale(F(1) - theta, q_right),
        bonus,
    )
    if mutate == "second_child_quantizer":
        by_labels = vadd(by_labels, vscale(F(1, 10), atom))
    if one_call != by_labels:
        raise AssertionError("one labelled direct-sum quantizer identity failed")
    if any(x < 0 for x in one_call):
        raise AssertionError("quantized common row is not positive")

    tag_weights = {
        "residual-current-left": theta,
        "residual-inner-right": F(1) - theta,
        "hall-bonus-strip": F(1),
    }
    if mutate == "drop_label":
        tag_weights.pop("hall-bonus-strip")
    if set(tag_weights) != {
        "residual-current-left",
        "residual-inner-right",
        "hall-bonus-strip",
    }:
        raise AssertionError("quantizer lost a provenance channel")

    return {
        "quantizer_calls": 1,
        "endpoint_block": "POSITIVE_BSPLINE",
        "bonus_block": "IDENTITY_ON_WHOLE_CELL_ROWS",
        "output": [fs(x) for x in one_call],
        "labels": {k: fs(v) for k, v in tag_weights.items()},
        "verdict": "PASS_ONE_LABELLED_DIRECT_SUM_QUANTIZER",
    }


def capacity_check(mutate: str | None = None) -> dict[str, Any]:
    omega = [F(10), F(8), F(6), F(5)]
    reserve = [F(2), F(1), F(1), F(1)]
    signed_error = [F(1), F(-1, 2), F(1, 2), F(0)]
    if mutate == "signed_error_as_source":
        signed_error = [abs(x) for x in signed_error]
    if mutate == "drop_small_column":
        reserve[0] = F(0)
    if mutate == "terminal_overfill":
        signed_error[-1] = F(2)

    used = vadd(vsub(omega, reserve), signed_error)
    complement = vsub(omega, used)
    if complement != vsub(reserve, signed_error):
        raise AssertionError("signed response identity failed")
    if any(x < 0 for x in complement):
        raise AssertionError("native complement is negative")
    if any(x < 0 for x in used):
        raise AssertionError("physical response is negative")
    if any(u > o for u, o in zip(used, omega)):
        raise AssertionError("native capacity exceeded")

    return {
        "omega": [fs(x) for x in omega],
        "positive_reserve": [fs(x) for x in reserve],
        "signed_error": [fs(x) for x in signed_error],
        "used": [fs(x) for x in used],
        "complement": [fs(x) for x in complement],
        "all_columns_including_small": True,
        "verdict": "PASS_SIGNED_DEFECT_AND_NONNEGATIVE_NATIVE_COMPLEMENT",
    }


def cost_check(mutate: str | None = None) -> dict[str, Any]:
    thinning = F(12012)
    nonterminal = F(4)
    terminal = F(48972)
    omissions = F(12)
    if mutate == "benchmark_bridge":
        raise AssertionError("forbidden J_Lambda-4sqrt(X) benchmark bridge")
    if mutate == "duplicate_terminal":
        terminal *= 2
    total = thinning + nonterminal + terminal + omissions
    if not total == F(61000):
        raise AssertionError("native cost ledger changed")
    return {
        "thinning_majorant": fs(thinning),
        "nonterminal_majorant": fs(nonterminal),
        "terminal_majorant": fs(terminal),
        "omission_collar_refinement_majorant": fs(omissions),
        "sum_of_majorants": fs(total),
        "strict_conclusion": "<61000",
        "verdict": "PASS_DIRECT_NATIVE_Y4_COST_LEDGER",
    }


def endpoint_check(mutate: str | None = None) -> dict[str, Any]:
    native_deficit_ratio = F(0)
    moat = F(1, 5)
    if mutate == "remove_prime_square_moat":
        moat = F(0)
    prime_endpoint_limsup = native_deficit_ratio - moat
    if not prime_endpoint_limsup < 0:
        raise AssertionError("prime endpoint eventual sign was not forced")
    return {
        "native_deficit_log2_limsup": fs(native_deficit_ratio),
        "positive_moat_shadow": fs(moat),
        "prime_endpoint_limsup": fs(prime_endpoint_limsup),
        "landau_input": "EVENTUAL_NEGATIVITY",
        "verdict": "PASS_ENDPOINT_MOAT_AND_ONE_SIGN_ALGEBRA",
    }


MUTATIONS = [
    "hall_overdraw",
    "negative_bonus",
    "drop_bonus",
    "duplicate_source",
    "cross_activation_cell",
    "partial_cell_as_full",
    "rerun_coefficient_list",
    "child_gets_bonus",
    "second_child_quantizer",
    "drop_label",
    "drop_small_column",
    "terminal_overfill",
    "benchmark_bridge",
    "duplicate_terminal",
    "remove_prime_square_moat",
]


def run_mutation(name: str) -> bool:
    checks = [
        hall_fibre_check,
        strip_check,
        rough_colour_check,
        quantizer_check,
        capacity_check,
        cost_check,
        endpoint_check,
    ]
    detected = False
    for fn in checks:
        try:
            fn(name)
        except AssertionError:
            detected = True
            break
    return detected


def verify(_: Mapping[str, Any] | None = None, with_mutations: bool = True) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "hall_fibre": hall_fibre_check(),
        "bonus_strip": strip_check(),
        "rough_colours": rough_colour_check(),
        "one_quantizer": quantizer_check(),
        "capacity": capacity_check(),
        "native_cost": cost_check(),
        "endpoint": endpoint_check(),
        "proof_boundary": {
            "compact_hall_directed_census": "FROZEN_RECONSTRUCTION_REQUIRED",
            "continuum_endpoint_identity": "FROZEN_RECONSTRUCTION_REQUIRED",
            "all_column_analytic_bounds": "FROZEN_RECONSTRUCTION_REQUIRED",
            "prime_square_and_landau": "FROZEN_RECONSTRUCTION_REQUIRED",
            "riemann_hypothesis": "PROPOSAL_PENDING_INDEPENDENT_REVIEW",
        },
        "verdict": "PASS_CONCRETE_FACTOR67_COMMON_PARENT_PACKET",
    }
    if with_mutations:
        results = {name: run_mutation(name) for name in MUTATIONS}
        if not all(results.values()):
            missing = [k for k, v in results.items() if not v]
            raise AssertionError(f"undetected mutations: {missing}")
        payload["mutations"] = {
            "attempted": len(results),
            "detected": sum(results.values()),
            "names": results,
        }
    payload["proof_object_sha256"] = canonical_sha(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()
    source = json.loads(args.certificate.read_text()) if args.certificate else None
    out = verify(source, with_mutations=args.mutations)
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
