"""Exact tests for the refusal-first cohomology inference packet."""

from __future__ import annotations

import inspect
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import guarded_cohomology_conjecture_inference as subject


class GuardedCohomologyConjectureInferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.build_certificate()
        cls.genus1 = cls.certificate["genus1_positive_control"]
        cls.genus2 = cls.certificate["genus2_guarded_candidates"]
        cls.channels = cls.genus2["channels"]

    def test_protocol_and_source_locks(self) -> None:
        self.assertEqual(
            self.certificate["status"],
            "EXACT_PROTOCOL_AND_NO_GO_WITH_GUARDED_CANDIDATES",
        )
        self.assertEqual(
            self.certificate["resource_contract"]["finite_fields_enumerated"], []
        )
        self.assertEqual(self.certificate["resource_contract"]["database_queries"], 0)
        self.assertEqual(
            self.certificate["resource_contract"]["frozen_q_values"], [3, 5, 7]
        )
        for name in ("genus1_fixture", "genus2_fixture"):
            lock = self.certificate["source_locks"][name]
            fixture_name = Path(lock["path"]).name
            self.assertEqual(
                lock["file_sha256_lf"],
                subject.EXPECTED_FIXTURE_SHA256_LF[fixture_name],
            )
            self.assertEqual(len(lock["payload_sha256"]), 64)
            self.assertEqual(len(lock["canonical_sha256"]), 64)

        source = inspect.getsource(subject)
        self.assertNotIn("genus2_q_scan", source)
        self.assertNotIn("balanced_control_family_scan", source)
        self.assertNotIn("requests", source)
        self.assertNotIn("assert ", source)

    def test_genus_one_positive_control_is_structural(self) -> None:
        self.assertEqual(self.genus1["status"], "POSITIVE_CONTROL_PASSED")
        decomposition = self.genus1["exact_su2_character_decomposition"]
        self.assertEqual(decomposition["usp2_catalan"], 42)
        self.assertEqual(
            [row["coefficient"] for row in decomposition["character_terms"]],
            [90, 75, 35, 9, 1],
        )
        rows = self.genus1["isolated_source_locked_rows"]
        self.assertEqual([row["q"] for row in rows], [3, 5, 7])
        self.assertEqual(
            [row["boundary_removed_theta12"] for row in rows],
            [252, 4830, -16744],
        )
        self.assertEqual(self.genus1["weight_inference"]["exact_dimension"], 1)
        self.assertEqual(
            self.genus1["identification"]["status"],
            "ACCEPTED_FROM_EXACT_STRUCTURE_NOT_PATTERN_MATCHING",
        )
        recurrence = self.genus1["symbolic_recurrence_control"]["audit"]
        self.assertEqual(recurrence["status"], "EXACT_RECURRENCE_MATCH")
        self.assertTrue(recurrence["matches"])

    def test_exact_c2_decompositions_and_weight_envelopes(self) -> None:
        expected = {
            "chi_(0,3)": ([3, 3], 6),
            "chi_(2,2)": ([4, 2], 6),
            "chi_(0,4)": ([4, 4], 8),
        }
        for name, (highest, weight) in expected.items():
            decomposition = self.channels[name]["exact_detector_decomposition"]
            self.assertEqual(decomposition["status"], "EXACT_IRREDUCIBLE_C2_CHARACTER")
            self.assertEqual(decomposition["highest_weight_e_basis"], highest)
            self.assertEqual(decomposition["multiplicity"], 1)
            envelope = self.channels[name]["conditional_weight_envelope"]
            self.assertEqual(envelope["local_system_weight"], weight)
            bounds = envelope["compact_support_degree_upper_weight_bounds"]
            self.assertEqual(
                [row["cohomological_degree"] for row in bounds], list(range(7))
            )
            self.assertEqual(
                [row["weight_at_most"] for row in bounds],
                list(range(weight, weight + 7)),
            )

    def test_complete_ambiguity_lattices(self) -> None:
        expected = {
            "chi_(0,3)": {
                "values": [74, 614, 2386],
                "base": [1574, -962, 154, 0, 0],
                "rank": 2,
                "coordinates": [15, 1],
                "minimum": 4,
                "nominated": [-1, -2, 0, 0, 1],
                "support": 3,
                "support_solutions": [
                    [-1, -2, 0, 0, 1],
                    [1574, -962, 154, 0, 0],
                ],
                "nominated_support_minimal": True,
                "nominated_unique_support": False,
            },
            "chi_(2,2)": {
                "values": [37, 213, 621],
                "base": [208, -144, 29, 0],
                "rank": 1,
                "coordinates": [2],
                "minimum": 7,
                "nominated": [-2, -2, -1, 2],
                "support": 3,
                "support_solutions": [[208, -144, 29, 0]],
                "nominated_support_minimal": False,
                "nominated_unique_support": False,
            },
            "chi_(0,4)": {
                "values": [-19, -51, -99],
                "base": [-1, 0, -2, 0],
                "rank": 1,
                "coordinates": [0],
                "minimum": 3,
                "nominated": [-1, 0, -2, 0],
                "support": 2,
                "support_solutions": [[-1, 0, -2, 0]],
                "nominated_support_minimal": True,
                "nominated_unique_support": True,
            },
        }
        vanisher = [-105, 71, -15, 1]
        for name, row in expected.items():
            ambiguity = self.channels[name]["ambiguity"]
            self.assertEqual(
                [item["normalized_trace"] for item in ambiguity["observations"]],
                row["values"],
            )
            self.assertEqual(
                ambiguity["base_quadratic_coefficients_low_to_high"], row["base"]
            )
            self.assertEqual(
                ambiguity["vanishing_polynomial_coefficients_low_to_high"],
                vanisher,
            )
            self.assertEqual(ambiguity["ambiguity_rank"], row["rank"])
            self.assertEqual(
                ambiguity["nominated_lattice_coordinates_low_to_high"],
                row["coordinates"],
            )
            self.assertEqual(ambiguity["minimum_l1_norm"], row["minimum"])
            self.assertEqual(ambiguity["minimum_l1_minimizers"], [row["nominated"]])
            self.assertTrue(ambiguity["nominated_is_unique_l1_minimizer"])
            self.assertEqual(ambiguity["minimum_monomial_support"], row["support"])
            self.assertEqual(
                ambiguity["minimum_support_solutions"], row["support_solutions"]
            )
            self.assertEqual(
                ambiguity["nominated_is_support_minimal"],
                row["nominated_support_minimal"],
            )
            self.assertEqual(
                ambiguity["nominated_is_unique_support_minimizer"],
                row["nominated_unique_support"],
            )

            base = ambiguity["base_quadratic_coefficients_low_to_high"]
            for basis in ambiguity["lattice_basis_coefficients_low_to_high"]:
                for scale in (-7, -1, 1, 9):
                    perturbed = [
                        base[index] + scale * basis[index] for index in range(len(base))
                    ]
                    for observation in ambiguity["observations"]:
                        self.assertEqual(
                            subject.evaluate_polynomial(perturbed, observation["q"]),
                            observation["normalized_trace"],
                        )

    def test_cross_prime_values_do_not_pass_recurrence_gate(self) -> None:
        for channel in self.channels.values():
            for audit in channel["recurrence_audits"]:
                self.assertEqual(
                    audit["status"],
                    "INSUFFICIENT_SAME_CHARACTERISTIC_EXTENSION_DATA",
                )
                self.assertEqual(audit["available_extension_degrees"], [1])
                self.assertEqual(audit["missing_extension_degrees"], [2, 3])
                self.assertIsNone(audit["determinant_exponent"])
                self.assertEqual(audit["determinant_status"], "NOT_INFERRED")

        rejection = subject.rank_two_recurrence_audit(3, 11, {1: 252, 2: 0, 3: 0})
        self.assertEqual(rejection["status"], "EXACT_RECURRENCE_REJECTION")
        self.assertFalse(rejection["matches"])

    def test_genus_two_names_are_refused(self) -> None:
        for channel in self.channels.values():
            schema = channel["machine_candidate_schema"]
            self.assertEqual(
                schema["status"],
                "CONJECTURE_UNIQUE_BY_L1_NOT_IDENTIFIED_COHOMOLOGICALLY",
            )
            self.assertIn("all-q theorem", schema["forbidden_promotions"])
            self.assertIn(
                "exact marked-stack/measure adapter", schema["proof_obligations"]
            )
            decision = channel["identification"]
            self.assertEqual(
                decision["status"],
                "REFUSED_UNSUPPORTED_COHOMOLOGY_IDENTIFICATION",
            )
            self.assertIn(
                "exact_family_trace_identity", decision["missing_requirements"]
            )
            self.assertIn("exact_geometric_adapter", decision["missing_requirements"])
            self.assertIn(
                "target_space_dimension_is_one", decision["missing_requirements"]
            )
        self.assertEqual(
            self.genus2["joint_no_go"]["status"], "EXACT_IDENTIFIABILITY_NO_GO"
        )

    def test_cli_json_is_serializable(self) -> None:
        encoded = json.dumps(self.certificate, allow_nan=False, sort_keys=True)
        self.assertIn("EXACT_IDENTIFIABILITY_NO_GO", encoded)
        self.assertIn("REFUSED_UNSUPPORTED_COHOMOLOGY_IDENTIFICATION", encoded)
        self.assertEqual(self.certificate, subject.build_certificate())


if __name__ == "__main__":
    unittest.main()
