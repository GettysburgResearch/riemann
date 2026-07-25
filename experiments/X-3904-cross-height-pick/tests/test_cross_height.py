import unittest
from fractions import Fraction

from cross_height import (
    Gaussian,
    matched_identities,
    matched_pole_vector,
    pick_contraction_coefficients,
)


class CrossHeightAlgebraTests(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            Gaussian(Fraction(1, 16), Fraction(0)),
            Gaussian(Fraction(1, 8), Fraction(-1, 32)),
            Gaussian(Fraction(1, 4), Fraction(1, 16)),
            Gaussian(Fraction(3, 8), Fraction(-1, 8)),
        ]
        self.d = Fraction(9, 256)
        self.vector = matched_pole_vector(self.nodes, self.d)

    def test_exact_matched_identities(self):
        identities = matched_identities(self.nodes, self.vector, self.d)
        self.assertTrue(all(value == Gaussian(0) for value in identities["moments"]))
        self.assertEqual(identities["alpha"], Gaussian(0))
        self.assertEqual(identities["beta"], Gaussian(-1))
        self.assertEqual(identities["modeled_pair_value"], -2 * self.d)

    def test_direct_pair_quadratic(self):
        def entry(z, w):
            return 2 * (z * w.conjugate() - self.d) / (
                (z * z - self.d) * (w.conjugate() * w.conjugate() - self.d)
            )

        total = Gaussian(0)
        for j, z in enumerate(self.nodes):
            for k, w in enumerate(self.nodes):
                total += self.vector[j].conjugate() * entry(z, w) * self.vector[k]
        self.assertEqual(total, Gaussian(-2 * self.d))

    def test_linear_contraction_matches_matrix(self):
        roots = [
            Gaussian(0, Fraction(-3, 2)),
            Gaussian(0, Fraction(1, 3)),
            Gaussian(0, Fraction(5, 2)),
        ]
        values = [sum((1 / (z - root) for root in roots), Gaussian(0)) for z in self.nodes]
        matrix_total = Gaussian(0)
        for j, z in enumerate(self.nodes):
            for k, w in enumerate(self.nodes):
                kernel = (values[j] + values[k].conjugate()) / (z + w.conjugate())
                matrix_total += self.vector[j].conjugate() * kernel * self.vector[k]
        coefficients = pick_contraction_coefficients(
            [z.real for z in self.nodes],
            [z.imag for z in self.nodes],
            self.vector,
        )
        linear = sum(
            (coefficient * value for coefficient, value in zip(coefficients, values)),
            Gaussian(0),
        ).real
        self.assertEqual(matrix_total.imag, 0)
        self.assertEqual(matrix_total.real, linear)
        self.assertGreater(linear, 0)

    def test_duplicate_nodes_rejected(self):
        with self.assertRaises(ValueError):
            matched_pole_vector([self.nodes[0], self.nodes[0]], self.d)


if __name__ == "__main__":
    unittest.main()
