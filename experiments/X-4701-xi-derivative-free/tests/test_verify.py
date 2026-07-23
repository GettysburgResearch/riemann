from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x4701_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)
CERTIFICATE = ROOT / "certificates" / "synthetic-offline-value-witnesses.json"


class DerivativeFreeWitnessTests(unittest.TestCase):
    def load(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_committed_certificate(self):
        result = VERIFY.verify_certificate(self.load())
        self.assertEqual(result["scalar_status"], "SYNTHETIC_POSITIVE_VALUES_NEGATIVE_SECANT")
        self.assertEqual(result["divided_status"], "SYNTHETIC_DIVIDED_DIFFERENCE_SIGN_VIOLATION")
        self.assertEqual(result["cross_loewner_status"], "SYNTHETIC_POSITIVE_ENTRIES_NEGATIVE_MINOR")
        self.assertLess(int(result["scalar_secant"]["numerator"]), 0)
        self.assertLess(int(result["cross_loewner_determinant"]["numerator"]), 0)

    def test_mutated_scalar_numerator_rejected(self):
        data = self.load()
        numerator = int(data["negative_secant"]["claimed"]["secant"]["numerator"])
        data["negative_secant"]["claimed"]["secant"]["numerator"] = str(numerator + 1)
        with self.assertRaisesRegex(VERIFY.CertificateError, "scalar secant mismatch"):
            VERIFY.verify_certificate(data)

    def test_mutated_determinant_rejected(self):
        data = self.load()
        numerator = int(data["cross_loewner"]["claimed_determinant"]["numerator"])
        data["cross_loewner"]["claimed_determinant"]["numerator"] = str(numerator - 1)
        with self.assertRaisesRegex(VERIFY.CertificateError, "determinant mismatch"):
            VERIFY.verify_certificate(data)

    def test_value_only_nodes_must_be_disjoint(self):
        data = self.load()
        data["cross_loewner"]["col_x"][0] = copy.deepcopy(data["cross_loewner"]["row_x"][0])
        with self.assertRaisesRegex(VERIFY.CertificateError, "must be disjoint"):
            VERIFY.verify_certificate(data)

    def test_node_order_is_not_silently_repaired(self):
        data = self.load()
        data["cross_loewner"]["row_x"].reverse()
        with self.assertRaisesRegex(VERIFY.CertificateError, "strictly increasing"):
            VERIFY.verify_certificate(data)

    def test_on_line_finite_model_obeys_divided_difference_signs(self):
        zeros = [
            (Fraction(0), Fraction(-4)),
            (Fraction(0), Fraction(-2)),
            (Fraction(0), Fraction(-1)),
            (Fraction(0), Fraction(1)),
            (Fraction(0), Fraction(2)),
            (Fraction(0), Fraction(4)),
        ]
        height = Fraction(1, 2)
        nodes = [Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(4, 5)]
        for order in range(1, 5):
            value = VERIFY.divided_difference(zeros, nodes[: order + 1], height)
            signed = value if order % 2 == 1 else -value
            self.assertGreater(signed, 0)

    def test_on_line_cross_loewner_minors_are_positive(self):
        zeros = [
            (Fraction(0), Fraction(-4)),
            (Fraction(0), Fraction(-2)),
            (Fraction(0), Fraction(-1)),
            (Fraction(0), Fraction(1)),
            (Fraction(0), Fraction(2)),
            (Fraction(0), Fraction(4)),
        ]
        height = Fraction(1, 2)
        rows = [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)]
        cols = [Fraction(1, 4), Fraction(3, 5), Fraction(9, 10)]
        matrix = VERIFY.cross_loewner(zeros, rows, cols, height)
        self.assertTrue(all(value > 0 for row in matrix for value in row))
        self.assertGreater(VERIFY.determinant(matrix), 0)
        for i0 in range(3):
            for i1 in range(i0 + 1, 3):
                for j0 in range(3):
                    for j1 in range(j0 + 1, 3):
                        minor = [
                            [matrix[i0][j0], matrix[i0][j1]],
                            [matrix[i1][j0], matrix[i1][j1]],
                        ]
                        self.assertGreater(VERIFY.determinant(minor), 0)

    def test_positive_entries_do_not_hide_negative_minor(self):
        result = VERIFY.verify_certificate(self.load())
        entries = result["cross_loewner_entries"]
        self.assertTrue(all(int(value["numerator"]) > 0 for row in entries for value in row))
        self.assertLess(int(result["cross_loewner_determinant"]["numerator"]), 0)


if __name__ == "__main__":
    unittest.main()
