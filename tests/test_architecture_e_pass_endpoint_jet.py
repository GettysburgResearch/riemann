"""Exact and hostile controls for the endpoint four-jet packet."""

import copy
import hashlib
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-five-hour-pass/architecture-e/endpoint_jet_replay.py"
)
SPEC = importlib.util.spec_from_file_location("architecture_e_endpoint_jet", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ExactAlgebraTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exact = M.exact_algebra()

    def test_complete_matrix(self):
        self.assertEqual([len(row) for row in self.exact["jet_matrix"]], [4] * 4)

    def test_all_leading_determinants(self):
        self.assertEqual(len(self.exact["leading_determinants"]), 4)

    def test_reflection_factors(self):
        self.assertEqual(len(self.exact["D4_reflection_factors"]), 2)
        self.assertEqual(len(self.exact["toeplitz_reflection_factors"]), 2)

    def test_wrong_sign_fails(self):
        matrix = M.jet_matrix()
        matrix[1][0] = M.scale(matrix[1][0], -1)
        declared, _, _ = M.declared_factors()
        self.assertNotEqual(M.determinant([row[:2] for row in matrix[:2]]), declared[1])

    def test_permutation_sign(self):
        self.assertEqual(M.permutation_sign((0, 1, 2, 3)), 1)
        self.assertEqual(M.permutation_sign((1, 0, 2, 3)), -1)


class ScoutAndAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = M.build()

    def test_fixed_precision_and_derivatives(self):
        scout = self.record["numerical_scout"]
        self.assertEqual(scout["precision_decimal_digits"], 100)
        self.assertEqual(len(scout["F_derivatives_0_through_7"]), 8)

    def test_four_endpoint_eigenvalues(self):
        values = self.record["numerical_scout"]["orthonormal_eigenvalues"]
        self.assertEqual(len(values), 4)
        self.assertTrue(all(not value.startswith("-") for value in values))

    def test_scope_firewall(self):
        scope = self.record["scope"]
        self.assertFalse(scope["endpoint_signs_interval_certified"])
        self.assertFalse(scope["local_neighborhood"])
        self.assertFalse(scope["continuum_four_node_theorem"])
        self.assertFalse(scope["rh"])

    def test_body_digest(self):
        bad = copy.deepcopy(self.record)
        bad["scope"]["rh"] = True
        with self.assertRaisesRegex(ValueError, "fresh typed"):
            M.accept(bad, self.record)
        body = {
            key: value for key, value in self.record.items() if key != "proof_sha256"
        }
        self.assertEqual(
            hashlib.sha256(M.canonical(body).encode()).hexdigest(),
            self.record["proof_sha256"],
        )

    def test_strict_json(self):
        for raw in ('{"x":1,"x":1}', '{"x":1.0}', '{"x":NaN}'):
            with self.assertRaises(ValueError):
                M.strict_load(raw)

    def test_fixture(self):
        M.accept(M.strict_load(M.ARTIFACT.read_text()), self.record)


if __name__ == "__main__":
    unittest.main()
