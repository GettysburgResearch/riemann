from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_mollified_beta_boundary_shell_identity.py"
)
SPEC = importlib.util.spec_from_file_location("beta_boundary_shell", MODULE_PATH)
assert SPEC and SPEC.loader
beta_boundary_shell = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(beta_boundary_shell)


class FfpsMollifiedBetaBoundaryShellIdentityTest(unittest.TestCase):
    def test_exact_odd_compressed_polynomial(self) -> None:
        self.assertEqual(
            beta_boundary_shell.odd_compressed_polynomial(),
            (
                (Fraction(1), Fraction(0)),
                (Fraction(-2), Fraction(-5, 2)),
                (Fraction(5), Fraction(5)),
                (Fraction(-8), Fraction(-7, 2)),
                (Fraction(4), Fraction(2)),
                (Fraction(0), Fraction(-1)),
            ),
        )

    def test_tail_annihilation_roots(self) -> None:
        polynomial = beta_boundary_shell.odd_compressed_polynomial()
        derivative = beta_boundary_shell.qderivative(polynomial)
        zero = (Fraction(0), Fraction(0))
        one = (Fraction(1), Fraction(0))
        inverse_sqrt_two = (Fraction(0), Fraction(1, 2))
        self.assertEqual(beta_boundary_shell.qeval(polynomial, one), zero)
        self.assertEqual(beta_boundary_shell.qeval(derivative, one), zero)
        self.assertEqual(
            beta_boundary_shell.qeval(polynomial, inverse_sqrt_two), zero
        )
        self.assertEqual(
            beta_boundary_shell.qeval(derivative, inverse_sqrt_two), zero
        )

    def test_complete_beta_two_adic_pairing(self) -> None:
        for odd in (1, 3, 9, 67, 201, 335):
            at_m, at_twice_m, at_four_m = beta_boundary_shell.source_pair(odd)
            self.assertEqual(at_twice_m, -at_m)
            self.assertEqual(at_four_m, 0)
        self.assertEqual(beta_boundary_shell.source_pair(67), (-2, 2, 0))
        with self.assertRaises(ValueError):
            beta_boundary_shell.source_pair(2)

    def test_reflection_primitive_polynomial(self) -> None:
        self.assertEqual(
            beta_boundary_shell.reflection_primitive_coefficients(),
            (Fraction(3, 4), Fraction(1, 4), Fraction(-6), Fraction(5)),
        )

    def test_causal_cell_boundary_and_jordan_identity(self) -> None:
        difference = beta_boundary_shell.cell_difference(
            (Fraction(3), Fraction(-1), Fraction(2))
        )
        self.assertEqual(
            difference,
            (Fraction(3), Fraction(-4), Fraction(3), Fraction(-2)),
        )
        self.assertEqual(sum(difference), 0)
        negative = sum(max(-value, Fraction(0)) for value in difference)
        absolute = sum(abs(value) for value in difference)
        self.assertEqual(absolute, 2 * negative + sum(difference))

    def test_formal_jordan_obstruction(self) -> None:
        sample = beta_boundary_shell.boundary_sample()
        self.assertEqual(sample["signed_mass"], "0")
        self.assertEqual(sample["terminal_boundary_cell"], "0")
        self.assertEqual(sample["negative_mass"], "3")
        self.assertEqual(sample["absolute_mass"], "6")

    def test_scope_boundary(self) -> None:
        result = beta_boundary_shell.run()
        self.assertFalse(result["equivalence"]["primitive_estimate_proved"])
        self.assertFalse(result["equivalence"]["mollified_estimate_proved"])
        self.assertFalse(result["equivalence"]["rh_proved"])
        self.assertFalse(result["equivalence"]["grh_proved"])
        self.assertEqual(result["resource_caps"]["zeros_enumerated"], 0)
        self.assertIn("boundary algebra alone", result["no_go"]["formal_scope"])


if __name__ == "__main__":
    unittest.main()
