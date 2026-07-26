from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9307_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
NEGATIVE = ROOT / "certificates" / "synthetic-negative.json"
POSITIVE = ROOT / "certificates" / "synthetic-positive.json"


class SimplicialPortfolioCheckerTests(unittest.TestCase):
    def load(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_negative_basis_witness(self):
        result = MODULE.verify(self.load(NEGATIVE))
        self.assertEqual(result["verdict"], "SYNTHETIC_NEGATIVE_BASIS_WITNESS")
        self.assertEqual(result["certified_negative_rows"], 1)
        self.assertEqual(result["basis_rows"][0]["status"], "CERTIFIED_NEGATIVE")
        self.assertEqual(result["basis_rows"][1]["status"], "CERTIFIED_NONNEGATIVE")

    def test_positive_entire_cone(self):
        result = MODULE.verify(self.load(POSITIVE))
        self.assertEqual(result["verdict"], "CERTIFIED_NONNEGATIVE_ENTIRE_CONE")
        self.assertEqual(result["certified_negative_rows"], 0)
        self.assertEqual(result["unresolved_rows"], 0)
        self.assertTrue(all(row["status"] == "CERTIFIED_NONNEGATIVE" for row in result["basis_rows"]))

    def test_three_node_basis_vectors(self):
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        self.assertEqual(
            MODULE.basis_vector(nodes, 0),
            [Fraction(-1, 2), Fraction(1), Fraction(-1, 2)],
        )
        self.assertEqual(
            MODULE.basis_vector(nodes, 1),
            [Fraction(1, 2), Fraction(-2), Fraction(3, 2)],
        )

    def test_response_identities(self):
        nodes = [Fraction(1), Fraction(2), Fraction(5), Fraction(7)]
        for degree in range(len(nodes) - 1):
            beta = MODULE.basis_vector(nodes, degree)
            self.assertEqual(sum(beta), 0)
            self.assertEqual(
                MODULE.response_polynomial(nodes, beta),
                [Fraction(0)] * degree + [Fraction(1)],
            )

    def test_repeated_node_rejected(self):
        data = self.load(POSITIVE)
        data["nodes"][1] = data["nodes"][0]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_feature_sha_mutation_rejected(self):
        data = self.load(POSITIVE)
        data["feature_table_sha256"] = "0" * 64
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_rational_rejected(self):
        data = self.load(POSITIVE)
        data["nodes"][0]["numerator"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
