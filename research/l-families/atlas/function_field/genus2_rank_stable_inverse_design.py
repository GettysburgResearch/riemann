#!/usr/bin/env python3
"""Inverse-design split filters null at both USp(4) and stable high genus.

The four-coordinate raw pool and the complete q=3,5,7 coefficient histograms
are imported through the locked genus-two inverse-design producer.  The new
search imposes the additional exact stable-Haar mean equation

    c1 + c2 + 2*c3 + 2*c4 = 0.

Only q=3,5 enter design.  The q=7 summary is accepted only by the subsequent
holdout audit.  No finite field, polynomial, curve, root, or member is
enumerated, and all arithmetic is integral or ``Fraction`` arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INVERSE_PRODUCER_PATH = HERE / "genus2_inverse_designed_split_filter.py"
INVERSE_FIXTURE_PATH = HERE / "genus2_inverse_designed_split_filter.json"
STABLE_PRODUCER_PATH = HERE / "usp_high_genus_interferometer_stability.py"
STABLE_FIXTURE_PATH = HERE / "usp_high_genus_interferometer_stability.json"
OUTPUT_PATH = HERE / "genus2_rank_stable_inverse_design.json"
NOTE_PATH = HERE / "GENUS2_RANK_STABLE_INVERSE_DESIGN.md"
TEST_PATH = ROOT / "tests" / "test_genus2_rank_stable_inverse_design.py"

TRAINING_Q_VALUES = (3, 5)
HELD_OUT_Q = 7
FROZEN_Q_VALUES = (*TRAINING_Q_VALUES, HELD_OUT_Q)
RAW_POOL_NAMES = ("I_(1,7)", "I_(1,9)", "I_(2,4)", "I_(2,8)")
STABLE_MEAN_VECTOR = (1, 1, 2, 2)
NULL_LATTICE_BASIS = (
    (-1, 1, 0, 0),
    (-2, 0, 1, 0),
    (-2, 0, 0, 1),
)
L1_CAP_INCLUSIVE = 8
SOURCE_ATOM_CAP_INCLUSIVE = 4_096
CANDIDATE_CAP_INCLUSIVE = 4_096
SCORE_EVALUATION_CAP_INCLUSIVE = 4_096

EXPECTED_LF_SHA256 = {
    "inverse_producer": "82226c433b7556e325a6c9b1ee6b88dee105662872f03267df437c4ad108d336",
    "inverse_fixture": "f0db62eded925d0907b1f7ae1a999f9a506b7d9160c3c1ba30994bf3329be7c5",
    "stable_producer": "cec434ded553f425636d32fd152d9810e7f4dfbc0eb780f080f5708fd20dc569",
    "stable_fixture": "6be5d2eb801e4ba1d65b308e7bc2f0b0929e6d4cc8aa41174f93cbd60688c219",
}
EXPECTED_PAYLOAD_SHA256 = {
    "inverse_fixture": "d3fb13ea244790bfcdf65a65b94397117f8c931ca6ecdd0c13fd8eb4896a2dda",
    "stable_fixture": "6f2893c8e62b836afbca99bb2fae4dfb57c4b24c8963d2cf0981b052dcb2f4ee",
}
EXPECTED_SOURCE_ATOMS = 251
EXPECTED_CANDIDATE_COUNT = 67
EXPECTED_TRAINING_ELIGIBLE_COUNT = 28
EXPECTED_HELD_OUT_SURVIVOR_COUNT = 2
EXPECTED_WINNER = (0, 2, -2, 1)
EXPECTED_RETROSPECTIVE_SURVIVOR = (2, 2, -1, -1)
PRIOR_F_STAR = (2, 4, -1, 1)


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _has_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(_has_float(key) or _has_float(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(_has_float(item) for item in value)
    return False


def _score_packet(score: Mapping[str, Fraction]) -> dict[str, list[int]]:
    return {name: _fraction_pair(value) for name, value in score.items()}


@dataclass
class ResourceGuard:
    """Fail-closed ledger for the bounded replay."""

    ledger: Counter[str] = field(default_factory=Counter)

    def charge(self, name: str, amount: int, cap: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise TypeError("resource charges must be nonnegative plain integers")
        if self.ledger[name] + amount > cap:
            raise RuntimeError(f"{name} inclusive cap would be exceeded")
        self.ledger[name] += amount

    def packet(self) -> dict[str, object]:
        return {
            "source_atom_cap_inclusive": SOURCE_ATOM_CAP_INCLUSIVE,
            "candidate_cap_inclusive": CANDIDATE_CAP_INCLUSIVE,
            "score_evaluation_cap_inclusive": SCORE_EVALUATION_CAP_INCLUSIVE,
            "ledger": dict(sorted(self.ledger.items())),
        }


def _verify_source_files() -> None:
    paths = {
        "inverse_producer": INVERSE_PRODUCER_PATH,
        "inverse_fixture": INVERSE_FIXTURE_PATH,
        "stable_producer": STABLE_PRODUCER_PATH,
        "stable_fixture": STABLE_FIXTURE_PATH,
    }
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"locked source is missing: {path}")
        observed = _lf_normalized_sha256(path)
        if observed != EXPECTED_LF_SHA256[name]:
            raise ValueError(f"locked source drifted for {name}: {observed}")


def _verified_fixture(path: Path, expected_payload: str) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = dict(data)
    claimed = payload.pop("payload_sha256", None)
    if claimed != expected_payload or claimed != _canonical_sha256(payload):
        raise ArithmeticError(f"fixture payload authentication failed: {path.name}")
    return data


def _load_locked_module(path: Path, digest: str, name: str) -> ModuleType:
    if _lf_normalized_sha256(path) != digest:
        raise ValueError(f"refusing to import drifted module: {path.name}")
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise ImportError(f"could not load locked module: {path.name}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def _stable_contract() -> dict[str, object]:
    stable = _verified_fixture(
        STABLE_FIXTURE_PATH, EXPECTED_PAYLOAD_SHA256["stable_fixture"]
    )
    pool = stable.get("inverse_raw_pool")
    if not isinstance(pool, dict):
        raise TypeError("stable fixture has no inverse raw pool")
    if tuple(pool.get("order", ())) != ("I_1_7", "I_1_9", "I_2_4", "I_2_8"):
        raise ValueError("stable raw-pool order drifted")
    if tuple(pool.get("USp4_means", ())) != (0, 0, 0, 0):
        raise ValueError("USp(4) raw-pool means drifted")
    if tuple(pool.get("stable_means", ())) != STABLE_MEAN_VECTOR:
        raise ValueError("stable raw-pool means drifted")
    lattice = pool.get("simultaneous_USp4_and_stable_null_lattice")
    if not isinstance(lattice, dict):
        raise TypeError("stable fixture has no simultaneous null lattice")
    if (
        tuple(tuple(row) for row in lattice.get("primitive_Z_basis_rows", ()))
        != NULL_LATTICE_BASIS
    ):
        raise ValueError("stable null-lattice basis drifted")
    if lattice.get("equation") != "c1+c2+2*c3+2*c4=0":
        raise ValueError("stable null equation drifted")
    return stable


def _source_summaries(inverse: ModuleType, guard: ResourceGuard) -> dict[int, object]:
    families = inverse._validated_families()
    engine = inverse._load_locked_module(
        inverse.INTERFEROMETER_PATH,
        inverse.EXPECTED_LF_SHA256["interferometer_engine"],
        "_locked_rank_stable_interferometer_engine",
    )
    split = inverse._load_locked_module(
        inverse.SPLIT_PREDICATE_PATH,
        inverse.EXPECTED_LF_SHA256["split_predicate"],
        "_locked_rank_stable_split_predicate",
    )
    dependency_guard = inverse.ResourceGuard()
    records = inverse._build_records(families, engine, split, dependency_guard)
    atom_count = sum(len(rows) for rows in records.values())
    if atom_count != EXPECTED_SOURCE_ATOMS:
        raise ArithmeticError("source atom count drifted")
    if dependency_guard.ledger["source_atoms"] != atom_count:
        raise ArithmeticError("dependency source-atom ledger drifted")
    guard.charge("source_atoms", atom_count, SOURCE_ATOM_CAP_INCLUSIVE)
    return {q: inverse._feature_summary(records[q]) for q in FROZEN_Q_VALUES}


def _candidate_vectors(guard: ResourceGuard) -> tuple[tuple[int, ...], ...]:
    candidates = []
    for coefficients in itertools.product(
        range(-L1_CAP_INCLUSIVE, L1_CAP_INCLUSIVE + 1), repeat=4
    ):
        if not any(coefficients):
            continue
        if sum(abs(value) for value in coefficients) > L1_CAP_INCLUSIVE:
            continue
        if math.gcd(*(abs(value) for value in coefficients)) != 1:
            continue
        if next(value for value in coefficients if value) < 0:
            continue
        if sum(
            coefficient * mean
            for coefficient, mean in zip(coefficients, STABLE_MEAN_VECTOR)
        ):
            continue
        guard.charge("candidates", 1, CANDIDATE_CAP_INCLUSIVE)
        candidates.append(coefficients)
    if len(candidates) != EXPECTED_CANDIDATE_COUNT:
        raise ArithmeticError("rank-stable primitive candidate count drifted")
    return tuple(candidates)


def _complexity(coefficients: Sequence[int]) -> tuple[object, ...]:
    return (
        sum(abs(value) for value in coefficients),
        sum(value != 0 for value in coefficients),
        max(abs(value) for value in coefficients),
        tuple(abs(value) for value in coefficients),
        tuple(coefficients),
    )


def _training_design(
    inverse: ModuleType,
    candidates: Sequence[tuple[int, ...]],
    training: Mapping[int, object],
    guard: ResourceGuard,
) -> dict[str, object]:
    """Design without accepting any q=7 object."""

    if tuple(sorted(training)) != TRAINING_Q_VALUES:
        raise ValueError("training design accepts exactly q=3,5 summaries")
    eligible = []
    objective_counts: Counter[tuple[Fraction, Fraction]] = Counter()
    for coefficients in candidates:
        scores = {}
        for q in TRAINING_Q_VALUES:
            guard.charge("score_evaluations", 1, SCORE_EVALUATION_CAP_INCLUSIVE)
            scores[q] = inverse._candidate_field_score(coefficients, training[q])
        if scores[3]["contrast"] * scores[5]["contrast"] <= 0:
            continue
        objective = (
            min(scores[3]["correlation_squared"], scores[5]["correlation_squared"]),
            scores[3]["correlation_squared"] + scores[5]["correlation_squared"],
        )
        complexity = _complexity(coefficients)
        objective_counts[objective] += 1
        eligible.append((coefficients, scores, objective, complexity))
    if len(eligible) != EXPECTED_TRAINING_ELIGIBLE_COUNT:
        raise ArithmeticError("training-eligible count drifted")
    best = max(
        eligible,
        key=lambda row: (
            row[2],
            tuple(-value for value in row[3][:3]),
            tuple(-value for value in row[3][3]),
            tuple(-value for value in row[3][4]),
        ),
    )
    orientation = 1 if best[1][3]["contrast"] > 0 else -1
    oriented = tuple(orientation * value for value in best[0])
    if oriented != EXPECTED_WINNER:
        raise ArithmeticError("rank-stable training winner drifted")
    if objective_counts[best[2]] != 1:
        raise ArithmeticError("rank-stable winning objective is no longer unique")
    return {
        "eligible_rows": eligible,
        "canonical_coefficients": best[0],
        "oriented_coefficients": oriented,
        "scores": best[1],
        "objective": best[2],
        "complexity": best[3],
        "winning_tie_count": objective_counts[best[2]],
    }


def _holdout_audit(
    inverse: ModuleType,
    design: Mapping[str, object],
    held_out_summary: object,
    guard: ResourceGuard,
) -> dict[str, object]:
    eligible_rows = design["eligible_rows"]
    if not isinstance(eligible_rows, list):
        raise TypeError("design eligibility ledger is malformed")
    survivor_rows = []
    winner_score = None
    for coefficients, training_scores, objective, complexity in eligible_rows:
        orientation = 1 if training_scores[3]["contrast"] > 0 else -1
        oriented = tuple(orientation * value for value in coefficients)
        guard.charge("score_evaluations", 1, SCORE_EVALUATION_CAP_INCLUSIVE)
        score7 = inverse._candidate_field_score(oriented, held_out_summary)
        if oriented == design["oriented_coefficients"]:
            winner_score = score7
        if score7["contrast"] > 0:
            survivor_rows.append(
                (oriented, training_scores, objective, complexity, score7, orientation)
            )
    if winner_score is None:
        raise ArithmeticError("winner was absent from holdout audit")
    if len(survivor_rows) != EXPECTED_HELD_OUT_SURVIVOR_COUNT:
        raise ArithmeticError("rank-stable holdout survivor count drifted")
    retrospective = max(
        survivor_rows,
        key=lambda row: (
            row[2],
            tuple(-value for value in row[3][:3]),
            tuple(-value for value in row[3][3]),
            tuple(-value for value in row[3][4]),
        ),
    )
    if retrospective[0] != EXPECTED_RETROSPECTIVE_SURVIVOR:
        raise ArithmeticError("retrospective survivor sentinel drifted")

    def survivor_packet(row: tuple[object, ...]) -> dict[str, object]:
        oriented, training_scores, objective, _complexity_row, score7, orientation = row
        return {
            "oriented_coefficients": list(oriented),
            "training_objective": [
                _fraction_pair(objective[0]),
                _fraction_pair(objective[1]),
            ],
            "field_scores": {
                "3": _score_packet(
                    {
                        name: orientation * value if name == "contrast" else value
                        for name, value in training_scores[3].items()
                    }
                ),
                "5": _score_packet(
                    {
                        name: orientation * value if name == "contrast" else value
                        for name, value in training_scores[5].items()
                    }
                ),
                "7": _score_packet(score7),
            },
        }

    return {
        "winner_score": winner_score,
        "survivor_rows": survivor_rows,
        "survivor_packets": [
            survivor_packet(row)
            for row in sorted(survivor_rows, key=lambda row: row[0])
        ],
        "retrospective_packet": survivor_packet(retrospective),
    }


def build_payload() -> dict[str, object]:
    _verify_source_files()
    _verified_fixture(INVERSE_FIXTURE_PATH, EXPECTED_PAYLOAD_SHA256["inverse_fixture"])
    stable = _stable_contract()
    inverse = _load_locked_module(
        INVERSE_PRODUCER_PATH,
        EXPECTED_LF_SHA256["inverse_producer"],
        "_locked_rank_stable_inverse_source",
    )
    guard = ResourceGuard()
    summaries = _source_summaries(inverse, guard)
    candidates = _candidate_vectors(guard)
    design = _training_design(
        inverse,
        candidates,
        {q: summaries[q] for q in TRAINING_Q_VALUES},
        guard,
    )
    holdout = _holdout_audit(inverse, design, summaries[HELD_OUT_Q], guard)

    prior_scores = {}
    for q in FROZEN_Q_VALUES:
        guard.charge("score_evaluations", 1, SCORE_EVALUATION_CAP_INCLUSIVE)
        prior_scores[q] = inverse._candidate_field_score(PRIOR_F_STAR, summaries[q])

    winner_scores = {
        **design["scores"],
        HELD_OUT_Q: holdout["winner_score"],
    }
    old_training_minimum = min(
        prior_scores[q]["correlation_squared"] for q in TRAINING_Q_VALUES
    )
    new_training_minimum = design["objective"][0]
    constrained_survival_fraction = Fraction(
        EXPECTED_HELD_OUT_SURVIVOR_COUNT, EXPECTED_TRAINING_ELIGIBLE_COUNT
    )
    old_survival_fraction = Fraction(80, 849)
    stable_pool = stable["inverse_raw_pool"]

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_rank_stable_inverse_design.v1",
        "status": "EXACT_BOUNDED_RANK_STABLE_TRAINING_WINNER_STILL_REVERSES_AT_Q7",
        "scope": (
            "member-uniform monic squarefree quintics at exactly q=3,5,7; "
            "compact Haar rank-stability is an imported mean constraint"
        ),
        "source_locks": {
            "lf_normalized_sha256": dict(EXPECTED_LF_SHA256),
            "canonical_payload_sha256": dict(EXPECTED_PAYLOAD_SHA256),
            "stable_theorem_source": stable["literature_dependency"],
        },
        "simultaneous_null_design_space": {
            "raw_pool_order": list(RAW_POOL_NAMES),
            "USp4_mean_vector": list(stable_pool["USp4_means"]),
            "high_genus_stable_mean_vector": list(STABLE_MEAN_VECTOR),
            "null_equation": "c1+c2+2*c3+2*c4=0",
            "primitive_Z_basis_rows": [list(row) for row in NULL_LATTICE_BASIS],
            "basis_parametrization": (
                "(u,v,w) maps to (-u-2v-2w,u,v,w); conversely u=c2, v=c3, w=c4"
            ),
            "nullity_scope": "mean-null at USp(4) and in the imported stable range; not pointwise or L2-null",
            "candidate_contract": (
                "primitive integer vectors modulo overall sign, first nonzero "
                "positive, ambient-coordinate L1<=8, satisfying the null equation"
            ),
            "L1_cap_inclusive": L1_CAP_INCLUSIVE,
            "candidate_count": len(candidates),
        },
        "training_design": {
            "training_q_values": list(TRAINING_Q_VALUES),
            "held_out_q_value": HELD_OUT_Q,
            "holdout_firewall": (
                "_training_design accepts exactly keys (3,5); only its frozen "
                "output enters _holdout_audit with the q=7 summary"
            ),
            "objective": (
                "require agreeing nonzero q3,q5 contrast signs; lexicographically "
                "maximize min(rho3^2,rho5^2), then their sum, with the inherited "
                "complexity tie-break"
            ),
            "training_eligible_candidate_count": EXPECTED_TRAINING_ELIGIBLE_COUNT,
            "training_rejected_direction_count": (
                EXPECTED_CANDIDATE_COUNT - EXPECTED_TRAINING_ELIGIBLE_COUNT
            ),
            "winning_objective_tie_count": design["winning_tie_count"],
            "winner_coefficients": list(design["oriented_coefficients"]),
            "winner_expression": "2*I_(1,9)-2*I_(2,4)+I_(2,8)",
            "winner_complexity": {
                "L1": design["complexity"][0],
                "support": design["complexity"][1],
                "maximum_absolute_coefficient": design["complexity"][2],
            },
            "winner_stable_mean": sum(
                coefficient * mean
                for coefficient, mean in zip(
                    design["oriented_coefficients"], STABLE_MEAN_VECTOR
                )
            ),
            "winner_field_scores": {
                str(q): _score_packet(winner_scores[q]) for q in FROZEN_Q_VALUES
            },
            "minimum_training_rho_squared": _fraction_pair(new_training_minimum),
        },
        "held_out_transport_audit": {
            "winner_verdict": "REVERSES_ON_HELD_OUT_Q7",
            "winner_q7_contrast": _fraction_pair(winner_scores[7]["contrast"]),
            "training_eligible_count": EXPECTED_TRAINING_ELIGIBLE_COUNT,
            "direction_survivor_count": EXPECTED_HELD_OUT_SURVIVOR_COUNT,
            "direction_reversal_or_zero_count": (
                EXPECTED_TRAINING_ELIGIBLE_COUNT - EXPECTED_HELD_OUT_SURVIVOR_COUNT
            ),
            "direction_survival_fraction": _fraction_pair(
                constrained_survival_fraction
            ),
            "all_survivors": holdout["survivor_packets"],
            "retrospective_best_training_rank_among_survivors": {
                **holdout["retrospective_packet"],
                "warning": "selected after q=7 labels were inspected; not a replacement detector",
            },
        },
        "comparison_with_prior_F_star": {
            "prior_coefficients": list(PRIOR_F_STAR),
            "prior_stable_mean": sum(
                coefficient * mean
                for coefficient, mean in zip(PRIOR_F_STAR, STABLE_MEAN_VECTOR)
            ),
            "prior_field_scores": {
                str(q): _score_packet(prior_scores[q]) for q in FROZEN_Q_VALUES
            },
            "prior_minimum_training_rho_squared": _fraction_pair(old_training_minimum),
            "new_to_prior_training_minimum_rho_squared_ratio": _fraction_pair(
                new_training_minimum / old_training_minimum
            ),
            "prior_lattice_direction_survival_fraction": _fraction_pair(
                old_survival_fraction
            ),
            "new_minus_prior_survival_fraction": _fraction_pair(
                constrained_survival_fraction - old_survival_fraction
            ),
            "new_to_prior_absolute_q7_contrast_ratio": _fraction_pair(
                abs(winner_scores[7]["contrast"]) / abs(prior_scores[7]["contrast"])
            ),
            "bounded_verdict": (
                "rank-stability removes the prior nonzero stable mean but does "
                "not improve direction transport: the new winner also reverses, "
                "and the constrained eligible lattice has a smaller exact q7 "
                "survival fraction"
            ),
        },
        "effect_size_definition": (
            "rho_q^2=pi_q*(1-pi_q)*(mean_split-mean_complement)^2/Var_all"
        ),
        "resource_contract": {
            "finite_field_or_curve_enumeration": False,
            "member_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "floating_point": False,
            **guard.packet(),
        },
        "interpretation_firewall": {
            "exact_claim": (
                "a complete bounded lattice search and exact three-field "
                "training/holdout comparison under an imported compact-Haar mean constraint"
            ),
            "finite_data_warning": (
                "q=3,5 training and one q=7 holdout do not establish an all-q law, "
                "asymptotic transport theorem, or optimal detector beyond the declared lattice"
            ),
            "forbidden_inference": (
                "mean nullity or finite split contrast does not identify a subgroup, "
                "split Jacobian, endomorphism algebra, motive, monodromy group, zero law, RH, or GRH consequence"
            ),
        },
    }
    if _has_float(payload):
        raise TypeError("claim payload contains a forbidden float")
    return payload


def build_fixture() -> dict[str, object]:
    payload = build_payload()
    fixture = dict(payload)
    fixture["payload_sha256"] = _canonical_sha256(payload)
    return fixture


def _check_committed() -> dict[str, object]:
    expected = build_fixture()
    observed = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    unhashed = dict(observed)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise ArithmeticError("committed fixture payload hash failed")
    if observed != expected:
        raise ArithmeticError("committed fixture differs from deterministic replay")
    return observed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write deterministic JSON")
    parser.add_argument("--check", action="store_true", help="check committed JSON")
    parser.add_argument("--show", action="store_true", help="print deterministic JSON")
    arguments = parser.parse_args()
    if sum((arguments.write, arguments.check, arguments.show)) > 1:
        parser.error("choose at most one of --write, --check, and --show")
    if arguments.write:
        fixture = build_fixture()
        OUTPUT_PATH.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    elif arguments.show:
        fixture = build_fixture()
        print(json.dumps(fixture, indent=2, sort_keys=True))
    else:
        fixture = _check_committed()
    print(
        "genus2 rank-stable inverse design: ok "
        f"candidates={fixture['simultaneous_null_design_space']['candidate_count']} "
        f"survivors={fixture['held_out_transport_audit']['direction_survivor_count']} "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
