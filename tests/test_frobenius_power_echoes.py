from __future__ import annotations

import importlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

echoes = importlib.import_module("frobenius_power_echoes")


class FrobeniusPowerEchoesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = echoes.build_fixture()

    def test_newton_initial_and_second_power_formulas(self) -> None:
        samples = ((0, 0, 3), (2, 4, 5), (-5, 13, 7), (3, 7, 3))
        for a, b, q in samples:
            self.assertEqual(echoes.frobenius_power_coefficients(a, b, q, 1), (a, b))
            self.assertEqual(
                echoes.frobenius_power_coefficients(a, b, q, 2),
                (2 * b - a * a, b * b - 2 * q * a * a + 2 * q * q),
            )

    def test_pointwise_echo_recurrence(self) -> None:
        input_data = json.loads(echoes.INPUT_PATH.read_text(encoding="utf-8"))
        for family in input_data["frozen_enumeration_facts"]["families"]:
            q = family["q"]
            for atom in family["joint_a_D_b_D_law"]["atoms"]:
                values = []
                for power in range(1, echoes.MAX_POWER + 1):
                    a_power, b_power = echoes.frobenius_power_coefficients(
                        atom["a_D"], atom["b_D"], q, power
                    )
                    values.append(echoes.balanced_value(a_power, b_power, q, power))
                self.assertEqual(
                    echoes.echo_recurrence_profile(values[0], values[1], echoes.MAX_POWER)[1:],
                    values,
                )

    def test_independent_haar_moments_and_orthogonality(self) -> None:
        packet, operations = echoes.build_haar_packet()
        expected_moments = {
            1: [[0, 1], [2, 1], [0, 1], [12, 1]],
            **{
                power: [[0, 1], [4, 1], [0, 1], [36, 1]]
                for power in range(2, echoes.MAX_POWER + 1)
            },
        }
        for row in packet["moments"]:
            self.assertEqual(
                [entry["haar_moment"] for entry in row["moments_1_through_4"]],
                expected_moments[row["power"]],
            )
        matrix = packet["pairwise_cross_moment_matrix"]["entries"]
        for left in range(echoes.MAX_POWER):
            for right in range(echoes.MAX_POWER):
                expected = [2 if left == right == 0 else 4 if left == right else 0, 1]
                self.assertEqual(matrix[left][right], expected)
        self.assertLess(operations["total"], echoes.MAX_LAURENT_OPERATIONS)

    def test_distinct_triple_additive_resonances(self) -> None:
        packet, _ = echoes.build_haar_packet()
        triple_packet = packet["strictly_distinct_mixed_third_moments"]
        self.assertEqual(triple_packet["triple_count"], 56)
        self.assertEqual(triple_packet["zero_triple_count"], 44)
        for record in triple_packet["nonzero_triples"]:
            left, middle, right = record["powers"]
            self.assertEqual(left + middle, right)
            self.assertEqual(
                record["haar_mixed_third_moment"], [-2 if left == 1 else -4, 1]
            )

        guard = echoes.ResourceGuard()
        density = echoes.c2_weyl_density(guard)
        for powers, expected in (((1, 11, 12), -2), ((7, 9, 16), -4), ((4, 7, 12), 0)):
            polynomial = {(0, 0): 1}
            for power in powers:
                polynomial = echoes.laurent_multiply(
                    polynomial, echoes.balanced_power_laurent(power), guard
                )
            self.assertEqual(
                echoes.haar_constant_term(polynomial, density, guard), expected
            )

    def test_frozen_family_accounting_and_two_coordinate_collapse(self) -> None:
        families = self.fixture["frozen_family_laws"]["families"]
        self.assertEqual([family["q"] for family in families], [3, 5, 7])
        for family in families:
            self.assertEqual(len(family["powers"]), echoes.MAX_POWER)
            prefix_counts = [
                record["count"] for record in family["prefix_distinct_profile_counts"]
            ]
            self.assertEqual(prefix_counts[1], prefix_counts[-1])
            self.assertTrue(all(
                prefix_counts[index] <= prefix_counts[index + 1]
                for index in range(len(prefix_counts) - 1)
            ))
            for row in family["powers"]:
                self.assertEqual(sum(row["sign_member_counts"].values()), family["member_count"])
                self.assertEqual(
                    sum(
                        atom[2]
                        for atom in row["powered_coefficient_joint_law"]["atoms"]
                    ),
                    family["member_count"],
                )
                self.assertEqual(
                    sum(
                        atom[2]
                        for atom in row["balanced_member_law"]["atoms"]
                    ),
                    family["member_count"],
                )
                self.assertEqual(
                    row["support_size"], row["balanced_member_law"]["support_size"]
                )
                self.assertLessEqual(
                    row["endpoint_member_counts"]["minus_four"]
                    + row["endpoint_member_counts"]["plus_four"],
                    family["member_count"],
                )

    def test_periodic_strata_have_exact_spectral_forms(self) -> None:
        families = self.fixture["frozen_family_laws"]["families"]
        self.assertEqual(
            [len(family["globally_periodic_or_antiperiodic_echoes"]) for family in families],
            [2, 2, 2],
        )
        for family in families:
            for signature in family["globally_periodic_or_antiperiodic_echoes"]:
                for state in signature["coefficient_states"]:
                    self.assertIn("recognized_exact_spectral_form", state)
                    self.assertIn(
                        "root", state["recognized_exact_spectral_form"]["spectral_statement"]
                    )

    def test_second_power_candidate_is_quarantined_and_matches_frozen_data(self) -> None:
        candidate = self.fixture["frozen_pattern_conjectures"]["mean_B2"]
        self.assertTrue(candidate["status"].startswith("CONJECTURAL_"))
        for evaluation in candidate["frozen_evaluations"]:
            self.assertEqual(
                Fraction(*evaluation["observed_mean_B2"]),
                echoes.conjectural_second_power_mean(evaluation["q"]),
            )
            self.assertTrue(evaluation["matches"])

    def test_resource_contract_and_no_field_enumeration(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertFalse(resource["finite_field_enumeration"])
        self.assertLess(
            resource["actual_laurent_operations"]["total"],
            resource["maximum_laurent_operations"],
        )
        self.assertLess(
            resource["actual_histogram_atom_steps"],
            resource["maximum_histogram_atom_steps"],
        )

    def test_source_locks_and_payload_hash(self) -> None:
        locks = self.fixture["producer_and_source_locks"]["locks"]
        expected_paths = {
            "input_fixture": echoes.INPUT_PATH,
            "input_producer": echoes.INPUT_PRODUCER_PATH,
            "producer": Path(echoes.__file__),
            "note": echoes.NOTE_PATH,
            "test": echoes.TEST_PATH,
        }
        for name, path in expected_paths.items():
            self.assertEqual(
                locks[name]["sha256_lf_normalized"],
                echoes._lf_normalized_sha256(path),
            )
        input_fixture = json.loads(echoes.INPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            locks["input_fixture"]["payload_sha256"],
            input_fixture["payload_sha256"],
        )
        payload = dict(self.fixture)
        digest = payload.pop("payload_sha256")
        self.assertEqual(digest, echoes._canonical_sha256(payload))

    def test_committed_fixture_is_current(self) -> None:
        committed = json.loads(echoes.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(committed, self.fixture)


if __name__ == "__main__":
    unittest.main()
