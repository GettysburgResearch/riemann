from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for name, path in (
    ("search", ROOT / "search.py"),
    ("basis_check", ROOT / "basis_check.py"),
):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)

import search
import basis_check


class SimplicialBasisTests(unittest.TestCase):
    def test_basis_polynomial_identities(self):
        nodes = [Fraction(1), Fraction(2), Fraction(5), Fraction(7)]
        for degree in range(len(nodes) - 1):
            beta = basis_check.basis_vector(nodes, degree)
            self.assertEqual(sum(beta), 0)
            self.assertEqual(
                search.response_polynomial(nodes, beta),
                [Fraction(0)] * degree + [Fraction(1)],
            )

    def test_three_node_basis_values(self):
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        self.assertEqual(
            basis_check.basis_vector(nodes, 0),
            [Fraction(-1, 2), Fraction(1), Fraction(-1, 2)],
        )
        self.assertEqual(
            basis_check.basis_vector(nodes, 1),
            [Fraction(1, 2), Fraction(-2), Fraction(3, 2)],
        )

    def test_subset_embedding_preserves_nonnegative_coefficients(self):
        subset_nodes = [Fraction(1), Fraction(5), Fraction(7)]
        subset_beta = [Fraction(-1, 2), Fraction(1), Fraction(-1, 2)]
        subset_polynomial = search.response_polynomial(subset_nodes, subset_beta)
        full_polynomial = search.polynomial_multiply(
            subset_polynomial, [Fraction(2), Fraction(1)]
        )
        self.assertTrue(all(value >= 0 for value in full_polynomial))


if __name__ == "__main__":
    unittest.main()
