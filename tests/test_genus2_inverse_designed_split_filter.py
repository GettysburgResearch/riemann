"""Independent checks for the bounded genus-two inverse-design packet."""

from __future__ import annotations

import importlib.util
import json
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
    / "genus2_inverse_designed_split_filter.py"
)
FIXTURE_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("GENUS2_INVERSE_DESIGNED_SPLIT_FILTER.md")

SPEC = importlib.util.spec_from_file_location(
    "genus2_inverse_designed_split_filter", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load inverse-design producer")
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


class Genus2InverseDesignedSplitFilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.payload = dict(cls.fixture)
        cls.claimed_hash = cls.payload.pop("payload_sha256")
        cls.by_q = {
            row["q"]: row for row in cls.fixture["exact_family_diagnostics"]["families"]
        }

    def test_payload_hash_and_deterministic_replay(self) -> None:
        self.assertEqual(
            self.claimed_hash,
            subject._canonical_sha256(self.payload),
        )
        self.assertEqual(self.fixture, subject.build_fixture())
        self.assertFalse(contains_float(self.fixture))

    def test_source_hashes_and_complete_histogram_sentinels(self) -> None:
        for name, required in subject.EXPECTED_LF_SHA256.items():
            path = {
                "histogram_fixture": subject.INPUT_PATH,
                "histogram_producer": subject.INPUT_PRODUCER_PATH,
                "interferometer_engine": subject.INTERFEROMETER_PATH,
                "split_predicate": subject.SPLIT_PREDICATE_PATH,
            }[name]
            self.assertEqual(subject._lf_normalized_sha256(path), required)
        self.assertEqual(
            self.fixture["source_locks"]["input_payload_sha256"],
            subject.EXPECTED_INPUT_PAYLOAD_SHA256,
        )
        self.assertEqual(
            [self.by_q[q]["signed_source_atom_count"] for q in (3, 5, 7)],
            [32, 81, 138],
        )
        self.assertEqual(
            [self.by_q[q]["member_count"] for q in (3, 5, 7)],
            [162, 2_500, 14_406],
        )

    def test_complete_ambient_zero_even_raw_pool_and_signatures(self) -> None:
        compact = self.fixture["compact_group_design_space"]
        self.assertEqual(
            tuple(tuple(row["frequencies"]) for row in compact["raw_pool"]),
            subject.RAW_POOL,
        )
        self.assertEqual(
            tuple(tuple(row["signature"]) for row in compact["raw_pool"]),
            subject.EXPECTED_RAW_SIGNATURES,
        )
        self.assertTrue(all(row["signature"][0] == 0 for row in compact["raw_pool"]))
        self.assertEqual(
            tuple(compact["winner_signature"]),
            subject.EXPECTED_WINNER_SIGNATURE,
        )
        decomposition = compact["exact_signature_decomposition"]
        self.assertEqual(decomposition["R_null_signature"], [0] * 7)
        reconstructed = [
            decomposition["P_signature"][index]
            + 2 * decomposition["D_signature"][index]
            + Fraction(decomposition["S_signature"][index], 2)
            for index in range(7)
        ]
        self.assertEqual(reconstructed, compact["winner_signature"])

    def test_candidate_cap_search_contract_and_unique_winner(self) -> None:
        contract = self.fixture["design_contract"]
        search = self.fixture["training_search_result"]
        self.assertEqual(contract["training_q_values"], [3, 5])
        self.assertEqual(contract["held_out_q_value"], 7)
        self.assertEqual(contract["candidate_count"], 1_640)
        self.assertLessEqual(contract["candidate_count"], 4_096)
        self.assertEqual(search["training_eligible_candidate_count"], 849)
        self.assertEqual(search["winning_objective_tie_count"], 1)
        self.assertEqual(
            search["rejected_opposite_or_zero_training_direction_count"], 791
        )
        self.assertEqual(
            tuple(search["canonical_coefficients_in_raw_pool_order"]),
            (2, 4, -1, 1),
        )
        self.assertEqual(
            tuple(search["training_oriented_coefficients_in_raw_pool_order"]),
            (2, 4, -1, 1),
        )
        self.assertEqual(
            search["complexity"],
            {"L1": 8, "support": 4, "maximum_absolute_coefficient": 4},
        )

    def test_training_objective_is_exact_and_winner_reverses_on_holdout(self) -> None:
        search = self.fixture["training_search_result"]
        scores = search["field_scores"]
        self.assertGreater(fraction(scores["3"]["contrast"]), 0)
        self.assertGreater(fraction(scores["5"]["contrast"]), 0)
        self.assertEqual(
            fraction(search["objective"]["minimum_training_rho_squared"]),
            min(
                fraction(scores["3"]["correlation_squared"]),
                fraction(scores["5"]["correlation_squared"]),
            ),
        )
        heldout = self.fixture["held_out_evaluation"]
        self.assertEqual(heldout["winner_direction_verdict"], "REVERSES_ON_HELD_OUT_Q7")
        self.assertLess(fraction(heldout["winner_q7_score"]["contrast"]), 0)
        self.assertEqual(heldout["direction_survivor_count_on_q7"], 80)
        self.assertEqual(heldout["direction_reversal_or_zero_count_on_q7"], 769)
        self.assertEqual(80 + 769, 849)

    def test_retrospective_survivor_is_not_promoted_and_collapses(self) -> None:
        row = self.fixture["held_out_evaluation"][
            "retrospective_best_training_rank_among_q7_survivors"
        ]
        self.assertIn("post hoc", row["warning"])
        self.assertEqual(
            tuple(row["oriented_coefficients_in_raw_pool_order"]),
            (2, 3, -2, -1),
        )
        for q in ("3", "5", "7"):
            self.assertGreater(fraction(row["field_scores"][q]["contrast"]), 0)
        self.assertLess(
            fraction(row["field_scores"]["7"]["correlation_squared"]),
            Fraction(1, 6_000),
        )

    def test_P_and_D_survive_while_S_and_inverse_winner_flip(self) -> None:
        comparison = self.fixture["benchmark_direction_comparison"]
        self.assertTrue(comparison["P"]["q7_direction_matches_q3"])
        self.assertTrue(comparison["D"]["q7_direction_matches_q3"])
        self.assertFalse(comparison["S"]["q7_direction_matches_q3"])
        self.assertGreater(fraction(comparison["P"]["contrast_by_q"]["3"]), 0)
        self.assertGreater(fraction(comparison["P"]["contrast_by_q"]["7"]), 0)
        self.assertLess(fraction(comparison["D"]["contrast_by_q"]["3"]), 0)
        self.assertLess(fraction(comparison["D"]["contrast_by_q"]["7"]), 0)

    def test_conditional_means_covariances_signs_and_tails_are_complete(self) -> None:
        expected_split_counts = {3: 27, 5: 705, 7: 3_570}
        for q, family in self.by_q.items():
            self.assertEqual(
                family["integral_plus_q_split_member_count"],
                expected_split_counts[q],
            )
            for conditioning in (
                "all_member_vector_moments",
                "split_conditional_vector_moments",
                "complement_conditional_vector_moments",
            ):
                packet = family[conditioning]
                matrix = packet["covariance_matrix"]
                self.assertEqual(len(matrix), 4)
                self.assertTrue(all(len(row) == 4 for row in matrix))
                for left in range(4):
                    self.assertGreaterEqual(fraction(matrix[left][left]), 0)
                    for right in range(4):
                        self.assertEqual(
                            fraction(matrix[left][right]),
                            fraction(matrix[right][left]),
                        )
            for detector in ("F_star", "P", "D", "S"):
                packet = family["detectors"][detector]
                signs = packet["sign_member_counts"]
                self.assertEqual(sum(signs["all"].values()), family["member_count"])
                self.assertEqual(sum(signs["split"].values()), expected_split_counts[q])
                self.assertEqual(
                    sum(signs["complement"].values()),
                    family["member_count"] - expected_split_counts[q],
                )
                tail = packet["outer_one_percent_absolute_tail"]
                self.assertGreaterEqual(
                    tail["member_count_including_ties"],
                    tail["target_member_count_ceiling"],
                )

    def test_root_free_polynomial_adapter_matches_declared_terms(self) -> None:
        adapter = self.fixture["root_free_reciprocal_quartic_adapter"]
        observed = {
            (a_power, e_power): coefficient
            for a_power, e_power, coefficient in adapter["winner_polynomial_terms"]
        }
        self.assertEqual(observed, subject.EXPECTED_WINNER_POLYNOMIAL)
        self.assertFalse(adapter["root_finding"])
        self.assertFalse(adapter["square_root_construction"])
        self.assertEqual(
            subject.winner_polynomial((2, 4, -1, 1)),
            subject.EXPECTED_WINNER_POLYNOMIAL,
        )

    def test_resource_caps_and_scope_firewall(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertEqual(resource["ledger"]["source_atoms"], 251)
        self.assertEqual(resource["ledger"]["candidates"], 1_640)
        self.assertLessEqual(
            resource["ledger"]["source_atoms"],
            resource["source_atom_cap_inclusive"],
        )
        self.assertLessEqual(
            resource["ledger"]["candidates"],
            resource["candidate_cap_inclusive"],
        )
        self.assertLess(
            resource["moment_contraction_total"],
            resource["moment_contraction_cap_exclusive"],
        )
        for forbidden in (
            "finite_field_enumeration",
            "curve_or_member_enumeration",
            "root_finding",
            "random_sampling",
            "external_data",
        ):
            self.assertFalse(resource[forbidden])
        firewall = self.fixture["interpretation_firewall"]["forbidden_inference"]
        for word in ("subgroup", "endomorphism", "motive", "monodromy", "RH/GRH"):
            self.assertIn(word, firewall)

    def test_normal_and_optimized_cli_replay(self) -> None:
        expected = "verdict=REVERSES_ON_HELD_OUT_Q7"
        for prefix in ([sys.executable], [sys.executable, "-O"]):
            completed = subprocess.run(
                [*prefix, str(MODULE_PATH), "--check"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertIn(expected, completed.stdout)

    def test_note_references_all_four_packet_files_and_hash(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for path in (MODULE_PATH, FIXTURE_PATH, NOTE_PATH, Path(__file__).resolve()):
            self.assertIn(path.name, note)
        self.assertIn(self.claimed_hash, note)
        self.assertIn("q=7", note)
        self.assertIn("held out", note.lower())


if __name__ == "__main__":
    unittest.main()
