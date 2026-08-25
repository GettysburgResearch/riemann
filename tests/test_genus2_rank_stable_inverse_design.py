"""Independent checks for the bounded rank-stable inverse-design packet."""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_rank_stable_inverse_design.py"
)
FIXTURE_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("GENUS2_RANK_STABLE_INVERSE_DESIGN.md")

SPEC = importlib.util.spec_from_file_location(
    "genus2_rank_stable_inverse_design", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load rank-stable inverse-design producer")
subject = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subject
SPEC.loader.exec_module(subject)


def fraction(pair: list[int]) -> Fraction:
    return Fraction(pair[0], pair[1])


def contains_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(
            contains_float(key) or contains_float(item) for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(contains_float(item) for item in value)
    return False


class Genus2RankStableInverseDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.payload = dict(cls.fixture)
        cls.claimed_hash = cls.payload.pop("payload_sha256")

    def test_payload_hash_replay_and_exact_arithmetic(self) -> None:
        self.assertEqual(
            self.claimed_hash,
            subject._canonical_sha256(self.payload),
        )
        self.assertEqual(self.fixture, subject.build_fixture())
        self.assertFalse(contains_float(self.fixture))

    def test_all_four_source_locks_and_payload_locks(self) -> None:
        paths = {
            "inverse_producer": subject.INVERSE_PRODUCER_PATH,
            "inverse_fixture": subject.INVERSE_FIXTURE_PATH,
            "stable_producer": subject.STABLE_PRODUCER_PATH,
            "stable_fixture": subject.STABLE_FIXTURE_PATH,
        }
        for name, path in paths.items():
            self.assertEqual(
                subject._lf_normalized_sha256(path),
                subject.EXPECTED_LF_SHA256[name],
            )
        for name, path in (
            ("inverse_fixture", subject.INVERSE_FIXTURE_PATH),
            ("stable_fixture", subject.STABLE_FIXTURE_PATH),
        ):
            source = json.loads(path.read_text(encoding="utf-8"))
            payload = dict(source)
            claimed = payload.pop("payload_sha256")
            self.assertEqual(claimed, subject.EXPECTED_PAYLOAD_SHA256[name])
            self.assertEqual(claimed, subject._canonical_sha256(payload))

    def test_null_lattice_basis_is_integral_saturated_and_rank_three(self) -> None:
        packet = self.fixture["simultaneous_null_design_space"]
        means = tuple(packet["high_genus_stable_mean_vector"])
        basis = tuple(tuple(row) for row in packet["primitive_Z_basis_rows"])
        self.assertEqual(means, (1, 1, 2, 2))
        self.assertEqual(basis, subject.NULL_LATTICE_BASIS)
        for row in basis:
            self.assertEqual(sum(a * b for a, b in zip(row, means)), 0)
        # The displayed inverse proves saturation, not merely rational span.
        for u, v, w in itertools.product(range(-2, 3), repeat=3):
            c = (-u - 2 * v - 2 * w, u, v, w)
            self.assertEqual(sum(a * b for a, b in zip(c, means)), 0)
            rebuilt = tuple(
                u * basis[0][i] + v * basis[1][i] + w * basis[2][i] for i in range(4)
            )
            self.assertEqual(rebuilt, c)

    def test_candidate_count_is_independently_exhaustive_under_l1_cap(self) -> None:
        candidates = []
        for coefficients in itertools.product(range(-8, 9), repeat=4):
            if not any(coefficients):
                continue
            if sum(abs(value) for value in coefficients) > 8:
                continue
            if math.gcd(*(abs(value) for value in coefficients)) != 1:
                continue
            if next(value for value in coefficients if value) < 0:
                continue
            if (
                coefficients[0]
                + coefficients[1]
                + 2 * coefficients[2]
                + 2 * coefficients[3]
            ):
                continue
            candidates.append(coefficients)
        self.assertEqual(len(candidates), 67)
        self.assertEqual(
            self.fixture["simultaneous_null_design_space"]["candidate_count"],
            len(candidates),
        )
        self.assertIn((0, 2, -2, 1), candidates)
        self.assertNotIn((2, 4, -1, 1), candidates)

    def test_unique_training_winner_and_exact_effect_sizes(self) -> None:
        design = self.fixture["training_design"]
        self.assertEqual(design["training_q_values"], [3, 5])
        self.assertEqual(design["held_out_q_value"], 7)
        self.assertEqual(design["training_eligible_candidate_count"], 28)
        self.assertEqual(design["training_rejected_direction_count"], 39)
        self.assertEqual(design["winning_objective_tie_count"], 1)
        self.assertEqual(tuple(design["winner_coefficients"]), (0, 2, -2, 1))
        self.assertEqual(design["winner_stable_mean"], 0)
        expected = {
            "3": (
                Fraction(8144, 2187),
                Fraction(10363240, 209169793),
            ),
            "5": (
                Fraction(22200752, 6327375),
                Fraction(38505733544180, 804703506645951),
            ),
            "7": (
                Fraction(-80029416, 61429585),
                Fraction(266862809387544, 44725418124652915),
            ),
        }
        for q, (contrast, rho_squared) in expected.items():
            score = design["winner_field_scores"][q]
            self.assertEqual(fraction(score["contrast"]), contrast)
            self.assertEqual(fraction(score["correlation_squared"]), rho_squared)
        self.assertEqual(
            fraction(design["minimum_training_rho_squared"]),
            expected["5"][1],
        )

    def test_holdout_reversal_and_complete_survivor_ledger(self) -> None:
        holdout = self.fixture["held_out_transport_audit"]
        self.assertEqual(holdout["winner_verdict"], "REVERSES_ON_HELD_OUT_Q7")
        self.assertLess(fraction(holdout["winner_q7_contrast"]), 0)
        self.assertEqual(holdout["training_eligible_count"], 28)
        self.assertEqual(holdout["direction_survivor_count"], 2)
        self.assertEqual(holdout["direction_reversal_or_zero_count"], 26)
        self.assertEqual(
            fraction(holdout["direction_survival_fraction"]), Fraction(1, 14)
        )
        survivors = {
            tuple(row["oriented_coefficients"]): row for row in holdout["all_survivors"]
        }
        self.assertEqual(
            set(survivors),
            {(1, 3, -1, -1), (2, 2, -1, -1)},
        )
        for row in survivors.values():
            for q in ("3", "5", "7"):
                self.assertGreater(fraction(row["field_scores"][q]["contrast"]), 0)
        retrospective = holdout["retrospective_best_training_rank_among_survivors"]
        self.assertEqual(
            tuple(retrospective["oriented_coefficients"]),
            (2, 2, -1, -1),
        )
        self.assertIn("not a replacement", retrospective["warning"])

    def test_rank_stability_does_not_improve_bounded_transport(self) -> None:
        comparison = self.fixture["comparison_with_prior_F_star"]
        self.assertEqual(comparison["prior_stable_mean"], 6)
        self.assertLess(fraction(comparison["prior_field_scores"]["7"]["contrast"]), 0)
        self.assertEqual(
            fraction(comparison["prior_lattice_direction_survival_fraction"]),
            Fraction(80, 849),
        )
        self.assertEqual(
            fraction(comparison["new_minus_prior_survival_fraction"]),
            Fraction(-271, 11886),
        )
        self.assertLess(
            fraction(comparison["new_to_prior_training_minimum_rho_squared_ratio"]),
            1,
        )
        self.assertLess(
            fraction(comparison["new_to_prior_absolute_q7_contrast_ratio"]),
            1,
        )
        self.assertIn("does not improve", comparison["bounded_verdict"])

    def test_training_api_rejects_a_q7_summary(self) -> None:
        inverse = subject._load_locked_module(
            subject.INVERSE_PRODUCER_PATH,
            subject.EXPECTED_LF_SHA256["inverse_producer"],
            "_rank_stable_api_test_inverse",
        )
        guard = subject.ResourceGuard()
        summaries = subject._source_summaries(inverse, guard)
        candidates = subject._candidate_vectors(guard)
        with self.assertRaisesRegex(ValueError, "exactly q=3,5"):
            subject._training_design(inverse, candidates, summaries, guard)

    def test_resource_caps_and_claim_firewall(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertEqual(
            resource["ledger"],
            {"candidates": 67, "score_evaluations": 165, "source_atoms": 251},
        )
        for name, cap_name in (
            ("candidates", "candidate_cap_inclusive"),
            ("score_evaluations", "score_evaluation_cap_inclusive"),
            ("source_atoms", "source_atom_cap_inclusive"),
        ):
            self.assertLessEqual(resource["ledger"][name], resource[cap_name])
            self.assertLessEqual(resource[cap_name], 4096)
        for forbidden in (
            "finite_field_or_curve_enumeration",
            "member_enumeration",
            "root_finding",
            "random_sampling",
            "floating_point",
        ):
            self.assertFalse(resource[forbidden])
        firewall = self.fixture["interpretation_firewall"]
        self.assertIn("q=3,5", firewall["finite_data_warning"])
        for word in ("subgroup", "motive", "monodromy", "RH"):
            self.assertIn(word, firewall["forbidden_inference"])

    def test_normal_and_optimized_cli_replay(self) -> None:
        for prefix in ([sys.executable], [sys.executable, "-O"]):
            completed = subprocess.run(
                [*prefix, str(MODULE_PATH), "--check"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertIn("candidates=67 survivors=2", completed.stdout)

    def test_note_references_four_files_hash_and_finite_scope(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for path in (MODULE_PATH, FIXTURE_PATH, NOTE_PATH, Path(__file__).resolve()):
            self.assertIn(path.name, note)
        self.assertIn(self.claimed_hash, note)
        self.assertIn("q=7", note)
        self.assertIn("does **not** repair transport", note)
        self.assertIn("all-q", note)


if __name__ == "__main__":
    unittest.main()
