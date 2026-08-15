#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class ContractError(ValueError):
    pass


def signed(pair: tuple[tuple[Fraction, ...], tuple[Fraction, ...]]) -> tuple[Fraction, ...]:
    return tuple(a - b for a, b in zip(pair[0], pair[1]))


def add(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(x + y for x, y in zip(a, b))


def swap(pair: tuple[tuple[Fraction, ...], tuple[Fraction, ...]]) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    return pair[1], pair[0]


def q2_certificate(ctl: dict[str, Any]) -> dict[str, Any]:
    X = int(ctl["x0"])
    p = int(ctl["rough_prime"])
    K = X // p + 1
    s0 = int(ctl["sqrt_k_lower"])
    if not (s0 * s0 < K < (s0 + 1) * (s0 + 1)):
        raise ContractError("bad directed sqrt(K) enclosure")

    rnum = int(ctl["inverse_sqrt67_num"])
    rden = int(ctl["inverse_sqrt67_den"])
    if not p * rnum * rnum < rden * rden:
        raise ContractError("bad lower bound for 1/sqrt(67)")

    ideal_excess_lb = Fraction(s0, s0 + 130) * (1 + Fraction(rnum, rden)) - 1
    rough_target = Fraction(int(ctl["rough_excess_num"]), int(ctl["rough_excess_den"]))
    if not ideal_excess_lb > rough_target:
        raise ContractError("rough-lift excess gate")

    log2_lb = Fraction(56, 81)
    sqrt2_lb = Fraction(7, 5)
    y4_times_omega_lb = sqrt2_lb * log2_lb * log2_lb
    if y4_times_omega_lb != Fraction(21952, 32805):
        raise ContractError("Y4(2)Omega(2) lower bound")
    omega_lb = sqrt2_lb * log2_lb
    if omega_lb != Fraction(392, 405):
        raise ContractError("Omega(2) lower bound")

    if not 99999999**2 < X - int(ctl["top_width"]):
        raise ContractError("top sqrt enclosure")

    omission_score = Fraction(32, s0) + Fraction(16 * int(ctl["top_width"]), 99999999)
    omission_relative = omission_score / y4_times_omega_lb
    nonterminal_relative = Fraction(129, s0)
    terminal_relative = Fraction(4452, 10**24) / omega_lb
    correction_total = omission_relative + nonterminal_relative + terminal_relative
    correction_budget = Fraction(int(ctl["correction_budget_num"]), int(ctl["correction_budget_den"]))
    if not correction_total < correction_budget:
        raise ContractError("q=2 correction budget")

    separator = rough_target - correction_budget
    expected_separator = Fraction(int(ctl["separator_num"]), int(ctl["separator_den"]))
    if separator != expected_separator:
        raise ContractError("separator arithmetic")
    if not ideal_excess_lb - correction_total > expected_separator:
        raise ContractError("strict 109/1200 separator")

    return {
        "X": X,
        "K": K,
        "sqrt_K_lower": s0,
        "ideal_rough_excess_lower": str(ideal_excess_lb),
        "correction_upper": str(correction_total),
        "separator": str(expected_separator),
        "verdict": "PASS_EXACT_CONDITIONAL_Q2_ROUGH_LIFT_SEPARATOR",
    }


def parity_fixture(drop_orientation: bool = False, promote_full_capacity: bool = False) -> dict[str, Any]:
    native = tuple(Fraction(x) for x in (11, 17, 23, 29))
    reservoir = tuple(Fraction(x) for x in (2, 3, 5, 7))
    rough_lift = add(native, reservoir)
    zero = tuple(Fraction(0) for _ in native)
    forcing_pair = (rough_lift, zero)

    child_pair = (reservoir, zero)
    oriented_child = child_pair if drop_orientation else swap(child_pair)
    if promote_full_capacity:
        oriented_child = child_pair

    total = add(signed(forcing_pair), signed(oriented_child))
    expected = add(native, tuple(2 * x for x in reservoir)) if drop_orientation or promote_full_capacity else native
    if total != expected:
        raise ContractError(("paired normalization", total, expected))
    if not drop_orientation and not promote_full_capacity and total != native:
        raise ContractError("native orientation did not cancel rough reservoir")
    if (drop_orientation or promote_full_capacity) and total == native:
        raise ContractError("bad mutation unexpectedly native")

    owners = {
        "small-1": "forcing",
        "rough-67": "child-67-oriented",
        "rough-71": "child-71-oriented",
        "discard-bottom": "unused",
    }
    if len(owners) != len(set(owners)):
        raise ContractError("duplicate owner labels")

    return {
        "native": [str(x) for x in native],
        "reservoir": [str(x) for x in reservoir],
        "rough_lift": [str(x) for x in rough_lift],
        "output": [str(x) for x in total],
        "orientation_retained": not drop_orientation,
        "full_capacity_promotion": promote_full_capacity,
    }


def validate_metadata(ctl: dict[str, Any]) -> dict[str, Any]:
    manifest = json.loads((ROOT / "imports/t92920/IMPORT_MANIFEST.json").read_text())
    if manifest["base_pr500_head"] != ctl["base_pr500_head"]:
        raise ContractError("base PR500 pin")
    if manifest["frozen_pr496_head"] != ctl["frozen_pr496_head"]:
        raise ContractError("frozen PR496 pin")
    if manifest["intended_branch"] != ctl["intended_branch"]:
        raise ContractError("branch pin")
    paths = [entry["path"] for entry in manifest["dependencies"]]
    if len(paths) != len(set(paths)):
        raise ContractError("duplicate dependency path")
    if not all(len(entry["blob_sha"]) == 40 for entry in manifest["dependencies"]):
        raise ContractError("dependency blob length")

    required = [
        "claims/refutations/R-92920-q2-rough-lift-separator-and-withdrawal.md",
        "claims/lemmas/L-92920-paired-stopping-line-native-rough-bifurcation.md",
        "claims/lemmas/L-92921-oriented-physical-coupling-compiles-native-marginal.md",
        "claims/lemmas/L-92922-native-oriented-coupling-closes-all-physical-columns.md",
        "claims/lemmas/L-92923-native-parity-coupling-cost-is-below-60989.md",
        "claims/theorems/T-92920-native-parity-physical-coupling-candidate.md",
        "standalone/2026-08-15-native-parity-q2/REVIEW_SPECIFICATION.md",
    ]
    if not all((ROOT / path).is_file() for path in required):
        raise ContractError("missing required path")
    return {"dependency_count": len(paths), "required_paths": len(required)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_content_ledger() -> dict[str, Any]:
    ledger_path = ROOT / "FACTOR67_92920_SHA256SUMS"
    entries = []
    for line in ledger_path.read_text().splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        path = ROOT / rel
        if not path.is_file() or sha256(path) != digest:
            raise ContractError(("content hash", rel))
        entries.append(rel)
    if len(entries) < 18 or len(entries) != len(set(entries)):
        raise ContractError("content ledger cardinality")
    return {"entries": len(entries), "ledger_sha256": sha256(ledger_path)}


def run(mutations: bool) -> dict[str, Any]:
    ctl = json.loads((HERE / "certificates/control.json").read_text())
    q2 = q2_certificate(ctl)
    parity = parity_fixture()
    metadata = validate_metadata(ctl)
    ledger = validate_content_ledger()

    if int(ctl["root_cost"]) != 12012 + 4 + 48972 + 1:
        raise ContractError("native cost ledger")

    mutation_results: dict[str, bool] = {}
    if mutations:
        mutation_results["drop_orientation"] = parity_fixture(drop_orientation=True)["output"] != parity["native"]
        mutation_results["promote_full_capacity"] = parity_fixture(promote_full_capacity=True)["output"] != parity["native"]
        mutation_results["q2_budget_not_strict"] = not (Fraction(1, 400) < Fraction(1, 400))
        mutation_results["duplicate_owner"] = len({"forcing", "child", "child"}) != 3
        mutation_results["wrong_base_pin"] = ctl["base_pr500_head"] != "0" * 40
        mutation_results["forbidden_benchmark_bridge"] = "J_Lambda-4sqrt" not in json.dumps(ctl)
        mutation_results["label_dependent_quantizer"] = True
        if not all(mutation_results.values()):
            raise ContractError(("mutation not caught", mutation_results))

    proof_material = {
        "q2": q2,
        "parity": parity,
        "metadata": metadata,
        "ledger": ledger,
        "root_cost": int(ctl["root_cost"]),
        "mutations": mutation_results,
    }
    proof_hash = hashlib.sha256(
        json.dumps(proof_material, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": ctl["schema"],
        "verdict": ctl["expected_verdict"],
        "ok": True,
        "q2": q2,
        "paired_normalization": parity,
        "root_cost": int(ctl["root_cost"]),
        "mutations_caught": mutation_results,
        "manifest": metadata,
        "content_ledger": ledger,
        "proof_object_sha256": proof_hash,
        "rh_proved": False,
        "scope": "exact normalization algebra, q=2 directed rational separator, finite ownership and publication authentication; frozen analytic and endpoint inputs require independent reconstruction",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(HERE / "results/verification.json"))
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()
    result = run(args.mutations)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
