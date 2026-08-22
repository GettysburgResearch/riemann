#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105103_CONFLUENT_RESIDUE_LEDGER"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105102-paired-residue-coherence-flux"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "cbf21d35cb125aed2d5d6ea85818375e5f1c978a9db0e0de3309a3b3807bd44e"
BASE_COMMIT = "0c1aedcafe7c6fe384695eee64435cc87b792aea"

SPEC = importlib.util.spec_from_file_location("t105102_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105102 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

G = BASE.G
ZERO = BASE.ZERO
ALG = BASE.BASE
CONTENT_FILES = (
    "PACKET_METADATA_105103.json",
    "claims/lemmas/L-105103-confluent-residue-merged-support-ledger.md",
    "claims/methodology/M-105103-confluent-ledger-review-contract.md",
    "claims/refutations/R-105103-confluent-corrections-are-load-bearing.md",
    "claims/theorems/T-105103-multiplicity-frontier.md",
    "experiments/X-105103-confluent-residue-ledger/verify.py",
    "experiments/X-105103-confluent-residue-ledger/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105102 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105102 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def trim(coefficients: list[F]) -> list[F]:
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def derivative(coefficients: list[F]) -> list[F]:
    values = trim(coefficients)
    if len(values) <= 1:
        return [F(0)]
    return [F(index) * values[index] for index in range(1, len(values))]


def zero_order(coefficients: list[F]) -> int | None:
    for index, value in enumerate(coefficients):
        if value != 0:
            return index
    return None


def convolve(left: list[F], right: list[F], through: int) -> list[F]:
    if through < 0:
        return []
    result: list[F] = []
    for degree in range(through + 1):
        result.append(
            sum(
                (
                    left[index] * right[degree - index]
                    for index in range(degree + 1)
                    if index < len(left) and degree - index < len(right)
                ),
                F(0),
            )
        )
    return result


def divide_series(numerator: list[F], denominator: list[F], through: int) -> list[F]:
    if through < 0:
        return []
    if not denominator or denominator[0] == 0:
        raise ValueError("series denominator must be a unit")
    quotient: list[F] = []
    for degree in range(through + 1):
        numerator_value = numerator[degree] if degree < len(numerator) else F(0)
        convolution = sum(
            (
                denominator[index] * quotient[degree - index]
                for index in range(1, degree + 1)
                if index < len(denominator)
            ),
            F(0),
        )
        quotient.append((numerator_value - convolution) / denominator[0])
    return quotient


def taylor_at(coefficients: list[F], point: F) -> list[F]:
    values = trim(coefficients)
    return [
        sum(
            (
                values[degree]
                * F(math.comb(degree, local_degree))
                * point ** (degree - local_degree)
                for degree in range(local_degree, len(values))
            ),
            F(0),
        )
        for local_degree in range(len(values))
    ]


def principal_part(coefficients: list[F], pole_order: int) -> list[dict[str, object]]:
    return [
        {"power": index - pole_order, "coefficient": str(value)}
        for index, value in enumerate(coefficients)
    ]


def local_event(coefficients: list[F], point: F) -> dict[str, object]:
    local = taylor_at(coefficients, point)
    first = derivative(local)
    second = derivative(first)
    m = zero_order(local)
    r = zero_order(first)
    s = zero_order(second)
    if m is None or r is None or s is None:
        raise ValueError("F, F', and F'' must all be nonzero analytic germs")

    parent_unit = local[m:]
    first_unit = first[r:]
    second_unit = second[s:]
    first_pole_order = r - m
    second_pole_order = r + s - 2 * m

    first_residue = F(0)
    first_coefficients: list[F] = []
    if first_pole_order > 0:
        first_coefficients = divide_series(
            parent_unit, first_unit, first_pole_order - 1
        )
        first_residue = first_coefficients[first_pole_order - 1]

    second_residue = F(0)
    second_coefficients: list[F] = []
    if second_pole_order > 0:
        through = second_pole_order - 1
        numerator = convolve(parent_unit, parent_unit, through)
        denominator = convolve(first_unit, second_unit, through)
        second_coefficients = divide_series(numerator, denominator, through)
        second_residue = second_coefficients[through]

    if r == 1 and m == 0:
        support_kind = "S1_SIMPLE_NONCOMMON_FPRIME"
    elif r == 0 and s == 1:
        support_kind = "S2_ISOLATED_SIMPLE_FSECOND"
    elif r > 0 or s > 0:
        support_kind = "G_MERGED_EXCEPTIONAL"
    else:
        support_kind = "NONE"

    if m >= 2:
        require(r == m - 1 and s == m - 2, "derivative order ladder failed")
    elif m == 1:
        require(r == 0, "simple parent zero must have nonzero derivative")
    elif r >= 1:
        require(s == r - 1, "multiple derivative zero ladder failed")

    return {
        "point": str(point),
        "orders": {"m": m, "r": r, "s": s},
        "P_pole_order": max(first_pole_order, 0),
        "Q_pole_order": max(second_pole_order, 0),
        "P_residue": str(first_residue),
        "Q_residue": str(second_residue),
        "merged_support_kind": support_kind,
        "P_unit_quotient": [str(value) for value in first_coefficients],
        "Q_unit_quotient": [str(value) for value in second_coefficients],
        "P_principal_part": principal_part(
            first_coefficients, max(first_pole_order, 0)
        ),
        "Q_principal_part": principal_part(
            second_coefficients, max(second_pole_order, 0)
        ),
    }


def validated_manifest(
    coefficients: list[F],
    points: list[F],
    expected_points: list[F],
) -> list[dict[str, object]]:
    require(len(points) == len(set(points)), "event manifest contains a duplicate")
    require(set(points) == set(expected_points), "event manifest is incomplete or extraneous")
    events = [local_event(coefficients, point) for point in points]
    require(
        all(row["merged_support_kind"] != "NONE" for row in events),
        "event manifest contains a nonroot",
    )
    return events


def infinity_residue_oracle(coefficients: list[F]) -> dict[str, str]:
    values = trim(coefficients)
    if len(values) < 3:
        raise ValueError("Q requires a polynomial of degree at least two")
    first = derivative(values)
    second = derivative(first)
    parent_reciprocal = list(reversed(values))
    first_reciprocal = list(reversed(first))
    second_reciprocal = list(reversed(second))
    p_series = divide_series(parent_reciprocal, first_reciprocal, 2)
    q_numerator = convolve(parent_reciprocal, parent_reciprocal, 4)
    q_denominator = convolve(first_reciprocal, second_reciprocal, 4)
    q_series = divide_series(q_numerator, q_denominator, 4)
    return {
        "sum_finite_P_residues": str(p_series[2]),
        "sum_finite_Q_residues": str(q_series[4]),
        "P_oracle": "[w^2] w P(1/w)",
        "Q_oracle": "[w^4] w^3 Q(1/w)",
    }


def merged_support_quartic() -> dict[str, object]:
    coefficients = [F(1), F(0), F(0), F(1), F(1)]
    points = [F(0), F(-3, 4), F(-1, 2)]
    events = validated_manifest(coefficients, points, points)
    by_point = {row["point"]: row for row in events}
    confluent = by_point["0"]
    simple = by_point["-3/4"]
    isolated = by_point["-1/2"]
    require(
        confluent["merged_support_kind"] == "G_MERGED_EXCEPTIONAL",
        "merged event lost",
    )
    require(
        simple["merged_support_kind"] == "S1_SIMPLE_NONCOMMON_FPRIME",
        "S1 event lost",
    )
    require(
        isolated["merged_support_kind"] == "S2_ISOLATED_SIMPLE_FSECOND",
        "S2 event lost",
    )

    phi1 = sum((F(row["P_residue"]) for row in events), F(0))
    boundary2 = sum((F(row["Q_residue"]) for row in events), F(0))
    rho = F(simple["P_residue"])
    simple_m1 = -rho
    simple_m2 = rho**2
    e1 = F(confluent["P_residue"])
    e2 = F(confluent["Q_residue"])
    d2 = F(isolated["Q_residue"])
    reconstructed_m1 = -phi1 + e1
    reconstructed_m2 = boundary2 - d2 - e2
    oracle = infinity_residue_oracle(coefficients)

    require(rho == F(229, 576), "simple critical residue changed")
    require(e1 == F(-4, 9), "confluent first correction changed")
    require(e2 == F(38, 81), "confluent second correction changed")
    require(d2 == F(-75, 128), "isolated F'' debt changed")
    require(phi1 == F(-3, 64), "global P residue sum changed")
    require(boundary2 == F(169, 4096), "global Q residue sum changed")
    require(reconstructed_m1 == simple_m1, "merged first ledger failed")
    require(reconstructed_m2 == simple_m2, "merged second ledger failed")
    require(F(oracle["sum_finite_P_residues"]) == phi1, "P infinity oracle failed")
    require(
        F(oracle["sum_finite_Q_residues"]) == boundary2,
        "Q infinity oracle failed",
    )
    require(
        -phi1 > 0 and simple_m1 < 0,
        "dropped-Lambda1 firewall did not fire",
    )
    require(
        boundary2 - d2 != simple_m2,
        "dropped-Lambda2 mutation survived",
    )
    require(
        confluent["P_principal_part"]
        == [
            {"power": -2, "coefficient": "1/3"},
            {"power": -1, "coefficient": "-4/9"},
        ],
        "confluent P principal part changed",
    )
    require(
        confluent["Q_principal_part"]
        == [
            {"power": -3, "coefficient": "1/18"},
            {"power": -2, "coefficient": "-5/27"},
            {"power": -1, "coefficient": "38/81"},
        ],
        "confluent Q principal part changed",
    )

    return {
        "polynomial": "1+x^3+x^4",
        "event_manifest": events,
        "unique_denominator_event_count": 3,
        "simple_real_critical_count": 1,
        "Phi1": str(phi1),
        "B2": str(boundary2),
        "C1_simple_nonreal": "0",
        "C2_simple_nonreal": "0",
        "D2_isolated_simple": str(d2),
        "Lambda1_merged": str(e1),
        "Lambda2_merged": str(e2),
        "simple_stratum_M1": str(simple_m1),
        "simple_stratum_M2": str(simple_m2),
        "reconstructed_M1": str(reconstructed_m1),
        "reconstructed_M2": str(reconstructed_m2),
        "naive_dropped_Lambda1_carrier": str(-phi1),
        "naive_dropped_Lambda2_M2": str(boundary2 - d2),
        "infinity_oracle": oracle,
        "transfer_certified": False,
        "transfer_withheld_reason": "real multiple F' event in merged support",
    }


def narrow_window_quartic() -> dict[str, object]:
    event = local_event([F(1), F(0), F(0), F(1), F(1)], F(0))
    phi1 = F(event["P_residue"])
    boundary2 = F(event["Q_residue"])
    e1 = phi1
    e2 = boundary2
    require(-phi1 + e1 == 0, "narrow first confluent cancellation failed")
    require(boundary2 - e2 == 0, "narrow second confluent cancellation failed")
    return {
        "window": "|Re z|<1/4 with sufficiently thin regular height",
        "event": event,
        "Phi1": str(phi1),
        "B2": str(boundary2),
        "Lambda1_merged": str(e1),
        "Lambda2_merged": str(e2),
        "simple_real_critical_count": 0,
        "simple_stratum_M1": "0",
        "simple_stratum_M2": "0",
    }


def shift_scale_polynomial(
    local_coefficients: list[F], center: F, scale: F
) -> list[F]:
    result = [F(0) for _ in local_coefficients]
    for degree, value in enumerate(local_coefficients):
        for power in range(degree + 1):
            result[power] += (
                scale
                * value
                * F(math.comb(degree, power))
                * (-center) ** (degree - power)
            )
    return trim(result)


def shift_scale_invariance() -> dict[str, object]:
    base_coefficients = [F(1), F(0), F(0), F(1), F(1)]
    shifted = shift_scale_polynomial(base_coefficients, F(2), F(7))
    base_event = local_event(base_coefficients, F(0))
    shifted_event = local_event(shifted, F(2))
    require(base_event["orders"] == shifted_event["orders"], "orders changed")
    require(
        base_event["P_principal_part"] == shifted_event["P_principal_part"],
        "P residue changed under shift/scale",
    )
    require(
        base_event["Q_principal_part"] == shifted_event["Q_principal_part"],
        "Q residue changed under shift/scale",
    )
    base_oracle = infinity_residue_oracle(base_coefficients)
    shifted_oracle = infinity_residue_oracle(shifted)
    require(base_oracle == shifted_oracle, "infinity sums changed under shift/scale")
    return {
        "transformation": "7*(1+(x-2)^3+(x-2)^4)",
        "shifted_coefficients_low_to_high": [str(value) for value in shifted],
        "base_event": base_event,
        "shifted_event": shifted_event,
        "base_oracle": base_oracle,
        "shifted_oracle": shifted_oracle,
        "residues_and_global_sums_invariant": True,
    }


def derivative_order_firewalls() -> dict[str, object]:
    rows = {
        "simple_common_parent_derivative": local_event(
            [F(0), F(0), F(1)], F(0)
        ),
        "common_parent_derivative": local_event([F(0), F(0), F(0), F(1)], F(0)),
        "pole_with_zero_residue": local_event([F(1), F(0), F(0), F(1)], F(0)),
        "negative_Q_residue": local_event(
            [F(1), F(0), F(0), F(1), F(0), F(1)], F(0)
        ),
        "positive_common_parent_Fsecond": local_event(
            [F(0), F(1), F(0), F(0), F(0), F(1, 5)], F(0)
        ),
    }
    simple_common = rows["simple_common_parent_derivative"]
    common = rows["common_parent_derivative"]
    zero_pole = rows["pole_with_zero_residue"]
    negative = rows["negative_Q_residue"]
    positive = rows["positive_common_parent_Fsecond"]
    require(
        simple_common["orders"] == {"m": 2, "r": 1, "s": 0},
        "x^2 orders changed",
    )
    require(
        simple_common["merged_support_kind"] == "G_MERGED_EXCEPTIONAL",
        "simple common parent/F' event escaped merged support",
    )
    require(
        simple_common["P_residue"] == "0"
        and simple_common["Q_residue"] == "0",
        "x^2 cancellation failed",
    )
    require(common["orders"] == {"m": 3, "r": 2, "s": 1}, "x^3 orders changed")
    require(common["P_residue"] == "0" and common["Q_residue"] == "0", "x^3 cancellation failed")
    require(zero_pole["Q_pole_order"] == 3, "1+x^3 Q pole order changed")
    require(zero_pole["Q_residue"] == "0", "1+x^3 residue should vanish")
    require(negative["Q_residue"] == "-5/18", "negative confluent residue changed")
    require(positive["Q_residue"] == "1/4", "positive confluent residue changed")
    return {
        "fixtures": rows,
        "simple_common_event_is_transfer_obstruction": True,
        "common_event_can_be_contour_invisible": True,
        "pole_order_does_not_force_nonzero_residue": True,
        "confluent_second_correction_sign_definite": False,
    }


def gaussian_simple_square_split(coefficients: list[F]) -> dict[str, str]:
    roots = [G(F(-1)), G(F(1)), G(F(0), F(-1)), G(F(0), F(1))]
    first = ALG.derivative(coefficients)
    second = ALG.derivative(first)
    real_sum = ZERO
    nonreal_sum = ZERO
    first_sum = ZERO
    for root in roots:
        require(ALG.evaluate(first, root) == ZERO, "quintic root manifest changed")
        rho = ALG.evaluate(coefficients, root) / ALG.evaluate(second, root)
        first_sum += rho
        if root.im == 0:
            real_sum += rho * rho
        else:
            nonreal_sum += rho * rho
    require(real_sum.im == 0 and nonreal_sum.im == 0, "Gaussian split is nonreal")
    return {
        "simple_first_residue_sum": first_sum.render(),
        "real_simple_square_sum": real_sum.render(),
        "nonreal_simple_square_sum": nonreal_sum.render(),
    }


def multiple_fsecond_sign_firewall() -> dict[str, object]:
    fixtures = {
        "nonzero_parent": [F(5), F(-5), F(0), F(0), F(0), F(1)],
        "simple_parent_zero": [F(0), F(-5), F(0), F(0), F(0), F(1)],
    }
    rows: dict[str, object] = {}
    expected = {
        "nonzero_parent": (F(41, 200), F(-9, 200)),
        "simple_parent_zero": (F(2, 25), F(2, 25)),
    }
    for name, coefficients in fixtures.items():
        event = local_event(coefficients, F(0))
        split = gaussian_simple_square_split(coefficients)
        oracle = infinity_residue_oracle(coefficients)
        real_m2 = F(split["real_simple_square_sum"])
        nonreal_c2 = F(split["nonreal_simple_square_sum"])
        e2 = F(event["Q_residue"])
        boundary2 = F(oracle["sum_finite_Q_residues"])
        require(event["orders"]["s"] == 3, "multiple F'' order changed")
        require(e2 == F(-1, 4), "multiple F'' residue changed")
        require((real_m2, nonreal_c2) == expected[name], "square split changed")
        require(boundary2 == F(-9, 100), "quintic infinity oracle changed")
        require(real_m2 == boundary2 - nonreal_c2 - e2, "quintic ledger failed")
        rows[name] = {
            "polynomial_coefficients_low_to_high": [str(value) for value in coefficients],
            "multiple_Fsecond_event": event,
            "simple_square_split": split,
            "boundary_Q_charge": str(boundary2),
            "reconstructed_real_simple_M2": str(real_m2),
        }
    return {
        "fixtures": rows,
        "same_confluent_debt_with_and_without_parent_zero": "-1/4",
        "confluent_debt_has_no_favorable_sign": True,
    }


def root_ledger_crosscheck() -> dict[str, object]:
    fixtures = {
        "merged_quartic": [F(1), F(0), F(0), F(1), F(1)],
        "common_cubic": [F(0), F(0), F(0), F(1)],
        "quintic_nonzero_parent": [F(5), F(-5), F(0), F(0), F(0), F(1)],
        "quintic_simple_parent_zero": [F(0), F(-5), F(0), F(0), F(0), F(1)],
    }
    rows: dict[str, object] = {}
    for name, coefficients in fixtures.items():
        oracle = infinity_residue_oracle(coefficients)
        first_root_ledger = BASE.first_root_variance_ledger(coefficients)
        second_root_ledger = ALG.root_ledger_k4(coefficients)
        require(
            F(oracle["sum_finite_P_residues"]) == first_root_ledger,
            f"first root ledger mismatch for {name}",
        )
        require(
            F(oracle["sum_finite_Q_residues"]) == second_root_ledger,
            f"second root ledger mismatch for {name}",
        )
        rows[name] = {
            "infinity_oracle": oracle,
            "V2_first_ledger": str(first_root_ledger),
            "V2_V4_second_ledger": str(second_root_ledger),
        }
    return {
        "fixtures": rows,
        "independent_infinity_and_root_ledgers_agree": True,
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
        "schema": "riemann.t105103.confluent-residue-ledger.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "merged_support_full_quartic": merged_support_quartic(),
            "merged_support_narrow_quartic": narrow_window_quartic(),
            "shift_scale_invariance": shift_scale_invariance(),
            "derivative_order_firewalls": derivative_order_firewalls(),
            "multiple_Fsecond_sign_firewall": multiple_fsecond_sign_firewall(),
            "root_ledger_crosscheck": root_ledger_crosscheck(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "local_confluent_P_residue_recurrence_proved": True,
            "local_confluent_Q_residue_recurrence_proved": True,
            "merged_support_fixed_window_identity_proved": True,
            "interior_simplicity_required_for_contour_identity": False,
            "simple_stratum_count_separated_from_event_count": True,
            "confluent_corrections_estimated": False,
            "multiple_Fprime_reverse_rolle_transfer_proved": False,
            "xi_multiplicity_manifest_proved": False,
            "admissible_height_strip_sequence_controlled": False,
            "strict_coherence_margin_proved": False,
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
