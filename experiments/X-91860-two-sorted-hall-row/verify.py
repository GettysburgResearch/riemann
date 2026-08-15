#!/usr/bin/env python3
"""Exact finite/type regression for T-91860.

This checker authenticates finite algebra, type separation, row identity,
ownership, common-row identifiers, rational constants and hostile mutations.
It does not replay the analytic factor-67 Hall census, endpoint estimates,
prime-square theorem, Mellin transform, Landau theorem, or RH.
"""
from __future__ import annotations

import argparse
import copy
import json
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from typing import Any

VERDICT = "PASS_T91860_TWO_SORTED_HALL_ROW_SUCCESSOR"
MUTATIONS = (
    "promote_bonus_to_complete_packet",
    "bonus_to_child",
    "negative_bonus_row",
    "hall_overdraw",
    "duplicate_hall_edge_owner",
    "duplicate_source_owner",
    "require_injective_first_owner",
    "different_cell_restriction",
    "second_bulk_quantizer",
    "label_dependent_quantizer",
    "different_channel_thinning",
    "row_id_mismatch",
    "signed_error_in_source",
    "omit_small_columns",
    "terminal_reversed",
    "weak_thinning",
    "y4_prices_other_row",
    "benchmark_bridge",
    "reverse_endpoint",
    "export_child",
)


@dataclass(frozen=True)
class Q2:
    """a + b*sqrt(2), exact sign by rational comparison."""
    a: F
    b: F

    def __add__(self, other: "Q2") -> "Q2":
        return Q2(self.a + other.a, self.b + other.b)

    def __sub__(self, other: "Q2") -> "Q2":
        return Q2(self.a - other.a, self.b - other.b)

    def scale(self, c: F) -> "Q2":
        return Q2(c * self.a, c * self.b)

    def sign(self) -> int:
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        cmp = a * a - 2 * b * b
        if a > 0 and b < 0:
            return (cmp > 0) - (cmp < 0)
        return (cmp < 0) - (cmp > 0)


