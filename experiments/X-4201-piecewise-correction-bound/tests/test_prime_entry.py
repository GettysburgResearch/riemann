from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x4201_prime_entry", ROOT / "prime_entry.py")
EVENT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = EVENT
SPEC.loader.exec_module(EVENT)


class PrimeEntryEventTests(unittest.TestCase):
    def setUp(self):
        self.k_cells = 8
        self.eta = Fraction(1, 100)
        self.phase = (Fraction(3, 5), Fraction(-4, 5))
        self.vector = [(Fraction(0), Fraction(0)) for _ in range(self.k_cells)]
        self.vector[0] = (Fraction(1, 2), Fraction(1, 3))
        self.vector[-1] = (Fraction(2, 5), Fraction(-1, 7))

    def test_first_cell_hat(self):
        self.assertEqual(EVENT.first_cell_hat(self.k_cells, self.eta), Fraction(8, 101))

    def test_corner_matrix_matches_fixed_vector_formula(self):
        direct = EVENT.stripped_matrix_quadratic(
            self.k_cells, self.eta, self.phase, self.vector
        )
        formula = EVENT.stripped_rayleigh(
            self.k_cells, self.eta, self.phase, self.vector
        )
        self.assertEqual(direct, formula)

    def test_derivative_limit(self):
        # tau(eta)/eta = K/(1+eta), so the stripped upper-corner
        # coefficient divided by eta tends to K/2.
        for denominator in (10, 100, 1000, 10000):
            eta = Fraction(1, denominator)
            if eta >= Fraction(1, self.k_cells - 1):
                continue
            quotient = EVENT.stripped_operator_norm(
                self.k_cells, eta, self.phase
            ) / eta
            self.assertEqual(quotient, Fraction(self.k_cells, 2) / (1 + eta))
            self.assertLess(quotient, Fraction(self.k_cells, 2))
        self.assertEqual(Fraction(self.k_cells, 2), 4)

    def test_endpoint_neutral_vector_annihilates_event(self):
        vector = list(self.vector)
        vector[0] = (Fraction(0), Fraction(0))
        self.assertEqual(
            EVENT.stripped_rayleigh(self.k_cells, self.eta, self.phase, vector),
            0,
        )
        vector = list(self.vector)
        vector[-1] = (Fraction(0), Fraction(0))
        self.assertEqual(
            EVENT.stripped_rayleigh(self.k_cells, self.eta, self.phase, vector),
            0,
        )

    def test_first_cell_norm_cap_and_boundary_rejection(self):
        norm = EVENT.stripped_operator_norm(self.k_cells, self.eta, self.phase)
        self.assertEqual(norm, Fraction(4, 101))
        self.assertLess(norm, Fraction(1, 2))
        with self.assertRaisesRegex(EVENT.EventError, "first deposition cell"):
            EVENT.first_cell_hat(
                self.k_cells, Fraction(1, self.k_cells - 1)
            )
        with self.assertRaisesRegex(EVENT.EventError, "first deposition cell"):
            EVENT.first_cell_hat(self.k_cells, Fraction(0))

    def test_nonunit_phase_rejected(self):
        with self.assertRaisesRegex(EVENT.EventError, "unit modulus"):
            EVENT.stripped_corner_coefficient(
                self.k_cells, self.eta, (Fraction(1), Fraction(1))
            )


if __name__ == "__main__":
    unittest.main()
