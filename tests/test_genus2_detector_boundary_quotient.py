"""Exact replay tests for the genus-two detector boundary quotient."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_detector_boundary_quotient as subject  # noqa: E402


class Genus2DetectorBoundaryQuotientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_matrix_determinant_and_upstream_specializations(self) -> None:
        matrix = subject.coefficient_matrix()
        self.assertEqual(
            matrix,
            (
                (-1, 0, -1, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 2, 0),
                (-1, -1, 0, -1, 0),
                (0, 0, -1, -2, -3),
            ),
        )
        self.assertEqual(subject._bareiss_determinant(matrix), 3)
        for q in (3, 5, 7, 9, 11, 13):
            expected = subject.upstream.candidate_low_weight_character_means(q)
            actual = {
                label: subject.evaluate_laurent(subject.MEAN_COLUMNS[label], q)
                for label in subject.BASIS
            }
            self.assertEqual(actual, expected)

    def test_inverse_formula_and_index_three_congruence(self) -> None:
        matrix = subject.coefficient_matrix()
        for vector in itertools.product((-1, 0, 1), repeat=5):
            m1, m2, m3, m4, m5 = subject.matrix_vector(matrix, vector)
            recovered = (
                m2,
                -2 * m2 - m3 - 2 * m4,
                -m1 - m2,
                m2 + m3 + m4,
                (m1 - m2 - 2 * m3 - 2 * m4 - m5) // 3,
            )
            self.assertEqual(
                (m1 - m2 - 2 * m3 - 2 * m4 - m5) % 3,
                0,
            )
            self.assertEqual(recovered, vector)

        # The congruence is genuinely restrictive, not an identity on Z^5.
        self.assertNotEqual((0 - 0 - 0 - 0 - 1) % 3, 0)

    def test_saturated_boundary_filtration(self) -> None:
        matrix = subject.coefficient_matrix()
        self.assertEqual(
            [len(subject.FILTRATION_BASES[order]) for order in range(1, 7)],
            [5, 4, 3, 2, 1, 0],
        )
        for order in range(1, 7):
            prefix = matrix[: order - 1]
            self.assertEqual(
                subject.rational_nullspace_basis(prefix),
                subject.FILTRATION_BASES[order],
            )
            for vector in subject.FILTRATION_BASES[order]:
                self.assertTrue(all(value == 0 for value in subject.matrix_vector(prefix, vector)))

    def test_distinguished_detectors_and_minimal_q4_support(self) -> None:
        vectors = {
            "B": (0, 1, -1, 0, 0),
            "D2": (1, 0, -1, 0, 0),
            "D3": (0, 1, 0, 0, 0),
            "D4": (0, -2, 0, 1, 0),
            "D5": (0, 0, 0, 0, 1),
        }
        expected = {
            "B": ((1, 0, 1, -1, 1), 1),
            "D2": ((0, 1, 0, -1, 1), 2),
            "D3": ((0, 0, 1, -1, 0), 3),
            "D4": ((0, 0, 0, 1, -2), 4),
            "D5": ((0, 0, 0, 0, -3), 5),
        }
        for name, vector in vectors.items():
            coefficients = subject.exact_mean_coefficients(vector)
            self.assertEqual(
                (coefficients, subject.leading_power(coefficients)), expected[name]
            )

        # Every exact-order-four vector is t*(-2 chi20 + chi21)+s*chi40.
        # Thus t != 0 forces L1 support at least three.
        for t in (-2, -1, 1, 2):
            for s in range(-2, 3):
                vector = (0, -2 * t, 0, t, s)
                self.assertGreaterEqual(sum(abs(value) for value in vector), 3)
                self.assertEqual(subject.leading_power(subject.exact_mean_coefficients(vector)), 4)

    def test_exact_fraction_evaluation(self) -> None:
        d4 = (0, -2, 0, 1, 0)
        for q in (3, 5, 7, 11):
            self.assertEqual(
                subject.detector_mean(d4, q),
                Fraction(1, q**4) - Fraction(2, q**5),
            )

    def test_fixture_and_locked_json_are_canonical(self) -> None:
        output = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(output, self.fixture)
        self.assertEqual(output["theorems"]["injectivity"]["determinant"], 3)
        self.assertEqual(
            output["theorems"]["cokernel"]["smith_invariants"],
            [1, 1, 1, 1, 3],
        )
        hashes = output["provenance"]["source_hashes_lf_sha256"]
        paths = {
            "producer": Path(subject.__file__),
            "note": subject.NOTE_PATH,
            "test": Path(__file__),
            "upstream_character_means": subject.UPSTREAM_PATH,
            "all_q_moment_proof_note": subject.MOMENT_NOTE_PATH,
            "null_module_note": subject.NULL_MODULE_PATH,
        }
        for label, path in paths.items():
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashes[label], hashlib.sha256(normalized).hexdigest())

    def test_refuses_invalid_domains(self) -> None:
        with self.assertRaises(ValueError):
            subject.evaluate_laurent((1, 2), 3)
        with self.assertRaises(ValueError):
            subject.evaluate_laurent((1, 2, 3, 4, 5), 1)
        with self.assertRaises(ValueError):
            subject.exact_mean_coefficients((1, 2))
        with self.assertRaises(ValueError):
            subject._bareiss_determinant(((1, 2, 3), (4, 5, 6)))


if __name__ == "__main__":
    unittest.main()
