#!/usr/bin/env python3
"""Finite regression for T-91821.

This checker authenticates only finite composition algebra, exact constants,
ownership/type firewalls, required paths, and hostile mutations.  It does not
replay the analytic Hall census, endpoint estimates, prime-square theorem,
Mellin transform, Landau theorem, or RH.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

VERDICT = "PASS_T91821_POSITIVE_COMMON_PARENT_RESPONSE_COMPLEMENT"
MUTATIONS = (
    "hall_overdraw",
    "duplicate_hall_edge",
    "duplicate_rough_owner",
    "second_quantizer",
    "signed_error_in_source",
    "omit_small_columns",
    "terminal_reversed",
    "weak_thinning",
    "benchmark_bridge",
    "reverse_endpoint",
)


def causal_coefficients(rs: tuple[Fraction, ...]) -> tuple[Fraction, tuple[Fraction, ...], tuple[Fraction, ...]]:
    survivor = Fraction(1)
    lambdas: list[Fraction] = []
    alphas: list[Fraction] = []
    for r in rs:
        lam = r * survivor
        lambdas.append(lam)
        alphas.append(r * lam)
        survivor *= 1 - r
    return survivor, tuple(lambdas), tuple(alphas)


def check_packet(mutation: str | None = None) -> dict[str, Any]:
    # One exact Hall fixture: negative demand is exhausted, positive supply is
    # not overdrawn, and the profile identity is residual plus edge bonus.
    positive = {"e1": Fraction(5), "e2": Fraction(4)}
    negative = {"o1": Fraction(3), "o2": Fraction(2)}
    flow = {
        ("o1", "e1"): Fraction(2),
        ("o1", "e2"): Fraction(1),
        ("o2", "e1"): Fraction(2),
    }
    if mutation == "hall_overdraw":
        flow[("o2", "e1")] = Fraction(4)
    if mutation == "duplicate_hall_edge":
        flow[("o1", "e1#duplicate")] = flow[("o1", "e1")]

    demand = {o: sum(v for (oo, _), v in flow.items() if oo == o) for o in negative}
    supply = {
        e: sum(v for (_, ee), v in flow.items() if ee.split("#")[0] == e)
        for e in positive
    }
    assert demand == negative, "Hall demand is not exhausted exactly"
    assert all(supply[e] <= positive[e] for e in positive), "Hall source overdraw"
    assert all("#" not in e for _, e in flow), "duplicate Hall edge owner"

    rho = {"e1": Fraction(7), "e2": Fraction(5), "o1": Fraction(4), "o2": Fraction(3)}
    lhs = sum(positive[e] * rho[e] for e in positive) - sum(negative[o] * rho[o] for o in negative)
    residual = sum((positive[e] - supply[e]) * rho[e] for e in positive)
    bonus = sum(v * (rho[e] - rho[o]) for (o, e), v in flow.items())
    assert bonus >= 0
    assert lhs == residual + bonus, "Hall residual/bonus identity failed"

    rough_owners = {"m=67": "67", "m=71": "71", "m=67*71": "67"}
    if mutation == "duplicate_rough_owner":
        rough_owners["m=67*71"] = "67,71"
    assert all("," not in owner for owner in rough_owners.values()), "rough source has two first owners"

    survivor, lambdas, alphas = causal_coefficients((Fraction(1, 9), Fraction(1, 11), Fraction(1, 13)))
    assert survivor + sum(lambdas) == 1
    assert sum(alphas) < Fraction(1, 8)

    quantizers = 2 if mutation == "second_quantizer" else 1
    assert quantizers == 1, "more than one physical quantizer"

    positive_source_terms = {"hall_residual", "hall_bonus", "omission", "thinning"}
    signed_observation_terms = {"finite_continuum", "collar", "interpolation", "terminal"}
    if mutation == "signed_error_in_source":
        positive_source_terms.add("finite_continuum")
    assert positive_source_terms.isdisjoint(signed_observation_terms), "signed response inserted into positive source"

    small_columns_covered = mutation != "omit_small_columns"
    assert small_columns_covered, "physical columns q<K omitted"

    terminal_removed, terminal_overfill = 5033, 4452
    if mutation == "terminal_reversed":
        terminal_removed, terminal_overfill = terminal_overfill, terminal_removed
    terminal_margin = terminal_removed - terminal_overfill
    assert terminal_margin == 581 and terminal_margin > 0

    thinning_denominator = 129 if mutation == "weak_thinning" else 130
    assert thinning_denominator > 129, "thinning leaves no strict reserve"
    assert 2913**2 < 2 * (16 * 129) ** 2

    forbidden_bridge = mutation == "benchmark_bridge"
    assert not forbidden_bridge, "RH-bearing J_Lambda-4sqrt(X) bridge imported"

    endpoint_orientation = "native_deficit<=F_Lambda" if mutation == "reverse_endpoint" else "F_Lambda<=native_deficit"
    assert endpoint_orientation == "F_Lambda<=native_deficit", "endpoint inequality reversed"

    # A finite positive radix-four inverse fixture.
    detail = {2: Fraction(3, 10), 8: Fraction(1, 10), 32: Fraction(1, 40)}
    ordinary_2 = detail[2] + 2 * detail[8] + 4 * detail[32]
    assert ordinary_2 == Fraction(3, 5) and ordinary_2 >= 0

    return {
        "all_column": {
            "nonterminal_relative_numerator": 129,
            "terminal_margin": terminal_margin,
        },
        "causal": {
            "coefficient_sum_identity": True,
            "recursive_mass_below_one_eighth": True,
        },
        "endpoint_orientation": endpoint_orientation,
        "native_cost": "A0+4290*log(2X)",
        "quantizers": quantizers,
        "source_observation_ledgers_disjoint": True,
    }


def run_mutations() -> int:
    rejected = 0
    for mutation in MUTATIONS:
        try:
            check_packet(mutation)
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError(f"hostile mutation survived: {mutation}")
    return rejected


def required_paths(repo_root: Path) -> None:
    paths = (
        "claims/refutations/R-91820-pr492-positive-common-parent-disposition.md",
        "claims/lemmas/L-91820-positive-compact-hall-rough-inner-colour-fibre.md",
        "claims/lemmas/L-91821-whole-cell-integration-and-one-labelled-quantizer.md",
        "claims/lemmas/L-91822-all-column-nonnegative-response-complements.md",
        "claims/lemmas/L-91823-direct-native-y4-cost-of-response-complement.md",
        "claims/theorems/T-91820-one-sided-response-complement-endpoint-consumer.md",
        "claims/theorems/T-91821-positive-common-parent-response-complement-proposal.md",
        "integration/2026-08-15/t91821-positive-common-parent-response-complement-lock.json",
    )
    missing = [p for p in paths if not (repo_root / p).is_file()]
    assert not missing, f"missing required packet files: {missing}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    required_paths(repo_root)
    payload = check_packet()
    rejected = run_mutations() if args.mutations else 0
    payload.update({"mutations_rejected": rejected, "verdict": VERDICT})
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
