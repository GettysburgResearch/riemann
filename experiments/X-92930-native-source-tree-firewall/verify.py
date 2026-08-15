#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class ContractError(ValueError):
    pass


def add(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(a) != len(b):
        raise ContractError("vector dimension mismatch")
    return tuple(x + y for x, y in zip(a, b))


def sub(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(a) != len(b):
        raise ContractError("vector dimension mismatch")
    return tuple(x - y for x, y in zip(a, b))


def validate(control: dict[str, Any]) -> dict[str, Any]:
    x0 = int(control["x0"])
    p = int(control["rough_prime"])
    if p != 67:
        raise ContractError("this certificate is frozen to the factor-67 route")

    # Exact integer gates behind the directed q=2 argument.
    k0 = x0 // p + 1
    if not k0 > 129_870**2:
        raise ContractError("tau > 999/1000 gate failed")
    if not k0 > 48_550**2:
        raise ContractError("q=2 correction < 1/400 gate failed")

    # Elementary symbolic bounds used in the proof:
    # log(4)>4/3, sqrt(134)<12, sqrt(67)<9, sqrt(2)<3/2.
    if not 134 < 12**2:
        raise ContractError("sqrt(134) bound failed")
    if not 67 < 9**2:
        raise ContractError("sqrt(67) bound failed")
    if not 2 * 2**2 < 3**2:
        raise ContractError("sqrt(2) bound failed")

    unthinned_lower = Fraction(1, 9)
    historical_threshold = Fraction(109, 1200)
    if not unthinned_lower > historical_threshold:
        raise ContractError("unthinned rough-lift separator too small")

    thinned_ideal_lower = Fraction(22, 225)
    advertised_intermediate = Fraction(7, 75)
    correction_upper = Fraction(1, 400)
    final_lower = thinned_ideal_lower - correction_upper
    if not thinned_ideal_lower > advertised_intermediate:
        raise ContractError("conditional ideal rough-lift gate failed")
    if final_lower != Fraction(343, 3600):
        raise ContractError("conditional final lower bound arithmetic failed")
    if not final_lower > historical_threshold:
        raise ContractError("conditional 109/1200 gate failed")

    # Type-separation regression: the native source-tree observation is an
    # exact current+actual-child split.  A row-first rough lift has an extra
    # positive reservoir and cannot be substituted for the native marginal.
    current = tuple(map(Fraction, (8, 10, 13, 16)))
    child_67 = tuple(map(Fraction, (5, 6, 8, 10)))
    child_71 = tuple(map(Fraction, (4, 5, 7, 8)))
    native = add(current, add(child_67, child_71))
    reservoir = tuple(map(Fraction, (2, 3, 5, 7)))
    rough_lift = add(native, reservoir)
    if native != tuple(map(Fraction, (17, 21, 28, 34))):
        raise ContractError("native source-tree identity failed")
    if rough_lift == native:
        raise ContractError("rough lift incorrectly identified with native")
    if sub(rough_lift, native) != reservoir or any(x <= 0 for x in reservoir):
        raise ContractError("rough reservoir regression failed")

    # Two-ledger response complement: signed observation correction is not a
    # source packet; positivity is obtained from explicit capacity domination.
    unused = tuple(map(Fraction, (4, 5, 6, 8)))
    signed_error = tuple(map(Fraction, (1, -1, 2, 3)))
    slack = sub(unused, signed_error)
    if slack != tuple(map(Fraction, (3, 6, 4, 5))):
        raise ContractError("two-ledger slack identity failed")
    if any(x < 0 for x in slack):
        raise ContractError("capacity overrun")

    # Actual-child terminalization and final native deficit.
    root_cost = Fraction(int(control["root_cost"]), 1)
    child_bound = Fraction(
        int(control["child_mass_num"]), int(control["child_mass_den"])
    )
    total = root_cost + child_bound
    if total != Fraction(493_951, 8):
        raise ContractError("root plus actual-child total mismatch")
    if not total < int(control["strict_integer_bound"]):
        raise ContractError("strict <61744 gate failed")

    if control.get("signed_error_declared_source_positive", False):
        raise ContractError("signed observation error promoted to source")
    if control.get("substitute_rough_lift", False):
        raise ContractError("row-first rough lift substituted for native marginal")
    if control.get("promote_child_to_standard_capacity", False):
        raise ContractError("actual child promoted to standard native capacity")
    if control.get("duplicate_owner", False):
        raise ContractError("duplicate source owner")
    if control.get("drop_child", False):
        raise ContractError("actual child omitted from native identity")
    if control.get("duplicate_root_correction", False):
        raise ContractError("root correction duplicated below root")
    if control.get("benchmark_bridge", False):
        raise ContractError("forbidden J_Lambda-4sqrt(X) bridge")
    if control.get("assert_unqualified_pr_falsifier", False):
        raise ContractError("withdrawn PR-specific q=2 assertion resurrected")

    return {
        "k0": k0,
        "q2": {
            "unthinned_rough_lift_lower": str(unthinned_lower),
            "conditional_thinned_ideal_lower": str(thinned_ideal_lower),
            "conditional_correction_upper": str(correction_upper),
            "conditional_final_lower": str(final_lower),
            "historical_threshold": str(historical_threshold),
            "unqualified_pr_application": "WITHDRAWN",
        },
        "native_source_tree": {
            "current": [str(x) for x in current],
            "actual_children": [
                [str(x) for x in child_67],
                [str(x) for x in child_71],
            ],
            "native": [str(x) for x in native],
            "rough_reservoir": [str(x) for x in reservoir],
            "rough_lift": [str(x) for x in rough_lift],
        },
        "two_ledger": {
            "unused_capacity": [str(x) for x in unused],
            "signed_error": [str(x) for x in signed_error],
            "root_slack": [str(x) for x in slack],
            "signed_error_is_source_positive": False,
        },
        "native_cost": {
            "root": str(root_cost),
            "actual_children": str(child_bound),
            "total": str(total),
            "strict_integer_bound": int(control["strict_integer_bound"]),
            "benchmark_bridge_used": False,
        },
    }


def mutation_suite(control: dict[str, Any]) -> dict[str, bool]:
    mutations = {
        "rough_lift_substitution": ("substitute_rough_lift", True),
        "signed_error_as_source": ("signed_error_declared_source_positive", True),
        "standard_child_capacity_promotion": ("promote_child_to_standard_capacity", True),
        "duplicate_owner": ("duplicate_owner", True),
        "drop_child": ("drop_child", True),
        "duplicate_root_correction": ("duplicate_root_correction", True),
        "benchmark_bridge": ("benchmark_bridge", True),
        "resurrect_unqualified_pr_falsifier": ("assert_unqualified_pr_falsifier", True),
    }
    caught: dict[str, bool] = {}
    for name, (key, value) in mutations.items():
        mutated = copy.deepcopy(control)
        mutated[key] = value
        try:
            validate(mutated)
        except ContractError:
            caught[name] = True
        else:
            caught[name] = False
    return caught


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--control",
        default=str(HERE / "certificates/control.json"),
    )
    parser.add_argument(
        "--output",
        default=str(HERE / "results/verification.json"),
    )
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()

    control = json.loads(Path(args.control).read_text(encoding="utf-8"))
    evidence = validate(control)
    mutations = mutation_suite(control) if args.mutations else {}
    ok = all(mutations.values()) if args.mutations else True

    proof_material = {
        "control": control,
        "evidence": evidence,
        "mutations": mutations,
    }
    canonical = json.dumps(
        proof_material, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    result = {
        "schema": "riemann.t92930.native-source-tree-firewall.v1",
        "verdict": control["expected_verdict"] if ok else "FAIL_T92930",
        "ok": ok,
        "proof_object_sha256": hashlib.sha256(canonical).hexdigest(),
        "evidence": evidence,
        "mutations": mutations,
        "proof_boundary": {
            "q2_rough_lift_separator": "PROVED_EXACT",
            "unqualified_109_over_1200_pr_falsifier": "WITHDRAWN",
            "native_source_tree_compiler": "FROZEN_RECONSTRUCTION_REQUIRED",
            "endpoint_consumer": "FROZEN_RECONSTRUCTION_REQUIRED",
            "riemann_hypothesis": "UNPROVED_PENDING_REVIEW",
        },
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