def vadd(a: tuple[F, ...], b: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(x + y for x, y in zip(a, b))


def vsub(a: tuple[F, ...], b: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(x - y for x, y in zip(a, b))


def vscale(c: F, a: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(c * x for x in a)


def vzero(n: int) -> tuple[F, ...]:
    return tuple(F(0) for _ in range(n))


def hall_fixture() -> dict[str, Any]:
    even = {1: F(9), 3: F(5)}
    odd = {2: F(4), 4: F(3)}
    flow = {(2, 1): F(4), (4, 1): F(3)}
    profiles = {
        1: (F(7), F(5), F(3)),
        2: (F(6), F(4), F(2)),
        3: (F(5), F(3), F(2)),
        4: (F(4), F(2), F(1)),
    }
    score_per_target = {1: F(3, 2), 2: F(2), 3: F(5, 2), 4: F(3)}
    return {
        "even": even,
        "odd": odd,
        "flow": flow,
        "profiles": profiles,
        "score_per_target": score_per_target,
    }


def validate_hall(f: dict[str, Any]) -> dict[str, Any]:
    even, odd, flow = f["even"], f["odd"], f["flow"]
    profiles, g = f["profiles"], f["score_per_target"]
    for o, m in odd.items():
        assert sum(v for (oo, _), v in flow.items() if oo == o) == m
    used = {e: sum(v for (_, ee), v in flow.items() if ee == e) for e in even}
    assert all(used[e] <= even[e] for e in even)
    assert all(e <= o for (o, e) in flow)
    residual = {e: even[e] - used[e] for e in even}
    assert all(v >= 0 for v in residual.values())

    dim = len(next(iter(profiles.values())))
    signed_row = vzero(dim)
    for e, m in even.items():
        signed_row = vadd(signed_row, vscale(m, profiles[e]))
    for o, m in odd.items():
        signed_row = vsub(signed_row, vscale(m, profiles[o]))
    residual_row = vzero(dim)
    for e, m in residual.items():
        residual_row = vadd(residual_row, vscale(m, profiles[e]))
    bonus = vzero(dim)
    for (o, e), m in flow.items():
        diff = vsub(profiles[e], profiles[o])
        assert all(x >= 0 for x in diff)
        bonus = vadd(bonus, vscale(m, diff))
    assert signed_row == vadd(residual_row, bonus)

    signed_score = sum(even[e] * g[e] for e in even) - sum(odd[o] * g[o] for o in odd)
    residual_score = sum(residual[e] * g[e] for e in residual)
    assert residual_score >= signed_score
    literal_bonus_score = sum(F(i + 1) * x for i, x in enumerate(bonus))
    assert literal_bonus_score >= 0
    return {
        "residual": residual,
        "bonus": bonus,
        "signed_row": signed_row,
        "residual_score": residual_score,
        "signed_score": signed_score,
        "literal_bonus_score": literal_bonus_score,
    }


def exact_x2_obstruction() -> dict[str, Any]:
    target_e = Q2(F(-3), F(4))
    score_e = Q2(F(-3), F(5))
    assert target_e.sign() > 0
    cross = score_e - target_e.scale(F(2))
    assert cross == Q2(F(3), F(-3))
    assert cross.sign() < 0
    return {
        "forced_edge": "2->1",
        "score_cross": "3-3*sqrt(2)<0",
        "complete_target_null_bonus_packet": False,
    }


def base_certificate() -> dict[str, Any]:
    return {
        "hall": hall_fixture(),
        "bonus_type": {
            "sort": "row",
            "target": None,
            "declared_score": None,
            "current_only": True,
            "rough_owner": None,
            "child": False,
        },
        "first_owner": {67: 67, 67 * 71: 67, 71: 71},
        "require_owner_injective": False,
        "causal": {
            "residual@67": {"current": F(15, 16), "child@67": F(1, 16)},
            "residual@71": {"current": F(10, 11), "child@71": F(1, 11)},
        },
        "exported_children": False,
        "retained_cells_source": tuple(range(12, 17)),
        "retained_cells_bonus": tuple(range(12, 17)),
        "realization": {
            "blocks": ("I_anc", "I_bonus", "Q_bulk"),
            "bulk_quantizers": 1,
            "label_dependent": False,
            "row_id": "X|cells12-16|Ianc+Ibonus+Qbulk|tau",
        },
        "channel_thinning": {"anchor": F(7, 9), "bonus": F(7, 9), "bulk": F(7, 9)},
        "comparison": {
            "row_id": "X|cells12-16|Ianc+Ibonus+Qbulk|tau",
            "signed_terms_are_source": False,
            "small_columns_covered": True,
            "terminal_removed": 5033,
            "terminal_overfill": 4452,
            "thinning_denominator": 130,
        },
        "capacity": {
            "row_id": "X|cells12-16|Ianc+Ibonus+Qbulk|tau",
            "unused": (F(7), F(5), F(4)),
            "signed_error": (F(2), F(-1), F(1)),
        },
        "y4": {
            "row_id": "X|cells12-16|Ianc+Ibonus+Qbulk|tau",
            "weights": (F(3), F(2), F(1)),
        },
        "native_ledger": {"thinning": 12012, "nonterminal": 4, "terminal": 48972, "omissions": 1},
        "forbidden_benchmark_bridge": False,
        "endpoint_orientation": "F_Lambda<=native_deficit",
    }


def validate_certificate(c: dict[str, Any]) -> dict[str, Any]:
    obstruction = exact_x2_obstruction()
    hall = validate_hall(c["hall"])

    bt = c["bonus_type"]
    assert bt["sort"] == "row"
    assert bt["target"] is None and bt["declared_score"] is None
    assert bt["current_only"] and bt["rough_owner"] is None and not bt["child"]
    assert all(x >= 0 for x in hall["bonus"])

    owners = c["first_owner"]
    assert not c["require_owner_injective"]
    for monomial, owner in owners.items():
        factors = [p for p in (67, 71, 73, 79) if monomial % p == 0]
        assert factors and owner == min(factors)
    assert len(set(owners.values())) < len(owners)

    total_child = F(0)
    total_mass = F(0)
    for weights in c["causal"].values():
        assert all(v >= 0 for v in weights.values())
        assert sum(weights.values()) == 1
        total_child += sum(v for k, v in weights.items() if k.startswith("child"))
        total_mass += 1
    assert total_child < F(1, 8) * total_mass
    assert not c["exported_children"]

    assert c["retained_cells_source"] == c["retained_cells_bonus"]
    cells = c["retained_cells_source"]
    assert cells == tuple(range(min(cells), max(cells) + 1))

    rz = c["realization"]
    assert rz["blocks"] == ("I_anc", "I_bonus", "Q_bulk")
    assert rz["bulk_quantizers"] == 1 and not rz["label_dependent"]
    thinning = c["channel_thinning"]
    assert len(set(thinning.values())) == 1
    tau = next(iter(thinning.values()))
    assert F(0) <= tau <= F(1)

    comp, cap, y4 = c["comparison"], c["capacity"], c["y4"]
    assert comp["row_id"] == cap["row_id"] == y4["row_id"] == rz["row_id"]
    assert not comp["signed_terms_are_source"]
    assert comp["small_columns_covered"]
    assert 2913**2 < 2 * (16 * 129) ** 2
    assert comp["thinning_denominator"] > 129
    terminal_margin = comp["terminal_removed"] - comp["terminal_overfill"]
    assert terminal_margin == 581 and terminal_margin > 0

    slack = vsub(cap["unused"], cap["signed_error"])
    assert all(x >= 0 for x in slack)
    cost_fixture = sum(a * b for a, b in zip(y4["weights"], slack))
    assert cost_fixture >= 0

    ledger = c["native_ledger"]
    assert ledger == {"thinning": 12012, "nonterminal": 4, "terminal": 48972, "omissions": 1}
    assert sum(ledger.values()) == 60989
    assert not c["forbidden_benchmark_bridge"]
    assert c["endpoint_orientation"] == "F_Lambda<=native_deficit"

    return {
        "bonus_row": [str(x) for x in hall["bonus"]],
        "bonus_target": None,
        "bonus_declared_score": None,
        "forced_x2_obstruction": obstruction,
        "many_to_one_first_owner_accepted": True,
        "one_block_realization": True,
        "one_row_identifier": rz["row_id"],
        "terminal_margin": terminal_margin,
        "native_total": sum(ledger.values()),
        "fixture_y4_cost": str(cost_fixture),
        "endpoint_orientation": c["endpoint_orientation"],
    }


def mutated(name: str) -> dict[str, Any]:
    c = copy.deepcopy(base_certificate())
    if name == "promote_bonus_to_complete_packet":
        c["bonus_type"]["target"] = F(0)
        c["bonus_type"]["declared_score"] = F(-1)
    elif name == "bonus_to_child":
        c["bonus_type"]["child"] = True
    elif name == "negative_bonus_row":
        c["hall"]["profiles"][1] = (F(0), F(0), F(0))
    elif name == "hall_overdraw":
        c["hall"]["flow"][(4, 1)] = F(8)
    elif name == "duplicate_hall_edge_owner":
        c["hall"]["flow"][(2, 3)] = c["hall"]["flow"][(2, 1)]
    elif name == "duplicate_source_owner":
        c["first_owner"][67 * 71] = 71
    elif name == "require_injective_first_owner":
        c["require_owner_injective"] = True
    elif name == "different_cell_restriction":
        c["retained_cells_bonus"] = tuple(range(13, 17))
    elif name == "second_bulk_quantizer":
        c["realization"]["bulk_quantizers"] = 2
    elif name == "label_dependent_quantizer":
        c["realization"]["label_dependent"] = True
    elif name == "different_channel_thinning":
        c["channel_thinning"]["bonus"] = F(8, 9)
    elif name == "row_id_mismatch":
        c["comparison"]["row_id"] = "other-row"
    elif name == "signed_error_in_source":
        c["comparison"]["signed_terms_are_source"] = True
    elif name == "omit_small_columns":
        c["comparison"]["small_columns_covered"] = False
    elif name == "terminal_reversed":
        c["comparison"]["terminal_removed"], c["comparison"]["terminal_overfill"] = 4452, 5033
    elif name == "weak_thinning":
        c["comparison"]["thinning_denominator"] = 129
    elif name == "y4_prices_other_row":
        c["y4"]["row_id"] = "other-row"
    elif name == "benchmark_bridge":
        c["forbidden_benchmark_bridge"] = True
    elif name == "reverse_endpoint":
        c["endpoint_orientation"] = "native_deficit<=F_Lambda"
    elif name == "export_child":
        c["exported_children"] = True
    else:
        raise KeyError(name)
    return c


def run_mutations() -> list[str]:
    rejected: list[str] = []
    for name in MUTATIONS:
        try:
            validate_certificate(mutated(name))
        except (AssertionError, ValueError):
            rejected.append(name)
        else:
            raise AssertionError(f"hostile mutation survived: {name}")
    return rejected


def required_paths(repo_root: Path) -> None:
    required = (
        "claims/refutations/R-91860-target-null-hall-bonus-is-row-only.md",
        "claims/lemmas/L-91860-two-sorted-hall-fibre.md",
        "claims/lemmas/L-91861-one-block-realization-of-two-sorted-fibre.md",
        "claims/lemmas/L-91862-same-row-all-column-complement.md",
        "claims/lemmas/L-91863-same-row-direct-y4-cost-below-60989.md",
        "claims/theorems/T-91860-two-sorted-hall-row-factor67-successor.md",
        "integration/2026-08-15/t91860-two-sorted-hall-row-lock.json",
    )
    missing = [p for p in required if not (repo_root / p).is_file()]
    assert not missing, f"missing required packet files: {missing}"


def payload(with_mutations: bool) -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[2]
    required_paths(repo_root)
    result = validate_certificate(base_certificate())
    rejected = run_mutations() if with_mutations else []
    result.update({
        "arithmetic_class": "EXACT_RATIONAL_PLUS_QUADRATIC_SIGN",
        "hostile_mutations_rejected": len(rejected),
        "mutations": rejected,
        "rh_established": False,
        "verdict": VERDICT,
    })
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()
    out = payload(args.mutations)
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
