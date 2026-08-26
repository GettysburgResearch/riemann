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
    / "ffps_boundary_field_primitive_pair_large_sieve_gate.py"
)
SPEC = importlib.util.spec_from_file_location("primitive_pair_large_sieve", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BoundaryFieldPrimitivePairLargeSieveGateTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_beta_exceptional_states(self) -> None:
        self.assertEqual(subject.beta(1), 1)
        self.assertEqual(subject.beta(67), -2)
        self.assertEqual(subject.beta(67**2), 1)
        self.assertEqual(subject.beta(67**3), 0)
        self.assertEqual(subject.CHANNELS, ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2)))

    def test_exact_common_factor_swap(self) -> None:
        height = 1
        while height < subject.TOY_PREFIX:
            with self.subTest(height=height):
                self.assertEqual(
                    subject.direct_shell(subject.TOY_PREFIX, height),
                    subject.formula_shell(subject.TOY_PREFIX, height),
                )
            height *= 2

    def test_exact_dyadic_reconstruction(self) -> None:
        reconstructed: subject.RadicalForm = {}
        height = 1
        while height < subject.TOY_PREFIX:
            reconstructed = subject.add_forms(
                reconstructed, subject.formula_shell(subject.TOY_PREFIX, height)
            )
            height *= 2
        self.assertEqual(reconstructed, subject.direct_off_diagonal(subject.TOY_PREFIX))

    def test_channel_reciprocity(self) -> None:
        for alpha, gamma, sieve, height, upper in subject.RECIPROCITY_ROWS:
            with self.subTest(alpha=alpha, gamma=gamma):
                self.assertEqual(
                    subject.panel_form(alpha, gamma, sieve, height, upper),
                    subject.panel_form(gamma, alpha, sieve, height, upper),
                )

    def test_toy_correlation_and_radical_arithmetic(self) -> None:
        self.assertEqual(subject.toy_correlation(3, 5), Fraction(3, 5))
        self.assertEqual(subject.toy_correlation(5, 3), Fraction(3, 5))
        self.assertEqual(subject.toy_correlation(1, 17), 0)
        self.assertEqual(subject.square_decomposition(67**2 * 30), (67, 30))
        form: subject.RadicalForm = {}
        subject.add_radical_term(form, 12, Fraction(3))
        self.assertEqual(form, {3: Fraction(3, 2)})

    def test_conditional_scope_and_guards(self) -> None:
        result = subject.run(check_sources=False)
        gate = result["conditional_gate"]
        self.assertFalse(gate["estimate_proved"])
        self.assertTrue(gate["conditional_implication_to_rh_proved"])
        self.assertFalse(gate["rh_implies_gate_claimed"])
        self.assertFalse(gate["rh_proved"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        with self.assertRaises(ValueError):
            subject.beta(0)
        with self.assertRaises(ValueError):
            subject.toy_correlation(0, 1)
        with self.assertRaises(ValueError):
            subject.direct_shell(1, 1)
        with self.assertRaises(ValueError):
            subject.panel_form(1, 1, 1, 1, 2)


if __name__ == "__main__":
    unittest.main()
