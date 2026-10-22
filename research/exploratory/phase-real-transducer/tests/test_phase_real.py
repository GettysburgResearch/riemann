from __future__ import annotations

from fractions import Fraction
import math
from pathlib import Path
import sys
import unittest

CODE = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE))

from phase_real import (  # noqa: E402
    Zero,
    depoissonized_response,
    derivative_coefficients,
    phase_fourier_transform,
    petal_participation_lower_bound,
    quartet_derivative_coefficients,
    quartet_energy_closed,
    quartet_pick_two_point_eigenvalues,
    quartet_polynomial_coefficients,
    quartet_response,
    quartet_zeros,
    response_energy_cauchy,
)


class PhaseRealTests(unittest.TestCase):
    def test_petal_participation(self) -> None:
        areas = [1.0, 2.0, 3.0]
        bound = petal_participation_lower_bound(areas)
        self.assertLessEqual(bound, len(areas))
        self.assertAlmostEqual(bound, 36.0 / 14.0)

    def test_quartet_derivative_exact(self) -> None:
        a = Fraction(7, 5)
        b = Fraction(2, 9)
        self.assertEqual(
            derivative_coefficients(quartet_polynomial_coefficients(a, b)),
            quartet_derivative_coefficients(a, b),
        )

    def test_quartet_response(self) -> None:
        a = 1.4
        b = 0.2
        zeros = quartet_zeros(a, b)
        for t in [0.0, 0.3, 1.1, 2.7]:
            self.assertAlmostEqual(
                depoissonized_response(t, zeros).real,
                quartet_response(t, a, b),
                places=12,
            )
            self.assertAlmostEqual(depoissonized_response(t, zeros).imag, 0.0, places=12)

    def test_fourier_semigroup_independence(self) -> None:
        zeros = quartet_zeros(1.1, 0.25)
        t = 0.8
        r1 = math.exp(0.7 * abs(t)) * phase_fourier_transform(t, 0.7, zeros) / math.pi
        r2 = math.exp(1.2 * abs(t)) * phase_fourier_transform(t, 1.2, zeros) / math.pi
        self.assertAlmostEqual(r1.real, r2.real, places=12)
        self.assertAlmostEqual(r1.imag, r2.imag, places=12)

    def test_energy_formulas_agree(self) -> None:
        a = 1.25
        b = 0.3
        sigma = 0.9
        zeros = quartet_zeros(a, b)
        self.assertAlmostEqual(
            response_energy_cauchy(sigma, zeros),
            quartet_energy_closed(sigma, a, b),
            places=11,
        )

    def test_energy_rejects_boundary(self) -> None:
        zeros = (Zero(1.0, 0.4), Zero(1.0, -0.4))
        with self.assertRaises(ValueError):
            response_energy_cauchy(0.4, zeros)

    def test_two_point_off_axis_witness(self) -> None:
        lower, upper = quartet_pick_two_point_eigenvalues(2.0, 0.1)
        self.assertLess(lower, 0.0)
        self.assertGreater(upper, 0.0)


if __name__ == "__main__":
    unittest.main()
