"""Replay tests for the source-locked product-variety tensor packet."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import product_variety_tensor_family as subject  # noqa: E402


class ProductVarietyTensorFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            row["q"]: row for row in cls.fixture["frozen_histogram_convolutions"]
        }

    def test_closed_tensor_polynomial_equals_independent_newton_recurrence(self) -> None:
        genus1 = json.loads(subject.GENUS1_FIXTURE_PATH.read_text(encoding="utf-8"))
        balanced = json.loads(subject.BALANCED_FIXTURE_PATH.read_text(encoding="utf-8"))
        genus1_by_q = {row["q"]: row for row in genus1["finite_regressions"]}
        genus2_by_q = {
            row["q"]: row
            for row in balanced["frozen_enumeration_facts"]["families"]
        }
        operations = 0
        for q in subject.FROZEN_Q_VALUES:
            e_histogram = genus1_by_q[q]["model_trace_histogram"]
            genus2_atoms = genus2_by_q[q]["joint_a_D_b_D_law"]["atoms"]
            for trace_e_text in e_histogram:
                for atom in genus2_atoms:
                    # The source fixture stores t_E in 1-t_E*T+q*T^2;
                    # the tensor packet uses A=-t_E in 1+A*T+q*T^2.
                    a_e = -int(trace_e_text)
                    a_c = atom["a_D"]
                    b_c = atom["b_D"]
                    closed = subject.tensor_coefficients(a_e, a_c, b_c, q)
                    recurrence = subject.tensor_coefficients_via_newton(
                        a_e, a_c, b_c, q
                    )
                    self.assertEqual(closed, recurrence)
                    self.assertEqual(subject.tensor_hypersurface_residual(closed, q), 0)
                    self.assertEqual(closed[5], q**2 * closed[3])
                    self.assertEqual(closed[6], q**4 * closed[2])
                    self.assertEqual(closed[7], q**6 * closed[1])
                    self.assertEqual(closed[8], q**8)
                    operations += 1
        self.assertEqual(operations, 2471)
        self.assertLess(operations, subject.MAX_EXACT_OPERATIONS)

    def test_rank_three_hypersurface_includes_trace_zero(self) -> None:
        q = 7
        coefficients = subject.tensor_coefficients(0, 5, -3, q)
        self.assertEqual(coefficients[1], 0)
        self.assertEqual(coefficients[3], 0)
        self.assertEqual(subject.tensor_hypersurface_residual(coefficients, q), 0)
        theorem = self.fixture["rank_three_coefficient_hypersurface"]
        self.assertEqual(theorem["status"], "EXACT_MEMBERWISE_NOT_A_STATISTICAL_FIT")
        self.assertIn("u^2*h", theorem["equation"])

    def test_exact_all_q_trace_moments_and_factorization(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            expected = {
                0: Fraction(1),
                1: Fraction(0),
                2: Fraction(
                    (q**2 - 1) * (q**4 - q**3 + q**2 + q - 2), q**6
                ),
                3: Fraction(0),
                4: Fraction(
                    (2 * q**3 - 3 * q - 1)
                    * (3 * q**5 - 7 * q**4 + 5 * q**3 + 12 * q**2 - 14 * q - 11),
                    q**8,
                ),
            }
            for order in range(5):
                self.assertEqual(
                    subject.tensor_normalized_trace_moment(order, q), expected[order]
                )
                self.assertEqual(
                    subject.tensor_normalized_trace_moment(order, q),
                    subject.genus1_normalized_trace_moment(order, q)
                    * subject.genus2_normalized_trace_moment(order, q),
                )

    def test_exact_all_q_coefficient_fingerprint_means(self) -> None:
        for q in (3, 5, 7, 9, 11, 25, 49):
            means = subject.all_q_coefficient_fingerprint_means(q)
            self.assertEqual(
                means["mean_v"],
                -Fraction((q - 1) * (q**3 - q**2 + q + 1), q**6),
            )
            self.assertEqual(
                means["mean_h"],
                Fraction(q**6 - 2 * q**5 + q**4 - 2 * q**2 - 2 * q + 2, q**6),
            )
            self.assertEqual(
                means["mean_u_times_w"],
                Fraction(
                    (q - 1)
                    * (q + 1) ** 2
                    * (q**4 - 4 * q**3 + 5 * q**2 - q - 5),
                    q**7,
                ),
            )

    def test_product_haar_and_generic_so8_first_diverge_at_fourth_trace_moment(self) -> None:
        usp2 = [
            subject.symplectic_standard_haar_moment(1, order)
            for order in range(9)
        ]
        usp4 = [
            subject.symplectic_standard_haar_moment(2, order)
            for order in range(9)
        ]
        self.assertEqual(usp2, [1, 0, 1, 0, 2, 0, 5, 0, 14])
        self.assertEqual(usp4, [1, 0, 1, 0, 3, 0, 14, 0, 84])
        product = [subject.product_haar_trace_moment(order) for order in range(7)]
        so8 = [subject.so8_standard_trace_haar_moment(order) for order in range(7)]
        self.assertEqual(product, [1, 0, 1, 0, 6, 0, 70])
        self.assertEqual(so8, [1, 0, 1, 0, 3, 0, 15])
        self.assertEqual(product[:4], so8[:4])
        self.assertNotEqual(product[4], so8[4])
        fingerprint = self.fixture["compact_group_baselines"]
        self.assertEqual(fingerprint["earliest_trace_moment_fingerprint"]["order"], 4)
        self.assertEqual(
            fingerprint["coefficient_fingerprints_at_same_representation_degree"],
            {
                "mean_h_product_image": 1,
                "mean_h_SO8": 0,
                "mean_u_times_w_product_image": 1,
                "mean_u_times_w_SO8": 0,
                "proof": "the product image has one invariant in exterior^4(V2 tensor V4) and one copy of V2 tensor V4 inside exterior^3; generic SO(8) has neither",
            },
        )

    def test_frozen_laws_are_complete_histogram_convolutions(self) -> None:
        expected_counts = {
            3: 18 * 162,
            5: 100 * 2500,
            7: 294 * 14406,
        }
        expected_pair_operations = {3: 7 * 32, 5: 9 * 81, 7: 11 * 138}
        expected_compressed_sizes = {
            3: (112, 13, 41),
            5: (354, 27, 106),
            7: (751, 45, 236),
        }
        for q, row in self.by_q.items():
            self.assertEqual(row["product_model_pair_count"], expected_counts[q])
            self.assertEqual(
                row["source_histogram_sizes"]["cartesian_atom_pairs"],
                expected_pair_operations[q],
            )
            coefficient_law = row["complete_tensor_coefficient_law"]
            self.assertEqual(
                (
                    coefficient_law["atom_count_after_exact_compression"],
                    row["normalized_trace_law"]["support_size"],
                    row["normalized_middle_coefficient_law"]["support_size"],
                ),
                expected_compressed_sizes[q],
            )
            self.assertEqual(
                sum(atom["pair_count"] for atom in coefficient_law["atoms"]),
                expected_counts[q],
            )
            trace_law = row["normalized_trace_law"]
            self.assertEqual(
                sum(atom["pair_count"] for atom in trace_law["atoms"]),
                expected_counts[q],
            )
            for record in trace_law["moments_0_through_8"][:5]:
                self.assertTrue(record["all_q_formula_checked"])
                self.assertEqual(
                    Fraction(*record["family_mean_normalized_trace_to_order"]),
                    subject.tensor_normalized_trace_moment(record["order"], q),
                )
            fingerprints = row["coefficient_fingerprint_means"]
            exact = subject.all_q_coefficient_fingerprint_means(q)
            self.assertEqual(Fraction(*fingerprints["mean_v"]), exact["mean_v"])
            self.assertEqual(Fraction(*fingerprints["mean_h"]), exact["mean_h"])
            self.assertEqual(
                Fraction(*fingerprints["mean_u_times_w"]), exact["mean_u_times_w"]
            )

    def test_twist_and_measure_firewall(self) -> None:
        self.assertEqual(
            self.fixture["input_convention_bridge"]["frozen_histogram_conversion"],
            "each genus-one trace key t_E is negated before tensor coefficient reconstruction",
        )
        for q, row in self.by_q.items():
            measure = row["measure_separation"]
            self.assertFalse(
                measure[
                    "full_signed_tensor_polynomial_descends_to_independent_branch_orbits"
                ]
            )
            self.assertTrue(
                measure["simultaneous_quadratic_twist_leaves_tensor_polynomial_fixed"]
            )
            self.assertGreater(
                Fraction(*measure["genus1_model_vs_uniform_branch_coarse_tv"]), 0
            )
            self.assertGreater(
                Fraction(*measure["genus2_model_vs_uniform_branch_coarse_tv"]), 0
            )
            self.assertLessEqual(
                Fraction(*measure["even_coefficient_product_coarse_tv_upper_bound"]),
                Fraction(1),
            )

            # Simultaneously changing both trace signs fixes the complete
            # tensor polynomial; changing only one flips its odd half.
            witness = row["newton_recurrence_witnesses"][0]
            self.assertEqual(witness["converted_A_E"], -witness["source_trace_t_E"])
            first = witness["input_A_E_a_C_b_C"]
            self.assertEqual(first[0], witness["converted_A_E"])
            a_e, a_c, b_c = first
            original = subject.tensor_coefficients(a_e, a_c, b_c, q)
            simultaneous = subject.tensor_coefficients(-a_e, -a_c, b_c, q)
            single = subject.tensor_coefficients(-a_e, a_c, b_c, q)
            self.assertEqual(original, simultaneous)
            self.assertEqual(original[2], single[2])
            self.assertEqual(original[4], single[4])
            self.assertEqual(original[1], -single[1])
            self.assertEqual(original[3], -single[3])

    def test_fixture_hashes_resource_cap_and_no_enumeration_contract(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        locks = stored["producer_and_source_locks"]["locks"]
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(
                b"\r", b"\n"
            )
            self.assertEqual(
                lock["sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )
        resources = stored["resource_contract"]
        self.assertLess(
            resources["operation_ledger"]["total_exact_operations"],
            resources["hard_exact_operation_cap"],
        )
        self.assertEqual(resources["field_or_curve_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertTrue(stored["producer_and_source_locks"]["no_field_enumeration"])

    def test_refusals(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5))
        for invalid_q in (2, 4, 8, 15):
            with self.subTest(q=invalid_q):
                with self.assertRaises(ValueError):
                    subject.tensor_coefficients(1, 1, 1, invalid_q)
        with self.assertRaisesRegex(ValueError, "orders 0..4"):
            subject.tensor_normalized_trace_moment(5, 5)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.so8_standard_trace_haar_moment(8)
        guard = subject.ResourceGuard(atom_pair_operations=subject.MAX_EXACT_OPERATIONS)
        with self.assertRaisesRegex(RuntimeError, "cap exceeded"):
            guard.charge_atoms()


if __name__ == "__main__":
    unittest.main()
