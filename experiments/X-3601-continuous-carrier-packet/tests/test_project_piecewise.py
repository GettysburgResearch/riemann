import unittest
from fractions import Fraction

from project_piecewise import project


def vector(real, imag=None, bits=0):
    if imag is None:
        imag = [0] * len(real)
    return {
        "dyadic_vector": {
            "scale_bits": bits,
            "real_numerators": real,
            "imag_numerators": imag,
        }
    }


def frac(raw):
    return Fraction(raw["numerator"], raw["denominator"])


class PiecewiseProjectionTests(unittest.TestCase):
    def test_constant_vector_is_exact_degree_zero(self):
        result = project(vector([1, 1, 1, 1]), 8)
        self.assertEqual(frac(result["degrees"][0]["captured_energy"]), 1)
        for row in result["degrees"][1:]:
            self.assertEqual(frac(row["mode_energy"]), 0)
            self.assertEqual(frac(row["tail_energy"]), 0)

    def test_scale_invariance(self):
        first = project(vector([1, -2, 3, 4]), 7)
        second = project(vector([8, -16, 24, 32]), 7)
        self.assertEqual(first["degrees"], second["degrees"])

    def test_complex_energy_is_rational_and_monotone(self):
        result = project(vector([1, 2, -1, 3], [2, -1, 4, 0], bits=3), 10)
        previous = Fraction(0)
        for row in result["degrees"]:
            captured = frac(row["captured_energy"])
            tail = frac(row["tail_energy"])
            self.assertGreaterEqual(captured, previous)
            self.assertGreaterEqual(tail, 0)
            self.assertEqual(captured + tail, 1)
            previous = captured

    def test_zero_vector_rejected(self):
        with self.assertRaises(ValueError):
            project(vector([0, 0]), 4)

    def test_bad_degree_rejected(self):
        with self.assertRaises(ValueError):
            project(vector([1]), -1)


if __name__ == "__main__":
    unittest.main()
