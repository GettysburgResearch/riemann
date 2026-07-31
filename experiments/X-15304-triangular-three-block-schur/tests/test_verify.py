from __future__ import annotations

import copy
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify import CertificateError, load, verify  # noqa: E402


class ThreeBlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = load(ROOT / "certificates" / "synthetic.json")

    def test_synthetic_passes_and_cancellation_is_exact(self):
        result = verify(copy.deepcopy(self.base))
        self.assertTrue(result["verified"])
        self.assertEqual(
            result["corrected_radical_visible_cross"][0][0],
            {"numerator": "0", "denominator": "1"},
        )
        self.assertEqual(
            result["floors_and_losses"]["final_negative_floor"],
            {"numerator": "17", "denominator": "1250"},
        )

    def test_complement_floor_mutation_rejected(self):
        data = copy.deepcopy(self.base)
        data["C"] = [[{"numerator": 9, "denominator": 10}]]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_visible_schur_mutation_rejected(self):
        data = copy.deepcopy(self.base)
        data["B_V"] = [[1]]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_corrected_cross_mutation_rejected(self):
        data = copy.deepcopy(self.base)
        data["X"] = [[1]]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_radical_diagonal_mutation_rejected(self):
        data = copy.deepcopy(self.base)
        data["B_R"] = [[{"numerator": -1, "denominator": 10}]]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_negative_assembly_radius_rejected(self):
        data = copy.deepcopy(self.base)
        data["assembly_radius"] = {"numerator": -1, "denominator": 100}
        with self.assertRaises(CertificateError):
            verify(data)

    def test_boolean_rational_rejected(self):
        data = copy.deepcopy(self.base)
        data["complement_floor"] = True
        with self.assertRaises(CertificateError):
            verify(data)

    def test_dimension_mismatch_rejected(self):
        data = copy.deepcopy(self.base)
        data["Z"] = [[1, 0]]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_nonsymmetric_metric_rejected(self):
        data = copy.deepcopy(self.base)
        data["G_R"] = [[1, 1], [0, 1]]
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
