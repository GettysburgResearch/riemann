"""Exact replay tests for the genus-two R6 proof reconnaissance."""

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

import genus2_r6_proof_reconnaissance as subject


class Genus2R6ProofReconnaissanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_echo_reduction_and_rank_two_certificate(self) -> None:
        reduction = self.fixture["echo_reduction"]
        self.assertEqual(
            reduction["pointwise_identity"],
            "R6-2*chi_(0,3)=-3*B_1*B_2-2*B_3",
        )
        self.assertEqual(
            reduction["separated_coefficient_matrix"], [[-3, -3], [-3, -1]]
        )
        self.assertEqual(reduction["separated_determinant"], -6)
        self.assertEqual(reduction["exact_separated_tensor_rank"], 2)
        self.assertEqual(
            reduction["torus_support"],
            {
                "R6": 37,
                "chi_(0,3)": 25,
                "R6_minus_2_chi_(0,3)": 16,
                "B_1_B_2": 16,
                "B_3": 4,
            },
        )

    def test_exact_haar_orthogonality_no_go(self) -> None:
        no_go = self.fixture["low_moment_no_go"]
        gram = no_go["haar_gram_matrix"]
        self.assertEqual(len(gram), 8)
        for row in range(8):
            for column in range(8):
                expected = (24 if row == 7 else 1) if row == column else 0
                self.assertEqual(gram[row][column], expected)
        self.assertEqual(no_go["R6_squared_norm"], 24)
        self.assertEqual(no_go["R6_uniform_triangle_bound"], 1620)

    def test_positive_probability_ambiguity(self) -> None:
        dimensions = self.fixture["low_moment_no_go"]["low_character_dimensions"]
        for q in (19, 25, 49, 121):
            budget = subject._weighted_dimension_budget(q, dimensions)
            delta = 1 - budget
            self.assertGreater(delta, 0)
            self.assertEqual(
                Fraction(24, 2 * 1620) * delta,
                delta / 135,
            )
        witness = self.fixture["low_moment_no_go"]["q_19_witness"]
        self.assertEqual(witness["S"], [2469973, 2476099])
        self.assertEqual(witness["delta"], [6126, 2476099])
        self.assertEqual(witness["absolute_R6_mean"], [2042, 111424455])

    def test_shifted_polynomial_is_a_symbolic_not_sampled_proof(self) -> None:
        dimensions = self.fixture["low_moment_no_go"]["low_character_dimensions"]
        self.assertEqual(
            subject._dimension_budget_coefficients(dimensions),
            {1: 19, 2: -5, 3: 80, 4: -40, 5: 49},
        )
        for name, _weight in subject.LOW_WEIGHTS:
            sign_shift = subject._poly_shift(subject._signed_mean_numerator(name), 3)
            self.assertGreater(sign_shift[0], 0)
            self.assertTrue(all(coefficient >= 0 for coefficient in sign_shift))
        shifted = subject._poly_shift((-49, 40, -80, 5, -19, 1), 19)
        self.assertEqual(shifted, (6126, 132736, 27641, 2171, 76, 1))
        self.assertTrue(all(coefficient > 0 for coefficient in shifted))

    def test_no_field_values_and_source_atom_cap(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["observed_R6_values_consumed"], 0)
        self.assertEqual(scope["primitive_family_source_records_consumed"], 0)
        self.assertLessEqual(
            scope["actual_source_atoms"],
            scope["maximum_source_atoms"],
        )
        self.assertEqual(scope["maximum_source_atoms"], 4096)

    def test_fixture_and_source_manifest_are_locked(self) -> None:
        frozen = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.fixture)
        for record in frozen["source_manifest"]:
            path = ROOT / record["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                record["sha256_lf_normalized"], hashlib.sha256(normalized).hexdigest()
            )

        payload_without_hash = dict(frozen)
        stored_hash = payload_without_hash.pop("canonical_payload_sha256")
        self.assertEqual(stored_hash, subject._canonical_sha256(payload_without_hash))

    def test_invalid_domains_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            subject._low_means(2)
        with self.assertRaises(ValueError):
            subject._adams({(0, 0): 1}, 0)


if __name__ == "__main__":
    unittest.main()
