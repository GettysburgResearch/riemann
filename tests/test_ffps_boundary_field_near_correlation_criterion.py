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
    / "ffps_boundary_field_near_correlation_criterion.py"
)
SPEC = importlib.util.spec_from_file_location("boundary_near_correlation", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BoundaryFieldNearCorrelationCriterionTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_beta_square_euler_coefficients(self) -> None:
        for value in range(1, subject.COEFFICIENT_CAP + 1):
            self.assertEqual(
                subject.beta(value) ** 2, subject.beta_square_from_euler(value)
            )
        self.assertEqual(subject.beta_square_local(67, 1), 4)
        self.assertEqual(subject.beta_square_local(67, 2), 1)
        self.assertEqual(subject.beta_square_local(67, 3), 0)

    def test_exceptional_residue_ratio(self) -> None:
        self.assertEqual(subject.exceptional_residue_ratio(), Fraction(2379, 2278))

    def test_exact_finite_gram_identity(self) -> None:
        source = tuple(Fraction(subject.beta(value), value) for value in range(1, 19))
        kernel = (Fraction(3), Fraction(-2), Fraction(1))
        direct = subject.direct_toy_energy(source, kernel)
        gram = subject.gram_toy_energy(source, kernel)
        self.assertEqual(direct, gram)
        self.assertGreaterEqual(gram, 0)

    def test_autocorrelation_is_even_and_compact(self) -> None:
        kernel = (Fraction(1), Fraction(2), Fraction(-1), Fraction(3))
        correlation = subject.autocorrelation(kernel)
        for shift, value in correlation.items():
            self.assertEqual(value, correlation[-shift])
        self.assertEqual(correlation[0], sum(value * value for value in kernel))
        self.assertNotIn(len(kernel), correlation)

    def test_scope_and_guards(self) -> None:
        result = subject.run(check_sources=False)
        self.assertFalse(result["criterion"]["estimate_proved"])
        self.assertFalse(result["criterion"]["rh_proved"])
        self.assertEqual(result["criterion"]["ratio_support"], "1/16 <= m/n <= 16")
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        with self.assertRaises(ValueError):
            subject.beta(0)
        with self.assertRaises(ValueError):
            subject.beta_square_local(67, -1)
        with self.assertRaises(ValueError):
            subject.autocorrelation(())
        with self.assertRaises(ValueError):
            subject.direct_toy_energy((), (Fraction(1),))


if __name__ == "__main__":
    unittest.main()
